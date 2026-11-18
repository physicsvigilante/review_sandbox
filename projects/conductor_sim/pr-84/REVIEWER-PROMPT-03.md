# M36a — Independent targeted reviewer prompt #03 (exact corrected source)

You are **Chat B**, a fresh separate-context GPT-6 reviewer of **conductor_sim PR #84**. Your previous-context peer's [review #01](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/conductor_sim/pr-84/reviews/review-01-chat-b.md) returned **CHANGES REQUESTED** and is retained. You must **independently** check the corrected source and respond to the specific blockers, not copy the implementer's claims.

**READ ALL OF:** [full source-pinned correction request #03](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/conductor_sim/pr-84/REQUEST-03.md), [status chronology](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/conductor_sim/pr-84/STATUS.md) and the original review report.

- **Draft source PR:** https://github.com/physicsvigilante/conductor_sim/pull/84
- **Exact pinned HEAD:** `527e6cee5f96a011729d2d0a668da9b688ab03d0`
- **Exact Git TREE:** `fff1c03417c857b6cce04156427e3eeaf9919a65`
- **Reviewed predecessor:** `b6d7fccad26666100b172097b01738aedc8c9cf6` — **CHANGES REQUESTED**
- **Released base main:** `73e076cf7eaf7fefbae2b24afc1f54ff8f0b6fc6`
- **Frozen original charter-only commit:** `13eb3afde0efac049387d90a64eff44227f2acb4`

**STOP if PR HEAD/TREE changed.** This prompt is source-specific; never infer a fresh revision is reviewed from a prior old verdict.

## Required independent work

1. Verify **F-01** on actual GitHub *current-source* workflow: historical visualization's old 10-minute run #44156812874 really was CANCELLED and late browser cases SKIPPED. New `.github/workflows/visualization.yml` retains the original 60+ source/Chromium tasks and has a 25-minute timeout. Check that current-source CI runs **fully complete SUCCESS**, including the formerly skipped M15/M16/M17/M26/M27 steps. Separate green browser workflows do not compensate for a cancelled full workflow.
2. Verify **F-02** with ORIGINAL newly-authored adversarial input: change official 2021 case source to fabricated-source.pdf, Questions 9–10 to Questions 9–11, or question_ids to Q9/Q11. Candidate must fail closed. The legitimate 2021 **one-apparatus** Question 9+10 record must pass. Check all 29 historical cases unchanged.
3. Verify **F-03**: try swapping the route of **p70-three-cavities** or the other required local 3D refusals to supported, and swapping a genuine supported case to unsupported so declared 24/3/3 totals remain exactly correct. Candidate must still reject this. Do not infer a 3D local induced field from Gauss-law total induced charge.
4. Verify **F-04**: independent source PDF byte-tamper against frozen SHA256 actual content, not only equal JSON strings. Verify both original PDFs actually match historical hashes and original Git blob IDs where possible. Try modifying both metadata copies to matching false digests; fail closed.
5. Confirm **F-05** reviewer STATUS link now targets Prompt #02 and that this new Prompt #03 targets this exact head. Independently execute the changed source audit/tests (new 23 test instances) and read all Python 3.10/3.12 + real FEMM + Chromium CI. **Do not issue PASS if the current-head CI is unfinished or cancelled**, even if some workflow jobs are green.

Compare the original first-source failed audit test and second-source cancelled visualization CI without rewriting evidence. The scope remains **provisional source-anchored planning**: 24 suggested qualified routes, 3 partial, 3 unsupported and **zero new original JEE problem native replays / verified physical simulations / viewer inspections** in this milestone. This is not a JEE solver score, universal physical certification or an invitation to modify production.

## Publish distinct review #02

Publish your **original** findings to `physicsvigilante/review_sandbox` at `projects/conductor_sim/pr-84/reviews/review-02-chat-b.md`. Include exact reviewed commit and tree, reproducible hostile controls, F-01–F-05 resolutions or blockers, actual CI and evidence limits, and **PASS / CHANGES-REQUESTED / INSUFFICIENT-EVIDENCE** for the *bounded correction*. If tools cannot execute your probes, state this limitation; do not fabricate a PASS. Reviewer does not edit source, mark PR ready, merge, or authorize release.

After a scoped no-blocker PASS and full current-head CI, Chat A still needs **separate owner approval** for exact-head merge and must verify full postmerge main tree and workflows. The real source-specific JEE-30 replay evaluation is an entirely separate next milestone.
