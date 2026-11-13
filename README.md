<div align="center">

# ✈️ flight-deals

### Points or cash? Find the flight with the best return, and prove it with numbers.

Most "cheap flight" advice stops at the sticker price. But a $340 ticket and a 15,000-point award are not comparable until you put them on one scale, and the cheapest option is often hiding somewhere you didn't search: a partner program, a hidden-city ticket, a co-brand card price, a separate GoWild booking through a hub. **flight-deals sweeps cash fares and award space, converts every option to one effective cost, scores each award in cents per point against what your points are actually worth, and red-teams the winner** before you spend a dollar or a point.

A skill for [Claude Code](https://docs.claude.com/en/docs/claude-code).

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/for-Claude%20Code-d97757)](https://docs.claude.com/en/docs/claude-code)
[![Never books for you](https://img.shields.io/badge/never-books%20for%20you-2b6cb0)](#safety)

</div>

---

## Install

```bash
git clone https://github.com/thisizmsk-png/flight-deals.git ~/.claude/skills/flight-deals
cp ~/.claude/skills/flight-deals/wallet.example.md ~/.claude/skills/flight-deals/wallet.md   # then list your cards
```

For the cash-fare scanner (optional, uses Google Flights data through [fli](https://github.com/punitarani/fli)):

```bash
python3 -m venv ~/.venvs/fli && ~/.venvs/fli/bin/pip install flights
```

Then in a Claude Code session, just ask, or call it directly:

```
/flight-deals one-way from Boston or Providence to Seattle, Jan 15-16, carry-on only, no weekday daytime flights
```

---

## What it does (the method)

1. **Pin the constraints.** Which airports you'll accept and how far you'll drive, date window and blackout times, bags, stops, what's already booked. Every option gets checked against these before you see it.
2. **Cash sweep.** Nearby-airport and flexible-date fan-out, a hidden-city scan (tickets to cities past your destination whose first leg lands where you want to be), and the low-cost carriers Google misses. For Frontier GoWild holders: separate nonstop bookings through a hub, because each extra segment adds fees.
3. **Award sweep.** PointsYeah and the airline sites in your logged-in browser, so it sees real Saver space and co-brand card prices. Then the cross-program routes that often win: Delta flights through Virgin Atlantic, American flights through Alaska Atmos, United flights through LifeMiles or Turkish.
4. **One scale.** `effective cost = cash + taxes + points x value of a point - rewards earned on cash`. Every award also gets `cpp = (cash price of the same flight - taxes) / points` and a verdict against that currency's floor and value.
5. **Red-team the top three.** Fits every constraint? Price verified on the airline site? What breaks it (sold out, rate-limit artifact, bag fees, missed self-transfer, hidden-city reroute, blackout)? What's the fallback?
6. **Present.** A ranked table and one plain recommendation with exact steps: transfer X points from card Y to program Z, book on site W, before date D.

See [`SKILL.md`](SKILL.md) for the full playbook.

---

## What you get out

A real run (one-way domestic, prices verified on airline sites where marked in the session):

```
 #  option                                      eff $  pocket $  points   cpp  verdict
 1  Frontier GoWild, two nonstops + hotel      147.00    147.00
 2  United Saver 2 stops, United award         260.60      5.60   15000  2.23  GREAT - use points
 3  Delta nonstop, hidden-city cash            310.00    310.00
 4  AA 1-stop evening, Alaska Atmos award      323.10     25.60   17500  1.87  OK - fair use of points
 5  AA 1-stop evening, cash                    352.00    352.00
 6  Delta nonstop, Virgin Atlantic award       379.60      5.60   22000  1.38  WEAK - pay cash, save points
 7  Nonstop from a farther airport, cash       527.00    527.00
```

The cheapest line is not automatically the answer: #1 needed a sold-out leg to open up, and #2 was a 14-hour weekday itinerary. The pick was #4, a flight that fit the schedule for 17,500 points and $25.60 instead of $352. Try it yourself: `python3 scripts/points_vs_cash.py examples/options.json`.

---

## What's inside

| File | What it is |
|---|---|
| [`SKILL.md`](SKILL.md) | The six-phase playbook Claude follows |
| [`scripts/points_vs_cash.py`](scripts/points_vs_cash.py) | Ranks options by effective cost, scores awards in cpp, gives a verdict. Point values in one dated table |
| [`scripts/fare_scan.py`](scripts/fare_scan.py) | Google Flights fan-out (airports x dates) and hidden-city scan |
| [`references/techniques.md`](references/techniques.md) | 20 money-saving techniques ranked by savings vs risk, with the 2025-2026 rule changes (Southwest Companion Pass ending, United cardmember pricing, Chase Points Boost, GoWild windows) |
| [`references/valuations.md`](references/valuations.md) | Cents-per-point valuations from four sources, the formula, decision rules, transfer partners and times |
| [`references/tools.md`](references/tools.md) | Which tools are alive in 2026 (fli, seats.aero, PointsYeah, Kiwi, Skiplagged, ITA) and which are dead, plus working search URL patterns |
| [`wallet.example.md`](wallet.example.md) | Template for your cards and loyalty accounts (your filled-in `wallet.md` is gitignored) |

---

## Why it is different

- **It compares like with like.** An award is scored against the cash price of that same flight, not against a cheaper but worse one.
- **It values points honestly.** Transferable points are priced at 1.7 cents by default, not the 2+ cents premium-cabin valuations that make every economy redemption look good.
- **It looks where the deals actually hide.** Partner programs, co-brand prices, hub-split GoWild bookings, hidden-city tickets.
- **It labels every price by source.** "Verified on the airline site" vs "Google Flights data". Scraped prices are a lead, not a quote.
- **It dates its facts.** Award rules changed a lot in 2025-2026; every reference file says when it was checked.

## Safety

It never books, pays, enters passwords, or transfers points. Transfers are irreversible, so it tells you to confirm award space right before you move points. Hidden-city and self-transfer tickets are flagged with their real risks. Scrapers are for personal, low-volume use.

---

## License

MIT. See [LICENSE](LICENSE). Fly more, pay less.
