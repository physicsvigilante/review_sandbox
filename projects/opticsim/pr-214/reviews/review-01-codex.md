# Independent Codex review of Opticsim PR #214

**CLEARED FOR OWNER DECISION.** The corrected final head resolves three observed fail-open Detector cases. I found no outstanding blocker in v32 authoring, geometry, native measurement semantics, or browser qualification.

| Identity | Reviewed value |
| --- | --- |
| Final candidate | `7a68ccec47204f297733a955a93d4d5487c4c7ec` |
| Tree | `5aff5e1a3e940e9eec1011e59baac73529440597` |
| Base | `85a2f7be6b8e1b2572ab4344241523dbeb1eb164` |
| CI merge | `4bcbf97b9d45d2aa5396d1b48fe5801feda168e4` |
| Browser app blob | `34d9be9c483f694b1a7c0a80a7125edf645bfad5` |
| PhyDemo pin | `811f508d2b070898c241a568b0c167dcb8645251` |

## Physical scope and corrected qualification

V32 selects a finite circular cap, a rightward on-axis directional source strictly inside, and a separated vertical passive detector beyond the pole. The pinned Glass retains the flat chord and true circular arc. The validator bounds height relative to radius, physical extents, incident cone, indices, source and detector separations, and detector length. The A27 example declares an interior probe displaced 0.0625 mm from the base, the exterior index, and the chosen source and detector properties. Its observations apply to the authored finite probe. The tabletop limit belongs to the frozen study and separate paraxial interpretation.

The audit tracks each emitted native ray object through one inside-to-outside arc contact and then one detector crossing. I reproduced three faulty native Detector callbacks on the prior head. The previous audit accepted an absorbed ray, a shifted post-hit origin and an incorrect zero signed power. The final head guards the post-hit origin and direction, extra or nonpassive branch signals, and signed power accumulation from the actual incident ray. It suppressed every reproduced case. Six further source, arc and detector faults also suppressed observations. I separately verified stale scene and stale profile-marker suppression, physical contact refusals and both sides of the detector clearance margin.

## Independent runs, browser and archives

The isolated exact candidate passed 31 focused tests. I checked 648 admissible native scenes across translated coordinates, cap thicknesses, radii, source distances, detector orientation and different indices. The independent circle and vector Snell calculation agreed with all 1,944 detector hits. The largest ordinate discrepancy was 1.51 × 10⁻⁸ mm and the largest transverse direction discrepancy was 7.2 × 10⁻¹². Both detector orientation signs gave the expected signed power. All 50 prior public examples and plans matched the base. Historical v21, v30 and v31 tests passed, and the browser app blob matches the appended provenance record.

Independent real Chrome passed all seven v32 checks, including base-contact refusal, cap-height revision, qualified save and reopened native results. All eleven hosted workflows passed on the revised candidate, including 1,246 Node tests and real Chrome profile qualification. The six v32 CLI records, six frozen-study records and qualified Chrome export matched my isolated run byte for byte. I verified the CLI archive SHA-256 `313dff98f832c22e9332da67c705008539b6a876574c2adca3a225efa05489a1` and the profile browser archive SHA-256 `90bfb2291f68db873e5eb85ef01561b9393ab281e5249176ed78c66adbdc832c`. [Optical composition run](https://github.com/physicsvigilante/opticsim/actions/runs/44866601310) · [CLI and native archive](https://github.com/physicsvigilante/opticsim/actions/runs/44866601310/artifacts/14692390903) · [Profile Chrome archive](https://github.com/physicsvigilante/opticsim/actions/runs/44866601310/artifacts/14692111509)
