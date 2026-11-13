# Point valuations and the points-vs-cash rules (as of 2026-11-13)

## Published cents per point
Sources: The Points Guy (Nov 2, 2026), Upgraded Points (Nov 13, 2026), One Mile at a Time (Nov 2026, page date uncertain), Frequent Miler RRV (snippets only, conservative "reasonable" value).

| Program | TPG | UP | OMAAT | FM | Median | Used in script |
|---|---|---|---|---|---|---|
| Chase UR | 2.05 | 2.0 | 1.7 | n/a | 2.0 | 1.7 |
| Bilt | 2.2 | 2.0 | 1.7 | n/a | 2.0 | 1.7 |
| Amex MR | 2.0 | 2.2 | 1.7 | n/a | 2.0 | 1.7 |
| Capital One | 1.85 | 1.8 | 1.7 | n/a | 1.8 | 1.7 |
| Citi ThankYou | 1.95 | 1.6 | 1.7 | n/a | 1.7 | 1.7 |
| United | 1.2 | 1.2 | 1.3 | 1.3 | 1.25 | 1.25 |
| Southwest | 1.25 | 1.3 | 1.2 | n/a | 1.25 | 1.25 |
| Alaska Atmos | 1.6 | 1.6 | 1.5 | 1.5 | 1.55 | 1.55 |
| American | 1.45 | 1.4 | 1.5 | n/a | 1.45 | 1.45 |
| Delta | 1.2 | 1.2 | 1.1 | 1.1 | 1.15 | 1.15 |
| Aeroplan | 1.45 | 1.5 | 1.4 | n/a | 1.45 | 1.45 |
| LifeMiles | 1.65 | 1.4 | 1.3 | n/a | 1.4 | 1.4 |
| Flying Blue | 1.45 | 1.3 | 1.3 | n/a | 1.3 | 1.3 |
| Frontier | 1.3 | 1.1 | n/a | n/a | 1.2 | 1.2 |

Why the script uses 1.7c, not 2.0c, for bank points: the 2c medians assume long-haul premium cabins. For someone who mostly flies domestic economy, 1.7c is the realistic bar. If you're saving for business class, raise it to 2.0 in `VALUES`.

**Floors (what you can always get):** Chase 1.0c cash/portal base (Points Boost up to 1.5c Preferred / 2.0c Reserve on select bookings only; points earned before Oct 26, 2025 may keep the old fixed rate until ~Oct 2027, unverified). Bilt ~1.0-1.25c portal (Bilt 2.0, check app). Amex 1.0c (Fanatics, new Nov 2026). Capital One 1.0c. Never redeem below the floor.

## Formula
```
cpp = (cash price of the SAME flight − award taxes/fees) ÷ points × 100
```
Honest adjustments (subtract from the cash side before dividing):
- miles/status the cash ticket would have earned (e.g. 5 miles/$ × airline value),
- card rewards on the cash purchase (e.g. 3x Chase × 1.7c ≈ 5% back),
- flexibility: US-carrier awards usually cancel free with points back; basic-economy cash does not. Put a dollar value on whichever side is more flexible.

## Decision rules
1. Use points only if cpp ≥ the currency's value; ≥1.3× value is a great redemption. Below value, pay cash and keep the points. Below the floor, never.
2. Domestic economy under ~$150 cash almost never clears the bar: pay cash.
3. Compare cash vs portal (Points Boost) vs transfer for the same seat every time.
4. Transfer only after confirming award space at the airline (PointsYeah/seats.aero can show cached or phantom space). Transfers are irreversible.
5. Don't transfer speculatively to chase a bonus; bonuses only help a redemption you already planned.
6. Earn and burn: points devalue (Hyatt went 4:3 on Chase Preferred Oct 2026; Bilt→Hyatt reportedly 4:3 from Jan 2027).

## Transfer partners and times (AwardWallet, Nov 12, 2026)
- **Chase UR, 1:1:** United (instant), Southwest (instant), Virgin Atlantic (instant), Flying Blue (instant), BA/Iberia/Aer Lingus (instant; +30% to Dec 1, 2026), Aeroplan (~47 min), JetBlue, Singapore (~1 day). Hyatt 1:1 on Reserve, 4:3 on Preferred since Oct 1, 2026. Chase allows up to 7 business days.
- **Bilt, 1:1 (min 2,000):** United, Alaska Atmos (~9h), Southwest (up to 72h), Virgin Atlantic (~15h), Aeroplan, Flying Blue, LifeMiles, BA, Iberia, Aer Lingus, Cathay, Emirates, Etihad, JAL, JetBlue, Qatar, TAP, Turkish (~6 days). Rent Day bonuses on the 1st of each month.
- Live Nov 2026 bonuses elsewhere: Capital One→Virgin +30% (Nov 20), →Flying Blue +20% (Nov 30); Citi→Turkish +40% (Nov 30); Amex→Virgin +30%.

## PointsYeah facts
Free: 4-day window, 1 origin/1 destination, 4 flight alerts. Premium $11.99/mo or $99.99/yr (Black Friday discounts common). No public API. Explorer and alerts use cached data; live search is fresher. Delta is pricing only. Shows co-brand card prices and bank logos per fare.
