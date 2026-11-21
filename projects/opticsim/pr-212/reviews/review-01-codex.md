# Independent Codex review of Opticsim PR #212

**CLEARED FOR OWNER DECISION.** I found no blocker in the conditional mirror and plane conjugates, their numerical qualification, or public dispatch.

| Identity | Reviewed value |
| --- | --- |
| Candidate | `bf188bbb7911c044e6d89222f13c10c0ae2d398f` |
| Tree | `7a5144ae5e88fbb0ce1aa82af21fa88b523004f8` |
| Base | `6b3490e44f964f63e773961db9c410f7680f9f80` |
| CI merge | `45f8b10f06d17599d648f6d4c03e4469e48259c2` |
| Freeze commit | `a2bb444b40bd95cfba251fc67df8038ab950bb7d` |
| Frozen protocol blob | `d5b29985b1709c83084fffff6fca7131893a3097` |
| Analytical source blob | `28302874005d2be4b3b066a2d6583b6947df6f7f` |
| PhyDemo pin | `811f508d2b070898c241a568b0c167dcb8645251` |

## Source and conditional coordinates

I verified the A28 Problems image SHA-256 `2f95c58717b644ca282fc22957899410c3e3c02d2c753eabfaa815682728380c`. Its hemisphere radius is 10 cm and glass index is 1.5. The curved face is silvered and the axial bubble is 5 cm from the plane. The public request states the added point-scatterer, paraxial and unit-index exterior assumptions. With the plane as origin and the positive axis into the body, the direct conjugate is a virtual depth of 10/3 cm. The singly reflected conjugate is afocal at the mirror focal setting. A finite reflected interior continuation at signed coordinate s gives the exterior conjugate at s times the exterior/interior index ratio. Negative depth is exterior real, positive depth is apparent into the medium, and zero is the exit plane.

I used an independent two-slope propagation from the axial point through the mirror and exit plane across 34,560 valid combinations of pole, object, curvature, unit and indices. Of the reflected results, 31,440 were virtual, 2,580 exterior real, 340 afocal, 80 exactly at the exit plane and 120 withheld because of numerical qualification. The direct branch remained available across these 120 cases. The maximum finite position discrepancy against the independently intersected lines was 3.4 × 10⁻⁷ mm. The maximum line-height residual at the reported position was 5.9 × 10⁻¹¹ mm. Exact focus and plane equality, both near-boundary guards, coincident geometric conjugates and unsupported reflector contact were independently checked. Sign is preserved by positive material scaling.

## Integration and evidence

All 49 prior public example inputs and plans matched the base. I independently exercised mixed requests through the CLI in both directions. A v31 native scene retained all four qualified observations alongside the two incompatible analytical requests. Reduced A28 facts retained both conditional analytical results alongside the native-scene-required diagnostic. The new public A28 evidence records no native run. Its six separate, unchanged native controls provide finite geometry for the selected paths. I reran all six in the exact candidate and checked their 45 actual callbacks and signed finite or focal residuals.

The isolated candidate passed 29 focused tests. All eleven hosted workflows passed on the candidate tree and expected parents, including 1,241 Node tests and the v30 and v31 real Chrome suites. The four analytical records and six prior native control records in the hosted archive matched my isolated runs byte for byte. Archive SHA-256 is `30be45ce580f9cdf71f79c0ac8a0168992fa80f8bbde5add71993d9bebc24ec0`. [Optical composition run](https://github.com/physicsvigilante/opticsim/actions/runs/44864939581) · [Evidence archive](https://github.com/physicsvigilante/opticsim/actions/runs/44864939581/artifacts/14691730959)
