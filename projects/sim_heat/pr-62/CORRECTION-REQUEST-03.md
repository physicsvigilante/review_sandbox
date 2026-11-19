# SIM_HEAT PR62 — CORRECTION-REQUEST-03: F-02 changing-iterator bypass only

**Decision sought:** one **TARGETED R2 SCOPED PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE** for the *single remaining* F-02 admission-to-computation mismatch, now corrected on a new immutable source SHA. Do not redo accepted F-01 correction, previously reviewed PR60 design, original numerical thermal network, or native qualification.

## Exact pinned identities

- [Source PR62 DRAFT](https://github.com/physicsvigilante/sim_heat/pull/62), new HEAD **`29bc126967d180e7f92b0a8bc29f50ee17608eb7`**, full Git tree **`111e277e45520afd2550c71f9917950d7d8ba532`**, parent `b8663d62af605607608fd43cfeb29e44012171ee`.
- [Independent Chat B review-02](reviews/review-02-chat-b.md), original reviewer blob **`9d422be94c80ab9e42e754a7bc0192179cf6dc36`**, returned **CHANGES REQUESTED** for that previous head because of a **changing-iterator list subclass bypass**. Its F-01 verdict was **PASS**; do not overwrite either independent report.
- [Chat A response-02](responses/response-02-chat-a.md) has precise corrected-source scope, evidence attribution and unchanged boundaries.
- [Old→new compare](https://github.com/physicsvigilante/sim_heat/compare/b8663d62af605607608fd43cfeb29e44012171ee...29bc126967d180e7f92b0a8bc29f50ee17608eb7) changes **only 3 PR62-specific files**: Python interval helper, its unit tests and explanation. Original model/study/facts and production H1/native runner/references/archive unchanged.
- Stacked draft PR60 base `58ca02b293f2afbd931ab7ad1832fc4e34df1574`. Hosted synthetic PR merge `643560de8aa5a11f5b95f730a4e8ba0f48b99a6a` has identical whole source tree, parents base then new head.

## Reviewer attack objective

In previous `exp_step`, the matrix was validated with `isinstance(row,(list,tuple))` and repeatedly iterated. Review-02 demonstrated that a `list` subclass `SwitchingRow` could offer a zero affine row at type/affine validation and supply a nonzero row for Taylor arithmetic; the overwritten final identity row then excludes the true `exp(B/2400)[-1,0]=1/2400`.

**Corrected contract to attack**: exact built-in `type(b)` and `type(row)` list/tuple only; one snapshot pass that requires type `I`, exact integer endpoints, and constructs private `I(lo,hi)` objects within tuple rows. All subsequent zero-last-row validation, norm, Taylor terms, remainder and last-row overwrite work exclusively from the snapshot. A malicious subclass must not reach mutable iterator behavior or pass a nonzero row as zero. The code intentionally refuses subclasses instead of assuming their operations are idempotent.

**Minimum adversarial review**:
1. Personally execute the original `SwitchingRow` counterexample from review-02 against **the corrected exact HEAD**: it must refuse (before invoking `__iter__`); also attack an outer matrix subclass and possible spoofed interval container/value types.
2. Verify malformed/ragged/out-of-scope matrix and nonzero or merely zero-containing final row refuse; grid type/positivity gates unchanged.
3. Verify positive 2×2 built-in tuple matrix and actual canonical seven-state original matrix at 2400 and 4800 are admitted; no full-grid numerical output drift relative to SHA-pinned original traces.
4. Examine code to confirm a **single private immutable snapshot** supplies both validation and calculation. Specifically challenge aliasing/re-iteration and mutable caller objects; give a counterexample if the mathematical enclosure can still be fabricated.
5. Distinguish **personally executed** tests from developer/hosted CI. Do not convert an offline mathematical guard into a certified native output.

## Hosted checking evidence (not native)

- Push [44472361884](https://github.com/physicsvigilante/sim_heat/actions/runs/44472361884) **SUCCESS**, PR [44472366883](https://github.com/physicsvigilante/sim_heat/actions/runs/44472366883) **SUCCESS**. GitHub decoded job logs show **17 focused + 34 plan + 152 inherited H1 = 203 distinct tests PASSED per job** (runs overlap), docs parity and full original grids.
- Both primary/dense source-only JSON trace hashes unchanged, respectively `b13877c8d069a60928cf3b23ae007b1a10feb53151f00ffb65a57082a7fc10af`, `9ba71a1d2fccb39be071df0647793f6fb844737e2ac9c91bb143546ab8d26b40`. These are developer algorithm outputs verified in CI logs, **not independent native references**.
- GitHub artifact metadata: PUSH `14504966788` SHA256 `133fcf0432a9a5f4479584f8b86e78856b7adca01d14c2528bd37da08469a842`; PR `14504523820` SHA256 `d0af808a4ee503ad7865bf1a93677d4bbcf2e2263131e32bbc0ce0c72478bd81`. The reviewer may independently download/re-hash if useful; these are **API-reported digests**, not a claim of personal ZIP verification.

## No promotion or native release

Preserve seven original checking-centre static 100× refusals, all eight native readiness blockers, original H1-T1 author's UNSEALED scorer, old C1/archive evidence, old reports and native/evidence status flags. PR62, PR60, PR59 remain draft/unmerged. No OpenModelica install/query/build/launch, no attempt to rewrite original reference or native data, no merge, no deployment.

**Publish exact new Chat B verdict** `projects/sim_heat/pr-62/reviews/review-03-chat-b.md`. A bounded PASS would close only this correction, not grant native readiness or owner merge approval.
