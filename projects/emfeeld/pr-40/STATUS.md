# EM Fields PR #40 — current reliability-audit status

**2026-11-18 IST: MERGED; post-merge Windows release closure pending.** This current-status page supersedes the pre-merge snapshots retained in its Git history. Original review reports, failed cases, responses and archive audits remain unchanged.

## Source and independent review

- Actual main/merge: **`883242106e127c7b8f976660377b07a49aeded88`**.
- Exact reviewed feature: **`f56ce83e791e3fcd3b1f17609c38a2f98a999c41`**.
- Identical reviewed and merged Git tree: **`48baa0d760a2e99d0e953d6df5d7b999801d48cd`**, 372 tracked files, 30 engine Python modules.
- [Final independent review-02](reviews/review-02-chat-b.md): **targeted PASS**, 43 numerical/telemetry and 45 preservation tests. R2-01/02/03 closed within tested scope. Only the final verified-execution publication is qualifying evidence; its initial unsupported publication and subsequent withdrawal are explicitly retained in history. Review-01 remains CHANGES REQUESTED on the old head.
- Expected-head guarded merge returned success. Actual main/tree and ordered parents [previous qualified main, reviewed feature] were separately verified. Owner standing integration direction is distinct from the reviewer technical verdict.

## Actual-main release gates

[New main-push workflow 44154671635](https://github.com/physicsvigilante/emfeeld/actions/runs/44154671635): Ubuntu completed success and its original ZIP passed source/native/integrity audit; Windows was still finishing at this update. [New viewer workflow 44154671754](https://github.com/physicsvigilante/emfeeld/actions/runs/44154671754) completed success, original source tree reconstructed, nine offscreen cases and 17 PNG receipts verified.

Fresh actual merged-source local execution: **1,642 headless passed**, **18 historical passed /one obsolete guard deselected**, published V6 ten cases, discovery two cases and physics-demo one case /17 native observations /64 checks passed. These are author checks, not additional reviewer-owned tests.

[Merge record](MERGE-REPORT.md) and [new actual-main original archive audit](POSTMERGE-ARCHIVE-AUDIT-01.md) contain exact identities and current gates. **Issue #39 remains open until Windows completes and its new original ZIP is audited.** Old PR-preview artifacts are not substituted for actual-main release evidence.

## Preserved boundaries

The deliberately corrupted rejection fixture stays invalid and unavailable, not counted as intact evidence. All other checked inventories and source maps must match. Historical implementation-pinned studies keep their original source/receipts; replay unchanged inputs into new outputs rather than resealing originals. No blanket extreme-scale correctness, malicious concurrency protection, arbitrary-language interpretation, independent teacher trial, human Windows interaction or full visual acceptance is claimed. Issue #36 remains separate.