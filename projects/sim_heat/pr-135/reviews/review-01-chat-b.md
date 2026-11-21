# Independent R2 review of SIM_HEAT PR 135

**Verdict: accept for the scoped offline target-time calculation.** No blocking finding. Source base `1ecb933f313fc5fa00d49f4730c49aeabef71f1b`, head `2d061edc4114851d94bcb4d2cb197946e1054be6`, review packet `c97c973f170348c49916bb787d8352ab31732d1a`. GitHub reported the source PR open, draft and unmerged. [Pinned source](https://github.com/physicsvigilante/sim_heat/blob/2d061edc4114851d94bcb4d2cb197946e1054be6/tools/radiating_body_time.py)

## Physical and numerical reasoning

With rods in quasi-steady balance, the power into the isothermal body is the sum of the effective bath-to-body conductances times the corresponding differences in integrated conductivity potential, plus the enclosure-to-body radiation power. Positive material conductivity makes the potential strictly increasing over the checked temperature range. Each allowed conductive power decreases with body temperature, as does the radiation power at nonnegative Kelvin temperatures. Clipping a coupling's lower bound to zero uses the passivity of the steady network. The factorized fourth-power difference preserves the sign at equilibrium.

Along either direction of travel the power in the direction of motion decreases. A positive lower bound at the target guarantees positive directed power along the whole path. When the upper bound at the target is nonpositive, the body must stop short, approach equilibrium asymptotically or move away. The smooth power law precludes finite-time arrival at an equilibrium from a distinct initial temperature. An interval straddling zero prevents a finite-time decision. On a reachable path the left endpoint upper power bounds the reciprocal below and the right endpoint lower power bounds it above. Python Fraction arithmetic and outward per-panel rounding preserve that enclosure. Fixed 512-panel bounds can widen near an asymptote.

## Independent checks

I ran the three pinned body-time unit tests and additional cases through the source entry point. The table reports seconds, rounded for display. The independent reflective-wall solution used 2 W/K, 137 J/K and the logarithmic approach to the 380 K bath. The star used reference 310 K, relative slope -0.002/K, bath couplings 1.5 and 0.6 W/K at 280 and 380 K, enclosure 352 K, area 0.75 m², emissivity 0.73 and sigma 5.67e-8 W/(m² K⁴). Its independent midpoint calculation used 32,768 panels and the average affine conductivity between each bath and the body.

| Case | Initial → target K | Independent time | Returned interval | Stored energy J |
| --- | --- | ---: | --- | ---: |
| Reflective wall | 200 → 301 | 56.410366 | 56.362407–56.458383 | +13837 |
| Reflective wall | 600 → 480 | 54.009329 | 53.965569–54.053140 | −16440 |
| Radiating star | 295 → 306 | 6.416908 | 6.415278–6.418539 | +1507 |
| Radiating star | 399 → 365 | 14.945536 | 14.931035–14.960055 | −4658 |

Independent star power into the body decreased from +266.163 to +205.548 W during heating. During cooling it ran from −487.764 to −190.839 W. The interval tests and the exact signed C times temperature change agreed in all four cases.

The reflective wall returned unreachable with no time for 380 → 381 K, 292 → 290 K and 500 → 380 K. Identical 262 K endpoints returned zero time. A synthetic response-row probe supplied a warm-bath conductance interval [0.49, 0.51] W/K at a 305 K target. Starting from both 290 K and 320 K gave unresolved with no time. The synthetic interval exercises the decision branch only. Unknown port, incorrect source facts hash, nonpositive conductivity and emissivity above one each raised a refusal.

## CI and provenance

GitHub reported success and the exact reviewed head for both runs and both jobs. I downloaded both original ZIP files, recomputed SHA-256 and checked every member's ZIP CRC.

- [General conduction job](https://github.com/physicsvigilante/sim_heat/actions/runs/44874719391/job/136756774813) and [archive](https://github.com/physicsvigilante/sim_heat/actions/runs/44874719391/artifacts/14695277152). SHA-256 `99580b2679a66135ac9b2013f612f7c8adca3feb3aa791a504ef2a13cbc175de`. The source-head file matches the pin. The archive contains seven control records, 41 oracle records and a readable compressed offline output.
- [Series extension job](https://github.com/physicsvigilante/sim_heat/actions/runs/44874719400/job/136756774967) and [archive](https://github.com/physicsvigilante/sim_heat/actions/runs/44874719400/artifacts/14695104589). SHA-256 `2344833a9dd5aba31c40a3e386b00e72d750056fe18e22cbfb04fab7e5c60493`. The five members include the target-time result. Recomputing that record from the pinned star reproduced every JSON field, including the study, facts and model hashes, +4000 J stored energy, both rational time limits and four false qualification/runner flags.

The finding covers an offline, lumped-body calculation attached to a steady rod network. Native transient behavior and independently certified reference qualification are outside this verdict. Source merge requires separate owner approval.
