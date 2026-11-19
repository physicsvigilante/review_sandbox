# Ready-to-paste independent Chat B — SIM_HEAT PR66 R2 generic graph-balance review

You are **independent reviewer Chat B**. Perform one R2 source/physics review of a new OFFLINE **generic thermal graph assembly and user-trial inspector**. Do not call it a native simulator, complete time solver or certified numerical reference.

**DRAFT PR #66:** https://github.com/physicsvigilante/sim_heat/pull/66  
**EXACT HEAD:** `563e10eaa3ec9d7433752172e332cb28b9b9fb41`  
**Whole Git tree:** `9b06cabe69c64d9ae33f5ebfc1cba9901ad5e39c`  
**Stacked, reviewed-in-scope PR65 base:** `f533d10fd38dc38710bba223e0bdb88f264e4398` (still draft/unmerged).  
**Synthetic PR checkout:** `b3665ad7d928bd21ae60a180cd2c844f2498fe9a`, identical Git tree.

**READ FULL REQUEST FIRST:**  
https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-66/REQUEST.md

Read central protocol/risk policy, source AGENTS.md and H1 contracts. Inspect the exact four N5 additions, particularly `qualification/h1_n5/thermal_graph.py` and its tests. No unchanged H1 runner, PR65 static math, PR64 owner trust design or C1 history needs a new broad audit unless N5 breaks assumptions.

**Independently attack physical composition:** For any supported source rod `a→b`, is `q_ab=G(T_a−T_b)` physically and sign correctly assembled with source-exact rational G interval? Is each port `+q`/ `−q`, every body `C dT/dt=−sum Qout`, ownerless junction zero-outflow, and fixed boundary source outward supply correct? Try unfamiliar steady/transient graphs, serial/parallel branches, circular rod with Pi bounds and **reversed orientation**. Verify isolated-body and connected-graph admission. Check whether interval arithmetic and antisymmetry claims are sound without conflating numerical interval sums with structural identity.

**Independently attack the trial boundary:** `evaluate_trial` must require one exact decimal STRING per node and enforce fixed boundary temperatures, refuse missing/extra, floats, nonfinite, negative/zero and source SHA drift; an arbitrarily guessed nonzero junction residual must stay visible, never be repaired or reported as a solved state. Try a genuine equilibrium trial and a nonequilibrium trial; independently derive a few heat flows and initial instantaneous rates. Inspect statuses and trust: N5 is not an all-grid trajectory, independent source authority, native reference bundle or OpenModelica run.

**Hosted current-head CI:** [PUSH 44519403103](https://github.com/physicsvigilante/sim_heat/actions/runs/44519403103) and [PR 44519762430](https://github.com/physicsvigilante/sim_heat/actions/runs/44519762430) both SUCCESS, each **11+15+12+16+17+34+152=257** distinct offline tests, docs parity, original seven static physical-100× failures and eight native blockers preserved. The labelled source-only assembly/trial JSON is NOT an executed simulation.

**Publish exactly one independent report directly to:**  
`physicsvigilante/review_sandbox/projects/sim_heat/pr-66/reviews/review-01-chat-b.md`.

Verdict **SCOPED PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE** for the exact new source commit. State what you personally executed separately from hosted results, any reproducible fail-closed defects, and scope limits. Preserve old reviewer records. No OpenModelica installation, version query, build, launch, native output, reference promotion, historical C1 edits, deployment or PR66/65/64/63/62/60/59 merge. When complete, owner can say **“review done”** to Chat A.
