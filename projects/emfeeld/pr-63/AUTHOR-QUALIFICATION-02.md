# EMFEELD PR #63 — author correction R2 evidence (not independent review)

**Author-side checkpoint, 20 Nov 2026; NOT independently accepted, NOT merged.**
Historical independent [review-01 CHANGES REQUESTED](reviews/review-01-chat-b.md) remains unchanged. [Correction response](responses/response-01-chat-a.md) and [new independent R2 prompt](REVIEWER-PROMPT-02.md) are separate.

## Exact source identity and scope

PR #63 feature HEAD `d3385fc5efa023c9519510ef84207c0741861a45`; tree `c15bd147bcd0618253d906b704b06d3d864829d2`. Qualified main base `52aecd34338662e269fba091c0ff6664e8e1eca7`. Exactly **nine new files** against main, no existing source file modified. Two small source correction commits after reviewed `b2e19bad` tighten F1 and F2 and stabilize normalized-axis JSON round trips; original physics equation and older lessons remain unchanged.

## Exact-head validation

- [Dedicated native circular-loop run **44696085642**](https://github.com/physicsvigilante/emfeeld/actions/runs/44696085642) **SUCCESS**: 36 analytical / genuine native VTK tests, `-W error`, and **9 real PyVista scene PNGs** with original/current state receipts.
- [Original native artifact **14611150396**](https://github.com/physicsvigilante/emfeeld/actions/runs/44696085642/artifacts/14611150396) was downloaded, independently hashed and CRC checked. Whole ZIP SHA-256 **`c6a9d849684fe28cd72a9b4241760bdaf12aba3fcc9a07048e69c0ab0d074109`**; 79 unique ZIP entries, 0 bad CRC, nine original scene directories and **63/63 authentic SHA256 per-scene file references**. Screenshots visibly contain both horizontal native slider rails in the right information pane; source/current physical values, current sign, probe field and signed arrow metadata checked against separate SI expressions for all nine.
- The native ZIP's original `tested-source.tar` SHA-256 is **`4cf69b76ffb407552b15d60795b5e731a4c4040e05429f0662d1b3dceec105f6`**. Rebuilt the standard SHA-1 Git tree from all **461 tracked source file bytes/modes** in that original TAR; it equals the exact feature-tree SHA `c15bd147bcd0618253d906b704b06d3d864829d2`. The CI original checkout identity is GitHub's synthetic PR test merge `61fc3f5b4f2ade099c53075a6094cd95e9ab59f3`, not actual merged main.
- [Original source-snapshot run **44696085577**](https://github.com/physicsvigilante/emfeeld/actions/runs/44696085577) **SUCCESS**. Separate artifact **14611110050**, ZIP SHA-256 **`335567e235aefe0ad7d7da56f31a9fc173921cdc706edf3a1930cc04e15d8478`**, CRC clean. Its independently obtained source TAR is **byte-identical** (same SHA above) to native original; checked each of the **461** Git blob SHA-1s and mode bits against the original `git-tree.txt` ledger, with no mismatches.
- Local author execution of the exact correction file bytes: **126** focused pure-Python circular-loop and wire analytic tests passed with warnings as errors. Native tests and screenshots above were produced on hosted real VTK; local headless tests are not native graphical tests.

## Current CI status and release boundary

As of this record, other exact-head Gauss, straight wire, cavity, dipole, capacitor, browser and real-PyVista qualification jobs had **SUCCESS**. The [full Linux and Windows clean-install workflow **44696085549**](https://github.com/physicsvigilante/emfeeld/actions/runs/44696085549) **remains IN PROGRESS** during original real-PyVista regression. Do not label full dual-OS gate complete until both jobs and original archives are separately checked.

These are **author and CI** checks, not separate Chat B scientific/native acceptance. Reviewer-01 explicitly lacked PyVista and could not produce an independent screenshot. The new reviewer must independently run PyVista (including native sliders and keys), produce a **new reviewer-owned PNG**, rerun F1/F2 challenges and inspect exact-source artifacts. Until a supported exact-head R2 PASS, **do not merge**. After PASS, fresh actual-merged-main Linux/Windows/PNG/archive validation is mandatory. No general off-axis Biot–Savart or human classroom-effectiveness claim.

## Later full-Linux qualification and original archive audit

The [fresh Linux/Windows release workflow 44696085549](https://github.com/physicsvigilante/emfeeld/actions/runs/44696085549) has completed its **Linux** job SUCCESS on exact source test merge `61fc3f5b4f2ade099c53075a6094cd95e9ab59f3`. Linux original logs: **2,200 headless tests PASS and 107 real-PyVista tests PASS**, warnings as errors. Original Linux archive **14610868868** independently downloaded from GitHub Actions; original ZIP SHA256 **`a9e9fb473ef022511d1d90c30ed7ef9d3cd89af08159c4cd1f2c9cd861991c4a`**, **2,186 unique entries**, CRC clean, **173 integrity manifests**; **1,749 valid original file-hash references, zero missing, and exactly one deliberately corrupted negative-test reference** at `derived-001/G1/review-challenge-resealed-native/native/result.json`, correctly recorded as negative evidence rather than a new regression. The original `head-sha.txt` identifies the exact source-tested synthetic PR merge, not production `main`.

**At this addendum, Windows is still running real-PyVista regression and is NOT qualified.** The separate Windows job outcome and original artifact audit remain pending. Neither Linux nor author screenshots substitute for the independent R2 native reviewer challenge.
