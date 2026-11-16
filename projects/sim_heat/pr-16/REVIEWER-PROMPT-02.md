# SIM_HEAT PR #16 — Chat B targeted R2 Review 02 prompt

Continue as independent **Chat B** for **SIM_HEAT PR #16**. Read the [targeted follow-up](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-16/FOLLOW-UP-02.md), [original Review 01](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-16/reviews/review-01-chat-b.md), [Chat A's response](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-16/responses/response-01-chat-a.md), the central protocol and review template.

Review only the **three-file correction diff** at exact source commit **`099bd4330a56e129f35493b42231830209a9e964`** (tree `85a62320977092f47cf5d100bf98c4b2bf955599`), not the floating branch. [Correction compare](https://github.com/physicsvigilante/sim_heat/compare/e76df818fcbb9b6826b03db776b6140dd40c4be4...099bd4330a56e129f35493b42231830209a9e964). Successful exact-head [CI 43834101967](https://github.com/physicsvigilante/sim_heat/actions/runs/43834101967), artifact 14210406363, ZIP SHA-256 `015ee3b1874996df29e70f2ec2aefa33902704b271fe60e3d11b183c9159a92d`.

Reassess original F-01 (re-hashed ZIPs with false check `passed`, fabricated request values, wrong reference seals/digests, incomplete manifest), F-02 (missing native members must refuse with typed error), and F-03 (external expected run/commit pins and explicitly limited authentication). **Independently replay the archived S1 native ZIP and repacked, fully re-hashed negative examples where possible.** Separate tests personally executed from author CI. Check the original three transient case bundles/physics remain unchanged and no new native simulation is claimed; native evidence stays `diagnostic_only`, `nativeQualified=false`.

Write a **new independent report**, following REVIEW-TEMPLATE.md, directly to:
`physicsvigilante/review_sandbox/projects/sim_heat/pr-16/reviews/review-02-chat-b.md`.

Do not overwrite Review 01, edit source, merge PR #16, or claim an unperformed test passed. Return the committed report URL. A scoped PASS is **not** owner merge approval.
