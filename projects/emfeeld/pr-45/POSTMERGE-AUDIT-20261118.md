# PR #45 — actual-main release gate complete

Date: 2026-11-18. Author audit, not a new independent R2 physics review.

Actual main `aeea3fedb00de4e20304d1f88aa038f3fac1e99e`; Git tree `d1892d73d8f19443ba523ab5c2dc8f709e260ebe`. Main-push workflow 44270547699 completed successfully on Ubuntu job 134685764689 and Windows job 134685765029. This closes the PENDING post-merge gate recorded in MERGE-REPORT.md; the original pending entry and cancelled PR44 attempt remain historical records.

Original archives downloaded and checked, not recreated ZIPs:

| OS | Artifact | Whole ZIP SHA256 |
|---|---|---|
| Ubuntu | 14413200389 | `54a57701a5cd3bda60339dc4ccfad1e51e9d32089e885f14f00112fbadea13e6` |
| Windows | 14411909946 | `3c8b359b3ae2c26c51eb0b592776a69d696aeb5a7198255a5ed0043763eb3752` |

Both archives have 2,186 unique safe relative paths and pass ZIP CRC checks. Both original head-sha.txt files identify the actual main SHA above. Each archive contains 173 integrity manifests and 1,750 hash references: 1,749 match; the sole mismatch is the deliberately altered negative fixture `derived-001/G1/review-challenge-resealed-native/native/result.json`. It is retained as a negative, not certified as intact evidence. Both original logs report 1,709 headless tests, 18 historical tests with one obsolete guard deselected, and 37 real-PyVista tests passed. Signed E1 readout remains complete; G1 remains partial.

All 32 implementation-module digests in the original native run receipt match the source (Windows CRLF bytes reconstructed in memory only). Source identity was also checked against the original PR47 source artifact 14412682586: its 384-file tree reconstructs to `7315587ed3b06ae7e8fca55b2bd5f5a6b5144e1b`; removing precisely the two added Gauss-law files reconstructs the exact 382-file PR45 main tree `d1892d73d8f19443ba523ab5c2dc8f709e260ebe`. No archived file was edited or resealed.

PR45 is now release-qualified for its one-line CI timeout change. The unchanged conductor lesson retains its separate PR44 independent scientific review and dedicated viewer/lesson evidence; these are not mislabeled as new PR45 dedicated jobs. No manual Windows acceptance, teacher trial, new physical law or arbitrary-scale correctness claim follows.
