# PR #122 — held v18 physics + directional detector footprint integration

**INDEPENDENT CHAT B REVIEW #1: INTEGRATION CLEARED FOR OWNER DECISION at exact reviewed research source HEAD/tree. No P0/P1 integration blocker found. DRAFT / UNMERGED / NOT RELEASED; OWNER AUTHORIZATION PENDING.**

Exact source HEAD `70cf502d19e243e4a8d7d1e0795f008c101c582d`, tree `df9282da11ff416d0033cdf7e09509ba8dc24bc9`; synthetic main-target CI merge `1ec478b5a84dcae89a23e613103f7b98f9bc1f6c` has identical tree. Correct PR dependency base restored to held `feature/native-thick-lens-aperture-v18`. Neither original reviewed source was changed.

All **865/865 Node tests and 11/11 standard workflows** passed exact-source CI, including **5/5 public detector-footprint CLI acceptance cases**, **7/7 real Chrome footprint checks**, **13/13 v18 native aperture Chrome checks**, and four new combined native tests. True v18 return has one real native crossing per signed group, N=1 and sample RMS=0 (not an image). Aperture blocking yields no crossings with N=0 and null centroids/RMS. Shallow incomplete trace suppresses both derived and original samples. Standalone footprint-only request correctly captures existing hits.

First attempt failed because the independent v18 viewer's historical source blob SHA was not the combined app blob; fixed in research branch only by adding a separate integration source pin and preserving both original feature viewer pins and the historic R1 freeze. No physics or native cutoff code changed.

[Review request](REQUEST.md) · [Ready-to-paste Chat B prompt](REVIEWER-PROMPT-01.md). Published [Chat B independent integration review #1](reviews/review-01-chat-b.md) verified exact source tree, 20-file diff, shared opt-in capture, physical detector-normal geometry, standalone source pins, CLI and real-Chrome CI evidence. **Verdict: INTEGRATION CLEARED FOR OWNER DECISION.** Reviewer did not independently run PhyDemo/Node/Chrome. Nonblocking follow-ups: F1 combined v18 Fresnel-on incomplete footprint gating; F2 if feasible v18 genuine >32 detector hit overflow; F3 combined v18 plus footprint-only browser import/edit/reopen; F4 README language. None is an observed physics defect or merge authorization.

**HOLD** all dependent/unrelated PRs #107, #110, #113, #116, #118, #119, #120, #121 and this research-only #122. #120 original v18 physical R2 review was separately published and **CLEARED FOR OWNER DECISION** on exact original v18 source; both reviews still require separate owner release decisions.

## Review reconciliation (2026-11-17)

[Separate v18 R2 review #1](../pr-120/reviews/review-01-chat-b.md) and this [independent integration review #1](reviews/review-01-chat-b.md) are now both published at their respective frozen source HEADs. The phrase “#120 pending” in the original, frozen integration reviewer report refers to the chronology *when it was written*, not current review status. Neither review establishes full independent runtime replication, universal optical numerical correctness or permission to merge held PRs. Any F1–F4 modifications must use a separately reviewed follow-up source tree, preserving these reviewed exact heads.
