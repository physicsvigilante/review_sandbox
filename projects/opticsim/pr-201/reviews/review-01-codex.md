# Independent Codex review of Opticsim PR #201

**CLEARED FOR OWNER DECISION.** I found no blocking issue in the signed paraxial result, its numerical guards, the public dispatcher or the native comparison.

| Identity | Reviewed value |
| --- | --- |
| Reviewer | Codex, independently assigned by the owner |
| Head | `7487e981b35166f2366409afac02f73919e428db` |
| Tree | `59ee2ab342efb0f8de83504624271a561f60cd96` |
| Base | `43ce9d0c00d207abc4837bfa56a7e4ceb4db9f37` |
| Protocol commit | `fe8cea9a7303bc2a0cd03d99be03457472be582d` |
| Native control commit | `4e6bfbf8fbcf4d2da89a2eff964875805f22815d` |
| Pinned PhyDemo | `811f508d2b070898c241a568b0c167dcb8645251` |

## Source and interpretation

I read A29's Problems PNG. It gives a parallel beam near normal incidence, a solid sphere of radius R, and the sphere index μ. It supplies neither an exterior index nor a distance origin. The example explicitly assumes a common exterior, uses m = nCore/nExterior, and labels the centre and rear-pole results. The PNG SHA-256 matches the freeze at `d5dedd786f55af52f8b80d4296b53460cddcf2c3520dc27a9e81506bff56bbe5`. The protocol preceded the native control, which preceded the implementation. Their unchanged Git blobs are `aa246de38c5a4903ea709c924d10614d85f2fb0e` and `290316d1c44c61ef003d6b1e359537ae468c4acf`, respectively. [Frozen protocol](https://github.com/physicsvigilante/opticsim/blob/fe8cea9a7303bc2a0cd03d99be03457472be582d/evaluation/two-surface-paraxial-focus-v1/frozen-protocol.json)

## Reviewer results

I rebuilt the pinned native core in a disposable export with the nine changed files restored from the reviewed Git blobs. All 59 focused tests passed. I also performed the following independent checks.

- **Signed paraxial physics.** I propagated a parallel unit-height ray using the signed local normal and linearized Snell refraction at each surface, then found the axial intercept of the outgoing direction. I compared the public result for 9,216 combinations of absolute indices, signed front and rear curvatures, positive axial thickness and units. The 9,213 qualified results comprised 3,534 downstream, 4,776 upstream, 288 rear-pole and 615 afocal states. Three near-degenerate represented cases withheld a value. The signed distances and dioptre powers agreed within scaled tolerance 10⁻¹⁰ for all qualified cases.
- **Sphere and asymmetric examples.** Substituting front radius +R, rear radius −R and thickness 2R gives rear distance R(2−m)/[2(m−1)]. Adding R gives the centre distance Rm/[2(m−1)]. Matched indices gave afocal output, and m = 2 gave a rear-pole focus. The explicitly asymmetric +120/−80 mm example gave 2720/29 mm behind the rear pole and 10.0694444444 D. The public CLI returned conditional analytical evidence with zero native calls for both examples.
- **Numerical boundaries.** The integer polynomial uses a common binary scale sufficient for every admitted binary64 radius, thickness and material index. It distinguishes represented zero system power from a near cancellation and exact zero ray height from a numerical near miss. I probed both sides of m = 1, m = 2, exact zero composite power and zero height. Nearby inputs withheld values, as did a general conjugate above the 1,000,000 m cap. The symbolic form remains available with symbolic facts.
- **Native corroboration.** I reran the frozen v23 CircleGlass and v15 SphericalLens controls. The two measured circle slopes gave rear intercepts of 199.99349 mm versus the 200 mm paraxial prediction. Four asymmetric-lens intercepts ranged from 93.77415 to 93.78837 mm versus 93.79310 mm. I then independently tested four other 300 mm-radius sphere configurations, including upstream extrapolations for core/exterior ratios 2.5 and 5/6. Eight native detector events agreed within 0.031 mm. Three further asymmetric native lenses, including an exterior index of 1.25, gave 12 detector directions and one event at each named curved face per ray. Their largest intercept discrepancy was 0.023 mm. These are finite-height measured directions. The stated focal positions are extrapolations.
- **Historical dispatch.** I compared complete pre-execution plans, including diagnostics and native readiness, for all 39 pre-existing public problem examples against the base-equivalent PR #200 export. All matched. The two-surface family is discoverable in public method suitability. Native geometry policies, historical core and historical evaluation records have no delta in this PR.

## Exact-head hosted evidence

All eleven pull-request workflows succeeded. The optical job logged 1,186 passing Node tests, including the v23 sphere and v15 asymmetric native controls. I verified the downloaded authoring ZIP against its SHA-256 digest `ae778b83aac0cd91cdadbdd072008ccf7bd11cd58c8b4c305dcecd5083cd6a5e`. All ten two-surface files matched independently produced bytes, including both native summaries and four public analytical files per example. The full-suite count is hosted CI evidence. The focused suites, additional native trials, dispatcher comparison and paraxial grid were executed independently. [Optical CI job](https://github.com/physicsvigilante/opticsim/actions/runs/44855653387/job/136697119733) · [Authoring evidence ZIP](https://github.com/physicsvigilante/opticsim/actions/runs/44855653387/artifacts/14687671535)
