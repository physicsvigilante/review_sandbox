# Chat B — Opticsim PR #138 independent B1a source / native-physics review

**Date:** 2026-11-18  
**Verdict: CHANGES REQUESTED.** The tested B1a native-hit-only physics and strict input gates are substantially supported, but one **P1 evidence-integrity defect** prevents an owner-clearance verdict. No merge, release, B1b coordinate, eye/pupil, unique image, physical darkness or calibrated native-accuracy claim is authorized.

## 1. Immutable source identity and reviewed scope

| Property | Independently observed |
| --- | --- |
| [Draft Opticsim PR #138](https://github.com/physicsvigilante/opticsim/pull/138) | Open, draft, unmerged; current PR head rechecked |
| **Authored HEAD** | `936f7d8bca9af0db950ab258e6df2f0e3a37914a` |
| **HEAD tree** | `182a8c51dfcc9cd618e9d92f25ea0d5cb49edc30` |
| **Production base** | `d3509e82fb65d81aabe336666851f8f2962623f4`; tree `45ff3bcd9093a527652f13f76c3cc0b02826642f` |
| **Tested PR synthetic merge** | `7970f61daea3e13789f801a82626e95bfc8ef471`; **same tree `182a8c51dfcc9cd618e9d92f25ea0d5cb49edc30`**; parents base first, authored HEAD second |
| Base-to-HEAD compare | 13 commits ahead, 0 behind; **five added files, 1,131 added lines, zero deletions** |
| Native pin | `811f508d2b070898c241a568b0c167dcb8645251` |

These identities were checked using **raw Git commit objects**, the base-to-head comparison and live PR metadata, not copied from PR prose. Precisely the following files are added: `src/detector-pair-json.js`, `src/detector-pair-plan.js`, `scripts/detector-selected-pair.mjs`, `test/detector-selected-pair.test.mjs`, and `examples/jee-detector-selected-native-pair-v1.json`. No old source, native solver, schema, workflow or UI file was modified. Baseline/final blob equality was separately checked: `scripts/run-problem.mjs` = `2efecbf3eddcd9322782cc1667b02fe495fd4fa8`; `scripts/author-scene.mjs` = `0d2ecff53aa03575f96390622ac438fb87aa4a30`.

I read [REQUEST.md](../REQUEST.md), [the exact reviewer prompt](../REVIEWER-PROMPT-01.md), all five full changed files, the baseline `authoring.js`, `contract.js`, `planar-media.js`, `qualified-utils.js`, `observables.js`, `scripts/author-scene.mjs` and `scripts/authoring-evidence.mjs`, and the [#137 independently reviewed R2 design](../../pr-137/reviews/review-02-chat-b.md) plus its actual 197-line contract. #137 was **design-only** clearance, never #138 source clearance. No held PR is a dependency.

## 2. Builder CI inspected — not independent execution

The GitHub Actions commit-specific API returned **11/11 completed SUCCESS** workflows at authored HEAD. I inspected the actual workflow jobs/steps and downloaded the **raw job logs** for:

- [Native/Node24 mirror-angular run #44254113527](https://github.com/physicsvigilante/opticsim/actions/runs/44254113527), job `134631558264`: checkout was the synthetic merge `7970f61...`; Node **v24.19.0**; pin **`811f508...`** checked out and built as the 1,164-module headless core; **810 tests, 810 pass, 0 fail**; the actual `[b1a-native-hit-evidence]` line was present.
- [Optical composition / Chrome run #44254113567](https://github.com/physicsvigilante/opticsim/actions/runs/44254113567), job `134631558480`: same tested merge and native pin; 810/810 Node; build/native/hosted path/browser steps successful; reported **27 browser acceptance checks / 15 screenshots** and **5 hosted smoke checks / 1 screenshot** on **Google Chrome 157.0.8103.50**. These are existing-browser regressions, not a new B1a UI.
- Other current workflows, including planar refraction, original refraction pair, unified problem, qualified authoring, curves, motion and numerical diagnostics, all concluded success; the run-job summaries were additionally inspected for representative native and browser steps. The 20 registered B1a tests in `test/detector-selected-pair.test.mjs` are included in the final 810 tests.

The failure history is real and not laundered: first source `f657b9762e4b30b847a0d69cfb47546a0366b1cb` had **803/804 passing, 1 failing**, and 11 failed workflows. I retrieved the raw failure job: its reverse-normal/units case asserted `0 !== 2`, consistent with applying a raw detector-length bound before converting cm/m. The intermediate correction `15fee6589bd098ce88acf9cb7f3075e024e2d9f1` had 11 successful workflows and 804/804 tests. **Neither intermediate CI identity was used in place of final-HEAD CI.** Final source validates positive authored length and checks the **2–10 mm** scope after canonical conversion.

**What I independently did:** fetched/verifiably compared Git objects, complete source and baseline contracts; inspected builder workflows and raw logs; traced validation/refusal and manifest code; independently calculated optical reference geometry using Python math. **What I did not independently run:** PhyDemo, Node24 test suite, Chrome, or a fresh CLI/manifest attack reproduction. The execution environment had no GitHub network/DNS route for a separate checkout; observed CI remains *builder CI*, not an independent native replay. The counterexample in P1 below is a code-path proof by inspection, not a claim of a separately executed exploit.

## 3. Physics, authorability, provenance and refusal assessment

**Correct bounded physical model (supported by source and builder native evidence).** One explicit v5 `point-source` with single-ray emission, one native `PlaneGlass`, one real 2–10 mm finite `ray-detector`; second absolute heading is applied only to a clone of the first canonical scene. It makes **two distinct native executions**, four individually requested observations each (`source-emissions`, `interface-first-event`, `detector-crossings`, opt-in `detector-hit-events`). It neither implements a second Snell solver nor fabricates a ray. The family canonicalization sorts all component IDs by JS code-unit order and strips only the designated source direction; the two full scene hashes differ and the family hashes agree. Native pin and scene hash are checked before selected evidence is accepted; the baseline observable dispatcher additionally rehashes a snapshot.

**Independently recomputed scalar optics.** For source `(-120,0)` mm, plane at `x=0`, 1.5→1, detector centre `(40,0)` mm and `±0.5°`, Snell gives transmitted angle magnitude **0.7500118999902258°**, predicted detector `|y|=1.5708611274685715` mm and 5 mm finite endpoint margin **0.9291388725314285 mm**. The final *raw native CI log* gives run-A `(40,-1.5708611274685678)`, run-B `(40,+1.5708611274685678)`, incoming/transmitted unit `(0.9999143248553549,±0.013089803247560816)`, exactly one source emission, one transmitted first-event branch, one finite crossing and one hit event per run. Run-A scene SHA `bf785bcde6f7f5ae8b47f7c5214519ff04f696cd2dee24df8d4fb80d8ca96444`; run-B `01e8e811a7c7f6d4f4c39298c2c4f6c913e657e38fbd18ec746252500e2f1423`. Both are pinned-native completed runs. The native reflected Fresnel branch is separate (roughly 4% vs 96% transmitted). For equal indices my independent prediction is **1.3962988465214063 mm**, consistent with the native values asserted by the registered tests; the 2 mm centred detector should miss and 10 mm should hit.

**Strict input and physical checks.** The new byte parser caps original UTF-8 at 1 MiB and rejects nested/escaped equivalent duplicate member names before `JSON.parse`, malformed input and nesting >40. The authoring scan prioritizes supplied unknown/wrong fields before missing required facts and unsupported physical scope. It requires all physical fields, stable IDs, explicit Fresnel and run policy and one of each supported component. Geometry uses canonical mm conversion before detector-length bounds, signed media sides from the actual normal, at least 1 mm opposite-side clearance, finite endpoints, tangent modulo-180 parallelism, and heading modulo-360 identity (±180 equivalent, ≤1e-9° refused). Existing canonical `validate` and native adapter are reused. Valid aim-away/TIR/short-window miss cases remain native negative controls, not quietly repaired inputs.

**Status discipline and limits.** Positive B1a only reports actual native finite-window measurements: public `geometry:{status:'withheld',value:null,reasonCode:'B1B_NUMERICAL_GATE_NOT_RELEASED'}` and `observerAssessment:'not-assessed'` / `imageAssessment:'not-assessed'`. The source has no B1b backintersection. It checks one emitted ray, first-event transmission, side-appropriate incident/destination indices, exactly one transmitted native branch, one crossing/hit, detector interval and an explicit `1e-8` same-native-branch unit-direction agreement (not a native physical-accuracy budget). It retains separate reflected branch, run-local provenance, and per-run raw warnings. Full Fresnel-off is **qualified**, not promoted to available; unknown native warnings and stale/incomplete runs are suppressed. Completed 0/[] misses remain distinct from TIR/aim-away or missing opt-in capture. Execution failures do not generate finalized manifests. These protections are well exercised in builder CI; limitations and P2 findings follow.

## 4. Ranked findings and required corrections

### P0 — None identified

No P0 physical false-image claim, unpinned native change, frozen-script edit or scope breach was found in the five-file diff.

### **P1-F1 — Manifest verifies checksums but not semantic identity of native/readout files (BLOCKER)**

**Location:** [`scripts/detector-selected-pair.mjs`, `verifyDetectorPairManifest`](https://github.com/physicsvigilante/opticsim/blob/936f7d8bca9af0db950ab258e6df2f0e3a37914a/scripts/detector-selected-pair.mjs#L241-L289).

The verifier mandates the nine intended files and hashes every file; it parses **only** `plan.json`, `report.json` and the two serialized scenes for cross-file identity. It **never parses `native-A.json`, `native-B.json`, `readouts-A.json` or `readouts-B.json`** to check their recorded native scene SHA, upstream pin, role, run summary, hit evidence, readout statuses or equality to `report.runs[A/B]`.

A concrete static counterexample: in an otherwise valid two-run finalized directory, save B's native data in `native-A.json` and update that entry's `sha256`/`bytes` in the final manifest, keeping the original plan, scene-A, report and readouts. Every check the current function performs can still pass; it has no code path that reads native-A's actual scene/run identity. An analogous replacement of `readouts-A.json` is also undetected after the manifest entry is updated. This is **not** a claim that an ordinary unchanged manifest could miss a byte-level tamper: it cannot. It is a failure to verify the contract's *internally consistent two native executions* and swapped/historical-evidence refusal. The manifest is not cryptographic independent authentication, and no fix should claim that it is.

**Required:** During verification, parse each actual native and readout artifact and bind `native-[A/B].summary.canonicalSha256`, native pin, serialized scene, readout role, input/family/scene SHA and recorded observations to the corresponding scene, plan and `report.runs[A/B]`; reject swapped/stale/incomplete/mismatched pairs. Check the two scene SHAs are distinct and recompute/verify complete family identity from the serialized scenes. Add a negative test that constructs a *rehash-linked but internally mismatched* finalized directory and proves refusal, rather than only deleting a filename or editing a file without updating the manifest. Preserve last-write and no-clobber rules.

### P2-F1 — Negative observable records do not satisfy the complete per-observable warning/reason-code shape

**Location:** [`scripts/detector-selected-pair.mjs` lines 139–157](https://github.com/physicsvigilante/opticsim/blob/936f7d8bca9af0db950ab258e6df2f0e3a37914a/scripts/detector-selected-pair.mjs#L139-L157) and unchanged [`src/observables.js`](https://github.com/physicsvigilante/opticsim/blob/d3509e82fb65d81aabe336666851f8f2962623f4/src/observables.js).

B1a copies the baseline `evaluateObservables().results` without normalizing them. Baseline `base` has `status/value/method/unit/reason`, but **not guaranteed `warnings:[]` or `reasonCode`** on unavailable/suppressed first-interface and missing-capture records. Thus the R2-required consistent `id,kind,componentId,status,value,method,warnings[],reasonCode,reason` per readout is not realized across negative states, despite retained raw native warnings.

**Correction:** In the new B1a record only, retain upstream status/value/reason without promotion, always materialize explicit warning lists (empty where truly none) and stable nullable reason codes for unavailable/suppressed observable states; test aim-away, TIR, absent hit capture and stale summaries for the complete shape. Do not modify historical observable behavior.

### P2-F2 — Setup/build failure may be counted as an actual native attempt

**Location:** [`scripts/detector-selected-pair.mjs` lines 29–37 and 177–183](https://github.com/physicsvigilante/opticsim/blob/936f7d8bca9af0db950ab258e6df2f0e3a37914a/scripts/detector-selected-pair.mjs#L29-L37).

`nativeAttempted++` happens before `execute(...)`. But the default `executeNative` first runs a `build.mjs --test` process and loads a core *before* it invokes `evaluateDocument`. If that setup/build fails, report says one native attempt even though none reached the pinned solver. Actual native-executor errors after invocation are already recorded properly; the concern is the **pre-native setup** boundary.

**Correction:** Prepare and validate the core before incrementing actual native attempts, or separately report setup attempts versus actual native invocations. Add a setup-failure-specific test demonstrating 0 native attempts and no manifest; keep genuine first- and second-invocation error counts intact.

### P2-F3 — Programmatic test-executor seam needs an explicit trust boundary

**Location:** [`runDetectorPairEvidence({inputBytes,outputPath,execute=executeNative})`](https://github.com/physicsvigilante/opticsim/blob/936f7d8bca9af0db950ab258e6df2f0e3a37914a/scripts/detector-selected-pair.mjs#L140-L143).

The public standalone CLI always selects the built-in pinned executor, and input JSON has no field to inject native results; **that CLI trust boundary is sound in the reviewed source**. The exported JS function, however, permits a programmatic caller to replace `execute` with an arbitrary summary producer and generate a positive-looking report/manifest. This is useful for negative tests but should not be marketed as a trusted public-native API.

**Correction:** Keep the injection seam explicitly test/internal-only, or split a trusted export from a testable internal executor; do not let synthetic execution become unlabelled trusted production evidence. This is **not** evidence of a JSON/CLI exploit, and is lower severity than P1-F1.

### P3-F1 — Add explicit source-completeness and rotated-apparatus tests

The run records do not separately expose `schemaVersion` (although the saved canonical scenes do); add that simple field if the R2 run-record schema remains normative. In addition to current reverse-normal, equal-index, unit and reordered-ID cases, exercise a **non-cardinal rotated valid plane/detector** through the B1a pair CLI. Neither is permission for a B1b coordinate.

## 5. Decision and release boundary

**CHANGES REQUESTED** for this **exact** `936f7d8...` / `182a8c...` source, primarily P1-F1. The positive pinned-native observations, full frozen-history preservation, strict input authoring, refusal cases, 810/810 exact-source Node and 11/11 exact-head builder CI are credible evidence for the narrowly bounded B1a functionality, **not a replacement for full evidence consistency verification**. Correct P1, cover it with a targeted negative test and obtain new exact-head CI plus independent follow-up review; disposition the P2 items explicitly. If any source changes, pin the new head/tree/merge and do not transfer this review's identity. Keep PR #138 draft/unmerged and leave production main, issue #123 and all unrelated held PRs unchanged. **B1b mathematical location, eye/image/observer claims, a native accuracy certificate and release are outside this decision.**
