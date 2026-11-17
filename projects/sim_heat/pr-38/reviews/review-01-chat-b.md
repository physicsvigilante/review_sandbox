# SIM_HEAT PR #38 — independent Chat B R2 review (review-01)

**Verdict: CHANGES REQUESTED — narrowly scoped to offline build-text preview manifest integrity.** The source preservation, original saved reference identity, passive Modelica text, non-execution boundary, and exact-head hosted CI are substantiated. One **MAJOR** new readback defect must be corrected before a scoped R2 PASS. **This is neither a native qualification nor native-launch/merge authorization.**

- **Reviewer/date:** Chat B, separate ChatGPT conversation (GPT-6), 2026-11-17. Independent context, not independent human/credentialed expert assessment.
- **Project/source:** [physicsvigilante/sim_heat draft PR #38](https://github.com/physicsvigilante/sim_heat/pull/38), open, draft, unmerged; historical F0 experiment **NEVER MERGE TO MAIN**.
- **Exactly reviewed head:** [a570e3c589457d21b6673701a2d126d7046e1c3c](https://github.com/physicsvigilante/sim_heat/commit/a570e3c589457d21b6673701a2d126d7046e1c3c).
- **Exact reviewed source Git tree:** `0f5af0d11d3c96b5b4decc3ea8dd0fae2ae201b6` (GitHub run/head commit and ZIP `head-tree.txt` agree).
- **Immediate base:** `2f2b8d5008f51b9972897058328aed8cbcbfbbce`, tree `de397fe3af9bb3385c4ef55354e49c33571dc99b`, previously corrected PR #37 source. [Exact-base comparison](https://github.com/physicsvigilante/sim_heat/compare/2f2b8d5008f51b9972897058328aed8cbcbfbbce...a570e3c589457d21b6673701a2d126d7046e1c3c): ahead 4 / behind 0, **four additions only, 450 added lines, zero changes/deletions to inherited paths**.
- **Four new files:** `.github/workflows/h1-c1-f02-build-text-preview.yml`, `qualification/h1_c1/f02/{offline_build_script_preview.py,test_offline_build_script_preview.py,BUILD_TEXT_PREVIEW_SCOPE.md}`. Original H1 physics, checker, old native runner, first-author model/study, PR31 reference, and earlier staging/control files remain unchanged relative to the immediate base.
- **Risk/scope:** R2, prospective native-input/evidence interpretation only; **review of non-regenerating text formatter, exact staging provenance, strict readback, refusals, and CI; no native execution**.
- **Reviewer mutations:** None to `sim_heat`, frozen inputs, CI, source PR, approvals, histories or tolerances. Only this new independent report in `review_sandbox` is authored.
- **CI:** [run #44030612438](https://github.com/physicsvigilante/sim_heat/actions/runs/44030612438), push, attempt 1, exact reviewed SHA, completed SUCCESS; job `133861389432` SUCCESS. [Downloaded artifact #14305570982](https://github.com/physicsvigilante/sim_heat/actions/runs/44030612438/artifacts/14305570982), personally opened/rehashed (details below).

## Findings

### F-01 — MAJOR / CHANGES REQUESTED: type-ambiguous JSON equality accepts falsified literal manifest types

**Location:** [`offline_build_script_preview.py` lines 120–134](https://github.com/physicsvigilante/sim_heat/blob/a570e3c589457d21b6673701a2d126d7046e1c3c/qualification/h1_c1/f02/offline_build_script_preview.py#L120-L134), especially:

`doc=staging.strict_metadata(target/MANIFEST)`

`need(saved==raw and doc==contract(label,raw), "build text/manifest differs from verified source")`

The shared `staging.strict_metadata` rejects duplicate keys, non-finite constants and malformed/oversized metadata, but **does not enforce exact Python JSON value types**. The new equality uses Python dictionary equality, where `0 == False` and `4000.0 == 4000`. Thus a changed full manifest with an unauthorized JSON type substitution can pass the purported exact expected-manifest check.

**Independently reproduced from the actual saved PR38 artifact:** parse `ci-text-preview/NONNATIVE_BUILD_PREVIEW_MANIFEST.json`, replace one field and compare the resulting parsed JSON object to the saved expected object using the source's `==` predicate. Each of the following mutations independently still compares equal:

- `"nativeAllowed": false` → `"nativeAllowed": 0`
- `"ownerNativeLaunchApproved": false` → `"ownerNativeLaunchApproved": 0`
- `"nativeExecuted": false`, `"buildInvoked": false` or `"referenceRegenerated": false` → numeric `0`
- `"frozenF0Original100xPassed": false` or `"pr32BitwiseRegenerationPassed": false` → numeric `0`
- `"targetIntervals": 4000` → `"targetIntervals": 4000.0`

The imported strict parser would accept these as valid JSON with unique keys; the saved build-script bytes and staged bytes are unchanged. **Expected:** verification rejects literal false-to-number and integer-to-float drift, as it rejects other forged permission metadata. **Observed:** the exact comparison predicate accepts it. This is an independent predicate-level adversarial reproduction plus code-path inspection, **not** a claimed execution of the full `preview.verify` method under the mutated filesystem. The 12 new hosted tests cover `true` for `nativeAllowed` and duplicate-key injection, but not these equal-valued, different-type substitutions ([tests lines 71–89](https://github.com/physicsvigilante/sim_heat/blob/a570e3c589457d21b6673701a2d126d7046e1c3c/qualification/h1_c1/f02/test_offline_build_script_preview.py#L71-L89)).

**Impact/limit:** Violates the R2 promise of complete exact readback and literal false permissions, and can mask altered evidence types. Numeric zero does **not** grant actual native permission and this does **not** establish an OMC execution path. Nevertheless the evidence contract must not silently equate a number and a permission boolean, especially after PR #37 corrected this class of metadata ambiguity.

**Smallest correction:** After `strict_metadata` (preserve explicit duplicate-key refusal), compare the actual manifest bytes to the canonical `encoded(contract(label,raw))` bytes already written by `prepare`; or enforce recursively exact JSON types plus required literal `is False` flags and `type(targetIntervals) is int`. Add independent regression tests mutating each critical false permission/history field to integer `0` and floating `0.0`, and `targetIntervals` to `4000.0`, while preserving all other stage/script bytes. Demand nonzero CLI refusal and no native side effects. Retain the original first failure and new correction at a **new exact source SHA**, with new current-head CI and targeted R2 re-review; do not edit frozen physics or relax a gate.

### F-02 — NO DEMONSTRATED DEFECT: passive Modelica text and source-bound script settings

Code inspection of [new adapter](https://github.com/physicsvigilante/sim_heat/blob/a570e3c589457d21b6673701a2d126d7046e1c3c/qualification/h1_c1/f02/offline_build_script_preview.py), [old frozen formatter](https://github.com/physicsvigilante/sim_heat/blob/a570e3c589457d21b6673701a2d126d7046e1c3c/tools/h1_native_batch.py#L108-L128), and [CI workflow](https://github.com/physicsvigilante/sim_heat/blob/a570e3c589457d21b6673701a2d126d7046e1c3c/.github/workflows/h1-c1-f02-build-text-preview.yml) shows:

- The new adapter calls **only** `build_script(study, staged/SimHeat.mo, staged/model.mo)`, an existing pure string formatter. It never calls `h1_native_batch.prepare`, `execute`, `invoke`, `reference.prepare`, `subprocess` or an OMC executable. Importing the old runner loads definitions (including an unused `subprocess` import) but the old runner's `main` is guarded by `if __name__=='__main__'`. The forbidden old `prepare` does regenerate reference data and remains disallowed.
- Saved `unexecuted-build-script.mos.txt` is **797 bytes**, SHA-256 `eeb216779afc98986fc1c2649c07a036d835743a9118971a21a8f7acddad110e`, matching both manifest and receipt. It contains one **unexecuted text** `buildModel(TwoBufferParallelBridge, ...)`. MSL `loadModel(Modelica, {"4.0.0"})` and version guard; `loadFile` for the CI-host-specific absolute staged `SimHeat.mo` and `model.mo`; start `0`, stop `1810.609003248995` seconds, 4000 intervals, tolerance `1e-8`, `method="dassl"`, `fileNamePrefix="model"`, `outputFormat="mat"`, `variableFilter=".*"`, and prospective MSL source/version text logging. It is **not** a portable attested native plan.
- Only CLI actions `preview-text-only` / `verify-preview-only` are available. Saved CI stderr shows `invalid choice` refusal for each `execute`, `compile`, `build`, `launch`, `native`, `approve`, `run`. Source/test cases refuse repeated label, unsafe label, changed script, forged `true` permission, duplicate metadata key, modified staged model, mismatched stage label, missing/extra files including `build.mos`; inherited staging tests check source/reference tamper and other negative paths.
- The ZIP preview subdirectory contains **exactly two** files, TXT script and `NONNATIVE_BUILD_PREVIEW_MANIFEST.json`; no native `build.mos`, executable, MAT trace or simulation output. Manifest/receipt declare all native, owner-launch, host-observed, reference-regenerated, one-shot and qualification flags false (noting F-01 allows numeric type drift if manifest is later edited).

Generating Modelica code-like text in a public repository is acceptable for this **data-only** review under clear refusal/permission boundaries; it is also manually copyable and must not be treated as executable authority.

### F-03 — Historical scientific failure and native gates preserved, NOT resolved

The original frozen F0 `hotLead.G` static checking accuracy had only **80×** margin against required **≥100×**; original FAIL continues (the first frozen failed reference seal was `d76c98f37a0629b56d977c960d1e75694e1121832a9d5281f68bb972d31a365b`). The historical PR32 attempt at bitwise regeneration of approved PR31 V2 across two hosts also **FAILED**. This PR does not fix either or claim native qualification. The nine original public requests remain **not_computed** by native OpenModelica. No compiler query, model build/launch, or native MAT measurement was authorized or performed here.

## Independently inspected provenance and CI evidence

**Source identities:** I separately fetched source contents at the exact pinned head and independently SHA-256 hashed their decoded UTF-8 bytes (not just read prose claims):

| Identity | Confirmed raw SHA-256 |
|---|---|
| Original first-author `h1/cases/H1_C1_MODAL/model.mo` (872 bytes) | `9a165e5ce2cc85da84ecc8bc4e63e2990f2066f3547dc6ba8508fa1afbe5f435` |
| Evaluator-only `h1/cases/H1_C1_MODAL/study.json` (6616 bytes) | `b43e85b6b10afd6550a43322cf98097fe9781a606ee01bc031eadbfd4783b31b` |
| Original `experiments/h1_spike/SimHeat.mo` (3674 bytes) | `e57955b6c32cb34321a6b1908306c4ea9a63ae259b95a5fd48c7e8d3b4da10ea` |
| Frozen `tools/h1_native_batch.py` (14329 bytes) | `f2e43274f2eb08f58dcff34b327bac7c36bdba7c367efe6994cdb4fb335b61e1` |

The new source uses the previous PR37 strict six-file stage/readback, independently pinned disabled preview and original source/checker identities. Workflow `sha256sum --check` reports **14/14 frozen original source pins OK**; inherited offline checks include the older 23 source-plan pins. Actual CI `focused-diff.txt` independently matches GitHub's exact-base four-additions-only comparison.

**Original saved scientific reference, independently retrieved:** I separately downloaded original [PR31 run #43915934653 artifact #14249313720](https://github.com/physicsvigilante/sim_heat/actions/runs/43915934653/artifacts/14249313720), ZIP size **2,348,945 bytes**, SHA-256 `d9259837e0e03c70989b50b2c9dcbf13aca260da4d1cb0ae000b2a23ef65732e`, **13/13 CRC-valid**. Its original `C1_REFERENCE_V2_BUNDLE.json` is **4,409,800 bytes**, independently computed raw SHA-256 `0db511dd8dba023d16518667de256029cf3e073463ea21e2478aeac8afd1f368`, saved canonical seal `d2b8e2ca8e1f929cac7b028dcc3f7d0b453921d193f877eb091e23ac70aa4ce9`. The repeated PR31 original JSON is byte-identical. I inspected **37/37 channel arrays each 4001 samples**, and the 4001-point time grid. These raw identity/seal values match PR38's new manifest/receipt and prior fixture manifest. PR38's workflow separately checked Git-XZ archived fixture SHA `fc5a7df5928c3fb8aef2ba4af516dfbd32b42c0450ebef1051ad4fd7efebd17f` and fixture manifest SHA `50467b138ed64cdb908f2c763bc777e6babf0bb04a0711568acc559112e66f84`. **Limitation:** PR38's compact ZIP does not itself include the staged 4.4 MB reference; its staging bytes were checked by the source-executed CI and traced receipts, not personally recovered from that compact ZIP.

**PR38 exact-head CI and saved artifact, independently inspected:**

- [Run #44030612438](https://github.com/physicsvigilante/sim_heat/actions/runs/44030612438) `event=push`, `head_sha=a570e3c...`, attempt 1, `status=completed`/`conclusion=success`. All job steps succeeded; `contents:read`, checkout `persist-credentials:false`, no paths filter, only Python checking dependencies and offline testing; **no OMC/Modelica installation or CLI invocation**.
- [Artifact #14305570982](https://github.com/physicsvigilante/sim_heat/actions/runs/44030612438/artifacts/14305570982): personally downloaded **22,033 bytes**; independently computed full ZIP SHA-256 **`7e3196d673c0b2a1d71166da81b1ac58fdcd256121c3029e61fc2b37525179f1`**; **33/33 ZIP CRC valid**. Saved `head-sha.txt` and `head-tree.txt` match reviewed Git SHA and tree. Saved preview/receipt and source file hashes verified; `text-preview-receipt.json` and `text-preview-readback.json` are byte-identical, with status `NONEXECUTABLE_BUILD_TEXT_PREVIEW_VERIFIED` and all receipt native flags false.
- Inspected all seven saved negative CLI stderr files; every unauthorized action returned argparse invalid-choice refusal with empty stdout. Inspected new and inherited negative-test names and their hosted PASS/OK outcomes. The new numeric-zero/float adversarial case is **not covered** (F-01).

**229/229 hosted OFFLINE unittest methods passed, counted from saved actual logs, not personally rerun:**

| CI suite | Count | Result |
|---|---:|---|
| New build-text preview | 12 | OK |
| Original strict staging | 24 | OK |
| Disabled control/type preflight | 16 | OK |
| Owner-approved offline reference consumer | 11 | OK |
| Immutable reference binding | 8 | OK |
| Archive/fixture integrity | 9 | OK |
| Original frozen H1 | 149 | OK |
| **Total** | **229** | **All hosted suites OK** |

**Personally run offline checks:** downloaded ZIP byte SHA/CRC checks, direct source-text SHA computation for four original files, original PR31 reference raw SHA/shape/seal checks, script/manifest/receipt crosschecks, saved CLI denial-inspection, and independent Python-dictionary mutation replay of F-01. **Not run:** full 229-suite locally, real source `preview.verify` against a mutated stage, a native compiler/version command, build, simulation, MAT decoding, browser capture, or new scientific reference calculation. The exact-head CI logs show the 229-suite execution by GitHub, not by Chat B.

## Separate scope judgments

| Dimension | Judgment | Basis |
|---|---|---|
| Source interpretation fidelity | **PASS (limited)** | Original model, modal study and library independently hashed; stage and one text-only formatter bind the original named model and nine requests. |
| Physical/numerical correctness | **NOT QUALIFIED** | No new physics computation; original frozen F0 80× failure and PR32 regeneration failure preserved, not repaired. |
| Native simulation/observable coverage | **NOT RUN / UNKNOWN** | No OMC, compiled setup, 37 native exports, MAT trace, or the nine measured outputs. |
| Evidence integrity and provenance | **CHANGES REQUESTED** | All major source/reference/ZIP pins corroborate, but F-01 allows equal-valued JSON type drift on exact manifest readback. No authenticated release trust root. |
| Teacher-facing usefulness | **NOT EVALUATED** | This is private engineering evidence formatting, no viewer/student interaction tested. |
| Textbook-answer completeness | **NOT APPLICABLE** | No problem-answer coverage work. |

## Required correction and remaining native safeguards

**Required before a scoped offline PASS:** fix **F-01** in the new readback only, add literal-type/canonical-manifest regression(s), push a **new exact head**, rerun the full relevant CI and perform a focused correction re-review. Do not change frozen original physics, reference data, native runner, source author files, numerical tolerance or historical failure records. Retain this review as the first outcome for `a570e3c...`.

**Still separately required for any future native attempt, unaffected by eventual offline PASS:** (1) owner-authenticated protected source/release root and retained verified backup; (2) a distinct non-regenerating **executable** adapter and exactly pinned prospective plan, source and original saved scientific reference; (3) authenticated target host, OMC, MSL 4.0.0, compiler/runtime fingerprints and effective build/experiment/export checks (including 37 variables); (4) atomic durable cross-run one-shot reservation/no retry, with partial/failure evidence retained; (5) independent **pre-native R2** on that actual executable adapter and plan; (6) **new, explicit owner approval** for a single specifically named version-query/build/launch budget; then (7) independently reviewed native traces, MAT and numerics afterward. The passive script includes absolute paths tied to the ephemeral CI runner and is not a trusted host-specific executable launch artifact.

**Hard stop respected:** no OpenModelica invocation, installation, physical edits, old PR merges, tolerance relaxations, source reclassification, or native authorization. **Final verdict at the reviewed SHA: CHANGES REQUESTED (offline manifest readback integrity only).**
