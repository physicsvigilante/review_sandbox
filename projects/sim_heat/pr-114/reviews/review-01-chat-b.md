# Chat B R2 review of closed two-bath equilibrium

**Verdict: accept the offline equilibrium calculation at `e4c64a026917d0fa23ed6997fde7c7db12a63cfc`.** I found no blocking or major defect. The comparison base was `0fc55da0ea00c4094654fc15d6fc03cbd6b8b9f7`. I reviewed the pinned diff in a fresh reviewer context, exercised the public investigation function and inspected the downloaded CI evidence. [PR 114](https://github.com/physicsvigilante/sim_heat/pull/114) · [Review request](https://github.com/physicsvigilante/review_sandbox/blob/030bb6a19e49eb478525eb36bd0e71c1fca5d8b3/projects/sim_heat/pr-114/REQUEST.md)

## Physical regimes and ledgers

The initial hot bath can give up its liquid's freezing energy F. The cold bath can absorb its solid's melting energy M. For a positive temperature gap d, if F + Ch d ≤ M the cold transition fixes the final temperature. If M + Cc d ≤ F the hot transition fixes it. At equality the final traces of both participating phases disappear. Between those cases both baths are single-phase at equilibrium and raising their common temperature above the cold transition by one kelvin costs Ch + Cc joules. Equal initial temperatures yield zero transfer. These conditions assume an insulated pair, a connected storage-free conducting network, constant phase-specific heats and no other transition in the interval.

I used exact rational expectations for hot/cold transitions of 311/301 K, total heat capacities of 12/15 J/K, and 2 kg solid plus 1 kg liquid per bath. Each row gives positive energy received by the colder bath.

| F (J) | M (J) | Final temperature (K) | Transfer (J) |
| ---: | ---: | ---: | ---: |
| 60 | 200 | 301 | 180 |
| 60 | 180 | 301 | 180 |
| 200 | 40 | 311 | 190 |
| 190 | 40 | 311 | 190 |
| 100 | 80 | 301 + 140/27 | 220 − 1680/27 |

I added an equal-transition case and ran all six with both argument orders, both assignments of warm material to terminal name, and horizons of 0 and 999 s. All 48 returned the expected temperature, each phase mass, and signed latent, sensible and total joules. Removing the optional equilibrium member reproduced the complete base implementation result for each input.

A separate case used a 311 K donor with 1 kg solid and 2 kg liquid, latent heat 45 J/kg and solid specific heat 4 J/(kg K). The 301 K receiver contained 0.5 kg solid and 1.5 kg liquid with 80 J/kg and liquid specific heat 9 J/(kg K). Both argument orders gave 920/3 K. The donor ended with 3 kg solid and lost 90 J latent plus 52 J sensible. The receiver ended with 2 kg liquid and gained 40 J latent plus 102 J sensible.

## Refusals and preservation

Twelve independent negative controls passed. Eight challenged the heat-capacity tuple length, zero, negative, nonfinite and exponent forms. Four separately set transition temperature, latent heat, initial solid or initial liquid to zero. Five repository equilibrium and first-event tests also passed locally using the supplied pinned interpreter.

## CI archives

Both jobs succeeded at the reviewed head, with explicit PR-head checkout. I downloaded both ZIPs, hashed the bytes, and checked member CRCs.

- Study artifact 14692731310, SHA-256 `2012df0e09ae5584efe71396d2256f4840b00643d1f8130cd5b94ce035e19df7`. All fields in the 300 s, 1000 s and optional equilibrium JSONs matched local replay. The 750 s first event and 120 W rate coexist with a limiting 273.15 K, 156000 J transferred and 11/334 kg cold solid. The native execution, qualification, independent-reference certification and runner-consumable flags were all false. [Study job](https://github.com/physicsvigilante/sim_heat/actions/runs/44867190188/job/136733388479)
- General conduction artifact 14692462230, SHA-256 `986ab8c07bf6036e20d73a0503dedfeb67699ed360f5cfef4a39dd328cde4475`. Its source-head member matched the reviewed SHA. The archive contains the compressed replay, oracle results and seven negative-control outcomes. [Replay job](https://github.com/physicsvigilante/sim_heat/actions/runs/44867190319/job/136733388834)

The worked example supports the stated limiting temperature and remaining ice mass. It supplies no arrival time or post-exhaustion trajectory. Classroom effectiveness and native behavior were outside the review. Owner approval remains a separate merge decision.
