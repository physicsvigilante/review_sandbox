# PR #40 — final actual-main original archive audit 01

## Final disposition

**2026-11-18 IST: all declared automated post-merge release and original-archive gates PASS on both operating systems.** This is an author release audit, not a new independent R2 verdict, a proof that every defect is absent, or general physics/teaching certification. Earlier pending versions of this report remain in Git history.

Actual merged main **`883242106e127c7b8f976660377b07a49aeded88`**, canonical tree **`48baa0d760a2e99d0e953d6df5d7b999801d48cd`**, equals the exact final reviewed candidate. Ordered merge parents are `[066c94e4953c3ef29302c0bb6d0ee2f6cb8b8ca0, f56ce83e791e3fcd3b1f17609c38a2f98a999c41]`. Final independent [review-02](reviews/review-02-chat-b.md), blob `03972595ed2f6c2e7292b6f190f4220e5d8e4eac`, reports targeted PASS with 88 reviewer-owned tests. Its explicitly withdrawn initial publication is not qualifying evidence; review-01's old-source failures remain preserved. The reviewer chat-only bundle was unavailable in this author workspace and was not claimed downloaded or rehashed here.

## Fresh actual-main workflow conclusions

[Actual-main clean-install workflow 44154671635](https://github.com/physicsvigilante/emfeeld/actions/runs/44154671635), event `push`, head `883242106e127c7b8f976660377b07a49aeded88`, completed **success**. Both Ubuntu job **134292073771** and Windows job **134292073163** completed success. Original archived logs on EACH OS show **1,642 headless passed; 18 historical behavioral passed with one explicitly deselected obsolete snapshot guard; 33 real-PyVista passed**. New correction tests are already included in the 1,642 total.

[Actual-main viewer workflow 44154671754](https://github.com/physicsvigilante/emfeeld/actions/runs/44154671754), same event and head, job **134292074432**, completed **success**. These are new actual-main runs, not relabeled PR-preview qualification.

## Three new original artifacts actually audited

| Artifact | GitHub artifact ID | Whole original ZIP SHA256 | Audit |
|---|---:|---|---|
| Main-push viewer | 14360512873 | `5dc8ffe85ada69b480915252964a9cafc411dcc77279bb4bf5619099c13a23b1` | PASS; 22 CRC-clean unique safe entries |
| Main-push Ubuntu | 14360198789 | `c2301d9acde27164f5cc6a55f8457fdc12c841665648a65dc7ec5a0fc226cb5f` | PASS; 2,186 CRC-clean unique safe entries |
| Main-push Windows | 14360523709 | `b4bb0ad3bf47d1b753377caab4e9d3d79ebe67bd229157a058a0adfa63807663` | PASS; 2,186 CRC-clean unique safe entries |

Original GitHub artifact digests were compared to whole downloaded ZIP bytes. Every member was decompressed/read for CRC and checked for unsafe absolute/traversal paths, links, exact duplicates and casefold duplicate names. Both OS original `head-sha.txt` files equal actual merged main.

### Viewer and exact source

Original viewer report records **9 offscreen cases PASS**, **17 PNG SHA256 receipts** verified against valid original PNG bytes, and **1,642 headless passes** in its original log. The original `visual_inspection=PENDING` label remains unchanged: automated offscreen execution and image checksums do not establish human visual or manual Windows/classroom acceptance.

Embedded source TAR SHA256 **`29b5ad4f6a92944c339ae0b3f852e7eea2a3865e223db1444a6e44a971bd2d14`**. Safe extraction and a fresh Git index reconstruct **372 tracked files** and exact tree **`48baa0d760a2e99d0e953d6df5d7b999801d48cd`**. After all supplemental local tests, tracked source remained unchanged and `git write-tree` again returned this tree. Actual source identity, not raw equality to an earlier TAR, is the source gate.

## Read-only deep audit of EACH original OS release ZIP

### Inventories and expected negative fixture

Checked **173 integrity inventories and 1,750 referenced hashes per OS**, including exact recursive membership: no unlisted or missing files inside inventoried roots. **172 inventories are intact.** Exactly one intentionally invalid child remains at:

`derived-001/G1/review-challenge-resealed-native/native/integrity.json -> result.json`

The fixture deliberately sets a field magnitude to **-2.5** and reseals only its parent. Its downstream result remains partial with unavailable/null and `operand_unavailable`. It is labeled **EXPECTED_NEGATIVE_NOT_VALIDATED_EVIDENCE**, not repaired, silently waived, or counted as intact evidence. ZIP CRC cleanliness is distinct from scientific/inventory validity of an intentionally corrupted test fixture.

### Source receipts

Checked **all 30 engine modules in 105 complete source maps per OS**: 100 `implementation_sha256` and five `engine_sha256` maps. These repeated maps are not 105 independent runs. Ubuntu maps match canonical LF source bytes; Windows maps match standard CRLF checkout translation computed in memory. Original source, ZIP bytes and stored receipts were not normalized or rewritten.

### Original source-first chains and native measurements

Both developer-gravity and public NASA lock/question/receipt/packet/native/assessment/state chains match the original tracked question and packet bytes. Rehashed raw source and native files against their own assessment bindings, separately from canonical packet-object hashes. Requested IDs, quantities, units and actual physical saved contexts match. Native counts are **5/5** and **1/1 ok** respectively; execution is complete. Interpretation remains **not_verified**; independent physics, educational usefulness and textbook completeness remain **not_evaluated**. The NASA exercise remains explicitly non-blind.

| Raw binding | Developer gravity | Public NASA |
|---|---|---|
| Question SHA256 | `36f56dcc11d6347a1db47adfb103b16472a8e1270641869f52c7220bd086a361` | `cd797751a84d86caa57c2024620215895c1414169c6682b96933e4b4cf25cc23` |
| Packet SHA256 | `6fe25bf6c738ee13fa837793414b343feeb53116737bcfafcf19c56c36adac5d` | `f86211065ec99e3e82181de256d321a6ebb054f9b397440996529a3ec6ccfeda` |
| Actual Ubuntu native SHA256 | `bf11cc7a6abd598bba0ae1746ca934eaf2ebc8c383aff79373676d5b4b06b947` | `ab928b94cbb930d8589352a1ba180f81e4d7dda67997b57473bc35c05242ec20` |
| Actual Windows native SHA256 | `bf11cc7a6abd598bba0ae1746ca934eaf2ebc8c383aff79373676d5b4b06b947` | `ab928b94cbb930d8589352a1ba180f81e4d7dda67997b57473bc35c05242ec20` |

In THIS actual-main run the two OS native files happen to be byte-identical; that equality was observed, not required. Earlier PR-head OS-native differences remain accurately recorded in their own original reports. NASA speed is **43,484.58452036887 m/s**, true saved index20/time `3.2195317385273e-8 s`, with external unit conversion distinct from the native SI measurement. Developer final sample20/time2s contexts and uniform-acceleration values were separately checked.

### Physics demonstration and signed comparisons

Each original OS physics demonstration retains **17 native ok observations and 64/64 recorded analytic checks**. All 17 values were additionally recomputed from separately written constant-acceleration, uniform-field/potential and energy expressions in this author audit, without calling engine functions for the reference. This is same-author mathematical corroboration, not a new independent scientific verdict.

Signed right-minus-left differences were recomputed from original native operands, with raw packet/run and readout/comparison receipt checks. **E1:** ten successful comparison/readout rows and global complete. **G1:** fourteen successful plus two unavailable/null rows across retained comparison files; its selected readout has seven successful plus one unavailable/null row and global partial. Unknown operands are not silently zero-filled or promoted to complete.

## Supplemental actual merged-source local execution

From the new viewer TAR, exact source tree unchanged, Linux Python **3.13.5**, NumPy **2.3.5**, SciPy **1.17.0**, pytest **9.0.2**:

- `PYTHONPATH=<absolute src>:<absolute tests> PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -W error -m pytest -q`: **1,642 passed in 131.15 s**, retained original complete log.
- Historical behavioral suite: **18 passed, one obsolete guard deselected**, exit0.
- Exact published-input V6: **ten cases**, discovery: **two cases**, physics demonstration: **one case /17 native observations /64 checks**; all passed into new outputs, exit0.

The initial streaming-container invocation was rejected by the tool before any test result existed; ordinary subprocess execution was then used, and the tooling failure remains recorded. No product tests failed in these subsequent executions. Author-local, original hosted and reviewer-owned scopes are distinct and not added to each other's counts.

Original release native reports record NumPy **2.5.5** / SciPy **1.18.1**; local and separate-viewer environments differ. Record these as observed environments, not an assumed identical dependency matrix or blanket compatibility certification. Separate viewer records PyVista0.48.4 / VTK9.6.2; local real-PyVista was not executed.

## Closure and limits

**All declared automated release/evidence gates for PR #40 are closed on actual main `88324210...`.** The author-side audit scripts, machine-readable results, original logs and three unchanged new original ZIPs are retained in the execution workspace. This supports closing Issue #39 as completed, not claiming all possible project errors are eliminated.

Historical implementation-pinned studies retain their original source/environment and receipts. Replay unchanged inputs into distinct new outputs; never reseal old evidence to force compatibility. General extreme-scale correctness, malicious concurrent-filesystem security, authenticated unseen teacher questions, arbitrary-language interpretation, full human visual inspection and manual desktop usefulness remain outside this release verdict. Issue #36 remains separate.