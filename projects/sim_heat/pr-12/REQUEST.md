# SIM_HEAT PR #12 — R2 integration-review request

- **projectId:** sim_heat
- **sourceRepo:** `physicsvigilante/sim_heat`
- **sourcePR:** https://github.com/physicsvigilante/sim_heat/pull/12
- **baseSha:** `49a2cc42462b47026e86313bfeff39a9b17081cd` (original `main`, source PDF only)
- **headSha:** `f2bb5369425a250cef78b74baaf486925f8fa6bd` (**exact candidate; do not review floating branch heads**)
- **sourceTreeSha:** `92fd29ee3b55ef6e49e438dd326ea159b7cdb446`
- **reviewClass:** **R2 — physical/evidence critical** (first promotion of simulation, checking and native-runner code to main, even though physical implementations were imported unchanged)
- **scope:** bounded source integration/release-readiness review of reusable H1 thermal-network engine; focus on contracts, negative controls, native provenance, accurate status labels and source identity. **Not** a new physics implementation, blind held-out case, classroom trial, or automatic acceptance of all historical experiments.
- **review destination:** `projects/sim_heat/pr-12/reviews/review-01-chat-b.md` — a **new** file authored by Chat B on central `main`, or on a separate central review-only PR if necessary. Do not overwrite reports.
- **status:** `awaiting-review`; Chat A has not performed or impersonated the separate-chat review.

## Final-head CI and immutable evidence

**Current offline CI:** https://github.com/physicsvigilante/sim_heat/actions/runs/43723198188 — **SUCCESS**, attempt 1, exact head `f2bb5369425a250cef78b74baaf486925f8fa6bd`.

- Python 3.13.5 / NumPy 2.3.5 / SciPy 1.17.0; checking-only mpmath 1.3.0; Ubuntu 24.04 host.
- Current source's **149/149** H1 unit tests and **4/4** original analytical reference arithmetic tests passed.
- Developer bridge study admission passed (`admitted=true`, `nativeExecuted=false`); the separately authored checking-only reference prepared and sealed. This is not native execution or independent reference authentication.
- **CI artifact:** https://github.com/physicsvigilante/sim_heat/actions/runs/43723198188/artifacts/14165546204 ; name `h2-h1-offline-evidence-f2bb5369425a250cef78b74baaf486925f8fa6bd`; **SHA-256:** `e5214690068af2bc596daa6da75374610970396aaeb7dfb661951e2cacf2bdb4`, 647,502 bytes. Contains commit identity, 111 tracked source-file hashes, test logs, resolved dependency versions, admission and prepared-reference records. Chat A downloaded the ZIP and checked CRC, test counts, pinned head and offline status; reviewer should verify independently as feasible.
- **Zero native compiler builds/launches** in this integration CI. The workflow does not install OpenModelica or invoke a native runner.

**Prior real native evidence (historical, not source-head CI or independent external confirmation):**
- S1 MATv4 first-run failure and post-hoc adapter correction: https://github.com/physicsvigilante/sim_heat/actions/runs/43689753800 — original failure preserved.
- D1/D2 transients: https://github.com/physicsvigilante/sim_heat/actions/runs/43691263273 ; artifact 14152886226, SHA-256 `8fc38b9e2f040b48ab5cbeab34e8698b7c99c4d462a1e31e8bc33b0395185379`.
- Conductivity revision and grid/tolerance companions: https://github.com/physicsvigilante/sim_heat/actions/runs/43693191224 ; artifact 14153251022, SHA-256 `dc32a0a36a27f031ce7a13da83ebdd26a3dd6ac1d14612fa597b36cb439f4843`.
- Developer-authored two-body/two-reservoir/five-rod bridge: https://github.com/physicsvigilante/sim_heat/actions/runs/43699424883 ; artifact 14155084346, SHA-256 `f16975a25eea79f61f7819fb9e704ab04a33630044a51a0d062b8399c1c9ce38`; 42 mandatory outputs and 98/98 diagnostic checks; separate-author C1 **not** executed.

## Source identity and curation assertions to challenge

Imported from exact native-tested experiment head `a314671828b32b24876250a84f5c057c9d93411f` on PR #10. Expected Git identities at the integration head:

