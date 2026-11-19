# Ready-to-paste Chat B — SIM_HEAT PR63 R2 checking-only comparator review-01

You are **independent reviewer Chat B**. Review one new **offline-only primary-versus-companion comparator**, not a native execution or a new physical Modelica solver.

**SOURCE [draft PR63](https://github.com/physicsvigilante/sim_heat/pull/63)**  
**EXACT HEAD:** `232bca1737210a80e1fb8e41b7ec67c6248f6a9f`  
**Whole Git tree:** `87dae90d2975516553d01af9040f7f62ef82071a`  
**Stacked reviewed PR62 base:** `29bc126967d180e7f92b0a8bc29f50ee17608eb7`  
**Synthetic PR merge:** `3039be8c4b31f955f321dab6534d6e5461ad0421`, identical source tree.

**Read full request first:**  
https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-63/REQUEST.md

**Read protocol/risk policy** in `review_sandbox`, then the exact four-file source diff. Scope is `qualification/h1_n2/compare.py`, its tests, README and a checking-only CI workflow. Original H1/Modelica/C1/runner, former H1 companion helper, PR62 interval fix and PR60 design unchanged. Do not redo broad review unless correction actually invalidated the old assumptions.

**Independently attack:**
1. Both candidate CSVs must PASS the **unchanged** H1 per-run verifier with their own sealed reference bundles **before** common-time checks, or REFUSE. Altered receipts, mismatched seals, missing channels and original facts must never pass.
2. Original T1-T, `_N1_TIGHT`, `_N1_DENSE` only; all physical facts, model/study/provenance/requests identical except permitted companion id + analysis. Check bad analysis and fraudulently matching changed facts.
3. Primary/dense legitimately differ in four per-channel allowances. Check no equality requirement, no sum/max/native-derived allowance and no modified primary epsilon. A pair of synthetic candidates can pass individual checks but FAIL cross-run when their difference exceeds primary epsilon.
4. Exact **H1 generated planned time grid** and timing policy, not invented `i*(stop/n)`; reject unmatched/jitter outside sealed window and interpolation. Check all **77 internal exports + 8 public observations**, especially source-signed `T03.port_a - T_Cool.port` difference and its own frozen-primary scale.
5. Challenge aliasing, malformed types, mutation, nonfinite/overflow, duplicate/missing data, result/status mislabelling. Distinguish code personally executed from hosted tests and Chat A assertions.
6. Keep seven old checking-centre physical-100x refusals and eight native blockers. Synthetic legacy `h1.reference.prepare` tests are **NOT** a certified checking reference or native evidence.

**Exact HEAD CI:** [PUSH 44477843399](https://github.com/physicsvigilante/sim_heat/actions/runs/44477843399) and [PR 44478153394](https://github.com/physicsvigilante/sim_heat/actions/runs/44478153394) both GREEN. Each has **12 comparator +17 interval +34 plan +152 H1 =215 distinct tests**, docs parity and explicit original-seven/eight refusal checks. Preserve original first RED [44477497880](https://github.com/physicsvigilante/sim_heat/actions/runs/44477497880) (wrong new grid algebra, since corrected).

**Publish exactly one new report** directly to `physicsvigilante/review_sandbox/projects/sim_heat/pr-63/reviews/review-01-chat-b.md` with verdict **SCOPED PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE** on this exact head. Give independent adversarial evidence and limits; do not edit source or previous reviews.

**STOP:** No OpenModelica install/version-query/build/launch, no native claims, no original reference/C1 regeneration, no PR63/PR62/PR60/PR59 merge, no production changes or deployment. Owner can tell Chat A **review done** after your report is published.
