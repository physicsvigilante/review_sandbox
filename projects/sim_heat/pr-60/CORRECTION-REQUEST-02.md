# SIM_HEAT PR60 — targeted R2 correction review 02: F-01 constant-arithmetic targets

**PRE-NATIVE DESIGN ONLY. No native execution, compiler query, installation, build, launch, production merge or reference replacement authorized.** Review the F-01 correction and its implications, not the whole unchanged project or the previously accepted T1 source-authoring trial.

## Exact source and independent history

| Item | Pin |
|---|---|
| Source PR | [physicsvigilante/sim_heat draft PR60](https://github.com/physicsvigilante/sim_heat/pull/60), branch `planning/h1-n1-t1t` |
| **New corrected HEAD** | **`58ca02b293f2afbd931ab7ad1832fc4e34df1574`** |
| **New complete Git tree** | **`c31fe1a37a598f30fa5859227a3ccbc5abf5c470`** |
| Old reviewed HEAD/tree | `469ab08f4b0fbe3144110bae41b57d29695447bb` / `7e2158153d0ef8aa7e8afa3d12a0b996e2af49db` |
| Pinned main/tree | `f52613c39c539b2d4543a9838e5658d526fca10e` / `0c44961b473d23737b0c9f3b3f2cd3db65b9f264` |
| Actual successful PR CI checkout | `0c6f885043a2cdc813f2e82991bedbef822716a2`, **same complete tree as current HEAD**, ordered parents pinned main then corrected HEAD |
| Original independent report | [Chat B review-01](reviews/review-01-chat-b.md), immutable blob `8d0712c75c56f7fa13b7bb80f7bebe63964b8abb`, **CHANGES REQUESTED** for old source |
| Developer disposition | [response-01-chat-a](responses/response-01-chat-a.md): accepts/reproduces F-01; no independent closure claim |
| New reviewer report | **NEW** `projects/sim_heat/pr-60/reviews/review-02-chat-b.md` |

One corrective commit changes exactly **five existing N1 paths**: `REFERENCE-CONTRACT.md`, `plan.json`, `check_plan.py`, `tests/test_plan.py`, and `.github/workflows/h1-n1-plan-ci.yml`. The full PR still adds exactly **twelve** plan/input/test/workflow paths relative to main. All original T1-T model/study/notes, production H1 physics/parser/reference/policy, Modelica library, native runner, source viewer, archived results and historical C1 remain unchanged. Original model SHA256 `2c60e40f1ad8d85f46968f03712d23e8cd6b9c656cf6099a38a97d198d0873ae`; original study SHA256 `12ad51f59d2bd6c6561d4059f68b4263e7d4e39cdf5493f353a7affee6929d2a`.

Read the original independent report, this correction, exact new contract/ledger/checker/tests and unchanged underlying formulas. Follow source AGENTS and the central protocol/risk policy. Original review-01 remains binding to its old source and must not be rewritten.

## The original finding is reproduced, not waived

For T10.G the exact source-decimal physical result is `95*0.00013/0.40 = 247/8000 W/K`. Current checking expression yields `0x1.f9db22d0e5602p-6`, 0.030874999999999993. Its discrepancy is approximately **7.271960811294776e-18 W/K**, while the unchanged static `64 ULP /100` budget is **2.220446049250313e-18 W/K**. Ratio **3.275**, therefore **REFUSE**. Simply treating parsed binary64 literals as exact but ignoring intermediate rounding still misses the budget, ratio approximately **1.285009765625**.

For T06.A/G, the checking radius-squared order and apparent Modelica `pi*d*d/4` order differ by **one ULP** in ordinary binary64. That is larger than the 0.64-ULP reference-certification budget but does not demonstrate failure of the full 64-ULP native comparison. **No actual OMC arithmetic or output was observed.** Chat A first ran a standalone old-code reproduction with physical-pass assertions for T10.G, T06.A and T06.G: all three failed, exit 1. The later passing regression suite intentionally verifies these refusals; it does not relabel the physical failures as accuracy successes.

## What the correction defines

**Level P — physical mathematics, still the mandatory target.** Each exact public/source decimal is a rational; true Pi is independently enclosed using the Machin identity with exact alternating-series remainder. All fourteen C/G/A exports have a per-export ledger of source values, dimensions, physical formulas, checking-order interpretation, separate source-order hypothesis and unchanged checking bits. The mandatory condition remains

`max(abs(v_ref - Plo), abs(v_ref - Phi)) <= epsilon/100`.

For constants, `epsilon = 64*ulp(abs(v_ref))` is unchanged. No exemption, new absolute floor, 80x substitution, summed/maximized allowance or native-output-fitted target is allowed. Dynamic/energy/initial/request budgets remain their prior physical enclosure requirements.

**Level R — separately declared floating-point representation.** An independent exact-rational helper evaluates bounded RN-even binary64 input conversions and intermediate operations, including ties/carry/subnormal behavior. Independent mathematical Pi rounds uniquely to `0x1.921fb54442d18p+1`; this is NOT actual compiler/MSL attestation. Current checking functions are cross-checked only AFTER independently constructing these targets. Agreement with R is **rounding consistency**, never a replacement for P. An R-based proof would still have to include its R-to-P discrepancy. The source-order hypothesis is not an output-selected alternative target; unknown constant folding, reassociation/FMA and native Pi stay unobserved.

**All current physical failures stay explicit.** Seven of fourteen unchanged checking centres fail the physical 100x requirement: **T02.G, T06.A, T06.G, T07.G, T08.G, T10.G, T_Plug.C**. This is distinct from the previously identified four primary/dense flow allowance mismatches. The checker outputs `REFUSED_UNCHANGED_CHECKING_CENTRES` and an eighth execution blocker, `STATIC_CHECKING_CENTRES_FAIL_PHYSICAL_100X_BOUND`. Green design CI requires these failures to remain visible.

**Feasibility witnesses are NOT adopted references.** Only when both endpoints of P round to the same binary64 value does the probe report that uniquely correctly rounded physical centre. The fourteen case-specific witnesses meet the physical 0.64-ULP budget, including T10 witness `0x1.f9db22d0e5604p-6`. This is a source-derived existence check, not a new checking bundle, native value or full certificate. No witness changes `v_ref`, a saved reference, source model or native field. Later use requires a separately versioned/reviewed **generic N1 checking-reference implementation**, full dynamics/integral bounds and independently fixed runtime/re-preparation/seals. The old runner would reject a hand-edited reference bundle. **Current numerical readiness remains false.**

This follows the review's fail-closed option instead of choosing an operational target solely to pass. Please assess whether this removes the design ambiguity soundly, while retaining the genuine numerical implementation blocker.

## Targeted adversarial review questions

1. Is the physical-versus-representation ledger explicit, complete and fixed before native output? Does every static quantity retain the same strict physical 100x gate rather than certifying agreement with its own rounding recipe?
2. Independently reproduce T10.G, parsed-literal intermediate-order warning and T06.A/G physical/order discrepancies. Challenge RN-even ties/carry/subnormal/overflow and the exact rational Pi enclosure. Check all fourteen exports and the seven refused original centres; coverage and source/diameter/units must match.
3. Verify the non-adopted nearest-physical witnesses are not used to repair references or assert execution readiness. Any feasible future checking implementation needs a new prospective version and runner binding, not replacing a frozen centre after output. Check no policy/budget or original-source changes occur.
4. Test or inspect the negative controls: omitted/duplicate field, changed geometry/order/Pi, hypothetical native attestation, fitted target, exemptions, 80x/128-ULP substitution, witness adoption, exact epsilon/100 boundary versus just-over. Source-order hypotheses must not be mislabeled observed OMC results.
5. Confirm unchanged 0–2400 s physical source, proposed 3-query/3-build/3-launch maximum with zero retries, all77-export/full-grid obligations, native hold, historical C1 and original UNSEALED authorability limitation. Full interval-dynamics certificate, comparator, runtime/host seals, containment and owner permission remain absent gates, not achievements.

## Verified exact-current-head CI and attribution

[Push run **44376836623**](https://github.com/physicsvigilante/sim_heat/actions/runs/44376836623) **SUCCESS** at exact source HEAD. Artifact [**14460713898**](https://github.com/physicsvigilante/sim_heat/actions/runs/44376836623/artifacts/14460713898): **1,457,976 bytes**, SHA256 **`d372964c84a6986b7d56219eb64b4126e5c62f705eb0ba99b1a77f66e0af5818`**, **10 unique CRC-valid ZIP entries**.

[PR run **44376848205**](https://github.com/physicsvigilante/sim_heat/actions/runs/44376848205), job135058149402, **SUCCESS** at actual synthetic commit `0c6f885043a2cdc813f2e82991bedbef822716a2`, identical full source tree. Artifact [**14461696589**](https://github.com/physicsvigilante/sim_heat/actions/runs/44376848205/artifacts/14461696589): **1,457,978 bytes**, SHA256 **`2f45c1ae60ac2e75814a3eb4c9a82f74f5faee84e4cd5410d2e97c7644e12928`**, **10 unique CRC-valid entries**.

[Audit-core run **44376847910**](https://github.com/physicsvigilante/sim_heat/actions/runs/44376847910), job135058146596, **SUCCESS**. Artifact [**14462475448**](https://github.com/physicsvigilante/sim_heat/actions/runs/44376847910/artifacts/14462475448): **5,874,377 bytes**, SHA256 **`30baefd86bebfd19489971f7902cb4ecc15f14f13fd705123e37862264032305`**, **33 unique CRC-valid ZIP entries**. Hosted archive receipt records all six D1/D2/DEV_BRIDGE/TEACH_RING4/S1/D2_K2 **BYTE_IDENTICAL**, `nativeExecutedByReplay=false`; existing explorer Chromium steps PASS.

Chat A personally downloaded/rehashed/CRC-checked all three actual ZIPs and reconstructed both plan `source.tar` Git trees to exact **`c31fe1a37a598f30fa5859227a3ccbc5abf5c470`**. Personally executed locally: **34 plan/negative tests +152 inherited H1 tests =186 distinct unit PASSES**, docs parity PASS. Hosted plan jobs show the same counts and preserve eight blockers, seven static precision refusals, zero native calls and no adopted witness. Local/push/PR totals overlap and must not be summed. Original six archive replay and browser smoke are hosted execution inspected through artifacts, not personally rerun locally. No all-grid numerical certificate or native result has been generated.

## Required independent output and stop

Write your own **NEW** `projects/sim_heat/pr-60/reviews/review-02-chat-b.md`, giving **SCOPED PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE** for the targeted **F-01 pre-native DESIGN correction**. State exact source HEAD/tree, personal versus hosted tests, whether the ambiguity is resolved, and every remaining execution gate. A scoped design pass does not turn seven current centre failures into a numerical pass or certify absent implementations. Preserve review-01 and original reproduction failures unchanged.

Do not modify source, merge PR60/PR59, install/query/build/launch OpenModelica, invoke the native runner, regenerate frozen references, integrate C1 history, promote diagnostic results or deploy. Only the original F-01 path warrants renewed scrutiny; do not restart an unrelated whole-project or per-problem review.
