# PR #35 — final actual main-push original archive audit 01

**Author-side post-merge release qualification COMPLETE (2026-11-17), for exactly merged commit `510014fc078c73d37146b9804763e29d04ac0018`.** This report derives from new original **main-push** GitHub Actions jobs and separately downloaded original artifact ZIPs, not from the earlier draft-PR archives. This is an author audit, not a teacher, independently authored physics-question trial, or manual Windows visual acceptance.

## Immutable reviewed and merged source

- [PR #35](https://github.com/physicsvigilante/emfeeld/pull/35) CLOSED/MERGED. Actual current `main` commit `510014fc078c73d37146b9804763e29d04ac0018`; ordered Git parents **[`1b0149d773f924e67e0cd1f950da8b5d0ffacaa2`, `72873b800db9b57051e1587aafd7ba5d938e1e41`]**.
- Independently reconstructed actual main Git tree **`a82188148568653311581d9d4c02e8c96a37d3cf`** matches the exact source corrected, tested and independently [reviewed R2 PASS](reviews/review-02-chat-b.md). Old [R2 review-01 CHANGES REQUESTED](reviews/review-01-chat-b.md) remains preserved for superseded failed `addb6ab3...` saved-time gate. An exact-head merge guard `expected_head_sha=72873b8...` was used.
- Source has **362 tracked files** (all ordinary tracked blobs/modes/paths included in exact reconstructed canonical Git tree). No changes to the 29-file `src/emfeeld` physics engine/field laws, solver, viewer, original stored studies or old numerical tolerances were introduced by PR #35. New source-first workflow is opt-in and does not certify user question interpretation.

## Original *NEW* main-push workflows, not pre-merge runs

- [Linux/Windows clean-install release #44075528373](https://github.com/physicsvigilante/emfeeld/actions/runs/44075528373): `event=push`, `head_sha=510014fc...`, COMPLETED **SUCCESS**, original Ubuntu-24.04 job `134012445917` and Windows-2022 job `134012446345` both **COMPLETED SUCCESS**. Every OS original ZIP test log records **1,580 headless passed + 18 historical behavioral passed (one obsolete all-file freeze guard deselected) + 33 real-PyVista passed**. The 11 new B1 tests are part of the 1,580; never double-count.
- [Separate real-PyVista #44075528342](https://github.com/physicsvigilante/emfeeld/actions/runs/44075528342): `event=push`, `head_sha=510014fc...`, COMPLETED **SUCCESS**; nine offscreen scene/slider cases PASS, original viewer `tests.log` records 1,580 headless passed, 17 original image receipts verified. Full visual inspection remains explicitly PENDING.

### Every original post-merge ZIP downloaded and checked

| New actual-main artifact | Original GitHub artifact ID | Original whole ZIP SHA256 | Direct independent audit |
|---|---:|---|---|
| Ubuntu 24.04 release | **14325586236** | **`0bf131fe1a4b3b9ffed52f7bb9f67029ecb5286d32d1a3ab262839e5055c397f`** | **2,176** unique/CRC-clean/casefold-safe members |
| Windows 2022 release | **14326255395** | **`0f916440177da6a7f9ed3babc758386fc132bcc266931fbc43a0841fcf2ab6c7`** | **2,176** unique/CRC-clean/casefold-safe members |
| Separate real-PyVista viewer | **14325081441** | **`14f09acd069ef6ab6f01df7de5889cffbb086df89b9fa7e7d26c536f83d2cf3f`** | **22** unique/CRC-clean members; **9/9 offscreen PASS, 17/17 PNG hashes** |

For **each** downloaded original ZIP the author independently computed the whole ZIP SHA256 and compared to GitHub's exact artifact digest; extracted/read **every** file to validate ZIP CRC, required relative safe paths, exact and casefold uniqueness. Each OS release `head-sha.txt` equals **actual merged `510014fc...`**, not an old PR preview.

From the **new viewer ZIP**: original `tested-source.tar` SHA256 **`f119a59ad82e2b4f937a1a68b4e06f3171c2c3be14018add5c30bd1d01eb38bf`**; author safely extracted, fresh-`git add -A; git write-tree`-indexed all **362** tracked files, obtained exact merged tree **`a821881...`**. Its tar bytes are not identical to the pre-merge source-snapshot TAR, but the canonical tracked Git tree **is identical**. Original viewer JSON labels `visual_inspection=PENDING`, regardless of nine automated render/slider PASS cases; no human Windows interactive pointer trial is claimed. All 17 original image PNG signatures and SHA256 receipts were directly checked.

## Raw source-first question, retained native results and status in both ORIGINAL OS ZIPs

Read and compared the original ZIPs' `question-first-v1/lock/question.json`, `lock/receipt.json`, `attempt/question.json`, `attempt/receipt.json`, `attempt/packet.json`, `attempt/native-result.json`, `attempt/assessment.json`, and `attempt/state.json`:

- Original frozen **developer-authored** question raw SHA256 **`36f56dcc11d6347a1db47adfb103b16472a8e1270641869f52c7220bd086a361`**, original authored observation packet SHA256 **`6fe25bf6c738ee13fa837793414b343feeb53116737bcfafcf19c56c36adac5d`**. Both raw bytes match each other across their archived copies and the newly merged Git-tracked originals; receipt equals the exact source hash/ordered five requested IDs, source-authenticity `not_authenticated`, `developer_authored`.
- Each original native report has exact five distinct named `status=ok` results and aggregate `status=ok`. Original field `(0,-2,0) m/s²` at launch, final `r(2)=(1.8,0.4,0.2) m`, final `v(2)=(0.4,-2.8,0.1) m/s`, actual saved `sample_index=20` / `time_s=2.0` and initial/final `total_energy=12.0125 J` at indices 0/20. Values checked against separate uniform-gravity closed form and explicit SI/time/index requirements with bounded numerical tolerance; the analytic check is **same-author**, not externally certified science.
- Both actual main-push OS native report JSON files happen to have original SHA256 **`bf11cc7a6abd598bba0ae1746ca934eaf2ebc8c383aff79373676d5b4b06b947`** in this run, with each original assessment binding that native report SHA256. This **observed** equality is not a cross-platform byte-identity requirement; the original PR-head Windows/Linux ZIP native reports differed and remain accurately documented in earlier audit.
- Original `state.json` reports `execution_complete=true`, `native_measurement_coverage=complete` and original `assessment.json` has **five requested observations, issues=[]**. Four distinct scientific interpretation/certification assessments remain **`interpretation_fidelity=not_verified`**, **`independent_physics_correctness=not_evaluated`**, **`educational_usefulness=not_evaluated`**, **`textbook_answer_completeness=not_evaluated`**. No `complete` coverage claim means independent scientific/teacher correctness.

## Preserved previous physical evidence and source

- Original per-OS Physics Demonstration V1 persisted **17 distinct named actual `status=ok` measurements**, **64/64 same-author analytic reference comparisons passed**. Original `physics-demo-v1/summary.json` includes **29 engine-file SHA256 receipts**, each rehashed from the **actual newly merged viewer source TAR**, accepting ordinary Windows CRLF checkout vs canonical Linux LF bytes as supported by the original artifacts, no retyped source values.
- Signed E1 ensemble saved measurement projection retains global **complete, 10/10 `ok`** original measurements. Signed G1 remains honest global **partial**, **seven `ok` plus one `unavailable` with `code=unknown_operand`, `value=null`**, including originally absent `body-4-absent`. Nothing converted `null` to zero or an incomplete question to complete.
- Original stored source and test evidence were not modified. Local author post-merge focused replay from the viewer's exact source TAR independently passed **54/54 question-first tests** and **18/18 historical behavioral tests** `-W error` (one obsolete all-file freeze guard deselected). Full **1,580 headless per OS** PASS is grounded in the original complete hosted CI logs, not a claim of local complete rerun.

## Final bounded disposition

**For PR #35 Question-First Physics Trial V1, all declared pre-merge independent R2, exact-source integration, new actual post-merge Linux/Windows clean-install, separate real-PyVista and original ZIP/source/native-evidence release gates are CLOSED / PASS.** This qualifies **source-first original question raw-byte checkpointing and exact native measurement coverage of explicitly declared supported observations**. It does not mean a genuinely unseen externally sourced question, independently withheld judge, human physical correctness or teacher acceptance occurred.

A genuine prospective study is tracked separately in [Prospective Physics Question Trial V1 — Issue #36](https://github.com/physicsvigilante/emfeeld/issues/36), blocked on real independently authored question/judge inputs. No manual Windows desktop/pointer trial, general Maxwell/conductor physical law, teacher outcome, external source authentication against malicious all-file re-sealing, distributed ACID or guaranteed global numerical error bounds are claimed.
