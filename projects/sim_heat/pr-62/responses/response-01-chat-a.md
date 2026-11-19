# SIM_HEAT PR62 — Chat A disposition and corrections for independent R2 review-01

**Disposition:** **ACCEPT / REPRODUCE both R2 findings F-01 and F-02; corrected on NEW source HEAD, AWAIT targeted independent review-02.** This is Chat A's response, not a Chat B review or authorization to merge/run native physics. Original independent [review-01](../reviews/review-01-chat-b.md), exact reviewer-authored Git blob **`555024d5e4c5fcf36fd62b0e964c3ada89dcc7a3`**, remains **CHANGES REQUESTED on old head**, with original outcomes unchanged.

## Exact source and review chronology

- [Draft source PR62](https://github.com/physicsvigilante/sim_heat/pull/62) remains **open/DRAFT/UNMERGED**, stacked on independently reviewed design PR60 (also DRAFT/UNMERGED), not on production main.
- Reviewer inspected old HEAD **`12bb67e7abac54c8a2488109cb706d779c61bf93`**, complete tree **`bde985adb097d463627cfd6278b7f80f0b45ef10`**.
- Corrected HEAD **`b8663d62af605607608fd43cfeb29e44012171ee`**, complete tree **`3208ff20f46dd3ed1e1a2cd92e6f72f3f8f25309`**, parent precisely old reviewed HEAD. Base PR60 HEAD **`58ca02b293f2afbd931ab7ad1832fc4e34df1574`**, tree `c31fe1a37a598f30fa5859227a3ccbc5abf5c470`. Current main still `f52613c39c539b2d4543a9838e5658d526fca10e`, tree `0c44961b473d23737b0c9f3b3f2cd3db65b9f264`.
- Current hosted synthetic PR merge **`71416580726e47f41e9f3ec6fa1f59f8f3cb309b`** has exact identical candidate Git tree `3208ff20...`, ordered parents PR60 base then corrected HEAD.
- **Exactly THREE modified N1-only paths from old review**: `qualification/h1_n1/certified_reference.py`, `qualification/h1_n1/tests/test_certified_reference.py`, `qualification/h1_n1/INTERVAL-REFERENCE-V1.md`. The full stacked PR62 remains exactly four ADDED paths relative to PR60. No production H1/physics/numerical policy, original T1 model/study/provenance, Modelica, native runner, prior reference bundle, viewer, archived C1 or six historical diagnostic cases altered.

## F-01 reproduced and corrected — public callable must not stamp a forged source hash

Original `read_facts()` byte-checked the original source model/study/fact JSON, but `certify(s)` accepted arbitrary mutable in-memory `s` and unconditionally placed constant `FACTS_SHA256` in the result. The reviewer correctly identified that mathematical conservation checks could be run on **modified physics** while falsely claiming unchanged facts.

**FAIL-FIRST REGRESSION:** Chat A wrote actual first-attempt adversarial unit tests against the OLD source before editing it. These genuinely FAILED: mutation of `T10.k` to `Decimal('95.00000000000001')`, reversed/mutated rod orientation, warm boundary temperature, body initial temperature, horizon/grid, node ordering, study identity, provenance, added/removed fields, boolean-for-integer and float-for-exact-Decimal substitutions all reached the old `construct` path (the test's mock raises if this happens). These were real negative outcomes, not hypothetical and not misclassified as native results.

**Corrected callable:** At the beginning of `certify(s)`, independently call `read_facts()` again to verify canonical **raw** source-facts SHA and original model/study SHA, then recursively compare the caller's entire object to the pinned snapshot with **exact Python types** and exact `Decimal.as_tuple()`, order-sensitive lists and complete dict field identity. On any mismatch immediately `ValueError('pinned source-facts object identity mismatch')`, before `construct` or creating an output directory. On match, `certify` discards the caller-owned mutable object and calculates from the **privately freshly loaded source snapshot**, preventing later caller-side mutations from changing a reference stamped with the pinned hash. The positive canonical-call control still reaches `construct` with a **different trusted object**. One added test asserts a mutation creates **no output directory**.

**Post-correction:** all adversarial mutation controls now **REFUSE**, positive canonical S/T mathematical reference generation still passes; no original physical input or source evidence modified. This is a source/provenance trust-contract fix, not a native result.

## F-02 reproduced and corrected — affine final-row assumption must be proven

Original generic `exp_step(b, intervals)` unconditionally overwrote its entire last output row with an identity row, while **never validating that the last input row of B is exactly zero**. The reviewer provided valid mathematical counterexamples `[[I(1)]]` and `[[0,0],[1,0]]` where an unqualified row overwrite gives an incorrect bound.

**FAIL-FIRST REGRESSION:** Before source edit, direct calls using both examples and a last interval row merely *containing* zero **FAILED** the expected refusal assertions. Empty, non-square, inconsistent-row, malformed entries and invalid-grid cases likewise failed or errored rather than providing the explicit contract refusal. The first set of four new tests against original source ended **FAILED (21 subtest failures, 1 error)**. These are preserved in the local fail-first log; no old source Git commit, old reviewed report or hosted CI has been rewritten.

**Corrected helper:** `exp_step` now rejects a nonpositive/non-integer grid, anything other than a square **1–7 dimensional** interval matrix with integer-scaled interval endpoints, and **any** nonzero last-row endpoint (`lo != 0` OR `hi != 0`). Only for a provably exactly-zero affine final row may the routine apply its analytic identity-row replacement. Both reviewer counterexamples and all malformed shapes now fail closed. The original **7-state** T1-T matrix already has an exactly-zero last row, so its Taylor remainder/conservation dynamics were not modified.

**Post-correction:** current valid 2×2 and original 7×7 affine controls pass; bad-matrix controls refuse. No numerical acceptance allowance or physics law weakened.

## Corrected-source tests and artifact identity — not native qualification

**Local exact corrected-source:** all **16 focused interval/provenance/negative tests PASS**, **34 reviewed plan/arithmetic tests PASS**, **152 original H1 tests PASS** (202 distinct tests), documentation parity PASS. Full 2,401- and 4,801-sample original T1-T generation completed in scratch directories; their entire JSON trace SHA256 is **BYTE_IDENTICAL** to original reviewed pre-correction source:
- Primary `b13877c8d069a60928cf3b23ae007b1a10feb53151f00ffb65a57082a7fc10af`.
- Dense `9ba71a1d2fccb39be071df0647793f6fb844737e2ac9c91bb143546ab8d26b40`.

**Current exact corrected-head hosted GitHub CI BOTH SUCCESS:**
- [Push **44467515628**](https://github.com/physicsvigilante/sim_heat/actions/runs/44467515628), artifact [**14503276022**](https://github.com/physicsvigilante/sim_heat/actions/runs/44467515628/artifacts/14503276022), ZIP **5,586,161 bytes**, SHA256 **`14ae4e4c9708ffea84db99e72bfedb6650647c80b19d8b6b9d0e8989aa7959dc`**.
- [PR synthetic **44467521226**](https://github.com/physicsvigilante/sim_heat/actions/runs/44467521226), artifact [**14502537890**](https://github.com/physicsvigilante/sim_heat/actions/runs/44467521226/artifacts/14502537890), ZIP **5,586,161 bytes**, SHA256 **`a39e61d471dab621bdd1e01ca88161cbcd79c3fe60b911770a04c09d4eb8c354`**.
- Both jobs: **16 new interval +34 plan +152 H1 =202 distinct unit PASS per run**, documentation parity PASS, both full source-only grids PASS. Chat A personally downloaded/rehashed each ZIP, verified **18 distinct CRC-good entries per ZIP** and reconstructed both included `source.tar` snapshots to exact Git tree **`3208ff20f46dd3ed1e1a2cd92e6f72f3f8f25309`**, including corrected source, tests and docs. Both original mathematical traces remain BYTE_IDENTICAL across original/corrected source and push/PR CI.
- Both retained `old-plan-check.json` artifacts **still REFUSE seven old static checking centres** (`T02.G,T06.A,T06.G,T07.G,T08.G,T10.G,T_Plug.C`), **eight native execution blockers**, zero native calls and `referenceAccuracyCertified=false, nativeExecutionReady=false`. New output schema remains `sim_heat.h1_n1.interval_reference_candidate/1` with `independentlyCertifiedReference=false`, `runtimeReady=false`, `nativeExecuted=false`, `nativeQualified=false`.

**Boundary:** The reviewer independently checked some representative high-precision temperatures/flows/physical matrices, not the complete interval candidate's every sample; this new correction is not yet independently re-reviewed. Even a future PASS of the two safety fixes is **not a native reference bundle, external host seal, runner-ready numerical certificate or physical simulation**. The missing H1-T1 private scorer key remains UNSEALED. Six original archived native cases remain `diagnostic_only/nativeQualified=false`; original C1 failures and references unchanged. PR59, PR60 and PR62 all remain draft/unmerged; no owner source-merge or native-execution approval exists.

**Disposition / next:** request one **targeted independent R2 review-02 of F-01 and F-02 ONLY**, with current source HEAD, regressions, exact CI/artifacts, canonical-output identity and original flags. No redundant whole-project review or new numerical-law redesign. If independent correction review passes, proceed with separately scoped *future* runner/reference integration readiness work, still under explicit native hold.
