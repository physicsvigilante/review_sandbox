# SIM_HEAT PR62 — CORRECTION-REQUEST-02: targeted independent R2 re-review of F-01/F-02 only

**Decision sought:** SCOPED PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE for the **two corrected fail-closed source/provenance and matrix-arithmetic defects** on the exact corrected source, **not** a new full reference certification, native operation or production merge.

## Exact source and independent finding history

- Source [DRAFT PR62](https://github.com/physicsvigilante/sim_heat/pull/62), stacked on DRAFT PR60 (base still `58ca02b293f2afbd931ab7ad1832fc4e34df1574`).
- **New corrected HEAD `b8663d62af605607608fd43cfeb29e44012171ee`**, complete Git tree **`3208ff20f46dd3ed1e1a2cd92e6f72f3f8f25309`**.
- Original independent Chat B [review-01](reviews/review-01-chat-b.md) original blob **`555024d5e4c5fcf36fd62b0e964c3ada89dcc7a3`**, **CHANGES REQUESTED on OLD head `12bb67e7abac54c8a2488109cb706d779c61bf93`**, old tree `bde985adb097d463627cfd6278b7f80f0b45ef10`. **DO NOT edit or relabel that report.**
- Corrected commit's ONLY parent is old head. [Old→new single-commit comparison](https://github.com/physicsvigilante/sim_heat/compare/12bb67e7abac54c8a2488109cb706d779c61bf93...b8663d62af605607608fd43cfeb29e44012171ee) changes exactly THREE PR62-specific files: `qualification/h1_n1/certified_reference.py`, `qualification/h1_n1/tests/test_certified_reference.py` and `qualification/h1_n1/INTERVAL-REFERENCE-V1.md`. Full PR62 remains **four additions vs PR60**; no old model/study/H1 physical library/parser/viewer/numeric policy/native runner/current old reference/frozen C1 changes.
- GitHub synthetic PR commit **`71416580726e47f41e9f3ec6fa1f59f8f3cb309b`** has identical whole corrected tree `3208ff20...`, ordered parents `58ca02b...` then `b8663d...`. Production main still `f52613c39c539b2d4543a9838e5658d526fca10e`; source PR62, PR60 and PR59 remain draft/unmerged.

[Developer response-01](responses/response-01-chat-a.md) accepts both original findings and records genuine fail-first red tests, exact correction, full-grid preservation and CI. Reviewer should independently inspect code and run the negative cases if feasible, not substitute Chat A's desired verdict.

## Target F-01 — mutated in-memory fact object must not receive pinned hash

Original callable `certify(s)` accepted arbitrary mutated `s` and then reported constant `FACTS_SHA256`. Source file loading `read_facts()` was correct but **did not constrain the mutable object passed later to certify**.

**Corrected contract:** `certify` always freshly calls original `read_facts()` (verifies raw original facts/model/study byte digests); recursively checks the entire **typed** caller object against the canonical snapshot, including dict key sets, list positions, full analysis and provenance; uses exact `Decimal.as_tuple` for source decimal identities, so neither float-for-Decimal nor bool-for-int is silently equivalent. **On any discrepancy refuse before construct, computation or output creation**. If it matches, use a **private fresh trusted facts dict** for the entire computation, never caller-owned mutable `s`. No untrusted report can claim the original source hash with mutated physics.

**Adversarial tests to challenge:** `T10.k=Decimal('95.00000000000001')`, rod endpoint/orientation, body initial/boundary temperature, horizon/grid, node ordering, model/study digest, provenance claim, omitted/extra field, boolean/number type confusion, float instead of Decimal; no output directory created on refusal. Positive canonical input still computes normally on original source. If the guard can be bypassed with any accepted in-memory mutation, report blocker with reproduction.

## Target F-02 — matrix-exponential identity-row overwrite only under proved affine contract

Old `exp_step` claimed a valid enclosure for any `b` but unconditionally overwrote the last computed row with identity. Mathematically invalid for `[[I(1)]]` or `[[0,0],[1,0]]`: both generate nonzero exact last rows.

**Corrected contract:** refuse nonpositive/noninteger grid, malformed/non-square/out-of-scope (1–7)-dimensional matrices, non-integer-scaled interval entries and any last-row interval with `lo!=0` or `hi!=0` (even if it *contains* zero). Only when last row of input B is **exactly zero** may the helper overwrite the last output row with mathematically exact identity. The valid T1-T 7×7 model already has this exact structural property; its Taylor norm/tail/error conditions are unchanged.

**Adversarial tests to challenge:** reviewer's 1×1 `[[I(1)]]` and 2×2 `[[0,0],[1,0]]` counterexamples; final-row interval `I(-1,1)` **containing zero but not identically zero**; empty/ragged/out-of-range shapes; malformed type, invalid grid; canonical 2×2 and T1-T 7×7 positive paths.

## Fail-first then fixed — evidence attribution

Chat A **wrote the first four adversarial tests against old source before editing it** and ran that exact old implementation. Test suite genuinely **FAILED (21 subtest failures, 1 error)**, including 13 separate mutated-facts controls and three nonzero-row mathematical counterexamples. The log remains locally archived, SHA256 **`fb9d868b9f921cf98b2d2fd19eddfd1f176c7cf45fc890e860c8a5d21227df1f`** (30,216 bytes); it is *not* represented as independently authored Chat B or hosted CI evidence. The old-head source and reviewer report remain unchanged. Corrected source now passes the same tests plus an additional no-files-created control. Reviewer can independently reproduce using new test file against old source and inspect exact diff. No real native calculation was made.

**Corrected exact-head local tests:** **16 focused interval tests PASS**, **34 inherited plan/arithmetic tests PASS**, **152 original H1 tests PASS** (202 unique PASS; overlaps across separate repeated CI are not additive), docs Markdown/HTML parity PASS. Original T1-T full-grid reference candidate output bytes remain **exactly equal** to old HEAD for BOTH grids:
- Primary 2400 intervals / 2401 samples: SHA256 `b13877c8d069a60928cf3b23ae007b1a10feb53151f00ffb65a57082a7fc10af`.
- Dense 4800 intervals / 4801 samples: SHA256 `9ba71a1d2fccb39be071df0647793f6fb844737e2ac9c91bb143546ab8d26b40`.

**Corrected exact-head hosted CI ALL GREEN:**
- [Push run **44467515628**](https://github.com/physicsvigilante/sim_heat/actions/runs/44467515628) SUCCESS, artifact [**14503276022**](https://github.com/physicsvigilante/sim_heat/actions/runs/44467515628/artifacts/14503276022): ZIP **5,586,161 bytes**, SHA256 **`14ae4e4c9708ffea84db99e72bfedb6650647c80b19d8b6b9d0e8989aa7959dc`**, 18 distinct CRC-valid entries, exact source.tar tree **`3208ff20...`**.
- [PR run **44467521226**](https://github.com/physicsvigilante/sim_heat/actions/runs/44467521226) SUCCESS on identical synthetic tree, artifact [**14502537890**](https://github.com/physicsvigilante/sim_heat/actions/runs/44467521226/artifacts/14502537890): ZIP **5,586,161 bytes**, SHA256 **`a39e61d471dab621bdd1e01ca88161cbcd79c3fe60b911770a04c09d4eb8c354`**, 18 distinct CRC-valid files, exact source.tar tree `3208ff20...`.
- Chat A **personally downloaded both actual artifact ZIP bytes, SHA256/CRC/unique-entry validated both and independently reconstructed full source.tar Git trees**; read retained full primary/dense original-reference candidate JSONs, reran old-plan check, and verified all **seven old static checking-centre REFUSALS** and **eight native execution blockers** remain with `nativeCalls=0`. These are checking-only CI runs; no new native test was performed.

## Required risk-boundary verdict

The corrected output still has `sim_heat.h1_n1.interval_reference_candidate/1`, `mathematicalIntervalSelfCheckPassed=true`, **`independentlyCertifiedReference=false`, `runtimeReady=false`, `nativeExecuted=false`, `nativeQualified=false`**. Existing old `h1.reference` checking centres are NOT replaced and the current native runner is NOT prepared to consume these new mathematical values. Four original primary/dense flow allowance mismatches remain an independent comparator blocker. The original H1-T1 LLM evaluator private scorer key is lost/UNSEALED; the original historical C1 failures and six archived diagnostic-only records remain unchanged.

**Independent reviewer:** one **TARGETED R2 correction review-02** on this current exact SHA/tree. Do not redo PR60 source-design review, PR59 authoring trial or PR62's full already-tested mathematical proof unless the changes actually affect it. Verify F-01 and F-02 fail closed, no canonical-output change, faithful source/status claims and no hidden adoption, and report **SCOPED PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE**. Write your **NEW** report to `physicsvigilante/review_sandbox/projects/sim_heat/pr-62/reviews/review-02-chat-b.md` without modifying review-01. No PR merge, OpenModelica query/install/build/launch, reference regeneration, old C1 integration, promotion or deployment permitted.
