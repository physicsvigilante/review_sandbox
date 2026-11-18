# H1-T1 — independent selector protocol (one sealed three-task batch)

Role: a separate-context task selector, **not** Chat A and **not** the Modelica author. This is new H1-T1 source-only evidence, **not** historical C1. Implementation source is pinned to SIM_HEAT commit f52613c39c539b2d4543a9838e5658d526fca10e, tree 0c44961b473d23737b0c9f3b3f2cd3db65b9f264.

Read only the [H1-T1 author packet](AUTHOR-PACKET.md) to understand the supported interface. Do not consult SIM_HEAT implementation code, worked cases, example models, reviews, numerical answer keys or previous solutions. Disclose any project exposure or assistance. A fresh separate chat is not proof of distinct model weights or independent human judgment.

## Choose three original, JEE-relevant tasks and lock them BEFORE authoring

**T1-S — supported steady composite conduction.** No finite bodies; at least two maintained-temperature boundaries and four or more rods with an explicit original branched/parallel/junction connection graph that does not merely rename the previously seen two-rod series S1. Provide every boundary temperature T, every rod conductivity k, length L and area A or diameter d, units and physical assumptions. Include a small selection of public observation requests (named thermal ports/rods), no solved values.

**T1-T — supported transient conduction.** Two or more finite bodies, at least one maintained boundary, several conducting rods and a nontrivial original branch/junction/loop structure different from familiar D1, D2, Bridge, Ring4 and Split3. Provide each body's m, c, T_initial; every rod's k,L,A or d; every boundary T; explicit port connectivity; units, assumptions and a few valid public observations, including energyChange or heatFlow. This may be a novel illustrative network. Do not merely rename an existing case.

**T1-X — deliberately unsupported heat-transfer question.** Make convection or thermal radiation a necessary part of an original JEE-style problem. A faithful author must refuse that physical law rather than invent a surrogate conductive rod or a numerical prediction.

Clearly say when task values are selector-invented **illustrative** teaching inputs, not attributed to a real textbook. If paraphrasing a real problem, give an accurate source/locator without copying long copyrighted passages. Do not provide model.mo, study.json, solution code, numerical results or an expected answer.

The T1-S and T1-T source tasks must be fully specified, physically sensible and within the documented H1 component/connection limits. Do not knowingly require an unsupported law in S or T. If an independent evaluator later finds the selected task invalid or duplicative, preserve it as a task-design result, **never silently replace it after the author sees it**.

## Private commitment before publication

Create in your **selector-only conversation**, before publishing the task comment, a full private evaluator key called EVALUATOR_KEY_V1. It contains all expected source facts, exact topological incidence/thermal node ownership (not numerical solutions), reasonable source assumptions, expected public requests, the unsupported reason for X, and the structural novelty/exposure comparison. Include a **nonpublic random salt at least 128 bits long**.

Compute the SHA-256 of the **exact UTF-8 bytes of that entire private key including the salt**. Publish **only that SHA-256 digest** with the task set; never post the key or salt before the first author attempt is frozen by Chat A. Keep the private key in this same selector chat. After Chat A seals the first author submission, reveal the exact key/salt and verify its hash matches the original commitment before judging. If you cannot retain a key, disclose the limitation and stop; do not falsely claim sealed independent scoring.

## Stage 1: submit ONE immutable-capture candidate comment

Post one top-level comment to the separate H1-T1 intake GitHub issue supplied with this selector prompt, headed:

H1-T1 TASK_SET_V1 — SELECTOR ONLY — PUBLIC

Include: selector/model/identity as known; previous exposure; tool/assistance disclosures; source pin; selection time; exact public task statements T1-S, T1-T, T1-X; **hidden EVALUATOR_KEY_V1 SHA-256 commitment only**; and a clear pledge to retain the hidden key until after the author's attempt is frozen.

**Stop immediately after the task comment.** Do not model, validate, run H1, edit the source repository, execute OpenModelica or start any results/answer analysis. Chat A will record the comment ID, UTC time, unedited body/hash and only then authorize Stage 2.

If direct GitHub writing is unavailable, return the complete original raw comment for **manual relay** and stop. Manual relay must be labeled; do not claim its bytes originated at the author's or selector's GitHub tool if they did not.

Use a separate author conversation for Stage 2. Selecting and authoring your own tasks does **not** count as independently selected blind authorability. One consolidated evaluation/review at the end suffices unless real safety-relevant findings require more.