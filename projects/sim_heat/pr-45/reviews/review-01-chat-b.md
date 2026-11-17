# SIM_HEAT draft PR #45 — independent Chat B R2 review (review-01)

**VERDICT: SCOPED PASS — ONLY the finite-JSON and same-captured-byte correction to an ALWAYS-BLOCKED, READ-ONLY, UNTRUSTED local native-looking file inventory.** No demonstrated in-scope blocker. This is **NOT** trusted native evidence, a post-native verifier, an approved release, an owner signature, a real cross-host reservation, native-result qualification, a production merge, or authorization for any OpenModelica query/build/launch. **All 11 native-release safeguards remain MISSING; all nine actual native public readings remain NOT COMPUTED.**

## Identity, scope and reviewed source

- Project: [physicsvigilante/sim_heat](https://github.com/physicsvigilante/sim_heat), historical unmerged **draft [PR #45](https://github.com/physicsvigilante/sim_heat/pull/45)**; do not merge historical F0 branches into main.
- Immediate independently reviewed base: PR44 commit **331a04c34d465516ffb0ecbb580a334032fa7de2**, tree **fa139f1421c0c763600d1dc3650d152b3157e543**. Its original [Chat B scoped PASS](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-44/reviews/review-01-chat-b.md) remains valid and its F-06 observation is the sole correction target.
- **Exactly reviewed head:** **278f8224fa23ec20bc6c7342ab433b9be17e4434**; independently checked Git tree **fc0dbe955a14a73e7e54dd8060cb5d469a6f91e6**. [Exact commit comparison](https://github.com/physicsvigilante/sim_heat/compare/331a04c34d465516ffb0ecbb580a334032fa7de2...278f8224fa23ec20bc6c7342ab433b9be17e4434) is ahead five commits and touches **exactly FOUR paths: 3 modified, 1 added**.
- Modified: qualification/h1_c1/f02/offline_native_artifact_intake.py; qualification/h1_c1/f02/test_offline_native_artifact_intake.py; qualification/h1_c1/f02/UNTRUSTED_NATIVE_INTAKE_SCOPE.md. Added: .github/workflows/h1-c1-f02-intake-finite-json.yml. No inherited physics, study, checker, source/staging/readiness declaration, owner decision, scientific reference, native runner or frozen plan changed in this comparison.
- Original frozen F0 commit **dd8c9432abe97563414bb3ed809e61e673473812**.
- Reviewer: independent **Chat B, GPT-6**, separate ChatGPT conversation; **2026-11-17, Asia/Kolkata**. Context is independent from the implementer conversation, not human independence or proof of different model weights. R2 evidence/provenance semantics, bounded to this correction.
- Reviewer modified **no sim_heat source or frozen science** and did not merge any PR. This new report is the only intended GitHub write.
- Read [PR45 request](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-45/REQUEST.md), central review protocol/risk policy/template, PR44 independent review, exact pinned code/tests/scope/workflow, inherited JSON callbacks/readiness HOLD, reference manifest/Option A adoption, two historical scientific-failure documents, exact-head CI logs and original artifact. No root AGENTS.md was found at the pinned source ref.

## Independent findings

### F-01 — PASS: PR44 F-06 standard JSON exponent-overflow loophole is corrected

**Source:** [exact intake source](https://github.com/physicsvigilante/sim_heat/blob/278f8224fa23ec20bc6c7342ab433b9be17e4434/qualification/h1_c1/f02/offline_native_artifact_intake.py), functions _finite_float and _strict_untrusted_object; [new regression methods](https://github.com/physicsvigilante/sim_heat/blob/278f8224fa23ec20bc6c7342ab433b9be17e4434/qualification/h1_c1/f02/test_offline_native_artifact_intake.py).

PR44 correctly rejected nonstandard JSON constants through staged._reject_nonfinite but ordinary Python JSON float parsing could turn legal exponent notation such as 1e999 into infinity. New json.loads(parse_float=_finite_float) explicitly requires math.isfinite(float(token)). Standard-syntax 1e999, -1e999, 1E+9999 and deeply nested -2.5e999 now produce IntakeRefusal ("nonfinite JSON number in untrusted file"). Retained staged._reject_nonfinite refuses NaN, Infinity and -Infinity tokens; retained staged._no_duplicate_pairs refuses contradictory duplicate keys at top level and in nested objects. The top-level object rule remains.

**Personally executed:** 12 overflow refusals across three allowed JSON filenames; 3 nonstandard-constant refusals; 2 duplicate-key refusals; 3 malformed/UTF-8/non-object refusals. Five independent finite-exponent/finite-number controls, including 1e308, -1e308, 1e-308, underflow to zero, and forged truthy approval, returned the unchanged **BLOCKED** status and false authority fields. Parsing is format checking only, not scientific or owner verification.

**Finding:** correction satisfies the narrow F-06 requirement; no demonstrated blocker.

### F-02 — PASS, bounded: parsing and the SHA inventory use exactly one captured file-read result

**Source:** the same intake module, _inventory. For each JSON candidate, the code reads raw = path.read_bytes() once, verifies len(raw) against the prior stat size, passes raw to _strict_untrusted_object(raw), then hashes the same raw using _sha(raw). The prior staged.strict_metadata(path, ...) call, which would reopen by pathname, was removed from this path. The inherited strict duplicate/constant callbacks remain, but **the old pathname parser is not called**.

**Personally executed stronger adversarial controls:** substituted a single captured finite JSON byte sequence in the read while the on-disk JSON instead contained a same-length overflowing exponent. The result stayed BLOCKED, the file was read once, and the reported untrusted SHA matched exactly the **captured finite bytes**, not the different bytes on disk. In the reverse condition, the one captured read returned overflow bytes while the disk was finite; parsing rejected those captured bytes. A stub for staged.strict_metadata would raise if invoked and was not invoked.

**Important explicit limitation:** directory listing, symlink checks, stat, per-file read and inspection of separate files are different filesystem operations. Mutable entries can be replaced or changed by concurrent actors; matching byte counts do not prove unchanged identity. The implementation **does not create an atomic filesystem snapshot**, authenticated writer, protected release or durable shared CAS. The improvement closes the second-read discrepancy only; it is not a general TOCTOU cure.

### F-03 — PASS: even nine forged native-looking files and finite JSON remain unauthenticated and BLOCKED

**Personally executed:** all nine allowlisted files present in a disposable folder; every JSON claimed ownerSigned, nativeQualified, ownerNativeLaunchApproved, trustedReleaseReady, readingsComputed and nativeExecuted; model_res.mat and normalized.csv contained synthetic, deliberately non-native bytes. The actual intake function returned **BLOCKED_UNAUTHENTICATED_NATIVE_ARTIFACT_INTAKE** with zero missing filename entries, nine local hash-only records, releaseBlocked=true, nativePublicRequestsStillNotComputed=9, both provenance booleans false, every candidate originAuthenticated/nativeEvidenceVerified=false, and **all 15 NO_EXECUTION_FIELDS false**.

Source inspection confirms MAT/CSV are hashed only, never decoded or scientifically interpreted; JSON parsed values are ignored for native authority. Only the CLI action inspect-untrusted-files-only --label exists; success exit code 0 means an explicit **BLOCKED inventory**, not a native success. A malformed candidate refuses. Neither the intake import/call graph nor the CI workflow executes OMC, reference.prepare, MAT decode, native runner, signing or external CAS. The previously reviewed fake-CAS and release-HOLD refusal architecture is inherited unchanged.

### F-04 — PASS for precise CI/archive attribution, **not** independent re-execution of all hosted tests

**Current-head [CI run #44066896537](https://github.com/physicsvigilante/sim_heat/actions/runs/44066896537):** push, attempt 1, status completed, **SUCCESS**, exact head 278f8224fa23ec20bc6c7342ab433b9be17e4434. One successful job **133982780892**, with offline checkout, Python 3.13.5, offline packages, source/diff/reference/frozen pin checks, 13 unittest suites, denied CLI actions and artifact archiving. I inspected actual hosted job logs as well as the downloaded original ZIP.

**[Artifact #14321730592](https://github.com/physicsvigilante/sim_heat/actions/runs/44066896537/artifacts/14321730592):** I personally downloaded the original **27,486-byte** ZIP through the connected GitHub client and recomputed whole-file SHA-256 **b8ab525db9088747ccafdc8bab6e9e25f1c7922894ce9800b82a5bad11230587**. Exactly **41 unique ZIP members; 41/41 CRC valid**. Archived head-sha.txt is 278f8224fa23ec20bc6c7342ab433b9be17e4434; head-tree.txt is fc0dbe955a14a73e7e54dd8060cb5d469a6f91e6; source-diff.txt names exactly the 3 M + 1 A paths above. These agree with independently queried GitHub commit/tree/compare metadata. Source hash inventory contains 180 tracked paths.

I inspected all 13 complete saved unittest transcripts, including method outcomes, totals and OK conclusions. **333/333 hosted OFFLINE unittest methods PASS**, with no reported failing/error suites:

| Hosted offline test suite | Passing methods |
|---|---:|
| Untrusted native intake, including 4 new F-06 tests | 24 |
| Stale-snapshot fake CAS | 16 |
| Hypothetical one-shot state model | 18 |
| Release-readiness HOLD | 15 |
| Untrusted external fake CAS | 16 |
| Local SQLite demo | 12 |
| Nonexecuting Modelica build-text preview | 15 |
| Immutable staging | 24 |
| Disabled F02 control preflight | 16 |
| Owner-approved OFFLINE reference consumer | 11 |
| Source/reference binding | 8 |
| Original PR31 archived fixture | 9 |
| Frozen original H1 tests | 149 |
| **TOTAL** | **333** |

The archived frozen-f0-pins.txt independently observed as saved CI evidence reports **14/14 source-pin checks OK**. The BLOCKED receipt reports **23 inherited unlaunched native-plan/source pins verified**. The workflow performs SHA checks of original PR31 V2 XZ and complete manifest; the archived source inventory contains both expected hashes. Those CI-run repository checks are **hosted evidence**, not locally rerun full-repository checks by this reviewer. The receipt records all nine optional local candidate files absent, all nine native public observations uncomputed, 11 native gates missing, and all 15 native/owner/science-history success flags false. Ten forbidden CLI commands have rejection stderr and empty stdout in the artifact.

**Honest failure history:** [run #44066782667](https://github.com/physicsvigilante/sim_heat/actions/runs/44066782667) remains **completed FAILURE** at intermediate commit **77f0ef7d998f1403136967169c00f0687e2178c5**, with **zero jobs**. The workflow at that commit had an unquoted step name containing colon-space; exact HEAD separately quotes that step label. The earlier failure is neither deleted nor counted as a passing job. The new successful run is distinct. Previous PR44 [CI #44062963378](https://github.com/physicsvigilante/sim_heat/actions/runs/44062963378) passed **older F-06-affected** source, not this fix.

### F-05 — PASS: unchanged physics/reference inputs and historical negative evidence

The exact four-path diff does not modify any inherited source. In the current ZIP source.sha256, the first-author Modelica model remains **9a165e5ce2cc85da84ecc8bc4e63e2990f2066f3547dc6ba8508fa1afbe5f435**, the evaluator modal study remains **b43e85b6b10afd6550a43322cf98097fe9781a606ee01bc031eadbfd4783b31b**, the original archived PR31 V2 XZ remains **fc5a7df5928c3fb8aef2ba4af516dfbd32b42c0450ebef1051ad4fd7efebd17f**, and the whole manifest remains **50467b138ed64cdb908f2c763bc777e6babf0bb04a0711568acc559112e66f84**.

Current [Option A owner-adoption record](https://github.com/physicsvigilante/sim_heat/blob/278f8224fa23ec20bc6c7342ab433b9be17e4434/qualification/h1_c1/option_a/OWNER_ADOPTION.json) retains **offline checking-only** scope, reference raw SHA **0db511dd8dba023d16518667de256029cf3e073463ea21e2478aeac8afd1f368** (4,409,800 bytes), canonical seal **d2b8e2ca8e1f929cac7b028dcc3f7d0b453921d193f877eb091e23ac70aa4ce9**, no native permission, and no adoption of any alternate PR32 regenerated seal. The original archive manifest still explicitly says approvedForNative=false.

Historical scientifically negative findings are retained:
1. Original frozen F0 reference has hotLead.G stored at 0.44999999999999996 W/K against exact 9/20 W/K. I **personally** recomputed exact rational absolute error **4.440892098500626e-17 W/K** and original 64-ulp allowance **3.552713678800501e-15 W/K**, hence **80×** error margin versus the **required at least 100×: FAIL**. [Frozen disposition](https://github.com/physicsvigilante/sim_heat/blob/278f8224fa23ec20bc6c7342ab433b9be17e4434/qualification/h1_c1/evaluation/F01_STATIC_REFERENCE_DISPOSITION.md).
2. Original reviewed PR31 V2 seal was **not** reproduced bitwise in the PR32 cross-host trial; the alternate host-result seal was not adopted. That historical experiment remains **FAIL**. I inspected its [saved negative findings](https://github.com/physicsvigilante/sim_heat/blob/278f8224fa23ec20bc6c7342ab433b9be17e4434/qualification/h1_c1/evaluation/C1_REFERENCE_V2_CROSSHOST_FINDINGS.md), not a new scientific reference generation.

Green offline CI preserves these negatives; it does **not** make the frozen F0 100× gate pass or qualify any native physical observation.

### F-06 — SCOPE LIMITATION, not a new blocker: native-release prerequisites are still genuinely missing

The unchanged [release-absence declaration](https://github.com/physicsvigilante/sim_heat/blob/278f8224fa23ec20bc6c7342ab433b9be17e4434/qualification/h1_c1/f02/RELEASE_GATES_ABSENT.json) has Git blob **cf0d9841a7312082db038ef999ee307691987e44**; all 11 declared prerequisite values are still **null**, not signed or substantiated. Current CI BLOCKED receipt repeats all eleven exactly:

1. owner_native_launch_approval_for_named_budgets
2. owner_authenticated_protected_reviewed_reference_release
3. independent_retained_verified_reference_backup
4. live_fresh_source_ref_and_signed_commit_attestation
5. reviewed_nonregenerating_executable_native_adapter
6. exact_sha_pinned_native_runner_and_executable_plan
7. trusted_actual_host_image_and_omc_executable_hash
8. observed_omc_msl_compiler_and_runtime_identity
9. owner_controlled_shared_external_transactional_store
10. durable_across_runs_unique_reservation_and_crash_receipts
11. independent_pre_native_r2_and_post_native_evidence_policy

These are **actual missing controls**, not a checklist that a fabricated local JSON, matching local SHA, GitHub Actions success, or this reviewer verdict can fulfill. A genuine future native attempt requires the protected independently owner-authenticated scientific/source release and backup, live signed source provenance, independently reviewed real nonregenerating adapter/plan, observed host/OMC/MSL/compiler, protected shared durable owner-controlled atomic CAS with no-retry/crash semantics, independent pre-native R2, and **new distinct explicit owner permission** for its specifically named OMC version-query/build/single-model-launch budget. No such permission is implied.

## Tests personally performed versus evidence inspected

**Personally performed:**
- Reconstructed the corrected complete 9,342-byte intake module in a disposable reviewer area. Its **SHA-256 2093ed7d16e6672272638f8d63f399a3d9429fafdb6a247d5ed7b02c252a0691** matches the exact-head archive source inventory, and its independently computed **Git blob e84c70438cf3845df004a661b900428c505cd4aa** matches GitHub fetch_file. This confirms the module body run was byte-identical, not an approximate rewrite.
- **28 isolated adversarial intake/format checks**: 12 exponent overflow, 3 explicit constants, 2 duplicates, 5 finite controls, 3 invalid JSON/UTF-8/root, 1 all-nine forged packet, 2 single-read contradictory on-disk/captured-byte tests. All met the expected refusal or BLOCKED result.
- **One independent exact-rational physics calculation:** original F0 80× / mandatory 100× FAIL. **29 reviewer checks total.**
- Individually inspected exact Git commit trees and four-file diff, historical failure documents, owner-adoption record, source parser, tests and workflow, complete CI artifact, SHA/CRC and logs.

**Important test boundary:** The 28 isolated source-byte checks used **controlled test doubles** for the inherited readiness.audit() (a known explicit HOLD-shaped receipt) and staging duplicate-key/constant callbacks reproduced from their pinned source. I did **not** rerun the complete repository integrations or the 333 original unittest methods locally; those are attributed to the **genuine source-executed hosted CI** and its downloaded transcripts. Direct GitHub access to source worked, but a full git clone from this reviewer environment was blocked by GitHub DNS resolution. This limitation is not hidden or promoted into a local test PASS.

**Never executed by reviewer:** OpenModelica installation or version query, native model compilation/launch, MAT decoding, archived scientific reference regeneration, alternate seal adoption, protected signing, real owner-controlled CAS or cross-host reservation, native readings, production source modifications/merge.

## Separate judgments

| Dimension | Result | Basis |
|---|---|---|
| Source interpretation fidelity | **PASS, bounded** | Exact parser and same-read inventory semantics; 28 additional personal checks; explicit always-BLOCKED receipt |
| Physical/numerical correctness | **NOT REQUALIFIED** | No physics change; original F0 80× vs 100× FAIL and PR32 bitwise FAIL explicitly preserved |
| Native simulation and observable coverage | **NOT QUALIFIED** | Zero OMC/native/MAT observations; nine real public readings uncomputed |
| Evidence integrity / provenance | **PASS for exact-head OFFLINE CI ZIP; UNTRUSTED for candidate local files** | Rehashed 27,486-byte artifact; 41/41 CRC; 333 hosted tests; no owner authentication or atomic directory snapshot |
| Teacher-facing usefulness | **NOT EVALUATED** | No teacher-facing physics visualization or native output in this scope |
| Textbook-answer completeness | **NOT APPLICABLE** | Format/denial-only correction |

## Release advice and final boundary

**Final independent verdict: SCOPED PASS for F-06 finite JSON and one-captured-byte SHA/parse consistency only.** No in-scope blocker found. Retain historical PR #45 as draft/unmerged unless the owner separately decides its nonnative source workflow; **do not merge any historical F0 PR into production main on this report**. The former double pathname reopen is fixed, but actual concurrent filesystem races remain; trusted native provenance, eleven release safeguards, the two original scientific failures, and the nine missing physical observations remain unresolved. A future legitimate native campaign needs separate independently assessed gates and **new explicit owner authorization of the exact compiler-version-query/build/one-model-launch/no-retry budget**. This report grants **no native or release authority**.
