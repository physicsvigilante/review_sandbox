# Independent Codex review of Opticsim PR #207

**CLEARED FOR OWNER DECISION.** I found no blocking issue in the frozen A12 assumptions, six native controls, or the treatment of position and magnification. The evidence qualifies a test-only composition.

| Identity | Reviewed value |
| --- | --- |
| Candidate | `22349194e525219cf634cfadbfbc88f8014a3535` |
| Tree | `d30bd55e31b1d01e878d974b134135c012810c61` |
| Base | `23168ed96d3588dd47386f24724518b4e884d9f4` |
| CI merge | `8ea4de5b517fae0645de5090cd7ef0b8c15c6393` |
| Frozen protocol commit | `2b05d942141ff92198985bc4d4fcc8b3eb4f2ef7` |
| Frozen protocol blob | `73a7770e0ea6c6b67d9d44c5e349668a9ccbb447` |
| Native test blob | `290eea285b4847527756274584b6854849fedb57` |
| PhyDemo pin | `811f508d2b070898c241a568b0c167dcb8645251` |

## Source and paraxial comparison

I inspected the Problems entry A12 at `08_Ray_Optics_Explanations/03_General_Refraction/Problems/003.png` and verified its SHA-256 `d98c8b3aa6086b340c3d038d9821baf4be516bec27eb7892b94286bc7bed170d`. It specifies a 20 cm concave spherical radius, a 30 cm axial object distance and insertion of a 6 cm parallel slab of index 1.5 between the object and the centre of curvature. The exact axial placement, unit-index exterior, probe height, source emission, mirror aperture and detector are study assumptions. Both slab placements keep both faces between the object and the centre of curvature.

The chosen model uses reduced propagation through the slab before reflection. In millimetres, the effective object distance is 300 in the baseline and 300 − 60(1 − 1/1.5) = 280 with either slab placement. For focal length 100 mm, the real image falls 150 mm or 1400/9 mm from the mirror, with signed magnification −1/2 or −5/9 respectively. The resulting image planes lie before the returning ray re-enters the slab. The predicted image moves 50/9 mm away from the pole and grows by a factor of 10/9. The source leaves absolute object height unknown.

## Native evidence

I rebuilt the isolated candidate with the pinned core and reproduced all six native tests. The experiment uses an AngleSource, ArcMirror, Detector and, where applicable, two PlaneGlass components. Instance observers preserve each native call and the native ray object. Warning-free completion is required before interpreting observations. Three samples in each of six runs provided 18 actual rays and 102 native contacts. An independent check of the recorded native lines, contact positions, spherical normals and return directions found maximum line and arc residuals below 6 × 10⁻¹⁴ mm and reflection and observable Snell residuals below 7 × 10⁻¹⁶. Comparing actual returning detector line intersections with the independent paraxial result gave maximum residuals of 0.031694 mm axially and 0.000422 mm transversely.

These are finite sampled controls of the two-dimensional geometry. The intersections are computed from returning detector measurements and retain finite-aperture deviations. The candidate changes only the frozen protocol and native test.

## CI and archive

All 11 workflows passed on the candidate. The optical composition run passed 1,223 Node tests and its real Chrome acceptance. Its checked-out merge has the same tree as the candidate and the expected two parents. [Optical composition run](https://github.com/physicsvigilante/opticsim/actions/runs/44861009650)

I independently downloaded archive 14690355333, verified SHA-256 `25796c374970e29a81fca501a253df1af6cc3f08531b72eec354376d0fc1d648`, and matched all six archived native observations to my local rerun byte for byte. [Authoring evidence archive](https://github.com/physicsvigilante/opticsim/actions/runs/44861009650/artifacts/14690355333)
