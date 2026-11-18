# PR49 — focused review, guarded integration and release

## Status at integration — 18 November 2026

**MERGED; fresh actual-main release qualification PENDING.** Premerge success is not actual-main qualification.

## Independent review

[Chat B review-01](reviews/review-01-chat-b.md), original blob `fad0ee50d21125f6f3e803c0f03dd6a425a5f3e0`: **PASS (scoped R1 presentation/evidence metadata)** on candidate `9963c09d169a04cea488886db5f04c0de4074886`, tree `4da6b80f53d78b2394c8516b9463e442fffb50fe`, released base `f6a078354ec2a657ca010c5c92ea578a0f55a2ad`. No blocking affected-path defect identified.

The reviewer reran 39 existing presentation and five existing real-PyVista usability tests; these are not new reviewer-authored cases. Fresh reviewer work included nine caution configurations, eleven independently executed base/candidate comparisons (exact equality in that environment), real slider/native-resize/prediction/boundary sequences, screenshots and current-state/input/array/hash/output-protection checks. No aggregate statistically independent test count is asserted. A reviewer metadata helper KeyError was corrected without a candidate change; original author failures/cross-host roundoff observations remain retained.

The review did not independently verify preview ordered parents or live Actions artifact IDs through its available interface. The integration session separately checked preview ordered parents/tree through the Git-commit API and all five successful premerge workflows. The companion reviewer evidence ZIP is named in the review but was not supplied here; no inspection of its bytes is claimed.

Nonblocking opportunities: a short live no-banner-is-not-accuracy reminder; manual dense/extreme-value legibility at minimum size. No unreviewed follow-up was added to this merge. No teacher, manual Windows, all-DPI or sampling-accuracy certification.

## Source and premerge gates

All five exact-head workflows were re-read completed/success: source44302715755; full OS44302715851; Gauss44302715942; viewer44302715977; cavity44302715844. [Author report01](AUTHOR-QUALIFICATION-01.md) and [final CI/archive report02](AUTHOR-QUALIFICATION-02-CI-COMPLETE.md) retain original audits and failures: 1,822 headless +18 historical (one preexisting obsolete guard deselected) +51 real-PyVista per OS, 127 overlapping focused Gauss tests/14 scenes, six original archives. Focused counts overlap full suites.

Original source ZIP SHA256 `7ae28db3a740cd3aeb1feefd31f5a53600773aa130cde6be6858c943376aa4a7` and 51,894,870-byte handoff SHA256 `051b9b5d6860ce8de90190e30a7e656fbeab1a0000f174f1a99abf1775b6226c` were rehashed/CRC-checked during integration. Safe extraction of source TAR `375c61cbdea9c9fb2f9595fdc475f46f898143f55f22b75f421ed19646c7222e` recovered394 files; local `git write-tree` independently returned `4da6b80f53d78b2394c8516b9463e442fffb50fe`.

Six changed paths: three modified presentation/workflow/contract paths, three added qualification paths. All388 other baseline files, numerical physics modules and old tests remain unchanged. The warning threshold is informational, not a solver tolerance or measurement acceptance change.

## Exact guarded integration completed

Owner confirmed review completion under standing direction to continue bounded development and pause for independent review. After review assessment and live head/main/CI checks, PR49 was marked ready and merged with method `merge` and expected head `9963c09d169a04cea488886db5f04c0de4074886`.

**Actual merge:** `6bfeb2c314841ef861d7d66b67c894a6295b705e`.
**Actual tree:** `4da6b80f53d78b2394c8516b9463e442fffb50fe`, identical to reviewed head and preview.
**Ordered parents:** [`f6a078354ec2a657ca010c5c92ea578a0f55a2ad`, `9963c09d169a04cea488886db5f04c0de4074886`].

Separate post-merge Git-commit read verified these. Preview `7635a3e96079f54167dbbb14f96299e8397555a1` has the same tree and ordered parents, directly verified before integration. No source changes were added during merge.

## New actual-main gate — pending

New push runs on actual merge: full Linux/Windows **44310514548**; Gauss/usability **44310514516**; viewer **44310514531**; cavity **44310514570**. All were observed started. Require final successful jobs and new original archive whole-hash/CRC/path/source/current-state/image/module/evidence audits. Source snapshot is PR-only; source TARs are in actual-main viewer/lesson archives. Preserve E1 complete/G1 partial and the deliberate corrupt negative as a correctly refused negative, not validated evidence.

Issue48 remains open until this gate completes. Issue50 is the separately scoped next dipole milestone, not implemented by PR49.

## Operational record

The first attempt to create this report was rejected with GitHub409 because review_sandbox/main advanced concurrently. The directory was re-read and confirmed this path absent; this retry adds the new report without overwriting any other work. No product-source change or failed-physics claim follows from that write conflict.
