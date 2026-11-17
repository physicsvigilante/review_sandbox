# SIM_HEAT PR #37 — independent Chat B R2 correction re-review (review-02)

**Verdict: PASS (strictly scoped to corrected OFFLINE F-02 staging/readback contract F-01–F-04).** This does **not** pass a native qualification, create an executable plan, authenticate a durable release/attempt, approve any compiler invocation, or authorize a merge.

- **Reviewer/date:** Chat B, separate ChatGPT conversation (GPT-6), 2026-11-17. Separate-context LLM review is not a credentialed independent human expert assessment.
- **Source:** [physicsvigilante/sim_heat draft PR #37](https://github.com/physicsvigilante/sim_heat/pull/37), open, draft, unmerged; historical F0 experiment, **NEVER MERGE TO MAIN**.
- **Immediate PR base:** PR #36 HEAD 7cfa35a1cd5cc858e48bcdc4da453bf2dc22b7f2.
- **Previously reviewed head:** d1d6a32252b41dabad832668de642ecaf475a2a3, tree af85a6f1848a0f1231612144a1230689be8cf0f2; original [review-01 (CHANGES REQUESTED)](review-01-chat-b.md) remains valid and unchanged for that old source.
- **Exactly reviewed corrected head:** [2f2b8d5008f51b9972897058328aed8cbcbfbbce](https://github.com/physicsvigilante/sim_heat/commit/2f2b8d5008f51b9972897058328aed8cbcbfbbce).
- **Exact Git tree:** de397fe3af9bb3385c4ef55354e49c33571dc99b, obtained via GitHub Git-commit API and corroborated by exact-head CI receipt.
- **Comparison:** [old reviewed SHA … corrected SHA](https://github.com/physicsvigilante/sim_heat/compare/d1d6a32252b41dabad832668de642ecaf475a2a3...2f2b8d5008f51b9972897058328aed8cbcbfbbce), ahead 5 / behind 0; exactly five modified files and no additions/deletions: qualification/h1_c1/f02/{stage_immutable_inputs.py, test_stage_immutable_inputs.py, offline_control_preflight.py, test_offline_control_preflight.py, IMMUTABLE_INPUT_STAGE_SCOPE.md}.
- **Modification by reviewer:** NO source, CI, tests, frozen physics, references, owner approvals, native plans, historical PRs or historical review changed. Only this new independent review file is authored in review_sandbox.
- **Risk:** R2 evidence provenance, correction-only re-review. No OpenModelica version query, build, launch, simulation, MAT inspection or new reference generation performed.

## F-01–F-04 findings

### F-01 — CLOSED / PASS within offline metadata scope (formerly MAJOR)

At [corrected stage_immutable_inputs.py](https://github.com/physicsvigilante/sim_heat/blob/2f2b8d5008f51b9972897058328aed8cbcbfbbce/qualification/h1_c1/f02/stage_immutable_inputs.py), the actual readback calls strict_metadata for both STAGE_STATE.json and STAGED_INPUTS_MANIFEST.json. The object_pairs_hook refuses repeated keys at all nesting levels; parse_constant refuses NaN, Infinity and -Infinity; UTF-8, JSON-object, non-symlink file and 16 KiB metadata-size checks are imposed. All permission/history false fields are checked with literal identity (is False), not only Python equality.

**Personal test:** A fresh filesystem copy of the actual CI six-file stage passed a faithful independently implemented verification-predicate replay. On-disk duplication of each of the four specified manifest keys (nativeAllowed, nativeExecuted, ownerNativeLaunchApproved, status), three state keys (nativeAllowed, nativeExecuted, status), and a nested repeated model.mo SHA was refused in all eight cases. Separate NaN, Infinity and -Infinity mutations also refused. The real source-executed current CI tests cover the same attacks.

### F-02 — CLOSED / PASS within independent disabled-plan pin scope (formerly MAJOR)

The corrected readback uses f02.load_preview(root / f02.PLAN), which checks the **independently fixed** PR36 Git blob SHA-1 2c01301d1c493f33c9eb4bfb9778190adbb6d0bc, then separately demands the **code-literal raw SHA-256** 7e03896563ae8b4762b56bb8807612a93cddb759145a23fa94326363ea706326 and calls f02.validate_preview. The editable stage manifest is no longer the sole plan-identity authority. I separately reconstructed the exact 3,022-byte published disabled-plan content locally: its computed Git blob SHA-1 and raw SHA-256 match both expected pins.

**Personal test:** Replacing plan bytes and coordinating the manifest disabledPreviewSha256 to the same changed hash refused in the independent predicate replay. A mocked parser return of a valid document paired with an unpinned raw digest also refused. Source-executed CI explicitly passes test_post_stage_coordinated_preview_and_manifest_drift_refuses and test_standalone_preview_pin_is_independent_of_parser_result. There is no native runner or reference.prepare fallback in these changed readback paths. The local predicate replay does not claim to import the full source repository or execute the actual f02.load_preview implementation; that source-executed behavior is evidenced by the pinned CI tests and independent code inspection.

### F-03 — CLOSED for local staging-label and direct-path symlink checks; residual trust limitation documented (formerly MINOR)

Both persisted state and manifest now contain label and require exact equality with the verifier's requested safe label. The readback refuses a symlinked STAGE_PARENT, leaf staging directory and staged member. A genuine stage moved to a new safe directory label without rewriting metadata refused, and an independently constructed parent symlink refused. Current source-executed CI includes both cases.

**Residual, not a claimed capability:** I also deliberately changed the directory name **and both editable JSON label fields** together; the offline predicate replay then accepted the relabelled data. Thus the new equality gate prevents accidental/mismatched copying but is **not an authenticated attempt identity**. Local scratch directories, pathname checks, and non-atomic reads/writes remain vulnerable to active/concurrent writers, TOCTOU, coordinated edits and interrupted operations. This does not invalidate the explicitly stated nonnative scratch-evidence contract, but such evidence must **never** serve as the across-run native lock or owner-authenticated launch authority.

### F-04 — CLOSED / PASS for named strict numeric metadata fields (formerly MINOR)

Readback now enforces type(sourcePinCount) is int before checking value 23. The disabled plan validator now enforces type(frozenCheckerAndSourcePinsCount) is int before checking 23. The earlier PR36 strict type gates for maxLaunchesAfterSeparateApproval and modal study grid/scalar settings are preserved. **Personal tests:** On-disk stage metadata sourcePinCount=23.0 and true refused; numeric 0 in place of JSON false in both state and manifest refused. Locally checking the exact pinned disabled plan predicate with 23.0, true and 23 showed that only the integer 23 satisfies the required exact-type predicate. Current pinned CI source tests cover the full planned-value validator and the on-disk negatives. This is scoped to these identified fields, not a claim that every future JSON field has a general-purpose authenticated schema.

**No remaining demonstrated F-01–F-04 blocker** within this offline readback contract. The preceding F-01/F-02 defects remain real historical findings for the old head; this PASS does not rewrite review-01.

## Independently inspected exact-head CI and scientific byte identities

I inspected actual GitHub run/job records, [CI run #44028343008](https://github.com/physicsvigilante/sim_heat/actions/runs/44028343008), and its downloaded [artifact #14304102592](https://github.com/physicsvigilante/sim_heat/actions/runs/44028343008/artifacts/14304102592):

- **Run:** push event, attempt 1, HEAD 2f2b8d5008f51b9972897058328aed8cbcbfbbce; completed **SUCCESS**; job 133853987681 (offline-stage-only) completed SUCCESS. No OMC, compiler version query, native build or simulation in workflow steps. Actions permissions are contents:read; checkout disables credential persistence. The workflow runs on full branch push and has no paths filter.
- **Actual artifact ZIP:** 1,190,731 bytes, independently recomputed SHA-256 **256da986efc326fe806185dd36cf42ba5c652c268efef7d28ec2351dafa53191**; all **35 of 35 members CRC-valid** (Python ZipFile.testzip returned None). Artifact's recorded uploaded digest and size agree.
- **Actual saved staged inputs, personally SHA-256 hashed from ZIP:** model.mo 872 bytes = 9a165e5ce2cc85da84ecc8bc4e63e2990f2066f3547dc6ba8508fa1afbe5f435; study.json 6,616 bytes = b43e85b6b10afd6550a43322cf98097fe9781a606ee01bc031eadbfd4783b31b; SimHeat.mo 3,674 bytes = e57955b6c32cb34321a6b1908306c4ea9a63ae259b95a5fd48c7e8d3b4da10ea; reference.bundle.json 4,409,800 bytes = 0db511dd8dba023d16518667de256029cf3e073463ea21e2478aeac8afd1f368.
- **Original saved reference seal:** Personally parsed staged original reference, confirmed nativeQualified is false, and independently SHA-256 hashed sorted-key compact JSON excluding its seal: **d2b8e2ca8e1f929cac7b028dcc3f7d0b453921d193f877eb091e23ac70aa4ce9**. This is archived checking data; no original reference was regenerated. Git tree preservation plus CI SHA-checks support the unchanged original PR31 XZ archive (fc5a7df5928c3fb8aef2ba4af516dfbd32b42c0450ebef1051ad4fd7efebd17f) and reference manifest (50467b138ed64cdb908f2c763bc777e6babf0bb04a0711568acc559112e66f84). I did **not** independently re-download/re-hash the compressed XZ bytes in this correction cycle.
- **Frozen history:** Independently compared GitHub recursive tree blob identities for corrected head, previous reviewed head, PR36 and original frozen F0. All **14 original F0 physics/checker/runner source blob identities are equal** to original F0 dd8c9432abe97563414bb3ed809e61e673473812. Original first-authored and modal model/study, archived reference files, owner adoption, original unlaunched native plan and workflow are unchanged by the five-file correction; full Git-tree old-to-new difference confirms only the five named files changed.
- **217/217 actual CI test methods PASS**, counted directly in artifact logs: 24 staging (including F-01–F-04 on-disk negatives) + 16 disabled-preview/strict types + 11 owner offline consumer + 8 frozen binding + 9 original immutable archive + 149 original H1 offline. The 14 historical frozen SHA checks report OK. The seven forbidden staging CLI verbs (execute, build, launch, native, approve, reserve, run) are rejected. CI's stage and readback receipts agree on OFFLINE_STAGED_EXACT_INPUTS_NOT_NATIVE; all native/owner/one-shot claims remain false, no native output file.
- **Personal adversarial execution boundary:** With the actual extracted six staged CI files in temporary local directories, executed **22 independent on-disk negative predicate-replay cases, all refused**, plus an unmodified-stage positive and a deliberate coordinated-relabel residual case. This replay mirrored the reviewed readback predicates and hashes; it did **not** import/execute the full GitHub checkout. The separate GitHub Actions tests **did** exercise the actual committed Python modules.
- **Historical runs remain distinct:** [#44024037373](https://github.com/physicsvigilante/sim_heat/actions/runs/44024037373) completed SUCCESS at the **old** head d1d6a322..., not the corrected source. [#44023899014](https://github.com/physicsvigilante/sim_heat/actions/runs/44023899014) remains **FAILED** at 8a7507e0...; I inspected its failed job log and confirmed three failures were assertion-regex wording mismatches against actual refusals, not native/physics execution. No past CI result is relabelled or deleted.

## Separate scope judgments

| Dimension | Scoped judgment | Basis |
| --- | --- | --- |
| Source interpretation / original input fidelity | **PASS: unchanged inputs** | Five-file Git diff, 14 preserved F0 blobs, four exact staged byte hashes, original reference canonical seal |
| Physical/numerical correctness | **UNCHANGED / not retested** | Frozen laws/checker untouched; this re-review did not reproduce the 85-digit reference calculation |
| Native simulation and nine observable readings | **NOT RUN / NOT AUTHORIZED** | No executable native plan, OMC invocation, MAT, readings or owner launch approval |
| Offline evidence/readback integrity | **PASS for F-01–F-04 local stage contract** | Source inspection, actual source-executed CI negatives, independent staged-file attack replay |
| Teacher-facing visualization | **NOT TESTED** | No viewer scope |
| Textbook-answer completeness | **N/A** | Offline input staging only |

## Mandatory gates before any native qualification (all still OPEN)

1. Owner-authenticated, current, protected/signed or equivalently independently verifiable **reference-release identity and durable backup**, not a mutable cached branch or unsafeguarded CI snapshot.
2. Separately designed, independently reviewed **non-regenerating** native adapter/runner and an exact runnable plan pinned to source commit/tree, checker, four scientific inputs, archived reference, dependency/runtime artifacts and strict permitted budget. No fallback to reference.prepare or PR32 alternate c30e... seal.
3. Observed and attested host and toolchain identities, including actual OpenModelica executable/version/hash, MSL source tree, Python/dependency/compiler/runtime and host image; planned strings are not observed versions.
4. Persistent owner-controlled, fail-closed, crash-aware, **atomic one-shot across-run reservation**, protected against concurrent writers, symlinks, TOCTOU, retries and partial evidence; staged labels and CI concurrency are not substitutes.
5. **Distinct explicit owner authorization** for the named version query, build and single launch; another independent pre-native R2 on the runnable plan/runner and trusted reference is needed.
6. If a native run is separately authorized and occurs, independent post-run verification of MAT/traces, 37 required exports, four flow integrals, energy balances, grid/timestamps, all nine public observations and unchanged original numerical tolerances and failure flags.

The original F0 hotLead.G static **80× versus mandatory ≥100× FAIL** and PR32 two-host regeneration **bitwise FAIL** remain historical failures; this correction neither repairs them retroactively nor waives either. The adopted archived d2b8... reference is not interchangeable with regenerated c30e.... Do not merge historical draft PRs or relax tolerances.

**Final: SCOPED PASS for the corrected offline staged-input readback at exact 2f2b8d... only. NO native/release/merge readiness.**