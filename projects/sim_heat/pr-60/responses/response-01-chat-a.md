# PR60 — Chat A disposition of independent pre-native review-01

**Accept/reproduce F-01; corrected design candidate published, independent targeted disposition pending. No native execution or merge authority.**

Independent [Chat B review-01](../reviews/review-01-chat-b.md), immutable blob `8d0712c75c56f7fa13b7bb80f7bebe63964b8abb`, returned **CHANGES REQUESTED** on original HEAD `469ab08f4b0fbe3144110bae41b57d29695447bb`, tree `7e2158153d0ef8aa7e8afa3d12a0b996e2af49db`. It identified one material design ambiguity: what independent arithmetic target the mandatory 100x reference certificate uses for static C/G/A exports. Its positive findings on original source preservation, finite-window scope, bounded three-invocation proposal and intentionally closed runtime gates are retained; they do not constitute native permission or a completed numerical certificate.

## Reproduction, not a native failure

Chat A reconstructed the exact old source tree from original PR60 CI artifact 14456348414 (ZIP SHA256 `e71ecd0dc000da8afc76fd75f1b3f20b25d96d0b8453f5ff5dff09fb5bcf0c41`), then evaluated source arithmetic only. No OMC binary, native runner or reference trajectory was invoked.

For `T10.G`, exact source decimals imply `247/8000 W/K`. The unchanged checking expression returns binary64 `0x1.f9db22d0e5602p-6`, or 0.030874999999999993. The absolute physical discrepancy is 7.271960811294776e-18 W/K against an unchanged `64 ULP /100` budget of 2.220446049250313e-18 W/K: **3.275 times budget**, so the physical certificate must refuse. Exact rational arithmetic on parsed binary64 literals without intermediate rounding still exceeds the budget (ratio about 1.285009765625). A standalone three-control reproduction requiring the old checking values to meet the physical gate actually exited 1 with **three failures** for T10.G and T06.A/G. These are preserved numerical-design failures, not failed native runs or passed physical certificates.

For circular T06, the checking expression `pi*(d/2)**2` and the apparent Modelica source-order hypothesis `pi*d*d/4` differ by one binary64 ULP in both A and derived G. That one ULP exceeds the 0.64-ULP certification budget but not the full 64-ULP native comparison allowance. Actual OMC/MSL folding and arithmetic were **not observed**.

## Exact correction and deliberate stop

Current candidate **`58ca02b293f2afbd931ab7ad1832fc4e34df1574`**, tree **`c31fe1a37a598f30fa5859227a3ccbc5abf5c470`**, one commit after the reviewed head. Exactly **five existing N1 plan paths** changed: REFERENCE-CONTRACT.md, plan.json, check_plan.py, tests/test_plan.py, and the offline-only plan CI workflow. All five published Git blobs and the complete Git tree equal the locally tested bytes. The full PR still has the original twelve additions relative to baseline main `f52613c39c539b2d4543a9838e5658d526fca10e`. No original model/study/notes, H1 production implementation, Modelica source, numerical tolerance, reference bundle, runner, viewer or historical C1 bytes changed.

The correction fixes an explicit **two-level, per-export ledger** for all fourteen static exports:

- **P:** exact public/source decimal mathematics, with independent exact-rational Machin Pi enclosure. This remains the **mandatory** `delta_P <= epsilon/100` target. Constants are not exempted; the native comparison allowance remains 64 ULP, with no added floor or widened limit.
- **R:** prospectively declared RN-even binary64 input conversion and intermediate-operation trees. Checking bits and source-order hypotheses are distinct. Exact agreement with R is only rounding consistency and **cannot replace** the physical P bound or omit R-to-P discrepancy. Compiler identity, Pi and reassociation remain unobserved, not authenticated by these probes.

New exact-rational RN-even/Machin checks reveal **seven unchanged checking centres fail the physical 100x condition**: T02.G, T06.A, T06.G, T07.G, T08.G, T10.G and T_Plug.C. These are not the earlier four primary/dense flow-allowance mismatches. They remain explicitly reported as `REFUSED_UNCHANGED_CHECKING_CENTRES`, with an eighth readiness blocker `STATIC_CHECKING_CENTRES_FAIL_PHYSICAL_100X_BOUND`. Green plan tests confirm these refusals; they do not make the centres accurate.

For each constant, the probe also shows that a uniquely correctly rounded exact-physical value could meet the 0.64-ULP bound. These are **non-adopted feasibility witnesses**, selected from mathematical source facts, not native output. They do not replace `v_ref`, edit a bundle/seal, or supply any native field. Use later would require a separately versioned/reviewed generic checking-reference implementation, complete dynamics/integral certificate, new N1-only seals and exact runner re-preparation binding. The unchanged runner would reject a hand-edited reference seal. No historical references are regenerated, and no existing physical result is promoted.

## Verification and remaining limits

Personally executed locally on the byte-verified corrected tree: **34 plan/negative tests** (16 inherited plus 18 arithmetic controls), **152 inherited H1 tests**, and product Markdown/HTML parity, all PASS. Controls cover T10/T06 reproductions, all fourteen static exports, the seven known refusals, exact RN-even ties/carry/subnormals, independent Pi enclosure, actual unchanged checking-function bit correspondence, budget equality and just-over-budget/80x refusal, wrong inputs/diameter/order/Pi, omitted fields, forbidden target fitting, invented native attestation and prohibited witness adoption. This is **186 distinct unit passes**, not a full all-grid reference certificate.

The checker retains `nativeExecutionReady=false`, `referenceAccuracyCertified=false`, `nativeCallsThisCheck=0`, and eight explicit blockers. The machine-readable plan was compactly serialized, but unchanged budget/horizon/physical fields are checked by retained regressions. Exact-current-head hosted run/artifact evidence is recorded in the cycle-02 correction request/status after actual completion. No old reviewer-authored report or original evidence was modified.

## Review scope and authority

Request **targeted R2 re-review of F-01 only**, including the explicit physical target, separately justified representation ledger, exact probes, non-adopted witness boundary and retained failure gate. Do not repeat the entire original T1 source-fidelity review or demand native runs to review a plan that prohibits them. Do not infer a pass on the new source from old green CI or from Chat A's correction claim.

PR60 remains draft/unmerged; evidence-only PR59 remains unmerged; duplicate PR61 stays closed without merge. Full interval-dynamics certification, companion comparator, actual host/runtime identity, new reference seals, one-shot containment and separate owner native permission remain outstanding. **No OpenModelica install/query/build/launch, native runner, frozen reference regeneration, historical C1 integration, deployment or production merge occurred.** Original H1-T1 private-key loss remains UNSEALED and all source-only requested thermal outputs remain not_computed.
