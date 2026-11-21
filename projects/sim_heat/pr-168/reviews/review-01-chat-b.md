# Independent R2 review of SIM_HEAT #168

**Pass for the offline rod probe.** No demonstrated code defect. On 2026-11-21 I reviewed the four-file diff as a fresh Chat B reviewer, verified base `10d2a04d22c16cf498f4e0e4428911c16eb64413`, head `d6b0b9ae7ce792097566f427d2202b03d1bfd9c6` and packet `38c7ab0c354feb2c6bdc6ec7d28b9f7789d63766`. I made no source changes. [Source diff](https://github.com/physicsvigilante/sim_heat/compare/10d2a04d22c16cf498f4e0e4428911c16eb64413...d6b0b9ae7ce792097566f427d2202b03d1bfd9c6)

## Independently executed physics checks

In the steady bridge with facts SHA-256 `4cc763729e8d71b0abfc0eb5d1c3cc4d08185225104af8640541adcfdbf10bbf`, I heated the feed at 28 W and link at 70 W. Balancing half-source injections gives 5u − v = 49 and 3v − u = 35 for rises above 330 K. The link runs from upper at 343 K to lower at 346 K with conductance 1 W/K. Integrating Fourier conduction gives T(x) = 343 + 3x + 35x(1−x) K and Q(x) = −38 + 70x W toward lower.

| Fraction from upper | Expected temperature (K) | Expected current toward lower (W) |
|---|---:|---:|
| 0 | 343 | −38 |
| 1/8 | 22221/64 | −117/4 |
| 3/5 | 1766/5 | 4 |
| 1 | 346 | 32 |

All eight exact targets fell within reported intervals narrower than 10⁻¹² in their respective units. Orientation labels matched the facts. The endpoint current difference equals 70 W. The temperature expression weights endpoint temperatures and curvature with nonnegative factors on the admitted domain. The current expression applies interval multiplication to the signed endpoint difference.

## Refusals, compatibility and provenance

A missing rod and positions −0.001, 1.000000000000000001, NaN and 1/2 raised ValueError under the unsigned decimal grammar. Five focused tests passed. For the two-source bridge I compared generation-only and peak-profile outputs against a Git archive of the base. Both matched in full. Removing the probe field reproduced the head's peak-profile result for every position checked. Native execution, qualification, reference certification and runner eligibility flags all remained false.

My first local launch failed before importing the candidate because temporary paths differed between sandbox processes. I then executed the checks from an isolated archive of the pinned head at a stable path.

## CI evidence and release scope

Job 136854090306 succeeded. I downloaded artifact 14708008504 and verified its ZIP SHA-256 as `7069db4cf5dc1a2c117ceaff762b9cded66114cf8a40a6785e8b79bc842f9ce5`. It contained head.txt, regression.log, prediction.json and probe.json. The recorded head matched, the CI log recorded 240 passing tests, and the facing probe at 1/8 enclosed 380.625 K and 0 W with all four flags false. [CI job](https://github.com/physicsvigilante/sim_heat/actions/runs/44906825868/job/136854090306) · [Evidence archive](https://github.com/physicsvigilante/sim_heat/actions/runs/44906825868/artifacts/14708008504)

The result supports source interpretation, physical signs, enclosure behavior and evidence integrity for this offline diagnostic. Native measurement and classroom outcomes were untested. The PR remains an unmerged draft and merge approval remains with the owner.
