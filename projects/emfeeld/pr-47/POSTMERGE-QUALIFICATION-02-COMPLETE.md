# PR #47 — actual-main release qualification COMPLETE

2026-11-18. This final entry supersedes the pending status in the original integration record and checkpoint01; their observations and all historical failures remain preserved. **All actual-main automated release gates are complete.** This is not human Windows acceptance or teacher/JEE effectiveness certification.

## Exact source

Actual merge/main `f6a078354ec2a657ca010c5c92ea578a0f55a2ad`; tree `65935bb395552d3dfb466a6e48d03230f18b6b66`, identical to independently reviewed head `fcf9fede87ccd37597d0ba8c9b9013ee99b764f0`. The separate-context review-01 remains SCOPED PASS, blob `8b4718ea93d0c94862cf44aa263a5b16ca72715f`, with its original 143 reviewer-owned checks, timed-out full viewer rerun and limitations unchanged. Integration added nine files; all 382 baseline files were preserved (391 total tracked files, 34 Python package modules).

## Fresh actual-main workflows

- [Full Ubuntu/Windows clean install 44296944746](https://github.com/physicsvigilante/emfeeld/actions/runs/44296944746): both jobs COMPLETED/SUCCESS, all later evidence and upload steps complete. Ubuntu job134776324762 and Windows job134776325189 each recorded **1,783 headless +18 historical (one obsolete guard deselected) +46 actual-PyVista tests**.
- [Gauss lesson 44296944965](https://github.com/physicsvigilante/emfeeld/actions/runs/44296944965): SUCCESS, 83 overlapping focused tests and eight retained scenes.
- [Conductor lesson 44296944750](https://github.com/physicsvigilante/emfeeld/actions/runs/44296944750): SUCCESS, 71 overlapping focused tests and six scenes.
- [Legacy viewer 44296945003](https://github.com/physicsvigilante/emfeeld/actions/runs/44296945003): SUCCESS, 1,783 headless tests, nine legacy cases and 17 PNG receipts.

These are actual merged-source push runs, not the earlier PR preview. Focused counts overlap full suites. The source-snapshot workflow is PR-only; the actual-main source TAR is retained by the lesson/viewer archives.

## New original OS archives — read-only audit

| OS | Artifact ID | Bytes | Whole original ZIP SHA256 |
|---|---:|---:|---|
| Ubuntu | 14425475579 | 9867139 | `3e6f46ecbc8c07fc45b6d562550665838d68324e894a41af5a931dd5e6583b1f` |
| Windows | 14425945135 | 9722106 | `d0f4286c41f0414c04d2a75db8400f729d7dd50ecb12e7b975233ee11a89e401` |

Each ZIP matches GitHub's reported digest, passes CRC, contains **2,186 unique safe relative paths**, and records actual merge SHA in `head-sha.txt`. Each contains **173 integrity manifests /1,750 hash references**: 1,749 match and the one deliberately corrupted negative `derived-001/G1/review-challenge-resealed-native/native/result.json` remains a negative fixture. Its separately retained `review-challenge-rejected-out/result.json` is explicitly partial with `operand_unavailable`; it is not counted as valid measurement evidence.

All **82 top-level implementation receipt sets per OS**, each naming all34 modules, were compared against the exact source bytes. Windows checkout CRLF was represented in memory during comparison; no original archive was altered. Original test logs confirm the counts above. Signed ensemble E1 remains complete and G1 partial, including native-view delegation; G1's viewable member does not upgrade its overall ensemble status. The physics demonstration log remains passed.

## Lesson/viewer archive reconfirmation

Original Gauss artifact14425020701 SHA256 `aacb458f5f2998d7b1d35d05ab286c111668f58ce8602e121a0573d77c040569` (71 ZIP members;56 scene inventory references), conductor artifact14424161404 SHA256 `b3bc45e55b1cf4dcd973fe28c7efedc0521048b91c62bdcd3cb0b0aefdbff9ec` (49 members;36 scene inventory references), viewer artifact14423518406 SHA256 `031b8968c51f30f464fb3a4d0a05624606195172253121d4da2b055097560589` (22 members) were rehashed/CRC/path checked. All three TARs reproduce the same391 files. A fresh extracted Git index independently reconstructs tree `65935bb...`. Gauss and conductor scene implementation, current-state and image digests match. Gauss saved local normal-field samples equal the stored E dot n; the boundary scene retains null exact total and no field samples. Checkpoint01 preserves the original visual inspection.

## Disposition

PR47 is merged and fully qualified for its declared bounded static, opt-in lesson. Close Issue46 as completed. **Issue48 remains separate**: stronger sampling-discrepancy warning and small-window layout, without altering this reviewed physical source during release. The current chapter mapping, author/reviewer histories and evidence remain unchanged. A fresh 74-case focused headless rerun on the extracted unchanged merged source also passed; it is overlapping author evidence.

Not claimed: a general Maxwell/conductor/PDE solver, arbitrary-scale accuracy, native observation-packet integration, manual human Windows operation, independently established classroom usefulness, or an unseen JEE-task pass.
