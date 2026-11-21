# Chat B review of the three-thermometer inverse

**Verdict — accepted for the stated offline local-curvature scope.** No blocking findings. Reviewed base `d6b0b9ae7ce792097566f427d2202b03d1bfd9c6` and head `338f4a30f241d743972ad05fadd3f52b0b2f7121` against packet `da960af34e954ccfa5a7619da22791a3bc9d1f1d`. This was a separate reviewer-agent evaluation. [Source diff](https://github.com/physicsvigilante/sim_heat/pull/169/files)

## Independent reference

With axial position expressed as a fraction of rod length, the steady one-dimensional balance gives the quadratic coefficient of temperature as −P/(2G), where P is total rod generation in watts and G = kA/L is in W/K. The facing rod facts give G = 4 W/K. I obtained the quadratic coefficient by Lagrange interpolation, independently of the implementation's adjacent secants. At fractions (1/8, 3/8, 7/8), the coefficients mapping temperatures to power are (−128/3, 64, −64/3) W/K. The negative outer coefficients and positive middle coefficient determine the worst-case temperature choices.

For independent bands [365,366], [380,381], [370,373] K, I evaluated all eight rational corners and obtained [2240/3, 2752/3] W. I supplied the readings to the candidate in reverse spatial order. My initial assertion of exact equality failed because the implementation rounds its interval endpoints outward. A subsequent exact rational comparison confirmed enclosure at both ends, each with excess below 10⁻⁸⁵ W. The three supplied thermometer tests also passed independently against a Git archive of the head.

## Refusals and interpretation

I observed refusals for an unknown rod, coincident positions, a negative position, a position above one, reversed temperature bounds, an interval admitting both signs of curvature, and a mismatched facts digest. The uncertainty computation retains the shared central reading in both secants. A nonnegative interval can include zero. Three readings alone cannot establish that generation is uniform, that the rod is steady, or that its temperature profile agrees with other components or boundaries. The emitted scope conditions the power inference on the local model. Close probe spacing amplifies temperature uncertainty, as the position-dependent coefficients predict.

## Evidence

I downloaded the CI ZIP and independently obtained SHA-256 `92c5145a242e1cad02b8b6f97fd11f1265f4647db9e82caa9f303c8c0f6158f2`. Embedded head matched the reviewed SHA and the archived regression log recorded 243 passing tests. The replay reports G = 4 W/K and [288,352] W, as predicted by multiplying the midpoint excess of [9,11] K by 8G. Native execution, native qualification, independent reference certification, and runner consumption flags are all false. The review covers an offline inverse and provides no native observation or qualification. [Pinned CI job](https://github.com/physicsvigilante/sim_heat/actions/runs/44907141001/job/136855030482) · [Evidence archive](https://github.com/physicsvigilante/sim_heat/actions/runs/44907141001/artifacts/14708546248)
