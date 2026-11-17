# SIM_HEAT draft PR #46 — independent Chat B R2 review (review-01)

**VERDICT: SCOPED PASS — EXACT EXPECTED 37 MODEL EXPORT NAMES / FOUR FLOW-INTEGRAL HISTORIES / NINE AUTHORED PUBLIC REQUESTS, WITH ZERO OBSERVED OR QUALIFIED NATIVE DATA.** No demonstrated blocker within this expected-versus-uncomputed scientific-interface scope. This is **NOT** a native simulation pass, numerical-accuracy finding, authenticated owner release, native execution permission, source merge approval, or qualification of the intended Modelica exports on a real compiler.

## Identity, boundary, and provenance

- Source repository: [physicsvigilante/sim_heat](https://github.com/physicsvigilante/sim_heat); historical, still-unmerged draft [PR #46](https://github.com/physicsvigilante/sim_heat/pull/46).
- Immediate already-reviewed base (PR45): `278f8224fa23ec20bc6c7342ab433b9be17e4434`, tree `fc0dbe955a14a73e7e54dd8060cb5d469a6f91e6`; [earlier Chat B report](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-45/reviews/review-01-chat-b.md).
- **Exactly reviewed PR46 HEAD:** `6c09b44802e869f4a07a2dbda26e2ca37bff83b9`; independently fetched Git commit tree **`e25f39673a88d454921331f16d93b43ca9757e97`**.
- [Exact base-to-head Git compare](https://github.com/physicsvigilante/sim_heat/compare/278f8224fa23ec20bc6c7342ab433b9be17e4434...6c09b44802e869f4a07a2dbda26e2ca37bff83b9): four commits ahead, 0 behind; exactly four additions, **zero inherited modifications/deletions**:
  1. `qualification/h1_c1/f02/offline_expected_export_coverage.py` (267 new lines)
  2. `qualification/h1_c1/f02/test_offline_expected_export_coverage.py` (244 new lines)
  3. `qualification/h1_c1/f02/EXPECTED_EXPORT_COVERAGE_SCOPE.md` (36 new lines)
  4. `.github/workflows/h1-c1-f02-expected-export-coverage.yml` (175 new lines)
- Reviewer: Chat B, GPT-6, separate ChatGPT conversation, 2026-11-17 (Asia/Kolkata); **R2 scientific interface/evidence interpretation** only. Different chat context is not human-independent scientific adjudication.
- Source files changed during this review: **NONE**. No OpenModelica query/install/build/launch, native decoder, regeneration, historical merge, source branch change, or native release operation. Sole intended write: this report in the central review hub.
- Read central [PR46 REQUEST](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-46/REQUEST.md), [protocol](https://github.com/physicsvigilante/review_sandbox/blob/main/PROTOCOL.md), risk policy/template, exact new code/tests/workflow, frozen `h1/model.py` and `h1/study.py`, original modal Modelica and evaluator study, PR31 original saved artifact and manifest, Option A read-only consumer, PR41 readiness HOLD, and PR32 failure evidence. Root `AGENTS.md` was not present at the pinned PR46 source HEAD.

## Findings

### F-01 — PASS; original source isolation, reference identity, and HOLD governance

**Evidence:** [exact new implementation](https://github.com/physicsvigilante/sim_heat/blob/6c09b44802e869f4a07a2dbda26e2ca37bff83b9/qualification/h1_c1/f02/offline_expected_export_coverage.py), [workflow](https://github.com/physicsvigilante/sim_heat/blob/6c09b44802e869f4a07a2dbda26e2ca37bff83b9/.github/workflows/h1-c1-f02-expected-export-coverage.yml), Git compare, and downloaded CI artifact.

The diff has no edits to the first-author Modelica/study, frozen H1 laws/parser/checker/native runner, original unlaunched plan, owner decision, PR31 saved scientific reference/manifest, or previous historical CI. Actual Git tree and CI-archived `head-sha.txt`/`head-tree.txt` agree. CI independently checked 14 frozen F0 file SHA pins and original 23 source/input pins; source hash inventory records model raw SHA `9a165e5ce2cc85da84ecc8bc4e63e2990f2066f3547dc6ba8508fa1afbe5f435`, modal study `b43e85b6b10afd6550a43322cf98097fe9781a606ee01bc031eadbfd4783b31b`, and first-author study `b235d4242728c44dd994e09db3ffd92d197398dde3fe6c8f006a801981997fdc`.

The program requires prior PR41 readiness audit `BLOCKED_11_NATIVE_RELEASE_GATES_MISSING_OFFLINE_ONLY` and Option A `APPROVED_REFERENCE_DATA_OFFLINE_CHECKING_ONLY`. The 11 actual release/owner/host/adapter/atomic-store/pre-native prerequisites are still missing. This is inspection of an unprotected, unsigned checking-reference decision; not independent owner authentication or a native permission token.

### F-02 — PASS; independently derived exactly 37 original intended export names

**Evidence:** [frozen Modelica parser and export rules](https://github.com/physicsvigilante/sim_heat/blob/6c09b44802e869f4a07a2dbda26e2ca37bff83b9/h1/model.py), [original modal model](https://github.com/physicsvigilante/sim_heat/blob/6c09b44802e869f4a07a2dbda26e2ca37bff83b9/h1/cases/H1_C1_MODAL/model.mo), PR31 original raw bundle, PR46 `expected-not-observed.json`.

I separately transcribed the 872-byte original Modelica text and verified its raw SHA-256 **exactly** matches `9a165e5ce2cc85da84ecc8bc4e63e2990f2066f3547dc6ba8508fa1afbe5f435`. Independently enumerating the component declarations using the frozen `internal_exports` field rules yields:

| Original component(s) | Export suffixes for EACH component | Count |
|---|---|---:|
| `leftBuffer`, `rightBuffer` (Body) | `T` (K), `Q_in` (W), `dU` (J), `C` (J/K) | 2 x 4 = 8 |
| `hotBath`, `coldBath` (FixedTemperature) | `T` (K), `Q_to_network` (W) | 2 x 2 = 4 |
| `hotLead`, `flatBridge`, `coldLead` (RodArea) | `T_a`, `T_b` (K); `Q_flow`, `port_a.Q_flow`, `port_b.Q_flow` (W); `G` (W/K) | 3 x 6 = 18 |
| `roundBridge` (RodCircular) | RodArea's six export suffixes plus `A` (m2) | 1 x 7 = 7 |
| **Total** | **All distinct, alphabetically ordered** | **37** |

The **exact 37 fully qualified names and units** of this independently enumerated set match PR46 receipt row-for-row, and the key sets of PR31 original saved `columns`, `units`, `owners` and `allowances`. Each of the 37 PR31 **analytical checking** series has **4001 saved samples**; each receipt field has `nativeStatus="not_computed"` and `observedNativeSamples=null`. The original 4,409,800-byte PR31 raw JSON was obtained independently from the original archived PR31 CI artifact, not merely accepted from the PR46 author's claims.

These 37 are the *parser's expected names*; whether the real OMC-executed Modelica model exposes all 37 is **UNKNOWN**.

### F-03 — PASS; exactly four expected energy histories and nine original public requests

**Source:** [original evaluator modal study](https://github.com/physicsvigilante/sim_heat/blob/6c09b44802e869f4a07a2dbda26e2ca37bff83b9/h1/cases/H1_C1_MODAL/study.json), frozen [request validator](https://github.com/physicsvigilante/sim_heat/blob/6c09b44802e869f4a07a2dbda26e2ca37bff83b9/h1/model.py), original PR31 bundle, exact receipt.

There are **two** Body components and **two** FixedTemperature components. Their independently derived expected flow-integral keys, sorted and identically present in original PR31 `flowIntegrals` and `quadratureAllowances` and PR46 receipt, are:

- `coldBath.Q_to_network`
- `hotBath.Q_to_network`
- `leftBuffer.Q_in`
- `rightBuffer.Q_in`

All have **4001 saved analytical** reference integral samples. No native integral samples were observed (`observedNativeSamples=null`, `nativeStatus="not_computed"`).

The **nine** original author-ordered public request identities, operations, exact operands and units are:

| Original ID | Operation | Original operand(s) | Unit |
|---|---|---|---|
| `leftTemperature` | `temperature` | `target=leftBuffer.port` | K |
| `rightTemperature` | `temperature` | `target=rightBuffer.port` | K |
| `hotLeadFlow` | `heatFlow` | `target=hotLead` | W |
| `flatBridgeFlow` | `heatFlow` | `target=flatBridge` | W |
| `roundBridgeFlow` | `heatFlow` | `target=roundBridge` | W |
| `coldLeadFlow` | `heatFlow` | `target=coldLead` | W |
| `bufferTemperatureDifference` | `temperatureDifference` | `a=leftBuffer.port`, `b=rightBuffer.port` | K |
| `leftEnergyChange` | `energyChange` | `target=leftBuffer` | J |
| `rightEnergyChange` | `energyChange` | `target=rightBuffer` | J |

Every one is `nativeStatus="not_computed"` with `nativeValue=null`. No public answer was calculated. The receipt is a **12,998-byte names/counts/metadata document**, not a copy of the saved numerical arrays, observed MAT data, or a native results record.

### F-04 — PASS with explicit **usage boundary**; forged native/identity/permission claims refused by the COMPLETE exact-source check

**Source:** [new `validate_shape` and `assert_exact_expected`](https://github.com/physicsvigilante/sim_heat/blob/6c09b44802e869f4a07a2dbda26e2ca37bff83b9/qualification/h1_c1/f02/offline_expected_export_coverage.py), [17 hosted negative tests](https://github.com/physicsvigilante/sim_heat/blob/6c09b44802e869f4a07a2dbda26e2ca37bff83b9/qualification/h1_c1/f02/test_offline_expected_export_coverage.py).

Independently constructed **36 in-memory tampering candidates** from the actual downloaded PR46 JSON and checked a local source-equivalent reproduction of the pinned shape conditions plus canonical serialized-equality check. **36/36 refused.** Cases include forged native sample counts/statuses/`nativeValue` (0, false and infinity), reordered/renamed/duplicated exports and requests, changed exported unit, changed integral identity, changed request ID/operation/operand/unit, changed PR31 raw SHA and substitution of the historical PR32 alternative seal, falsified owner/native-qualified flags (including Python bool/int/float coercions), omitted/filled release gates, and injected unknown numerical-output fields. Untampered receipt passed the same checks.

**Important limitation:** the independently run 36-probe harness uses a transparently transcribed, source-equivalent implementation of the pinned validation conditions with the **downloaded original JSON as the required inventory**. It is not a new execution of the full GitHub Python module/owner anchor on this local host. The actual pinned module, its unmocked original source/reference initialization, and all 17 original-unit-test methods were executed in GitHub's exact-head CI; subsequent hosted adversarial test cases mock only the recomputation to isolate verifier comparison behavior.

**Nonblocking usage caveat:** `validate_shape` alone is intentionally **not** an exact identity validator: in the independent probe, 11 mutations (including a changed but unique request ID, wrong unit, reordered requests, or a filled gate string while preserving gate count) passed shape alone. Every such mutation was rejected by the **combined** `assert_exact_expected` canonical byte comparison. Therefore a later external-data consumer must invoke the complete **source-bound** exact check, never promote bare `validate_shape` to a trusted native-evidence validator. No exposed PR46 command does this promotion: its only successful verb is `describe-expected-only`, which creates its own pinned source-derived inventory.

All 13 report true-native/owner/historical-success fields are literal `false`; native observation/export/integral counts are literal integer 0; nine native public requests remain uncomputed; all 11 required release gates remain missing. No owner-signature or native trust is inferred.

### F-05 — PASS; pinned CI and both historical scientific failures preserved as negative evidence

**CI:** [exact-head run #44071491305](https://github.com/physicsvigilante/sim_heat/actions/runs/44071491305), completed **SUCCESS** at PR46 HEAD and single successful job `deny-native-proof-from-local-files` (job ID `133998565779`). The job uses ubuntu-24.04, pinned checkout/setup-python action SHAs, Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0 and mpmath 1.3.0, read-only `contents` permission, no persisted checkout credentials and **no native/OMC build, query, launch, or MAT decoding**.

**Downloaded exact [artifact #14322174126](https://github.com/physicsvigilante/sim_heat/actions/runs/44071491305/artifacts/14322174126):** 30,464 bytes, independently recomputed full ZIP SHA-256 **`2aad7d84dca757e59839904a6f66bfa32ca33e9ea1e36abc8cc90b3b5f2f293c`**, **43/43 ZIP members CRC-valid**. Its `head-sha.txt` = exact PR46 SHA; `head-tree.txt` = exact Git tree; `source-diff.txt` contains the four expected `A` rows only. `frozen-f0-pins.txt` records **14/14 OK**; original archived PR31 XZ and full manifest SHAs pass CI's pinned checksum checks.

**Hosted tests actually executed (from all 14 complete saved unittest logs, with no FAILED blocks):**

| Source test group | Tests passing |
|---|---:|
| New exact expected export/request coverage | 17 |
| Inherited local untrusted native intake | 24 |
| Stale fake snapshot CAS | 16 |
| Toy one-shot state model | 18 |
| Release readiness HOLD | 15 |
| Fake external-CAS contract | 16 |
| Local SQLite simulator | 12 |
| Modelica build script **text-only** preview | 15 |
| Immutable input staging | 24 |
| Disabled F02 control preflight | 16 |
| Option A checking-only consumer | 11 |
| Source-reference binding | 8 |
| Original PR31 archived reference fixture | 9 |
| Original frozen H1 methods | 149 |
| **Total** | **350/350** |

The artifact also contains a BLOCKED untrusted intake receipt: all nine expected untrusted filenames missing, no local native evidence, 11 missing gates, and all native/owner flags false. Ten forbidden arguments (`native`, `execute`, `approve`, `run`, `build`, `launch`, `omc`, `reserve-native`, `verify-native`, `qualify`) produced argparse invalid-choice refusals in preserved stderr logs.

**Independent original PR31 evidence:** separately downloaded [original PR31 artifact #14249313720](https://github.com/physicsvigilante/sim_heat/actions/runs/43915934653/artifacts/14249313720), 2,348,945 bytes; full ZIP SHA-256 **`d9259837e0e03c70989b50b2c9dcbf13aca260da4d1cb0ae000b2a23ef65732e`**, 13/13 CRC-valid entries; its exact raw saved reference bundle is 4,409,800 bytes with SHA-256 **`0db511dd8dba023d16518667de256029cf3e073463ea21e2478aeac8afd1f368`**. Independently recanonicalizing its contents under frozen `h1.reference.canonical` (excluding `seal`) reproduces **`d2b8e2ca8e1f929cac7b028dcc3f7d0b453921d193f877eb091e23ac70aa4ce9`**. The original saved `origin` remains `analytical_reference_only` and `nativeQualified=false`.

- **Original frozen F0 failure remains FAIL/HOLD.** The archived `F01_ORIGINAL_FAILURE_STILL_REPRODUCED.json` independently inspected in the original PR31 ZIP records `hotLead.G` at **80x** native-error margin against the untouched mandatory **100x** budget, `strict100xPass=false`, original seal `d76c98f37a0629b56d977c960d1e75694e1121832a9d5281f68bb972d31a365b`. PR46's `originalF0Strict100xPassed=false` is correct.
- **Original PR32 cross-host bitwise reproduction remains FAILED.** [Original two-host CI #43921113470](https://github.com/physicsvigilante/sim_heat/actions/runs/43921113470) was independently fetched and is **completed/failure**; [PR32](https://github.com/physicsvigilante/sim_heat/pull/32) records alternative `c30e8783d39c7b0198c1adf0273ac84568f698f08287f02bf79eeed224830b07` not adopted. PR46 retains original saved PR31 seal and `pr32BitwiseRegenerationPassed=false`; no alternate reference was substituted or regenerated.

## Tests and evidence: performed versus observed

**Performed independently by Chat B:** GitHub exact-head/tree/compare and pinned source/owner/hold code inspections; direct download, SHA-256, CRC, and JSON checks of PR46 and original PR31 archived artifacts; independent byte-matching mirror of original Modelica source; component-type/name/units enumeration against full original saved 37-column PR31 reference; original request mapping, flow-integral key, sample/flag checks; 36 independently authored negative candidates through locally reproduced validation predicates; direct GitHub check of original PR32 failed CI. These checks are Python/JSON/ZIP/regex inspection only.

**Inspected, not rerun locally:** all 350 hosted Python unittest results, 14 original frozen F0 pin checks, 23 earlier input pin checks, exact-head workflow log steps, original saved reference compressed XZ/manifest SHA assertions, and ten CLI refusals. GitHub workflow ran the actual module's 17 new tests; my 36 probes are supplementary and not a replacement for those hosted tests.

**Not performed:** any native compiler version query, OMC invocation, numerical reference regeneration, real MAT/CSV decode, observed host/toolchain/Modelica-runtime qualification, native public value calculation, energy conservation measurement, source signature authentication, atomic external CAS, protected release, or native one-shot launch.

## Separate judgments

| Dimension | Judgment | Basis |
|---|---|---|
| Source interpretation fidelity | **PASS, narrowly** | Original source/model SHA and frozen internal export rule reproduce 37; original authored evaluator requests reproduce nine; original PR31 bundle independently confirms all names/units and four flows. |
| Physical/numerical correctness | **UNKNOWN for native; old F0 FAIL retained** | The original PR31 V2 checking reference is archived and SHA-sealed, but no new physics or native values were computed. F0 80x / 100x scientific failure remains explicitly false. |
| Native simulation / observable coverage | **NOT COMPUTED** | 37 expected only; 4 analytical reference integral histories; 9 admitted native readings null; no actual Modelica output, no MAT/CSV, no native series. |
| Evidence integrity / provenance | **PASS for exact offline ZIP/source identification, not trusted release** | Pinned Git commit/tree, both independently SHA-checked ZIPs, PR31 raw/canonical seal, source hashes and 350 hosted logs. Eleven real release prerequisites absent; no signed owner trust root. |
| Teacher-facing usefulness | **LIMITED / informational** | Clear future expected-vs-observed interface; no explorable simulation or actual quantitative physical outputs. |
| Textbook-answer completeness | **NOT ASSESSED / not in scope** | This is an output-schema inventory, not a completed exercise or simulation. |

## Release advice and mandatory hard stop

**SCOPED PASS applies to this exact source SHA only.** The offline inventory correctly communicates original **expected** 37 exports, four integral histories and nine requests, all uncomputed by native execution. It does not approve the historical draft for production merge and must not be reported as H1-C1 native PASS or physical validation. The Python shape validator is deliberately insufficient on its own: any future caller processing externally supplied receipts must use full source-bound exact checking and separate native provenance gates.

**Keep PR46 historical/draft/unmerged.** Before any real native OMC version/build/launch, require a separately reviewed **non-regenerating executable adapter and plan**, protected owner-authenticated scientific release with independent backup, actual observed host/compiler/MSL fingerprints, durable owner-controlled external atomic one-shot reservation, independent pre-native R2, and **new explicit owner authorization naming the allowed version query, build, single launch and no-retry budget**. None is granted by this report or existing Option A.

**Final result: SCOPED PASS; no in-scope changes requested; no native permission.**
