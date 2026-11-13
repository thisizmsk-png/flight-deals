---
name: flight-deals
description: Find the best-value flight (cash, points, or a mix) and prove it with numbers. Use for "find me the cheapest flight", "points or cash?", "is this award worth it", "cheapest way to get from X to Y", hidden-city / split-ticket / GoWild / positioning hacks, cents-per-point math, PointsYeah or seats.aero searches, and which card or transfer to use. Ranks every option by effective cost, flags risk, never books or transfers without an explicit yes.
user-invocable: true
---

# flight-deals

Goal: the flight with the best return on money AND points, not just the lowest sticker price. Every option, cash or award, gets converted to one number (effective cost) so they can be ranked side by side.

Hard rules:
- **Never book, pay, or transfer points.** The user does it. Transfers are irreversible: tell them to confirm award space right before transferring.
- **Never enter passwords or payment details.** If a site asks to sign in, ask the user to sign in in their browser.
- **Label every price by source**: "verified on <airline>.com" vs "Google Flights data, unverified". Re-verify the winner on the airline site before recommending.
- Read `wallet.md` first: it says which cards and transfer paths the user actually has. If it doesn't exist, copy `wallet.example.md` to `wallet.md`, ask the user for their cards and loyalty accounts, and fill it in. `wallet.md` is gitignored: never commit or publish it.

## Phase 1: Pin the constraints (2 minutes, saves hours)
Ask or infer: origin/destination flexibility (which airports are acceptable, drive time they'll accept, rental car already?), date window and blackout times (e.g. "no weekday daytime"), bags (carry-on only unlocks hidden-city and GoWild), stops/overnight tolerance, travel companions, and which way is fixed (outbound already booked?). Write them down; re-check every option against them before presenting.

## Phase 2: Cash sweep (wide, cheap, fast)
1. `scripts/fare_scan.py direct --from A,B,C --to X,Y --dates d1,d2`: nearby-airport and date fan-out on Google Flights data. Add `--nonstop` for a nonstop-only pass. Google rate-limits after ~20-40 calls (empty results = throttled): wait, or check google.com/travel/flights by hand.
2. Hidden-city: `scripts/fare_scan.py hidden --from A --to X --dates d` lists tickets to cities beyond X whose first leg lands at X. Only for one-way, carry-on trips. Cross-check on skiplagged.com.
3. Low-cost carriers Google may miss or misprice: Southwest, Frontier, Spirit, Allegiant: check their sites (URL patterns in `references/tools.md`).
4. Frontier GoWild (if the user has the pass): it only prices one segment cheaply, so plan **separate nonstop bookings through a Frontier hub** (DEN, LAS, MCO, ATL...). Domestic GoWild opens the day before departure; a sold-out cash flight has no GoWild seats; always pair with a cancellable fallback.

## Phase 3: Award sweep
1. **PointsYeah** in the logged-in browser (URL template in `references/tools.md`). Each card shows points per program, taxes, which banks transfer there, co-brand-card pricing, and live transfer bonuses. Extract with page text, keep only programs reachable from `wallet.md`.
2. **Airline sites logged in** for the programs that matter (United `at=1` URL, etc.). Logged-in pages show cardmember discounts and real Saver space.
3. Cross-program checks that often win: Delta flights via **Virgin Atlantic**, American flights via **Alaska Atmos** (4,500 pts for partner flights under 700 mi), United flights via **LifeMiles/Turkish/Aeroplan**, transatlantic via **Flying Blue Promo Rewards**.
4. seats.aero (free 60-day window, Pro has an API/MCP) when PointsYeah is thin.

## Phase 4: Price everything on one scale
Build a JSON list of options and run `scripts/points_vs_cash.py options.json`:
- `effective cost = cash + taxes + points × value-of-point − rewards earned on cash`
- `cpp = (cash price of the same flight − award taxes) ÷ points × 100`
- Verdict per award: below the currency's floor → never; below its value → pay cash; ≥ value → use points; ≥ 1.3× value → great.
- Point values live in the script's `VALUES` table (medians from `references/valuations.md`). Update them when valuations move.
- Optional `hour_value` per option to charge for long itineraries (e.g. $20/h) so a 14-hour Saver doesn't win on paper only.

Compare the award against the cash price **of that same flight** (or the cheapest equivalent), not against a cheaper but worse flight.

## Phase 5: Red-team before presenting
For the top 3: Does it fit every constraint from Phase 1? Is the price verified on the airline site? What breaks it (sold out, rate-limit artifact, basic-economy bag fees, self-transfer missed connection, hidden-city reroute, GoWild blackout)? What's the fallback? Is there a cheaper path via a transfer bonus that expires soon?

## Phase 6: Present
A ranked table: option, effective $, out-of-pocket $, points (program + which card to transfer from), cpp + verdict, stops/duration, risk, source (verified/unverified). Then one recommendation in plain words, the fallback, and the exact steps the user takes (transfer X points from Y to Z, book on site W, before date D). Name what you did not verify.

## References
- `references/techniques.md`: every money-saving technique ranked by savings vs risk, with 2025-2026 rule changes.
- `references/tools.md`: tools (fli, seats.aero, PointsYeah, Kiwi, Skiplagged, ITA), install commands, URL patterns.
- `references/valuations.md`: cents-per-point valuations and the decision rules.
- `wallet.md`: the user's cards and loyalty accounts (personal; never publish).
