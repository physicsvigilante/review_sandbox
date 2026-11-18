# H1-T1 — independent first-attempt author prompt (Stage 2 ACTIVE)

**Author-only handoff, released after the selector task comment was frozen.** Use this in a FRESH separate ChatGPT conversation (Chat C), not the selector conversation or the evaluator conversation. The selector's original task set is captured in [TASK-LOCK-01](TASK-LOCK-01.md); do not read the evaluator protocol, hidden key, SIM_HEAT implementation, existing worked cases or earlier reports.

You are an independent LLM source author, not the task setter. Your job is to attempt **exactly the already selected tasks** without first seeing evaluator answers, validator results or previous source implementations. Disclose any relevant prior SIM_HEAT exposure, tools and mechanical assistance. A new chat does not, by itself, prove human independence or different training data.

**Read only the TWO author inputs below:**

1. The source-pinned [public H1-T1 authoring contract](https://github.com/physicsvigilante/review_sandbox/blob/047987e91a7dd49784bbeed70222ea354904c6d9/projects/sim_heat/h1-t1/AUTHOR-PACKET.md). Its Git blob is `27dd142034c28911370ddd2bab328f14dcfb6f71`.
2. The immutable, locked [selector task statement](https://github.com/physicsvigilante/review_sandbox/blob/3ea30eb390660cf541fca95e95b668ac17ee02fc/projects/sim_heat/h1-t1/intake/TASK_SET_V1_COMMENT_6981681502.raw.md). This is the unedited text from [issue comment 6981681502](https://github.com/physicsvigilante/sim_heat/issues/58#issuecomment-6981681502), whose exact full UTF-8 SHA-256 is `8f45ad3d4a763952e25d60658ae4d8eeae37fd266bd372b3cd80fb19b81fa2a2`. The pinned snapshot controls if the editable issue comment changes later.

**Do NOT read:** the H1 parser/study/verification implementation, GitHub source checkout or example models, evaluator-only charter, task selector's key or salt, numerical solutions, previous reviews or C1 results. **Do NOT run:** the SIM_HEAT H1 validator, local authoring workbench, GitHub Actions, OpenModelica or any solver for this first attempt. Do not ask the evaluator for corrections or simplify any locked task. Standard-library SHA-256 hashing of your own newly written model files is permitted when disclosed; a guessed digest is not.

**Submit all three tasks in one original first-attempt issue comment:**

- Supported **T1-S (steady)**: provide complete `S/model.mo`, `S/study.json` and `S/AUTHOR_NOTES.md`, preserving all locked physical input values, exact rod port_a/port_b orientation, independent ideal-junction ownership and requested observations. Use supported steady mode and an empty analysis object. Do not compute temperatures or heat flows.
- Supported **T1-T (transient)**: provide complete `T/model.mo`, `T/study.json` and `T/AUTHOR_NOTES.md`, preserving all original specified bodies, boundaries, rods, port connections/directions, requested observations and original 0–2400 s time window. Choose a permitted **provisional** analysis grid if necessary, mark it as provisional, and do not compute any thermal trajectories.
- Deliberately unsupported **T1-X**: provide `X/REFUSAL.md` explaining the required physical law and the library gap, without inventing a surrogate conduction model or claiming a numerical result.

Use the required physical source inputs, valid SI units and exact H1 Modelica/study syntax from the public packet. Give every effective physical input a truthful source/illustrative provenance record and state supported model-regime assumptions. Distinguish original selector-invented teaching numbers from actual textbook givens. For any SHA-256 you cannot calculate, honestly disclose `HASH_UNRESOLVED`; this is incomplete first-attempt authoring, not permission to fabricate a digest. State uncertainties, source assumptions and tool assistance in the notes.

Post **ONE new top-level comment** at https://github.com/physicsvigilante/sim_heat/issues/58, beginning with exactly:

**H1-T1 FIRST_ATTEMPT_V1 — INDEPENDENT AUTHOR**

Include all seven complete original artifacts in clearly labeled, separate code fences, and include your identity/model as known, task exposure and any tools used. **Stop immediately after posting the FIRST draft.** Do not edit or replace the comment after seeing feedback. If you cannot post to GitHub, output the complete unaltered text for a disclosed manual relay and then stop.

The evaluator will capture your entire original comment's ID, timestamp, raw body and hash **before** verifying source fidelity, requesting the selector's withheld scoring key or invoking pinned offline admission. Assistance and later corrected drafts are separate successor results, never backdated first-attempt passes. This trial is source-only: no native OpenModelica, historical C1 repairs, frozen-reference changes or production deployment.

After posting, the owner should notify Chat A with **"author done"**.