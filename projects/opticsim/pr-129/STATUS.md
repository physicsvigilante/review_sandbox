# PR #129 — narrow v19 forward post-lens stop admission correction

**RESEARCH/CORRECTIVE DRAFT / UNMERGED / NOT RELEASED. New-source independent review PENDING. Exact-head CI PENDING at packet creation.**

- [Correction PR #129](https://github.com/physicsvigilante/opticsim/pull/129), source HEAD `491229a29257a2cf7e4368372120d087e736a4c7`, Git tree `07ff1ea9a8ff5660520ae6d37389b895d49fb163`. Temporary `main` CI synthetic merge `51f4fea5ab18f1b4f784c110f7292d197f96b28c` has identical Git tree. The true prerequisite is preserved test-only PR #128 at `1b712dc00a0e49b0bc320b86b62f0c1d4bb94120`. Base will be restored after CI; main is not to be changed.
- Chat B R2 independently [cleared original v19 PR #127](../pr-127/reviews/review-01-chat-b.md) for owner decision on source `05385e3daefaffcfc56fb072a12ba81dd6432993`, **not** this later source. PR #128 contains actual pinned native post-lens endpoint counterexample and 812/812 Node/11 workflow source-CI evidence, not a separate independent reviewer native run.
- Corrective source change: fail closed for a forward source → ideal lens → aperture plane order in bounded v19. No synthetic refracted route or solver patch. Before-lens stop both directions remains admitted. Canonical v19 slab starting inside medium, reverse media and numerically shallow native incompleteness checks retained.
- Changed paths only: `src/parallel-beam.js`, `test/jee-v19-review-secondary-routes.test.mjs`, `docs/NATIVE-PARALLEL-BEAM-V19.md`. No old profile/contract, native pin, observer, historical frozen evaluation or reviewed PR source changed.
- Reviewer [REQUEST.md](REQUEST.md) and [REVIEWER-PROMPT-01.md](REVIEWER-PROMPT-01.md). Chat B report `reviews/review-01-chat-b.md` not received. Exact source CI must be examined before any physical clearance.

**Do not merge** PR #129, #128, #127 or existing held v14–v18/research/measurement PRs. Future production requires separate v14–v19 integrated source review, branch safety and owner authorization.
