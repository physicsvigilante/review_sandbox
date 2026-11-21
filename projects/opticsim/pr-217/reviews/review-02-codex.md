# Opticsim PR #217 independent focused review R2

**BLOCKED — B1 remains open.** The correction closes the original power mutations. A nonzero detector accumulator and an inconsistent segment origin still qualify at this exact source.

- Candidate `fd0121bd729c1ec1bbf5bc0cb983c65a6b47cbd8`, tree `7487378048374ea7385dd1875b82ae2353a849fb`.
- Production base `52d14f68725da5080a1cca112602e7776c9cc25e`.
- Synthetic test merge `9e89d6cb1de228da57b8ac9ad7893ffcf8a5c8cf` has the base and candidate as parents and the exact candidate tree.
- [Original independent verdict](https://github.com/physicsvigilante/review_sandbox/blob/e078a70082dff5ff7adcb7a281ccd42455bbcb81/projects/opticsim/pr-217/reviews/review-01-codex.md).

## Closed parts of B1

The original source, slab and detector brightness faults now withhold native observations. The auditor binds both channels to the authored SingleRay and preserves them across the zero-absorption, Fresnel-disabled glass. It also preserves the pre-delegation detector point and the outgoing polarization channels. The explicit detector length now matches the shared 1–5 mm scope.

Independent replays passed the nine focused tests, all 128 genuine public controls from R1, v25's 15 public CLI cases and nine real Chrome checks, and v33's seven real Chrome checks. The 128-case sweep again gave a maximum detector-position discrepancy of 0.001310768 mm, maximum tangential-direction discrepancy of 0.0000484934, and exact signed power for genuine runs.

## Remaining native qualification faults

- **B1a, detector accumulator.** I delegated the genuine detector's `onSimulationStart` and then wrote `this.power = 10`. The public signed native power was 10.08 for an authored brightness of 0.08, and v33 remained verified. The initial audit adds a correct increment to any finite accumulator rather than requiring the zero baseline. A second injection performed after the single detector hit, on its genuine outgoing intersection check, overwrote the exposed terminal power with 10 and also qualified. This exactly-one-hit profile should require zero before the incident and compare the public terminal signed power with the signed authored incident power.
- **B1b, incoming origin continuity.** I delegated the genuine slab intersection test and shifted both endpoints of the first incoming ray by 0.02 mm along the same ray line, after the source had emitted its verified original geometry. v33 still qualified. Its check uses the previous audited point, current direction and next contact but does not establish that the current native incoming origin is the previous audited point. Compare the incoming point before delegation at every glass and detector incident with the last audited point.

These are deliberately injected callback faults, not failures of the genuine pinned physics. A fresh exact-head review is required after the two outstanding checks and their nonpassive/stale-read regressions.
