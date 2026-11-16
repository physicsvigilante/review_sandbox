# conductor_sim PR #63 — M27b release status

**MERGED to `main` after independent R2 PASS and explicit owner approval.** Source pull request: [#63](https://github.com/physicsvigilante/conductor_sim/pull/63).

- **Exact R2-reviewed source head:** `08ad6ea0a30d440f70f83f89e865a87fe9a0f96f`.
- **Reviewed source Git tree:** `2affa61b9efd44f5949f5c6e8136f8ad179e893b`.
- **Independent report:** [Chat B review-01](reviews/review-01-chat-b.md), dated 2026-11-16, **PASS, scoped; no blocking findings**. Reviewer authored new native physical configurations and independent Coulomb/DOP853 reference, rotation, rejection and source-wire guard checks and rehashed both CI artifacts. The report did **not** authorize a merge.
- **Release decision:** Owner subsequently explicitly approved merging PR #63; draft PR marked ready, then merged using GitHub's head-SHA precondition equal to the reviewed source head.
- **Merge commit:** [`5bbc091f61202f991f2e72e1834071f958fcc9ec`](https://github.com/physicsvigilante/conductor_sim/commit/5bbc091f61202f991f2e72e1834071f958fcc9ec); GitHub reports merged 2026-11-16 08:15:03 UTC. GitHub comparison of merge SHA against `main` returned **identical** (ahead=0, behind=0).
- **Premerge tests:** All 17 PR-triggered workflows returned by the GitHub first-page run endpoint were successful on the exact reviewed source HEAD. Prior implementer summary reports 18/18 applicable checks; do not conflate this with an independently enumerated 18th workflow. Python 3.10 and 3.12 each passed 1,807 tests; real FEMM passed 97; focused motion passed 160; Chromium real event/driven viewer passed.
- **Postmerge CI:** All **17/17** push-triggered `main` workflows for exact merge SHA completed **SUCCESS**, including Python 3.10/3.12, real FEMM and full Chromium visualization. No post-merge failures.
- **Nonblocking follow-up F-01:** `tools/check_m27b_browser.py` browser CI summary incorrectly groups the workbook's **source-given +10 μC probe charge** with teacher-hypothetical mass/launch/duration. Production simulation and user-facing provenance already use correct charge. Defer CI-summary wording and source-anchored regression to a separate postmerge change, preserving the exact reviewed M27b source and original evidence.
- **Scope:** Actual planar motion only in separately certified meridian/equatorial ring symmetry planes, fixed prescribed sources, guard-bound numerical chords. No generic unrestricted 3D, contact, induction, conductor back-reaction or symbolic Q41 solution.

- **Nonblocking F-01 follow-up PR:** [conductor_sim draft PR #64](https://github.com/physicsvigilante/conductor_sim/pull/64) fixes only the browser acceptance report's probe-charge provenance and adds a source-anchored assertion. Source head `edc755ae2d95a774cb5d85f0b5ffc036c70b99d6`; based on verified M27b merge. This follow-up is **draft and unmerged** pending exact-head CI and separately requested owner approval.

**M27b is merged and postmerge-verified; any follow-up changes require separate scoped work and verification.**
