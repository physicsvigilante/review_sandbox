# PR #40 — reliability audit integration and release record

## Current disposition — merged, post-merge qualification pending

**2026-11-18 IST.** PR #40 was merged with GitHub's expected-head guard into actual main commit **`883242106e127c7b8f976660377b07a49aeded88`**. Fresh actual-main CI and original post-merge archive audits are separate requirements and were not complete when this record was first published. Issue #39 remains release tracking; no full release closure is claimed yet.

## Independent verdict and source identity

The final [independent Chat B review-02](reviews/review-02-chat-b.md), blob **`03972595ed2f6c2e7292b6f190f4220e5d8e4eac`**, gives targeted PASS on corrected head **`f56ce83e791e3fcd3b1f17609c38a2f98a999c41`**, tree **`48baa0d760a2e99d0e953d6df5d7b999801d48cd`**. It reports 43 reviewer-owned numerical/telemetry tests and 45 preservation tests passing, plus its separately executed full 1,642-test suite, 18 historical cases and published-input replays. It closes R2-01/02/03 within the tested domain, not every possible magnitude/geometry or general scientific correctness.

The report explicitly withdraws an initial unsupported review-02 publication, with its interim INSUFFICIENT EVIDENCE retained in Git history. **Only the final verified-execution report above is used for integration.** Review-01 remains CHANGES REQUESTED on old `9fa09dec...`, blob `42dac92cbb62974fb182c3dc3d9107ea4372d525`. No earlier failure or withdrawal was overwritten. The reviewer's final chat evidence bundle is not present in this author execution workspace and is not claimed downloaded here; its reported tests remain attributed to the independent reviewer.

Live pre-merge checks re-read exact PR head/base/mergeability and successful workflows **44143094109** (Linux/Windows), **44143094009** (viewer), **44143094100** (source). Source-equivalent preview `392ce9330322fd181116553063ae3ca5412134c1` had the same corrected tree and ordered parents `[066c94e4953c3ef29302c0bb6d0ee2f6cb8b8ca0, f56ce83e791e3fcd3b1f17609c38a2f98a999c41]`. All four retained original corrected-source ZIPs were rehashed/CRC-read in this session, and their 372-file source tree reconstructed again to the exact reviewed tree. This corroboration is author-side, not additional independent review.

Under the owner's standing bounded integration direction, PR was marked ready and merged with **`expected_head_sha=f56ce83e791e3fcd3b1f17609c38a2f98a999c41`**. GitHub returned `merged=true`, actual commit `883242106e127c7b8f976660377b07a49aeded88`. Subsequent Git API reads verified actual main points there, its tree is **`48baa0d760a2e99d0e953d6df5d7b999801d48cd`**, and ordered parents are exactly the qualified prior main and reviewed feature above. Reviewer PASS is a technical verdict; it was not treated as owner merge permission.

## Fresh actual-main requirements

New actual `push` workflows on `883242106e127c7b8f976660377b07a49aeded88`:

- [Linux/Windows clean-install 44154671635](https://github.com/physicsvigilante/emfeeld/actions/runs/44154671635): in progress at first observation.
- [Separate real-PyVista 44154671754](https://github.com/physicsvigilante/emfeeld/actions/runs/44154671754): in progress at first observation.

Required before closure: final job conclusions, new original Ubuntu/Windows/viewer ZIP downloads and whole-byte digest/CRC/path checks; actual-main source identity, test logs, source-first question/packet/native receipts, 30 engine modules, previous physics demonstration and signed ensemble results. Old PR-preview archives cannot substitute for these new main-push artifacts.

The review identified an intentionally corrupted child integrity inventory at `derived-001/G1/review-challenge-resealed-native/native/integrity.json`. This negative fixture must remain explicitly invalid and its downstream outcome rejected/unavailable; it must not be silently repaired, counted as intact evidence, or described as a release defect merely because its intended negative check fires. ZIP CRC integrity and validity of every scientific fixture are different claims.

## Compatibility and limits

Implementation hashes legitimately changed. Preserve original implementation-pinned studies and environments, or replay unchanged inputs into new outputs; do not rewrite old receipts. The correction adds no new physical law or solver tolerance. It does not establish arbitrary-scale accuracy, malicious concurrent-filesystem safety, blind question interpretation, teacher acceptance, full visual inspection or manual Windows interaction. Issue #36 remains separate.

This initial pending record is retained in Git history; subsequent release disposition must be based on actual new outputs.