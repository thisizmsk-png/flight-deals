#!/usr/bin/env python3
"""Cash fare scanner on Google Flights data (via the `fli` library).

Two modes:
  direct  - cheapest fares from every origin to every destination on every date
            (nearby-airport fan-out and flexible dates in one table)
  hidden  - hidden-city scan: fares to cities BEYOND your destination whose
            first flight lands at your destination. You fly the first leg only.

Setup (once):
  python3 -m venv ~/.venvs/fli && ~/.venvs/fli/bin/pip install flights
  (if `fli dates` errors on plotext: pip install plotext==5.2.8)

Examples:
  fare_scan.py direct --from SEA,PDX --to JFK,EWR,LGA --dates 2027-01-15,2027-01-16
  fare_scan.py direct --from SEA --to BOS --dates 2027-01-15 --nonstop
  fare_scan.py hidden --from JFK,BOS --to SEA --dates 2027-01-20

Google rate-limits fast loops (HTTP 429). The script sleeps between calls and
backs off on 429; if it still fails, wait ~10 minutes. Prices are Google's
snapshot: always re-check on the airline site before booking.
"""
import argparse, sys, time

try:
    from fli.models import (Airport, FlightSearchFilters, FlightSegment, PassengerInfo,
                            SeatType, MaxStops, SortBy, TripType)
    from fli.search import SearchFlights
except ImportError:
    sys.exit("fli not installed: python3 -m venv ~/.venvs/fli && ~/.venvs/fli/bin/pip install flights")

# Cities to try past a destination for hidden-city. Pick ones the destination is a
# hub or common connection for. Override with --beyond.
BEYOND = {
    "SEA": "ANC,FAI,JNU,KTN,SIT,GEG,PSC,BLI,BOI,PDX,YVR,YLW,MSO,BZN",
    "DEN": "ASE,EGE,GJT,HDN,MTJ,JAC,BZN,BIL,BOI,SLC,COS,DRO",
    "ORD": "MKE,MSN,GRB,CID,DSM,OMA,FSD,TVC,GRR,SBN",
    "ATL": "SAV,CHS,MYR,TLH,PNS,MOB,GSP,AVL,CHA,TYS",
    "DFW": "AUS,SAT,ELP,LBB,AMA,MAF,OKC,TUL,LIT",
    "CLT": "AVL,GSP,CHS,MYR,ILM,OAJ,TRI,CAE",
    "LAX": "SBA,SAN,PSP,SMF,SJC,OAK,FAT,LAS,PHX",
    "SFO": "SMF,RNO,MRY,EUG,MFR,ACV,FAT",
}
DEFAULT_BEYOND = "LAX,SFO,LAS,PHX,DEN,DFW,ORD,ATL,MIA,BOS,JFK,MSP,DTW,SLC,PDX,ANC"

def search(s, o, d, date, nonstop=False, tries=3):
    f = FlightSearchFilters(
        trip_type=TripType.ONE_WAY, passenger_info=PassengerInfo(adults=1),
        flight_segments=[FlightSegment(departure_airport=[[Airport[o], 0]],
                                       arrival_airport=[[Airport[d], 0]], travel_date=date)],
        stops=MaxStops.NON_STOP if nonstop else MaxStops.ANY,
        seat_type=SeatType.ECONOMY, sort_by=SortBy.CHEAPEST)
    for i in range(tries):
        try:
            return s.search(f) or []
        except Exception as e:
            if "429" in str(e) and i < tries - 1:
                time.sleep(30 * (i + 1)); continue
            print(f"  ! {o}-{d} {date}: {str(e)[:70]}", file=sys.stderr)
            return []

def fmt(fl):
    legs = fl.legs
    path = legs[0].departure_airport.name + "".join("-" + l.arrival_airport.name for l in legs)
    al = ",".join(sorted({f"{l.airline.name}" for l in legs}))
    t0 = legs[0].departure_datetime.strftime("%H:%M")
    t1 = legs[-1].arrival_datetime.strftime("%H:%M")
    return path, al, t0, t1, f"{fl.duration // 60}h{fl.duration % 60:02d}"

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("mode", choices=["direct", "hidden"])
    ap.add_argument("--from", dest="orig", required=True, help="comma list of IATA codes")
    ap.add_argument("--to", dest="dest", required=True, help="comma list (direct) or one code (hidden)")
    ap.add_argument("--dates", required=True, help="comma list YYYY-MM-DD")
    ap.add_argument("--beyond", help="hidden mode: comma list of cities past the destination")
    ap.add_argument("--nonstop", action="store_true")
    ap.add_argument("--top", type=int, default=5)
    ap.add_argument("--sleep", type=float, default=2.0)
    a = ap.parse_args()
    s = SearchFlights()
    origs, dates = a.orig.split(","), a.dates.split(",")
    rows = []
    if a.mode == "direct":
        for o in origs:
            for d in a.dest.split(","):
                for dt in dates:
                    for x in search(s, o, d, dt, a.nonstop)[: a.top]:
                        fl = x[0] if isinstance(x, tuple) else x
                        rows.append((fl.price, dt, *fmt(fl)))
                    time.sleep(a.sleep)
    else:
        hub = a.dest
        beyond = (a.beyond or BEYOND.get(hub, DEFAULT_BEYOND)).split(",")
        for o in origs:
            for dt in dates:
                for b in beyond:
                    if b in (o, hub) or b not in Airport.__members__:
                        continue
                    for x in search(s, o, b, dt)[:20]:
                        fl = x[0] if isinstance(x, tuple) else x
                        if len(fl.legs) >= 2 and fl.legs[0].arrival_airport.name == hub:
                            l0 = fl.legs[0]
                            rows.append((fl.price, dt, f"{o}-{hub} (ticket to {b})",
                                         f"{l0.airline.name}{l0.flight_number}",
                                         l0.departure_datetime.strftime("%H:%M"),
                                         l0.arrival_datetime.strftime("%H:%M"), "first leg"))
                            break
                    time.sleep(a.sleep)
    if not rows:
        sys.exit("No results. Google often returns empty (not an error) when it is rate-limiting: "
                 "wait 10-30 minutes and retry, or check the route on google.com/travel/flights.")
    rows.sort(key=lambda r: r[0])
    print(f"{'$':>6}  {'date':10}  {'route':28} {'airline':14} {'dep':5} {'arr':5} dur")
    for r in rows:
        print(f"{r[0]:>6.0f}  {r[1]:10}  {r[2][:28]:28} {r[3][:14]:14} {r[4]:5} {r[5]:5} {r[6]}")
    if a.mode == "hidden" and rows:
        print("\nHidden-city rules: one-way only, carry-on only (board early so it is not "
              "gate-checked), no frequent-flyer number, a rebooking can route you elsewhere.")

if __name__ == "__main__":
    main()
