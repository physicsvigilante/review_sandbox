# PR #40 — final reliability-audit integration and release record

## Final disposition — all declared automated release gates closed

**2026-11-18 IST.** PR #40 is **merged and post-merge release-qualified** at actual main commit **`883242106e127c7b8f976660377b07a49aeded88`**. Canonical Git tree **`48baa0d760a2e99d0e953d6df5d7b999801d48cd`** exactly matches independently reviewed corrected feature **`f56ce83e791e3fcd3b1f17609c38a2f98a999c41`**. All declared pre-merge review/source and fresh actual-main Linux/Windows/viewer/original-archive gates have passed. This closes the bounded reliability audit, not a claim that all possible bugs or scientific limitations are eliminated.

## Final independent verdict and preserved history

The final [Chat B review-02](reviews/review-02-chat-b.md), blob **`03972595ed2f6c2e7292b6f190f4220e5d8e4eac`**, gives targeted **PASS** on the exact corrected source/tree. It reports **43 numerical/telemetry plus 45 evidence-preservation tests passing** (88 reviewer-owned cases), separately executed 1,642 headless tests, 18 historical cases and published-input replays. R2-01/02/03 are closed for the tested domain: large finite sphere potential, tiny-scale sphere/shell arithmetic, and consistent invalid-grid no-integration telemetry.

The report explicitly withdraws its initial unsupported review-02 publication and preserves the subsequent INSUFFICIENT EVIDENCE record. **Only its final verified-execution publication was used for integration.** Review-01 remains CHANGES REQUESTED on old `9fa09dec...`, blob `42dac92cbb62974fb182c3dc3d9107ea4372d525`; original source failures, reviewer harness failures and withdrawals remain in history. The reviewer's chat-only bundle was not available in this author workspace and was not claimed independently downloaded here. Reviewer-owned executions remain attributed to that report.

## Guarded integration

Before integration, live main/base **`066c94e4953c3ef29302c0bb6d0ee2f6cb8b8ca0`**, feature head, mergeability, successful exact-head workflows **44143094109 /44143094009 /44143094100**, and source-equivalent preview **`392ce9330322fd181116553063ae3ca5412134c1`** were rechecked. Preview tree matched the reviewed tree and its parents were [base, corrected feature]. All four retained original corrected-source ZIPs were rehashed/CRC-read and the 372-file source reconstructed again in this session; this corroboration was author-side, not additional independent review.

Under the owner's standing bounded integration direction, PR was marked ready and merged using **`expected_head_sha=f56ce83e791e3fcd3b1f17609c38a2f98a999c41`**. GitHub returned `merged=true`. Subsequent Git reads verified actual main `88324210...`, exact same tree, and ordered parents **[`066c94e4953c3ef29302c0bb6d0ee2f6cb8b8ca0`, `f56ce83e791e3fcd3b1f17609c38a2f98a999c41`]**. Technical reviewer PASS was not substituted for owner integration direction.

## Fresh actual-main release results

Both NEW `event=push` workflows on actual main completed **success**:

- [Linux/Windows clean-install 44154671635](https://github.com/physicsvigilante/emfeeld/actions/runs/44154671635), Ubuntu job134292073771 and Windows job134292073163: **1,642 headless +18 historical +33 real-PyVista passed per OS**, one explicitly deselected obsolete historical snapshot guard.
- [Separate real-PyVista 44154671754](https://github.com/physicsvigilante/emfeeld/actions/runs/44154671754), job134292074432: **9 offscreen cases PASS, 17 original PNG receipts verified**, 1,642 headless passes; full visual inspection remains PENDING.

Original new artifacts were downloaded and directly audited, not substituted with PR-preview evidence:

| Artifact | ID | Whole ZIP SHA256 |
|---|---:|---|
| Ubuntu | 14360198789 | `c2301d9acde27164f5cc6a55f8457fdc12c841665648a65dc7ec5a0fc226cb5f` |
| Windows | 14360523709 | `b4bb0ad3bf47d1b753377caab4e9d3d79ebe67bd229157a058a0adfa63807663` |
| Viewer | 14360512873 | `5dc8ffe85ada69b480915252964a9cafc411dcc77279bb4bf5619099c13a23b1` |

**[Full post-merge archive audit](POSTMERGE-ARCHIVE-AUDIT-01.md)** records per-OS original logs, source/native receipts, environment differences and exact audit boundaries. Each OS ZIP has 2,186 safe unique CRC-clean entries. Viewer ZIP has 22, and its embedded TAR reconstructs 372 tracked files to the exact merged tree. Supplemental actual merged-source local replay independently ran 1,642 headless, 18 historical and all V6/discovery/physics-demo cases successfully.

Per OS, the deep audit checked 173 integrity inventories /1,750 referenced hashes and exact inventory membership: **172 intact and one deliberately invalid rejection fixture**. The child at `derived-001/G1/review-challenge-resealed-native/native/integrity.json` remains invalid with original negative magnitude -2.5, and downstream unavailable/null rejection. It is explicitly **EXPECTED_NEGATIVE_NOT_VALIDATED_EVIDENCE**, not repaired or counted intact. All 30 engine source files in each of 105 complete receipt maps match (Windows CRLF accounted). Repeated maps are not separate experiments.

Original source-first developer/NASA measurements retain their frozen input/receipt/native bindings and limited coverage claims. Physics demonstration retains 17 native observations and 64 analytic checks; separate mathematical expressions corroborated all 17 values. E1 remains complete, G1 partial, with signed comparisons recomputed from original operands and unknown operands kept unavailable/null.

## Compatibility and limits

No new physical law or solver tolerance was introduced. Implementation hashes legitimately change: preserve old source-pinned studies/environments or replay unchanged inputs into new outputs; never rewrite old receipts to force compatibility. This release does not certify every extreme numerical scale, malicious concurrent filesystem safety, arbitrary prose interpretation, authenticated unseen teacher inputs, classroom usefulness, full visual inspection or manual Windows interaction. Genuine independent question/withheld-judge work remains Issue #36.

Earlier pending versions of this current release record are retained in Git history; independent review files were not edited during release closure.