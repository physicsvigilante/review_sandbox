# PR #52 — actual-main post-merge qualification checkpoint 01

**2026-11-19. MERGED; FULL RELEASE NOT YET DECLARED AT THIS CHECKPOINT.**

## Exact immutable release source

Merged SHA `83ef4a1629e4e0f6e1742bb63019c1df45f326b8`, exact tree `f161a608853e5e180c459d68454e48c8fb734c39`. Both GitHub commit tree and real current main ref were verified; ordered parents [old main `6bfeb2c3...`, independently reviewed accepted head `43980b95...`]. This is the same 400-file tested tree as original candidate/source ZIP, not a fresh physics change. Independent R52-A/B review-02 PASS at exact corrected source, original review-01 CHANGES REQUESTED preserved.

## Fresh actual-main specialized and viewer workflows — PASSED, original artifacts read-only audited

- **Gauss 44460186471**: success; original artifact `14499352329` whole ZIP SHA256 `ead87eb0e2281d95532eb67caafe37a6941bbbadcfcbdc3d7f3ddcb0c0899679`. 114 safe unique ZIP files and CRC; 14 actual PyVista scenes; 14 integrity manifests with 92 matching file references; 14 × 35 = 490 module/source hash matches; 127 overlapping focused tests passed. Nested original source TAR had 400 files, byte-for-byte identical to independently reconstructible released tree; TAR SHA256 `6088832ae14581d4664e1ea85755053dbf785ffadfd063ea812f2fec6fd5d161`.
- **Conductor cavity 44460186485**: success; original artifact `14499337444` whole ZIP SHA256 `3e178ef68cfd398f25391ffb61ddde86c0672b689ad64e1050693cbc891b931b`. 49 unique safe files/CRC; six actual scenes and six manifests with 36 matching file references; six × 35 = 210 matching module hash receipts; 71 overlapping focused tests. Exact same 400-file original TAR.
- **General real-PyVista viewer 44460186414**: success; original artifact `14499009941`, whole ZIP SHA256 `04b9f95f6246b61c387e2b8a7c086b81cb9c2d8701faeb054dcd41bcaa8d5053`, 22 unique safe files/CRC; nine true PyVista scenes and 17 PNG SHA checks vs the original report. Full current source TAR is 400 files and reconstructs exact merged tree, with same nested TAR digest. **All 17 original PNG bytes match SHA256 exactly** against both prior independently reviewed candidate viewer artifact and previous released main `6bfeb2c3...` viewer artifact. Cross-host saved trajectory position floats do not warrant a blanket bitwise claim; report physical comparisons separately.

These are original hosted artifacts, not repacked summaries. The focused Gauss/cavity tests overlap full regression counts. The first independent review's failures remain retained; reviewer R2 review-02 and scoped limits unchanged.

## Still pending

Fresh actual-main clean-install Ubuntu and Windows workflow **44460186412**, both final successful jobs and original OS artifacts. They must be independently author-audited for whole-archive SHA256, 2,186 safe paths/CRC, 173 integrity inventories, 1,750 referenced hashes, known intentionally invalid negative, all 82 current-source module receipt sets × 35 modules, actual merged commit marker, numerical/stored evidence and complete logs before marking release complete. No author test substitutes for independent reviewer results. No manual human Windows, all-DPI, teacher usefulness, or browser parity assertion.

PR51 dipole correction remains separately independently reviewed and eligible for *later* guarded integration once PR52 is fully release-qualified. PR53 remains a distinct draft.
