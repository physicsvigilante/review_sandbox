# PR #52 — full postmerge release qualification

**2026-11-19. RELEASE QUALIFIED ON ACTUAL MAIN.**

## Exact source and review

- PR: https://github.com/physicsvigilante/emfeeld/pull/52
- Merged actual-main SHA: 83ef4a1629e4e0f6e1742bb63019c1df45f326b8.
- Actual merged Git tree: f161a608853e5e180c459d68454e48c8fb734c39; byte-identical to the independently accepted candidate 43980b952e533483a36fedac2e95eab3df980f82. Ordered GitHub parents [prior-main 6bfeb2c314841ef861d7d66b67c894a6295b705e, reviewed candidate] and expected-head merge guard were verified.
- The independent R52-A/R52-B review-02 PASS: https://github.com/physicsvigilante/review_sandbox/blob/main/projects/emfeeld/pr-52/reviews/review-02-chat-b.md (blob 881aee78a027b580f58463c8071a19865dacbe91). Both earlier CHANGES REQUESTED reports, reproduction logs and reviewer corrections are preserved. 37 independent reviewer tests and genuine PyVista challenges; no new physics or general renderer changes were introduced after review.
- Seven bounded main-relative changed paths; all old field laws, integrators, solver tolerances, original scene data and specialized JEE viewers retained.

## Actual-main CI and original artifacts

| Workflow on actual-main | Run ID | Original artifact ID | ZIP SHA256 | Result |
| --- | ---: | ---: | --- | --- |
| Clean install Ubuntu | 44460186412 | 14500331169 | 115861dd74306d05b98d9586e2199ab2828f1b4c1841b2022ceff6961bea34a4 | PASS/audited |
| Clean install Windows | 44460186412 | 14500815461 | 62ba36c32bd83a3fe1d5112aba85a76a57720b4be9acbe4e57cd94cafb0bad36 | PASS/audited |
| Real PyVista viewer | 44460186414 | 14499009941 | 04b9f95f6246b61c387e2b8a7c086b81cb9c2d8701faeb054dcd41bcaa8d5053 | PASS/audited |
| Gauss law | 44460186471 | 14499352329 | ead87eb0e2281d95532eb67caafe37a6941bbbadcfcbdc3d7f3ddcb0c0899679 | PASS/audited |
| Conductor cavity | 44460186485 | 14499337444 | 3e178ef68cfd398f25391ffb61ddde86c0672b689ad64e1050693cbc891b931b | PASS/audited |

All four actual-main push workflows completed SUCCESS. Each OS passed **1,857 headless +18 historical (one preexisting obsolete freeze guard deselected) +56 real-PyVista tests** with all downstream evidence/upload stages. Focused Gauss 127 and conductor 71 counts overlap full suite and are not new independent cases.

Both new original OS ZIPs were downloaded/read-only SHA256/CRC/safe-unique path audited: 2,186 members per OS, 173 integrity inventories, 1,750 hash references (1,749 correct plus exactly the known deliberate corrupt refusal fixture at derived-001/G1/review-challenge-resealed-native/native/result.json). The negative fixture remains invalid, never relabeled or repaired. Both have 82 x 35 = 2,870 matching current-source module-hash receipts (Windows CRLF accounted for without modifying source or ZIP), and actual-main head-sha.txt equals 83ef4a16... Source identity matches all 400 tracked files and the reviewed Git tree; E1 remains complete and G1 remains partial. Original logs and failures retained.

Fresh actual-main Gauss ZIP: 114 members,14 actual scenes,14 manifests/92 verified file refs and490 module refs. Cavity ZIP:49 members,6 scenes,6 manifests/36 refs and210 module refs. Viewer ZIP:22 members,9 real PyVista scenes,17 verified PNG receipt hashes. All **17 original viewer PNG bytes match SHA256 exactly** against both the accepted candidate viewer and prior released main. Original nested scene source TAR from these ZIPs:400 exact source files, SHA256 6088832ae14581d4664e1ea85755053dbf785ffadfd063ea812f2fec6fd5d161; verified tree f161a608... . Hosted cross-environment last-bit roundoff for numerical trajectory coordinates is not treated as a changed law or as bitwise equality across hosts.

## Separate downstream gates

PR51 dipole correction remains independently scoped R2 PASS on 68f1b170..., not yet merged here. Compatibility-only local preview combined this exact 400-file renderer source with ten additive dipole files: 410-file predicted tree 1ec88afdc7a3d057a21e39a52769c190fd1577f2, 1,929 headless and 73 actual PyVista tests passed with -W error. This is AUTHOR preview, not actual-main CI nor independent reviewer testing. PR51 must now receive its own guarded merge + fresh actual-main CI/original ZIP audit before Issue50 closure. PR53 browser prototype remains separately draft/unmerged, requires its own review/retargeting. No manual Windows, all-DPI, unseen-JEE or teacher acceptance is claimed.