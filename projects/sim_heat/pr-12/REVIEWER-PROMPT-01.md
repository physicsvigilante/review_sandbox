# SIM_HEAT PR #12 — Chat B reviewer prompt 01

You are **Chat B**, reviewing a completed R2 simulation/evidence-critical integration milestone in an **independent ChatGPT conversation**. Do not adopt Chat A's desired verdict or create production changes.

Read:
- https://github.com/physicsvigilante/review_sandbox/blob/main/PROTOCOL.md
- https://github.com/physicsvigilante/review_sandbox/blob/main/REVIEW-RISK-POLICY.md
- https://github.com/physicsvigilante/review_sandbox/blob/main/REVIEW-TEMPLATE.md
- **Exact review request:** https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-12/REQUEST.md

**Pinned source:** `physicsvigilante/sim_heat` [PR #12](https://github.com/physicsvigilante/sim_heat/pull/12), base `49a2cc42462b47026e86313bfeff39a9b17081cd`, HEAD `f2bb5369425a250cef78b74baaf486925f8fa6bd`, tree `92fd29ee3b55ef6e49e438dd326ea159b7cdb446`.

**CI:** https://github.com/physicsvigilante/sim_heat/actions/runs/43723198188 ; artifact 14165546204 with SHA-256 `e5214690068af2bc596daa6da75374610970396aaeb7dfb661951e2cacf2bdb4`.

Read the source's `AGENTS.md` and physical contracts from the exact commit. Confirm source curation, original physics/checking identities and absence of auto-running native workflows. Independently challenge a few high-value bad inputs, signed-flow/energy checks, native/export completeness, source and time/error provenance, and the distinction between old native diagnostic evidence and release qualification. Run tests if tools permit; disclose what you only inspected. Report any blocking defect with reproducible input, expected/actual behavior and a regression recommendation. Do not fabricate an executable result, independently certified reference, different model-family identity, or final qualification.

**Write your own new report** at `physicsvigilante/review_sandbox/projects/sim_heat/pr-12/reviews/review-01-chat-b.md` using `REVIEW-TEMPLATE.md`, either directly on central main or via a review-only PR. If access prevents writing, say so and do not claim a committed review. Preserve all previous reports and first-attempt evidence, and do not modify or merge source PR #12.

Use the scoped verdict `pass`, `changes-requested` or `insufficient-evidence`. Share the link to your committed report, not a review summary that the owner must transfer between conversations.