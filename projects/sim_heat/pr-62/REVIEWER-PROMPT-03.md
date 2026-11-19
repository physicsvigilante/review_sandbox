# Ready-to-paste Chat B — PR62 targeted R2 review-03 (F-02 switching-iterator bypass only)

You are **independent Chat B**, reviewing a narrow new F-02 fail-closed correction, not a new full physics/interval implementation or a native simulation.

**Source [DRAFT PR62](https://github.com/physicsvigilante/sim_heat/pull/62)**  
**EXACT source HEAD**: `29bc126967d180e7f92b0a8bc29f50ee17608eb7`  
**Full Git tree**: `111e277e45520afd2550c71f9917950d7d8ba532`  
**Previous rejected HEAD**: `b8663d62af605607608fd43cfeb29e44012171ee`  
**Stacked PR60 base**: `58ca02b293f2afbd931ab7ad1832fc4e34df1574` (draft/unmerged).

**READ the exact correction request FIRST:**  
https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-62/CORRECTION-REQUEST-03.md

Then read original independent [review-02](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-62/reviews/review-02-chat-b.md) (F-01 PASS, F-02 CHANGES REQUESTED) and [Chat A response-02](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-62/responses/response-02-chat-a.md). Inspect the one-commit OLD→NEW diff for exactly three N1-specific files.

**Independently attack only the F-02 bypass:** Previous `exp_step` let changing-iterator `list` subclasses fake a zero final row during validation and supply a nonzero row during arithmetic, then falsely overwrite the exponential final row to identity. New code admits only **exact built-in** list/tuple containers, snapshots every exact typed `I` cell's two integer endpoints into private immutable tuple rows, and validates and calculates on that snapshot. Personally rerun the review-02 `SwitchingRow` and outer-matrix subclass attacks; test malformed/aliased/nonzero-zero-containing rows, and canonical 2×2 and actual T1-T 7×7 matrices at both grids. Confirm no silent false enclosure remains.

**Exact-head hosted CI**: PUSH https://github.com/physicsvigilante/sim_heat/actions/runs/44472361884 and PR https://github.com/physicsvigilante/sim_heat/actions/runs/44472366883 both GREEN. Each runs **17 +34 +152 =203** checking-only tests plus both full grids; unchanged primary trace SHA `b13877c8d069a60928cf3b23ae007b1a10feb53151f00ffb65a57082a7fc10af`, dense `9ba71a1d2fccb39be071df0647793f6fb844737e2ac9c91bb143546ab8d26b40`. Distinguish your own reruns from hosted logs and developer assertions. All original seven checking-centre refusals and eight native blockers remain.

**Publish exactly one NEW independent report** directly to:
`physicsvigilante/review_sandbox/projects/sim_heat/pr-62/reviews/review-03-chat-b.md`.

Verdict **SCOPED PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE** for **F-02 only**; identify actual personal negative/positive controls, old/new SHA, remaining limitations. Do not redo accepted F-01, whole PR60 design, previous numerical physical checks, or rewrite older review reports. No OpenModelica install/version/build/launch, PR merge, reference/C1 changes, or native readiness claim. After publishing, the owner can tell Chat A **“review done”**.
