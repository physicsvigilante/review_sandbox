# Ready-to-paste Chat B — SIM_HEAT PR68 rigorous interval circular-junction R2 review-01

You are **independent reviewer Chat B** in a separate conversation. Review one new **offline-only rigorous physical/numerical method**: interval enclosure of thermal junction equilibrium on supported graphs containing RodCircular conductors. This is NOT a request for native simulation, general dynamic IVP qualification, source promotion or a PR merge.

**Draft source PR68:** https://github.com/physicsvigilante/sim_heat/pull/68  
**EXACT source HEAD:** `4f4bbabc1083f2e1f8a6ced66c00b95fea1a5128`  
**Whole Git tree:** `5cf0e68e87a81ba641b4d6ef5f9f215120670dc5`  
**Reviewed-in-scope DRAFT PR67 base:** `4517bf8e14f659e79255bc1d20f7fcb7b72ce695`.  
**Synthetic PR checkout:** `5d6384ba6949ecd52488960eacaa63862a5c3dbb`, identical complete source tree.

**READ THE FULL REVIEW REQUEST FIRST:**  
https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-68/REQUEST.md

Read central PROTOCOL/RISK POLICY, source AGENTS/H1 contracts, exact new `qualification/h1_n7/verified_junctions.py`, its tests and README. Review N6 exact rational Dirichlet helper and N4/N5 source Pi/conductance enclosure only as needed for this new proof; do not rerun broad previous accepted physics audits absent new issues.

**Attack the mathematical proof:** N7 takes exact rational bounds `G_e=[lo,hi]` for each positive source conductance and solves midpoint `x0` as an internal proof point only. For every true `g∈[lo,hi]`, verify `|b(g)-A(g)x0| ≤ r`; verify rowwise `A(g)v ≥ r` for all coefficients using **lo if v_i-v_j≥0, hi otherwise**, including known-neighbor terms, and `v≥0`. Verify the positive anchored M-matrix inverse is nonnegative; therefore `x0±v` rigorously contains the unique actual physical junction solution. Challenge missing sign, aliases, correlated parameters, graph source consistency and resource overgrowth. Confirm true-zero junction balances are not misrepresented by uncorrelated interval sums.

**Independent controls:** Test original T1-T with source-physical circular `T06` and assumed body T (do NOT claim solved IVP); independently derive the simple `G=π` one-junction serial case and interval endpoints; invent different multi-junction area/circular parallel/loop graph(s) and compare an independently generated rational corner solution with N7 enclosures. Test orientation, exact-area singleton, all-equal-boundary singleton, no unknown, small/large conductance interval refusal, singular/unanchored or false proof, caller hash/ASCII Kelvin boundaries, and all false native/trajectory/reference flags.

**Hosted exact-head evidence:** [PUSH CI 44535472230](https://github.com/physicsvigilante/sim_heat/actions/runs/44535472230) and [PR CI 44535966432](https://github.com/physicsvigilante/sim_heat/actions/runs/44535966432) both SUCCESS, **13 N7 +13 N6 +11 N5 +15 N4 +12 N3 +16 N2 +17 N1 interval +34 plan +152 H1 = 283 distinct OFFLINE checks each**, docs parity and old seven physical-reference 100× failures/eight native blockers. Old [PUSH RED 44535203687](https://github.com/physicsvigilante/sim_heat/actions/runs/44535203687) remains historical test-only error. Do not treat metadata/hosted runs as independent physics proof, and do not count runs twice.

**Publish one independent original report** directly to:  
`physicsvigilante/review_sandbox/projects/sim_heat/pr-68/reviews/review-01-chat-b.md`.

Verdict **SCOPED PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE** for N7 ONLY, pinpoint reproducible adversarial counterexamples and attribution of personal vs hosted evidence. Preserve earlier reviewer reports. Do NOT install/query/build/launch OpenModelica, adopt reference bundle, rewrite C1/history, execute native simulation, claim owner approval or merge PR68/67/66/65/64/63/62/60/59. Owner may tell Chat A “review done” only after this report is committed.
