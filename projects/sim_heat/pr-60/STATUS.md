# SIM_HEAT PR60 — F-01 design correction tested; targeted review pending, native hold

**Current state:** `REVIEW01_CHANGES_REQUESTED_OLD_HEAD; F01_REPRODUCED; CORRECTED_ARITHMETIC_SPECIFICATION_PUBLISHED; EXACT_HEAD_OFFLINE_CI_PASS; TARGETED_R2_REVIEW02_PENDING; SEVEN_STATIC_PRECISION_REFUSALS_RETAINED; EXECUTION_NOT_READY; NATIVE_CALLS_ZERO; DRAFT_UNMERGED`.

## Exact candidate and review history

[PR60](https://github.com/physicsvigilante/sim_heat/pull/60) remains open, draft and unmerged on branch `planning/h1-n1-t1t`. Current HEAD **`58ca02b293f2afbd931ab7ad1832fc4e34df1574`**, complete Git tree **`c31fe1a37a598f30fa5859227a3ccbc5abf5c470`**. Baseline main remains `f52613c39c539b2d4543a9838e5658d526fca10e`, tree `0c44961b473d23737b0c9f3b3f2cd3db65b9f264`. Successful current PR CI synthetic checkout `0c6f885043a2cdc813f2e82991bedbef822716a2` has the identical full candidate tree, with ordered parents main then current HEAD.

Original independent [Chat B review-01](reviews/review-01-chat-b.md), immutable blob **`8d0712c75c56f7fa13b7bb80f7bebe63964b8abb`**, returned **CHANGES REQUESTED** on old HEAD `469ab08f4b0fbe3144110bae41b57d29695447bb`, tree `7e2158153d0ef8aa7e8afa3d12a0b996e2af49db`. Its single material F-01 asks for explicit physical-versus-floating arithmetic targets before applying the 100x reference certificate to constants. Other source/finite-window/budget design findings were positive but did not establish runtime readiness. Original report remains unchanged. [Chat A response-01](responses/response-01-chat-a.md) accepts and reproduces F-01, records the correction and does not claim independent closure.

Only **five N1 plan/check/test/workflow files changed** after the old review: REFERENCE-CONTRACT.md, plan.json, check_plan.py, tests/test_plan.py and the offline plan workflow. Relative to main the full PR still has **twelve additions and no existing production file changes**. Original T1-T model/study/notes, H1 parser/physics/numerical policy, native runner, source viewer and frozen historical C1/reference/archives remain unchanged. Evidence-only PR59 remains separate/draft/unmerged; duplicate PR61 remains closed without merge and is not an alternative review target.

## F-01 correction, without an accuracy waiver

The new prospectively pinned ledger covers all **fourteen static C/G/A exports** with exact decimal inputs, units, physical formulas, checking-operation order and a separate source-order hypothesis. **Level P**, the exact physical mathematical enclosure (with independent rational Machin Pi bounds), remains the mandatory `delta_P <= epsilon/100` target. Static native comparison still uses **64 ULP**; the reference budget is therefore **0.64 ULP**. No exemptions, widened budgets, fitted targets or changed physical inputs.

**Level R** gives explicitly declared RN-even binary64 input/intermediate rounding. Exact operational agreement is only representation consistency: it cannot replace P or hide its R-to-P discrepancy. The independently bracketed nearest Pi is not an attestation of an actual OMC/MSL value, folding order or native result.

Original T10.G failure reproduced: exact physical `247/8000`, unchanged checking 0.030874999999999993, discrepancy **3.275 times** the reference-error budget. T06.A/G source-order hypotheses differ from checking by one ULP; no native solver output was observed. A standalone initial reproduction requiring physical accuracy failed all three expected T10/T06 controls. Corrected regression tests verify those refusals; they do not declare the original checking values accurate.

The all-export check now records **seven current physical100x refusals**: `T02.G,T06.A,T06.G,T07.G,T08.G,T10.G,T_Plug.C`. These are separate from the earlier four dense-grid flow-allowance mismatches. New eighth execution blocker: `STATIC_CHECKING_CENTRES_FAIL_PHYSICAL_100X_BOUND`. The status is explicitly `REFUSED_UNCHANGED_CHECKING_CENTRES`, not a certified reference.

Correctly rounded mathematical-centre examples show a feasible source-defined alternative for these constants, but are **NON-ADOPTED witnesses**. They do not replace checking values, saved references/seals, native fields or full-grid dynamics certificates. Future use requires a separately versioned/reviewed generic N1 checking-reference implementation and actual runner re-preparation binding; hand-editing an old sealed reference is prohibited. No original or historical reference was regenerated.

## Exact-current-source verification

[Push **44376836623**](https://github.com/physicsvigilante/sim_heat/actions/runs/44376836623), [PR **44376848205**](https://github.com/physicsvigilante/sim_heat/actions/runs/44376848205), and [audit-core **44376847910**](https://github.com/physicsvigilante/sim_heat/actions/runs/44376847910) all completed **SUCCESS**. Each plan job runs **34 focused plan/arithmetic/negative tests +152 inherited H1 tests =186 unique passes**, plus docs parity. All readiness flags remain false, native calls zero, eight blockers and seven precision refusals retained. Passing a refusal regression is not physical numerical qualification. Counts overlap across local/push/PR runs and are not additive.

- Push artifact **14460713898**: 1,457,976 bytes; SHA256 `d372964c84a6986b7d56219eb64b4126e5c62f705eb0ba99b1a77f66e0af5818`; **10 unique CRC-valid ZIP entries**.
- PR artifact **14461696589**: 1,457,978 bytes; SHA256 `2f45c1ae60ac2e75814a3eb4c9a82f74f5faee84e4cd5410d2e97c7644e12928`; **10 unique CRC-valid ZIP entries**.
- Audit artifact **14462475448**: 5,874,377 bytes; SHA256 `30baefd86bebfd19489971f7902cb4ecc15f14f13fd705123e37862264032305`; **33 unique CRC-valid entries**. Hosted archive receipt records D1/D2/DEV_BRIDGE/TEACH_RING4/S1/D2_K2 **BYTE_IDENTICAL**, `nativeExecutedByReplay=false`; existing explorer Chromium steps PASS.

Chat A personally downloaded/rehashed/CRC-checked all three current artifacts and reconstructed both complete plan source.tar trees to exact `c31fe1a37a598f30fa5859227a3ccbc5abf5c470`. Local exact-source 34+152 tests, checker and docs parity passed. The original archive replay/browser smoke are hosted executions inspected, not personally rerun or new native work. Original review-01's earlier 168-test evidence remains historical at its old head; new results do not retroactively approve that old design.

## Narrow review and execution gates

[CORRECTION-REQUEST-02](CORRECTION-REQUEST-02.md) and [REVIEWER-PROMPT-02](REVIEWER-PROMPT-02.md) request **one targeted R2 re-review of F-01**. Independent Chat B should write NEW `reviews/review-02-chat-b.md`. No new report exists at this update. Review the explicit arithmetic targets, exact bounds and refusal controls, non-adopted witnesses and preserved limits—not another whole-project/source-authorability audit. A scoped design pass would resolve the specification question only; it would not clear numerical failures or certify an absent implementation.

The original source-preserving 0–2400 s case and future primary/tight/dense proposal remain unchanged, with a potential maximum 3 queries/3 builds/3 launches/zero retries only after later authorization. Actual counts remain zero. Full independently certified trajectory/reference implementation, improved checking centres and runner binding, primary-only companion comparator, actual compiler/MSL/host identities, all new host-replayed reference seals, durable one-shot containment and explicit final owner permission remain required before execution.

**No merge, OpenModelica installation/query/build/launch, native runner, old-reference regeneration, historical C1 integration, qualification promotion or deployment is authorized/performed.** H1-T1 remains UNSEALED because its private scorer key was lost. Original authored outputs remain not_computed and six archived cases diagnostic_only/nativeQualified=false.
