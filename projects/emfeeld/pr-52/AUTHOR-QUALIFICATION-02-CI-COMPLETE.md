# PR52 — current-head hosted completion and OS archive audit

2026-11-18. **All five hosted workflows PASS on corrected head3ea61a4d79d211009fb0b038fa56b7cef1e1e38c. Independent review remains pending; draft/unmerged.** Tree49afa15dbd3c1e9b15d0a41719eea7bdabd0540a. This addendum closes the current-source CI/OS-archive checkpoint, not a merge or actual-main release gate.

## Exact current-source tests

Full Linux/Windows44347108199 completed SUCCESS. Both jobs passed **1,833 headless +18 historical (one preexisting obsolete all-file guard deselected) +54 real-PyVista**, then all downstream evidence and uploads. Source44347108397, viewer44347108249, Gauss44347108404 and cavity44347108222 also completed SUCCESS. These are live hosted outcomes, not inference from previous source. Full local suites on the same tree separately passed the same counts. Focused cases overlap those totals.

## Original OS payloads audited read-only

| OS | Artifact ID | Bytes | Whole original ZIP SHA256 |
|---|---:|---:|---|
| Ubuntu |14446474306|9871384|3351d5a4471779fe28706b494b54a8f9b043f4afa31bf3416fbe65935d3c3768|
| Windows |14448317667|9727747|ddfd1b003018a74932ea09fd9b5daddd9e100ef91c592e0ea919c8dc3f4a51b3|

Each ZIP was downloaded from the original artifact endpoint and checked against GitHub's digest. CRC,2186 safe unique members,original preview head marker d73eb8c5c00bcd1d6352c049057d66c918fb2f5b and original test counts passed. Each contains173 integrity inventories/1750 referenced hashes:1749 match and exactly one prior deliberate corrupted-negative fixture remains invalid and separately retained. It is not counted as valid evidence. All82 implementation-receipt sets per OS match35 current source modules (Windows checkout CRLF handled in memory only). E1 remains complete/G1 partial; signed evidence/view output logs are present.

Fresh original source artifact14447215687 and its398-file TAR were separately byte-checked against the local exact tree, as recorded in report01. The specialized workflow success statuses were checked; this addendum does not assert newly downloaded payload audits for every Gauss/cavity ZIP. The audited payloads here are the current source and both full OS archives. Prior-hosted screenshot parity is separately scoped historical evidence, not silently upgraded to new image testing.

The export-isolation first failures, old ba5e7a1e source and its own green CI/archives remain preserved. No numerical source, tolerance, field sample, trajectory or specialized viewer was changed in the correction.

## Gate

Proceed to the prepared independent focused architecture/meaning-preservation review. The author cannot issue that verdict. Do not merge or call the feature released from this report. Accepted independent review, guarded exact-head integration and new actual-main CI/archive audits remain required. Main remains6bfeb2c314841ef861d7d66b67c894a6295b705e; the separate stacked browser prototype does not bypass these gates.
