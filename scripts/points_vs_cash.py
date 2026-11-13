#!/usr/bin/env python3
"""Rank flight options by true cost, mixing cash and points fairly.

Every option is converted to one number: effective cost in dollars
  = cash paid + taxes + (points used x value of one point) - rewards you earn on cash
and gets a cents-per-point (cpp) verdict when it uses points.

Usage:
  points_vs_cash.py options.json            # rank a list of options
  points_vs_cash.py --cash 352 --points 17500 --taxes 25.6 --currency bilt
  points_vs_cash.py --show-values           # print the point valuations in use

options.json is a list of objects:
  {"name": "AA 1-stop (Atmos award)", "cash": 0, "points": 17500, "taxes": 25.6,
   "currency": "bilt", "compare_cash": 352, "minutes": 476, "stops": 1, "risk": "low"}
  {"name": "AA 1-stop (cash)", "cash": 352, "minutes": 476, "stops": 1}
Fields: cash (dollars paid), points, taxes (award fees), currency (key in VALUES),
compare_cash (cash price of the same flight, for cpp), minutes, stops,
risk (low/medium/high, a label only), earn_rate (points earned per dollar on a cash
ticket, default 0), earn_currency (currency of those earned points),
hour_value (dollars per hour of your time, default 0 = ignore travel time).
"""
import argparse, json, sys

# Cents per point. "floor" = what you can always get (cash-out / portal), so never
# redeem below it. "value" = median of published valuations, what a point is worth
# to you when you spend it well. Update these from references/valuations.md.
# Values as of 2026-11-13. Transferables use OMAAT's 1.7c (the most conservative of
# TPG/UpgradedPoints/OMAAT; their median is 2.0c, which assumes premium-cabin use).
# Airline values are the median of TPG/UP/OMAAT/Frequent Miler. See valuations.md.
VALUES = {
    # transferable bank currencies (floor = cash-out / base portal rate)
    "chase":     {"floor": 1.0,  "value": 1.7},
    "bilt":      {"floor": 1.0,  "value": 1.7},
    "amex":      {"floor": 1.0,  "value": 1.7},
    "capone":    {"floor": 1.0,  "value": 1.7},
    "citi":      {"floor": 1.0,  "value": 1.7},
    # airline currencies (no cash-out floor)
    "united":    {"floor": 0.0,  "value": 1.25},
    "southwest": {"floor": 0.0,  "value": 1.25},
    "atmos":     {"floor": 0.0,  "value": 1.55},
    "aa":        {"floor": 0.0,  "value": 1.45},
    "delta":     {"floor": 0.0,  "value": 1.15},
    "aeroplan":  {"floor": 0.0,  "value": 1.45},
    "virgin":    {"floor": 0.0,  "value": 1.4},
    "flyingblue":{"floor": 0.0,  "value": 1.3},
    "lifemiles": {"floor": 0.0,  "value": 1.4},
    "frontier":  {"floor": 0.0,  "value": 1.2},
}

def evaluate(o):
    cur = o.get("currency")
    pts = float(o.get("points", 0) or 0)
    taxes = float(o.get("taxes", 0) or 0)
    cash = float(o.get("cash", 0) or 0)
    v = VALUES.get(cur, {"floor": 0.0, "value": 1.0}) if cur else None
    earned = float(o.get("earn_rate", 0) or 0) * cash
    earn_v = VALUES.get(o.get("earn_currency", ""), {"value": 1.0})["value"]
    hours = float(o.get("minutes", 0) or 0) / 60
    eff = cash + taxes + (pts * v["value"] / 100 if v else 0) - earned * earn_v / 100 \
          + hours * float(o.get("hour_value", 0) or 0)
    r = {"name": o.get("name", "?"), "effective_cost": round(eff, 2),
         "out_of_pocket": round(cash + taxes, 2), "points": int(pts),
         "stops": o.get("stops", ""), "hours": round(hours, 1) if hours else "",
         "risk": o.get("risk", "")}
    if pts and o.get("compare_cash") is not None:
        cpp = (float(o["compare_cash"]) - taxes) / pts * 100
        r["cpp"] = round(cpp, 2)
        if cpp < v["floor"]:
            r["verdict"] = "NO - below floor, cash out instead"
        elif cpp < v["value"]:
            r["verdict"] = "WEAK - pay cash, save points"
        elif cpp < v["value"] * 1.3:
            r["verdict"] = "OK - fair use of points"
        else:
            r["verdict"] = "GREAT - use points"
    return r

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file", nargs="?")
    ap.add_argument("--cash", type=float, help="cash price of the same flight")
    ap.add_argument("--points", type=float)
    ap.add_argument("--taxes", type=float, default=0)
    ap.add_argument("--currency", default="chase")
    ap.add_argument("--show-values", action="store_true")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    if a.show_values:
        for k, v in VALUES.items():
            print(f"{k:11} floor {v['floor']:.2f}c  value {v['value']:.2f}c")
        return
    if a.file:
        opts = json.load(open(a.file))
    elif a.points and a.cash is not None:
        opts = [{"name": "points", "points": a.points, "taxes": a.taxes,
                 "currency": a.currency, "compare_cash": a.cash},
                {"name": "cash", "cash": a.cash}]
    else:
        ap.print_help(); sys.exit(1)
    rows = sorted((evaluate(o) for o in opts), key=lambda r: r["effective_cost"])
    if a.json:
        print(json.dumps(rows, indent=2)); return
    print(f"{'#':>2}  {'option':40} {'eff $':>8} {'pocket $':>9} {'points':>7} {'cpp':>5}  verdict")
    for i, r in enumerate(rows, 1):
        print(f"{i:>2}  {r['name'][:40]:40} {r['effective_cost']:>8.2f} {r['out_of_pocket']:>9.2f} "
              f"{r['points'] or '':>7} {r.get('cpp', ''):>5}  {r.get('verdict', '')}")

if __name__ == "__main__":
    main()
