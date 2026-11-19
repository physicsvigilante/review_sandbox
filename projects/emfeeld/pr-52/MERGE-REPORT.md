# PR #52 guarded integration — 2026-11-19

**MERGED; POSTMERGE RELEASE QUALIFICATION PENDING.** Do not confuse successful premerge author tests or independent scoped review with full actual-main qualification.

## Exact source and guarded merge

- [EMFEELD PR #52](https://github.com/physicsvigilante/emfeeld/pull/52) merge commit **`83ef4a1629e4e0f6e1742bb63019c1df45f326b8`**, Git tree **`f161a608853e5e180c459d68454e48c8fb734c39`**, precisely identical to the accepted corrected PR head **`43980b952e533483a36fedac2e95eab3df980f82`**.
- GitHub independently returned ordered parents **[old main `6bfeb2c314841ef861d7d66b67c894a6295b705e`, reviewed candidate `43980b95...`]**. The old main branch and PR base were checked immediately before merge, the PR head was checked using an `expected_head_sha` merge guard, and the final merged tree/main ref were verified afterwards. The PR was marked ready only after the exact-tree independent PASS.
- `main` now points to **`83ef4a16...`**. No opportunistic physics or browser code entered the merge; seven bounded modified/added paths vs the old main (visualization.py, viewer.py, documentation, and four tests).
- Independent **original review-01 and recheck** (historically CHANGES REQUESTED, preserved unchanged) found R52-A extreme finite-field directions and R52-B standalone recorded-frame validation. Both were corrected in presentation data only.
- Independent [review-02 PASS](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/emfeeld/pr-52/reviews/review-02-chat-b.md), reviewed blob **`881aee78a027b580f58463c8071a19865dacbe91`**, explicitly pins final exact head/tree and accepts *both* confined corrections. 37 new reviewer-authored tests, 40 existing author tests rerun separately, actual PyVista/VTK new extreme-vector glyphs and saved-frame interaction, plus ordinary-scene exact mesh/screenshot parity. Review preserves original first failures, limits and author-vs-review distinctions.

## Premerge author qualification

All five candidate workflows finished SUCCESS, full Linux and Windows each **1,857 headless +18 historical (one preexisting obsolete guard deselected) +56 actual-PyVista** with saved evidence stages. Original source/Ubuntu/Windows/viewer archives audited. The fixed tree is `f161a608...`, preview `d9e98328143b9a85c37bd77b5e36eeb256b86d85` and its ordered parents were checked. Both OS ZIPs retain all 2,186 original files, 173 integrity inventories, 1,750 hash references, the one known deliberate corrupt refusal fixture, all 82 ×35 implementation module receipt sets, E1 complete/G1 partial. Do not silently repair the corrupt negative or relabel it accepted.

## Fresh actual-main gate — outstanding, do not call released yet

Actual-main commit `83ef4a16...` automatically triggered:
- Full Linux/Windows [workflow 44460186412](https://github.com/physicsvigilante/emfeeld/actions/runs/44460186412);
- [Gauss lesson 44460186471](https://github.com/physicsvigilante/emfeeld/actions/runs/44460186471);
- [Real PyVista viewer 44460186414](https://github.com/physicsvigilante/emfeeld/actions/runs/44460186414);
- [Conductor cavity 44460186485](https://github.com/physicsvigilante/emfeeld/actions/runs/44460186485).

Each must be completed SUCCESS on the actual merge SHA. Original new archives must be downloaded/read-only audited for SHA, CRC, safe path, verified source and signed evidence; compare source-implementation identities and preserve existing deliberate negative evidence. Only after that can the PR52 release be marked completed and any downstream integration be based on the qualified actual main.

**Deferred:** PR51 dipole correction independently passed its own separate scoped R2-01 follow-up, but must be merged and fresh-release-qualified separately after PR52. PR53 prototype is draft, stacked against old PR52 head; no unreviewed retarget, broad merge or Three.js production release is implied. No manual Windows desktop, JEE teacher acceptance, all-DPI or arbitrary-scale physics certification.
