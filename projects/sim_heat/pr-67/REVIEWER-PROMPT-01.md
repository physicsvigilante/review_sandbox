# Ready-to-paste independent Chat B — SIM_HEAT PR67 R2 exact-junction solver review

You are independent reviewer Chat B. Review the new **OFFLINE-only exact-rational junction-equilibrium solver** for generic H1 `RodArea` networks. This is numerical/physical source code; perform R2 source/physics/error-bound review, not a native simulation or release decision.

**Source draft PR67:** https://github.com/physicsvigilante/sim_heat/pull/67  
**EXACT source HEAD:** `4517bf8e14f659e79255bc1d20f7fcb7b72ce695`  
**Complete Git tree:** `03f18f698252519acd2ec40ca288cd8905202018`  
**Reviewed-in-scope but still DRAFT PR66 base:** `563e10eaa3ec9d7433752172e332cb28b9b9fb41`.  
**PR synthetic checkout:** `43a07ead4626607b6ff468a2370c1c4661637957`, identical whole tree.

**READ the full request FIRST:**  
https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-67/REQUEST.md

Inspect all four N6 additions on the exact HEAD, central PROTOCOL/RISK POLICY and existing H1 contracts. Independently check `qualification/h1_n6/exact_junctions.py` and execute your own non-native controls where available. A new unfamiliar supported `RodArea` graph should solve with exact rational junction KCL, without changing any checker code. Challenge unique Dirichlet solvability, Gauss–Jordan positive pivots, source-exact G and original-node residuals, orientation and boundary/instantaneous-body signs, maximum principle, parallel/disconnected anchored graph cases, resource refusals and strict ASCII body-temperature grammar.

**Critical fail-closed scope:** original T1-T has a circular rod and must REFUSE in N6; no midpoint Pi or floating-point fabricated exact junction solution. N5 still supports circular interval trials. Source SHA is caller integrity, not independent owner provenance. Every output must explicitly distinguish *algebraically solved storage-free junctions* from assumed body temperatures, a true time-integrated IVP or qualified native state.

**Hosted source CI:** [PUSH 44529162842](https://github.com/physicsvigilante/sim_heat/actions/runs/44529162842) and [PR 44529604939](https://github.com/physicsvigilante/sim_heat/actions/runs/44529604939) both SUCCESS, **13 new N6 +11 N5 +15 N4 +12 N3 +16 N2 +17 N1 interval +34 N1 plan +152 H1 =270 distinct OFFLINE tests each**, docs parity, all original 7 physical static 100x failures and 8 native blockers. These jobs do NOT independently certify physics or prove native capability. Preserve historic evidence.

**Publish one NEW independent report directly to:**  
`physicsvigilante/review_sandbox/projects/sim_heat/pr-67/reviews/review-01-chat-b.md`.

Verdict SCOPED PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE on exact source HEAD; distinguish personally executed adversarial proof from hosted logs. Preserve older reviews. Do not query/install/build/launch OpenModelica, prepare actual native references, change original source, C1/archive, merge PR67/66/65/64/63/62/60/59, or deploy. After publication owner can tell Chat A **"review done"**.
