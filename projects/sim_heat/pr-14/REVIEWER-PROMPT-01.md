# H2-02 generic thermal explorer — Chat B reviewer prompt 01

You are **Chat B** in a separate ChatGPT conversation. Independently review SIM_HEAT's **R2 generic viewer evidence contract**, not Chat A's desired verdict.

Read:
- Central [PROTOCOL.md](https://github.com/physicsvigilante/review_sandbox/blob/main/PROTOCOL.md), [REVIEW-RISK-POLICY.md](https://github.com/physicsvigilante/review_sandbox/blob/main/REVIEW-RISK-POLICY.md), and [REVIEW-TEMPLATE.md](https://github.com/physicsvigilante/review_sandbox/blob/main/REVIEW-TEMPLATE.md).
- **Exact review request:** https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-14/REQUEST.md

Source: [SIM_HEAT draft PR #14](https://github.com/physicsvigilante/sim_heat/pull/14), **HEAD `281c5a45b536b698ea2b6896710e3cc49e20698b`**, tree `5ed4a1c0ac34a5fe5f463aafb1433abfa557c999`, base `a33a0d79da405ff4c7191b9bfb94e096b10e2a9f`. Do not review floating main/head.

**CI:** [run 43745347155](https://github.com/physicsvigilante/sim_heat/actions/runs/43745347155), PASS: 151 H1 + 4 analytical + 4 adapter + 7 Node tests and real Chromium desktop/mobile checks. Artifact 14173792995, ZIP SHA-256 `d0283eea89e5e4b4a413c767ac2560768f695876b83f4cd0216049523a0c62e8`. Original browser test failures [43744485774](https://github.com/physicsvigilante/sim_heat/actions/runs/43744485774) and [43745168791](https://github.com/physicsvigilante/sim_heat/actions/runs/43745168791) remain preserved.

Independently challenge the generic Python adapter, strict JS/CSV schema, graph owner/rod orientation and node types, real archived D1/D2/bridge preview values and model/CSV SHA pins, J/K/W sign/energy ownership, missing/stale values, async case-switch refusals and desktop/mobile browser behavior. Check that a fourth supported case changes **only data/catalog**, not renderer or H1 code. Distinguish your own test executions from inspected source CI; no invented independent native test or classroom certification. Original native data remain diagnostic-only, not independent physical measurements.

**Write your own new review file directly** at `physicsvigilante/review_sandbox/projects/sim_heat/pr-14/reviews/review-01-chat-b.md` (or a review-only PR) following REVIEW-TEMPLATE.md. Preserve failed attempts and any first reviewer test errors. Do not alter/merge source PR #14 or overwrite historical records. Give a scoped `pass`, `changes-requested` or `insufficient-evidence`, with reproducible source-backed findings and any independent execution limitations. Return a link to the committed report.