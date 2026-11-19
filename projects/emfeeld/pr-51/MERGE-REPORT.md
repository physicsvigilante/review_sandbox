# PR #51 — guarded JEE electric-dipole integration

**2026-11-19. MERGED; ACTUAL-MAIN RELEASE QUALIFICATION PENDING.**

## Source pins and approval gates

- GitHub merge commit: d3de5d7165945630e1a3979afa7252132d5efe5e, actual main ref verified.
- Merged exact Git tree: **1ec88afdc7a3d057a21e39a52769c190fd1577f2**, exactly matching the independently assembled/tested PR52-main plus PR51 additive preview (410 tracked source files).
- Verified GitHub ordered merge parents: [fresh fully release-qualified renderer-neutral main 83ef4a1629e4e0f6e1742bb63019c1df45f326b8, independently reviewed dipole head 68f1b170d90e257082f23ce33d427b037a962435]. Actual PR head was guarded by expected_head_sha and live base/main checked prior to merge.
- [Original independent R2-01 review-01](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/emfeeld/pr-51/reviews/review-01-chat-b.md) historically CHANGES REQUESTED due to falsely large fixed-size torque cue on rounded-alignment presets; physical finite-pair equations were accepted.
- [Independent R2-01 follow-up review-02](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/emfeeld/pr-51/reviews/review-02-chat-b.md), original blob e4b3f0711debf24950bd71e883748cbc22a681c6, gave PASS for the exact corrected candidate. [Supplementary independent review](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/emfeeld/pr-51/reviews/review-02-chat-b-independent-recheck-20261118.md) separately passed. No new unreviewed physics edits were made.
- Ten strictly additive dipole paths vs now-qualified main. The PyVista general viewer stays the already-qualified PR52 version. All original non-dipole physics laws/integrators, recorded studies and old evidence unchanged.

## Premerge qualification — does not substitute for new actual-main release

- Exact-source PR51 author CI all six workflows success on 68f1b170; per OS 1,894 headless + 18 historical (one obsolete freeze guard deselected) +68 actual PyVista, 89 overlapping focused dipole tests, 14 real-PyVista dipole scenes; original source, dipole, Linux/Windows ZIPs audited. Independent review explicitly separated author tests from reviewer-owned checks.
- Isolated local combined-source compatibility preview (after PR52 release): ten additive PR51 files over 400-file exact PR52 main, Git tree 1ec88afd...; **1,929 full headless +73 full real-PyVista tests passed with warnings as errors**, plus 107 focused headless and 22 focused PyVista overlapping cases. This was an author-only preview, not a production merge or independent review. Detailed record: https://github.com/physicsvigilante/review_sandbox/blob/main/projects/emfeeld/pr-51/PR52-MAIN-COMPATIBILITY-PREFLIGHT-01.md

## Mandatory actual-main release gate

All five fresh workflows started automatically on actual merge d3de5d71... . Do NOT claim release completed from prior PR51 or PR52 green runs.

| Actual-main workflow | GitHub Actions run ID |
| --- | ---: |
| Full clean-install Linux and Windows | 44462919758 |
| JEE dipole dedicated qualification | 44462919778 |
| Real PyVista viewer | 44462919691 |
| JEE Gauss law | 44462919793 |
| JEE conductor cavity | 44462919872 |

Require each completed SUCCESS and original newly uploaded artifact audits: whole SHA metadata, CRC/safe/unique entries, source 410-file tree and current module hashes (37 modules after dipole), saved physical states and screenshot receipts, deliberately corrupt negative refusal preserved invalid, retained E1/G1 state, Linux and Windows full suite logs. Only then close Issue50. Manual Windows human operation, all-DPI rendering, teacher acceptance, blind-JEE success, dynamic free-rotation and general Maxwell support are not asserted.

PR53 browser prototype remains separate draft, based on an older PR52 development ancestor. Do not merge/retarget silently or claim it has reviewed dipole/browser parity.