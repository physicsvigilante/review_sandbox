# Opticsim PR #217 independent focused review R3

**CLEARED for owner-authorized integration at the exact candidate below.** B1a and B1b are resolved. This verdict does not confer merge authority or establish post-merge verification.

| Identity | SHA |
|---|---|
| Candidate | `ed957941c95fec027462bce1f14bef19794e3910` |
| Candidate tree | `9f675ff992869da1ded700b427d8cf044b91c21f` |
| Production base | `52d14f68725da5080a1cca112602e7776c9cc25e` |
| GitHub PR test merge | `9289db8140c641dd193f56dc01e76dd2d445beb5` |
| Pinned PhyDemo | `811f508d2b070898c241a568b0c167dcb8645251` |

The PR test merge has the base and candidate as its two parents and the identical reviewed tree. [R1 blocked verdict](https://github.com/physicsvigilante/review_sandbox/blob/e078a70082dff5ff7adcb7a281ccd42455bbcb81/projects/opticsim/pr-217/reviews/review-01-codex.md), [R2 focused blocked verdict](https://github.com/physicsvigilante/review_sandbox/blob/154e9f1b74e8091b83eae75015fe42e9d9e8c913/projects/opticsim/pr-217/reviews/review-02-codex.md).

## Native qualification

- In v33's lossless, Fresnel-disabled branch, authored brightness fixes each polarization channel. The audit independently retains the native incident point, prior actual outgoing origin, channel values and normalized direction. It checks current incoming origin explicitly at the slab and passive detector, including the entrance and far-face handoff. Native handlers still choose all intersections and delegate exactly once.
- The single native detector crossing requires a zero pre-crossing accumulator. Its orientation fixes the physical sign. The native increment must agree with the incident channels, the outgoing ray must preserve the point, direction and channels, and the final exposed meter reading must equal the signed authored brightness. The report withholds measurements if the run cannot substantiate that passage.
- I independently exercised eleven mutated native-callback controls. The suite changed source and far-face polarization, applied detector attenuation or amplification, redistributed polarization at constant total brightness, changed detector position or outgoing direction, changed the pre-crossing or final detector accumulator, and shifted the glass or detector incoming origin along its real ray line. The targeted mutation fired once per control. Every control withheld both the hit and signed power.
- All 128 genuine public controls qualified across the two endpoint angles, interior incidences, lower and upper thickness limits, near-world-limit translations and both detector signs. Numerical quadrature of the conserved tangential optical momentum yielded a maximum detector-position residual of 0.001310768 mm and a maximum tangential-direction residual of 0.0000484934. The native signed-power residual was zero. The replay also passed the frozen 30-case translation grid, inherited six-row A15 non-grazing data and all 15 v25 qualification cases. The v25 trusted field and A15 source inputs are unchanged.
- Independent real Chrome 158.0.8127.37 passed all seven v33 checks, including grazing refusal, native retracing and qualified reopen, and all nine v25 checks. A broad Windows Node pass encountered three inherited CLI tests passing a drive URL pathname to `execFileSync`, and one symlink-privilege skip. The three unchanged CLI checks passed with a review-only Windows argument adapter. The hosted Linux test run below used unmodified sources and test harness.

## Hosted evidence

All 11 workflows on the exact head succeeded. Optical composition job [136740763841](https://github.com/physicsvigilante/opticsim/actions/runs/44869550048/job/136740763841) recorded 1,263 Node tests passed and successful v25 and v33 acceptance on Chrome for Testing 158.0.8127.36.

I downloaded the exact-head authoring archive [14693023276](https://github.com/physicsvigilante/opticsim/actions/runs/44869550048/artifacts/14693023276) and verified its declared SHA-256 `1f443b0749c64291b4aabe259162612aae831978469f5f732834526c6e48f03e`. All 14 relevant records matched the independent replay byte for byte: six v33 example files, six inherited A15 first-passage files and two frozen-grid residual reports.

The exact-head browser archive [14693247449](https://github.com/physicsvigilante/opticsim/actions/runs/44869550048/artifacts/14693247449) matched its SHA-256 `7e2bb5a8025246df4d8e4897e88b3317ac9e910ec261b6cde483bda1ef82ecb7`. It contains the seven passing v33 checks with the same check identities as the independent Windows run, the slab screenshot and a qualified revision download.

The evidence is limited to actual finite-angle passage in the versioned geometry and sampled native measurements. The original A15 grazing limit remains analytical, and the reported power is in signed native relative units.
