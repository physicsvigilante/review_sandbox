# Ready-to-paste Chat B — PR62 targeted R2 correction review-02 (F-01 and F-02 only)

You are **independent Chat B**, reviewing a narrow new correction on the existing numerical-reference source candidate. This is **NOT** a fresh broad thermal project review, independent native simulation, or permission to merge. Do not rewrite earlier reviewer reports or source.

**Source PR62 (DRAFT/UNMERGED):** https://github.com/physicsvigilante/sim_heat/pull/62
**EXACT corrected HEAD:** `b8663d62af605607608fd43cfeb29e44012171ee`
**Complete Git tree:** `3208ff20f46dd3ed1e1a2cd92e6f72f3f8f25309`
**Old reviewed HEAD:** `12bb67e7abac54c8a2488109cb706d779c61bf93`, original independent review-01 remains CHANGES REQUESTED on that old source.
**Stacked base:** reviewed design PR60 HEAD `58ca02b293f2afbd931ab7ad1832fc4e34df1574`, still draft/unmerged.
**Synthetic PR merge:** `71416580726e47f41e9f3ec6fa1f59f8f3cb309b`, identical complete corrected tree with parents design base then corrected source.

**READ complete correction request FIRST:**
https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-62/CORRECTION-REQUEST-02.md

Read prior independent [review-01](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-62/reviews/review-01-chat-b.md) and Chat A's [response-01](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-62/responses/response-01-chat-a.md). Inspect the EXACT old/new Git diff: **only three files changed** (`certified_reference.py`, its negative tests, and `INTERVAL-REFERENCE-V1.md`); original physical source/runner/reference/C1 unchanged.

### Independently challenge the TWO actual findings

**F-01**: Previously `certify(s)` would calculate from caller-mutated facts while stamping the original `FACTS_SHA256`. The correction must **recursively check full typed caller facts against a fresh SHA-pinned source snapshot**, refuse any T10 k/rod orientation/boundary/body/analysis/provenance/study identity/type mutation **before computation or creating output**, and then calculate from its private trusted snapshot rather than caller-owned mutable data. Test a canonical unmodified positive invocation too. Try to find a bypass.

**F-02**: Previously `exp_step` silently set its final result row to identity despite nonzero input last row. Check reviewer original **1×1 `[[I(1)]]`** and **2×2 `[[0,0],[1,0]]`** false-certification counterexamples now **REFUSE**, including a final interval containing zero but not exactly zero; malformed/mis-typed/ragged/too-large matrices and nonpositive grid must fail closed. Legitimate 7×7 T1-T affine zero-row remains accepted and its Taylor remainder/trace unchanged.

### Verified checking-only evidence

- Original 4 adversarial tests run against OLD code truly **FAILED** (21 subtest failures +1 error); new current source has 5 additional test methods, **16 interval tests PASS**, original **34 plan +152 H1 PASS**, docs parity PASS. Reviewer may reproduce old-vs-new directly; distinguish personal reruns from Chat A claims.
- **Corrected branch CI [44467515628](https://github.com/physicsvigilante/sim_heat/actions/runs/44467515628) SUCCESS**: artifact **14503276022**, SHA256 `14ae4e4c9708ffea84db99e72bfedb6650647c80b19d8b6b9d0e8989aa7959dc`.
- **Corrected PR CI [44467521226](https://github.com/physicsvigilante/sim_heat/actions/runs/44467521226) SUCCESS**, synthetic same-tree checkout: artifact **14502537890**, SHA256 `a39e61d471dab621bdd1e01ca88161cbcd79c3fe60b911770a04c09d4eb8c354`.
- Both full-grid mathematical JSON traces (2401/4801 samples) **BYTE_IDENTICAL before/after correction**: primary SHA256 `b13877c8d069a60928cf3b23ae007b1a10feb53151f00ffb65a57082a7fc10af`, dense `9ba71a1d2fccb39be071df0647793f6fb844737e2ac9c91bb143546ab8d26b40`. Chat A independently verified the 18 CRC-good ZIP entries and exact complete source.tar Git tree of BOTH corrected artifacts.
- **Existing old reference remains NOT APPROVED:** 7 original static checking-centre 100× REFUSALS still present, plus 8 native-execution blockers. New source-only JSON still declares `independentlyCertifiedReference=false`, `nativeExecuted=false`, `nativeQualified=false`, `runtimeReady=false`; the new candidate is NOT the runner's native reference bundle. Prior T1 source authorship remains UNSEALED due to lost scorer.

**Your task:** Issue ONLY a focused R2 judgment for F-01/F-02 on the exact corrected head. New complete report destination:
`physicsvigilante/review_sandbox/projects/sim_heat/pr-62/reviews/review-02-chat-b.md`

Verdict **SCOPED PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE**, with actual personally executed negative controls, counterexamples, unaltered canonical results, exact source identity, hosted-versus-personal attribution and remaining blockers. Do not request another whole-project/source-design review unless these changes truly invalidate it.

**STOP:** No OpenModelica install/version/build/launch, no PR62/PR60/PR59 merge, no historical C1/archive/reference regeneration, no promotion of old diagnostics, no deployment or claim of new native thermal outputs. After publishing the independent report, the owner can tell Chat A **“review done”**.
