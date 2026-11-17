> **HISTORICAL REVIEW-01 REQUEST:** This packet originally concerned source `a570e3c589457d21b6673701a2d126d7046e1c3c`, where [Chat B returned CHANGES REQUESTED](reviews/review-01-chat-b.md) for manifest literal-type ambiguity. The corrected new source `f87a9aa025caf5091da8fe3613734b62281ebe1c` has separate [targeted REQUEST-02.md](REQUEST-02.md) and [REVIEWER-PROMPT-02.md](REVIEWER-PROMPT-02.md), with green exact-head CI but awaiting **NEW** `reviews/review-02-chat-b.md`. The original review-01 outcome and CI remain historically correct. No native execution or production merge is authorized.

# SIM_HEAT PR #38 — focused R2: non-regenerating Modelica build TEXT preview (never executed)

**Source project:** [SIM_HEAT draft PR #38](https://github.com/physicsvigilante/sim_heat/pull/38). **Historical F0 experimental lineage, NEVER MERGE TO MAIN**.
**Exact source HEAD:** `a570e3c589457d21b6673701a2d126d7046e1c3c`.
**Immediate base:** PR #37 independently reviewed corrected offline staging HEAD `2f2b8d5008f51b9972897058328aed8cbcbfbbce`, tree `de397fe3af9bb3385c4ef55354e49c33571dc99b`.
**Original frozen F0 source:** `dd8c9432abe97563414bb3ed809e61e673473812`.
**Change class:** R2 future native-input/evidence interpretation; code remains entirely **offline, non-executing**. Four **ADDED** files only, zero edits to earlier source: `.github/workflows/h1-c1-f02-build-text-preview.yml`, `qualification/h1_c1/f02/offline_build_script_preview.py`, `test_offline_build_script_preview.py`, `BUILD_TEXT_PREVIEW_SCOPE.md`.
**Reviewer output:** NEW, independently written `projects/sim_heat/pr-38/reviews/review-01-chat-b.md`; PASS/CHANGES REQUESTED/INSUFFICIENT EVIDENCE. Neither a review nor a CI status grants native authorization.

## Original physical and reference facts

First author original model SHA `9a165e5ce2cc85da84ecc8bc4e63e2990f2066f3547dc6ba8508fa1afbe5f435`, evaluator-only modal study `b43e85b6b10afd6550a43322cf98097fe9781a606ee01bc031eadbfd4783b31b`, frozen physical library `SimHeat.mo` SHA `e57955b6c32cb34321a6b1908306c4ea9a63ae259b95a5fd48c7e8d3b4da10ea`. The original [PR #37 review-02](../pr-37/reviews/review-02-chat-b.md) verified exact byte-only staging, readback and 23 frozen source pins.

Owner-approved Option A **OFFLINE checking only** uses single exact original PR31 V2 scientific JSON, **4,409,800 bytes**, raw SHA `0db511dd8dba023d16518667de256029cf3e073463ea21e2478aeac8afd1f368`, canonical seal `d2b8e2ca8e1f929cac7b028dcc3f7d0b453921d193f877eb091e23ac70aa4ce9`; reviewed Git XZ SHA `fc5a7df5928c3fb8aef2ba4af516dfbd32b42c0450ebef1051ad4fd7efebd17f`, complete manifest SHA `50467b138ed64cdb908f2c763bc777e6babf0bb04a0711568acc559112e66f84`. The old frozen native runner `tools/h1_native_batch.py::prepare` **regenerates** reference data, which would not be the reviewed saved seal on all hosts; **must never be invoked here**.

The historical F0 checking-reference static `hotLead.G` physical exact-error margin was only **80×** against required **100×** — original FAIL remains. PR32 two new hosts' regen of reviewed PR31 seal **failed bitwise identity** (different `c30e8783...` seal vs original `d2b8...`) — original FAIL remains. There is no native OpenModelica simulation, no MAT/CSV trace and all nine original public readings remain not_computed.

## New read-only text adapter

The source requires the reviewed PR37 six-file stage to pass its strict checks and revalidates the model/study/source/ref bytes. It uses **only** frozen `tools.h1_native_batch.build_script(...)` as a **pure string-formatting function**, not frozen `prepare`, `execute`, `invoke`, `reference.prepare` or subprocess. It creates one fresh nonnative directory with exactly two files:

- **`unexecuted-build-script.mos.txt`** — TEXT of a prospective OpenModelica script with `loadModel(Modelica, {"4.0.0"})`, MSL version check, staged fixed library/model paths, exactly one `buildModel` call, start 0 s/stop `1810.609003248995` s / 4000 intervals / DASSL / tolerance `1e-8` / MAT / full variable filter. This is a **source preview**, not an executed or approved `.mos` plan. Paths are current CI-host-specific absolute paths, not portable attested host inputs. No compiler was invoked and no build result exists.
- **`NONNATIVE_BUILD_PREVIEW_MANIFEST.json`** — source hashes, script SHA, original saved V2 SHA/seal, source stage label, targets/limitations and all native, one-shot, host, owner-launch, F0 original accuracy and PR32 bitwise claims **false**.

`preview-text-only` and `verify-preview-only` are the only CLI actions. Stage/source tampering, changed saved script, changed full manifest, duplicate JSON metadata keys, missing/extra `build.mos` or executable, unsafe label and replayed duplicate preview all refuse. `verify` independently re-generates expected TEXT only, not scientific numerical reference values. This cannot execute, compile, reserve or award native qualification. The output receipt is **`NONEXECUTABLE_BUILD_TEXT_PREVIEW_VERIFIED`** and explicitly all native flags false.

## Exact-head CI evidence

[Run #44030612438](https://github.com/physicsvigilante/sim_heat/actions/runs/44030612438) **completed SUCCESS** at exact source HEAD. [Artifact #14305570982](https://github.com/physicsvigilante/sim_heat/actions/runs/44030612438/artifacts/14305570982): 22,033 bytes, whole ZIP SHA-256 **`7e3196d673c0b2a1d71166da81b1ac58fdcd256121c3029e61fc2b37525179f1`**. Chat A independently downloaded actual ZIP and rehashed, **33/33 member CRC valid**. Actual saved script SHA **`eeb216779afc98986fc1c2649c07a036d835743a9118971a21a8f7acddad110e`**, matched receipt; no `build.mos`, executable or MAT present.

**229/229 OFFLINE unittest methods passed:** 12 new text preview, 24 strict stage, 16 disabled control/type, 11 owner offline consumer, 8 immutable binding, 9 archive integrity and 149 original frozen H1. Original frozen 14 SHA pins and old 23 source-plan pins pass; workflow `contents:read`, no persisted credentials, no paths filter and **no `omc` query/build/launch**. These are source/test gates, NOT 229 native simulations.

## R2 reviewer tasks

1. Verify pinned source/base/head four-addition-only diff, preserved historical source/blob identities and original 37×4001 saved reference seal. No replaced physics or author files.
2. Independently inspect actual generated TEXT in ZIP; check expected MSL 4.0.0, model library path, model identity, DASSL, grid, tolerance, MAT and variableFilter. It embeds `buildModel` as **unexecuted text**: verify there is **no invocation path** to `omc` in CLI, workflow, import side effect or new code. The original frozen pure formatter may be imported, but its `prepare`/`execute` must not run.
3. Adversarially test or review refusals: staged/source/reference tamper, changed preview text, forged permission manifest, duplicate JSON keys, repeated preview, extra `build.mos`/exe or missing files, unsafe label, CLI `execute/build/launch/approve/native`, and absence of regeneration.
4. Inspect exact run and original ZIP SHA/CRC, all 229 tests and no native evidence; distinguish personally rerun tests, inspected hosted runs, saved output/status/limits.
5. Specifically assess whether generating runnable Modelica source TEXT in a publicly accessible repo is safe only as **data under separate approval**; ensure no erroneous implication that a script preview is an executable, trusted, fully pinned native plan, a one-shot reservation, or a completed scientific result.
6. Provide a **SCOPED PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE** verdict strictly for offline prospective text formatting and provenance. List actual remaining owner-authenticated protected source/root/backup, distinct non-regenerating runnable adapter and exact plan, authenticated host/OMC/MSL fingerprints, atomic durable one-shot lock with no retries, pre-native R2, **separate owner permission for a named native launch** and post-native trace review.

**Hard stop:** Do not modify source, merge old PRs, grant native permission, run `omc --version`, install OpenModelica, compile or execute a Modelica model, widen frozen tolerances or reclassify old failed evidence. Follow [PROTOCOL](../../../PROTOCOL.md), [RISK POLICY](../../../REVIEW-RISK-POLICY.md) and [review template](../../../REVIEW-TEMPLATE.md).