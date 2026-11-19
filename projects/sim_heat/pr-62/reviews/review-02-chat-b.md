# SIM_HEAT PR #62 — independent Chat B targeted R2 correction review-02

**Verdict: CHANGES REQUESTED — F-01 passes the targeted correction checks; F-02 has one remaining fail-closed bypass.** This judgment applies **only** to F-01/F-02 on the exact corrected source. It does not reopen the broader PR60 design or the earlier PR62 numerical implementation review, approve a native reference, authorize OpenModelica, or authorize a merge.

## Pinned identity and scope

- **Reviewed corrected PR62 HEAD:** [`b8663d62af605607608fd43cfeb29e44012171ee`](https://github.com/physicsvigilante/sim_heat/commit/b8663d62af605607608fd43cfeb29e44012171ee), Git tree **`3208ff20f46dd3ed1e1a2cd92e6f72f3f8f25309`**. GitHub commit metadata confirms sole parent **`12bb67e7abac54c8a2488109cb706d779c61bf93`**, the originally reviewed head.
- **Original independent review-01:** [CHANGES REQUESTED on the old SHA](review-01-chat-b.md); unchanged. Read [CORRECTION-REQUEST-02](../CORRECTION-REQUEST-02.md), [REVIEWER-PROMPT-02](../REVIEWER-PROMPT-02.md), and [Chat A response-01](../responses/response-01-chat-a.md).
- Independently compared old→new: **exactly three modified paths** (`qualification/h1_n1/certified_reference.py`, its `tests/test_certified_reference.py`, and `INTERVAL-REFERENCE-V1.md`); 46 source additions/1 deletion, 80 test additions, 9 documentation additions. The original model/study, old runner/reference, H1 libraries, C1 and archives were not changed in this correction.
- **Stacked design base:** PR60 `58ca02b293f2afbd931ab7ad1832fc4e34df1574`; **synthetic PR commit** `71416580726e47f41e9f3ec6fa1f59f8f3cb309b`, tree **identical** to the corrected source, with parents design base then corrected head. GitHub identifies PR62 as **draft/open/unmerged**.

## Independent adversarial execution and provenance

I inspected the exact corrected GitHub code and commit patch, then **personally executed isolated Python guard/arithmetic probes** using the F-01 typed comparator and F-02 `exp_step` logic transcribed from that source; the complete repository was **not cloned or executed as a full module**. I also manually reconstructed the actual `reference-facts.json` bytes; local SHA-256 equals pinned **`39f18db09fa618bc73bbe75ca40f33d41ded70a1c73865b2a0e376973d9adfbf`**. Model/study file-byte checks, complete source-only grids, the full test suite, hosted ZIP CRCs and artifact rehashes were **not** independently rerun here. The original source and its Modelica/study pin verification were inspected in code. No OpenModelica was run, queried, installed or built.

**Personally executed F-01 controls:** 24 distinct mutations of the authentic parsed facts object all **REFUSED** at the exact-type/recursive-value guard in the isolated harness, with no construct call or output-directory creation: tiny T10 conductivity change, both rod endpoints, circular diameter, both boundary temperatures, body temperature/capacity, analysis horizon/grid/solver, node order, model/study identities, provenance/source identity, extra/missing keys, boolean-for-int, float/int-for-Decimal, equal-numeric-but-different-`Decimal.as_tuple()` representation, and wrong list type. Tampering the raw facts bytes refused under its SHA check. An untouched typed deep copy and dict insertion-order permutation passed; a separately obtained private canonical snapshot was distinct from the caller object. **Code inspection of real `certify` establishes that `read_facts()` and this comparison precede `construct` and output creation, followed by `s=pinned`. F-01: PASS within this scope.**

**Personally executed F-02 ordinary controls:** 16 invalid-matrix/grid checks **REFUSED** in the isolated corrected implementation: original reviewer's `[[I(1)]]`, `[[0,0],[1,0]]`, a final interval `I(-1,1)` and one-sided nonzero intervals, malformed/empty/ragged/8×8 matrices, raw or wrongly typed interval entries, and zero/negative/float/bool grids. Positive affine 2×2 and representative 7×7 inputs passed. I separately assembled the **actual pinned T1-T 7×7** matrix using the source-facts bytes and inspected `construct`/rational-Pi algorithm; the last input row was exactly zero, and one-step `exp_step` passed at **both 2400 and 4800** with exact final identity row, 18 Taylor terms, `rho≈0.00123009101856 / 0.00061504550928`, and tail bounds `≈4.20e-73 / 8.02e-79`. This was **not** regeneration of either full-grid reference JSON.

### F-02 — BLOCKER: admitted list subclass changes between validation and arithmetic

The corrected [`exp_step` implementation](https://github.com/physicsvigilante/sim_heat/blob/b8663d62af605607608fd43cfeb29e44012171ee/qualification/h1_n1/certified_reference.py#L132-L177) uses `isinstance(row, (list, tuple))` and iterates the same caller-controlled row on **three separate occasions**: type checking, affine-zero-row checking, then numerical construction of `x`. A `list` subclass with non-idempotent `__iter__` passes both validation passes with `[0,0]`, then supplies its actual indexed content `[1,0]` during arithmetic. The helper silently overwrites the resulting nonzero final row with exact identity, producing a **false matrix-exponential enclosure**, even though that matrix is admitted by the implemented type checks.

**Minimal executable counterexample, observed in the isolated corrected `exp_step` implementation:**

```python
from fractions import Fraction
from qualification.h1_n1.certified_reference import interval, exp_step

z = interval(0)
one = interval(1)

class SwitchingRow(list):
    def __init__(self):
        super().__init__([one, z])  # indexed final row is [1, 0]
        self.passes = 0
    def __iter__(self):
        self.passes += 1
        if self.passes <= 2:  # entry-type and zero-row validation
            return iter([z, z])
        return iter([one, z])  # arithmetic consumes the nonzero row

r = SwitchingRow()
b = [[z, z], r]
e, _ = exp_step(b, 2400)       # ACCEPTS; r.passes == 3
assert e[-1][0].bounds() == (Fraction(0), Fraction(0))
# For indexed and arithmetically consumed B=[[0,0],[1,0]],
# exp(B/2400) = I + B/2400, so this true entry is 1/2400.
assert not (e[-1][0].bounds()[0] <= Fraction(1,2400)
            <= e[-1][0].bounds()[1])  # FALSE ENCLOSURE
```

**Personal observed result:** three row iterations; returned `e[-1][0]=[0,0]`; exact required value `1/2400`; enclosure check **FALSE**. This is not an OpenModelica issue or a defect in the stable original T1-T matrix, but it defeats the explicit corrected *public helper* fail-closed contract for malformed/caller-controlled matrices. It is a **new targeted counterexample**, separate from the original 1×1/2×2 regressions (which now correctly refuse).

**Required F-02 correction:** reject non-exact container types (`type(b)`, `type(row)` restricted to built-in `list`/`tuple`) **and/or**, preferably, create a private immutable matrix of newly constructed `I(int_lo,int_hi)` cells **once**, then run all shape/type/exact-zero checks **and every arithmetic operation on that same snapshot**. Do not repeatedly trust mutable or overridden caller iteration. Add the above changing-iterator refusal/control and a positive stable source-matrix case. Recheck unchanged primary/dense mathematical trace hashes after the minimal correction; request only another narrow review of this finding, not a complete implementation/design re-review.

## Hosted evidence, trace/status boundary (not personal reruns)

I independently queried GitHub run metadata: corrected-head [push CI `44467515628`](https://github.com/physicsvigilante/sim_heat/actions/runs/44467515628) and [PR CI `44467521226`](https://github.com/physicsvigilante/sim_heat/actions/runs/44467521226) both report `completed/success`, with `head_sha=b8663d62...`. **Chat A**, not this reviewer, reports 16 focused +34 plan +152 H1 tests passing in each, 18-entry valid ZIPs, artifact SHA checks, and entire original source-only primary/dense JSON traces byte-identical to the old candidate (SHA-256 primary `b13877c8d069a60928cf3b23ae007b1a10feb53151f00ffb65a57082a7fc10af`; dense `9ba71a1d2fccb39be071df0647793f6fb844737e2ac9c91bb143546ab8d26b40`). Those claims have **not** been re-established by a personal artifact download or full grid replay and do not resolve this uncovered F-02 bypass.

All previous native-readiness blockers remain: old checking centres still have **seven static 100× REFUSALS** and **eight execution blockers**; the corrected source-only schema still states `independentlyCertifiedReference=false`, `nativeExecuted=false`, `nativeQualified=false`, `runtimeReady=false`; no runner/reference adoption or lost-scorer recovery occurred. The original H1-T1 author trial stays **UNSEALED**. No PR62/PR60/PR59 merge, historical C1 work, native launch, reference promotion or deployment is approved.

**Final scoped outcome:** **F-01 correction accepted; F-02 correction not accepted. Overall CHANGES REQUESTED on `b8663d62af605607608fd43cfeb29e44012171ee`, for the single independently reproduced non-idempotent-matrix-input bypass.**