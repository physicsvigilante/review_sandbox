# PR #40 — actual-main original archive audit 01

## Current disposition

**2026-11-18 IST: actual-main viewer and Ubuntu qualification PASS; Windows final workflow/archive audit PENDING.** This is an author release audit, not a new independent R2 review or a general physics/teaching certification. Do not close Issue #39 until both OS gates and their new original archives pass.

Actual merged main **`883242106e127c7b8f976660377b07a49aeded88`**, canonical tree **`48baa0d760a2e99d0e953d6df5d7b999801d48cd`**, equals the exact final reviewed candidate. Merge parents are `[066c94e4953c3ef29302c0bb6d0ee2f6cb8b8ca0, f56ce83e791e3fcd3b1f17609c38a2f98a999c41]`. Final independent [review-02](reviews/review-02-chat-b.md), blob `03972595ed2f6c2e7292b6f190f4220e5d8e4eac`, reports targeted PASS with 88 reviewer-owned tests. Its explicitly withdrawn initial publication is not qualifying evidence; review-01's old-source failures remain preserved. The reviewer chat-only bundle was not available in this author workspace and was not claimed rehashed here.

## New original artifacts actually audited

| Artifact | ID | Whole original ZIP SHA256 | State |
|---|---:|---|---|
| Main-push viewer | 14360512873 | `5dc8ffe85ada69b480915252964a9cafc411dcc77279bb4bf5619099c13a23b1` | PASS, 22 CRC-clean unique safe entries |
| Main-push Ubuntu | 14360198789 | `c2301d9acde27164f5cc6a55f8457fdc12c841665648a65dc7ec5a0fc226cb5f` | PASS, 2,186 CRC-clean unique safe entries |
| Main-push Windows | Not yet available at first publication | Not yet audited | PENDING |

Original GitHub artifact digests were compared to whole downloaded ZIP bytes. Every member was read for CRC and checked for unsafe/absolute/traversal paths, links, exact and casefold duplicate names. These are NEW actual-main artifacts, not old PR-preview ZIPs.

### Viewer/source

[Actual-main viewer workflow 44154671754](https://github.com/physicsvigilante/emfeeld/actions/runs/44154671754), job 134292074432, completed success on `88324210...`. Original report records **9 offscreen cases PASS**, **17 original PNG SHA256 receipts** verified against valid PNG bytes, and **1,642 headless tests passed** in its original log. Original report still says visual inspection PENDING; no manual Windows/classroom claim follows.

Embedded source TAR SHA256 **`29b5ad4f6a92944c339ae0b3f852e7eea2a3865e223db1444a6e44a971bd2d14`**. Safe extraction and a fresh Git index reconstruct **372 tracked files** and exact tree `48baa0d7...`. Actual source identity, not raw equality to an earlier TAR, is the source gate.

### Ubuntu original release

[Actual-main clean-install workflow 44154671635](https://github.com/physicsvigilante/emfeeld/actions/runs/44154671635), Ubuntu job 134292073771, completed success. Original `head-sha.txt` equals actual merged main. Original logs: **1,642 headless PASS; 18 historical PASS with one explicitly deselected obsolete snapshot guard; 33 real-PyVista PASS**.

Read-only audit independently checked:

- **173 integrity inventories and 1,750 referenced file hashes:** 172 inventories intact. Exactly one intentionally invalid child remains at `derived-001/G1/review-challenge-resealed-native/native/integrity.json -> result.json`. Its field magnitude is deliberately -2.5; downstream result remains partial with unavailable/null and `operand_unavailable`. It is labeled **EXPECTED_NEGATIVE_NOT_VALIDATED_EVIDENCE**, not repaired or counted intact. ZIP CRC cleanliness does not validate this deliberately corrupted scientific fixture.
- **All 30 engine files in 105 complete source maps** (100 implementation maps, five engine maps) match original source bytes. Repeated maps are not independent runs.
- Both developer-gravity and public NASA source-first question/receipt/packet/native/assessment/state chains match original tracked source bytes and their raw hashes. Requested IDs, quantities, units and actual saved contexts match; native counts are **5/5** and **1/1 ok** respectively. Interpretation remains not_verified; independent physics, educational usefulness and textbook completeness remain not_evaluated. The NASA exercise remains non-blind.
- Physics demonstration retains **17 native ok values and 64/64 recorded analytic checks**. All 17 values were also recomputed with separately written constant-acceleration, uniform-field/potential and energy expressions in the author audit, without calling engine functions for the reference.
- Signed differences were recomputed from original left/right native operands with raw packet/run and readout/comparison receipt checks: E1 has **10 ok rows**, G1 has **14 ok plus two unavailable/null rows across comparisons**; the selected G1 readout retains **7 ok plus one unavailable/null**. E1 global complete and G1 global partial remain distinct.

Original Ubuntu native report hashes: developer `bf11cc7a6abd598bba0ae1746ca934eaf2ebc8c383aff79373676d5b4b06b947`; NASA `ab928b94cbb930d8589352a1ba180f81e4d7dda67997b57473bc35c05242ec20`. NASA speed `43484.58452036887 m/s`. Per-OS equality will not be assumed.

## Supplemental actual merged-source local execution

From the new viewer TAR, exact tree unchanged, Linux Python 3.13.5 / NumPy 2.3.5 / SciPy 1.17.0 / pytest 9.0.2:

- `PYTHONPATH=<absolute src>:<absolute tests> PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -W error -m pytest -q`: **1,642 passed in 131.15 s** in retained original log.
- Historical behavioral suite: **18 passed, one obsolete guard deselected**, exit 0.
- Exact published-input V6 replay: **10 cases**, discovery: **two cases**, physics demonstration: **one case /17 native observations /64 checks**, all passed into new output directories, exit 0.

The first streaming-container invocation was rejected by the tool before a test result existed. Ordinary subprocess execution was then used, with that tooling failure retained in execution notes. No product tests failed in these subsequent executions. Author local tests are distinct from reviewer-owned cases and original hosted tests; they are not added to each other's counts.

Original release native reports record NumPy 2.5.5 / SciPy 1.18.1; local and separate-viewer versions above differ. Record environments as observed, not as an assumed identical dependency matrix or blanket compatibility certification.

## Remaining boundary

Windows final release and original archive audit remain required. After both OS gates pass, update this current disposition and close release tracking. Preserve historical implementation-pinned studies and original receipts; replay into new outputs rather than resealing old evidence. General extreme-scale correctness, malicious concurrent-filesystem security, unseen teacher questions, arbitrary-language interpretation and human desktop usefulness remain outside this release verdict.