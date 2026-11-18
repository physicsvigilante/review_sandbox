# PR #47 — independent review, guarded integration and release

## Current status — 2026-11-18

**MERGED; fresh actual-main release qualification is PENDING.** Do not confuse premerge successful jobs with the new main-push gate.

## Independent review assessment

[Chat B review-01](reviews/review-01-chat-b.md), original blob `8b4718ea93d0c94862cf44aa263a5b16ca72715f`, gives **SCOPED PASS** on exact candidate `fcf9fede87ccd37597d0ba8c9b9013ee99b764f0`, tree `65935bb395552d3dfb466a6e48d03230f18b6b66`, base `aeea3fedb00de4e20304d1f88aa038f3fac1e99e`. No blocking physics, geometry, input or evidence defect was identified in the bounded static cube/sphere lesson.

Reviewer-owned completed checks: 87 physics +16 evidence/admission +38 real PyVista controller/receipt +2 geometry/glyph =143 scripted checks, not statistically independent trials. The reviewer also reran74 authored headless cases. The nine-test viewer rerun timed out after six observed passes and remains incomplete, not a pass. The separate fresh38-check controller suite and two actual screenshots completed. Intermediate camera rendering was skipped during that sweep; real VTK rendering was restored for its two screenshots. The initial reviewer harness failure assumed world x=1 remained a cube boundary after rotation; the harness was corrected, not candidate source. All these limitations remain in the original unmodified review.

Nonblocking follow-ups: emphasize unreliable near-surface sphere quadrature when error is large; prevent text/colorbar crowding in reduced viewports. The existing exact/sampled/error labels are truthful. Do not normalize samples or change physical values for presentation. This review is not manual Windows UI acceptance, a human teacher trial, a blind JEE evaluation or a general Maxwell/PDE capability claim.

## Source and premerge gates

Live PR/main/commit reads confirmed unchanged reviewed head, qualified main/base and same-tree CI preview `457e2e3d79b205a7bb61fe7c4af5d9d585415d96` with ordered parents [base,candidate]. All five exact-head workflows were rechecked completed/success. [Author qualification01](AUTHOR-QUALIFICATION-01.md) and [CI/archive addendum02](AUTHOR-QUALIFICATION-02-CI-COMPLETE.md) retain original evidence and failures. Both OS suites passed1,783 headless +18 historical (one obsolete guard deselected) +46 real-PyVista each. Focused counts overlap full suites. Six original premerge ZIPs were audited. The original source ZIP and50,688,045-byte handoff ZIP were rehashed/CRC-checked during integration; they match recorded digests.

## Guarded integration completed

The owner reported review completion after standing direction to continue bounded development and pause at independent review. After assessing that review and live guards, PR47 was marked ready, then merged with `merge_method=merge` and `expected_head_sha=fcf9fede87ccd37597d0ba8c9b9013ee99b764f0`.

**Actual merge:** `f6a078354ec2a657ca010c5c92ea578a0f55a2ad`.
**Actual merged tree:** `65935bb395552d3dfb466a6e48d03230f18b6b66`, exactly equal to the independently reviewed candidate and CI preview.
**Ordered actual parents:** [`aeea3fedb00de4e20304d1f88aa038f3fac1e99e`, `fcf9fede87ccd37597d0ba8c9b9013ee99b764f0`].

A separate GitHub Git-commit read verified these values after the merge. No review finding was fixed opportunistically during integration, and no unreviewed source was added. Nine additive paths preserve all382 baseline files;391 tracked files,34 package modules.

## Actual-main release gate — pending

Fresh push runs on actual merge `f6a07835...`:
- Full Linux/Windows clean-install:44296944746.
- Dedicated Gauss lesson:44296944965.
- Existing real viewer:44296945003.
- Existing conductor lesson:44296944750.

All four were observed started, not yet qualified at this entry. The source-snapshot workflow is PR-only; main source preservation is in the viewer/lesson archives. Verify new original ZIP hashes/CRC/safe paths, source TAR reconstruction to the reviewed tree, actual `head-sha.txt`, test outcomes, state/image/array receipts, all34 source-module hashes (including Windows checkout line endings), signed E1 complete/G1 partial semantics, and the deliberate corrupted-negative fixture as a refusal. Issue46 remains open until that actual-main gate completes.
