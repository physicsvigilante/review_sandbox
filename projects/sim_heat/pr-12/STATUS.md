# SIM_HEAT — H2-00 integration PR #12 central review status

**Status: `awaiting-review`** — independent separate-chat Chat B review has **not** been received or performed. This status is review coordination only, never authorization to merge.

| Item | Exact identity/status |
| --- | --- |
| Project | `sim_heat` |
| Source repository | https://github.com/physicsvigilante/sim_heat |
| Source PR | https://github.com/physicsvigilante/sim_heat/pull/12 — **draft, unmerged** |
| Source base SHA | `49a2cc42462b47026e86313bfeff39a9b17081cd` |
| Pinned source HEAD SHA | `f2bb5369425a250cef78b74baaf486925f8fa6bd` |
| Pinned tree SHA | `92fd29ee3b55ef6e49e438dd326ea159b7cdb446` |
| Risk class | **R2**, first mainline integration of simulation/verification engine code |
| Final-head CI | https://github.com/physicsvigilante/sim_heat/actions/runs/43723198188 — **success** |
| CI evidence | https://github.com/physicsvigilante/sim_heat/actions/runs/43723198188/artifacts/14165546204 |
| CI ZIP SHA-256 | `e5214690068af2bc596daa6da75374610970396aaeb7dfb661951e2cacf2bdb4` |
| Developer checks | 149 H1 tests + 4 independent-expression arithmetic tests + bridge admission/reference-preparation smoke passed |
| Integration native runs | **0**, by design; prior separately pinned native actions are cited in REQUEST.md |
| Current review cycle | **01 — request published; report not yet created** |
| Report path reserved | `reviews/review-01-chat-b.md`, **Chat B only** |
| Developer response | Not yet applicable; future file `responses/response-01-chat-a.md` only after attributed review |
| Owner merge approval | **Not granted** |
| Source merge / post-merge CI | **Not performed / not applicable** |

## Handoff

- [REQUEST.md](REQUEST.md) — R2 scope, exact source/CI identities and adversarial acceptance questions.
- [REVIEWER-PROMPT-01.md](REVIEWER-PROMPT-01.md) — ready-to-paste prompt for the separate ChatGPT reviewer.
- [REVIEW-TEMPLATE.md](../../../REVIEW-TEMPLATE.md) — required reviewer-authored report format.

Chat A must not create or prewrite Chat B's report. Chat B may use the same underlying model family but has a separate conversation context, not independently certified subject-matter expertise. It must distinguish tests it independently ran from earlier CI.

**Owner handoff:** paste the reviewer prompt into another ChatGPT conversation. On the owner's **"Review complete"** message in Chat A, retrieve the new report directly from this central GitHub path, check its pinned head and author attribution, reproduce blockers and fix with regressions. Request focused re-review only for changed scope. If the source head changes, this review is stale for the new head until new CI and scoped review.

Merging requires owner permission after review and blocker disposition. Only afterward append the exact merge SHA and post-merge CI results here; do not overwrite historical reports.