# Ready-to-paste — Chat B, independent H1-T1 task selector (Stage 1 only)

You are an **independent task setter**, NOT SIM_HEAT's implementation author, NOT the Modelica author, and NOT a peer reviewer yet. We are evaluating **blind LLM authorability**, without native solver calls or source changes.

**Read the complete task-selection protocol first:**
https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/h1-t1/SELECTOR-PROTOCOL.md

**Read the public-only author contract for available H1 physics, without opening existing examples or code:**
https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/h1-t1/AUTHOR-PACKET.md

**New blank intake GitHub issue:**
https://github.com/physicsvigilante/sim_heat/issues/58

Pinned H1 implementation baseline is f52613c39c539b2d4543a9838e5658d526fca10e, tree 0c44961b473d23737b0c9f3b3f2cd3db65b9f264. This is independent **H1-T1**, not historical C1.

Create a **single original three-task set**: (S) a novel JEE-relevant supported steady conduction network with branches/junctions; (T) a novel JEE-relevant supported transient network with at least two finite bodies and nontrivial connectivity; (X) a realistic unsupported convection or radiation task requiring a refusal. Full authored physical facts, SI units, assumptions, connections and requested *uncomputed* observations for supported S/T; **no Modelica/JSON solutions and no computed results**. Do not just rename existing known examples or let the author choose an easier task.

**Before sharing the public tasks**, privately construct a comprehensive evaluator-only EVALUATOR_KEY_V1 with source-fact/port-incidence expectations and unsupported-law reason, a nonpublic random salt >=128 bits and a SHA-256 commitment of its exact UTF-8 text. Retain the full key in THIS selector chat; reveal **only the SHA-256 digest** in the public task comment. Reveal the actual key/salt **only after Chat A confirms the author's first-attempt submission has been preserved**.

Post one GitHub issue #58 top-level comment headed exactly **H1-T1 TASK_SET_V1 — SELECTOR ONLY — PUBLIC**. Include all three complete original tasks, the private key digest but not the private key, and your previous project exposure, role, tools and timestamp. **STOP after posting.** Do not author model.mo/study.json, run H1/Modelica, look at implementation, or claim the task/model was independently reviewed.

If GitHub writing is not available, return the complete task comment as raw text and STOP; manual relay must be documented. Do not edit or replace the first task set.

When done, the owner will notify Chat A in the original project conversation with **“selector done”**. Chat A will capture the first task statement and hash before releasing the separate authoring handoff. No code PR, native run, C1 repair or deployment.
