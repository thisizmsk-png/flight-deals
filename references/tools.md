# Flight search tools (checked 2026-11-13)

Stars and push dates come from the GitHub API on that date. Re-check before relying on a tool: these break often.

## Use these

| Tool | What it is | Cost | Use it for |
|---|---|---|---|
| **fli** (`pip install flights`), github.com/punitarani/fli | Google Flights CLI + Python + MCP (`fli-mcp`). 3.5k stars, active | Free | Cash fares, cheapest-date sweeps (`fli dates`), nearby-airport fan-out, hidden-city scans (`scripts/fare_scan.py`) |
| **fast-flights**, github.com/AWeirdDev/flights | Google Flights scraper library. 2.1k stars, active | Free | A cron job that polls a route and alerts under a price |
| **seats.aero** (+ official MCP at seats.aero/mcp) | Award availability across ~20+ programs | Free covers 60 days out; Pro ~$110/yr adds full horizon + personal API (1,000 calls/day) | The only award search with an API and MCP. Best buy if you pay for one tool |
| **PointsYeah**, pointsyeah.com | Award search web app; shows each fare's bank transfer path, co-brand card prices, live transfer bonuses | Free (4-day window, 4 alerts); Premium ~$100-120/yr | Points vs cash for one trip. No API, drive it in the browser (URL pattern below) |
| **Kiwi MCP**, mcp.kiwi.com | Virtual interlining (split tickets across airlines that don't partner) | Free, no key | Self-transfer combos |
| **Skiplagged**, skiplagged.com, MCP at mcp.skiplagged.com/mcp (unverified) | Hidden-city fares | Free | Cross-check `fare_scan.py hidden` |
| **ITA Matrix**, matrix.itasoftware.com; CLIs `flight-cli` (ak2k), `itamx` | Fare construction, routing codes | Free | Forcing a specific connection or fare class, then booking it on the airline site |
| **ExpertFlyer** | Seat maps, fare buckets, award and upgrade alerts | $6-13/mo | United/AA saver-space alerts |
| **travel-hacking-toolkit**, github.com/borski/travel-hacking-toolkit | Claude Code plugin bundling the MCPs above + transfer and valuation references. 958 stars, MIT | Free; some parts need paid keys | One-shot install. Audit before installing: third-party code that wants your keys |

## Skip
- Kiwi Tequila API and anything built on it (closed to new users).
- AwardWiz (archived 2024), gavgrego/seats.aero-mcp-server (deprecated).
- Every open-source error-fare scraper found (0-1 stars, abandoned).

## PointsYeah URL pattern (no API, so build the URL)
```
https://www.pointsyeah.com/search?cabins=Economy&cabin=Economy&banks=Amex%2CBilt%2CCapital+One%2CChase%2CCiti%2CWF%2CUS+Bank&airlineProgram=AR%2CAM%2CAC%2CKL%2CAS%2CAA%2CAV%2CDL%2CET%2CB6%2CLH%2CQF%2CSK%2CTK%2CUA%2CVS%2CVA&tripType=1&adults=1&children=0&departure=SEA&arrival=JFK&departDate=2027-01-15&departDateSec=2027-01-15&multiday=false
```
Needs a logged-in browser. Each result card shows: points per program, taxes, which banks transfer there, "Co-Brand Card Pricing" (e.g. United 13.5k with a United Chase card vs 42k without), and active transfer bonuses. Read with page text, sort by points, then price each option with `points_vs_cash.py`.

## Airline site URL patterns that work
- United awards: `https://www.united.com/en/us/fsr/choose-flights?tt=1&at=1&f=SEA&t=JFK&d=2027-01-15&tqp=A&sc=7&px=1` (`at=1` = miles). Logged in shows co-brand prices.
- Frontier: `https://booking.flyfrontier.com/Flight/InternalSelect?o1=SEA&d1=DEN&dd1=Jan%2015,%202027&ADT=1&mon=true` then click the GoWild! toggle. GoWild prices only show inside the booking window.
- Southwest: `https://www.southwest.com/air/booking/select.html?originationAirportCode=DEN&destinationAirportCode=SEA&departureDate=2027-01-15&tripType=oneway&adultPassengersCount=1&fareType=USD&passengerType=ADULT&reset=true` (results render late; screenshot if text extraction fails).
- American (aa.com) ignores URL params; fill the form.

## Terms-of-service note
Google/ITA/Skiplagged scrapers break those sites' terms. Keep it personal and low-volume. Google returns HTTP 429 after ~20-40 fast calls, and a throttled IP can stay blocked 30-60 min (seen 2026-11-13: worked, then 429 on every call minutes later). `fare_scan.py` exits after 2 searches in a row stay throttled, so keep scans small: a few airports and dates, not a full grid.
