# PR #47 — actual-main qualification checkpoint 01

2026-11-18. **PARTIAL RELEASE CHECKPOINT, not full release completion.** This supplements [MERGE-REPORT.md](MERGE-REPORT.md); the independent scoped PASS and guarded integration are complete, but the full Linux/Windows release workflow and original OS archive audits remain pending at this entry.

## Exact actual-main identity

Merged main commit `f6a078354ec2a657ca010c5c92ea578a0f55a2ad`; canonical Git tree `65935bb395552d3dfb466a6e48d03230f18b6b66`, identical to reviewed candidate `fcf9fede87ccd37597d0ba8c9b9013ee99b764f0`. Ordered actual parents remain [qualified base `aeea3fedb00de4e20304d1f88aa038f3fac1e99e`, reviewed candidate]. All new records below are push runs on actual main, not the former PR merge preview.

## Three main-push jobs completed and original archives audited

| Scope | Run / job | Original artifact | Whole ZIP SHA256 |
|---|---|---|---|
| Gauss lesson | 44296944965 / 134776325004 | 14425020701 | `aacb458f5f2998d7b1d35d05ab286c111668f58ce8602e121a0573d77c040569` |
| Conductor lesson | 44296944750 / 134776327445 | 14424161404 | `b3bc45e55b1cf4dcd973fe28c7efedc0521048b91c62bdcd3cb0b0aefdbff9ec` |
| Existing viewer | 44296945003 / 134776325257 | 14423518406 | `031b8968c51f30f464fb3a4d0a05624606195172253121d4da2b055097560589` |

Live job reads established completed/success for all three. Original downloaded ZIP bytes match GitHub server digests; CRC, unique relative paths, no traversal and no symlink members checked. Their source TARs all have SHA256 `95221437094e7d1b06e5e142e93522f917d7f1f780f32779e0ca50b3c0340d49`, actual merge SHA in the Git archive comment, and all391 source files byte-identical to the reviewed source. The original reviewed TAR was separately reconstructed with `git add -f . && git write-tree` to the canonical tree above. Different premerge/main TAR hashes reflect commit metadata; per-file source is unchanged.

- **Gauss:** 83 overlapping focused tests passed; eight actual scenes;71 ZIP members;8 integrity inventories/56 matching references;34 implementation module hashes per scene matched. Original-input bytes, current lesson state, screenshot digests and E-dot-normal arrays checked. Central face values equal q/(6 epsilon0); off-centre face values differ but retain exact total; exterior/opposite-sign cases retain signed cancellation. Boundary scene has null exact total and no stale E array. Sphere refinement reduces the displayed unrenormalized sample-minus-exact discrepancy for this archived example, not a global convergence proof.
- **Conductor:** 71 focused tests passed; six scenes;49 ZIP members;6 integrity inventories/36 matching references;34 implementation receipts per scene and current-state/image hashes checked.
- **Viewer:** 1,783 headless tests passed in this distinct workflow; nine legacy cases and17 original PNG receipts matched;22 ZIP members. Python3.13.5, NumPy2.3.5, SciPy1.17.0, PyVista0.48.4, VTK9.6.2, pytest9.0.2 recorded. Do not conflate this successful Ubuntu viewer job with completion of the separate full OS workflow.

Author visually inspected contact sheets assembled from the original new Gauss and conductor screenshots. The Gauss images show actual rotated cube edges, spheres without an auxiliary cube, clear boundary unavailable state without stale colors/arrows, and the expected retained control panels. These are author visual checks of CI images, not new local rendering, reviewer-owned evidence, manual Windows interaction or teacher acceptance. The review's small-window and near-surface-caution follow-ups are recorded separately as emfeeld Issue48; source was not modified for them during this release.

## Remaining full OS gate

Full main-push workflow **44296944746**: Ubuntu job **134776324762**, Windows job **134776325189**. At the latest observed checkpoint, both jobs had passed headless, historical, published-input, demonstration, source-first/public-source and representative-scene stages; both were running the real-PyVista test stage. Neither full job nor its unavailable final OS archive is declared passed here. Remaining native/evidence workflows and artifact collection must complete, then original new Ubuntu/Windows ZIPs must be downloaded and audited against actual main. **Issue46 stays open.**

All prior premerge archives, independent-review limitations and historical failures remain unchanged. No new human acceptance, blind JEE performance or arbitrary-scale numerical guarantee follows from this checkpoint.
