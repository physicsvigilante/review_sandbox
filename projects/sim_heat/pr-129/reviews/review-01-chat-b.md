# PR 129 independent Chat B review

**Accept for the scoped offline entropy calculation.** No blocking findings. I reviewed head `7c7db37a3f529301187f4b3dc85490b0fc49fdcb` against base `3ece211710e6c10552b678ce2c7d04d61d123c3c`. [Pinned request](https://github.com/physicsvigilante/review_sandbox/blob/ed9c5baf13466be2288e46447f17ef99ec5edb6e/projects/sim_heat/pr-129/REQUEST.md)

## Independent physics checks

For a steady conductor exchanging heat with ideal isothermal reservoirs and a coexisting phase bath, entropy generated over the modeled interval equals the sum of their entropy changes. Each heat integral takes the sign of energy entering its reservoir and uses that reservoir's absolute temperature. Replacing the external enclosure between stages changes the temperature divisor. Restoring the phase inventory cancels the bath's net entropy change while heat transfer during recovery continues to generate entropy. External work to prepare or reset reservoirs is outside this system boundary.

I solved the face and two interior steady balances of the six-rod joined network at 110 decimal digits, with coolL as the 300 K bath, warmL as the radiating face, and separate maintained terminals at 330 and 280 K. For an independent total, I summed each physical rod's production rate G(Ta − Tb)²/(Ta Tb) and the net outward radiation power times (1/Tenclosure − 1/Tface). Each returned interval enclosed its independent reference, including both supports, the bath, each enclosure, the enclosure sum and total production.

| Exposure sequence | Independent entropy generated (J/K, rounded) |
|---|---:|
| 470 K for 19 s, then 225 K for 11 s | 7.811445884749667 |
| Same, followed by recovery at 240 K for 61.146881786643524 s | 13.89153412779721 |
| 520 K for 800 requested seconds with 200000 J available, ending at depletion after about 778.398951336816366 s | 383.3383875403858 |
| 520 K for 778.398951336816365782 requested seconds, inside the event-time bracket | 383.3383875403858 |

For uncertain depletion I used the earlier of the independently computed depletion time and requested duration. Both depletion cases stopped before the scheduled 250 K stage. Recovery after uncertain depletion, same-direction recovery and a modeled 0 K enclosure all raised the expected refusals. On a separate two-terminal link, equal 310 K temperatures and a 650 K enclosure with zero emissivity both gave exactly [0, 0] J/K. Nine focused repository tests passed, including star and triangle cases. The reported interval sums are conservative where stage times and heat rates are correlated. All four offline provenance and capability flags remained false in my joined-network runs.

## CI archives

I verified successful job conclusions, artifact/run identities, the exact source head, SHA-256 over both downloaded ZIP files, and ZIP member CRCs.

- [Series job](https://github.com/physicsvigilante/sim_heat/actions/runs/44872584601/job/136750185021) and [five-file archive](https://github.com/physicsvigilante/sim_heat/actions/runs/44872584601/artifacts/14694497128). SHA-256 `c8cd459516140520f5cdb15d3baf374338ee1355f677e2ea2fd6ec59a7b88cf9`. A local replay matched the complete archived star entropy JSON.
- [TwinBridge job](https://github.com/physicsvigilante/sim_heat/actions/runs/44872584615/job/136750184965) and [four-file archive](https://github.com/physicsvigilante/sim_heat/actions/runs/44872584615/artifacts/14694567081). SHA-256 `bf889f6b559bb681577edaf211ff6acdd4c3e1e495c9e7905c08dd77344a8a09`. The archived source-head file matched. The decompressed fresh output and both oracle and control JSON files matched the pinned held-out evidence.

This verdict covers analytical entropy accounting through the modeled coexistence interval and optional recovery. It grants no native qualification or source merge authorization.
