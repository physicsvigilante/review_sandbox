# Independent Codex review of Opticsim PR #204

**CLEARED FOR OWNER DECISION.** The revised head preserves valid native work when a material query is inapplicable. I found no outstanding blocker in the thin-lens comparison, its numerical limits or the finite native controls.

| Identity | Value |
| --- | --- |
| Reviewer | Codex, independently assigned by the owner |
| Head | `b69ce55effbb51e118b65953f97b37ecb3d23e9d` |
| Tree | `0e91b4b56b91206ab7ff54095efa02be036b264d` |
| Base | `ab897deae9408bdd665015cec2ead1e2eb922f77` |
| Protocol commit | `2a439924d61402972fc2dddc963ad7c850960352` |
| First native control commit | `1f59f451763281ff317434f7d1e80780d7848a66` |
| Upstream PhyDemo | `811f508d2b070898c241a568b0c167dcb8645251` |

## Source and scope

I read the A34 Problems image and confirmed its SHA-256 `26982ca24f70b6c009b9c82477fb1962be8a41f49ef9cc53306f5ae23d4eacc2`. The stated quantities are two identical double-convex shapes, glass indices 1.5 and 1.7 and a liquid index of 1.6 for part (b). A unit-index exterior for part (a) and the thin paraxial approximation are explicitly assumed. The image says a ray *parallel* to the axis. The off-axis and precisely axial cases are distinguished in the result limitations. The protocol retained its original Git blob `d6295b78cb4981f5c82306eae6fef74ef3f082e2` and preceded both the native test and production algebra. [Frozen A34 protocol](https://github.com/physicsvigilante/opticsim/blob/2a439924d61402972fc2dddc963ad7c850960352/evaluation/immersed-material-lens-v1/frozen-protocol.json)

## Physics, units and numerical controls

For the common signed curvature factor C = 1/Rfront − 1/Rrear in m⁻¹, the refracting power is (nglass−nmedium)C and the signed image-side focal length from the thin-element plane is nmedium/power in metres. Consequently f₁/f₂ in the assumed air is 7/5. In the liquid the index-1.5 lens diverges and the index-1.7 lens converges. For the synthetic +0.2/−0.2 m radii, the powers in air are +5 and +7 D. In liquid they are −1 and +1 D with signed focal lengths −1.6 and +1.6 m. A34's sign-only shape produces no invented absolute power or focal length for those materials.

- **Independent numerical check.** I propagated a unit-height parallel ray through the two successive normal tilts using linearized Snell refraction, independently of the shared implementation. Across 2,400 material-pair/medium/radius combinations I checked both powers, finite distances, actions, ratio order and named afocal handling. These included 1,394 individual afocal lens outputs arising from matched indices or equal signed radii. Nearby index matches and near-cancelling curvatures on either side withheld comparison, as did a finite focal distance beyond the declared numerical cap. Sign-only geometry withheld unknown magnitudes.
- **Reuse and preservation.** The #201 paraxial surface-pair arithmetic is exported with the same expressions and called at zero analytical thickness in the new numerical branch. Its original positive-thickness callers retain their bounds, units, reference origins and formulas. I compared the complete planner outputs for all 42 prior public examples with the base-equivalent v30 export and reran the #201 native and analytical tests. All comparisons passed.
- **Native corroboration.** I reran all four frozen v15 cases, covering each glass in each exterior. The actual 5 mm lens uses named front/back arcs, and both off-axis sampled rays reached a downstream detector after two refractions. Separately, I tested all four combinations at heights −0.75, 0 and +0.75 mm, with a different detector position. Every axial ray remained axial. Across the eight off-axis rays, the largest difference between the extrapolated detector direction and my independently propagated finite-thickness back focus was 0.0129 mm. I subtracted the rear pole at x = +2.5 mm before comparing intercepts. The thin focal distance and the finite lens's rear-pole distance are separately identified.
- **Public workflow.** In an isolated export, 42 focused tests passed on the final head. The A34 CLI run produced the original input, analytical result, plan and report, issued zero native calls and created no portable scene. I reproduced an initial dispatcher defect that blocked a valid v30 native face request when paired with an incompatible A34 request. On the revised head, the face measurement qualified with all 20 samples. The inapplicable analytical request returned unavailable with `UNSUPPORTED_FACTS`. An unsupported material model was distinguished via `UNSUPPORTED_MODEL`. The corrected result preserves the availability of independent measurements.

## Exact-head hosted evidence

All eleven pull-request workflows passed. The optical log recorded 1,200 passing Node tests and individually identified all four finite native controls and the mixed-request regression. I verified the downloaded authoring ZIP against SHA-256 `fbf2ad0acf55a1202d8ee9f7af13929660e60461a0b0c1bf78a6d85c09b4d017`. Four A34 public files, four native witness records and six mixed-request evidence files matched the corresponding independently generated files byte for byte. The full-suite count is hosted evidence. The numerical grid, source inspection, axial and off-axis rays, focused tests, dispatch comparison and archive verification were performed independently. [Optical CI job](https://github.com/physicsvigilante/opticsim/actions/runs/44858841630/job/136707285981) · [Authoring evidence ZIP](https://github.com/physicsvigilante/opticsim/actions/runs/44858841630/artifacts/14688652758)
