# SIM_HEAT PR #40 — independent Chat B R2 review (review-01)

**VERDICT: SCOPED PASS — the bounded, UNTRUSTED Python-only default-deny external-CAS contract and fake provider.** This verdict certifies **neither** a real external reservation service **nor** an owner-approved native launch. The PR must remain historical/draft, **NEVER MERGE TO PRODUCTION MAIN**; no OpenModelica, reference regeneration or native execution is authorized by this report.

- **Reviewer:** Chat B (GPT-6), separate ChatGPT conversation; independent context and adversarial probes, **not** independent human expertise, authenticated owner approval or a different model-family guarantee.
- **Date:** 2026-11-17.
- **Source:** [physicsvigilante/sim_heat draft PR #40](https://github.com/physicsvigilante/sim_heat/pull/40); **exact reviewed HEAD `ebe203781e87ba108e8dec845074ca7ca47972ef`**, tree `ca0254a94bb2f6785608c0ad8700a693a00f647e`.
- **Reviewed immediate base:** independently reviewed PR #39 `ffc96e743a78cb3c63c01d6bf292d1fa84c6164f`, tree `2bbb083437bd8166fc44e4c447521990a657d14a`; [exact diff](https://github.com/physicsvigilante/sim_heat/compare/ffc96e743a78cb3c63c01d6bf292d1fa84c6164f...ebe203781e87ba108e8dec845074ca7ca47972ef).
- **Original F0:** `dd8c9432abe97563414bb3ed809e61e673473812`, frozen history remains frozen.
- **Risk:** R2 (candidate affects future native authorization/evidence interpretation, although this source is nonnative).
- **Change scope:** **exactly four added paths and ZERO modified/deleted existing paths** relative to PR #39: `qualification/h1_c1/f02/offline_external_cas_contract.py` (259 lines); `qualification/h1_c1/f02/test_offline_external_cas_contract.py`; `qualification/h1_c1/f02/EXTERNAL_CAS_CONTRACT_SCOPE.md`; `.github/workflows/h1-c1-f02-external-cas-contract-preview.yml`. Four commits ahead of base.
- **Reviewer writes:** this **new report only** in `physicsvigilante/review_sandbox`. No `sim_heat` source, frozen physics, numerical policies, native runner, historical PR or test/CI workflow was modified.
- **Reading:** [review request](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-40/REQUEST.md), [pinned module](https://github.com/physicsvigilante/sim_heat/blob/ebe203781e87ba108e8dec845074ca7ca47972ef/qualification/h1_c1/f02/offline_external_cas_contract.py), [pinned tests](https://github.com/physicsvigilante/sim_heat/blob/ebe203781e87ba108e8dec845074ca7ca47972ef/qualification/h1_c1/f02/test_offline_external_cas_contract.py), [scope](https://github.com/physicsvigilante/sim_heat/blob/ebe203781e87ba108e8dec845074ca7ca47972ef/qualification/h1_c1/f02/EXTERNAL_CAS_CONTRACT_SCOPE.md), [workflow](https://github.com/physicsvigilante/sim_heat/blob/ebe203781e87ba108e8dec845074ca7ca47972ef/.github/workflows/h1-c1-f02-external-cas-contract-preview.yml).

## Findings

### F-01 — PASS, bounded: actual default-deny functions never authorize native operations

**Category:** authority guard and immutable off-line fact snapshot. **Severity:** no demonstrated blocker within scope.

`snapshot`, module lines 59–82, records fixed prior reviewed PR39 source SHA, original authored model SHA `9a165e5ce2cc85da84ecc8bc4e63e2990f2066f3547dc6ba8508fa1afbe5f435`, evaluator modal study SHA `b43e85b6b10afd6550a43322cf98097fe9781a606ee01bc031eadbfd4783b31b`, preserved PR31 V2 raw reference SHA `0db511dd8dba023d16518667de256029cf3e073463ea21e2478aeac8afd1f368` and seal `d2b8e2ca8e1f929cac7b028dcc3f7d0b453921d193f877eb091e23ac70aa4ce9`, and disabled plan SHA `7e03896563ae8b4762b56bb8807612a93cddb759145a23fa94326363ea706326`. Every owner/release/host/provider flag is `false`; `omcVersionQueries`, `modelBuilds`, `modelLaunches` and `retries` are **literal integer zero**.

`assert_snapshot`, lines 85–95, uses canonical JSON **byte equality** against a fresh fixed snapshot plus strict booleans and integer-zero budget verification; `reservation_key`, lines 98–101, hashes the *fake scenario* and does not attest a live Git ref or owner. `ExternalAuthorityUnavailable.reserve_native`, `validate_native_launch` and `require_native_permission` (133–144) each unconditionally throw `GateRefusal`. No alternate path from the fake to those functions exists. The saved base SHA is explicitly the *previously reviewed source label*, **not** a freshness proof for the PR40 HEAD or an external live release.

**Independent execution against exact source:** I reconstructed the Python file in a disposable local directory and verified its **Git blob SHA `80c5fc744749e9603880ada178222dcd305a6d64`**, raw SHA-256 **`00e8f63ab002293b0eaa16f9cd8cc24e8b6bdaa04cc4486d13bb706656b9b223`**, length **10,518 bytes**, 259 lines against GitHub and the actual CI `source.sha256`. Then I imported and exercised the actual module, not an invented logic reimplementation:

- 9 direct gate-call probes (3 entry points × empty, genuine fake snapshot, and forged owner/native receipt inputs): **all 9 rejected with `GateRefusal` and exact denied status**.
- 35 forged snapshot mutations (seven source/owner/simulated fields and 7 variants for each of four budgets): **0 accepted**. The reference, source, owner and native-budget modifications cannot turn this contract into an authorization token.
- Four actual CLI allowlisted actions returned 0 and explicitly nonnative JSON; nine forbidden `native`/`reserve-native`/`approve`/`omc`/`execute`/`build`/`launch`/`prepare`/`run` choices exited 2 with argparse stderr, no accepted stdout.
- `audit_contract_only()` reports **11 missing gates** and matches saved canonical fake fact SHA `f03a6bc2dd68ef236456fc3806e31365a5e83519b5dac6e54ea432cf6bf406a1`.

**Meaning:** the code demonstrates *unavailability*, rather than proving a real CAS provider or owner-verified trust root. The source has no external client/network import, owner credential processing, native plan invocation, reference generator, Modelica compiler/executable or native runner call.

### F-02 — PASS as deliberate negative experiment: fake split-brain and state-reset defeat one-shot

**Category:** simulated local contention / counterexamples to global durability. **Severity:** **CRITICAL BLOCKER if ever treated as a real native gate**; expected and explicitly advertised for the fake-only scope.

`FakeAtomicCAS`, lines 104–130, is a process-local `threading.Lock` and ordinary dictionary; `fake_put_if_absent` serializes only cooperative threads sharing the **same Python object**. It does not share records across Python processes, CI runs or hosts, does not persist state after exit or crash and has no protected tamper-resistant custody.

I independently tested the exact source:

1. **64 concurrent Python threads** contending for one fresh `FakeAtomicCAS` and one scenario key yielded **1 accepted / 63 refused**, and repeat same-object nonce was refused. This demonstrates only local thread mutual exclusion.
2. **Two separately constructed providers** with the **identical scenario key** each granted its own first claim, with independently selected syntactically valid nonce values (`111…` and `222…`). This demonstrates split-brain and nonshared storage, not two authorized launches.
3. After the first accepted claim, `fake_reset_unprotected_state` deleted the stored row; a **second fake claim succeeded** on the same provider. Recovery or recreation can therefore restore a fake slot.
4. A fully attacker-chosen syntactically valid nonce `22222222222222222222222222222222` was accepted and returned by `fake_lookup`, with no owner authentication. Fake receipt status or nonce cannot be passed into the unconditionally refusing real permission stub.
5. `simulate_contention`, `simulate_split_brain` and `simulate_reset_attack` returned respectively first/refusal counts **1/15**, isolated first claims **2**, before/after reset first claims **2**. All receipts' global/owner/native flags were literally false.

The reset and split-brain tests are explicit proofs that this **is not a globally shared, durable, owner-controlled cross-host one-shot gate**. A local SQLite file, CI concurrency group, unprotected Git ref, source-text SHA, fake process lock or random nonce would not cure this.

### F-03 — MINOR optional error-type cleanup, not authorization bypass

**Category:** negative-input exception typing. **Severity:** minor/nonblocking for this fake.

**Reproduction:** mutate any of the four integer-zero `nativeBudget` fields to IEEE NaN then call `assert_snapshot`. `canonical` (lines 54–56) raises **Python `ValueError`** because `allow_nan=False`, before `need` can raise custom `GateRefusal`. All four such probes still **refuse**. In contrast other 31 mutations in the independent 35-case set raised `GateRefusal`. The documented security property is fail closed, which is maintained. For a future *formal* denial API, wrap JSON serialization/validation errors into a stable typed refusal (and test NaN/Infinity); never silently coerce or approve them. **Not a condition of this scoped PASS.**

### F-04 — PASS for exact-head hosted OFFLINE evidence and unchanged prior science

**Category:** CI provenance and preservation; **severity:** no new defect found.

GitHub Actions **[run #44039595352](https://github.com/physicsvigilante/sim_heat/actions/runs/44039595352)**: completed **SUCCESS** on `push`, run attempt 1, pinned HEAD `ebe203781e87ba108e8dec845074ca7ca47972ef`, pinned Git tree `ca0254a94bb2f6785608c0ad8700a693a00f647e`; one successful job `133890668701` (`pure-python-default-deny`), every listed step completed successfully. Workflow uses `contents: read`, checkout with credentials not persisted, SHA-pinned official Actions, unfiltered branch pushes and only Python numerical checking deps; no OMC install/version query/build/model launch, native result or API external CAS.

**Artifact [#14308567981](https://github.com/physicsvigilante/sim_heat/actions/runs/44039595352/artifacts/14308567981)** was **independently downloaded** as actual bytes: ZIP **26,344 bytes**, full SHA-256 **`9c1b5d893d4f579d1efbf80475efb4244d76e6ec349e7adfab693ea3bf1fb3c8`**, **38/38 ZIP members CRC valid**. I parsed its exact source SHA and tree text, four `A`-only source diff, archived scientific source/file SHA inventory, all four receipts, nine forbidden-command stderr/stdout pairs, and all nine saved test logs. Forbidden commands all emitted argparse invalid-choice stderr, empty stdout. Every receipt had `nativeAllowed=false`, `nativeExecuted=false`, `ownerNativeLaunchApproved=false`, `realAcrossRunReservationAllocated=false`, `crossHostAtomicityProved=false`, `externalStoreConnected=false`, `compilerQueried=false`, `buildInvoked=false`, `modelLaunched=false`, historical failure flags false. No native outputs/MAT/CSV were present.

**Complete saved logs, not just a test-total claim:** 16 new external fake CAS + 12 old local SQLite + 15 nonexecuted build-text preview + 24 immutable stage + 16 disabled F02 control + 11 offline owner checking consumer + 8 source/reference binding + 9 archive integrity + 149 original frozen H1 = **260/260**; all archived `unittest` log summaries are **OK** with the corresponding completed test count. These **260 were GitHub-hosted**; I separately executed my own targeted adversarial probes rather than claiming to have rerun the entire inherited suite locally.

**Original identity preservation:** I compared original frozen F0 `dd8c9432…` Git trees against the pinned PR40 tree: **14/14 original F0 pinned source paths have the same Git blob SHA**. Also compared PR39 base and PR40 for the original first Modelica model/study, evaluator modal model/study, archived compressed PR31 reference, manifest, offline-only owner adoption, original unlaunched native plan and native runner: **9/9 Git blobs unchanged**. CI `source.sha256` records the unchanged original Modelica model SHA `9a165e5ce2cc85da84ecc8bc4e63e2990f2066f3547dc6ba8508fa1afbe5f435`, evaluator modal study `b43e85b6b10afd6550a43322cf98097fe9781a606ee01bc031eadbfd4783b31b`, saved compressed V2 `fc5a7df5928c3fb8aef2ba4af516dfbd32b42c0450ebef1051ad4fd7efebd17f` and whole manifest `50467b138ed64cdb908f2c763bc777e6babf0bb04a0711568acc559112e66f84`. Original 14 SHA checks and existing old 23-plan pins are preserved by the workflow and regression evidence. **No frozen reference was recreated or promoted.**

The historic F0 `hotLead.G` scientific accuracy margin is **80× against mandatory ≥100×: FAIL** (not corrected), and PR32 re-generation of the originally reviewed PR31 V2 seal across hosts is **bitwise FAIL**. The owner Option A decision authorizes **only read-only offline checking** of the exact archived PR31 V2 scientific reference; this is **not** authenticated native approval. The nine actual C1 native requested public outputs remain **not_computed**. The green offline CI cannot change any of these facts.

## Separate scope judgments

| Dimension | Outcome | Justification |
|---|---|---|
| Source interpretation fidelity | **SCOPED PASS** | Pinned exact four-addition diff, zero-budget/false authority snapshot; no native-call path |
| Physical/numerical correctness | **UNCHANGED; historical FAILs** | No physics edits; original F0 strict accuracy 80×/100× FAIL and PR32 bitwise FAIL remain |
| Native simulation / observable coverage | **NOT RUN / NO AUTHORITY** | No OpenModelica/version/build/launch, MAT, native evidence, or nine completed observations |
| Evidence integrity / provenance | **PASS for offline only** | Independently rehashed downloaded artifact, inspected 38 CRCs, four receipts, 260 archived test outcomes, frozen Git blobs |
| Educational/teacher visualization usefulness | **NOT EVALUATED** | Internal control-design demonstration, no new visualization |
| Textbook-answer completeness | **NOT APPLICABLE** | No authored problem/answer in scope |

## Remaining mandatory gates — completely separate future R2/native release

A genuine durable one-shot mechanism must obtain **independently authenticated explicit owner native authorization** for a *specific* immutable source/model/study/reference/plan/host and separately allocated version-query, build, single-model-launch and no-retry budgets; establish a protected, trusted **owner release root plus independently retained immutable reference backup**; verify current live source and named executable plan, not only hardcoded prior-source labels; record actual pinned OS/host/OMC executable hash, OpenModelica/MSL/compiler/runtime and package hashes; independently review a minimal nonregenerating/native executable adapter so it cannot bypass the gate or regenerate the reference; implement one protected **shared external atomic transactional compare-and-set** consumed before each authorized action, with no fallback store, no anonymous reset/replay, crash/cancel/network outage/refailure fail-closed policy and durable audit plus multi-host adverse testing; secure signed/attested receipts and recovery history that cannot resurrect a consumed budget; and complete independent pre-native R2 and post-native MAT/37 export channels, four integrals, energy-balance and nine public-observation checking against unchanged scientific requirements.

**Recommendation:** Accept the nonnative fake and its negative demonstrations *only as offline contract-learning evidence*. The 11 reported missing gates remain missing. Do not allow an unconditional or real native provider to be added to this PR and retroactively reuse this scoped PASS; that candidate requires a **new explicit owner native approval and a fresh full R2 review**. No production merge and no OpenModelica query/build/launch from this review.
