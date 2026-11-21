# Opticsim PR #219 independent focused review R2

**CLEARED for owner-authorized integration at the exact candidate below.** Both numerical witnesses from R1 are resolved. No release blocker remains.

| Identity | SHA |
|---|---|
| Candidate | `839aefbd7a25a14993aa4010f3a76aead8fce8a7` |
| Candidate tree | `fb0df83acc587cf1a31072049e0aaf29ea7aae22` |
| Production base | `3f8e800f0be6e48a99419fe6aa21e542b176d0f0` |
| GitHub PR test merge | `cf147c40cf8d64121f6bd6f085cf4fc4245714e4` |
| PhyDemo pin | `811f508d2b070898c241a568b0c167dcb8645251` |

The PR test merge has the base and candidate as parents and the exact candidate tree. [Original blocked review](https://github.com/physicsvigilante/review_sandbox/blob/98bd4cf3158411e27d5a1edf8e4d5badc1fc17d1/projects/opticsim/pr-219/reviews/review-01-codex.md).

## Source and geometry

- I viewed only the original A09 Problems image, whose SHA-256 `073a971a9eaca6a664e6f509e8b3d6e4428cd736ad80fe81b0fa0bc8e2092947` matches the frozen record. The figure supports the axis-based trapezoid, its taller near end, both transverse end edges and location beyond the centre. Those relations imply an inverted trapezoid between focus and centre, with the near-side image farther from the mirror and taller. Absolute object and image dimensions remain unspecified.
- For the general outline, the dimensional gap u−f is positive at every vertex and therefore across the complete convex polygon. The mapping is projective on that domain and preserves strict winding and edge order. The binary64 projection now uses the dimensional gap and compares every represented coordinate difference and every triple's signed area with exact rational geometry. The cross-multiplied comparison enforces the documented relative 1% limit, including exact zero differences. Equivalent exact heights share one deterministic rounded coordinate, independent of input winding.
- The formerly collapsed near-focus triangle now gives both resolved adjacent axial offsets of about 1.114e−7 mm. The unresolved microscopic triangle withholds its vertices. I independently qualified 360 ordinary outlines across three units and both windings and checked 1,620 projective edges. The maximum coordinate residual versus the dimensional relation was 7.28e−11 mm. I also independently checked 288 exactly horizontal image edges in both windings. The grouped rounding was exercised by 48 controls whose individual height evaluations initially rounded differently.
- The A09 CLI returns an explicitly conditional analytical result with no native run. An optional detector request without authored native apparatus remains unresolved and does not suppress the conditional outline. The four separate v6 native controls each recorded three genuine AngleSource roots and one real ArcMirror reflection followed by a sampled detector crossing for each root. Pairwise line-derived estimates agreed with the conditional point locations within 0.063399 mm axially and 0.001163 mm transversely. The point controls establish neither a native outline nor finite visibility.

## Verification and archived evidence

- All 11 exact-head workflows succeeded. The [optical composition job](https://github.com/physicsvigilante/opticsim/actions/runs/44871484137/job/136746770193) passed 1,277 Node tests. The independent run passed 34 focused tests covering old single-point queries, the v9 helper extraction, projection and native points.
- The [A09 authoring archive](https://github.com/physicsvigilante/opticsim/actions/runs/44871484137/artifacts/14693229224) matched SHA-256 `7889a50c6069f0f33c5d88349655038fae4ff6a94c0aff9e34aa9201288d69e7`. The four normal qualitative CLI records and four native v6 point records matched independent execution byte for byte.
- Eight historical v9 public cases and ten actual Chrome checks passed independently. The exact rational helper extraction preserved all 42 deterministic v9 case artifacts byte for byte against the reviewed production tree and the [hosted compatibility archive](https://github.com/physicsvigilante/opticsim/actions/runs/44871484097/artifacts/14694465603), SHA-256 `97071b3a4335edc654fbe998ca6839c557693b20bec52a71cb7f337737aa799f`. The legacy rotated computed-critical case retains documented native variability and was excluded from byte-equivalence claims.
- The [hosted v9 Chrome archive](https://github.com/physicsvigilante/opticsim/actions/runs/44871484097/artifacts/14693718430) matched SHA-256 `6896fa5c0d5e4474f41332f6cdafec71b42253a133fef9e2c91bdbcefecfad1f`. It contains the same ten acceptance check identities and two screenshots, with a passing report on Chrome for Testing 158.0.8127.36. The A09 outline is CLI-only.

Integration and the merged-tree CI check remain separate gates.
