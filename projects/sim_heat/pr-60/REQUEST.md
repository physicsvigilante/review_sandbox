# SIM_HEAT PR60 — H1-N1-P0 independent R2 PRE-NATIVE DESIGN review

**Review the proposed plan, not an unexecuted native result.** No source execution, installation, compiler/version query, original-reference repair, production merge or deployment is authorized. The owner approved **preparing a bounded execution/reference plan** after H1-T1-UNSEALED, with independent review and a later separate execution decision. Do not reinterpret that as native permission.

## Frozen candidate and review scope

| Item | Exact pin |
|---|---|
| Source | [physicsvigilante/sim_heat draft PR60](https://github.com/physicsvigilante/sim_heat/pull/60) |
| Branch | `planning/h1-n1-t1t` |
| **Candidate HEAD** | **`469ab08f4b0fbe3144110bae41b57d29695447bb`** |
| **Candidate Git tree** | **`7e2158153d0ef8aa7e8afa3d12a0b996e2af49db`** |
| Base main | `f52613c39c539b2d4543a9838e5658d526fca10e`, tree `0c44961b473d23737b0c9f3b3f2cd3db65b9f264` |
| Actual PR CI synthetic commit | `04b4860d06de32d7ed26ac9a197f378ac4cb434a`, **same entire candidate tree**, parents baseline then candidate |
| Changed scope | Exactly **12 added paths**: eleven under `qualification/h1_n1/`, one offline plan-check workflow; no existing file modifications/deletions |
| Risk | **R2 prospective physical/numerical/evidence design**, not a completed implementation/native numerical acceptance review |
| Independent output | NEW `projects/sim_heat/pr-60/reviews/review-01-chat-b.md` |
| Present posture | **PLAN REVIEW READY; EXECUTION NOT READY.** Both source PR60 and evidence PR59 remain draft/unmerged. |

Read source `AGENTS.md`, the central `PROTOCOL.md`, `REVIEW-RISK-POLICY.md` and `REVIEW-TEMPLATE.md`. All source paths below mean this exact candidate SHA, never floating main. The prior [PR59 independent report](../pr-59/reviews/review-01-chat-b.md), blob `21263c59bbbd4411e4f5365f3c2e23160e1cf812`, establishes only bounded source-fidelity and offline admission of the original illustrative tasks. No need to repeat that whole review unless a new discrepancy is found.

## Source documents to review

Primary [PLAN.md](https://github.com/physicsvigilante/sim_heat/blob/469ab08f4b0fbe3144110bae41b57d29695447bb/qualification/h1_n1/PLAN.md); [REFERENCE-CONTRACT.md](https://github.com/physicsvigilante/sim_heat/blob/469ab08f4b0fbe3144110bae41b57d29695447bb/qualification/h1_n1/REFERENCE-CONTRACT.md); machine-readable `plan.json`; `reference-facts.json`; `SOURCE-PINS.json`; labelled noncertified `PLANNING-SCREENING.json`; `check_plan.py` and its sixteen tests; exact copied original T1-T model/study/notes; `.github/workflows/h1-n1-plan-ci.yml`.

Verify actual unchanged `tools/h1_native_batch.py`, `tools/h1_resolution_campaign.py`, `tools/h1_compare_companions.py`, `h1/reference.py`, `h1/policy.py`, `h1/temporal.py`, `h1/verification.py`, MAT decoder and `experiments/h1_spike/SimHeat.mo` against source pins. Use current `docs/H1_OFFLINE_AMENDMENT.md`, not superseded whole-network tolerances from the original historical proposed contract. Original `qualification/h1_c1/FREEZE.md` and prior failures are preservation context, not permission to reopen or fix them.

## Proposed physical experiment and strictly bounded operations

One already authored and source-reviewed **T1-T** transient conduction composition: 3 finite bodies, 2 maintained boundaries, 10 rods, 7 logical nodes, 8 public requests. Original model SHA256 `2c60e40f1ad8d85f46968f03712d23e8cd6b9c656cf6099a38a97d198d0873ae`, study SHA256 `12ad51f59d2bd6c6561d4059f68b4263e7d4e39cdf5493f353a7affee6929d2a`.

Preserve its **0–2400 s** horizon and all physical fields/ports/requests/provenance. Three future *single-case* runner invocations: primary exact original descriptor (2400 intervals, DASSL1e-8); analysis-only tight companion (same grid,1e-10); analysis-only dense companion (4800 intervals,1e-8). **Maximum 3 compiler version queries,3 fresh builds,3 launches,0 retries**, not three physical models. Stop at first unexpected failure. All plans/references must be prepared and sealed before even the first OMC version query. Future companion bytes and runnable manifests are **not yet created** here. Current actual native counts all zero.

There is no native launcher, native trigger, compiler script, runtime image download or executable-native schema in this candidate. `plan.json` deliberately says `PLAN_ONLY_NOT_EXECUTABLE`, `nativeExecutionReady=false`, reference certification absent and seven blockers. The existing runner's true GitHub Actions/push/approved-branch/run_attempt=1 guard must not be spoofed. Runtime desired OMC1.27.0/MSL4.0.0 versions are source requirements; actual image, compiler binary, complete MSL and host manifests are **unbound**, not guessed from an old run.

## Findings already discovered — challenge them independently

**A. Runner/campaign incompatibility.** The current batch runner admits at most two cases in one plan and spends one version query per invocation. The older resolution helper hard-codes a 1000-grid three-case/seven-launch campaign and is not a generic substitute. Check that the proposed three ordered one-case calls, explicit query budget, fresh builds and stop policy do not invent binary reuse or hidden probes. No bypass, automatic retry or source parameter override permitted.

**B. Dense-grid allowance mismatch.** New N1-only float64 screening found slightly different primary and dense allowances for `T02.Q_flow`, both its port flows and `T_Warm.Q_to_network`. The unchanged existing companion comparator requires exact equality and would refuse. The design retains each run's own independently presealed per-run tolerances and proposes a **new checking-only comparator using PRIMARY allowance only** for common-time native differences. It must never sum/max/widen budgets or select them after output. Include the derived public temperature difference with its own scale. This comparator is **not implemented or reviewed yet** and remains an execution blocker; do not certify it from prose.

**C. Finite-window versus C1 policy.** Screening decay rates are about `0.00015747,0.00052901,0.00100714/s`; primary hλmax≈0.00101, and five slowest time constants≈31,753s. These are explicitly **uncertified same-author analytic screening** values. N1 preserves the original2400s task and claims no equilibrium or historical C1 five-time-constant completion. Review whether that prospective finite-window scope is scientifically honest, rather than requiring a hidden horizon change to make old C1 policy appear passed.

**D. Independent numerical reference.** Existing float64 expm/spectral agreement is explicitly not a certified reference-error bound. New facts are independently expressed from the already public task, not generated from the H1 parser graph or native output. Proposed checking-only method: weighted Laplacian and interval Schur elimination; dimensionless affine seven-state system including exact energy-integral states; independently bracketed Pi/input arithmetic; outward-rounded Taylor/scaling-and-squaring with normρ≤1/2 and explicit series-tail bound. Require total reference discrepancy ≤ each applicable native allowance/100 on **every assessed primary/dense sample**, all77mandatory exports,8public requests,constants and integrals. Mere extra precision or agreement of two algorithms is insufficient. Carefully challenge interval dependencies, floating-input semantics, static64ULP allowance interactions, transformations, accumulated rounding, units/signs, initial states, conditioning, quadrature and temporal-budget coverage. This is a **method design**, not an implemented/certified oracle. A mathematically unjustified design is a valid blocking finding even though the execution gate is closed.

**E. Host/reference identity and single use.** Before native, the exact actual host/image/OMC/MSL/dependencies, companion bytes, certified reference files, replayed seals, comparator implementation, execution manifest and single-use budget enforcement must be pinned and independently checked. All three NEW N1 references must replay identically in two fresh directories on the bound host before query/build; a different seal cannot replace the first expected value. Do not regenerate historical C1. Existing Python process timeouts do not prove memory/storage/network isolation; proposed 4GiB/512MiB containment needs real host enforcement. A version string, rolling CI image label or overwritten JSON flag is not authentication. Examine how the final approval should bind to a real manifest rather than approving unknown hashes.

**F. Native data and report claims.** Require true MAT data_1/data_2 constants/series and signed alias mappings for all77exports, no reference-filled or guessed missing channels, full-grid/initial/boundary/local rod/junction/body/network conservation and trusted request derivations. Preserve raw files and first failures. Current verifier stays `nativeExecuted=false/nativeQualified=false`, with `diagnostic_only` candidates; a separate future attempt attestation must truthfully distinguish actual run provenance from the verifier's semantics. No source-only or historical diagnostics may be silently promoted.

## What is complete versus explicitly outstanding

**Complete here:** source-preserving plan, exact input copies, separately expressed source-fact binding, finite-grid screening with honest limitations, static/negative plan checker,16 focused tests, unchanged152 H1 regressions, docs parity and exact-head CI. Local Git tree and all published blobs match. No native operations.

**Outstanding before actual execution:** (1) plan's R2 design disposition; (2) actual pinned runtime/host; (3) implemented/validated100x reference certificate, independent-context interpretation and complete error data; (4) all three host-specific reference seals/replay; (5) implemented/reviewed primary-only convergence comparator; (6) exact companion/run manifests and persistent single-use/containment control; (7) explicit final owner permission. The machine-readable plan lists those gates and all readiness flags remain false. A scoped **plan pass must preserve every unsatisfied gate**; it is not sign-off on absent implementations or unseen results.

## Exact-head offline CI and personally verified artifacts

[Push **44364726234**](https://github.com/physicsvigilante/sim_heat/actions/runs/44364726234), job135015310603: **SUCCESS**, actual candidate HEAD/tree. Artifact [**14455733364**](https://github.com/physicsvigilante/sim_heat/actions/runs/44364726234/artifacts/14455733364), **1,442,847 bytes**, SHA256 **`80f0576bc65ee41592ffa42cfc2bd324f6d82dac878023b87b7de2240e367d43`**,10uniqueCRC-valid entries.

[PR **44364885661**](https://github.com/physicsvigilante/sim_heat/actions/runs/44364885661): **SUCCESS** at synthetic commit `04b4860d06de32d7ed26ac9a197f378ac4cb434a`, same complete candidate tree. Artifact [**14456348414**](https://github.com/physicsvigilante/sim_heat/actions/runs/44364885661/artifacts/14456348414), **1,442,844 bytes**, SHA256 **`e71ecd0dc000da8afc76fd75f1b3f20b25d96d0b8453f5ff5dff09fb5bcf0c41`**,10uniqueCRC-valid entries.

Both plan CI runs: **16 plan/negative +152 original H1 =168 unit passes**, docs parityPASS; exact12added-path receipt; native calls0; `nativeExecuted=false`, `nativeQualified=false`, `nativeExecutionReady=false`, `referenceAccuracyCertified=false`,7blockers. These tests check the P0 contract, not nonexistent reference-certification software. Local developer exact-source same168 tests and parity also passed; overlapping counts are not additive. Chat A personally downloaded/rehashed both ZIPs and reconstructed their source.tar Git trees to exact`7e215815...`.

Existing [audit-core **44364885768**](https://github.com/physicsvigilante/sim_heat/actions/runs/44364885768), job135015858358: **SUCCESS**. Artifact **14455918630**, **5,874,362 bytes**, SHA256 **`678b10b040b4c7c6b9c48ecc59ccbf30b4faa2e985e347660f8f2eb0128cb060`**,33uniqueCRC-valid entries, personally downloaded/verified. Hosted receipt records **D1,D2,DEV_BRIDGE,TEACH_RING4,S1,D2_K2 all BYTE_IDENTICAL**, `nativeExecutedByReplay=false`; old explorer desktop/mobile/refusal smokePASS. Chat A inspected these hosted receipts; it is not a fresh local replay or native simulation. The plan itself adds no browser feature, so no separate new UI review is needed.

## Required review and stopping point

Start a fresh reviewer context, read pinned sources and original public task, challenge the **design and safeguards** independently, and report only actually executed offline probes versus inspected hosted evidence. Do not perform compiler/version/install/build/launch probes or native preflight while reviewing. Do not edit any original source, the reviewer history or prior C1/T1 records.

Write **your own NEW** report to `physicsvigilante/review_sandbox/projects/sim_heat/pr-60/reviews/review-01-chat-b.md`. Give **SCOPED PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE**, explicitly for **pre-native design only**. Identify concrete plan defects and smallest corrections, separate acceptable design from open readiness gates, and do not treat absence of intentionally deferred native data as if a native acceptance claim had been made. Conversely, do not accept an unsound reference or host control design merely because execution is blocked.

This is **one coherent R2 scope**. Later checking implementations/readiness evidence need targeted examination of the changed critical parts, not repeated broad review of unchanged source fidelity. Actual numerical results require later evidence assessment; a prospective pass cannot certify future results. Do not merge PR60 or PR59, execute OpenModelica, regenerate original references, integrate historical C1 or deploy. The earlier H1-T1 key custody limitation, original source-only `not_computed` values and six historical `diagnostic_only/nativeQualified=false` cases remain unchanged.