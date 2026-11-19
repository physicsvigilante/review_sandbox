# SIM_HEAT PR #62 — independent Chat B targeted R2 review-03

**Verdict: SCOPED PASS — F-02 only, at `29bc126967d180e7f92b0a8bc29f50ee17608eb7`.**

The changing-iterator admission-to-computation mismatch is closed for the stated exact-built-in-container / exact-interval input contract. I reproduced the previous failure, executed the corrected source rather than a transcribed implementation, inspected the completed private snapshot, attacked caller-object aliasing and mutation, and personally replayed both complete source-only grids. No remaining F-02 blocker was found in this scope. This is **not** full-PR acceptance, independent certification of the entire numerical method, native readiness, execution permission, or merge authorization.

## 1. Scope and authenticated source

Read [CORRECTION-REQUEST-03](../CORRECTION-REQUEST-03.md) first, followed by [independent review-02](review-02-chat-b.md) and [Chat A response-02](../responses/response-02-chat-a.md), under [REVIEWER-PROMPT-03](../REVIEWER-PROMPT-03.md). F-01 remains accepted under review-02; I did not reopen its correction, PR60's design, or the earlier thermal/interval-method review.

| Identity | Independently checked value |
|---|---|
| Reviewed source HEAD | `29bc126967d180e7f92b0a8bc29f50ee17608eb7` |
| Reviewed whole Git tree | `111e277e45520afd2550c71f9917950d7d8ba532` |
| Sole parent / rejected source HEAD | `b8663d62af605607608fd43cfeb29e44012171ee` |
| Stacked PR60 base reported by PR metadata | `58ca02b293f2afbd931ab7ad1832fc4e34df1574` |
| Corrected Python Git blob | `145fdd3e2d8e7c870e3ae609ac46a0c2694b7898` |
| Previous Python Git blob | `08908a2ff0bc9bf69367992a08b896e859feebbb` |

