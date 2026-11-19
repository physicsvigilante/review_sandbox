# Ready-to-paste independent Chat B — SIM_HEAT PR71 targeted R2 correction review-02

You are independent reviewer Chat B. Review **ONLY corrections to original PR71 review-01 findings F-01 (BLOCKER), F-02 (BLOCKER) and F-03 (MAJOR)** in the new teacher-facing source-only comparison interface. Do not re-review unchanged H1 thermal physics or pretend this feature computes a temperature trajectory, heat flow, native result, certified source attribution or a final answer.

**DRAFT source PR71:** https://github.com/physicsvigilante/sim_heat/pull/71
**EXACT corrected HEAD:** 9199e695f5aae410cb8d0e89f463b3b1b6e57c15
**Full Git tree:** f8ff88fd9526d32fc713cbcc0ce346f312f25860
**Original Chat B review-01 CHANGES REQUESTED HEAD:** 85ac4ce2ec7c8c7be5ab85bacf5a1b5ed7b76114
**Reviewed-in-scope, still DRAFT PR70 base:** c2bd9ce63a6d725fdcd63d2d5d7c5416c7843739
**Synthetic PR checkout:** 64669bc058de79306003eb431074c8b594b20099 (identical whole source tree with parents [PR70 base, corrected PR71 head])

**READ THE FULL CORRECTION REQUEST FIRST:**
https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-71/CORRECTION-REQUEST-02.md

Read the original [independent review-01](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-71/reviews/review-01-chat-b.md) and [Chat A response-01](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-71/responses/response-01-chat-a.md). Compare only FIVE original-reviewed-to-current source files: viewer/source_preview/app.mjs, compare_core.mjs, core.test.mjs, tests/browser_authoring_workbench.py and docs/ADMITTED_SOURCE_PREVIEW.md; everything in Modelica/H1 physics, native runner, old C1/reference, prior N1–N8 candidate stack and main remains unchanged.

**F-01 attack:** Real D2 baseline/D2_K2 scenario; view scenario A, import a legitimate separate D1 or S1 B, and confirm graph, details, source SHA identity and request labels belong to B, not A. Import bad C and require baseline restored, diff cleared, variant disabled. Delay slow A before fast B file selection and ensure last selection wins, even after slow A resolves. Challenge pending baseline replacement and startup default scenario fetch. Review new scenarioVersion together with loadVersion, not merely unit assertions.

**F-02 attack:** Import a source-only preview with SAME studySha256 as baseline but DIFFERENT modelSha256, with identical component values/ports. New code must refuse contradictory study-model identity; distinct study SHA with common model SHA remains allowed. Browser JSON import is display-schema validation ONLY, never source/model/owner external authentication.

**F-03 attack:** A valid source-only RodArea to RodCircular physical-law change (area input A removed, diameter d added) must show kind, BOTH SI input changes and original source/component attribution. Adding/removing a supported isolated body must show original m/c/T_initial and input provenance, not only a presence label. No apparatus-specific physical solver or fabricated results.

**Actual test-first and current source CI:** First tests-only [PUSH RED 44615181485](https://github.com/physicsvigilante/sim_heat/actions/runs/44615181485) and [PR RED 44615191720](https://github.com/physicsvigilante/sim_heat/actions/runs/44615191720) each failed exactly THREE new JS tests against unchanged source, proving F-02/F-03. Original reviewer independently reproduced F-01 in a Chromium DOM harness without HTTP. After application fixes, added fuller Chromium F-02/F-03 tests; test-harness [RED 44617145920](https://github.com/physicsvigilante/sim_heat/actions/runs/44617145920) was a strict CSP wait_for_function issue BEFORE assertions, resolved by locator-safe polling with no application changes.

Current exact-head [PUSH 44617692656](https://github.com/physicsvigilante/sim_heat/actions/runs/44617692656) and [PR 44617707030](https://github.com/physicsvigilante/sim_heat/actions/runs/44617707030) BOTH SUCCESS: **327 distinct tests collected, 326 pass +1 optional adapter skip** per workflow; docs parity, original source and archive-index identities, six original native diagnostic outputs replayed offline, and real hosted HTTP Chromium B->C refusal, slow/fast import race, forged study/model hash refusal and cross-kind provenance UI. Push artifact 14575976673 ZIP SHA256 b2ea7a04df90b058085621887c3db2abfc4271cac7979b862d88497141ba9bb1 was downloaded, independently SHA256/CRC verified and reconstructed to the exact source Git tree; PR ZIP digest is GitHub metadata only. Hosted CI must not be represented as personally executed Chat B controls.

**Publish ONE NEW independent reviewer report directly to:**
physicsvigilante/review_sandbox/projects/sim_heat/pr-71/reviews/review-02-chat-b.md

Verdict SCOPED PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE pinned to exact corrected HEAD. Preserve original review-01 as historical CHANGES REQUESTED. No OpenModelica installation/version query/build/launch, native/reference promotion, original C1 rewrite, source PR merge or deployment. All PR71/70/69 and earlier stack remain DRAFT/unmerged; seven original 100x physical reference refusals and eight native blockers still active. Owner may tell Chat A "review done" only after this NEW report is committed.
