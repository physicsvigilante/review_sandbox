# SIM_HEAT — H2-00 integration PR #12 central review status

**Status: `awaiting-targeted-re-review`** — Chat B review 01 is committed (`changes-requested`); Chat A's correction and new exact-head CI are complete. **Chat B review 02 has NOT yet occurred.** No source merge is authorized.

| Item | Exact identity/status |
| --- | --- |
| Project | `sim_heat` |
| Source repository | https://github.com/physicsvigilante/sim_heat |
| Source PR | https://github.com/physicsvigilante/sim_heat/pull/12 — **draft, unmerged** |
| Source base SHA | `49a2cc42462b47026e86313bfeff39a9b17081cd` |
| Pinned source HEAD SHA | `adb1b664d1a026f2f6cf017c11eda057d791595e` (original review 01 head: `f2bb5369425a250cef78b74baaf486925f8fa6bd`) |
| Pinned tree SHA | `618a3f774ff2d304295803f25eda79e78adb1492` |
| Risk class | **R2**, first mainline integration of simulation/verification engine code |
| Final-head CI | https://github.com/physicsvigilante/sim_heat/actions/runs/43728497707 — **success**, original 43723198188 pass and intermediate 43728041002 failure preserved |
| CI evidence | https://github.com/physicsvigilante/sim_heat/actions/runs/43728497707/artifacts/14166838398 |
| CI ZIP SHA-256 | `51f0ea680b64b9b11b1562654878d908ef40639677c620baabc61c323d7d4e77` |
| Developer checks | 151 H1 tests + 4 analytical tests + bridge admission/reference-preparation smoke passed |
| Integration native runs | **0**, by design; prior separately pinned native actions are cited in REQUEST.md |
| Current review cycle | **01 — changes-requested**; Chat A response recorded; **02 — awaiting targeted re-review** |
| Report path reserved | `reviews/review-02-chat-b.md`, **Chat B only**, new immutable report; review 01 retained |
| Developer response | [response-01-chat-a.md](responses/response-01-chat-a.md) published, F-01 confirmed and corrected; F-02 clarified; F-03 remains open |
| Owner merge approval | **Not granted** |
| Source merge / post-merge CI | **Not performed / not applicable** |

## Handoff

- [REQUEST.md](REQUEST.md) — R2 scope, exact source/CI identities and adversarial acceptance questions.
- [REVIEWER-PROMPT-01.md](REVIEWER-PROMPT-01.md) — immutable original prompt.
- [review-01-chat-b.md](reviews/review-01-chat-b.md) — committed first independent review, `changes-requested`.
- [response-01-chat-a.md](responses/response-01-chat-a.md) — developer defect disposition and CI evidence.
- [FOLLOW-UP-02.md](FOLLOW-UP-02.md) and [REVIEWER-PROMPT-02.md](REVIEWER-PROMPT-02.md) — targeted Chat B re-review at the new SHA.
- [REVIEW-TEMPLATE.md](../../../REVIEW-TEMPLATE.md) — required reviewer-authored report format.

Chat A must not create or prewrite Chat B's next report. Chat B may use the same underlying model family but has a separate conversation context, not independently certified subject-matter expertise. It must distinguish tests it independently ran from earlier CI.

**Owner handoff:** paste the reviewer prompt into another ChatGPT conversation. On the owner's **"Review complete"** message in Chat A, retrieve the new report directly from this central GitHub path, check its pinned head and author attribution, reproduce blockers and fix with regressions. Request focused re-review only for changed scope. If the source head changes, this review is stale for the new head until new CI and scoped review.

Merging requires owner permission after review and blocker disposition. Only afterward append the exact merge SHA and post-merge CI results here; do not overwrite historical reports.
## Chronology and correction accounting

- **2026-11-15 — original request:** R2 first-head CI 43723198188 passed 149 H1 + 4 arithmetic tests at `f2bb5369425a250cef78b74baaf486925f8fa6bd`. Original REQUEST.md / reviewer prompt 01 and GitHub artifact remain immutable.
- **Review 01:** Chat B's independent-in-context report [review-01-chat-b.md](reviews/review-01-chat-b.md) found **F-01 major**: unique indexed MAT rows were misleadingly marked independent measurements; F-02 documentation and F-03 open qualification. Outcome `changes-requested`; no physical-equation or numerical-checker defect shown.
- **First correction source:** `8b172f3efa4776229fb7a5251648cd4ad39d54f1`; CI 43728041002 **FAILED** seven historical-plan fixture tests because old SHA-pinned plans correctly refused new MATv4 bytes. Those historical plans were **not rewritten**.
- **Second correction source:** `adb1b664d1a026f2f6cf017c11eda057d791595e`; current CI 43728497707 **PASS**, 151 H1 + 4 arithmetic tests, and bridge admission + prepared reference. v2 channel uniqueness regression and strict historical-plan refusal regressions passed. The new source diff touches exactly six files; no native execution or merge.
- **Next:** Chat B authors **new** [review-02-chat-b.md](reviews/review-02-chat-b.md) once completed, focused on the corrected v2 metadata and historical-plan test path. This link is a reserved future path, not an existing/approved report. Owner says “Review complete” afterward; Chat A retrieves the report and updates this status with a new attributable outcome. **Merging still requires separate owner approval.**
