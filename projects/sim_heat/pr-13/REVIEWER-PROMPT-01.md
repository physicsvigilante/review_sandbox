# SIM_HEAT H2-01 — Chat B reviewer prompt 01

You are Chat B in a **separate ChatGPT conversation**. Conduct a **focused R1 independent-in-context review** of SIM_HEAT's read-only thermal bridge viewer, **not** a new general R2 physics audit. Read:
- https://github.com/physicsvigilante/review_sandbox/blob/main/PROTOCOL.md
- https://github.com/physicsvigilante/review_sandbox/blob/main/REVIEW-RISK-POLICY.md
- https://github.com/physicsvigilante/review_sandbox/blob/main/REVIEW-TEMPLATE.md
- **Exact request:** https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-13/REQUEST.md

Review source [PR #13](https://github.com/physicsvigilante/sim_heat/pull/13) at **exact HEAD `e8449989ba55a972976ebba7e9708bc4e2351a18`**, base `ecebc38dd3f6eaffd297bd3df97a0883e591c6ac`, tree `c342ace7233dd112fa494be91785f79f23debeca`. Read its pinned `AGENTS.md`, H2-01 contract and eight-file diff. Check the native bridge source/preview, all signed rod arrows and temperature/energy/power units, the 1720/1730-second reversal, honest diagnostic-only labels, fail-closed file hashes, and no physics or verifier changes. Inspect screenshots or actually drive desktop/mobile and import refusals if tools permit, distinguishing *what you ran* from inspected author CI.

Final source CI https://github.com/physicsvigilante/sim_heat/actions/runs/43736122931 PASSED: 151 H1 tests, 4 analytical tests, 7 viewer tests and real Chromium smoke; screenshot/log artifact 14169479149 (SHA-256 `f5100b7f9ab2ddb2e8634eda1b11d4a3f9b1d31c67031aa59c0ebf35c91bf640`). The first failed viewer test run 43735810229 is preserved and must not be retroactively rewritten. Historic native data comes from run 43699424883; do not claim any new native launch.

**Write your own new report** directly to `physicsvigilante/review_sandbox/projects/sim_heat/pr-13/reviews/review-01-chat-b.md`, using REVIEW-TEMPLATE.md; do not overwrite prior reports or edit/merge PR #13. Give a scoped `pass`, `changes-requested` or `insufficient-evidence` with findings and limitations and return a link to the committed report. Independent conversation context is not necessarily an independent model or human expert.