# PR #49 — actual-main release qualification COMPLETE

2026-11-18. Actual merge **6bfeb2c314841ef861d7d66b67c894a6295b705e**, Git tree **4da6b80f53d78b2394c8516b9463e442fffb50fe**, identical to reviewed candidate **9963c09d169a04cea488886db5f04c0de4074886**. This addendum completes the pending OS/archive gate in [checkpoint 01](POSTMERGE-QUALIFICATION-01.md) and [integration record](MERGE-REPORT.md); dated earlier pending entries remain historical, not rewritten.

## Final actual-main OS evidence

Live connected GitHub jobs for release workflow **44310514548** are both COMPLETED/SUCCESS, including all downstream evidence/upload/cleanup steps. Ubuntu job **134823116967** and Windows job **134823117447** each retain **1,822 headless +18 historical (one pre-existing obsolete guard deselected) +51 real-PyVista** passes in their original logs. These are CI/author checks, not new independent reviewer checks.

Original new postmerge archives were downloaded through the connected GitHub artifact action, then audited read-only:

| OS | Artifact | Bytes | Whole ZIP SHA256 |
|---|---:|---:|---|
| Ubuntu | 14430258848 | 9866976 | ca28879c0a0432997fc9c4a2f663dd697b5c9a014e070985fcd2c0a553431b46 |
| Windows | 14430832900 | 9723078 | 4e033230020ac8cb238a7c78b67dbf9dfcac078388b671a2b31af21f18f0e1e0 |

Both hashes match GitHub artifact metadata tied to actual merge SHA. Both ZIPs pass CRC and unique safe relative-path checks: **2,186 members, 173 integrity manifests, 1,750 recorded hash references each**. There are **1,749 matching references** plus exactly the previously declared deliberately corrupted negative `derived-001/G1/review-challenge-resealed-native/native/result.json`, separately preserved rather than called valid evidence. The archived `head-sha.txt` equals actual merge SHA in both. All **82 implementation-receipt sets per OS** match all **34 package modules** from the reviewed source (Windows checkout CRLF handled in memory). Signed ensemble E1 remains `complete`, G1 remains `partial`; both native view logs and old physics demonstration evidence remain present.

The prior OS audit helper was reused with only the archive/source/output locations and expected actual-main SHA changed. Its original and this adapted helper, outputs and JSON audit results are retained in the current author work directory. The host's unrelated Python startup printed an artifact_tool initialization exception to stderr; both audit subprocesses returned 0 and completed their assertions. This is disclosed environment noise, not a product failure, and the original stdout/stderr logs are retained.

## Source and other actual-main gates

The original postmerge Gauss source TAR was re-extracted with safe-path/link checks. `git init; git add -A; git write-tree` independently reconstructs **4da6b80f53d78b2394c8516b9463e442fffb50fe**, **394 tracked files**. Its identities record the actual merge SHA. Main was re-read and still points to that merge. No product source was changed during qualification.

The three completed postmerge workflow/archive audits in checkpoint01 remain: Gauss/usability **44310514516 / 14429738484** (127 overlapping focused tests, 14 scenes); conductor **44310514570 / 14430291674** (71 focused, six scenes); viewer **44310514531 / 14429981956** (1,822 headless, nine legacy cases, 17 PNG receipts). Their new original source, state, sample and image checks and author screenshot inspection are already recorded there. Focused counts overlap the full suites. Together with the two OS ZIPs, all **five original actual-main archives** are audited; premerge archives are separate historical evidence.

## Decision and limitations

**PR49 is fully release-qualified in its bounded presentation scope; Issue48 can close completed.** The separate-context scoped R1 PASS remains [review01](reviews/review-01-chat-b.md), original blob fad0ee50d21125f6f3e803c0f03dd6a425a5f3e0. The warning remains informational: no banner is not an accuracy certificate. Numerical laws, admission and measured values were not changed. No human Windows operation, independent teacher trial, unseen-JEE success, arbitrary viewport/DPI or global numerical proof is asserted. Original failures and reviewer limitations remain unchanged. The next separately scoped physics work is Issue50 (dipole forces, torque and orientation energy).