The [one-commit correction](https://github.com/physicsvigilante/sim_heat/commit/29bc126967d180e7f92b0a8bc29f50ee17608eb7) changes exactly three N1-specific paths: `certified_reference.py` (+20/-6), `tests/test_certified_reference.py` (+35), and `INTERVAL-REFERENCE-V1.md` (+2). The arithmetic after admission, original model/study/facts, production libraries, native runner, historical references and C1/archive material are unchanged by this correction. PR62 metadata was open/draft/unmerged at inspection, with the requested exact HEAD.

Direct container network cloning was unavailable. Instead I personally downloaded **push artifact `14504966788`**, checked all **18 ZIP entries** for CRC integrity, and computed ZIP SHA-256 **`133fcf0432a9a5f4479584f8b86e78856b7adca01d14c2528bd37da08469a842`**. I reconstructed Git blobs and directory trees from the archived source bytes and modes: the whole tree equals the pinned `111e277e...`, not merely the artifact's text claim. The Python/test/document blobs also match GitHub's commit metadata. After testing, all **231 archived regular source files remained byte-identical**, with no extra source files.

For the old-version negative control I reversed only the authenticated guard patch in a separate scratch copy of the Python module, then verified the resulting complete file against GitHub's old blob `08908a2f...`. Both old and corrected modules were imported as real complete modules. The old helper used the unchanged supporting code from the authenticated current source. This was **not** an isolated reimplementation of `exp_step`.

Personal environment: Python **3.13.5**, mpmath **1.3.0**, NumPy **2.3.5**, SciPy **1.17.0**, already available; no dependencies were installed. Independent harnesses blocked child/native process creation with a Python audit hook. All generated mathematical output was written to new scratch directories outside the source repository.

## 2. Original exploit and outer-container variant: personally executed

I ran the exact review-02 `SwitchingRow` behavior: stored final row `[one, zero]`, first two iterations yielding `[zero, zero]`, third iteration yielding the nonzero stored row. I also supplied a switching outer `list` subclass whose first two iterations yielded zero rows and third iteration supplied the nonzero matrix to arithmetic.

For the matrix consumed by arithmetic,

`B = [[0, 0], [1, 0]]`, so `B² = 0` and `exp(B/g)[1,0] = 1/g` exactly.

| Attack and grids | Old `b8663d62...` | Corrected `29bc1269...` |
|---|---|---|
| Original switching row, 2400 and 4800 | Accepted after **3** overridden iterations; returned `[0,0]`, excluding exact `1/2400` or `1/4800` | **ValueError refusal; 0 overridden iterations** |
| Switching outer matrix, 2400 and 4800 | Accepted after **3** overridden iterations; returned `[0,0]`, excluding `1/g` for the matrix actually supplied to arithmetic | **ValueError refusal; 0 overridden iterations** |

These are **8 personal old/new executions**: four old-source demonstrations and four corrected-source refusals. For the original row attack, the indexed stored matrix and arithmetic-consumed matrix agree. For the outer variant, its stored pre-switch zeros and arithmetic-consumed matrix deliberately differ; it demonstrates the same validation/computation mismatch rather than assuming ordinary indexing and overridden iteration agree.

The corrected refusal was `Taylor requires a square matrix of dimension 1..7`, before either malicious iterator was invoked.

## 3. Additional personal controls: 87/87 passed

These are reviewer-authored controls against the authenticated production module, separate from hosted CI and the repository's existing tests.

| Control group | Cases | Observed result |
|---|---:|---|
| Malformed, empty, ragged, generator, mapping, scalar-row and 8×8 shapes | 14 | Refused |
| Poisoned `list`/`tuple` subclasses at outer and row boundaries | 4 | Refused without invoking overridden iteration, length or indexing |
| Wrong cell types, interval subclass, and `__class__` interval spoof | 8 | Refused |
| Wrong endpoint types: bool, float, int subclass, string, and callback-bearing objects | 10 | Refused before endpoint callbacks |
| Forged exact `I` with reversed integer endpoints | 1 | Refused when constructing the copied `I` |
| Zero/negative/non-exact-int grids, including bool and int subclass | 10 | Refused |
| Nonzero final rows, merely zero-containing intervals, and original 1×1/2×2 regressions | 12 | Refused |
| Unchanged zero-norm / excessive-norm preconditions | 2 | Refused |
| Aliased nonzero last row and shared all-zero rows | 2 | Correct affine/norm refusal retained |
| Exact nilpotent 2×2 positives, all list/tuple combinations, both signs and both grids | 16 | Exact rational entries enclosed; old/new endpoints and proof identical |
| Ordinary tuple 2×2 diagonal positive at both grids | 2 | Admitted; old/new endpoints identical; 100-digit mpmath spot-check passed |
| Actual canonical source-derived T1-T 7×7 matrix at both grids | 2 | Admitted; old/new endpoints and proof identical; exact identity final row |
| Valid shared-row/shared-cell 3×3 positives at both grids | 2 | Same result as alias-free copy; exact nilpotent entries enclosed |
| Live completed-snapshot inspection and caller-mutation attacks | 2 | Private snapshot and result unchanged |

Total: **63 refusal controls + 22 positive controls + 2 snapshot-mutation controls = 87**. The mpmath comparison is a non-certifying numerical spot-check, not a proof or native reference. Exact nilpotent controls use `exp(B/g) = I + B/g`, providing rational positive controls without a floating-point oracle.

I also personally reran these **three existing F-02 unittest methods**, all passing:

- `ArithmeticSafety.test_f02_nonzero_affine_last_row_refuses_instead_of_false_enclosure`
- `ArithmeticSafety.test_f02_matrix_shape_and_types_refused`
- `ArithmeticSafety.test_f02_switching_container_cannot_change_matrix_after_admission`

I did **not** present the entire 17/34/152 hosted suites as my own reruns or use their success to substitute for the independent attacks.

## 4. Immutable snapshot inspection and aliasing challenge

The [exact corrected implementation, lines 138–180](https://github.com/physicsvigilante/sim_heat/blob/29bc126967d180e7f92b0a8bc29f50ee17608eb7/qualification/h1_n1/certified_reference.py#L138-L180) has the required sequence:

1. Exact positive `int` grid; exact built-in outer `list`/`tuple`; dimension 1–7.
2. Exact built-in rows of the required length; exact type `I` cells; exact `int` endpoints.
3. New `I(lo, hi)` for every occurrence, tuple rows, then `b = tuple(private_rows)`.
4. Exact-zero final-row validation and construction of `x` from **that same private `b`**. Norm, Taylor terms, tail and final-row overwrite thereafter depend only on the snapshot or its derived arithmetic values.

I used a line-tracing hook immediately after line 160, **before** the affine-row check at line 161. Without modifying the production function, I inspected the live local `b` and established that its outer container and rows were exact tuples, every cell was a fresh exact `I`, every endpoint was an exact integer, and even repeated caller-cell aliases produced distinct private cells. Ordinary assignment to the outer tuple, inner tuple and frozen interval cell was refused.

While paused at that boundary I changed **caller-owned** interval endpoints using `object.__setattr__` (deliberately bypassing their frozen setter), cleared/replaced caller rows, and cleared the caller's outer list. The already-captured endpoint values did not change. At both grids, the final result and proof were exactly equal to an unmodified baseline. The trace hook did not mutate snapshot cells, module globals or arithmetic methods.

**Conclusion:** admission and computation no longer re-read caller-controlled matrix contents separately. The former zero-row/nonzero-arithmetic substitution cannot enter through overridden container methods, and caller-cell aliases do not leak into the completed snapshot.

This is a bounded Python API input review, not a sandbox against arbitrary code execution, monkey-patched module classes/globals, or direct mutation of private frame locals. It also does not certify an atomic multi-threaded transaction over caller containers while the snapshot is being built. The checked contract is computation on the copied snapshot, including isolation from caller mutation after it is completed.

## 5. Both complete grids personally replayed: no numerical drift

I called the actual corrected `certify(read_facts(), grid, output=...)` on each full grid in new outside-repository scratch directories. Each run retained all **77 exports, 8 requested quantities and 5 flow integrals**. I independently hashed the newly written complete JSON trace and compared its bytes to the downloaded exact-head artifact trace and the correction request's pinned historical trace digest.

| Grid | Samples | Personal full-trace SHA-256 | Result |
|---|---:|---|---|
| 2400 | 2401 | `b13877c8d069a60928cf3b23ae007b1a10feb53151f00ffb65a57082a7fc10af` | **MATCH; byte-identical** |
| 4800 | 4801 | `9ba71a1d2fccb39be071df0647793f6fb844737e2ac9c91bb143546ab8d26b40` | **MATCH; byte-identical** |

These are personal complete **source-only mathematical reruns**, not merely inspection of developer hashes. They establish regression stability of this guard change; they do not constitute a fresh independent proof of the whole thermal assembly or interval algorithm. I did not rerun the old module's full grids: old/new helper endpoints and proofs were compared directly, and the new full traces match the already pinned original digests.

## 6. Hosted evidence versus personal evidence

I independently queried GitHub job metadata for [push run 44472361884](https://github.com/physicsvigilante/sim_heat/actions/runs/44472361884) and [PR run 44472366883](https://github.com/physicsvigilante/sim_heat/actions/runs/44472366883). Both report completed/success and `head_sha=29bc126967d180e7f92b0a8bc29f50ee17608eb7`.

From the **personally downloaded push artifact**, I read the successful **17 interval + 34 plan + 152 inherited H1 = 203** hosted test logs and documentation-parity log. I separately parsed its unchanged plan-check output: seven checking-centre refusals, eight execution blockers, zero native calls, and false reference-accuracy/native-readiness flags. Those hosted suite results are not additional personal test executions. I did not download/re-hash the PR artifact or independently reconstruct its synthetic merge tree; neither is needed for the authenticated exact-head source reviewed here.

The companion reviewer scratch evidence bundle supplied in chat contains the executable personal harnesses, logs/results, authenticated source archive, downloaded trace bytes and a file-hash manifest. Bundle SHA-256: **`f05ed2a6e2880120ca53e4eef90ddc3b3e6608711c8976b2748c75fafd7933c7`**. It is supporting review evidence, not a repository release or native reference. Harness SHA-256 values:

- `reproduce_switching.py`: `a2b3ec80ef748892a517afe71ccc6bb3c7d8743e409cf61804954d0ba0c02619`
- `adversarial_controls.py`: `1a4d448fb11ff2e4285a3fd6848ba411563a4b3a92ab220f742d6eb540aa074c`
- `full_grid_replay.py`: `764e0a16cd28422aeecfadf18edb40c1111b1be00aabc5d3e03863e6d55c4eae`

## 7. Unchanged holds and final disposition

The seven original checking-centre static 100× refusals remain `T02.G`, `T06.A`, `T06.G`, `T07.G`, `T08.G`, `T10.G`, `T_Plug.C`. All eight native-readiness blockers remain. The personally regenerated mathematical reports retain `independentlyCertifiedReference=false`, `runtimeReady=false`, `nativeExecuted=false`, `nativeQualified=false`, `originalCheckingCentresAdopted=false`, and `historicalReferenceRegenerated=false`. The original H1-T1 scorer remains **UNSEALED**.

No OpenModelica installation, version query, compilation, launch or simulation was performed. No production source, earlier report, original reference, historical C1/archive evidence, PR state or native gate was changed. This publication adds only this new review report. Earlier review-01 and review-02 remain historical CHANGES REQUESTED decisions for their respective rejected SHAs; review-02's F-01 acceptance is not rewritten.

**Final disposition: SCOPED PASS for the remaining F-02 changing-iterator correction at `29bc126967d180e7f92b0a8bc29f50ee17608eb7`. No further correction is required for this scoped finding. PR62/PR60/PR59 must remain unmerged under the existing holds; this review grants neither native permission nor owner merge approval. The owner may tell Chat A: “review done.”**
