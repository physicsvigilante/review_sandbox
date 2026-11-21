# Independent R2 review of the radiating-wall probe

**Disposition.** Clear for the offline steady-conduction observation at source head `d93914eb6b00b87d6956bd25d2daddcd1c91395b`. I found no blocking or major defect in the reviewed change. Base `338f4a30f241d743972ad05fadd3f52b0b2f7121`. [Review packet](https://github.com/physicsvigilante/review_sandbox/tree/39a867fb99a6c94c202ed76a5ae3821d49e99dea/projects/sim_heat/pr-170) · [Source diff](https://github.com/physicsvigilante/sim_heat/compare/338f4a30f241d743972ad05fadd3f52b0b2f7121...d93914eb6b00b87d6956bd25d2daddcd1c91395b)

## CI and archive

All listed steps of job 136855971128 succeeded. I downloaded artifact 14708890440, computed its SHA-256 as `9981bae97f564c20bc8b9c94a8319cbd2893deea2c244efebedf78f0be5cefcf`, verified ZIP integrity and checked head.txt against the full head above. The archived log records 244 passing tests. Running the archived wall case on a fresh Git archive of the pinned tree reproduced the complete parsed radiating-wall-probe.json. Six focused powered-wall and rod-generation unit tests also passed locally. [CI job](https://github.com/physicsvigilante/sim_heat/actions/runs/44907454380/job/136855971128) · [Archive](https://github.com/physicsvigilante/sim_heat/actions/runs/44907454380/artifacts/14708890440)

## Independent physical case

I used the pinned composite wall, generated 80 W uniformly in the insert and released the cold port. I selected enclosure 300 K, air 450 K, surface area 0.2 m², emissivity 1, sigma 5×10⁻⁸ W/(m² K⁴), and h = 15.5 W/(m² K). The facing, strip and insert conductances are 4, 1 and 3 W/K. At a trial surface of 400 K the joint balance gives (4×380 + 4×400 + 40)/8 = 395 K. The surface receives 40 + 4×(395−400) = 20 W from the rods. Radiation removes 175 W and air contributes 155 W, closing the exterior balance at 400 K. The maintained hot bath supplies −60 W, closing the whole-network balance with the 80 W source.

The insert runs from outside to interface. At a quarter of its length its temperature is 400 − 5/4 + (80/6)×(1/4)×(3/4) = 401.25 K. Fourier heat current toward the interface is 3×(400−395) + 80×(1/4−1/2) = −5 W. An independent exact-fraction check found all eight expected values inside the reported intervals, each narrower than 10⁻¹² in its reported units. The returned endpoint names agreed with the physical orientation.

## Controls and scope

Code inspection confirmed that the calculated surface interval replaces the released node's fixed temperature before solving the network profile. The fraction is interpreted from the selected rod's a endpoint. The probe call reproduced every profiles-only field. Dropping the two profile fields from profiles-only output reproduced the default no-probe result. The API refused an unknown rod and the fractions `-1`, `1.01`, `1/2` and `NaN`. The new case returned false for nativeExecuted, nativeQualified, independentlyCertifiedReference and runnerConsumable. The exact-head diff leaves the native paths untouched. This review establishes an offline result on the pinned illustrative wall. Native qualification and release decisions remain outside this finding.
