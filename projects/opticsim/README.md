# Opticsim review index

Source repository: https://github.com/physicsvigilante/opticsim

- [PR #75 — detector-hit measurements](pr-75/STATUS.md): both Chat B reports imported verbatim from [Opticsim PR #77](https://github.com/physicsvigilante/opticsim/pull/77). First verdict was **insufficient-evidence**; second was a **scoped pass** after three new native adversarial tests. The implementation PR #75 and independently authored test-only PR #78 are now merged; both post-merge CI suites passed.

- [Current-main source-backed transfer + native-ray lineage feasibility, research-only PR #79](research/source-backed-transfer-v2/REPORT.md): exact frozen-request replay on Node24, 0/5 complete original tasks, and narrow native parent/child event feasibility; no production or independent Chat B review claim.


- [Research-only PR #80 — adversarial native ray-lineage boundary study](https://github.com/physicsvigilante/opticsim/pull/80): Node 24.19.0 CI 11/11 passed; 12 native scenarios, eight narrowly observed and four withheld, plus one geometry preflight refusal. Test-only research, still draft/unmerged; not a general lineage guarantee.

- [PR #81 — **independent R2 design-only PASS; superseded by merged implementation #83**](pr-81/STATUS.md): [Chat B review-01](pr-81/reviews/review-01-chat-b.md) requested changes at v1 SHA; [Chat B review-02](pr-81/reviews/review-02-chat-b.md) passed revised v2 design SHA `d814455cf823907551cbc7914d1f8b3b508efcab`. Separate [PR #83](pr-83/MERGE-REPORT.md) subsequently implemented and independently validated this narrow feature, with its own owner approval, merge and post-merge checks. PR #81 itself was not merged.

- [PR #82 — bounded native detector parentage, **R2 implementation code/evidence review pending**](pr-82/STATUS.md): separate draft implementation, with pinned-native/failure-injection/public/Chrome acceptance, [review packet](pr-82/REQUEST.md) and [Chat B prompt](pr-82/REVIEWER-PROMPT-01.md). This is a new code-review gate, not a repeat of PR #81's design-only pass. No merge authorization.

- [PR #83 — native detector-ray provenance, **MERGED, 11/11 post-merge CI PASS**](pr-83/STATUS.md): owner-approved merge `39cdfda9b8e0244e6877bfb3656bc66da557df02` has the **same Git tree** as independently reviewed source head `366037a3ed68c2110434e2132899cd0a2cbc610a`. [Chat B R2 implementation report](pr-83/reviews/review-01-chat-b.md) passed; five reviewer-authored test-only controls in unmerged PR #85 had **750/750 Node tests, 11/11 workflows**. The merged main's **745/745 Node, 5 native cases and 9 Chrome checks** passed. [Release verification record](pr-83/MERGE-REPORT.md). Reviewer-only PRs remain unmerged; no deployment.

- [PR #86 — permanently retain Chat B's five ray-parentage regressions, **MERGED, 11/11 post-merge CI passed**](pr-86/STATUS.md): owner-approved one-file (179-line) test-only merge `fa158fc78da7a35b6a02eaed58c0cdbd4b699220`; exact Git blob matches corrected reviewer PR #85. All **750/750 Node tests, five public native cases, nine real-Chrome checks** and 11 GitHub workflows passed on merged `main`. [Full merge record](pr-86/MERGE-REPORT.md). Review-only PRs #84/#85 remain unmerged.

- [PR #88 — v9 finite-forward hit safeguard, **Chat B R2 design review-01 CHANGES REQUESTED; v2 pending review-02**](pr-88/STATUS.md): three high-severity and two major design findings in [Chat B review-01](pr-88/reviews/review-01-chat-b.md) at original SHA `28c4aa94...`. Revised docs-only proposal SHA `391047a5...` replaces premature mandatory v9 suppression with **test-only research → separately approved opt-in noncertifying diagnostic → future separately approved mandatory policy**; adds native-hit point agreement, counterfactual public gating matrix and complete observer/cap tests. Revised-head **11/11 workflows passed**, but no new production feature. [Chat A response](pr-88/responses/response-01-chat-a.md), [targeted request](pr-88/FOLLOW-UP-02.md) and [Chat B prompt-02](pr-88/REVIEWER-PROMPT-02.md). PR remains draft/unmerged; no second independent verdict yet.

Historical coordination: Opticsim [closed, unmerged PR #76](https://github.com/physicsvigilante/opticsim/pull/76) retains the original draft collaboration protocol and frozen review packet. Original [review-only PR #77](https://github.com/physicsvigilante/opticsim/pull/77) was also closed unmerged after verbatim preservation of both Chat B reports. The central hub is now the intended home for NEW review packets and reports; original source PRs and evidence are not rewritten.

All source-engine, physical/teaching and merge rules still come from Opticsim's `AGENTS.md`, its pinned PhyDemo and its own CI.
