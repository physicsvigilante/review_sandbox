# Independent Codex review of Opticsim PR #216

**CLEARED FOR OWNER DECISION.** The final head preserves the exact stated refractive-index law in the A15 source. I found no outstanding blocker in the conditional first-passage model, numerics, or finite native runs.

| Identity | Reviewed value |
| --- | --- |
| Final candidate | `9bcd411ec6b3063ebfde16144f93aca21d2813cb` |
| Tree | `9c6fb49a94be1f02eb9cdf7852c166902a481f56` |
| Base | `040dedaeee64b7d74cd26908adbeb0ce5406c230` |
| CI merge | `faafce1e65d947f493678506275f30c69cb66f5a` |
| Freeze commit | `eacdee72e20f8d4a73381404dc7b99bfecd5bd21` |
| Frozen protocol blob | `3bee21264a7531bb7600b016f7d54c1627b8bae1` |
| Analytical source blob | `d5cbecfd757ba94e16f18582b4b8917955492896` |
| PhyDemo pin | `811f508d2b070898c241a568b0c167dcb8645251` |

## Source, first passage and limiting branch

I inspected the Problems-only A15 image `08_Ray_Optics_Explanations/03_General_Refraction/Problems/012.png` and confirmed SHA-256 `abb40484b40dcd9b9a4c663751cad54c00971d218eb42a018e638b66e024bca1`. The statement gives grazing incidence, index equal to the square root of one plus the given inward coordinate, and symbolic thickness. The corrected public example keeps the equality. It introduces an explicit gradient length to express the dimensioned model and states the unit-index exteriors and inward grazing limit as assumptions.

The tangential momentum q is conserved. The normal momentum satisfies the inward root of the eikonal speed constraint and increases with tangential position because the gradient is positive. For q > 0 its derivative with respect to x equals 1/(2qL), including the immediate inward branch at zero initial normal momentum. This rules out a delayed entry branch. For the matched limit in A15, the dimensionless path is y/L = (x/L)²/4 and first far-face position is (2√(d/L), d/L). The far boundary is an exact critical direction under the stated exteriors.

I independently integrated tangential displacement transformed to avoid the endpoint singularity. The check covered 3,924 qualified dimensional cases in mm, cm and m, including 765 normal cases, 51 exact far-face critical limits, 42 unresolved far critical results with positions preserved, and 399 far-face TIR cases. Another 1,323 could not enter and 108 uncertain entry degeneracies stayed withheld. The maximum first-contact discrepancy was 2.64 × 10⁻¹¹ mm. Matched far indices preserve the internal direction. First contact and outgoing classification remain distinct.

## Native, compatibility and archived evidence

The isolated candidate passed 48 focused tests. I independently replayed all six pinned finite-angle runs and checked 8,417 actual medium callbacks. The maximum exit-position difference against the analytical first passage was 0.000348 mm and the maximum detector tangential-component difference was 0.000153. The two Euler steps are finite controls. The largest sampled interior invariant difference was 0.000217. Every run completed with one real downstream detector crossing.

All 52 prior public example inputs and plans matched the base. A mixed request against a v25 scene preserved all three native observations alongside an unavailable inapplicable analytical request. Reduced A15 facts preserved the conditional result alongside the native-scene-required diagnostic. The v25 public scope and numerical guard remain separate. Its nine real Chrome checks passed independently and in hosted CI.

All eleven workflows passed on the final candidate tree. The optical job passed 1,255 Node tests. The four byte-bound analytical records and six native evidence records matched my independent runs byte for byte. I verified archive SHA-256 `02d1d16e055b38ea1a9b190878f411327884bf6a2ef220f4c3cf2f76eed80d4b`. [Optical composition run](https://github.com/physicsvigilante/opticsim/actions/runs/44867872101) · [Evidence archive](https://github.com/physicsvigilante/opticsim/actions/runs/44867872101/artifacts/14692633746)
