# SIM_HEAT PR55 — source-only unfamiliar composition, independent R2 pending

**Status: `PUBLISHED-EXACT-HEAD; HOSTED-CI-PASS; AWAITING-INDEPENDENT-R2; DRAFT-UNMERGED; NO-NATIVE-AUTHORIZATION`.**

[Source PR55](https://github.com/physicsvigilante/sim_heat/pull/55), branch `product/novel-source-preview`, candidate SHA **`0b15c02e5c3c60af32224e0ec5f29a2920927d5a`**, Git tree **`1be95f7dc60bd729d691e437c06f7914f0e045e4`**, base exact `main` **`0278b79b4da1c3196edca7903189713e0482f3f6`**, tree `c73f86e58be8b9eb55756432aae064f00719487f`. GitHub's direct diff confirms 14 added paths, no modifications/deletions, one commit. The previously supplied publication package was actually recovered; Git patch SHA-256 `e3f244565031f5bdd79e0da2612c47ff891bf3c4f012323d5ca38afa773109bd` was verified; clean local `git apply --index` yielded the exact expected tree, and each created GitHub blob had the identical local Git blob SHA-1. No hand-authored reconstruction was substituted.

**Scope:** `TEACH_SPLIT3`, a developer-authored, illustrative unfamiliar supported composition (3 finite bodies, 2 fixed-temperature boundaries, 7 rods, an ownerless ideal junction, shortcut and 4 source-only observation requests). The new `h1/source_preview.py` emits `sim_heat.viewer.admitted_source/1` with source-linked SI inputs/attributions, logical ports/nodes and requests `not_computed`. New generic browser shows source-only topology and refuses malformed/forged imports while preventing stale out-of-order file reads from restoring refused state. This does **not** compute any native temperature, flow, trajectory or geometry and is not blind author transfer.

## Verified exact-head evidence

[GitHub Actions **44257880331**](https://github.com/physicsvigilante/sim_heat/actions/runs/44257880331), job `134643839279`: SUCCESS (source-diff guards, offline suites, archived original replay and real Chromium smoke).

[Artifact **14407310945**](https://github.com/physicsvigilante/sim_heat/actions/runs/44257880331/artifacts/14407310945): **7,438,185 bytes**, full SHA-256 **`ab328892f0c5796987e091e447c1d1fb78732c7bb6c70f6378ab409aed9ed1b2`**, downloaded and rehashed by Chat A, **44/44 distinct CRC-valid entries**. `head-sha.txt`, `head-tree.txt` and `source-diff.txt` match source PR. No unobserved CI status is claimed.

- H1 152 PASS; analytical 4 PASS; viewer/adapter 62 PASS +1 existing optional SKIP; product/source preview 19 PASS; Node 39 PASS = **276 unique unit passes, one optional skip, zero failures**. Same suite also ran locally against verified patch source; those outcomes are overlapping rather than additive.
- **All six original archived diagnostic case bundles BYTE_IDENTICAL** (D1, D2, DEV_BRIDGE, TEACH_RING4, S1, D2_K2), `nativeExecutedByReplay=false`. Published D2/D2_K2 comparison output is byte-identical. Source-only TEACH_SPLIT3 regeneration also byte-identical to the new source-only data file.
- Hosted real Chromium: original historical explorer PASS, root entry navigation PASS, **new source-only viewer desktop/mobile PASS**, including source/requests statuses, a second D2 topology, refused forged native flag with old graph/request clearing, and both orderings of stale asynchronous imports. Existing old local Chromium HTTP navigation was environment-blocked, **not** counted as local PASS. Minor favicon HTTP 404 is separate from zero JS page errors.
- Workflow and tests did **not** install/query/launch OpenModelica, run the native batch executor or regenerate original adopted references. Existing six public cases remain `diagnostic_only` and `nativeQualified=false`. Source-only requests remain `not_computed`.

**Preservation:** original `h1/model.py`, `h1/study.py`, model library, numerical checking sources/thresholds, native runner, all historical C1 artifacts, original `viewer/network` data/catalog/comparison and prior failure records unchanged. Frozen C1 original reference precision 80× versus required 100× and cross-host original saved-reference seal reproduction still FAIL; its nine original public native requests remain uncomputed. No new native authorization or owner-signature trust root exists.

PR54 (`product/authoring-guide`, reviewed head `8f6ef1d0f8d0ebd938620c5694bc11856a5c9e7e`) remains a **separate open/draft unmerged** candidate, and its files were not included. Main remains at PR53 merge `0278b79...`.

## Next gate

The complete [independent R2 REQUEST](REQUEST.md) and [ready Chat B prompt](REVIEWER-PROMPT-01.md) are published. **Only Chat B in a separate conversation** may create NEW `reviews/review-01-chat-b.md` with verdict SCOPED PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE on this exact candidate. Source-preview provenance, untrusted imports, observable statuses and races warrant R2; this is not a whole-project audit or new numerical qualification. No merge, deployment or native execution follows automatically from any verdict. New source changes require a new SHA and exact-head CI before review.
