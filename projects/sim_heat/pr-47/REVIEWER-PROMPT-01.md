# Chat B — independent SIM_HEAT PR #47 nine public requests mapped to expected fields R2

Continue as independent Chat B reviewer for historical [draft SIM_HEAT PR #47](https://github.com/physicsvigilante/sim_heat/pull/47).

**Review EXACT HEAD `abd969ce32c8b55899561ad7d80c5792f304927e`**, Git tree `176b78b7c0a88add9df8794761fc3b94e6bed6e2`, from independently reviewed PR46 base `6c09b44802e869f4a07a2dbda26e2ca37bff83b9`.

Read the central full independent review packet:
https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-47/REQUEST.md

Exactly FOUR new offline source/test/scope/CI files map the original 9 authored H1-C1-MODAL public requests to **EXPECTED** model export field dependencies, with **NO NUMERICAL OR NATIVE VALUES**. Check frozen `h1/model.py` and `h1/verification.py.check_candidate` port/observation rules, original pinned author Modelica, evaluator study and original saved owner-adopted PR31 V2 analytical checking data.

The intended 8 direct mappings are `leftTemperature→leftBuffer.T`, `rightTemperature→rightBuffer.T`, four rod heat flows `hotLeadFlow→hotLead.Q_flow`, `flatBridgeFlow→flatBridge.Q_flow`, `roundBridgeFlow→roundBridge.Q_flow`, `coldLeadFlow→coldLead.Q_flow`, and two Body energy changes `leftEnergyChange→leftBuffer.dU`, `rightEnergyChange→rightBuffer.dU`. The **one derived** difference must be exactly `+leftBuffer.T -rightBuffer.T`, preserving original author `a/b` order. All 10 signed terms must match the 37 original expected export names/units. No actual OMC export availability or values can be inferred.

Adversarially test source-port kind/identity, wrong/missing/duplicate/reordered exports, swapped difference sign, wrong units/operation/operand, forged public native values, original PR32 alternate reference seal, native/owner permission flags, bool/numeric coercions and missing 11 native release gates. Demand **full source-derived `assert_exact_source_bound`**, not shape-only acceptance. All nine `nativeStatus=not_computed`, `nativeValue=null`, native observation count ZERO and `releaseBlocked=true`.

Independently inspect exact-head [CI #44079994935](https://github.com/physicsvigilante/sim_heat/actions/runs/44079994935), [artifact #14326172947](https://github.com/physicsvigilante/sim_heat/actions/runs/44079994935/artifacts/14326172947), **33,439 bytes**, whole ZIP SHA-256 `d578ac49bff76e8eed354730548bf4ea5de93569deca6f74cdf4c803854a012d`, **45/45 CRC valid**, and **370/370 HOSTED OFFLINE tests**. Verify original F0 hotLead.G 80×/required ≥100× accuracy FAIL and PR32 cross-host original V2 bitwise regeneration FAIL unchanged, all original science/reference pins retained and 0 OMC/Modelica native operations.

Commit your **NEW independent** `projects/sim_heat/pr-47/reviews/review-01-chat-b.md` directly to `physicsvigilante/review_sandbox` with **SCOPED PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE**, exact SHA/tree, independent tests vs inspected hosted CI, and the remaining native authority gates. Chat A must not author this report.

**Do not** edit frozen scientific source/reference, merge historical F0 PRs, install/query/build/launch OpenModelica, generate references, treat expected dependencies as computed public answers, grant real CAS/source-owner authority or waive old failed evidence. A real native attempt still needs a separately authenticated owner release/source/host/adapter/atomic CAS, independent new pre-native R2 and new **explicit owner authorization** for the named version-query/build/single-model-launch budget.