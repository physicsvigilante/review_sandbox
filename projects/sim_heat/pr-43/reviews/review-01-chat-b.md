# SIM_HEAT PR #43 — independent Chat B R2 review (review-01)

**VERDICT: SCOPED PASS — OFFLINE, IN-MEMORY STALE-SNAPSHOT CAS DIFFERENTIAL ONLY.** The five deliberately fictional demonstrations behave as described, the exact-head CI evidence is internally consistent, and the review found **no demonstrated blocker in the advertised OFFLINE scope**. This is **not** an authenticated or durable cross-host reservation, a native launch authorization, a physics qualification, a waiver of historical failures, or permission to merge into production. All **11 real native-release gates remain MISSING**.

- **Project / source:** [physicsvigilante/sim_heat](https://github.com/physicsvigilante/sim_heat).
- **Source PR:** [draft #43](https://github.com/physicsvigilante/sim_heat/pull/43), historical F0 experimental branch, open, unmerged. The source PR must **never be merged into production main** under this approval.
- **Immediate base:** reviewed PR #42 `32cbb7d02b7db0cbc322fb0e7826861fd902a77a`; original frozen F0 `dd8c9432abe97563414bb3ed809e61e673473812`.
- **EXACT reviewed HEAD:** `4e220a152e702c06b07320850f5caacff1091bb3`.
- **EXACT reviewed Git tree:** `4a931c0e017eb650c0b4a63c5dfdf38097ad9d72`, cross-checked against Git commit API and artifact.
- **Diff:** [base-to-HEAD](https://github.com/physicsvigilante/sim_heat/compare/32cbb7d02b7db0cbc322fb0e7826861fd902a77a...4e220a152e702c06b07320850f5caacff1091bb3), four commits ahead, exactly **four ADDED** paths and **zero modified/deleted** paths: `qualification/h1_c1/f02/offline_stale_snapshot_cas_model.py`, `test_offline_stale_snapshot_cas_model.py`, `STALE_SNAPSHOT_CAS_SCOPE.md` in the same directory, and `.github/workflows/h1-c1-f02-stale-snapshot-cas.yml`.
- **Reviewer / date:** Chat B, GPT-6, separate ChatGPT conversation; 2026-11-17, Asia/Kolkata. Separate context is not a distinct human or cryptographically independent subject-matter attestation.
- **Scope / class:** R2 because eventual native authority, at-most-once semantics and scientific provenance are critical; reviewed changes are strictly non-native Python demonstrations plus offline tests, scope and CI.
- **Review rules read:** [central REQUEST](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-43/REQUEST.md), central `PROTOCOL.md`, `REVIEW-RISK-POLICY.md`, `REVIEW-TEMPLATE.md`, [prior independent PR42 report](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-42/reviews/review-01-chat-b.md), inherited release-HOLD source/declaration. No root `AGENTS.md` was present at the exact source ref.
- **Source edits during review:** **none**. Only this new independent review file is written to the central `review_sandbox`.
- **Exact-head CI:** [run #44051422673](https://github.com/physicsvigilante/sim_heat/actions/runs/44051422673), push, attempt 1, completed **success**, one successful job `133929932278`, pinned HEAD/tree.
- **Real CI artifact personally downloaded and inspected:** [artifact #14313149095](https://github.com/physicsvigilante/sim_heat/actions/runs/44051422673/artifacts/14313149095); ZIP **30,078 bytes**, independently recalculated whole SHA-256 **`00d70f397c6e05fd5746583390c92fae3970e635684abb7bac2b99e24958d46c`**, 44 unique members, **44/44 CRC-valid**.

## Findings

### F-01 — PASS: exactly one fictional claim in a single shared volatile object (offline logic)

**Source:** [snapshot/store lines 43–99](https://github.com/physicsvigilante/sim_heat/blob/4e220a152e702c06b07320850f5caacff1091bb3/qualification/h1_c1/f02/offline_stale_snapshot_cas_model.py#L43-L99), [16-contender experiment lines 168–190](https://github.com/physicsvigilante/sim_heat/blob/4e220a152e702c06b07320850f5caacff1091bb3/qualification/h1_c1/f02/offline_stale_snapshot_cas_model.py#L168-L190), [tests lines 23–60](https://github.com/physicsvigilante/sim_heat/blob/4e220a152e702c06b07320850f5caacff1091bb3/qualification/h1_c1/f02/test_offline_stale_snapshot_cas_model.py#L23-L60).

A `VolatileVersionedCASFake` holds an epoch, version, consumed bit and `threading.Lock`. Every reader receives **the same pre-claim `ObservedToyState`**. Shape/type checks run before the compare, while the current epoch/version/consumed comparison and state consumption occur under **one object-local lock**. Once a claim changes version 0 to 1, all other attempts with that stale state refuse. The hosted receipt independently inspected from the ZIP reports **16 contenders, exactly 1 accepted, 15 stale refused and final fake version 1**. The tests also cover 2/8/32 contenders, replay of a stale snapshot, new reads after consumption and wrong epoch.

**Independent adversarial semantic check:** wrote and ran a separate, disposable RAM-only Python re-expression, with a barrier to force simultaneous entry. **500 trials × 16 contenders** each returned exactly 1 claim / 15 refusals. This independently checks the *stated algorithm*, **not** the actual repository's implementation or real cross-process atomicity. A Python lock protecting one object is not a protected or durable global CAS.

### F-02 — PASS with explicit bound: unsafe stale read can yield two fictional claims

**Source:** [lines 193–208](https://github.com/physicsvigilante/sim_heat/blob/4e220a152e702c06b07320850f5caacff1091bb3/qualification/h1_c1/f02/offline_stale_snapshot_cas_model.py#L193-L208).

The intentionally naive calculation trusts the same old `already_claimed=False` observation twice; it produces `unprotectedStaleReadFirstClaims=2`, with `linearizableCASActuallyUsed=false`. The independent barrier-synchronized two-reader re-expression also produced two fictional claims. **Precision:** the repository's naive function models two reads and two logical acceptances; it does not perform an actual interleaved write schedule or external race. This is fully disclosed by the source and scope. A successful test here is evidence of a counterexample *in the fictional model*, not evidence of a real storage system vulnerability or of native effects.

### F-03 — PASS: distinct instances and reset defeat global one-shot claims

**Source:** [lines 210–240](https://github.com/physicsvigilante/sim_heat/blob/4e220a152e702c06b07320850f5caacff1091bb3/qualification/h1_c1/f02/offline_stale_snapshot_cas_model.py#L210-L240).

Two different objects with the **same campaign string** independently grant one first claim each: **2 fictional claims**, `globallySharedStoreCount=0`. Clearing the same fake's consumed bit/version and assigning a fresh untrusted in-memory epoch permits a new first claim after reset; the old epoch is rejected in the exercised scenario, yet claims before/after reset total **2**. The ZIP receipts and hosted tests agree; a separate local re-expression reproduced both. There is no durable authority, owner-signed credential, historical monotonic ledger or across-host atomicity. Random fake epoch replacement is a pedagogical marker, not immutable identity or a formal non-reset guarantee.

### F-04 — PASS: acknowledgment loss is uncertainty, not retry or execution authority

**Source:** [lines 242–260](https://github.com/physicsvigilante/sim_heat/blob/4e220a152e702c06b07320850f5caacff1091bb3/qualification/h1_c1/f02/offline_stale_snapshot_cas_model.py#L242-L260).

The fixture obtains a successful **fake** internal commit, *pretends* its acknowledgment was lost, and checks that retrying the old snapshot on the **same fake** refuses. Its receipt says `fakeCommitOccurred=true`, `fakeRepeatClaimAccepted=false`, `callerCanInferNativeEffect=false` and `newExternalPermitIssued=false`. This is correct no-retry guidance. No real network drop, actual OMC operation, crash-recovery store, remote acknowledgment or physical execution occurred. The fictional internal commit cannot be used as proof that a model was launched.

### F-05 — PASS: scalar/type refusal, permanent real-native default-deny, inherited HOLD

**Source:** [lines 53–61, 101–165, 263–307](https://github.com/physicsvigilante/sim_heat/blob/4e220a152e702c06b07320850f5caacff1091bb3/qualification/h1_c1/f02/offline_stale_snapshot_cas_model.py#L53-L307); [new tests](https://github.com/physicsvigilante/sim_heat/blob/4e220a152e702c06b07320850f5caacff1091bb3/qualification/h1_c1/f02/test_offline_stale_snapshot_cas_model.py).

Malformed snapshot versions (`True`, float, 2), non-Boolean consumed flags, malformed epochs and wrong campaign names are refused. Real-budget fields must be literal integer zero (not Boolean `False` or numeric `0.0`), and owner/native/release flags must remain literal false. `require_real_native_permission(*args, **kwargs)` **unconditionally raises `CASRefusal`**. The only five accepted CLI actions are fake demonstration/audit labels; the artifact contains **ten forbidden actions** (`omc`, `approve`, `native`, `release`, `execute`, `build`, `launch`, `reserve-native`, `run`, `retry`), all with empty stdout and argparse refusal in stderr. A zero exit from an accepted fake action cannot authorize real action.

`audited_fake_run` invokes the inherited **PR41 read-only readiness HOLD** and demands status BLOCKED, `missingRequiredGateCount=11`, `releaseBlocked=true`, no native allowance and no real across-run reservation. I inspected `RELEASE_GATES_ABSENT.json` at the exact head: all 11 required fields are still `null`, with real authority/approval/native/qualification flags false. The model imports Python standard-library primitives and this inherited read-only audit, not a native adapter or external transactional store. Hosted adversarial tests mock forbidden reference regeneration and native preparation/invocation and pass. No native or scientific side effect was independently triggered.

### F-06 — MINOR / explicit non-authority limitation: fake snapshots and receipts are not authenticated

**Source:** [lines 43–61, 106–165](https://github.com/physicsvigilante/sim_heat/blob/4e220a152e702c06b07320850f5caacff1091bb3/qualification/h1_c1/f02/offline_stale_snapshot_cas_model.py#L43-L165).

`check_toy_snapshot` establishes **shape**, not who observed or owned the state. An actor who copies the openly returned current epoch/version/claimed values into a well-formed `ObservedToyState` can submit an equivalent value; its acceptance depends only on the local store's current state. The test of malformed/incorrect values **must not** be construed as a proof of provenance or forgery resistance. Likewise, `validate_receipt` enforces critical literal-false native flags and zero budgets but does **not** authenticate `status`, `fakeCounts`, `reviewedPriorToySourceCommit` or origin/signature. A tampered fictional count/status could remain shape-valid while all authority flags are still false.

This is **not a blocker to the explicitly unauthenticated fake model**: source-generated routines assert the expected demonstration values, saved CI receipts were individually inspected, and the authors clearly disclaim trustworthy provenance. **Non-blocking hardening recommendation:** add a negative test for a well-formed copied snapshot and tampered fake count/status, asserting that these cannot establish owner authority, or label the validator as a *denial-fields consistency check* only. A future real release interface must replace these semantics, not reuse them as authenticated evidence.

### F-07 — PASS: exact source, hosted offline CI and original evidence preservation

GitHub commit metadata and the independently downloaded ZIP agree on HEAD/tree. The ZIP's `source-diff.txt` contains precisely four `A\tpath` rows, `source.sha256` contains **175 tracked-file hashes**, `head-sha.txt` and `head-tree.txt` match the exact Git commit, and all **14** original F0 pin checks say `OK`. The inherited original unlaunched native preflight still checks **23** source/input identity pins. The workflow checks the original PR31 compressed reference and manifest SHA-256, then runs Python-only tests; it has read-only GitHub permissions, no persisted checkout credentials, pinned checkout/setup actions and **no OMC query/build/launch**. Job log and run metadata show success for all named steps, including artifact upload.

I parsed the **12 distinct saved unittest transcripts**, each with an `OK` final result and no failing method, and reconciled the counts:

| Suite | Offline PASS methods |
|---|---:|
| New stale-CAS/refusal | 16 |
| Previous hypothetical one-shot state | 18 |
| Readiness HOLD | 15 |
| Untrusted external CAS | 16 |
| Local SQLite | 12 |
| Nonexecuting Modelica build-text preview | 15 |
| Exact-input staging | 24 |
| Disabled F02 preflight | 16 |
| Approved saved offline reference consumer | 11 |
| Source/reference binding | 8 |
| Original PR31 archive tests | 9 |
| Original frozen H1 | 149 |
| **Total** | **309** |

Original first-authored Modelica SHA-256 **`9a165e5ce2cc85da84ecc8bc4e63e2990f2066f3547dc6ba8508fa1afbe5f435`** and evaluator modal study SHA-256 **`b43e85b6b10afd6550a43322cf98097fe9781a606ee01bc031eadbfd4783b31b`** appear unchanged in the exact-head SHA inventory. The only owner-approved PR31 V2 raw analytical reference for **OFFLINE checking** retains declared raw SHA-256 **`0db511dd8dba023d16518667de256029cf3e073463ea21e2478aeac8afd1f368`**, canonical seal **`d2b8e2ca8e1f929cac7b028dcc3f7d0b453921d193f877eb091e23ac70aa4ce9`**, XZ SHA-256 **`fc5a7df5928c3fb8aef2ba4af516dfbd32b42c0450ebef1051ad4fd7efebd17f`** and whole manifest SHA-256 **`50467b138ed64cdb908f2c763bc777e6babf0bb04a0711568acc559112e66f84`**. Hash equality and byte preservation are supported by the changed-path comparison, artifact source inventory and CI's original archive checks; **these are not independent owner signatures**.

Crucially, the historical frozen F0 `hotLead.G` **80× accuracy against required ≥100× remains FAIL**, PR32 two-host original-seal bitwise regeneration remains **FAIL**, and **nine C1 native results remain `not_computed`**. The new 309 tests do not reclassify those failures, recalculate the reference, or supply any native observation.

## Personally performed versus externally observed evidence

**Personally read/analyzed:** the exact pinned model (310 source lines), all 16 new tests, scope, workflow, PR41 inherited HOLD logic and all-null 11-gate declaration, central protocol/policy/template/packet, prior Chat B review, source commit and Git tree/changed-path comparison. Checked the original downloaded CI ZIP, its SHA-256/CRC, file list, five receipt JSON objects and literal native/owner/budget flags, ten forbidden-CLI stdout/stderr pairs, all 12 individual suite summaries and original F0/source SHA inventories. The GitHub job log was inspected against the ZIP transcripts.

**Personally executed:** a scratch, independently expressed **RAM-only** concurrency probe: 500 trials of 16 barrier-synchronized contenders, plus separate naive stale-reader, independent-store, reset/old-epoch, lost-ack and strict scalar-type probes. All passed. This is a **semantic cross-check**, *not* execution of the actual pinned implementation.

**Not personally executed:** a source checkout and rerun of the repository's exact Python tests. The isolated local reviewer environment could not resolve the public raw GitHub source host, so the **309 genuine repository test results derive from the independently inspected exact-head CI/job logs and artifact**, not local execution by Chat B. No actual OMC, model build, external CAS, live owner signing, native launch, scientific regeneration, native numerical reference calculation or classroom visual test was performed. The original archived XZ bytes were not separately downloaded and rehashed by Chat B; the archive integrity checks quoted above are from original exact-head CI and its inspected SHA inventory. These distinctions limit any sign-off to **offline fake demonstrations**.

## Separate scope judgments

| Dimension | Judgment | Basis |
|---|---|---|
| Source interpretation fidelity | **PASS, toy only** | Single-object lock CAS, two naïve claims, split stores, reset, lost ack and negative authorizations match advertised fictional semantics |
| Physical/numerical correctness | **NOT QUALIFIED** | No new physics; original frozen 80×/100× failure and PR32 bitwise failure retained |
| Native simulation / observable coverage | **NOT QUALIFIED (zero)** | No compiler query/build/launch; nine requested native C1 outputs not computed |
| Evidence integrity and provenance | **PASS for hosted OFFLINE artifact only** | Exact HEAD/tree, 44 CRC-valid entries, independently verified ZIP hash, 309 CI methods, unchanged inherited SHA pins; no protected owner/native attestation |
| Teacher-facing usefulness | **LIMITED / NOT EVALUATED** | Abstract storage counterexamples, no new teaching viewer or actual physical exploration |
| Textbook-answer completeness | **NOT APPLICABLE** | Protocol model only |

## Release advice: all real native prerequisites still MISSING

The exact-head inherited absence declaration has `null` for every one of the **11** required gates:

1. Explicit owner approval for named version-query/build/single-launch budgets.
2. Owner-authenticated protected reviewed source and reference release.
3. Independently retained/verified reference backup.
4. Live fresh source ref and signed commit attestation.
5. Independently reviewed non-regenerating executable native adapter.
6. Exact-SHA-pinned native runner and executable plan.
7. Trusted actual host image and OMC executable hash.
8. Observed OMC/MSL/compiler/runtime identity.
9. Owner-controlled shared external transactional CAS store.
10. Durable across-run unique reservation and crash/partial-output receipts.
11. Independent pre-native R2 and post-native evidence policy.

**SCOPED PASS recommends no mandatory correction to this fictional offline model** and does **not** advance a single native gate. Preserve PR #43 and historical source PRs as **draft/unmerged experimental branches**. Never turn a successful fake CLI return or this review into a native launch permission. If a real one-shot controller is ever proposed, the smallest separate R2 qualification is a genuinely owner-controlled, protected *shared durable transaction* exercised against distinct processes/hosts with stale observations, lost acknowledgments, crash before/after reservation, persistent consumed history and **no automatic retry**. That work requires a separately authenticated source/host/plan, owner review and a **new explicit approval** before even a named OMC version query, model build or single launch. This review neither authorizes nor requests those operations.

**Final verdict: SCOPED PASS — OFFLINE COUNTEREXAMPLE SEMANTICS ONLY. NO NATIVE LAUNCH OR PRODUCTION MERGE AUTHORIZED.**
