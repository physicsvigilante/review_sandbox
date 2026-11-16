# EM Fields PR #20 — R2 review and correction status

**CHAT B R2 CHANGES REQUESTED; CORRECTION SOURCE HEAD IN QUALIFICATION — DO NOT MERGE** (2026-11-16, Asia/Kolkata). The owner approved implementation only; no owner merge authorization or scoped R2 pass is implied.

## Preserved first review

- [Original R2 request](REQUEST.md) and [reviewer prompt 01](REVIEWER-PROMPT-01.md) pin original source head 4b51a833c0ed5ef189becf5881064d1b516df21b, tree 8e8999b40949d1128050cf66c0440fb07bb08670.
- Independently authored [Chat B review 01](reviews/review-01-chat-b.md) reports **CHANGES REQUESTED**, not pass. Original Git blob 3ecb837b03bd6c1644f289a50fa5b33794212fb5 must remain untouched. Its tests reproduced F-01 **blocker** (NPZ values selected by a different request index/time), F-02 **major** (unselected native sample/field magnitude contradictions), and F-03 **minor** (nonboolean check receipt passed=0).
- These are evidence-consistency failures, not demonstrated errors in unchanged source fields, physical integrator or vetted E1/G1/T1 physical values. Separate-context LLM review is not independent human physical certification. Do not retroactively describe the old source as passed.

## Correction candidate and pending gates

- [Draft source PR #20](https://github.com/physicsvigilante/emfeeld/pull/20) remains **open, draft, unmerged**. New correction head **145b68fcab75201a6a31876e91c075c3f00b0fc8**, on the same isolated implementation branch, with narrow production and test changes only.
- Author reproduced the original F-01 complete-at-0s failure against copied exact E1 evidence; first new focused warnings-as-errors tests were **11 failing / 1 passing** against old source, demonstrating missing guards. After correction, **45 focused tests passed**; one interrupted local full headless replay is not claimed as passed.
- Correction verifies **every** recorded successful native trajectory sample against the authored index/exact-time/nearest-time selector, saved NPZ time grid/row and offset before output; verifies every native field vector/magnitude; and requires strict boolean true in check receipts. This applies to unselected observations. Original archived Linux/Windows E1/G1/T1 comparison results were read-only inspected under the correction and retain their prior statuses.
- New exact-head [Linux+Windows clean-install release #43837372118](https://github.com/physicsvigilante/emfeeld/actions/runs/43837372118), [separate real-PyVista #43837372318](https://github.com/physicsvigilante/emfeeld/actions/runs/43837372318), and [source snapshot #43837372230](https://github.com/physicsvigilante/emfeeld/actions/runs/43837372230) require final result checks. **No unfinished workflow is counted as passed.** A downloaded hosted source snapshot was independently exercised with 45 focused tests.
- Qualified baseline main remains PR #17 merge 1b7d5c652bb635723746b3c6ce77baee536b997e. Design-only PR #19 remains separate.

## Next gate

After fresh exact-head CI passes, audit new Linux/Windows saved artifacts and submit **NEW** targeted FOLLOW-UP-02.md and REVIEWER-PROMPT-02.md pinning the corrected head/tree, new tests and original F-01–F-03 findings. **Only Chat B** creates reviews/review-02-chat-b.md (or separate review-only PR). Any further source changes require new source SHA, qualification and proportionate review. **Merge requires later distinct owner approval**, followed by fresh merged-main CI and append-only release report. No user Conda installation, saved physical model, physical laws, tolerances or teaching evaluation were changed.
