# SIM_HEAT PR #44 — independent Chat B R2 review (review-01)

**VERDICT: SCOPED PASS — READ-ONLY, ALWAYS-BLOCKED UNTRUSTED LOCAL ARTIFACT INTAKE ONLY.** At the reviewed SHA, the inventory does not promote nine local native-looking filenames, forged owner/native assertions, a modified fake-CAS receipt, synthetic MAT/CSV bytes, or matching local SHA-256 hashes into authenticated evidence or launch authority. No demonstrated blocker to this **denial-only** scope was found. **This is NOT a post-native verification engine, native result qualification, source release, owner signature, real across-run reservation, OMC authorization or production-merge approval. All eleven real native-release gates remain MISSING and all nine C1 native public requests remain NOT COMPUTED.**

- **Source:** [physicsvigilante/sim_heat](https://github.com/physicsvigilante/sim_heat), historical [draft PR #44](https://github.com/physicsvigilante/sim_heat/pull/44); open and unmerged when checked. **Do not merge historical F0 PRs into production main.**
- **Immediate reviewed base:** PR #43 `4e220a152e702c06b07320850f5caacff1091bb3` (tree `4a931c0e017eb650c0b4a63c5dfdf38097ad9d72`).
- **Exactly reviewed HEAD:** `331a04c34d465516ffb0ecbb580a334032fa7de2`.
- **Exactly reviewed Git tree:** `fa139f1421c0c763600d1dc3650d152b3157e543`, independently cross-checked with the Git commit API, GitHub Actions run metadata and downloaded artifact.
- **Source diff:** [exact base-to-head comparison](https://github.com/physicsvigilante/sim_heat/compare/4e220a152e702c06b07320850f5caacff1091bb3...331a04c34d465516ffb0ecbb580a334032fa7de2): **four added paths, zero pre-existing modifications/deletions**: `qualification/h1_c1/f02/offline_native_artifact_intake.py`, `qualification/h1_c1/f02/test_offline_native_artifact_intake.py`, `qualification/h1_c1/f02/UNTRUSTED_NATIVE_INTAKE_SCOPE.md`, and `.github/workflows/h1-c1-f02-untrusted-native-intake.yml`.
- **Original frozen F0:** `dd8c9432abe97563414bb3ed809e61e673473812`.
- **Reviewer:** independent Chat B, GPT-6, separate conversation, 2026-11-17 (Asia/Kolkata). Separate chat context is not human expert independence or proof of distinct model weights.
- **Risk/scope:** R2, provenance/native-qualification boundary; no new physics or native execution. Read the [central request](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-44/REQUEST.md), reviewer prompt, status, `PROTOCOL.md`, `REVIEW-RISK-POLICY.md`, `REVIEW-TEMPLATE.md`, prior Chat B PR43 report, pinned intake/tests/scope/workflow and inherited PR41/PR37 audit/parser. No source-root `AGENTS.md` was found at the pinned ref.
- **Source edits made during review:** none. Only this new Chat B report is committed to `review_sandbox`.
- **Exact-head hosted evidence:** [CI run #44062963378](https://github.com/physicsvigilante/sim_heat/actions/runs/44062963378), push/attempt 1, completed SUCCESS at the pinned SHA; [artifact #14319136950](https://github.com/physicsvigilante/sim_heat/actions/runs/44062963378/artifacts/14319136950), **27,322-byte** original ZIP, independently downloaded and SHA-256 rehashed to **`a76e171341f5002ff2654bd109952ba20911debfac0bdf78711761866be6152c`**, **41 unique members, 41/41 CRC-valid**. One successful job `133969287639`.

## Independent findings

### F-01 — PASS: exact scope, source identity and frozen evidence preservation

**Basis:** exact Git comparison and commit/tree, [source workflow](https://github.com/physicsvigilante/sim_heat/blob/331a04c34d465516ffb0ecbb580a334032fa7de2/.github/workflows/h1-c1-f02-untrusted-native-intake.yml), saved `source-diff.txt`, `source.sha256`, `frozen-f0-pins.txt`.

The commit really adds only the four advertised paths. The archived CI source inventory lists 179 tracked-file hashes; all **14 original F0 frozen source hash checks** explicitly report OK. The original unlaunched disabled F02 preflight reports 23 verified source/plan pins. Original first-author and modal model files retain SHA-256 `9a165e5ce2cc85da84ecc8bc4e63e2990f2066f3547dc6ba8508fa1afbe5f435` and the evaluator modal study retains `b43e85b6b10afd6550a43322cf98097fe9781a606ee01bc031eadbfd4783b31b` in the saved source SHA inventory. No old checker, physics, runner, reference, owner record, scientific threshold or native plan was changed by this diff.

The approved original PR31 V2 analytical checking-only reference remains pinned to **raw SHA-256 `0db511dd8dba023d16518667de256029cf3e073463ea21e2478aeac8afd1f368`**, canonical seal `d2b8e2ca8e1f929cac7b028dcc3f7d0b453921d193f877eb091e23ac70aa4ce9`, archived XZ SHA `fc5a7df5928c3fb8aef2ba4af516dfbd32b42c0450ebef1051ad4fd7efebd17f` and whole saved manifest SHA `50467b138ed64cdb908f2c763bc777e6babf0bb04a0711568acc559112e66f84`. The last two checks ran successfully in hosted CI, not in a new local extraction by this reviewer. The pinned checking data is not owner authentication.

The [F01 original static rounding disposition](https://github.com/physicsvigilante/sim_heat/blob/331a04c34d465516ffb0ecbb580a334032fa7de2/qualification/h1_c1/evaluation/F01_STATIC_REFERENCE_DISPOSITION.md) remains negative: `hotLead.G` was stored as `0.44999999999999996` W/K against exact `9/20` W/K. I separately recalculated its exact-rational error `4.440892098500626e-17` W/K and the original `64*ulp` allowance `3.552713678800501e-15` W/K, giving **80×, not the required ≥100×: FAIL**. The [PR32 saved original-seal cross-host comparison](https://github.com/physicsvigilante/sim_heat/blob/331a04c34d465516ffb0ecbb580a334032fa7de2/qualification/h1_c1/evaluation/C1_REFERENCE_V2_CROSSHOST_FINDINGS.md) still records **bitwise original-seal reproduction FAIL**; its alternate generated V2 seal is not adopted. Neither historical issue is remedied or waived by green offline tests.

### F-02 — PASS: inherited scientific HOLD and eleven real gate refusals remain authoritative

**Basis:** [intake lines 113–153](https://github.com/physicsvigilante/sim_heat/blob/331a04c34d465516ffb0ecbb580a334032fa7de2/qualification/h1_c1/f02/offline_native_artifact_intake.py#L113-L153); pinned `offline_release_readiness_hold.py`, `RELEASE_GATES_ABSENT.json`, disabled F02 `offline_control_preflight.py`.

Before accessing candidate files, `inspect_only` invokes `readiness.audit`. The inherited audit validates the exact Git-blob-pinned absence declaration (`cf0d9841a7312082db038ef999ee307691987e44`), original source/model/reference binding and nonexecuting F02 plan, and the fake external-CAS denial contract. Its release declaration has **eleven `null` prerequisites** and literal-false native/owner/release flags. The new intake checks the returned HOLD status, eleven missing gates, native/owner/reservation false fields and original saved reference raw SHA/seal. A false nativeAllowed or changed reference seal caused explicit refusal in isolated adversarial tests. The real inherited tests and full readiness audit passed in exact-head CI.

This is a test that prerequisites **remain absent**. Neither the declaration nor its matching hash becomes a release credential. Local evidence files do not modify the inherited audit or close a single actual gate.

### F-03 — PASS: all nine forged native-looking filenames cannot promote evidence

**Basis:** [intake lines 34–52, 78–153](https://github.com/physicsvigilante/sim_heat/blob/331a04c34d465516ffb0ecbb580a334032fa7de2/qualification/h1_c1/f02/offline_native_artifact_intake.py#L34-L153); [new tests](https://github.com/physicsvigilante/sim_heat/blob/331a04c34d465516ffb0ecbb580a334032fa7de2/qualification/h1_c1/f02/test_offline_native_artifact_intake.py).

I ran an **additional isolated case against an SHA-matched, byte-identical 196-line copy of the actual intake implementation**. The candidate folder contained all nine allowed names. Each JSON candidate asserted fabricated `ownerSigned`, `nativeQualified`, `trustedReleaseReady`, `nativeAllowed`, `nativeExecuted`, `OWNER_SIGNED_APPROVED` and fake-CAS counts; `model_res.mat` contained synthetic non-MAT bytes; `normalized.csv` contained fictitious numerical observations. The *executed intake code* returned **`BLOCKED_UNAUTHENTICATED_NATIVE_ARTIFACT_INTAKE`**, **`missingFilenames=[]`**, nine `localFilesOnly` records, **`releaseBlocked=true`**, **`nativePublicRequestsStillNotComputed=9`**, **`allFileNamesPresentWouldBeNativeProof=false`**, **`localFileHashesAreAuthenticProvenance=false`**, and **every one of the 15 `NO_EXECUTION_FIELDS` literal false**. Each file's `originAuthenticated` and `nativeEvidenceVerified` was false.

A separate forged fake-CAS scenario from PR43 F-06 changes the receipt `status` and `fakeCounts.oneFakeFirstClaims` (999), without any authentication. The repository's hosted test `test_false_owner_or_fake_CAS_never_accepted_from_prior_stage` passed; it also invokes the old fake `require_real_native_permission` and expects refusal. The inventory itself does not trust or interpret that receipt. Local byte hashes merely fingerprint mutable attacker-supplied data. **Nine candidate file names are not the nine public physical observables.**

### F-04 — PASS, with explicit trust boundary: malformed and unsafe local candidates refuse

**Basis:** [intake lines 58–111](https://github.com/physicsvigilante/sim_heat/blob/331a04c34d465516ffb0ecbb580a334032fa7de2/qualification/h1_c1/f02/offline_native_artifact_intake.py#L58-L111), inherited `stage_immutable_inputs.strict_metadata`.

The separately executed isolated probes covered nested and top-level duplicate JSON keys; explicit `NaN`, `Infinity` and `-Infinity` tokens; malformed JSON, invalid UTF-8, wrong top-level JSON type; empty and oversized files; unexpected executable-looking `build.mos`; symlinked candidate parent, folder and member; invalid/escaping labels; and absent folder creation. Every expected refusal occurred. Valid present candidates are regular files with bounded local byte counts and SHA-256 only. Hosted full-source tests independently corroborate these classes.

**Scope boundary:** this is only local, best-effort checking. `Path.resolve`, `is_symlink`, `stat`, `read_bytes` and JSON parsing are separate operations; the JSON parser reopens the file after its inventory bytes were hashed. A concurrently malicious writer could change bytes, directory entries or links between checks. There are no directory-fd/openat/`O_NOFOLLOW`/atomic-snapshot guarantees, no signed identity, no network provenance and no multi-host CAS. This is expressly acknowledged in the scope and result limits; do not present it as a secure file-verification service. All results remain denied even if local inspection succeeds.

### F-05 — PASS: no native decode, reference regeneration, OMC call or native action

**Basis:** intake import/call graph and CLI [lines 156–196](https://github.com/physicsvigilante/sim_heat/blob/331a04c34d465516ffb0ecbb580a334032fa7de2/qualification/h1_c1/f02/offline_native_artifact_intake.py#L156-L196), test `test_no_native_MAT_decoder_reference_regenerator_or_subprocess` and exact-head workflow/job log.

The intake imports standard-library parsing/path/hashing tools plus inherited **read-only** `readiness` and `staged` parser. It does not import or call the MATv4 decoder, reference preparer, native batch preparer/execute/invoke, OMC, a command runner or a remote owner/CAS provider. It only hashes `model_res.mat` bytes and never reads CSV numerically. The hosted guard test mocks `matv4.decode_mat_file`, `reference.prepare` and `h1_native_batch.prepare/execute/invoke` to fail if called, and passed. Workflow commands are offline Python checks and source/reference SHA validations; no OMC install/version query/build/launch or native MAT acceptance was observed in its logs or artifact.

The only accepted CLI action is `inspect-untrusted-files-only --label <safe-label>`; **exit 0 means a BLOCKED inspection completed, not PASS/native-qualified**. Ten forbidden action strings (`native`, `execute`, `approve`, `run`, `build`, `launch`, `omc`, `reserve-native`, `verify-native`, `qualify`) all had argparse rejection in the saved stderr and empty stdout. Inspecting the real native data or regenerating a reference is outside this program's scope.

### F-06 — MINOR, non-blocking precision issue: exponent overflow can yield a nonfinite parsed value

**Independent novel input:** `{"value":1e999,"status":"OWNER_APPROVED"}` inside a permitted JSON filename.

The inherited strict JSON parser rejects *explicit nonstandard* `NaN`/`Infinity` tokens using `parse_constant`, but standard-syntax `1e999` is decoded by Python as `float('inf')`. I executed this edge case in the isolated exact-intake probe: the file **was inventoried**, but the receipt remained **BLOCKED**, unauthenticated and unqualified. Therefore this is **not** an authorization/denial defect for this PR. It does mean prose should say “rejects nonstandard NaN/Infinity constants” rather than claim comprehensive rejection of every representationally nonfinite parsed number.

**Non-blocking improvement:** if a future contract requires genuinely finite parsed JSON values, reject float overflow with `parse_float` and/or recursively check finite floats; add a regression. Do not turn additional parser acceptance checks into authenticity or native approval. No change is required to preserve the present always-BLOCKED contract.

### F-07 — PASS: exact-head offline CI/artifact reconciliation, not native qualification

I personally downloaded the real ZIP from GitHub Actions through the connected GitHub client; independently calculated **27,322 bytes**, SHA-256 **`a76e171341f5002ff2654bd109952ba20911debfac0bdf78711761866be6152c`**, **41 unique filenames** and **zero ZIP CRC errors**. Extracted `head-sha.txt` and `head-tree.txt` match GitHub commit and CI metadata; `source-diff.txt` has exactly four `A` entries and no others. The actual `untrusted-native-INCOMPLETE.json` says all nine candidate names absent, **11 release gates missing, 9 public requests not computed**, and all authority/native/history-success flags false. Ten rejected CLI action stderr/stdout pairs were inspected.

I read all **13 saved unittest transcripts** (including individual method result rows and summary line) and reconciled **329/329 passing offline methods**, all `OK`, zero failed/error methods:

| Suite | Hosted offline methods passed |
|---|---:|
| New untrusted intake/forgery/refusal | 20 |
| PR43 stale-snapshot fake CAS | 16 |
| Hypothetical one-shot state | 18 |
| PR41 release readiness HOLD | 15 |
| Untrusted external CAS contract | 16 |
| Local SQLite simulator | 12 |
| Nonexecuting Modelica build-text preview | 15 |
| Exact immutable input staging | 24 |
| Disabled F02 control plan | 16 |
| Owner-approved OFFLINE reference consumer | 11 |
| Source/reference binding | 8 |
| Original PR31 reference archive | 9 |
| Frozen H1 physics/source checks | 149 |
| **TOTAL** | **329** |

The workflow declares `contents: read` only, SHA-pinned checkout/setup/upload actions, `persist-credentials: false`, Python 3.13.5 and checking packages, and an unfiltered push on the historical source branch. Read-only CI test success proves the reviewed **offline** behaviors; it does not prove native observation or owner approval.

## Personally executed vs CI-inspected evidence

**Personally executed:** 25 disposable isolated adversarial probes of the **exact same 196-line intake module bytes** (locally reconstructed and independently SHA-256 matched to the actual exact-head CI `source.sha256` entry: `e08050f130e102b82531dd0d7cad71f10a8dd3e5efc7d164a9ec9c9981058ac6`). They include the full nine-file forged owner/native/CAS/MAT/CSV packet, absent folder, duplicate-key/nonfinite/malformed/wrong-root/oversized/extra-file/symlink/label refusals, upstream inflated release and altered reference seal, plus the `1e999` edge case. **25/25 passed their stated expected behavior.** I intentionally supplied *test doubles* for the inherited `readiness.audit` and `stage.strict_metadata` integration: the former used the verified offline BLOCK receipt's baseline fields, the latter reproduced the inspected strict JSON parsing algorithm. These probes directly execute the byte-identical intake body, **not** the entire original repository or authenticated external gate. Their PASS is bounded accordingly.

**Personally downloaded/inspected:** exact original hosted CI artifact, its whole ZIP SHA and member CRC, actual receipt/10 CLI rejection pairs/13 full transcripts/source SHA inventory/head-tree-diff records, GitHub current PR and commit metadata, job summaries/log, pinned changed source/tests/scope/workflow and inherited readiness/parser/absence declaration, frozen historic failure documents. Separately computed the original static `hotLead.G` 80× error from rational arithmetic.

**Observed through exact-head hosted CI, not personally rerun:** 329 actual unmodified repository unittest methods, full inherited source/reference hold, 14 original frozen SHA checks, original 23-input preflight, archived PR31 XZ/manifest hash checks and native-call guard mocks. I could not clone the full repository into the isolated reviewer container (GitHub DNS unavailable), so I did **not** rerun those 329 methods or independently decompress/re-hash the archived 4,409,800-byte reference. All such qualifications are attributed to independently inspected hosted CI artifacts, not claimed as personally executed. No OpenModelica, native query/build/launch, MAT decode, reference generation, external CAS, owner signing or native numerical verification was performed by this reviewer.

## Separate scope judgments

| Dimension | Judgment | Basis |
|---|---|---|
| Source interpretation fidelity | **PASS — denial/inventory only** | Fixed names, bounded hashes, explicit untrusted fields, 11-gate HOLD, refusal conditions and 25 isolated tests |
| Physical / numerical correctness | **NOT QUALIFIED; frozen historical failures preserved** | No new physics; old F0 80×/100× FAIL and PR32 bitwise FAIL remain |
| Native simulation and observable coverage | **NOT QUALIFIED — zero** | No OMC, MAT decoding or 9 computed public native requests |
| Evidence integrity and provenance | **PASS for SHA-pinned OFFLINE CI; NO trusted native provenance** | Exact HEAD/tree, 41 CRC-valid ZIP members, 329 hosted tests; local candidate hashes/synthetic claims never authenticated |
| Teacher-facing usefulness | **LIMITED / NOT EVALUATED** | Offline safety/provenance exercise, not a teacher-facing thermal simulation |
| Textbook-answer completeness | **NOT APPLICABLE** | No exercise solving or native verification |

## Release advice / strict hard stop

**SCOPED PASS does not close any actual native release gate.** All eleven remain explicitly missing: named-budget owner permission; authenticated protected reviewed source/reference release; independently protected reference backup; live signed source provenance; reviewed non-regenerating executable native adapter; exact pinned executable plan/runner; trusted host and OMC executable identity; observed OMC/MSL/compiler/runtime; genuinely shared owner-controlled transactional CAS; durable unique across-run reservation/crash/no-retry receipts; independent pre-native R2 and post-native evidence policy. Current JSON/ZIP hashes are local content checks, not owner cryptographic credentials or protected release roots.

No source edits, new physics, native work, alternate PR32 seal adoption, frozen-threshold waiver, production merge, signed owner release or native budget allocation are justified. Historical PR #44 remains draft/unmerged. A future real native campaign would require **new independent pre-native review and separate explicit owner approval for the exact named OMC version-query, build and single-model-launch/no-retry budget**, with all source/host/release/backup/shared-CAS prerequisites independently established; this report supplies none of those permissions.

**Final verdict: SCOPED PASS — ALWAYS-BLOCKED LOCAL UNTRUSTED FILE INTAKE ONLY. NO NATIVE LAUNCH, NATIVE QUALIFICATION OR PRODUCTION MERGE AUTHORIZED.**
