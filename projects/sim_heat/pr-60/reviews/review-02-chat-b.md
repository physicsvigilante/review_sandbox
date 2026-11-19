# SIM_HEAT PR #60 — Chat B independent targeted F-01 correction review 02

**Verdict: SCOPED PASS — F-01 arithmetic-target DESIGN ambiguity resolved at the exact corrected source HEAD, with the numerical/reference and native-execution gates still CLOSED.** This is an R2 **PRE-NATIVE DESIGN** re-review only. It is **not** approval of the unchanged checking centres, a 100x numerical-reference certificate, native runtime readiness, source merge, or historical qualification.

| Review identity | Independently verified |
| --- | --- |
| Source draft PR | [physicsvigilante/sim_heat #60](https://github.com/physicsvigilante/sim_heat/pull/60), open/draft/unmerged |
| **Exact reviewed HEAD** | `58ca02b293f2afbd931ab7ad1832fc4e34df1574` |
| **Complete source Git tree** | `c31fe1a37a598f30fa5859227a3ccbc5abf5c470` (queried from Git commit object) |
| Prior reviewed source | `469ab08f4b0fbe3144110bae41b57d29695447bb` (original Chat B review-01 is unchanged and applies only to that HEAD) |
| Pinned baseline | `f52613c39c539b2d4543a9838e5658d526fca10e` |
| PR CI synthetic checkout | `0c6f885043a2cdc813f2e82991bedbef822716a2`; **identical complete tree**, parents baseline then corrected HEAD |
| Review scope | F-01 physical-versus-rounded constant targets, accuracy requirements, static regression/refusal controls, boundaries of claimed evidence |
| Reviewer | Chat B, separate conversation/GPT-6; independent in context, not a human audit or distinct trained model |
| Date | 2026-11-19 |
| New report | `review_sandbox/projects/sim_heat/pr-60/reviews/review-02-chat-b.md` |

## 1. What changed, and the scoped decision

I read [REVIEWER-PROMPT-02](../REVIEWER-PROMPT-02.md), [CORRECTION-REQUEST-02](../CORRECTION-REQUEST-02.md), the unmodified [original review-01](review-01-chat-b.md), [Chat A's response](../responses/response-01-chat-a.md), source `AGENTS.md` and the hub protocol/risk policy. Git comparison from the old HEAD to the new HEAD confirms **one corrective commit with exactly five modified files**: `qualification/h1_n1/REFERENCE-CONTRACT.md`, `plan.json`, `check_plan.py`, `tests/test_plan.py` and `.github/workflows/h1-n1-plan-ci.yml`. The full PR still adds twelve N1-only files against pinned main. The original `model.mo`/`study.json`/notes, `experiments/h1_spike/SimHeat.mo`, production `h1`, runner, reference bundles, viewer and historical C1 are outside this correction and unchanged.

**F-01 design correction: PASS, scoped.** The new [reference contract](https://github.com/physicsvigilante/sim_heat/blob/58ca02b293f2afbd931ab7ad1832fc4e34df1574/qualification/h1_n1/REFERENCE-CONTRACT.md) and [machine-readable ledger](https://github.com/physicsvigilante/sim_heat/blob/58ca02b293f2afbd931ab7ad1832fc4e34df1574/qualification/h1_n1/plan.json) prospectively distinguish:

- **P, mandatory physical result:** exact public/source decimal rationals, exact `C=m*c`, `G=k*A/L` and circular `A=pi*d*d/4`, with independent rational Pi enclosure. For each unchanged checking value `v_ref` and rigorous enclosure `[Plo,Phi]`, the obligatory test is `max(|v_ref-Plo|, |v_ref-Phi|) <= epsilon/100`. A failed physical result **refuses**, regardless of binary64 operational agreement.
- **R, declared representation diagnostic:** RN-even binary64 source-literal conversion and specified intermediate operation trees, with an independently derived nearest-binary64 Pi bit pattern. The checking-expression order and **unobserved** Modelica apparent source-order hypothesis are separately pinned. Agreement with R cannot replace P, discard R-to-P error, or attest what OpenModelica/MSL actually did.

The same static native comparison policy (`epsilon=64*ulp(abs(v_ref))`) and **100x tighter** reference-error requirement (0.64 ULP for constants) remain intact. No constant exemption, 80x relaxation, increased ULP limit, absolute floor, native-output-selected target, reinterpreted physical diameter, fused/reassociated operation grant, or reference substitution was found. The 77-export/full-grid and dynamic K/W/J/initial-temperature obligations are not relaxed.

This **resolves the ambiguity in the specification**, but it deliberately does **not** repair the checking numbers. The legitimate outcome at this stage is a well-defined **failed physical gate**.

## 2. Independent arithmetic challenge, all fourteen static exports

I independently recomputed the physical ratios using exact `fractions.Fraction` source-decimal values, a separately written alternating-arctangent rational Pi enclosure (45 terms per arctangent rather than the source checker's 40), and exact rational discrepancies against the pinned float64 hex values. I separately reproduced all fourteen declared checking hex bits using Python binary64 expression evaluation. The independent Pi bracket contains a high-precision cross-check, has width approximately `4.35e-65` and both endpoints uniquely round to `0x1.921fb54442d18p+1`. Python arithmetic is **not** an observation of the Modelica compiler.

The numbers below are `delta_P / (epsilon/100)`, with the strict acceptance boundary **at 1**:

| Static export | Independent upper-ratio (approx.) | Original centre physical 100x |
| --- | ---: | --- |
| `T01.G` | 0.285714 | PASS |
| `T02.G` | **1.518382** | **REFUSE** |
| `T03.G` | 0.345395 | PASS |
| `T04.G` | 0.793269 | PASS |
| `T05.G` | 0.750000 | PASS |
| `T06.A` | **1.235315** | **REFUSE** |
| `T06.G` | **1.039472** | **REFUSE** |
| `T07.G` | **1.181818** | **REFUSE** |
| `T08.G` | **1.083333** | **REFUSE** |
| `T09.G` | 0.634722 | PASS |
| `T10.G` | **3.275000** | **REFUSE** |
| `T_Collar.C` | 0.625000 | PASS |
| `T_Plug.C` | **1.250000** | **REFUSE** |
| `T_Ridge.C` | 0.937500 | PASS |

This reproduces exactly **seven physical refusals**: **`T02.G`, `T06.A`, `T06.G`, `T07.G`, `T08.G`, `T10.G` and `T_Plug.C`**. All fourteen static exports are covered; no failed field was omitted to obtain a green checker result.

**T10.G counterexample (reproduced independently):** `95 * 0.00013 / 0.40 = 247/8000 = 0.030875 W/K` exactly from source decimals. The unchanged checking centre is `0x1.f9db22d0e5602p-6` = 0.030874999999999993 W/K. Exact physical discrepancy is about `7.271960811294776e-18 W/K` versus `64*ulp(v_ref)/100 = 2.220446049250313e-18 W/K`, ratio **3.275**. Treating parsed binary64 literals as exact and suppressing intermediate rounding still leaves approximately **1.285009765625** times the bound; that is not a cure.

**T06.A/G order warning (reproduced independently):** the existing check's `pi*(d/2)**2` and the apparent source `pi*d*d/4` give checking versus source-order hypotheses **one ULP apart** for both `A` and `G` under ordinary Python binary64 evaluation. The corresponding physical upper-ratios are approximately **1.235315** and **1.039472**, respectively. This is **not** native arithmetic evidence. The source's circular input is **diameter d=0.016 m** and its area has units m²; the ledger and checked formulas preserve both.

## 3. Static control and adversarial review

I inspected the corrected [rational checker](https://github.com/physicsvigilante/sim_heat/blob/58ca02b293f2afbd931ab7ad1832fc4e34df1574/qualification/h1_n1/check_plan.py), [negative tests](https://github.com/physicsvigilante/sim_heat/blob/58ca02b293f2afbd931ab7ad1832fc4e34df1574/qualification/h1_n1/tests/test_plan.py) and [plan-only workflow](https://github.com/physicsvigilante/sim_heat/blob/58ca02b293f2afbd931ab7ad1832fc4e34df1574/.github/workflows/h1-n1-plan-ci.yml).

- The checker uses positive exact rational arithmetic and RN-even quotient/remainder parity; handles ties, carry and subnormals, and explicitly refuses overflows. Its Pi enclosure uses the exact Machin identity plus the alternating remainder, not an unbounded approximate Pi literal. Per-entry source facts are compared as exact rationals to independently parsed `reference-facts.json`; expected exports are derived from all source-fact body/rod inventories, not a hand-picked passing subset.
- `physical_certificate` checks both enclosure endpoints with exact rational `epsilon/100`. Only after constructing independent P/R targets does the probe compare existing checking bits. It reports `roundingConsistency=EXACT_MATCH_NOT_PHYSICAL_CERTIFICATION` separately from `physical100x=REFUSED` and **never** upgrades a passing R check to a physical pass.
- The test file contains separate RN-even tie/carry/subnormal/overflow probes, Pi-bracket probe, T10 exact and parsed-input failures, T06.A/G one-ULP hypotheses, all-fourteen coverage and exact checking-bit comparison. Negative controls cover missing/duplicated exports, changed source decimal/diameter, modified operation order, incorrect Pi bit or fabricated compiler attestation, target-fitting, reassociation, removed exemption guard, 80x or 128-ULP widening, and exact-budget pass versus just-over-budget refusal. Tests for hypothetical witness adoption or historical-reference rewriting also refuse.
- The checker outputs `REFUSED_UNCHANGED_CHECKING_CENTRES` with the seven failures, and preserves the **eighth** execution blocker `STATIC_CHECKING_CENTRES_FAIL_PHYSICAL_100X_BOUND`. The workflow asserts that result, all 14 static exports, **eight blockers**, `nativeCallsThisCheck=0`, `referenceAccuracyCertified=false` and `nativeExecutionReady=false`. It does not install or run OpenModelica.

The witness probe rounds the physical enclosure only if its endpoints produce the same float64. For each of these fourteen constants it finds a possible centre within the 0.64-ULP physical budget (e.g. T10 `0x1.f9db22d0e5604p-6`); **all witnesses remain non-adopted**. They are examples of mathematical feasibility, **not** saved checking values, new sealed bundles, native results, or a trajectory certificate. The unchanged runner re-prepares the original checking algorithm; manually swapping values in a bundle would violate the bound seal. Any future use of witnesses requires a **new prospective checking implementation and version**, independent review, complete dynamic/integral certification, new N1-only seals/replays and exact runner binding.

**No new F-01 design blocker found.** An additional future edge-case property test near maximum-finite binary64 would be a useful optional hardening measure for a general rounding library; it does not invalidate the reviewed positive-source-input, fail-closed arithmetic design.

## 4. Exact-source hosted verification, with attribution

I **personally queried GitHub metadata/steps/logs** for the current runs. All returned completed **SUCCESS**; I observed `Ran 34 tests` and `Ran 152 tests` in **each** plan job, source preservation and docs-parity steps succeeded, and saw the eighth refusal blocker in their plan-check outputs. These are **186 distinct passing tests per plan job**, not 372 distinct tests across two overlapping runs. The tests confirm the checker **correctly refuses** its seven static centres; they do not certify those values.

| Run | Personally checked hosted outcome | Artifact metadata observed |
| --- | --- | --- |
| [Push 44376836623](https://github.com/physicsvigilante/sim_heat/actions/runs/44376836623) | `head_sha=58ca02b...`, plan-only job `135058109724` PASS, 34 + 152 tests and docs parity | ID `14460713898`, 1,457,976 B, provider SHA256 `d372964c84a6986b7d56219eb64b4126e5c62f705eb0ba99b1a77f66e0af5818` |
| [PR 44376848205](https://github.com/physicsvigilante/sim_heat/actions/runs/44376848205) | Corrected source head and exact-tree synthetic checkout, plan-only job `135058149402` PASS, 34 + 152 tests and docs parity | ID `14461696589`, 1,457,978 B, provider SHA256 `2f45c1ae60ac2e75814a3eb4c9a82f74f5faee84e4cd5410d2e97c7644e12928` |
| [Audit 44376847910](https://github.com/physicsvigilante/sim_heat/actions/runs/44376847910) | Audit job `135058146596` PASS, including hosted offline-archive replay and browser-smoke steps | ID `14462475448`, 5,874,377 B, provider SHA256 `30baefd86bebfd19489971f7902cb4ecc15f14f13fd705123e37862264032305` |

**Personal work:** pinned Git objects/diff, source contract/checker/tests/workflow, relevant Modelica and existing reference arithmetic, hub rules/reports, independent fourteen-export exact-rational/Pi arithmetic and Python binary64 checking-order probes, hosted CI run/step/log and provider artifact metadata inspection. **Not personally executed:** corrected repository unit suites, artifact ZIP download/CRC/tree reconstruction, six original archive byte replays, Chromium interaction, source reference preparation or any native simulation. Chat A separately **reports** personal ZIP rehash/CRC checks and source.tar tree reconstruction; my checks above independently verify **provider metadata** and the relevant Git tree, **not those downloaded ZIP bytes**. The historical six archives' `BYTE_IDENTICAL` receipt and `nativeExecutedByReplay=false` are hosted records, not a fresh N1 model execution or independent archive replay by me.

## 5. Still-closed gates — explicitly not accepted by this review

1. **Current static centres fail physical 100x on seven exports**. The independent full-trajectory 100x physical/reference certificate is still **absent**: no validated all-time interval dynamics/integral implementation, no all-77-export primary/dense coverage, and no completed eight-public-observation certificate. Static witness feasibility does not satisfy this gate.
2. The separately reviewed **checking implementation/version plus actual runner re-preparation binding** and three newly certified, twice-replayed, host-specific N1-only reference bundles/seals do not exist. Existing checking values/bundles cannot be patched or historical C1 regenerated.
3. The **primary-only exact-common-time companion comparator** is not implemented/reviewed; four previously identified primary/dense **flow allowance mismatches** remain separate from the seven physical-constant failures. No max/sum/widened allowances or interpolation.
4. Actual host/image/compiler binary/MSL identity, authenticated exact execution manifest, read-only input and credential isolation, memory/storage/network containment, durable **single-use 3 version queries / 3 fresh builds / 3 launches / zero retries**, and **separate explicit owner native permission** remain absent. **Actual new native counts are zero**. A future 0–2400 s finite-window campaign must not be relabeled equilibrium or historical C1 qualification.
5. PR60 and evidence-only PR59 remain draft/unmerged. All old C1 evidence and six archived diagnostic results retain their original meanings; no `nativeQualified=true` promotion. The original H1-T1 private scoring key remains lost/**UNSEALED**, and source-only requested values remain `not_computed`.

## Disposition

**F-01 is closed at the PRE-NATIVE ARITHMETIC-DESIGN SPECIFICATION level only: SCOPED PASS.** The correction makes the physical oracle target unambiguous, prospectively fixes the separate binary64 rounding diagnostics, independently reproduces the counterexamples and all seven precision refusals, and retains the exact stricter limits. It **does not** close the numeric-reference accuracy gate or confer execution readiness. Keep this report as an additive review of the new HEAD; [review-01](review-01-chat-b.md) remains unchanged and valid for its old HEAD.

**Stop:** no OpenModelica installation/version query/build/launch, no native runner, no source merge, no historical C1 integration, no frozen-reference regeneration, no unreviewed witness adoption, no diagnostic promotion or deployment.