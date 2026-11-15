# Opticsim review index

Source repository: https://github.com/physicsvigilante/opticsim

- [PR #75 — detector-hit measurements](pr-75/STATUS.md): both Chat B reports imported verbatim from [Opticsim PR #77](https://github.com/physicsvigilante/opticsim/pull/77). First verdict was **insufficient-evidence**; second was a **scoped pass** after three new native adversarial tests. The implementation PR #75 and independently authored test-only PR #78 are now merged; both post-merge CI suites passed.

- [Current-main source-backed transfer + native-ray lineage feasibility, research-only PR #79](research/source-backed-transfer-v2/REPORT.md): exact frozen-request replay on Node24, 0/5 complete original tasks, and narrow native parent/child event feasibility; no production or independent Chat B review claim.


- [Research-only PR #80 — adversarial native ray-lineage boundary study](https://github.com/physicsvigilante/opticsim/pull/80): Node 24.19.0 CI 11/11 passed; 12 native scenarios, eight narrowly observed and four withheld, plus one geometry preflight refusal. Test-only research, still draft/unmerged; not a general lineage guarantee.

- [PR #81 — bounded detector-ray provenance, **independent R2 design-only PASS**](pr-81/STATUS.md): [Chat B review-01](pr-81/reviews/review-01-chat-b.md) requested changes at v1 SHA; [Chat B review-02](pr-81/reviews/review-02-chat-b.md) passed revised v2 exact head `d814455cf823907551cbc7914d1f8b3b508efcab`, with nonblocking detector/interface observer-installation test watchpoint A-01. No implementation exists or is authorized; future code needs separate owner approval and a fresh full R2 code/evidence review.

- [PR #82 — bounded native detector parentage, **R2 implementation code/evidence review pending**](pr-82/STATUS.md): separate draft implementation, with pinned-native/failure-injection/public/Chrome acceptance, [review packet](pr-82/REQUEST.md) and [Chat B prompt](pr-82/REVIEWER-PROMPT-01.md). This is a new code-review gate, not a repeat of PR #81's design-only pass. No merge authorization.

Historical coordination: Opticsim [closed, unmerged PR #76](https://github.com/physicsvigilante/opticsim/pull/76) retains the original draft collaboration protocol and frozen review packet. Original [review-only PR #77](https://github.com/physicsvigilante/opticsim/pull/77) was also closed unmerged after verbatim preservation of both Chat B reports. The central hub is now the intended home for NEW review packets and reports; original source PRs and evidence are not rewritten.

All source-engine, physical/teaching and merge rules still come from Opticsim's `AGENTS.md`, its pinned PhyDemo and its own CI.