| Path | Expected Git tree/blob identity |
|---|---|
| `h1/` | tree `3f695b7a68bc6e344ae2512886ca7d9fffd9a539` |
| `experiments/` | tree `895f450964832465d7f1d84099c2ab444ddc1094` |
| `qualification/` | tree `e2f741e3ee535236f628d3559b7a95d6c7935a34` |
| `tools/h1_native_batch.py` | blob `6e6d97f69650e695a90c48f82fcd864618e569e9` |
| `tools/h1_compare_companions.py` | blob `accf8d253aac35bc8014cc08874a23d758249b13` |
| `01_heat.pdf` | blob `18755813329b21f5e2ac432b2a5aebfe6dc21a60`, unchanged from main |

The only newly active CI is `.github/workflows/h2-h1-offline-ci.yml`. Seven historical `*once.yml` workflows and two S1-specific one-shot launch scripts are deliberately **excluded from the integration tree** and remain preserved on original experiment branches. The reusable host-guarded batch runner and saved pinned example plans are present but are *not called by standard CI*. Expect 110 added paths, no modifications/deletions of pre-existing main paths. AGENTS.md and the root README reflect current candidate status; historical docs and source-fidelity debates are not rewritten.

**Inspect at pinned SHA:** `AGENTS.md`, `README.md`, `docs/H2_00_INTEGRATION_SCOPE.md`, `docs/H1_IMPLEMENTATION_CONTRACT.md`, `docs/H1_OFFLINE_AMENDMENT.md`, `qualification/h1_c1/FREEZE.md`, `experiments/h1_spike/SimHeat.mo`, `h1/{model,study,policy,temporal,reference,decoder,matv4,verification}.py`, `tools/h1_native_batch.py`, relevant test modules, CI YAML and the exact PR diff.

## Expected source-backed physical and evidence behavior

The supported law is uniform lumped-body storage, storage-free one-dimensional conduction and maintained-temperature boundaries, with SI quantities. Flow `rod.Q_flow = G*(T_a-T_b)` is oriented `a` to `b`; component thermal-port signs and `body.dU = m*c*(T - T_initial)` must be consistent. No topology-specific solver, inferred material properties, fabricated geometry or reference-backed missing native outputs. Required internal exports must be present before reports; MATv4 signed/shared aliases require truthful provenance, not claims of independent measurements.

Model admission accepts only a restricted fully consumed grammar and bounded topology, validates references/provenance/full request operands and reports refusals without executing arbitrary code. JSON model/study identities, SHA pins, temporal grid/error allowances, energy-integral checks, request statuses and historical evidence labels must stay coherent. `nativeQualified=false`/`diagnostic_only` **must not be promoted** merely because historical execution passed. No unrestricted compiler/sandbox or classroom-effectiveness claim is permitted.

## Adversarial reviewer questions (do not aim for a particular verdict)

1. Does the source PR truly preserve tested H1 physics/verification bytes and original PDF while excluding every automated one-shot native trigger? Does the supplied CI run actually correspond to the pinned head, without relying on an alias/main?
2. Can a syntactically plausible but invalid request, undeclared object/port, inconsistent topology, wrong unit/parameter, duplicate JSON key, stale model hash, missing MAT parameter/alias, invalid time grid or signed-energy defect slip from admission to a falsely successful result? Pick a few high-value independent negative tests; do **not** silently repair inputs.
3. Does the checker distinguish solver/native values from model parameters, reference predictions and diagnostic-only requests? Are direct aliases/shared channels and temporal/integral error budgets reported with sufficient provenance and conservative bounds?
4. Can the bundled runner or CI execute arbitrary untrusted Modelica, network/install side effects or native builds without the explicit host/plan/source/budget guards? State the trust boundary; SHA integrity is not execution authentication.
5. Do prior S1 failures, successful D1/D2/resolution/bridge runs, prepared reference-error claims and the pending independent R1/R2/R3 gates support **only** the stated limited integration candidate, without overstating composability or native qualification?
6. Is a release without renewed native execution justifiable given *identical* implementation source hashes, existing pinned native evidence, full final-head offline CI and explicitly preserved residual risk? If not, identify the smallest missing evidence, not another broad architecture redesign.

When possible, execute the source's offline regression suite, review selected negative inputs and independently verify artifact hashes, one physical conservation identity and one output-provenance claim. **Separate what you ran from what you read** and mark inaccessible external artifacts as not independently inspected.

## Risk/status and release gate

This is **one full R2 separate-chat review** of a completed milestone by default. Chat A author self-check/CI are not independent Chat B findings. A reviewer report of `insufficient-evidence` or a blocker keeps the source PR draft. Re-review only affected paths after corrections unless physical/evidence semantics change significantly. **No source PR merge until owner separately approves**, blockers are resolved, and post-merge CI can be verified.

Neither a Chat B report nor this central packet is an automated required GitHub status check.