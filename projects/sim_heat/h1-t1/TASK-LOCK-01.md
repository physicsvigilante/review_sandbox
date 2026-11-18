# H1-T1 selector Stage 1 — immutable original task-set capture

**State:** `TASK_SET_V1_CAPTURED; READY_FOR_SEPARATE_AUTHOR_FIRST_ATTEMPT; KEY_REVEAL_FORBIDDEN_UNTIL_AUTHOR_CAPTURE`.

**This is the first selector task-set submission**, not an H1 admission result, an independent physics certification, a source-model submission or a native simulation.

| Captured item | Exact original |
|---|---|
| Source intake issue | [SIM_HEAT Issue #58](https://github.com/physicsvigilante/sim_heat/issues/58) |
| **Original selector issue comment** | [Comment 6981681502](https://github.com/physicsvigilante/sim_heat/issues/58#issuecomment-6981681502) |
| GitHub comment ID | `6981681502` |
| GitHub comment `created_at` UTC | **`2026-11-18T14:36:12Z`** |
| GitHub comment `updated_at` UTC | `2026-11-18T14:36:12Z` (same as creation at capture) |
| GitHub posting account | `physicsvigilante`; author self-identifies as separate-context GPT-6 task selector in the comment |
| Selector-stated preparation time UTC | `2026-11-18T14:34:31Z` (self-reported, **not** GitHub's post timestamp) |
| **Original complete comment-body SHA-256** | **`8f45ad3d4a763952e25d60658ae4d8eeae37fd266bd372b3cd80fb19b81fa2a2`** |
| Original comment UTF-8 bytes | **10,233** |
| Original comment JavaScript text length | 10,188 UTF-16 code units |
| **Exact original body snapshot** | [TASK_SET_V1_COMMENT_6981681502.raw.md](intake/TASK_SET_V1_COMMENT_6981681502.raw.md) |
| Snapshot Git blob SHA-1 | `33b373a4448923f1b32f9998e607828a5ef3a231` |
| Snapshot creation commit | `3ea30eb390660cf541fca95e95b668ac17ee02fc` |
| Selector's **private evaluator key salted SHA-256 commitment** | **`49cc3397ae5bbbabff823e674491d9d44d8341bbd8b9556694c86f5ffffb6319`** (digest **only**; key and salt not received) |
| Fixed H1 evaluator implementation | [SIM_HEAT `f52613c39c539b2d4543a9838e5658d526fca10e`](https://github.com/physicsvigilante/sim_heat/commit/f52613c39c539b2d4543a9838e5658d526fca10e), tree `0c44961b473d23737b0c9f3b3f2cd3db65b9f264` |
| Exact public author contract Git blob | `27dd142034c28911370ddd2bab328f14dcfb6f71` |

## Capture integrity

Chat A retrieved the original comment directly from the GitHub issue-comment API, checked the title, three distinct task headings T1-S/T1-T/T1-X, fixed implementation identity and presence of the 64-character hidden-key SHA-256 commitment. Original GitHub comment reported `created_at == updated_at`. Chat A computed the UTF-8 SHA-256 of the **complete original comment body** using a standard SHA-256 implementation with known test vectors verified before using it. It wrote the body itself **with no header, footer, newline adjustment, editorial summary or content correction** to the `.raw.md` snapshot. It fetched the committed central file and compared its full returned content equal to the original GitHub API comment body, with Git blob above. No key/salt was revealed and no evaluator source model was constructed.

**Important:** GitHub comments are editable; the original comment URL is an attribution pointer, not a cryptographic immutability guarantee. The committed raw file and its SHA-256 are the sealed snapshot. If the original comment changes subsequently, retain this version unchanged and record a separate amended version; do not silently replace Stage 1. Original comment and original repository evidence were not modified.

## What the selector publicly specified (not evaluated yet)

- **T1-S:** `Three-thermostat guarded heat spreader`, original illustrative **steady** graph with three maintained-temperature boundaries, three ownerless junctions, eight rods and six public requests.
- **T1-T:** `Two-feed three-block thermal lattice`, original illustrative **transient** graph with two maintained boundaries, three finite bodies, two ownerless junctions, ten rods, eight requests and a 0–2400 s prescribed time window.
- **T1-X:** `Vacuum-chamber glowing bead`, a **thermal radiation** problem with missing required physics in the H1 component library; expected correct boundary behavior is transparent refusal, not a surrogate numerical calculation.

These are selector-authored illustrative educational tasks, **not quotations from authenticated JEE textbooks**, not Modelica source files, not solved heat-transfer values, and not independently certified physically/numerically valid tasks. Selector disclosed previous general SIM_HEAT H1 planning/status exposure; independence is limited to a separate conversation and task/model role division, **not independent human expert judgment or unseen underlying model training**.

## Stage 2 boundary: separate author only

Stage 1 original statement is **locked**. Chat A **has not** run H1 admission, source-preview, numerical verification or native execution on these tasks; no Modelica or study.json submission is present at seal. The original selector comment is the sole issue comment at task-lock verification; there is **no `FIRST_ATTEMPT_V1` comment yet**.

Proceed to a **different, fresh author conversation (Chat C)** with **ONLY** the [public author packet](AUTHOR-PACKET.md) and the exact [selector task comment](https://github.com/physicsvigilante/sim_heat/issues/58#issuecomment-6981681502). Do **not** provide evaluator key, selector protocol, preexisting example models, Chat A analyses or project implementation. The author submits unedited supported-task model/study/notes and unsupported-task refusal **in one original first-attempt issue comment**, then stops; only **after** Chat A seals that full raw comment may the selector disclose the private evaluator key/salt, to verify its earlier commitment before source-fidelity scoring.

No new GitHub source PR, engine/core change, OpenModelica query/install/build/launch, C1 historical integration, frozen reference regeneration, archive mutation, qualified native readings, deployment or source-to-result success claim is authorized by this capture.

**Review budget:** This was R0 evidence capture, no independent code review needed. Plan one consolidated independent evidence review after three first attempts have been captured and evaluated, with R2 reserved for any actual change in physics, interpretation, numerical or qualification semantics.
