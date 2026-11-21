# Opticsim PR #222 independent focused review R2

**CLEARED for owner-authorized integration at this exact candidate.** All three represented-geometry blockers are resolved.

| Identity | SHA |
|---|---|
| Candidate | `e07b3880cd71204b6d7ccc5486d32f18ff9bf736` |
| Candidate tree | `7fb2a792d398a549aef03b4f0a42245925784f1b` |
| Production base | `8991e8c4c8dc2f1b26999f5ea7bffb5f84acb64f` |
| GitHub PR test merge | `83c45b34317eb86a180070f6927ff0eb617e3b50` |
| PhyDemo pin | `811f508d2b070898c241a568b0c167dcb8645251` |

The PR test merge has the reviewed candidate and base as parents and exactly the candidate tree. [Original blocked review](https://github.com/physicsvigilante/review_sandbox/blob/d624db3cfbc79fc44f77378d4990b20d5d12a842/projects/opticsim/pr-222/reviews/review-01-codex.md).

## Source and geometric qualification

I independently viewed the original A04 Problems image. SHA-256 `ec0d4946a67825e5df7df46eb97940864c4217ce38d74f0d3f1352da08d6e4db` matches the frozen record. Solutions stayed unopened. A and B lie in the drawing plane and the ray must reflect once from each of the four straight walls. The image supplies no numerical dimensions. The public input therefore keeps the answer symbolic. Under the stated ideal specular model, each axis crosses exactly two alternating walls, leaving the final sign of each velocity component unchanged. The four translated copies B+(±2W,±2H) exhaust the possible unfolded directions. Each admissible reversed journey uses the negative final direction and reverses the contact order.

The corrected numeric query sorts exact represented crossing parameters and excludes equal-time corner ties. Fixed contact coordinates are exactly at their authored wall planes. The code tests the strict 1e−10 clearance band on original exact contacts, on the serialized along-wall coordinates, and on the exact-rational trajectories of both public binary64 headings. The prior out-of-box witness now has exact wall coordinates. Both rounding-boundary witnesses withhold their direction and contact fields. Partial coverage retains clear branches while exposing unresolved ones.

I independently enumerated all 24 wall permutations over 113 rectangles in mm, cm and m, using rational reflections and event propagation in the physical box. The 2,712 permutation controls established the four-copy candidate completeness away from corner ties. Across the represented branches the review found 443 qualifying routes, seven withheld near-corner branches and two exact corner ties. I traced every accepted heading in both directions and checked 3,544 contact positions for the correct order, exact fixed coordinate and adequate represented corner clearance. Qualified reverse results agree with a fresh request using the endpoints exchanged.

## Native controls and hosted evidence

The eight separate pinned PhyDemo controls use one genuine SingleRay, four real finite mirrors and an opaque native Blocker. Each observed four actual reflections in the expected order and the final actual absorption at the recorded target coordinate. Minimum measured corner clearance was 1.5384615 mm. The reversed runs independently reverse the wall order. Lower processed-limit runs stop before any absorption. Test-only corner gaps and the finite absorber qualify these chosen runs. The public query remains conditional analysis and requests no native scene.

The independent Windows run passed 31 focused tests using relative test entry paths, including A04, inherited A08 and the A07/A09 tests. The normal A04 CLI produced its symbolic conditional result with native status `not-run`.

All 11 exact-head hosted workflows passed. [Optical composition job](https://github.com/physicsvigilante/opticsim/actions/runs/44873856195/job/136754104335) passed 1,299 Node tests. The [exact-head authoring archive](https://github.com/physicsvigilante/opticsim/actions/runs/44873856195/artifacts/14695086838) matched SHA-256 `f528ba81e3a76170b562f2d429967a1dc1683088fb894b93d574a1bb070a6ed7`. I compared all 35 scoped records byte for byte, comprising four A04 symbolic query files, eight A04 native records and 23 inherited A08/A07/A09 records.

The verdict applies to the exact reviewed source. Integration and verification of the merged tree remain separate checks.
