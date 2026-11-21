# Opticsim PR #219 independent review R1

**BLOCKED at exact candidate `54259ecfe948f6e389d08314ae4ebd6938d3aa0c`.** The public numerical polygon accepts distorted image outlines in two reproduced cases.

| Identity | SHA |
|---|---|
| Candidate tree | `8d700d1b15eea7b0fe6348f884a9aed1682e25ac` |
| Production base | `3f8e800f0be6e48a99419fe6aa21e542b176d0f0` |
| GitHub PR test merge | `4a4ca7870fd3322cde6797c2de179504377c0383` |
| PhyDemo pin | `811f508d2b070898c241a568b0c167dcb8645251` |

The synthetic merge has that base and candidate as its parents and exactly the candidate tree.

## B1 — conditioning of projected outlines

Both witnesses are triangles in millimetres with three distinct IDs. Input and returned winding checks pass, while the reported local geometry is distorted.

- **Near-focus ratio cancellation.** Use f=1400 and A=(1402.0000000000007, 0), B=(1402.000000000001, 1.5916157281020816e−10), C=(1402.0000000000011, 0). The exact axial offsets of B′ and C′ from A′ are approximately −1.1141310e−7 and −2.2282620e−7. These offsets are hundreds of binary64 steps at the image coordinates. The historical point solver first rounds u/f and then subtracts one. This gives A and B the same rounded ratio. The outline is marked conditional with A′ and B′ at exactly the same axial distance. The projected triangle loses its nearly symmetric placement despite the local axial offsets being representable.
- **Absolute image coordinates too coarse for the outline.** Use f=1 and A=(9000, 0), B=(9000.000000003, 8e−13), C=(9000.00000003, 0). The analytic offsets are approximately −3.704e−17 and −3.705e−16. B′ therefore lies at about 10% of the projected axial span from A′. Returned binary64 absolute coordinates put B′ halfway across the span. Stable dimensional arithmetic alone does not resolve this example.

Use the represented dimensional difference u−f for the new outline. Compute the offsets and conditioning without losing the projected geometric scale, and withhold an outline when its absolute coordinate representation cannot resolve its local shape. Retain the historical single-point query behavior and add regressions for both triangles.

## Source, optics and positive controls

- I independently viewed the original A09 Problems image. Its SHA-256 `073a971a9eaca6a664e6f509e8b3d6e4428cd736ad80fe81b0fa0bc8e2092947` agrees with the frozen source record. No Solutions entry was used. The image shows A and D on the axis, two transverse end edges, the taller end closer to the mirror, and the object beyond the centre of curvature. These relations imply the inverted trapezoid, farther D′, longer D′E′ and interval between focus and centre. No drawing dimensions enter the calculation.
- For a convex outline with all u>f, the projective point transform has one positive denominator throughout each edge and interiors, and the signed area orientation is preserved. The normal public CLI returns a conditional qualitative result with no native run and includes its finite illumination and visibility limitations. In a mixed request, an absent detector remains unavailable while the conditional shape is retained.
- An independent replay passed 360 ordinary numerical cases and checked 1,620 projected edges across both winding orders, three to six vertices, three units and focus ratios from 1.005 through 3.5. Maximum residual against an independently evaluated dimensional coordinate was 6.06e−9 mm and against straight-line projective interpolation was 1.46e−8 mm. These controls do not address the small-scale witnesses above.
- Sixteen focused Node tests passed, including four distinct v6 native source trials. Each trial recorded three emitted rays, a genuine mirror reflection per ray, and three incoming and three outgoing detector callbacks. Pairwise returning-line intersections lay within 0.063399 mm axially and 0.001163 mm transversely of the conditional point locations. Those finite source tests do not measure the image of a full polygon or observer visibility.

The numerical blocker prevents integration of this exact candidate. A corrected head needs focused verification and hosted CI.
