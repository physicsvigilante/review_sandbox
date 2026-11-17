# M36a — Fresh Chat B scientific/source-interpretation reviewer prompt #01

You are a **fresh separate-context GPT-6 Chat B reviewer**, not the author of conductor_sim PR #84. This is an **R2 source-interpretation and evidence-meaning review of a planning inventory**, **not** independent certification of 30 simulated JEE problems.

**Read and follow this full request FIRST:** https://github.com/physicsvigilante/review_sandbox/blob/main/projects/conductor_sim/pr-84/REQUEST.md

**Source draft PR:** https://github.com/physicsvigilante/conductor_sim/pull/84

**Immutable target HEAD:** `796d3f31d67dbeb5d82f57bf02512cf05242df64`

**Native Git TREE:** `c79540e3c4807673bb6037ebbc9fad014144c706`

**Released baseline `main`:** `73e076cf7eaf7fefbae2b24afc1f54ff8f0b6fc6`

### Mandatory independent actions

1. Verify **live** PR SHA/tree, its draft/unmerged state and ALL current-source required CI on GitHub. At handoff authoring, some full Python/FEMM/Chromium checks had not completed. **Do not PASS until each required source-head check actually finishes successfully.** STOP as stale-head if source changed; ask for a repinned request.
2. Read complete frozen charter, M21a historical 29-case JSON, current 30-case JSON, evaluation contract, original source docs/source PDFs where available, M36a CLI tests and review risk protocol/template. The new official 2021 Paper 1 Q9–10 is **one apparatus**, not two successes; 29 old anchors must be exactly preserved.
3. Independently challenge the **24 candidate 'supported_scoped' labels**: is each scope actually qualified for the original question, or are any supported only with extra assumptions that belong in partial? Pay special attention to the ideal conducting sheet and stopped electron; the real dipole energy-only question; proton with qE+mg, source-given vertical plates; transverse field in two-ring work; far-separated sphere approximation; static Kelvin sphere versus induced current; incomplete oil-drop transient; general irregular multi-cavity local 3D fields. Read representative implementation code and anchor source facts, not just M36a's labels.
4. Execute original/hostile audit probes independently if possible: mutate source page/anchor, source PDF digest, 30th apparatus identity, fake a physics PASS, edit route counts, remove a doc, mutate 3D refusal, claim an unobserved JEE viewer, etc. Compare the 29 historic originals against candidate; run the exact-source `python -m tools.m36a_jee30_audit` and `pytest tests/test_m36a_jee30_audit.py`. Note first failures rather than silently deleting them.
5. Independently derive a small sample of paper-level source physics: p2 ideal metal plane E=sigma/epsilon0, p5 dipole U=-p·E, p15 proton qE=mg, p12 ring work with nonzero transverse force, official 2021 V=0 circle. These reference probes assess **scope accuracy**; even if correct, they DO NOT turn all 30 into new end-to-end native simulation passes.
6. Enforce honest denominators: the new matrix presently says **24 documented scoped routes, 3 partial, 3 unsupported**, AND **zero source-specific M36a native replays, zero independently verified JEE runs, zero new browser inspection, zero new PDF visual reinspection**. Check whether these labels are accurate. An unsupported but justified refusal is never a completed simulation. Keep textbook answer completeness optional/separate.

### Original report and release authority

Publish your ORIGINAL report under:

`projects/conductor_sim/pr-84/reviews/review-01-chat-b.md`

in `physicsvigilante/review_sandbox` (directly or via review PR). Give source SHA/TREE, test failures/successes you actually observed, independent source-physics challenges, questionable candidate classifications and explicit **PASS / CHANGES-REQUESTED / INSUFFICIENT-EVIDENCE** for the *inventory review only*. If you cannot execute independent probes, report limitations accurately. This is not 30-case numerical coverage certification.

Do not change `conductor_sim` production, mark its draft PR ready, merge it, or infer owner approval. After your review, Chat A checks unchanged SHA/tree and source-head CI; owner separately approves exact-head merge and main-push release verification. Further genuine JEE case executions remain a distinct milestone regardless of this report.
