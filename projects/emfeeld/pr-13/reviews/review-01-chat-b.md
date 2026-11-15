# EM Fields PR #13 — independent R2 review (Chat B, first report)

- **Project / source repository:** `emfeeld` / [physicsvigilante/emfeeld](https://github.com/physicsvigilante/emfeeld).
- **Source PR:** [#13](https://github.com/physicsvigilante/emfeeld/pull/13), draft and unmerged when reviewed.
- **Base SHA:** `c67d1115ad6fc982f29fe113583430e676938902`.
- **Exactly reviewed head SHA:** **`766633a60679208f534c5d299578b100d2d29eea`**.
- **Exact source tree SHA:** `6b10046d4b3b1f8480f53b59467b5cc84656960f`.
- **Diff:** [pinned base-to-head comparison](https://github.com/physicsvigilante/emfeeld/compare/c67d1115ad6fc982f29fe113583430e676938902...766633a60679208f534c5d299578b100d2d29eea).
- **Reviewer:** Chat B; separate ChatGPT conversation using GPT-6, **not** an independent human reviewer or demonstrably a different model family.
- **Date/time:** 2026-11-15, evidence completed at approximately 14:52 UTC.
- **Scope / risk class:** **R2 — physical/evidence critical**. Derived scalar ratios, units and signedness, synchronized saved-particle separation, numeric/refusal paths, sealed input/output integrity, source/CI evidence; no changes to source physics laws, integrator or viewer.
- **Were source files changed by Chat B?** **No.** Local disposable copies and test harnesses were used; no source PR commits, source PR reviews, merges or CI mutations were made.
- **Outcome: `changes-requested` (scoped to PR #13 at the SHA above).**

## Verdict summary

The architectural boundary is sound for the reviewed ordinary cases: derived observations use a complete sealed native run, existing named observations, matched trajectory sample indices **and** actual saved times, dimensionally identical scalar units, and Euclidean position distance. The independently written physical references match E1, G1 and T1. The recorded CI and ZIP evidence is authentic *as observed* and matches the pinned source tree. However, four new adversarial cases fail, including a nonzero ratio emitted as zero and a re-sealed derived report that passes `inspect` and exits **0** while its own per-item outcomes are partial. Two are recommended **required corrections** before merge; two are malformed-input robustness improvements. A self-consistently rewritten SHA-256 inventory is not cryptographic authentication; no stronger security claim is inferred.

## Findings

### F-01 — MAJOR — nonzero scalar ratio silently underflows to a successful zero

- **Source:** [`src/emfeeld/derived_observations.py:109-115`](https://github.com/physicsvigilante/emfeeld/blob/766633a60679208f534c5d299578b100d2d29eea/src/emfeeld/derived_observations.py#L109-L115).
- **Evidence type:** Independently executed novel input against exact Git-blob-verified source; repeated against the extracted CI source snapshot, **not** a new native solution.
- **Reproduction:** `_ratio` with two otherwise eligible, `status:"ok"`, `unit:"N/C"` field magnitudes: numerator `5e-324`, denominator `1e308`. Use `{"id":"tiny","type":"ratio","numerator":{"id":"a","part":"magnitude"},"denominator":{"id":"b","part":"magnitude"}}`.
- **Expected:** Since both source scalars are finite and nonzero but their mathematical ratio is approximately `4.94e-632` (outside the float64 representable range), return `unavailable / numeric_range` rather than falsely imply zero.
- **Observed:** `{"status":"ok","value":0.0,"unit":"1","code":null,...}`, and a one-item batch would be `complete`.
- **Impact / qualification:** Numerical edge only; not observed in the three real CI scenes. But the ratio grammar accepts both finite operands, and an exact `0` is physically different from an unrepresentably small nonzero result. Division overflow is already rejected, so fail-closed underflow is the consistent boundary.
- **Correction/regression:** After division, if `av != 0.0 and value == 0.0`, emit `numeric_range` (without rejecting legitimate zero numerators or valid near-zero nonzero quotients). Test positive/negative and signed subnormal cases, exact zero numerator, exactly zero denominator, finite small denominators, and overflow.

### F-02 — MAJOR — `inspect` accepts inconsistent reported overall completion

- **Source:** [`src/emfeeld/derived_observations.py:197-219`](https://github.com/physicsvigilante/emfeeld/blob/766633a60679208f534c5d299578b100d2d29eea/src/emfeeld/derived_observations.py#L197-L219) and [CLI exit at 235-236](https://github.com/physicsvigilante/emfeeld/blob/766633a60679208f534c5d299578b100d2d29eea/src/emfeeld/derived_observations.py#L235-L236).
- **Evidence type:** Independently executed **against the real unmodified G1 native source** recovered from SHA-256-verified Linux CI artifact; only a **disposable copy** of `derived-001/G1/result` was edited.
- **Reproduction:** Copy the artifact's G1 derived output, whose stored status is `partial` and whose `G1-invalid-time` item has `unavailable/different_saved_times`. Change only `result.json.status` to `complete`; regenerate that copy's `integrity.json` using `emfeeld.derived_observations._inventory(copy)`. Invoke:
  `python -m emfeeld.derived_observations inspect COPY --using <same original sweep-G1/sweep/baseline>`.
- **Expected:** `derived_integrity` rejection: top-level completion must equal `all(recomputed_item.status == "ok")`. A partial request batch cannot claim complete.
- **Observed:** The exact production `inspect` returns the altered status `complete`, retains `G1-invalid-time: unavailable`, produces **CLI exit code 0** and no stderr. It compares the recomputed observation array but **does not compare/recompute top-level `status`**.
- **Impact / qualification:** Unmodified output catches simple one-file edits through inventory mismatch, and no complete-status problem was found in a normally produced report. This test deliberately re-seals a derived **copy**; SHA-256 inventories do not authenticate the author of the bytes. Nonetheless the advertised deterministic semantic reinspection can and should reject internally contradictory completion independent of signature security.
- **Correction/regression:** Recompute/verify `result.status` from expected outcomes; verify `summary.execution_complete` and report usability at inspection, and reject structurally inconsistent result metadata. Regression must demonstrate that a re-sealed G1 `complete` forgery remains rejected and exit code is nonzero while intact G1 remains honestly `partial`.

### F-03 — MINOR (malformed-source boundary) — negative saved vector magnitude accepted as physical ratio

- **Source:** [`src/emfeeld/derived_observations.py:75-89`](https://github.com/physicsvigilante/emfeeld/blob/766633a60679208f534c5d299578b100d2d29eea/src/emfeeld/derived_observations.py#L75-L89), [`model_runs.py:196-223`](https://github.com/physicsvigilante/emfeeld/blob/766633a60679208f534c5d299578b100d2d29eea/src/emfeeld/model_runs.py#L196-L223).
- **Evidence type:** First independently executed direct helper input; independently repeated as **actual `derive`/native inspection** against a disposable copy of G1 native evidence.
- **Reproduction:** Copy `sweep-G1/sweep/baseline`; in the copy's `native/result.json`, replace the first successful field observation's `magnitude` with `-2.5`, and update the copy's existing `integrity.json` with `model_runs._inventory(copy)`. Keep original `run.json` and its pin unchanged. A field_0/field_1 ratio is marked `ok`, negative, and the derived batch `complete`, even though no vector magnitude can be negative. `inspect_run(copy)` accepts this self-consistently re-sealed source.
- **Expected:** Refuse negative, malformed magnitude/speed/kinetic-energy scalars; at minimum a nonnegative finite check for quantities with nonnegative physical definitions. Prefer also validating scalar vector magnitude against the saved 3-vector within a documented float64 tolerance.
- **Qualification:** **This is not demonstrated for any native report produced by the unchanged solver.** Ordinary tampering **without** updating native inventory is correctly caught. An actor allowed to rewrite data and unkeyed hashes can forge other plausible values too; this finding requests bounded input-shape/physical-invariant hardening, **not** cryptographic authenticity or re-solving physics. Does not independently block the PR once the two major findings are fixed unless the contract promises acceptance of arbitrary external native records.

### F-04 — MINOR — oversized integer `time_s` raises unhandled `OverflowError` instead of a local refusal

- **Source:** [`src/emfeeld/derived_observations.py:103-106,144-149`](https://github.com/physicsvigilante/emfeeld/blob/766633a60679208f534c5d299578b100d2d29eea/src/emfeeld/derived_observations.py#L103-L106), [CLI exception policy 228-239](https://github.com/physicsvigilante/emfeeld/blob/766633a60679208f534c5d299578b100d2d29eea/src/emfeeld/derived_observations.py#L228-L239).
- **Evidence type:** Independently executed malformed-row synthetic input against exact source, **not an output produced by a valid native trajectory**.
- **Reproduction:** Two otherwise successful position rows with distinct `particle_index`, same `sample_index:5` and `time_s: 10**500`; run `_separation`. `math.isfinite(10**500)` raises `OverflowError: int too large to convert to float` before returning `invalid_saved_time`. Analogous ratio path also invokes unguarded `math.isfinite`.
- **Expected:** Fail closed with `unavailable/invalid_saved_time` for malformed evidence, not a traceback. A canonical native saved `time_s` is a finite float, so this is a robustness rather than ordinary physical accuracy bug.
- **Correction/regression:** Validate time with the existing safe finite-float conversion, catching overflow, and retain actual-time plus index equality. Test very large integers, `bool`, absent time, `NaN`, `Infinity`, and mismatched index/time.

## Tests and independent evidence

### Source and CI identity, independently checked

- [Review request](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/emfeeld/pr-13/REQUEST.md); [contract](https://github.com/physicsvigilante/emfeeld/blob/766633a60679208f534c5d299578b100d2d29eea/docs/DERIVED_OBSERVATIONS_V1.md); [source `AGENTS.md`](https://github.com/physicsvigilante/emfeeld/blob/766633a60679208f534c5d299578b100d2d29eea/AGENTS.md); [protocol](https://github.com/physicsvigilante/review_sandbox/blob/main/PROTOCOL.md) and [R2 risk policy](https://github.com/physicsvigilante/review_sandbox/blob/main/REVIEW-RISK-POLICY.md) read.
- GitHub commit/tree API independently confirms **both** head `766633a...` and CI merge-preview `30d8413...` have the **identical exact tree** `6b10046d4b3b1f8480f53b59467b5cc84656960f`. The changed files are the derived module, its test module, qualification tool, design contract and additive release workflow step; no existing physics law or integrator file was changed by this PR.
- Downloaded and directly hashed the two original **GitHub Actions release artifacts**. Linux: run [43724035417](https://github.com/physicsvigilante/emfeeld/actions/runs/43724035417), artifact ID **14165479296**, ZIP SHA256 **`0c2fb874d84725a70fe3bc345a1035d541e3d18ca49d04ddff7eaa7efc92f8ca`**. Windows: same run, ID **14165888630**, ZIP SHA256 **`174b21de4360ee0e565f5d82db99be594ac503a769dedf36cc552e377c49937a`**. Each archive contains **1,230 files**, all archive CRC entries passed; `head-sha.txt` in each records the merge-preview checkout.
- Downloaded the separate source-snapshot run [43724035513](https://github.com/physicsvigilante/emfeeld/actions/runs/43724035513), artifact ID **14165247176**. ZIP SHA256 `22a67b6711ed05c0752148ce9ea07ec6c8113643824890f52cd67cd868728bbf`; `tested-source.tar` SHA256 `a78b2c596b9bc6be4f3c73c466b125ac9b50b527664788c8f4730a7180d343fe`, matching enclosed manifest. `identities.txt` records the same merge SHA and tree. Git blob SHA1 of the independently extracted **exact** `src/emfeeld/derived_observations.py` is **`e6ca4bc57a4a4f58e920ad982bd6b5e35f4128d9`**, matching GitHub's pinned blob. This is source-byte verification, not a fresh solver qualification.
- Read original Linux/Windows workflow job logs and files inside both release artifacts. Each OS logs **1,244 headless passing**, **18 historical behavior passing / 1 historical all-file-freeze assertion deselected**, **33 real-PyVista passing**, plus a **second execution of the same 25 derived tests**. Thus **1,295 distinct test executions by suite membership per OS** (`1244+18+33`), *not* 2,590 different tests or an extra 25 distinct tests. Both workflow jobs succeeded. The separate real-PyVista [run 43724035504](https://github.com/physicsvigilante/emfeeld/actions/runs/43724035504) also succeeded. All of these are **existing CI evidence**, not Chat B's own Windows or viewer runs.
- Headless source references in `tools/qualify_derived_observations.py` are **same-author** ideal-source formulas/RK4, not an independent model-family or peer-reviewed certificate. Original local full-headless timeout in Chat A's request is correctly described as **not passed**.

### Independently executed by Chat B (not CI)

Environment: separate Linux container, CPython **3.13.5**, NumPy **2.3.5**, SciPy **1.17.0**, pytest **9.0.2**. PyVista **not installed**. No installations performed.

1. Extracted the tree-verified source archive to a temporary directory. Ran `PYTHONPATH=src python -m pytest -q -W error tests/test_derived_observations.py`: **25 passed** in **4.59 seconds**. This is an independent *rerun* of the existing test cases, not 25 newly invented cases.
2. Imported a **Git-blob-SHA-matched** verbatim local source module, with only its `model_revisions` and `inspect_run` dependencies stubbed, and authored 12 novel boundary checks. Command `python -m pytest -q -vv --tb=short test_chat_b_adversarial.py`: **8 passed, 4 failed**. First failing cases were underflow, negative magnitude, enormous time and forged overall status. Test-harness SHA256: `4afbbb4154d495be77c15a55efbc94c0fac93d76dacfaa6f5dfa6d29859182bf`. These tests are genuine executions of the exact production module **but not native solver runs**.
3. Authored a second suite running the **original extracted source and real sealed Linux CI native E1/G1/T1 artifacts without any dependency stubs**. Final command `PYTHONPATH=src python -m pytest -q --tb=short /tmp/emfeeld_pr13_review/test_chat_b_native_artifacts.py`: **6 passed, 4 failed**. Test-harness SHA256: `cd7302671f8e12bbd8c84e2147e765209a60a327e479e217494c10bfb94217a4`. The four final failures reproduce F-01 through F-04. Earlier first attempt at this second suite failed to collect due a reviewer-authored line-continuation syntax error; the next attempt had **5 passed / 5 failed**, with three failures caused by test-harness mistakes (create-only `put` used for editing a file and an overly narrow error-message match). Corrected only the **local test harness**, then observed the final **6/4**. No production changes or discarded negative production observations.
4. Wrote **independent** static field equations for an electric line plus uniform field (E1), a gravitational sphere plus point (G1) and a static electric shell plus point (T1), using the scene's recorded SI parameters and SciPy fundamental constants. Ratios calculated by Chat B versus artifact: **E1 1.201106296660619 / 1.201106296660619**; **G1 0.8318483227835431 / 0.8318483227835429**; **T1 11.781609195402293 / 11.781609195402293**, second T1 ratio **0.36585365853658547 / 0.36585365853658547**. This supports the checked source geometries and vector norms; it is not a held-out textbook interpretation.
5. Independently authored **fixed-step RK4 (5,000 steps; separate acceleration routine)** for the two G1 test particles using the recorded gravitational point and sphere sources. Calculated **2.686918279985714 m** at **t = 2.5 s**, versus recorded **2.6869182799857136 m**, absolute discrepancy **4.44e-16 m**. The stored G1 measurement uses `sample_index:50` and actual `time_s:2.5`; the different-time request remains unavailable with no interpolation or inferred particle-particle interaction. This is an independently written calculation **over original recorded inputs**, not a new emfeeld native solve.
6. Used original G1 sealed native run to author an **additional derived batch** (not a new trajectory): same-time **J/J kinetic-energy ratio** succeeds with unit `1`; two different particles' index-100 positions yield metre separation at `t=5`; index-50/index-100 separation refuses with `different_saved_times`; saved potential-energy ratio refuses with `operand_unavailable`. The batch is correctly `partial`, and intact reinspection succeeds. Wrong `run.json` pin, an un-resealed corrupted native `result.json`, unit mismatch, absolute potential, failed authored check, nonfinite coordinate and same-body selections were also refused correctly.
7. Repeated the most consequential negative control with the **real G1 CI artifact**: re-sealed **only the copied derived result's** `status` from `partial` to `complete`, using the untouched original native source. Running `python -m emfeeld.derived_observations inspect` returned **exit code 0, `status:"complete"`, and `G1-invalid-time.status:"unavailable"`**. This is F-02, not an assumed defect.

**Representative minimal standalone reproductions** (run in the pinned source checkout):

```python
from emfeeld.derived_observations import _ratio, _separation

r = {"id":"r","type":"ratio",
     "numerator":{"id":"a","part":"magnitude"},
     "denominator":{"id":"b","part":"magnitude"}}
x = {"a":{"type":"field","status":"ok","unit":"N/C","magnitude":5e-324},
     "b":{"type":"field","status":"ok","unit":"N/C","magnitude":1e308}}
print(_ratio(r,x))  # OBSERVED: ok, value=0.0, unit=1; EXPECTED: unavailable

s = {"id":"s","type":"separation","left_id":"a","right_id":"b"}
a = {"type":"trajectory_sample","quantity":"position","unit":"m",
     "status":"ok","value":[0.,0.,0.],"particle_index":0,
     "sample_index":5,"time_s":10**500}
print(_separation(s,{"a":a,"b":{**a,"particle_index":1,"value":[1.,0.,0.]}}))
# OBSERVED: OverflowError; EXPECTED: unavailable / invalid_saved_time
```

For F-02, use `derived-001/G1/result` plus `sweep-G1/sweep/baseline` from original Linux release artifact; alter **a copied** `result.json.status`, then replace **the copy's** `integrity.json` bytes with `encode({"files":_inventory(copy)})` from `emfeeld.derived_observations`. The source `run.json`, underlying native artifact and original CI files are never modified. For F-03, copy the G1 native run and modify/re-seal **that copy only**, using `model_runs._inventory`; this models a fully rewritten unkeyed inventory, not undetected single-file corruption.

### Evidence boundaries / not run

- **Did not** re-run original E1/G1/T1 emfeeld integrations, all 1,244 headless tests, Windows or real-PyVista rendering. The original 25 focused tests and newly written post-processing tests **were** executed locally.
- **Did not** independently download every separate viewer artifact or validate Windows interactive mouse behavior. Offscreen CI and real-PyVista job success are recorded **CI evidence only**.
- Original sealed artifacts cannot cryptographically attest to a malicious writer; an attacker who can rewrite the entire run and hashes can forge plausible data. This is a provenance trust boundary, not a signature failure discovered in a product that promises digital signing.
- No new general source interpretation, unfamiliar textbook answer, classroom user study or independent human subject-matter evaluation was conducted. Input source facts and scenario assumptions are author-recorded; the T1 preselected **electric** (not gravitational) shell/point label correction is acknowledged without relabeling it as a new blinded test.
- Ordinary exact-byte integrity and wrong-pinned-run checks passed; source semantic authenticity and numerical accuracy for unseen configurations remain separate questions.

## Separate scope judgments

| Dimension | Pass / Fail / Unknown | Basis |
|---|---|---|
| Source interpretation fidelity | **Unknown** | Pinned E1/G1/T1 input scenes and domains preserved; no fresh interpretation from external textbook material; source attribution is author-recorded. |
| Physical/numerical correctness | **Fail (scoped)** | Independent E1/G1/T1 formulas and G1 RK4 agree to numerical precision; however valid finite scalar inputs can produce an incorrect successful exact zero on underflow (F-01). |
| Native simulation / observable coverage | **Pass (reviewed post-processing slice only)** | G1 same-actual-time and index separation, named measurement reuse, negative requests and partial status verified over real sealed native artifacts. No new native solver or broad unseen-model guarantee. |
| Evidence integrity and provenance | **Fail (scoped)** | Direct hash inventory and pin checks pass; F-02 allows re-sealed contradictory completion; F-03 exposes missing basic sanity validation on a self-consistently rewritten native source. No digital signatures were promised. |
| Teacher-facing usefulness | **Unknown** | Units, operand IDs, explicit unavailable reasons and `error_bound:null` help inspection; no teacher assessment or classroom observation. |
| Textbook-answer completeness | **Unknown / not evaluated** | This PR operates on named saved observations, not entire textbook problem interpretation or solving. |

## Release advice and smallest next gate

**Keep PR #13 draft/unmerged at this head: `changes-requested`.** Require F-01 and F-02 corrections with targeted regressions before accepting R2. F-03 (basic physical-invariant validation of magnitudes) and F-04 (safe finite saved-time handling) are small, low-complexity robustness fixes recommended in the same bounded patch; they do **not** justify reopening the overall architecture. Add regressions over **the actual saved G1 partial case** and synthetic extreme/malformed rows, without altering CI snapshots or original negative evidence. Re-run complete current-source Linux/Windows CI against the **new** head, identify the new source tree/ZIPs, and request a **targeted re-review** of changed measurement/inspection paths. No production merge, acceptance of teacher usefulness, or cryptographic authenticity follows from the existing CI or this review.

**Independence caveat:** This is a separate-context LLM review with newly executed tests and independently written physics calculations. It is not a human expert adjudication, a different proven model family, a novel held-out teaching corpus, or an approval to merge.
