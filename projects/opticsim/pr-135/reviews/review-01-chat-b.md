# Chat B — independent native-physics review: Opticsim PR #135

**Date:** 2026-11-18  
**Verdict: CHANGES REQUESTED.** The central 5 mm finite-window native feasibility result is independently corroborated from the archived GitHub logs and mathematical reconstruction. However, preregistration [#134](https://github.com/physicsvigilante/opticsim/issues/134) explicitly requires an **equal-refractive-index native control**, which the new test does not contain. This is a **P1 research-acceptance completeness issue**, not evidence that the reported native crossings or geometry are wrong. The requested correction must remain test-only, be rerun on a new exact source, and receive a fresh identity/evidence review. **No production B capability, image claim, or merge is approved.**

## 1. Exact-source identity and independent evidence inspection

| Item | Independently checked result |
| --- | --- |
| Reviewed PR | [Opticsim #135](https://github.com/physicsvigilante/opticsim/pull/135), open, draft, unmerged at final recheck |
| Production base | `d3509e82fb65d81aabe336666851f8f2962623f4` |
| Reviewed HEAD | `58001725e8fd97cbfeb00ee9eaff705a864ecae5` |
| Reviewed HEAD Git tree | `ff0c6e46ea97b650c5e7e58680f180c458a437c1` |
| Tested synthetic PR merge | `a2a798de26b70e0fcf2cd04366bed660184abbba` |
| Tested merge Git tree | `ff0c6e46ea97b650c5e7e58680f180c458a437c1` — **identical** |
| Authored tracked diff | **One addition only:** `test/jee-finite-detector-window-feasibility.test.mjs`, 462 lines added, zero deleted; file blob `d79c185ba0f438c3c4a996c00bd5fa6dc8808adb` |
| Native execution | [run 44235111520 / job 134569243452](https://github.com/physicsvigilante/opticsim/actions/runs/44235111520/job/134569243452), Node `v24.19.0`, PhyDemo pin `811f508d2b070898c241a568b0c167dcb8645251`, **799/799 passed**, none failed/skipped/cancelled; nine new B research tests reported passing |
| Standard CI | Queried run records for this exact HEAD: **11/11 completed/success**, each `run_attempt=1`. [Optical composition / browser run 44235111578](https://github.com/physicsvigilante/opticsim/actions/runs/44235111578) includes successful existing preinstalled-Chrome and hosted browser regression steps |

I fetched the actual Git commit objects rather than relying on the PR description. The reviewed HEAD's parent is `ad4ab62c8c2fa70abcbe48c05742bac4303870bd`, the preserved first test-only source. GitHub's base-to-head comparison has **two commits ahead, zero behind, and exactly the one new test file**. The tested merge commit has both the declared base and final HEAD as parents, and its tree matches the reviewed HEAD. The actual native CI checkout is logged as `a2a798d...`, not merely asserted in the PR. The issue was created before PR creation and the new CI run.

I read all 462 added source lines, the corrective commit diff (33 added / 4 removed lines), and relevant exact-HEAD `src/observables.js`, `src/native-observations.js`, `src/planar-media.js`, `src/qualified-utils.js`, and `scripts/author-scene.mjs` code. I retrieved and parsed the 350,842-character, 1,137-line actual native job log and its **71 structured finite-window research entries**. This review independently checks source, Git identities, CI metadata, log contents and arithmetic. **I did not independently execute PhyDemo, Node24, or Chrome.** Eleven builder CI workflows are not eleven independent physics replications.

## 2. Independent physical geometry from the actual native measurements

The logged default apparatus is exactly one v5 `S1` source at `(-120,0)` mm, one `I1` planar 1.5→1 interface at `x=0`, and the same real receiving-side `D1` detector at `x=40` mm, orientation +90°, **full length 5 mm**, therefore `-2.5 ≤ y ≤ +2.5` mm. Simulation policy: `rayDensity=0.2`, `maxRayDepth=8`, `processedRayLimit=10000`. The two independent source headings are `-0.5°` and `+0.5°`, with **different** canonical scene hashes:

- Negative heading: `4007c919f63cdbd4a1d0ff6f57ec5ac438fa6295eee4ac1f4bdca70d19e6ccf0`.
- Positive heading: `37fb3a4da5b1f87ecf794e3f148b07cbe7bc6351efb802f73da2b6bf351569f3`.

Each actual native run reports `completed`, one emission, one interface encounter, exactly one transmitted and one reflected branch, one native detector crossing, no truncation, no undefined behavior, no warnings. The transmitted and reflected relative powers are approximately `0.9599999995214483` and `0.04000000047855171`, consistent with Fresnel behavior. The logged detector-hit direction is exactly the logged native transmitted branch direction in each case, not a manufactured or guessed path.

| Quantity | Independent calculation / actual logged event |
| --- | --- |
| Snell angle | `asin(1.5 sin 0.5°) = 0.750011899990226°` |
| Interface height | `120 tan 0.5° = 1.047224134891055 mm` (signed ±) |
| Independently predicted crossing | `±(120 tan 0.5° + 40 tan 0.750011899990226°) = ±1.570861127468572 mm` |
| **Actual native crossings** | `(40, -1.5708611274685678)` and `(40, +1.5708611274685678)` mm |
| Actual native unit directions | `(0.9999143248553549, ∓0.013089803247560816)` |
| Direct finite-segment clearance from logged hit coordinate | `2.5 - abs(1.5708611274685678) = 0.9291388725314322 mm` |
| Independent intersection of **logged** lines | `(-79.99619199829817, 0)` mm |
| Both backward line parameters | `s1 = s2 = -120.00647357027965 mm` |
| Line determinant absolute value | `0.02617736355354841` |
| Independent scalar depth control | `120 tan 0.5° / tan 0.750011899990226° = 79.99619199829765 mm` |

For the intersection, I separately solved the 2×2 system `p1 + s1 u1 = p2 + s2 u2` using the **recorded** detector positions/directions; I did not just recopy the source's predicted image-depth formula. The approximately `5.3e-13 mm` difference between scalar Snell depth and measured-line reconstructed depth is arithmetic agreement on this fixture, **not a measured native error bound**. Both negative line parameters extend backward into the source-side medium. An algebraically zero line self-residual is tautological for two nonparallel 2D lines and is correctly not used by the source as optical accuracy evidence.

## 3. Native finite-window, refusal, and provenance controls

| Native/derived control | What the archived native log and source demonstrate |
| --- | --- |
| Shift detector center to `y=+2.5 mm` | Real native crossings `[0,1]`; derived `unavailable`, null point, `DETECTOR_WINDOW_DOES_NOT_SELECT_ONE_TRANSMISSION` |
| Shorten centered detector to 2 mm | Native `[0,0]`, derived unavailable/null |
| Move finite detector to `y=+10 mm` | Native `[0,0]`, derived unavailable/null |
| Reverse / rotate / translate / cm / m | Eight coordinate/unit cases each pass; reported depth remains approximately `79.996192 mm` with source-side orientation handled by the plane normal |
| Full Fresnel | Both native readouts `available`; test-only derived geometry `available` without image interpretation |
| Transmitted-only `partialReflection:false` | Native readings `qualified`, reflected branch count zero, derived geometry **`qualified`**; each run's Fresnel warning remains attributed |
| Transmitted-only + real first-run detector miss | Native counts `[0,1]`, derived `unavailable/null` but **both** invocation labels, scene SHA values, readout statuses and distinct run-linked Fresnel warnings retained |
| TIR ±50°; just-below-critical ±(asin(1/1.5)-0.00001°) | TIR has no transmitted branch; near-critical cases transmit but both miss this finite segment; no derived intersection |
| Near-parallel ±0.000001° and synthetic antiparallel | Geometric intersection withheld with `ILL_CONDITIONED_LINES`; synthetic antiparallel is an algebra control, not a native run |
| `simulation.maxRayDepth=0` | Separate incomplete native records give `suppressed/null`; this is **not** zero geometric source depth |
| Stale revision; opt-in capture absent; duplicate/single input; mismatch; extra plane | Test code exercises typed refusal; source rejects incompatible geometry and numerical settings, and keeps both evaluated readouts in capture/staleness cases |
| Native capture on/off | Exact canonical scene hash and all prior native observation keys/meters match; hit-events appear only under opt-in recording |

The source's `family()` sorts apparatus components and removes **only** `point-source.emission.directionDeg` from its physical/numerical comparison; `derivePair()` requires separate invocation labels, nonidentical scene hashes, one source/plane/detector, one native transmission, a matching outgoing hit direction, a non-endpoint finite crossing, a nonparallel backward intersection and a source-side result. This is appropriately strict for the **named research fixture**, not a general multi-ray lineage or observer selector.

The correction from `ad4ab62c...` to `58001725...` is real and verified in the commit diff: the final helper first collects both readout/provenance snapshots and only then evaluates hit/refusal conditions. The newly added qualified-miss test and actual CI entries demonstrate that a null result no longer silently discards the **second run's** completed/qualified warning. The prior first-source deficiency remains part of history, not retroactively reclassified as passing.

## 4. Ranked findings and required action

### P0 — None identified

No evidence of a wrong baseline refraction direction, fictitious native finite hit, false merge-tree identity or production-code alteration in the reviewed source.

### P1 — F1: A preregistered equal-index native case is missing (**research-acceptance blocker**)

[Issue #134](https://github.com/physicsvigilante/opticsim/issues/134) explicitly says the research cases **must include equal indices**. The complete new test file covers mismatched media in a comparison-only *rejection* test (`objectIndex:1.6` against a 1.5 baseline), but no **actual paired native run** with `objectIndex===receivingIndex`. This leaves untested the physically important no-index-contrast reference: a properly selected finite detector should give a backward depth equal to the real source depth, approximately **120 mm**, rather than the 1.5→1 apparent-depth result (~80 mm). For ±0.5° at `x=40 mm`, the predicted equal-index hits are `±160 tan 0.5° ≈ ±1.3963 mm`, inside the 5 mm segment; native branch handling (including any zero-power reflection behavior) must be observed, not presumed.

**Required:** Add a test-only equal-index paired native control to this same file. Assert the actual native counts/hit directions, real endpoint clearance, completed/qualified readouts as applicable, source-side backward-intersection depth ≈120 mm, and appropriate refusal/qualification on any unavailable branch. Do not pre-inject a path or write native code to make the test pass. Re-run the existing CI gates on the **new** exact source. Until then, the explicit preregistered case coverage is incomplete even though the existing 5 mm fixture's result is physically corroborated.

### P2 — F2: Cross-run component-order compatibility is not directly exercised

Source lines 291–311 create a `reverseOrder:true` case, but **both** independent runs use that same reversed ordering. This proves each reversed-order scene works; it does not directly test pairing a normal-order run with a reversed-order run under `family()`'s sorting rule. **Recommended correction in the same bounded test-only change:** run one baseline ordering and one reordered equivalent with differing source direction, then assert the expected geometric result and provenance. This is a coverage gap, not a demonstrated algorithm defect.

### P2 — F3: Warning preservation is demonstrated for completed/qualified misses, not all suppressed failures

`provenance()` (lines 136–142) saves warnings obtained from `evaluateObservables()`. On an incomplete/stale run, existing `src/observables.js` returns `suppressed` before attaching readout warnings; the helper does **not** separately retain `execution.summary.native.warnings`. Consequently its evidence structure cannot claim complete native-warning retention across *every* incomplete/early-refusal path, even though it correctly retains both identities and the Fresnel-omission warnings in the newly tested **completed qualified-miss** case. **Before general reuse**, record raw per-invocation native warnings separately and exercise a warning-bearing suppressed case where feasible. Do not mistake this concern for failure of the observed qualified-miss regression.

### P2 — F4: Conditioning thresholds and sensitivity are not native uncertainty certification

`MIN_LINE_SINE=1e-4`, `MIN_ENDPOINT_CLEARANCE_MM=0.05`, and `MAX_EXTENSION_SCENE_RATIO=10` (source lines 119–123) are explicit test-local heuristics. The synthetic ±`1e-4 mm` / ±`1e-6 rad` perturbations yielded at most `0.0015291726268600314 mm` output movement **for this particular pair**. They do not establish a bound on native ray tracing, detector-edge error, scene-scale dependence, grazing/critical conditioning or physical image localization. The source itself describes this accurately. **Required only before production B admission:** a separately reviewed conditioning/error policy and adversarial boundary experiments, not promotion of these fixture thresholds.

### P3 — Interpretive and follow-on limitations

The 5 mm segment is a geometric native detector, **not an eye, pupil, camera, focal surface, or retinal observer**. Two non-simultaneous runs each crossing an identical segment do not demonstrate two rays simultaneously passing through one physical pupil, brightness at an observer, actual ray backpropagation, continuous irradiance or a unique stigmatic image. The 2D point is only an intersection of two post-native, backward-extended measured lines. An extension to general observer selection, source/path identity or user-visible B results needs a distinct approved model/schema, provenance and browser integration. Existing held #129/#131/#133 and main-protection #123 remain separate.

## 5. Gate consequence

**CHANGES REQUESTED** for this exact source's **preregistered test-completeness** gate (F1). The core native finite-window evidence is valid as *bounded research evidence* but cannot yet be marked fully cleared under #134's declared checklist. Add the no-index-contrast native control; preferably add the mixed-order pair (F2) in the same test-only revision. Keep the first-source correction history, production engine, PhyDemo pin, schema and existing checks unchanged. Obtain new exact HEAD/tree, rerun Node24/native and existing Chrome workflows, and request a fresh independent source/evidence review. **Do not merge this PR or release any B/observer/image capability on this review.**
