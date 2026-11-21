# Opticsim PR #218 independent review R1

**BLOCKED at exact candidate `ddcd4463c32ffe1f453695a6bb493060756f30e3`.** The native audit can accept a reflection on the un-authored half of the backing circle.

- Candidate tree `6ae9e14330f0ae80b1841e9f048eb6359c44fdc0`.
- Merged base `f6fa244f58993e2e741561d3395b91eb015d7314`.
- Synthetic merge `3e30b8ed82edca52ecd0d5208fe2b50a0a0094e3` has the exact candidate tree and the candidate and base as parents.
- PhyDemo pin `811f508d2b070898c241a568b0c167dcb8645251`.

## B1 — full-circle membership admits a reflection outside the declared minor arc

The native audit accepts an actual callback that matches the full circle's normal, a radial distance and the finite y rim. The opposite half of that circle has the same radius and y range, but the versioned mirror is only the minor arc near the right-hand pole.

I authored a valid v34 scene with a source at x=50 mm, an exit plane at 0, a 50 mm radius mirror with pole x=200 and 30 mm aperture, a unit-index exterior and 1.5 interior, and a 100 mm detector centred on the axis at x=−15. Genuine PhyDemo callbacks reported the three qualifying reflections at the intended patch. I then wrapped the real `ArcMirror.checkRayIntersects`, delegated it exactly once, and substituted the other forward circle root each time it reported a true patch hit. The genuine `ArcMirror.onRayIncident` and all other native handlers were left in use.

v34 still reported three qualified samples and `v34ImmersedArcVerified:true`. The detector y coordinates changed from approximately −15.160, −3.024 and 9.080 mm to 6.565, 1.312 and −3.936 mm. The faulty mirror samples were near x=100 instead of x=200. These are deliberate contradictory callbacks. They do not show a general defect in the pinned implementation.

Both shared callers use left-facing concave minor arcs with the centre to the left of the pole. Require positive radial x with the existing circle, rim and reflection checks. Add the opposite-branch native mutation as a regression.

## Independently replayed positive controls

- The original A28 image matches its frozen SHA-256 `2f95c58717b644ca282fc22957899410c3e3c02d2c753eabfaa815682728380c`. It describes a 100 mm radius silvered hemisphere, index 1.5, and an air bubble 50 mm from the plane. v34 clearly authors a half-space, a single finite immersed mirror patch, a sampled source and an exterior detector. The independent A28 conjugate query and original data remain separate.
- I recorded the genuine chronological callbacks of 702 native rays across 216 v34 and 18 v31 configurations. The v34 set included direct sources in both equivalent axial headings and singly reflected sources, four world offsets, three radii/index ratios, both detector orientations, and three axial depths per geometry. Independent finite circle reflection and planar Snell calculations agreed within 1.40e−8 mm in position and 1.03e−11 in unit direction. The A28 finite-ray line intercepts agreed within 0.007713 mm of their separate paraxial values and the focal-setting residual slope was at most 7.27e−7.
- v31 retained actual front/rear/detector/mirror/detector/rear/front sequences. Native detector increment signs reversed between each leg at both detector orientations and densities 0.95, 0.97 and 1. Each sample used the genuine authored-channel brightness.
- Independent real Chrome passed all seven v34 checks and all seven v31 checks. This blocked verdict is based on the contradictory exact-source native control, regardless of hosted test results.

No merge is cleared for this exact source. A corrected exact head requires focused verification and hosted evidence.
