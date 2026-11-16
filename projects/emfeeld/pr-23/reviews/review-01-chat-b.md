# EM Fields PR #23 — independent Chat B R2 review (review-01)

**Verdict: CHANGES REQUESTED.** Scoped to Bounded Scenario Ensemble V1 at source commit **38773a546d76616fe815eb302c418281bded7c1d**, Git tree **5bcb842ff3f14991cf12f069daa6a3dc3978f7bf**. Date: 2026-11-16 (Asia/Kolkata). This is an independent-context, independently executed adversarial review; it is not a human physics certification. **Do not merge PR #23 on this review.** No source files, source PR metadata, branches, or merges were modified by this reviewer.

## Identity, scope, and evidence provenance

- Request: [R2 REQUEST](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/emfeeld/pr-23/REQUEST.md); [review protocol](https://github.com/physicsvigilante/review_sandbox/blob/main/PROTOCOL.md); [R2 risk policy](https://github.com/physicsvigilante/review_sandbox/blob/main/REVIEW-RISK-POLICY.md).
- [Source PR #23](https://github.com/physicsvigilante/emfeeld/pull/23), base f0fc993dae1831432ca43b651a12e64fa0b2fdd5 (qualified main), pinned head 38773a546d76616fe815eb302c418281bded7c1d, tree 5bcb842ff3f14991cf12f069daa6a3dc3978f7bf. Checked through the GitHub Git-commit object and PR metadata: head is draft, open and unmerged. GitHub's merge-preview cce77c7767a824558ea702492ddbf6ce7d95c101 has the **same Git tree** and parents qualified main + exact source head.
- The pinned base-to-head diff contains exactly six changed paths: design document, new ensemble module, new focused tests, qualification driver, reference checker and six additive workflow lines. No pre-existing numerical law, solver, comparator, renderer or threshold file changed in this diff.
- Independently downloaded snapshot artifact 14222041939 from [snapshot workflow 43858694305](https://github.com/physicsvigilante/emfeeld/actions/runs/43858694305). Original ZIP SHA256 **50c5b9e810a0142af207b1d407aa09c22965a8b76721f024a830d96b6adaeb39**; contained tested-source.tar SHA256 **2e591d52119c28f345dcef11e201cf13fab964457e9af265c72d4c0e4b0714a2**. Independently checked all **346/346** recorded Git blob SHA1 identities, zero missing/mismatched/unlisted source files. Rebuilt the Git tree from the extracted source using git add and git write-tree: exact **5bcb842ff3f14991cf12f069daa6a3dc3978f7bf**. The checked-out source was not patched; independent tests were kept outside it.
- Read the complete R2 request and protocol, source AGENTS.md, docs/BOUNDED_SCENARIO_ENSEMBLE_V1.md, docs/PHYSICS.md, the new source module, focused tests, and relevant V3 store/native-run/sealed-comparison implementations.

## Required corrections

### R2-01 — BLOCKER: nested native grammar is not fully preflighted

**Pinned source:** [scenario_ensembles.py lines 86–104](https://github.com/physicsvigilante/emfeeld/blob/38773a546d76616fe815eb302c418281bded7c1d/src/emfeeld/scenario_ensembles.py#L86-L104) validates only the presence of a few investigation/analysis/presentation keys and versions; [lines 169–225](https://github.com/physicsvigilante/emfeeld/blob/38773a546d76616fe815eb302c418281bded7c1d/src/emfeeld/scenario_ensembles.py#L169-L225) publishes physical revisions before the underlying native grammar is checked during member execution.

**First independent reproduction:** Start from a complete fresh sealed two-source static electric baseline and two valid V3 siblings. Add an unexpected key to the **first member's analysis**: analysis["unexpected_token"] = "malformed". Call run_ensemble.

**Expected under R2 preflight contract:** Refusal before ensemble output creation or physical revision acceptance. **Observed:** No exception. A sealed **partial** ensemble was produced; fresh baseline complete; both physical sibling revisions **accepted**; member 1 native run **rejected** because of the malformed analysis; member 2 completed. The model store had **three revisions** including the root, rather than only the root. This is a reproducible preflight contract violation, not evidence of an incorrect numerical value.

**Correction:** Before creating the output or calling revise, validate the **complete syntactic schema, unknown keys, versions, types, shapes and finiteness** of all nested authored V1 objects. Keep *physical* admission/removed-body observation failures as per-member outcomes where the contract intentionally permits them; do not conflate malformed JSON grammar with an admissible but unsupported member investigation. Add a regression asserting zero side effects for unknown nested analysis/investigation/presentation keys.

### R2-02 — BLOCKER: a JSON numeric exponent can bypass finite-input preflight and reserve a revision

**Pinned source:** [scenario_ensembles.py lines 112–139](https://github.com/physicsvigilante/emfeeld/blob/38773a546d76616fe815eb302c418281bded7c1d/src/emfeeld/scenario_ensembles.py#L112-L139) has no deep finite-number guard; [model_revisions.py decode](https://github.com/physicsvigilante/emfeeld/blob/38773a546d76616fe815eb302c418281bded7c1d/src/emfeeld/model_revisions.py#L44-L55) rejects explicit NaN/Infinity tokens but the standard JSON numeric token **1e400** is converted by Python's default float parser to infinity.

**First independent reproduction:** Change the first member's field observation x coordinate to the literal JSON token 1e400 (not the non-JSON Infinity token). Keep the other member, all physical proposals, and sealed original template valid. Call run_ensemble.

**Expected:** Strict preflight rejection; original source/model store and original run unchanged; no ensemble output or accepted child. **Observed:** A ValueError was ultimately raised **after** output/started/baseline were written and the first physical V3 revision was **accepted**. The attempt lacks summary.json and integrity.json (correctly **not** a false complete marker), but a revision identity is already consumed; the store contained **two revisions** including root. This is more consequential than a cosmetic parser error because replay of the same IDs is now blocked.

**Correction:** Reject all nonfinite values from JSON numeric-token overflow **before any writes**; check every recursively nested authored number and pre-serialize/validate all data that execution later encodes. Either supply a strict finite-aware JSON float parser or a deep finite guard in the new ensemble input path, without weakening the existing shared parser's duplicate-key protection. Add regression with literal 1e400, not merely NaN or Infinity.

### R2-03 — MAJOR EVIDENCE DEFECT: inspector does not re-bind stored proposal bytes to a rejected decision

**Pinned source:** [scenario_ensembles.py lines 296–324](https://github.com/physicsvigilante/emfeeld/blob/38773a546d76616fe815eb302c418281bded7c1d/src/emfeeld/scenario_ensembles.py#L296-L324) compares output decision.json to the store's decision.json, but does **not** verify the store's proposals/<hash-id>/proposal.json bytes against the decision's already-recorded proposal_sha256 (or against the retained member proposal). [ModelStore.revise](https://github.com/physicsvigilante/emfeeld/blob/38773a546d76616fe815eb302c418281bded7c1d/src/emfeeld/model_revisions.py#L389-L420) explicitly records proposal_sha256 at original attempt creation.

**First independent reproduction:** Produce a partial ensemble where member 1 is physically rejected on a deliberately wrong expected old source property and member 2 succeeds. Confirm inspect_ensemble passes. Alter **only** member 1's proposal.json in the native model store, without modifying its decision.json or any ensemble sealed file. The stored proposal's SHA256 now differs from decision.proposal_sha256. **Observed:** inspect_ensemble still passes unchanged. It therefore reports a valid retained rejected decision even though the model store no longer contains the original proposal bytes associated with that decision. This does **not** require attacker re-signing of unkeyed hashes, and can occur from accidental file drift.

**Correction:** On inspection of **every** member, accepted and rejected, verify (a) store proposal bytes SHA256 equals decision.proposal_sha256, (b) the store's original proposal equals the exact retained member proposal bytes/identity, and (c) the proposal ID maps to the correct store directory; preserve rejected/no-op outcomes and exact original bytes. Add negative regression for store proposal drift, including rejected members.

## Independently executed tests and first attempts

All tests below are **Chat B-authored**, outside the extracted source tree; author CI and author-written E1/G1/T1 reference checks are not counted as independent Chat B test definitions.

**Environment:** Linux container; CPython 3.13.5, NumPy 2.3.5, SciPy 1.17.0, pytest 9.0.2; source imported via PYTHONPATH to the pinned extracted tested-source. No Conda modification, pip installation, renderer usage, source PR edits, or saved user-study edits.

**First test batch:** 12 newly authored pytest definitions: **10 passed / 2 failed**. Source/script file emfeeld_r2_review_tests.py; exact first command equivalent to:

    PYTHONPATH=/mnt/data/emfeeld_review/src:/mnt/data/emfeeld_review/tests \
      python -m pytest -q -rA /mnt/data/emfeeld_r2_review_tests.py

First log file emfeeld_R2_first_attempt.log, SHA256 **08158a28069cfc54908e109c5f358b92b75b65b152b5189387ff98412dd2b542**. First failure signatures were **Failed: DID NOT RAISE** for the unexpected nested analysis key and **AssertionError: 1e400 parsed to float infinity and got past preflight** for the finite-input guard.

**Supplementary batch:** 8 additional new pytest definitions: **7 passed / 1 failed**. Script emfeeld_r2_followup_tests.py. Exact first log emfeeld_R2_supplement_attempt.log SHA256 **bac3b87540d9901297e52a391650219039a327e7df9074c8b9e22e587a579f2c**. Failure signature: **Failed: DID NOT RAISE RevisionError** after a rejected store proposal changed while its native decision was unmodified.

**Total Chat B pytest definitions:** **20 distinct, 17 passed, 3 failed**. Original first logs were retained without replacing them with corrected/green expectations. This is a finding on the pinned PR, not a repaired source candidate.

**Positive adversarial tests:** original root and sealed template byte preservation; same-root alternatives and strict signed comparison; stale raw baseline SHA preflight refusal; duplicate JSON key refusal; one rejected sibling leaving another complete; re-signed aggregate completion inconsistency refusal; re-signed native field/vector magnitude mismatch refusal; re-signed authored expectation/check forgery refusal; re-signed NPZ saved sample contradicted by its native result refusal; mismatched world-coordinate probe typed **different_world_point/unavailable/null**; swapped ordered potential endpoints typed **endpoints_mismatch/unavailable/null**; output symlink alias refusal; incomplete revision history and stale structural lock fail-closed; removed ancestor physical-ID reuse rejected without destroying a valid sibling; interrupted baseline retained started/pending evidence only. A deliberately injected incomplete **fresh** baseline yielded two **not_attempted** members and no accepted revisions (synthetic injection to exercise the branch, not a real spontaneous native failure).

**Concurrency:** A separately executed fork-based adversarial race synchronized two processes just before first ModelStore.revise; both had already passed preflight for the same proposal IDs but used different fresh output paths. First attempt: **one complete accepted ensemble; the other FileExistsError on proposal mkdir, with started marker but no summary/integrity; three revisions total**. This is an observed fail-closed local race, **not** proof of global transaction atomicity, crash recovery or distributed locking. Original log emfeeld_R2_concurrency_attempt.log SHA256 **a29aba53707112c2da9584869f47304c8803b49a099cfe8dde5a963d7d92f672**.

## Novel independently expressed physical references (not author E1/G1/T1)

**New electric case:** Two separately centered uniform solid spheres (radius 2 m each; centers x=-0.2 m, +0.2 m), with initial charges -1e-9 C and -2e-9 C. Two independently authored V3 sibling alternatives set charges to (-3e-9,+1e-9) C and (-4e-9,+3e-9) C. Independently computed the **inside and outside** fields using E=kQ(r-c)/R^3 inside and E=kQ(r-c)/|r-c|^3 outside, with inside V=kQ(3R²-|r-c|²)/(2R³), outside V=kQ/|r-c|. Evaluated at world positions [0.25,0.2,0.1] m and [3.5,-0.8,0.5] m. Checked **eight** signed cross-revision measurements total: outside vector and magnitude, inside vector, and the *ordered* potential difference, for both siblings; all passed **rtol=2e-12, atol=1e-11** (SI units). Verified same immutable root, two independent child parents, exact unmodified parent run bytes.

**New gravitational case:** One prescribed uniform gravitational acceleration g₀=[0.1,-0.2,0.3] m/s² and two independent test bodies. First V3 alternative changes g to [0.5,-0.1,-0.2] m/s², **removes the earlier-indexed test body** and inserts a fresh body, so the surviving named body changes native index **1→0**. Second changes g to [-0.3,0.4,0.2] m/s² and inserts a different fresh body, keeping the survivor at index 1. For both siblings, checked the field, the ordered potential difference ΔΦ=−Δg·(r_to−r_from), the surviving body's saved position difference Δx=½Δg t² and velocity difference Δv=Δg t at **actual saved t=0.5 s** (sample index 10): **eight** signed comparisons, all passed (field absolute tolerance 1e-14; potential 1e-12; trajectories 1e-9 SI). Confirmed mappings and saved physical time on both sides; no index retargeting or fabricated added-body motion.

These independently selected formulas and choices do not establish generic physical correctness for unsupported laws, material conductors, collisions or all integration horizons.

## Exact-head CI and original release artifact cross-check

[Exact-head clean-install Linux/Windows workflow 43858694317](https://github.com/physicsvigilante/emfeeld/actions/runs/43858694317) is GitHub-reported **completed/success**, attempt 1, both Ubuntu 24.04 and Windows 2022 jobs. [Separate real-PyVista workflow 43858694370](https://github.com/physicsvigilante/emfeeld/actions/runs/43858694370) is **completed/success**. Both run records identify the exact pinned source head; the [source snapshot workflow 43858694305](https://github.com/physicsvigilante/emfeeld/actions/runs/43858694305) likewise succeeded. The request reports 1,424 headless + 18 historical behavioral + 33 real-PyVista = 1,475 suite memberships **per OS**, with 22 ensemble focused definitions included in headless. These are **author CI**, not new reviewer tests. Independently ran the 22 existing focused tests against the extracted archive: **22 passed** locally (also author-defined tests, not added to the 20 above).

Independently downloaded the **original release ZIP bytes**:
- Linux artifact 14222248006, SHA256 **5483c2754d7513fafe61a1823c0b09c8c60a25706f47fc8685292bf2f101ad2f**.
- Windows artifact 14222274292, SHA256 **eb9e17b42531a889a7de03c70c71f087bf803c1109b1aeaa229537623897c970**.

**Per OS:** 2,151 ZIP entries, 2,151 distinct paths, zero CRC failures. Saved head-sha.txt equals merge-preview cce77c7767a824558ea702492ddbf6ce7d95c101 with exactly the requested Git tree. An independent Python SHA256/inventory audit of the actual archived scenario-ensembles subtree verified **18 ensemble/run/comparison inventories**, **9 native nested inventories**, **9 complete native runs**, **6 comparison records** (4 complete, 2 partial), **32 fulfilled signed comparisons and 2 explicitly unavailable/null/unknown_operand**, and **12 trajectory-pair equal-time bindings**, separately on Linux and Windows. It checked each retained comparison's arithmetic against its archived native operands; the pinned source's deterministic inspect_ensemble also passed for all six archived E1/G1/T1 ensembles. E1 and T1 aggregate complete; G1 partial by explicit absent-body comparisons. The original ZIP and nested byte checks are not a second independent physical reference for author-preselected E1/G1/T1.

Independent archive audit command equivalent to:

    PYTHONPATH=/mnt/data/emfeeld_review/src python /mnt/data/emfeeld_archive_audit.py

Original audit log SHA256 **83ec1dd279c45f4343da9e803aecd5fcf2f6b072e9f996d338f8635134e441ce**; audited both original ZIPs with source snapshot separately extracted.

## Review boundary and merge gate

**Supported within this review:** atomic V3 sibling proposals genuinely reference one parent and publish no half-accepted intermediate V3 snapshots; fresh baseline calculation rather than inherited pass; member native completion is separate from construction acceptance; genuine comparison coordinates, potential sign, units, time and stable ID are protected in tested paths; incomplete outputs are not false complete; local writer lock/collision cases fail closed; deterministic inspector catches numerous re-signed contradictions; archive evidence is internally coherent. **The three defects above remain open.**

**Not established:** malicious-party authenticity if an attacker rewrites and re-seals *all* unkeyed evidence; distributed/crash-safe transaction guarantees; manual Windows pointer interaction or classroom usefulness; comprehensive blind held-out physics qualification; new solver laws. No entire 1,424-test suite or real PyVista UI was rerun by Chat B locally; those remain clearly attributed to GitHub author CI. The concurrency injection and synthetic failed baseline are fault-injection tests, not organic production incidents.

**Required before merge:**
1. Fix R2-01 and R2-02 so malformed/overflowed member input cannot reserve physical revisions, create completed/partial ensembles, or leave avoidable pending output after supposedly strict preflight; preserve intentional physically invalid member outcomes.
2. Fix R2-03 by checking native store proposal bytes against the retained decision SHA and exact member proposal on inspection, including rejected and no-op members.
3. Preserve the failing tests and original evidence; add targeted cumulative regressions for each; publish a new exact head SHA/tree and rerun proportionate full Linux/Windows clean-install CI, separate viewer workflow and original archive integrity checks.
4. Re-review the corrected preflight and inspector paths at the new SHA; retain this review unchanged for the original commit. Do **not** treat this report as source merge authorization. User/owner approval and post-merge verification remain separate gates.

**Final scoped verdict: CHANGES REQUESTED** for **38773a546d76616fe815eb302c418281bded7c1d** only.