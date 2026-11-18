# M37a PR #89 — Targeted independent F4 re-review PROMPT #03

You are an **independent scientific/evidence reviewer**. You may be the **same Chat B who found F4 in review #02**; no fresh-from-zero review is required for unchanged solver physics. This assignment is a **targeted scientific-export integrity re-review**, not a new broad feature review.

**READ COMPLETE EXACT-SOURCE REQUEST #03 FIRST:**
https://github.com/physicsvigilante/review_sandbox/blob/main/projects/conductor_sim/pr-89/REQUEST-03.md

**Production PR:** https://github.com/physicsvigilante/conductor_sim/pull/89 — DRAFT, UNMERGED at prompt publication.
**EXACT corrected candidate HEAD:** `630f6d320a1b4cb00bf7bb0780cd3deca4ec0f7e`
**Actual native Git TREE:** `796f319edf5829455e842d9bad63b770d17ff9fa`

Prior independently reviewed #02 source `adfe9098...` had **CHANGES REQUESTED** for 3 genuinely accepted false M16a exported JSON claims: huge falsified maximum energy drift, negative `guard_m`, and impossible extra surface-guard event on a completed-duration run. [Read review #02](https://github.com/physicsvigilante/review_sandbox/blob/review/conductor-pr89-r2-20261118/projects/conductor_sim/pr-89/reviews/review-02-chat-b.md). Its first 99-case independently executed F1–F3/physics suite otherwise passed. Preserve its FAILED [real workflow](https://github.com/physicsvigilante/review_sandbox/actions/runs/44315235077), do not relabel PASS.

This corrected HEAD differs from that reviewed source only in **`tools/m37a_ground_wire_reference.py`, `tests/test_m37a_grounded_wire_current.py` and `docs/m37a.md`**. Confirm exact SHA, Git tree, changed file list and original production code unchanged. If different, STOP as STALE. A new full blind physics review and independent PDF redownload are unnecessary if untouched source bytes and prior verified provenance are explicitly confirmed.

**Required real execution:** use the original reviewer-owned test script as a starting point (not the developer's oracle); pin the new HEAD/TREE and re-run all original F4 failures against freshly generated JSON. Add novel self-authored hostile cases covering negative/Boolean/NaN guard, forged max drift, event kind, timing, non-axial/displacement mismatch, terminal guard position/time, and false duration claims. Test **genuine duration, turning and guarded M16a** JSON still accepted, and original F1–F3 attacks remain rejected. Source checker must still import NO production physics, accurately distinguish internal JSON consistency from the native re-integration requirement. Refusals must be from intended physical assertions, not harness/setup errors. Use `set -euo pipefail`; keep first-run evidence even if it fails.

**Production CI must finish:** all exact HEAD branch+PR Python 3.10/3.12, new focused M37a SI check, real FEMM5 and historical Chromium/source workflows; no green claim while queued, failed or cancelled. Focused author run at this SHA passed **120 tests each on Python 3.10 and 3.12**. This is developer-controlled evidence, not your independent verdict.

**JEE source:** prior independently inspected original workbook `02_conductors_half_size.pdf` physical p8 Q21, p17 answer key, positive charge approaching grounded sphere at **constant prescribed speed**, answer options **(1),(3)**. No need for another visual reinspection if source PDF bytes and unchanged authoring scope verified. Do not claim the free M16a trajectory is literally the original prescribed-speed question.

Publish `projects/conductor_sim/pr-89/reviews/review-03-chat-b.md` on main or a separate review PR: exact SHA/TREE, PASS/CHANGES REQUESTED/INSUFFICIENT EVIDENCE, actual first reviewer run, new hostile matrix, live exact-head CI and bounded limitations. Preserve historical failed reports untouched.

**No production edits or merge.** An independent scoped PASS triggers a separate explicit owner decision. Chat A then safeguards the merge with `expected_head_sha`, compares the actual merged Git TREE, and requires all actual postmerge main CI success.
