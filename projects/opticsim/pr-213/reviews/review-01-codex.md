# Independent Codex review of Opticsim PR #213

**CLEARED FOR OWNER DECISION.** I found no blocker in the frozen test-only A27 cap geometry, the nearby interior controls, or the signed observer-distance comparison.

| Identity | Reviewed value |
| --- | --- |
| Candidate | `06c5b3d296788c0a7b20018ccbc72c0731bec6b4` |
| Tree | `3d5d618793af157e2d591b834055f30bf319b9dc` |
| Base | `154ef86a5a9cfb5cda98d00716a95a42b605f867` |
| CI merge | `14fe3a975b06e83267146258f27d1042f302052b` |
| Protocol freeze | `85ecb1873d0db81c9cd44579fb4434309018487f` |
| Frozen protocol blob | `2eb90294348a3549c2e127a1a170cafe1ac216ba` |
| Test blob | `feb4e3337bc37c4165c7edfad136546333913719` |
| PhyDemo pin | `811f508d2b070898c241a568b0c167dcb8645251` |

## Source and geometric distinction

I inspected the Problems-only A27 image `08_Ray_Optics_Explanations/06_Refraction_at_Curved_Surfaces/Problems/004.png` and verified SHA-256 `e0b938a74df9e6d302ee63a259164b9cfe31fe65b01a93e708774a3e5b404989`. The illustrated cap is 3 cm high, cut 2 cm from the centre of a 5 cm sphere of index 1.6. The axial observer is 8 cm above the table. The external index of one and paraxial approach from the glass side of the base are explicit study assumptions. The shallow cap, finite probe offsets, cone, detector and brightness are separate controls. The candidate changes only the frozen protocol and test.

The pinned Glass uses a true arc through the pole and retains the chord closing the base. Its spherical centre lies at height minus radius, and its chord half-extent is the square root of h(2R−h). I checked the retained chord with an independent native leftward experiment for each cap, with three real chord exits and three exterior detector crossings per run. The intended rightward experiments instead measure transmission at the arc. All probe x values remain strictly inside, separate from the base. The observer position denotes the plane carrying a passive detector. Signed back-extrapolation from its actual sampled lines provides a geometrical comparison.

## Native and numerical evidence

I rebuilt the isolated candidate from pinned PhyDemo and passed 39 focused tests. Independent circle intersections and vector Snell reconstruction verified 18 rays and 36 actual arc/detector contacts. The maximum arc-coordinate residual was 1.1 × 10⁻¹⁴ mm, the largest outgoing direction vector residual was 2.3 × 10⁻¹⁶, and the largest observed-plane ordinate residual was 4.3 × 10⁻¹⁵ mm. Independent stopped controls terminated before a detector crossing in both caps.

Using the small-slope exit refraction relation, the zero-probe limits are 74.193548 mm from the observer for A27 and 56.326531 mm for the shallow control. The maximum error against the model at each actual probe offset was 0.000712 mm. As the offset decreased from 1 to 0.25 to 0.0625 mm, A27's maximum distance from the mathematical limit fell from 1.03126 to 0.26014 to 0.06561 mm. The corresponding shallow-cap errors were 0.86437, 0.21713 and 0.05485 mm. These results corroborate a limit of the chosen geometrical model using finite native rays. Table illumination and observer visibility are outside the study.

## CI and archive

All eleven hosted workflows passed. The optical composition job checked out the matching tree and expected merge parents, passed 1,243 Node tests, and ran existing v30 and v31 real Chrome qualification. The v30 Chrome checks also passed independently. The six native archive records matched my isolated runs byte for byte. I verified archive SHA-256 `0de5f8942e664098a6ceae899b4c68c0dbc90b031cc86d3b2da72763052cd83e`. [Optical composition run](https://github.com/physicsvigilante/opticsim/actions/runs/44865692517) · [A27 evidence archive](https://github.com/physicsvigilante/opticsim/actions/runs/44865692517/artifacts/14692275583)
