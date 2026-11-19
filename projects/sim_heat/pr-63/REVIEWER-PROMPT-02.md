# Ready-to-paste Chat B — SIM_HEAT PR63 focused R2 correction review-02

You are **independent Chat B** in a separate conversation. Conduct **one narrowly scoped R2 correction review of PR63 F-01 and F-02**, not a new full thermal physics or native simulation review.

**Source [DRAFT PR #63](https://github.com/physicsvigilante/sim_heat/pull/63)**  
**EXACT corrected HEAD:** `6baba681ae1680e2fcae1ea8efbf0953afcb031b`  
**Full Git tree:** `27b6ce015d5ba8229ee5990d3fa1e90352fe3f45`  
**Rejected initial reviewed HEAD:** `232bca1737210a80e1fb8e41b7ec67c6248f6a9f`  
**Fail-first tests-only HEAD:** `41d735e500d306d0d235b5306eabf880734078ab`  
**Stacked accepted PR62 source base:** `29bc126967d180e7f92b0a8bc29f50ee17608eb7` (still draft/unmerged).

**READ this exact correction request FIRST:**  
https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-63/CORRECTION-REQUEST-02.md

Read independent [review-01](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-63/reviews/review-01-chat-b.md) and [Chat A response-01](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-63/responses/response-01-chat-a.md). Review the exact OLD→NEW change limited to three N2-only files.

**F-01:** Previously original facts/study SHA verified first byte reads then parsed second, unverified reads. Reviewer personally created a scratch-file race and re-sealed forged provenance pair that passed. New `_original_inputs` must read facts/model/study **once each**, hash exactly these byte snapshots and parse those same bytes. Reproduce old bypass if feasible and challenge corrected code with after-first-read replacement of facts/provenance and study, and caller-supplied re-sealed specs. Corrected code must never use unverified later reads or issue false `checks_passed`.

**F-02:** Previously malformed bundle dict/list, oversized allowance integer and ill-formed Unicode CSV raised raw exceptions. Test direct public `compare_candidates` on these and new malformed types. New shallow source shape admission, finite-number guard, CSV encoding gate and public typed Refusal wrapper should reject without raw exceptions. Check that old normal primary-only / per-run semantics and known negative numerical comparisons are unchanged.

**Evidence:** Full [PUSH 44482539578](https://github.com/physicsvigilante/sim_heat/actions/runs/44482539578) and [PR 44482548998](https://github.com/physicsvigilante/sim_heat/actions/runs/44482548998) both GREEN, each **16+17+34+152=219** unique offline tests. Original [FAIL-FIRST 44482131234](https://github.com/physicsvigilante/sim_heat/actions/runs/44482131234) preserved with 2 failing adversarial race tests/3 malformed exception errors. PR synthetic merge `d7e368ed34ce6c5f04a5ecb1301972ca91f37a77` has same complete corrected HEAD tree. No physics or native code changed. Attribute hosted evidence versus your own test executions.

**Write one NEW independent report directly to:**  
`physicsvigilante/review_sandbox/projects/sim_heat/pr-63/reviews/review-02-chat-b.md`.

Verdict **SCOPED PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE** at the exact HEAD, with regression and provenance evidence and remaining limits. Do NOT overwrite review-01, request another broad PR60/PR62 review, or invent a native certificate. Original seven checking-centre refusals, eight native blockers and UNSEALED scorer remain; PR63/PR62/PR60/PR59 stay draft/unmerged.

**STOP:** No OpenModelica installation, version query, build or launch; no native result, old reference regeneration/C1 archive edit, merge or deployment. After publishing, the owner can tell Chat A **“review done”**.
