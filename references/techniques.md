# Techniques to pay less (researched 2026-11-13)

Ordered by savings per unit of risk. [CHG] = changed in 2025-2026. [UNV] = secondary sources only. Re-verify anything dated before you lean on it.

## Tier 1: always do these (near-zero risk)

1. **24-hour rule as a free price lock.** Book direct with a US airline ≥7 days out → free cancel within 24h (DOT 14 CFR 259.5(b)(4)). Book the good fare now, keep hunting for 24h, rebook if cheaper. OTAs are not covered.
2. **Reprice after booking.** Delta/United/American main cabin: no change fees, change to the same flight at the lower fare, keep the difference as credit. Southwest: no cancel fees; Basic fares can only cancel (credit expires 6 months from the original booking), Choice+ can be repriced; **points bookings refund the drop as points that never expire**. [CHG] Alaska dropped its price guarantee in 2025: cancel and rebook yourself (Main/Premium); Saver is locked after 24h. Track your exact flight in Google Flights. Typical: $30-150.
3. **One-ways.** US domestic is priced per direction, so two one-ways usually equal a round trip and let you mix airlines. International round trips are often cheaper: price both.
4. **Fan out airports and dates.** All airports within 2-3h drive each end, ±2-3 days. 10-40% typical. Timing data is weak: book domestic ~1-3 months out (Google 2026: ~39 days avg), international 2-6 months. Tue/Wed flights tend cheapest. Flexibility on travel day beats choosing a booking day.
5. **Deal alerts.** Going (free/$49/yr), Thrifty Traveler Premium ($130/yr). Book on alert, rely on the 24h rule. Error fares: don't book nonrefundable hotels until the ticket has held a few days.

## Tier 2: big savings, low risk (needs points/cards/planning)

6. **Points when cpp beats your point's value**: run `scripts/points_vs_cash.py`. Transfer only after confirming award space; transfers are irreversible.
7. **Transfer bonuses** (live list on PointsYeah and Frequent Miler). Nov 2026 examples: Chase→BA/Iberia/Aer Lingus 30% (to Dec 1), Amex→Virgin 30% (Nov 30), Capital One→Flying Blue 20% (Nov 30).
8. **Book United flights through a partner.** Search united.com logged in (Saver space is what partners see), then price in LifeMiles (no surcharges, beware phantom space), Turkish, Aeroplan ([CHG] dynamic on United since Mar 2025 + ~$30 fee). [CHG] United cardholders get ≥10% off United awards from Apr 2026, and **co-brand pricing can be dramatic** (seen: 13.5k with card vs 42k without on the same domestic route). Excursionist Perk is gone (Aug 2025).
9. **Alaska Atmos sweet spots.** Partner (American) flights under 700 miles in the Americas: **4,500 points** one-way. Stopovers allowed on partner awards. ~$20 partner fee. Bilt transfers 1:1. [CHG] Saver fares no longer earn points/status. Seen: an American 1-stop domestic at 17,500 Atmos vs $352 cash (1.9cpp).
10. **Virgin Atlantic for Delta flights.** Often far cheaper than SkyMiles for Delta domestic (seen: a Delta domestic nonstop at 22k Virgin points). Chase/Bilt/Amex/Cap One/Citi all transfer.
11. **Flying Blue Promo Rewards.** Monthly, ~25% off. Nov 2026: US-Europe economy from 18,750 one-way, book by Nov 30. Surcharges ~$100-250.
12. **Southwest Companion Pass.** Companion flies for taxes. 2026 threshold 135k qualifying points. [CHG, BIG] **Qualifying points are retired Dec 31, 2026**; a pass earned in 2026 lasts through Dec 31, 2027. Card approved by ~Dec 2, 2026 counts toward 2026. Only worth it if you fly Southwest with the same person often. [CHG] Southwest now charges bags ($45/$55) and assigns seats.
13. **Card portals.** [CHG] Chase Reserve's fixed 1.5cpp is gone for points earned since Oct 26, 2025 (Points Boost, ~1.15-2cpp, devalued repeatedly); older points keep 1.5cpp until ~Oct 2027. Portal wins on cheap domestic cash fares with no award space; transfers win on long-haul/premium.
14. **Delta dynamic awards.** No chart; cardholders get 15% off Delta-operated awards. Below ~1.1cpp is poor.

## Tier 3: moderate risk

15. **Basic economy.** Only when solo, carry-on, plans certain. [CHG] United basic earns redeemable miles only with a card/status (Apr 2026); American basic lost elite perks (May 2026). Main cabin keeps free changes and repricing: often worth $40-60 more.
16. **Split tickets / self-transfer** (Kiwi MCP). 20-50% international. No protection on a missed connection: 4h+ buffer domestic, overnight international, carry-on, insurance, check transit visas.
17. **Positioning flights.** Cheap flight to a gateway with better fares/award space, the day before.
18. **Frontier GoWild.** $0.01 + taxes per segment, each extra segment adds taxes, so book separate nonstops through a hub (e.g. X→DEN, DEN→SEA as two bookings). Domestic opens the day before departure (12:00am local); international 10 days out. [CHG] Fall/Winter 2026 pass $199 through Feb 28, 2027; paid early booking $29-89; blackout days bookable with a $79-159 Peak Day Charge; Thanksgiving/Christmas blacked out [UNV exact dates]. Capacity-controlled: a sold-out cash flight has no GoWild seats. **Always hold a cancellable fallback** (Southwest, or a 24h-rule booking).
19. **Point-of-sale / VPN.** Mostly a myth for US carriers (0-15%, inconsistent). Sometimes works on foreign carriers' local sites; use a no-FX-fee card.

## Tier 4: big savings, real risk

20. **Hidden city (skiplagging).** Book A→B→C, get off at B. Legal, but breaches every major US contract of carriage. American won $9.4M from Skiplagged (copyright, 2024; upheld May 2025) and has locked AAdvantage accounts of repeat users. Rules: one-way only, carry-on only (board early: a gate-checked bag goes to C), never attach your frequent-flyer number, irregular-ops rerouting can skip B, do it rarely. 20-60% on hub-premium routes. Scan with `scripts/fare_scan.py hidden`, cross-check on skiplagged.com.

## Sources
Federal Register 2026-13675; Frontier newsroom; Southwest Rapid Rewards; Skift and Bloomberg Law (Skiplagged); One Mile at a Time; Frequent Miler; The Points Guy; Thrifty Traveler; AwardWallet; View from the Wing; Expedia 2026 Air Hacks; CheapAir 2024 study.
