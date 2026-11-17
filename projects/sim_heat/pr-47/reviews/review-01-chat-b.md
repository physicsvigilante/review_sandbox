# SIM_HEAT draft PR #47 — independent Chat B R2 review (review-01)

**VERDICT: SCOPED PASS — ORIGINAL NINE AUTHORED PUBLIC OBSERVATIONS TO EXPECTED SOURCE EXPORT DEPENDENCY NAMES/SIGNS/UNITS ONLY.** This is not an approval of physical or native numerical results, Modelica output availability on a real compiler, owner-authenticated provenance, native execution, reference regeneration, release readiness, or merging the historical source PR.

## Identity, review scope, and source isolation

- **Source repository:** [physicsvigilante/sim_heat](https://github.com/physicsvigilante/sim_heat); historical draft [PR #47](https://github.com/physicsvigilante/sim_heat/pull/47).
- **Exactly reviewed source HEAD:** abd969ce32c8b55899561ad7d80c5792f304927e, with CI-archived tree **176b78b7c0a88add9df8794761fc3b94e6bed6e2**.
- **Immediate base (PR46):** 6c09b44802e869f4a07a2dbda26e2ca37bff83b9, previously independently reviewed; [base-to-head comparison](https://github.com/physicsvigilante/sim_heat/compare/6c09b44802e869f4a07a2dbda26e2ca37bff83b9...abd969ce32c8b55899561ad7d80c5792f304927e).
- **Source difference:** five commits ahead, zero behind; exactly four **ADDED** paths, with no modified or deleted inherited files: [new source dependency mapper](https://github.com/physicsvigilante/sim_heat/blob/abd969ce32c8b55899561ad7d80c5792f304927e/qualification/h1_c1/f02/offline_public_request_dependencies.py), [20-method test module](https://github.com/physicsvigilante/sim_heat/blob/abd969ce32c8b55899561ad7d80c5792f304927e/qualification/h1_c1/f02/test_offline_public_request_dependencies.py), [scope document](https://github.com/physicsvigilante/sim_heat/blob/abd969ce32c8b55899561ad7d80c5792f304927e/qualification/h1_c1/f02/PUBLIC_REQUEST_DEPENDENCY_SCOPE.md), and [offline CI workflow](https://github.com/physicsvigilante/sim_heat/blob/abd969ce32c8b55899561ad7d80c5792f304927e/.github/workflows/h1-c1-f02-public-request-dependencies.yml).
- **Review request:** [central PR47 REQUEST](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-47/REQUEST.md), with [central protocol](https://github.com/physicsvigilante/review_sandbox/blob/main/PROTOCOL.md) and R2 risk policy.
- **Reviewer:** Chat B, GPT-6, separate ChatGPT conversation; 2026-11-17 (Asia/Kolkata). Independence means separate conversation and independently checked evidence, not a different human expert or independently proven model family.
- **Changes made:** no source, source PR, review request, frozen F0, numerical reference, owner decision or CI modifications. The sole authorized write is this review file in the central review hub.

## Findings

### F-01 — PASS (source identity and preserved inherited scientific constraints)

The exact Git base-to-head comparison independently returned only the four paths above as additions. CI's saved head-sha.txt equals the pinned HEAD and head-tree.txt records the specified tree. The diff snapshot contains exactly those four added paths. No first-author Modelica, evaluator study, original H1 physics/parser/checker/native runner, original PR31 checking reference, PR41 HOLD or owner authorization was modified in this PR.

The original 14 frozen F0 file SHA checks in the downloaded CI archive each say OK, including h1/model.py, h1/verification.py and tools/h1_native_batch.py. Inherited PR46 expected-coverage checks report 23 source/input pins verified, and the archived original analytical reference identities remain raw SHA-256 **0db511dd8dba023d16518667de256029cf3e073463ea21e2478aeac8afd1f368** and canonical seal **d2b8e2ca8e1f929cac7b028dcc3f7d0b453921d193f877eb091e23ac70aa4ce9**. These checks identify saved checking data; they are **not** owner authentication or trust in observed native outputs.

### F-02 — PASS (independently reconstructed original nine public request projections)

I separately reconstructed the exact original 872-byte [Modelica source](https://github.com/physicsvigilante/sim_heat/blob/abd969ce32c8b55899561ad7d80c5792f304927e/h1/cases/H1_C1_MODAL/model.mo) and computed its SHA-256, obtaining **9a165e5ce2cc85da84ecc8bc4e63e2990f2066f3547dc6ba8508fa1afbe5f435**, matching the frozen model descriptor and dependency report. It declares two Body components, two FixedTemperature boundaries, three RodArea conductors and one RodCircular conductor. Using the unchanged [internal_exports rules](https://github.com/physicsvigilante/sim_heat/blob/abd969ce32c8b55899561ad7d80c5792f304927e/h1/model.py) yields **37 distinct intended field names**, exactly the set in the archived PR46 expected-only coverage report. This is a source-derived *expected* inventory, not a native export measurement.

Independently transcribing the nine author-ordered request IDs, operations and operands from the original [modal study](https://github.com/physicsvigilante/sim_heat/blob/abd969ce32c8b55899561ad7d80c5792f304927e/h1/cases/H1_C1_MODAL/study.json) and applying the frozen [verification.py check_candidate port_key and observations](https://github.com/physicsvigilante/sim_heat/blob/abd969ce32c8b55899561ad7d80c5792f304927e/h1/verification.py) yielded these exact receipt rows:

| Original public ID | Authored operation/target | Ordered expected source terms | Unit |
|---|---|---|---|
| leftTemperature | temperature(leftBuffer.port) | +1 leftBuffer.T | K |
| rightTemperature | temperature(rightBuffer.port) | +1 rightBuffer.T | K |
| hotLeadFlow | heatFlow(hotLead) | +1 hotLead.Q_flow | W |
| flatBridgeFlow | heatFlow(flatBridge) | +1 flatBridge.Q_flow | W |
| roundBridgeFlow | heatFlow(roundBridge) | +1 roundBridge.Q_flow | W |
| coldLeadFlow | heatFlow(coldLead) | +1 coldLead.Q_flow | W |
| bufferTemperatureDifference | temperatureDifference(a=leftBuffer.port, b=rightBuffer.port) | **+1 leftBuffer.T; -1 rightBuffer.T (ordered)** | K |
| leftEnergyChange | energyChange(leftBuffer) | +1 leftBuffer.dU | J |
| rightEnergyChange | energyChange(rightBuffer) | +1 rightBuffer.dU | J |

All **9/9** rows matched the real artifact's ID, operation, authored operands, dependency kind, ordered terms, units and informational native-null status. Totals: **eight direct one-term requests, one derived two-term difference, ten signed source terms**. Every term is in the original 37 expected-field names and has the correct original analytical-checking unit.

Crucial directionality: frozen verifier's direct rod heatFlow selects **rod.Q_flow**, not a potentially sign-reversed port_b.Q_flow. The unchanged rod checks define port_a.Q_flow = Q_flow, port_b.Q_flow = -Q_flow and Q_flow = G(T_a - T_b) for the candidate validation convention; this review endorses the intended **name/sign convention only**, not the unobserved native result. Frozen temperatureDifference selects **first port temperature minus second**, not the reverse. Body and FixedTemperature port temperature maps to .T; rod port_a/port_b to .T_a/.T_b. Body energyChange maps to .dU. The new code's strict port/kind checks agree with these original operands.

### F-03 — PASS within scope; full source-bound exactness required (shape-only is not proof)

The new source builds its report from inherited expected.inventory, which checks the original saved analytical reference and offline-release HOLD, plus load_study/model component and request validations. It does not numerically combine or subtract field values; its output is a field/sign/metadata description only. The one successful CLI operation is describe-dependencies-only. Its schema explicitly identifies all nine readings as **not_computed**, nativeValue=null, nativePublicValues=null, zero native observations/series, and releaseBlocked=true.

I constructed **31 distinct modifications of the exact downloaded JSON receipt** and checked their canonical JSON bytes independently against the unmodified original. **31/31** differ and are rejected by the *full canonical source-identity comparison*. Cases included renamed/duplicate/dropped/reordered request rows; incorrect authored targets, operations, units or fields; flipped, swapped, float and boolean signs; wrong first-minus-second order; invented values and observed status; false/0 and integer/boolean coercion; changed original source SHA, raw checking SHA and PR32 alternative seal; erased/filled release gates; unrecognized provenance/numerical keys; fake original-F0 success and release approval. This is a **separate, source-equivalent canonical-comparison probe**, NOT a local execution of the checked-in mapper or its actual verifier. The actual mapper's twenty tests ran in pinned hosted CI (see F-04).

**Important usage rule:** validate_shape alone is *not* a source-identity/provenance assertion. For example, structurally plausible changes of request names, operands, units or filled gate *labels* can survive coarse shape checks. Any future copied external dependency report must pass **assert_exact_source_bound**, which re-derives the complete pinned source report and compares canonical serialized bytes. Even that does **not** authenticate a native run, compiler environment, owner consent, or provenance outside the source tree. No exposed PR47 command promotes shape-only data into observed native evidence.

### F-04 — PASS (independently examined exact-head hosted CI evidence, with accurate provenance limits)

[GitHub Actions run #44079994935](https://github.com/physicsvigilante/sim_heat/actions/runs/44079994935) contains one completed **SUCCESS** job, deny-native-proof-from-local-files, at the requested HEAD. I downloaded [artifact #14326172947](https://github.com/physicsvigilante/sim_heat/actions/runs/44079994935/artifacts/14326172947) and personally verified:
- Exact ZIP length **33,439 bytes** and independently recomputed full SHA-256 **d578ac49bff76e8eed354730548bf4ea5de93569deca6f74cdf4c803854a012d**.
- **45/45 unique ZIP entries**, all CRC-valid; head SHA and tree, four-path add-only diff, receipt JSON, all fifteen test-group logs, frozen pin checks, ten forbidden-native CLI stderr receipts, and explicit blocked-untrusted-native report.
- All **370/370 hosted offline unittest methods PASS**, counted from their preserved log summaries: 20 new dependency tests, 17 inherited expected-only coverage, 24 untrusted intake, 16 stale snapshot, 18 one-shot state model, 15 HOLD, 16 external-CAS fake contract, 12 local SQLite, 15 build-text preview, 24 staged inputs, 16 disabled F02, 11 Option A consumer, 8 reference-binding, 9 original PR31 fixture and 149 original frozen H1 tests. No local rerun of the actual repository tests is claimed.
- Original report identities, all 9 exact names/units/terms, expected 37 exports/four analytical flow-integral histories, all 11 missing real release gates, and **zero observed native output and no computed public value**. The untrusted-native intake status remains BLOCKED_UNAUTHENTICATED_NATIVE_ARTIFACT_INTAKE and all nine native files are absent.
- The workflow installs only offline Python checking dependencies; its steps show **no OpenModelica installation, query, compilation, launch, MAT decode, reference.prepare, native comparison, owner-native permission or authenticated release**. Ten prohibited native/owner CLI verbs are refused.

### F-05 — Historical real scientific failures preserved; no native-release permission

The original F0 hotLead.G check remains an explicit **FAIL: 80x margin against mandatory >=100x**. Original PR32 cross-host bitwise regeneration of the PR31 V2 seal remains **FAIL**, and the alternate PR32 seal **c30e8783d39c7b0198c1adf0273ac84568f698f08287f02bf79eeed224830b07** was not adopted. The original preserved saved PR31 reference is only approved for offline checking. PR47 neither repairs these failures nor supplies a real native observation; it must stay a historical draft, unmerged to production.

No demonstrated blocker was found **inside this narrowly bounded expected-field dependency naming task**. The above historical failures are blockers for any attempt to treat it as a native scientific qualification or release, not blockers to an honest name-only informational report.

## Tests performed vs evidence inspected

**Performed by this reviewer:** pinned GitHub source/CI and base-to-head diff inspection; original 872-byte Modelica SHA-256 reconstruction; independent eight-component and 37-name expected-export enumeration; all nine source-study requests mapped again from frozen verifier rules, including heat-flow orientation and left-minus-right; independent ZIP hash, CRC and per-file inspection; 370-method log counting; and 31 independent canonical JSON mutation probes. Read the new implementation, test cases, new workflow, original h1/model.py and h1/verification.py and the review protocol.

**Observed through hosted CI, not rerun locally:** actual PR47 source module execution, 20 new and 350 inherited tests, original frozen pin checks and 23 source/input pins, and blocked CLI refusals.

**Not performed, and not implied by this verdict:** OpenModelica version query/install/build/one launch; any actual native Modelica result or MAT/CSV reading; native exported field attestation; reference regeneration; source or owner cryptographic authentication; shared durable external atomic reservation; independent real-host check; numerical physics accuracy qualification; browser visualization or teacher usability test. The 31 supplementary probes ran against downloaded receipt bytes and canonical comparison independently, not by importing the original source module.

## Separate scoped judgments

| Dimension | Finding | Reason |
|---|---|---|
| Source interpretation fidelity | **SCOPED PASS** | Nine original authored requests map to precisely the same expected source keys, units, signs and order as frozen verifier. |
| Physical/numerical correctness | **UNKNOWN for native; historical F0 FAIL intact** | Names only, no physical values, no OMC; F0 80x vs 100x requirement not waived. |
| Native simulation / observable coverage | **NOT COMPUTED** | 37 source-expected exports, four checking-reference integrals, nine actual public values absent. |
| Evidence integrity and provenance | **PASS for reproducible offline identity; NOT authenticated release** | Exact-head archived ZIP independently hash/CRC verified and source-pinned; 11 real owner/native prerequisites absent. |
| Teacher-facing usefulness | **INFORMATIONAL ONLY** | Helpful for future model authoring/observable wiring, not yet a live simulation or visualization. |
| Textbook-answer completeness | **NOT APPLICABLE** | Neither a textbook-answer engine nor a computed scientific response. |

## Release recommendation and next boundary

**SCOPED PASS for R2 original expected dependency names/signs/units and truthful zero-native status only.** No source edit is required to justify this informational result. Preserve the frozen F0 and PR32 failures, the original PR31 checking-only identity, all eleven missing prerequisites, and the historical unmerged draft. Never use a standalone validate_shape as a trust boundary.

The next real-native attempt would require, separately, a reviewed *executable nonregenerating* adapter and plan, protected source/reference and backups, observed host/OMC/MSL identities, durable owner-controlled external atomic single-attempt reservation, independent pre-native R2, and **new explicit owner approval for precisely named version-query, build and one-launch/no-retry budgets**. This review supplies no such authorization and makes no source-merge decision.
