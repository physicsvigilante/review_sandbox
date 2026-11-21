# Independent Codex review of Opticsim PR #211

**CLEARED FOR OWNER DECISION.** I found no blocker within the test-only scope of the A28 direct and silvered-return controls.

| Identity | Reviewed value |
| --- | --- |
| Candidate | `896d1044971b50b32968cbedf53ef18f74913067` |
| Tree | `909073479240f1db09d34110305a5e266421a882` |
| Base | `ed19df1d0d18e34cbfb73681d05889db1a06370a` |
| CI merge | `7cb7de45a93fa5a920d79ae201ea3d364b946a77` |
| Freeze commit | `66bc5d5a567c2eed0f29f40e2ddedaa3d9a3cb4e` |
| Frozen protocol blob | `3980698ce81ce2197f2768c1347a2d5e0d6834e8` |
| Native test blob | `9119e625ce436ce1d02261ded62029c3baba63c7` |
| PhyDemo pin | `811f508d2b070898c241a568b0c167dcb8645251` |

## Source and scope

I inspected A28 at `08_Ray_Optics_Explanations/06_Refraction_at_Curved_Surfaces/Problems/007.png` and verified SHA-256 `2f95c58717b644ca282fc22957899410c3e3c02d2c753eabfaa815682728380c`. The source gives a silvered glass hemisphere of radius 100 mm and index 1.5, an axial air bubble 50 mm from the flat face, and observation through that face. The study represents the bubble as a point probe, assumes unit-index exterior, and qualifies two selected near-axis paths separately. The 25 and 75 mm depths, angular cone, relative brightness, detector, numerical density and finite mirror aperture are controlled choices. The candidate diff contains only the protocol and the native test. The publicly supported v30 and v31 compositions retain their own boundaries.

With the flat face at x = 0 and positive x into the body, the direct apparent depths are 50/3, 100/3 and 50 mm. The reflected bundle first forms a paraxial conjugate with mirror focal length 50 mm. The plane exit then scales its signed axis position by the inverse index ratio. The reflected outputs are real at x = −100/3 mm for depth 25 mm, paraxially afocal for depth 50 mm, and virtual at x = 100 mm for depth 75 mm. These are geometric extrapolations. The study supplies finite ray geometry and separate residuals at the focal setting.

## Native and CI evidence

I rebuilt the isolated exact tree from the pinned PhyDemo core and passed 27 focused tests. All six runs used actual AngleSource, ArcMirror, Detector and PlaneGlass objects. The mirror and plane remained different, separated native components. Across 18 emitted samples and 45 actual callbacks, the direct runs gave plane and detector encounters in order, and the reflected runs added a first mirror encounter. All completed without warnings, truncation or undefined behavior. An independent vector check confirmed continuity and local reflection and refraction. Mirror contacts stayed within 1.179 mm of the axis on the positive-x spherical patch. Maximum finite intercept deviation was 0.007713 mm, and maximum absolute focal-return slope was 7.268 × 10⁻⁷. These bounds establish the measured near-axis behavior for the chosen patch, with finite spherical aberration.

All eleven workflows passed on the candidate tree and expected merge parents. Optical composition passed 1,238 Node tests and the existing v30 and v31 Chrome qualification suites. The six native archived records matched my isolated run byte for byte. I verified the archive SHA-256 `caa8b6b4dfe0f7bd45f3ad646d56b1e3b4282b54af0432ee80d3a3cea8604fcf`. [Optical composition run](https://github.com/physicsvigilante/opticsim/actions/runs/44864482973) · [Native evidence archive](https://github.com/physicsvigilante/opticsim/actions/runs/44864482973/artifacts/14691680501)
