# Chat B — SIM_HEAT PR56 focused independent CI applicability review

Source: [draft PR56](https://github.com/physicsvigilante/sim_heat/pull/56), `physicsvigilante/sim_heat`.
**Exact candidate HEAD:** `21eac064f98d76f12a31f03daf3bad3470cfbf96`
**Exact Git tree:** `0b789438b4aa1d0ecf6cbc6d38030eb540b97d48`
**Base main:** `0278b79b4da1c3196edca7903189713e0482f3f6`; tree `c73f86e58be8b9eb55756432aae064f00719487f`.
**Hosted PR CI merge-ref:** `1818ed1c4c6deaf586dfe14bc71ba74918dddba3`, tree **identical** to candidate tree.

Read full central [REQUEST](REQUEST.md), source `AGENTS.md`, central `PROTOCOL.md`, `REVIEW-RISK-POLICY.md` and `REVIEW-TEMPLATE.md`, plus [PR55 independent review-04](../pr-55/reviews/review-04-chat-b.md), the **scoped R2 PASS for corrected source HEAD but NOT MERGE READY** because of CI-GATE-01.

**Task:** Independently review precisely two changed paths: `.github/workflows/product-entry-ci.yml` (prospective product-only workflow trigger/guard correction) and new `tests/test_product_ci_scope.py`. The original [product-entry CI 44272592968](https://github.com/physicsvigilante/sim_heat/actions/runs/44272592968) genuinely **FAILED** when `tests/**` unexpectedly triggered it for PR55, and its product-only H1/viewer diff guard saw legitimate source-preview changes. Do not relabel it green.

Check narrowed PR path patterns include product-owned docs, renderer, product tests and workflow changes, while excluding unrelated source-preview tests/paths. Validate the guard still **refuses a product-only candidate that actually edits H1/viewer/experiments/qualification**, now comparing against the current PR base; pinned baseline self-comparison remains. Exercise negative/positive test globs and temporary Git diff behavior independently. Look for CI coverage gaps or required-check bypass; escalate risk if evidence semantics are weakened.

Inspect exact [product-entry PR CI 44278285853](https://github.com/physicsvigilante/sim_heat/actions/runs/44278285853), actual candidate job `134711947163` at synthetic merge `1818ed...`, artifact [14416131352](https://github.com/physicsvigilante/sim_heat/actions/runs/44278285853/artifacts/14416131352), 6,455,105 bytes SHA-256 `a3a2398b8e0ea96cc243680609803e3c7f27001b1af8846347e214ef56561c7e`, **39 unique CRC-valid entries**. Hosted **260 unit PASS, one optional SKIP**, all six original archive bundles BYTE_IDENTICAL, saved comparison unchanged, browser explorer/product smoke PASS. Baseline job `134711947770` PASSED. [Audit-core CI 44278285564](https://github.com/physicsvigilante/sim_heat/actions/runs/44278285564) PASSED. Do not double count overlapping tests or claim personal execution where only logs were inspected.

**Critical forward caveat:** PR55's dedicated source-preview workflow has a fixed old-main 14-added-file guard; if PR56 merges into main first, a future PR55 synthetic merge can fail that allowlist. Assess smallest future corrective path/current-base CI policy without changing PR55 now. GitHub branch protection API is inaccessible (403), so do not assert all required checks are known/waived. The PR56 correction alone does **not** authorize or complete PR55 integration.

Give SCOPED PASS, CHANGES REQUESTED, or INSUFFICIENT EVIDENCE; specify concrete counterexamples, review risk and scope. Author and commit **your own new report** to `physicsvigilante/review_sandbox/projects/sim_heat/pr-56/reviews/review-01-chat-b.md`. Do not overwrite previous reports; do not modify production source, original archives, C1, PR54 or PR55. No OpenModelica installation/query/build/launch, frozen-reference regeneration, production merge or deployment. Owner approves merges separately.
