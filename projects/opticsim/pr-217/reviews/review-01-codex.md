# Opticsim PR #217 independent review R1

**BLOCKED — B1 remains open at this exact source.** Do not integrate.

| Identity | SHA |
|---|---|
| Candidate | `f780bbee7fb3045d721c4d7944589551c51a659e` |
| Candidate tree | `b388ebce8b19b1f8c718fb252e8fc041ed692735` |
| Production base | `52d14f68725da5080a1cca112602e7776c9cc25e` |
| GitHub PR test merge | `4009672f33e4457ad606f9dfbad2de2fa19bb4e0` |
| Pinned PhyDemo | `811f508d2b070898c241a568b0c167dcb8645251` |

GitHub's test merge has the base and candidate as parents and the same tree as the candidate. All 11 hosted workflows passed, including the v25 and v33 real Chrome steps in optical composition run [44868615080](https://github.com/physicsvigilante/opticsim/actions/runs/44868615080). The failure below is a gap in the independent qualification, reproduced with deliberate mutations of native callbacks.

## B1 — v33 accepts a brightness-changing passive detector and contradictory source or glass power

`src/native-entering-graded-slab.js` validates direction, point and callback count. `src/native-detector-audit.js` predicts the signed increment using incident brightness and checks it after Detector delegates. The checks do not establish that either polarization channel survives that callback or remains consistent with the authored source through the glass.

I ran the public v33 example and wrapped individual prototypes, delegating each genuine callback exactly once. After Detector delegated, halving or doubling the ray's brightness channels still left the run completed and `v33GradedSlabVerified:true`. The same qualification survived doubling only the p channel after the SingleRay emitted or doubling only the s channel after the final GrinGlass callback. The latter two faults changed the accepted public detector signed-power reading from 0.08 to 0.12 relative units for the unchanged authored source. These are adversarial injections. The genuine pinned callbacks do preserve the channels under this explicit zero-absorption, Fresnel-disabled policy.

Bind each emitted channel to half the authored SingleRay brightness. Check both channels through the owning GrinGlass and Detector callbacks, keep the actual signed increment check, and add prototype-level regressions covering both the reported power and outgoing detector passivity.

## Qualified placements and compatibility

- The fixed trusted local native field represents the stated positive physical index-squared gradient in y-up coordinates. Horizontal optical momentum and an inward normal component remain positive throughout the declared finite-angle transmission branch. At the unit-index exterior beyond the opposed face, the outgoing analytic direction matches the incident direction.
- In an independent 128-case sweep of the public profile, the actual pinned runs completed at all tested positions, including 10° and 70° tangent-relative incidence, 0.2 and 0.4 mm slabs, translated entry points to within 1 mm of a world boundary, 0.10001 mm entrance lateral clearance and both signed detector orientations. Independent Simpson integration gave a maximum detector-position residual of 0.001310768 mm and maximum tangent-component residual of 0.0000484934. The genuine signed-power residual was exactly zero.
- The seven focused tests replayed 30 frozen translated native controls and the six previous non-grazing A15 cases. The independent public CLI and seven actual Chrome checks passed, including grazing refusal, incidence retrace and qualified reopen.
- The inherited v25 integration passed 15 independent acceptance cases and nine actual Chrome checks. Its trusted field, optical integration and source model remain separate. A15's sealed analytical and first-passage case inputs and upstream pin are unchanged.
- v33's dedicated validator specifies a 0.5 mm detector lower bound, but the historical shared component schema refuses detector length below 1 mm. This conservative discrepancy prevents short detectors from being authored. Align the scope declaration with the effective accepted interval.

The positional and directional tests attest to observed sampled behavior within the declared envelope. No original A15 grazing detection, arbitrary GRIN field, measured optical flux or global Euler error bound is established. Standing integration authorization still requires a corrected exact head to clear independent review and CI.
