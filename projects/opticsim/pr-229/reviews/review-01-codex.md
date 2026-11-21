# Independent Codex review of Opticsim PR #229

**Outcome: pass. No unresolved blockers or demonstrated defects within the frozen study.**

- [Source PR #229](https://github.com/physicsvigilante/opticsim/pull/229), production base `72be0c44c74a24df97b4873978508b645529ae3c`.
- Exact reviewed head `b8263ae4b69afdb3ffe60d08934f0b1798dc7d05`, Git tree `92d85ee85461872800beb017c03d47204defe96b`. [Exact source](https://github.com/physicsvigilante/opticsim/tree/b8263ae4b69afdb3ffe60d08934f0b1798dc7d05)
- Reviewer: independent-in-context Codex agent, 2026-11-21. Scope: Problems-only antecedent, frozen paraxial predictions, genuine spherical-lens and detector callbacks, signed conjugates, evidence and existing contract preservation. No production files changed during the review.

## Source and method

I read only the A29 Problems crop. SHA-256 `d5dedd786f55af52f8b80d4296b53460cddcf2c3520dc27a9e81506bff56bbe5` matches the atlas. A29 asks about a near-normal parallel beam through a solid sphere in terms of refractive index and radius. The finite object distances, differing surface radii and separated doublet in this work are explicit synthetic controls. The frozen bytes match commit `2ed15125359dcac372acd8e33b476dab998a969d` and predate the implementation. Solutions material was unopened. The PR changes only the frozen control, study notes and a test file.

I independently propagated the two ray-transfer basis vectors with exact rational reduced slope. Each spherical interface uses power `(n_out − n_in)/R` with a positive front radius and negative rear radius. The system includes translation through each actual center thickness, the 92.5 mm air gap in the doublet and the declared object distance. In the rear-pole plane matrix, the signed conjugate is `−B/D` and the transverse magnification is `1/D`, as verified by its unit determinant.

| Frozen control | Exact signed distance from last rear pole (mm) | Exact magnification | Largest axial residual (mm) | Largest transverse residual (mm) |
|---|---:|---:|---:|---:|
| Single lens, real | 8800/43 | −48/43 | 0.0154575 | 0.00002809 |
| Single lens, virtual | −4000/59 | 96/59 | 0.00027406 | 0.000000803 |
| Separated doublet, real | 9031350/249121 | −107520/249121 | 0.0027970 | 0.000004249 |

The detector is 25 mm beyond the last rear pole in all three controls. All real intersections were forward from the detector. Every virtual estimate used a backward mathematical extrapolation of the outgoing lines after their real detector crossings. The tabulated values and calculations apply to the 18 sampled pairwise estimates and the frozen tolerances of 0.08 mm axial and 0.001 mm transverse. They do not measure a continuous spot or detect an image.

## Pinned native evidence

I rebuilt PhyDemo `811f508d2b070898c241a568b0c167dcb8645251` in an isolated exact archive. All three study tests and 20 existing thick-lens/preservation tests passed. A separate native callback probe performed all 18 runs using the ordinary schema-v15 SingleRay, one or two SphericalLens objects and a genuine passive Detector. Each ray reached its front and rear arcs in physical order and then reached the detector once. All 66 delegated events matched the exported native face and detector coordinates and directions. Outgoing direction continuity into the following callback agreed exactly at binary64 resolution.

Independently solved the spherical intersections and used tangential Snell refraction for all 48 arc contacts. The maximum component-wise contact residual was `1.28e-13 mm` and the maximum direction-component residual was `2.23e-16`. The 18 predicted detector lines matched measured detector coordinates to `6.27e-15 mm`. Minimum aperture-edge clearance exceeded 12.39 mm, and the smallest pairwise slope separation was `6.1458e-4`. Every run completed with zero truncation, undefined behavior or rim contacts.

## Hosted CI and exact archive

All 11 hosted exact-head PR workflows passed. Optical composition identifies synthetic merge checkout `8d4f0b6be9ab29fce87c796e65f8163e4c886fb3`, its stated base and head, and 1,333 Node tests with zero failures or skips. The independent Git merge-tree computation reproduced the reviewed tree. Existing real Chrome suites passed in hosted CI. The study changes no browser UI. The independent full Windows run had 1,332 passes, zero failures and the expected symlink-privilege skip. [Optical composition run](https://github.com/physicsvigilante/opticsim/actions/runs/44882761061) · [Unified workflow run](https://github.com/physicsvigilante/opticsim/actions/runs/44882761292)

I downloaded the exact-head authoring archive `14698643103` and verified SHA-256 `2fea1e89401343f3536bdc1637f66c4632bf97de80e8cb2cdbc4236377e40629`. All six study JSON files matched the independent Windows replay byte for byte. [Archived evidence](https://github.com/physicsvigilante/opticsim/actions/runs/44882761061/artifacts/14698643103)

The other passing workflow IDs are `44882761049`, `44882761060`, `44882761065`, `44882761084`, `44882761095`, `44882761106`, `44882761125`, `44882761176` and `44882761214`. This clears the exact test-only source for owner-authorized integration. Public authoring and general finite-conjugate numerical claims require their own scope and review.
