# Ready-to-paste Chat B prompt — SIM_HEAT PR73 targeted R2 review-01

You are independent reviewer Chat B. Review only the bounded PR72 N-01/N-02 correction, not unchanged physics. **FIRST READ** https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-73/REQUEST.md and the original independent https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-72/reviews/review-01-chat-b.md.

**Draft PR73:** https://github.com/physicsvigilante/sim_heat/pull/73
**Exact HEAD:** `ba625afe3223d4c0fda5d23b88445d08d64771c6`; **base PR72:** `617cfee3b91d7acf567ecad779f133b7429a8611`. Four changed paths: tools/published_diagnostic_bridge.py, tests/test_authoring_workbench.py, tests/browser_authoring_workbench.py, .github/workflows/teacher-archive-handoff-ci.yml.

Verify the new strict **runtime byte equality** of generated vs published ORIGINAL archived compare index; challenge a JSON reserialization with identical parsed content. Confirm negative test *actually intercepts valid in-root index bytes*, not just a forbidden external path; verify original D2→D2_K2 still opens and unrelated or corrupted evidence remains source-only. Verify browser's NEXT original saved instant `468.75 s` and original `cold.T` **296.468 / 299.052 K** displays, initial signed flows +12 / +24 W, and unchanged diagnostic-only flags. No new solver or OMC runs, no reference promotion.

**Hosted PR CI** https://github.com/physicsvigilante/sim_heat/actions/runs/44680586259 **SUCCESS**, 331 collected, 330 pass/one existing optional skip; real Chromium and six offline original archive replays. Artifact 14603669026 has **GitHub-reported** digest only; reviewer must attribute personally run evidence separately. No OpenModelica installation/version/query/build/launch permitted.

Write exactly ONE original independent report directly to `physicsvigilante/review_sandbox/projects/sim_heat/pr-73/reviews/review-01-chat-b.md` with verdict SCOPED PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE, pinned to exact HEAD. Keep historical reports and all original inputs unchanged; PRs remain DRAFT/UNMERGED, seven old static reference failures, eight native blockers and unsealed private scorer are not fixed. Do not merge, deploy or execute native builds.
