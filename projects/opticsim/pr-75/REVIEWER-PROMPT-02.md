> **Archived prompt.** The second Chat B review has already been completed and published in [review-02-chat-b.md](reviews/review-02-chat-b.md). Do not start another identical review; issue a new prompt only when a new review cycle is necessary.

# Paste into the second ChatGPT conversation — Opticsim PR #75 targeted review

You are Chat B, the separately situated reviewer. Do **not** repeat your original broad review. The original verdict was **insufficient-evidence**, not a demonstrated production physics bug.

**Central review hub:** https://github.com/physicsvigilante/review_sandbox
**Current request:** https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-75/REQUEST.md
**Original report imported verbatim:** https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-75/reviews/review-01-chat-b.md
**Original Chat B PR:** https://github.com/physicsvigilante/opticsim/pull/77
**Opticsim source PR:** https://github.com/physicsvigilante/opticsim/pull/75
**EXACT implementation head:** `f4fddec213e04d733920399dc0eeea0b29a60dac`

1. Read the **central** `PROTOCOL.md`, `REVIEW-RISK-POLICY.md`, current `REQUEST.md`, first report and preserved original protocol refs from `ORIGINS.md`. Compare G-01 against the original docs at the original exact commit, preserving the true old default-branch 404.
2. Focus on E-02: **genuinely new test-only native/browser checks** for detector endpoint/reverse orientation, two-detector overflow isolation and one stale/failure or ray-event inconsistency case. If local execution is blocked, publish test-only source changes in a NEW Opticsim review branch rooted at PR #75's exact head and let GitHub CI execute; capture actual run IDs. Never edit PR #75 source or historical fixtures, PhyDemo, numerical policies or production logic. If unavailable, document why.
3. Document H-03 as a trusted-internal-runtime evidence boundary, not a manufactured production exploit. Defer U-04/O-05 optional improvements unless a new test proves a real defect.
4. **Write a new second-pass review report directly to the CENTRAL repository** at `projects/opticsim/pr-75/reviews/review-02-chat-b.md`. Use `REVIEW-TEMPLATE.md`. Preserve original review-01. A separately created review PR is fine if preferred, but direct creation of this unique file on central main is supported. Provide the direct GitHub URL to the new file. Do not simply reply with a review in the ChatGPT conversation.
5. Do not merge any PR. State `pass`, `changes-requested` or `insufficient-evidence` **for the targeted supported scope**, with exact implementation/test commits, CI and limitations. If PR #75 head has moved, stop and declare stale-head.

This is independent **ChatGPT conversation context**, not automatically an independently trained model, a human physics reviewer or classroom certification.
