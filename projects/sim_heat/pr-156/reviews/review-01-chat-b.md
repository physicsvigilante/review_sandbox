# Independent R2 review of PR 156

**Verdict.** The pinned implementation passes the requested offline mixed-surface review. I found no blocking defect in its physical balance, reported intervals or offline evidence. Source head `5a43df5821389472681a4724443e7557134158a1`, base `545d1b6c78ca9b2ff83892b9f5dc177b54467557`, request commit `29a34a5ab8bcf0bd1135f53d3f5f55762f4b6a09`. [Source diff](https://github.com/physicsvigilante/sim_heat/compare/545d1b6c78ca9b2ff83892b9f5dc177b54467557...5a43df5821389472681a4724443e7557134158a1)

## Physical balance and uncertainty

For outward air and radiation rates, steady state gives (Topen − T)/R = hA(T − Tair) + εσA(T⁴ − Tenc⁴). The outward-minus-inward residual increases strictly on nonnegative Kelvin temperatures. Its root lies between the minimum and maximum of the three imposed temperatures. The source's equivalent open temperature is monotone in Topen and, at each fixed Topen, monotone in R with direction determined by Tair − Topen. The endpoint evaluations therefore bound it. R/(1 + RhA) increases with R. Treating these effective intervals independently can widen the root interval while retaining the physical solution. Both exterior powers increase weakly with T. Intersecting their summed interval with the wall's independently bounded signed power preserves the true wall rate.

I solved the unreduced equation by 220 rounds of exact rational bisection (or an exact residual zero) and evaluated all three powers on that bracket. Across 32 combinations, each of the four returned intervals intersected its corresponding reference bracket. I used the composite wall (380 K, 1/2 K/W) and the three-terminal network's middle port (2160/7 K, 10/21 K/W). For each I crossed air temperatures {0, 600} K, enclosure temperatures {0, 620} K, h values {0, 2500} W/(m² K) and emissivity {0, 1}, with A = 0.2 m² and σ = 5 × 10⁻⁸ W/(m² K⁴). Offline provenance flags stayed false in every case. Eight source tests for mixed and radiation-only surfaces passed, including incomplete option pairs, negative h and the signed 400 K example (wall −40 W, air −215 W, enclosure +175 W).

## CI archive replay

I downloaded both archives, verified their full SHA-256 and all ZIP member CRCs. The mixed-surface JSON matched fresh exact-head output field for field. TwinBridge's embedded head matched the candidate and its fresh JSON, oracle and control results matched the pinned original evidence after decoding. The historical implementation and held-out freeze diffs were empty. Eight local H1/TwinBridge tests also passed on a byte-preserving export.

- TwinBridge digest `cf4f9cec868a635a48020ef772d63255451764ab4e473e15a3611ceaeda707a9`. [CI archive](https://github.com/physicsvigilante/sim_heat/actions/runs/44884215817/artifacts/14699196500)
- Series extension digest `ea5e2ba03d93022c88e7a6ed3a5eca60566ade4c9410b05c6d41883cfd78eccb`. [CI archive](https://github.com/physicsvigilante/sim_heat/actions/runs/44884215839/artifacts/14699321242)

**Execution notes.** The first multi-command replay lost its temporary checkout between sandbox calls and failed on imports. The next extraction passed the 32 probes but the historical original-T test refused a model hash in the default Windows Git archive. Re-exporting the identical head with core.autocrlf=false preserved source bytes and passed all eight H1/TwinBridge tests. Native OpenModelica execution, measured convection and calibration of h remain outside this offline review. The draft source requires separate owner approval for merge.
