# Independent R2 review — conductor_sim M31a PR #71

- **Project/source:** [physicsvigilante/conductor_sim](https://github.com/physicsvigilante/conductor_sim)
- **Source PR:** [#71](https://github.com/physicsvigilante/conductor_sim/pull/71), DRAFT and UNMERGED at review close.
- **Source base:** `293d4b22a6eeb4bc56a5598d8b6935ef91f19826`
- **Exactly reviewed source HEAD:** `e8970e26b91f6f8dfe3bd8bffcaf8f181449870b`
- **Verified actual Git tree (from Git commit API):** `15e658dfae00289e27a577f5f1df1c340e8e1c72`
- **Pinned diff:** [PR #71 files](https://github.com/physicsvigilante/conductor_sim/pull/71/files)
- **Reviewer:** Chat B, separate ChatGPT conversation, GPT-6. Separate context is not independent human adjudication or guaranteed different weights.
- **Date/time:** 2026-11-16, approximately 23:36 IST.
- **Review scope:** R2 physical/numerical composability, source lineage, typed evidence integrity, refusal boundaries, CI and historical nonregression.
- **Source changes by reviewer:** None. No branch, PR, tests, merge or approval changed in `conductor_sim`.
- **Outcome: CHANGES-REQUESTED (one bounded evidence-integrity blocker, not a demonstrated physical-law or numerical-path defect).**

## Finding F-01 — BLOCKER / result evidence authentication and numerical-status classification

**Locations (exact reviewed HEAD):**
- [`src/conductor_sim/coupled_physical_family.py` lines 217–224](https://github.com/physicsvigilante/conductor_sim/blob/e8970e26b91f6f8dfe3bd8bffcaf8f181449870b/src/conductor_sim/coupled_physical_family.py#L217-L224): `CoupledPhysicalRun.__post_init__` checks trajectory `.spec` identity and `.termination`, but not native trajectory type or actual comparison contents.
- [lines 299–311](https://github.com/physicsvigilante/conductor_sim/blob/e8970e26b91f6f8dfe3bd8bffcaf8f181449870b/src/conductor_sim/coupled_physical_family.py#L299-L311): any return termination other than `duration` is labeled `censored`.
- [lines 166–173](https://github.com/physicsvigilante/conductor_sim/blob/e8970e26b91f6f8dfe3bd8bffcaf8f181449870b/src/conductor_sim/coupled_physical_family.py#L166-L173): serialization emits `entry.trajectory.as_dict()` and user-supplied comparison rows.
- [`src/conductor_sim/prescribed_motion.py` lines 212–220](https://github.com/physicsvigilante/conductor_sim/blob/e8970e26b91f6f8dfe3bd8bffcaf8f181449870b/src/conductor_sim/prescribed_motion.py#L212-L220): `TestChargeMotionResult` has no constructor-level termination enum enforcement.

**Expected:** Under the frozen M31a P8 acceptance requirement, a public typed result must not accept an arbitrary non-native object impersonating a native trajectory, an unrecognized numerical termination, or invented comparison timestamps as evidence of a completed/censored physical run. The retained ordinary native solver has `duration` and mapped `source-guard` terminations; unexpected codes are not evidence of a source guard.

**Observed in pinned source (static, deterministic code-path finding):** An object with arbitrary `as_dict()` data, attributes `spec` pointing to an accepted candidate's exact `spec` object and `termination="duration"` is sufficient to pass the `CoupledPhysicalRun` trajectory checks if supplied in a manually constructed `CoupledPhysicalEntry` with `status="complete"`. A `dataclasses.replace` copy of a genuine `TestChargeMotionResult` with `termination="unknown"` similarly passes when entry `status="censored"`. Separately, `entry.comparisons` is accepted as any tuple of dicts, including invented timestamps, because it is not checked against `_shared_rows` in the result validator.

**Small reproducible regression request (source-execution probe; not claimed as personally run):**

~~~python
from dataclasses import replace
from conductor_sim.coupled_physical_family import CoupledPhysicalRun

# Use a real complete result: run = run_coupled_physical_family(valid_plan)
good = run.entries[0]
class FauxNative:
    def __init__(self, spec):
        self.spec, self.termination = spec, "duration"
    def as_dict(self):
        return {"schema": "forged", "samples": [{"time_s": 9999}]}

bad_type = replace(good, trajectory=FauxNative(good.scenario.spec),
                   status="complete", comparisons=())
# Current code path allows this instead of refusing it:
CoupledPhysicalRun(run.plan, run.structural_run, (bad_type, *run.entries[1:]))

bad_termination = replace(
    good, trajectory=replace(good.trajectory, termination="unknown"),
    status="censored", comparisons=())
CoupledPhysicalRun(run.plan, run.structural_run,
                   (bad_termination, *run.entries[1:]))

bad_rows = replace(good, comparisons=({"time_s": 9999,
                                       "delta_position_m": (999, 0, 0)},))
CoupledPhysicalRun(run.plan, run.structural_run,
                   (bad_rows, *run.entries[1:]))
~~~

This is **not** evidence that the actual `run_coupled_physical_family` currently fabricated a history: the reviewed genuine native samples all had `duration`, and its internally computed `_shared_rows` were truthful. The defect is the **public typed result validation** accepting manually substituted non-native/mismatched evidence, contrary to P8, and the unchecked unknown-termination fallback. This is not a claim of cryptographic provenance or a requirement to distrust all authored Python code.

**Required bounded correction:** Enforce `type(trajectory) is TestChargeMotionResult` and explicitly accepted native terminations (`duration` / `source-guard`) in the validator and runner. Reject an unknown termination rather than silently translating it to `censored`. Cross-check comparison rows against `_shared_rows(actual_immediate_parent_trajectory, trajectory)`, including exact time provenance, rather than trusting an arbitrary tuple. Add focused regressions for the three probes above plus legitimate guard censoring and the existing jointly valid +z translation. Do not alter the physical field laws, whole-model requalification, integrator, historical data, or existing original-source evidence. If the result object is intentionally not a trust boundary, narrow the P8/authenticity claims explicitly instead of allowing a broader guarantee to stand.

**Evidence type:** independent pinned-source reading and logically derived counterexample; **the above negative probes were not run against an installed source package in this reviewer environment**. Confidence high on the precise Python branch conditions; final correction should be verified with actual source-execution tests.

## Independent evidence, numerical calculations and source lineage

### Live source and CI

- Rechecked PR #71 via the connected GitHub API: head remained `e8970e26...`, base `293d4b22...`, draft `true`, merged `false`. Queried exact Git commit API and verified actual source tree `15e658df...`.
- Queried all exact-head workflow runs: **16/16 completed SUCCESS**. Inspected source GitHub Actions job logs, not merely developer's packet.
- [Python checks #43920210856](https://github.com/physicsvigilante/conductor_sim/actions/runs/43920210856): Python 3.10 and 3.12 logs each say **1,886 passed, 97 skipped, 16 warnings**, with ten new M31a tests passing (test file shows ten dots). This is CI evidence, **not** tests I personally reran.
- [Real FEMM 5 #43920210710](https://github.com/physicsvigilante/conductor_sim/actions/runs/43920210710): successful historical real-conductor workflow; its 97 historical tests are not independent M31a nested-source numerical references.
- [Visualization #43920210929](https://github.com/physicsvigilante/conductor_sim/actions/runs/43920210929): successful historical real Chromium/browser workflow. No M31a-specific HTML is claimed or present in the downloaded artifact. Its `commit.txt` contains synthetic PR merge SHA `7928409dec3d9360f8b17010bf154d3f122855db`; **not** the exact reviewed source HEAD.
- Root source `AGENTS.md` lookup returned 404 at the pinned source HEAD. Read original [M20b](https://github.com/physicsvigilante/conductor_sim/blob/e8970e26b91f6f8dfe3bd8bffcaf8f181449870b/docs/m20b.md), [M22a](https://github.com/physicsvigilante/conductor_sim/blob/e8970e26b91f6f8dfe3bd8bffcaf8f181449870b/docs/m22a.md), [M28a](https://github.com/physicsvigilante/conductor_sim/blob/e8970e26b91f6f8dfe3bd8bffcaf8f181449870b/docs/m28a.md), [M29a](https://github.com/physicsvigilante/conductor_sim/blob/e8970e26b91f6f8dfe3bd8bffcaf8f181449870b/docs/m29a.md), [M30a](https://github.com/physicsvigilante/conductor_sim/blob/e8970e26b91f6f8dfe3bd8bffcaf8f181449870b/docs/m30a.md), [M30b](https://github.com/physicsvigilante/conductor_sim/blob/e8970e26b91f6f8dfe3bd8bffcaf8f181449870b/docs/m30b.md) and exact M31a charter/contract.

### Actual downloaded, independently hashed artifacts

| Original GitHub artifact | Independently downloaded ZIP SHA-256 | Result |
| --- | --- | --- |
| [Native transfer #14253131868](https://github.com/physicsvigilante/review_sandbox/actions/runs/43920562002/artifacts/14253131868) | `207c779839324dd4d4ab581259928ba16233254c32c3c1a0ac9595ceb79c5397` | Matches GitHub-reported digest |
| [Historical Chromium artifact #14253092476](https://github.com/physicsvigilante/conductor_sim/actions/runs/43920210929/artifacts/14253092476) | `63300d2c64945872fda47f0bdeae639ab1242cefa8bc6e0caa16ef27b83bb2eb` | Matches GitHub-reported digest |

Within the native ZIP, independently hashed `native-coupled-worlds.json`: `d9835a918da148bae7b48f8a09f3d08c5ca95df69f6fc4f4f3a49e0c7da96190`; its digest agrees with the downloaded `transfer-receipt.json`. No claim is made that a SHA proves physical correctness: that required separate recalculation.

### Independently recalculated physics against the *actual retained native samples*

Parsed the raw original/native structural/coupled trajectory JSON and independently coded:
1. A **closed-form electric field of a finite uniformly charged straight rod** (not the developer's 96-point quadrature, and not conductor_sim's production field evaluator), plus two original signed point charges and the added held source when present.
2. Standalone SI force and acceleration `F=qE+mg`; separately checked stored electric field, electric force, gravitational force and total force at **every retained sample**.
3. A separate high-accuracy **SciPy DOP853** integration at the actual 101 saved times in each of four recorded runs (rtol `8e-13`, atol `8e-15`, max_step `0.003 s`, using actual initial state and mass). This is an independent reference solver run locally, **not** a new invocation of the source engine.
4. An auxiliary 192-node Gauss–Legendre check of the analytical rod field at the origin. Its difference from the closed form was `1.35e-11 V/m`, corroborating the finite-line expression without relying on native field code.

| Recorded real native world | Samples | Maximum position difference (m) | Maximum velocity difference (m/s) |
| --- | ---: | ---: | ---: |
| Original tilted rod + two signed points + gravity | 101 | 6.54e-15 | 2.72e-14 |
| Independently reassembled world with +1.5 nC new held point | 101 | 6.89e-15 | 3.20e-14 |
| Coupled new source +2.4 nC and probe mass 1.5e-5 kg | 101 | 4.02e-15 | 1.18e-14 |
| Coupled new source +0.6 nC and probe mass 1.1e-5 kg | 101 | 5.30e-15 | 1.86e-14 |

- All 404 saved 3D states span 0 to 0.42 s on the original 0.0042-s clock; all have exact z=0 under the qualified physical plane.
- Maximum recorded-field versus closed-form electric-field vector difference: **1.14e-12 V/m**; maximum recorded total-force discrepancy: **1.07e-21 N**. All 404 gravitational-force components matched exactly in this calculation; acceleration vector residual max **1.12e-16 m/s²**. These are stronger than the developer's coarse pass thresholds (`2e-7 m`, `2e-6 m/s`, `1e-10 N`).
- Both coupled grandchildren have 101 parent-relative exact-time comparison rows; I independently recalculated their 3D Δposition, Δvelocity and norms against the **actual reassembled parent** and found at most **3.47e-18** floating-point discrepancy. No invented time, index matching or interpolation found in this retained sample.
- Reconstructed each scenario's canonical SHA-256 from its exported record: original `a4d09944652460b2c3a36198041c96a9b23fbb62b83c9173dc9d282a7610d1cd`; structural parent `d17fc54584371e8ec2a81881f33d72bd897961cf51f8c8cfabdd936ce327ee30`; coupled strong `49302308d3800152549f98bc06d12280910e6258c6e18ddb9412a8267bc97fcf`; coupled weak `ccc03dafb97ced681658ceb27b0451e42f9af8a531b9e2c2ffa1d035dc3fddbb`. Recomputed M22a assembly digest `4d373dcc2d1663e7853ad067a20147b993324480d913c681aaf79c85d56acefa`. All match the actual retained records; immediate grandchild `parent_revision_id` is the *structural* SHA, not the unrelated original.
- Inspected real source inventories including type and label, stable retained IDs `rod:tilted`, `point:plus`, `point:minus`, added `point:added`. Strong and weak revisions change only `point:added.charge_c` and `test-particle.mass_kg`; no source membership changed by a property revision.

### Scientific/refusal challenges distinguished by evidence level

- **P1 constant electric field + changed mass:** source tests implement independent kinematics. Separately calculated the expected revised acceleration as **(0.0125, 0.0025, 0) m/s²** from q=1 nC, E=(250,50,0) V/m, m=2e-5 kg. The matching actual CI test is [`test_m31a...` lines 42–80](https://github.com/physicsvigilante/conductor_sim/blob/e8970e26b91f6f8dfe3bd8bffcaf8f181449870b/tests/test_m31a_coupled_physical_family.py#L42-L80); I did not freshly execute this original example's native engine.
- **P2 atomic +0.05 m z translation:** mathematically, Coulomb force and the relative probe trajectory are invariant under simultaneous translation of held point and probe, whereas the individually shifted models violate the original fixed-point reflection/plane certificate. The original source CI test checks both one-sided rejections and all samples of admitted translated path ([lines 82–120](https://github.com/physicsvigilante/conductor_sim/blob/e8970e26b91f6f8dfe3bd8bffcaf8f181449870b/tests/test_m31a_coupled_physical_family.py#L82-L120)). Native source was not rerun in my local environment; the analytical invariant was independently assessed.
- **P3 replaced new source / retired old ID:** production selects inventory by actual stable IDs, with source membership carried from structural parent; source tests cover `field:Ey-new` and retired `field:Ey` ([lines 122–138](https://github.com/physicsvigilante/conductor_sim/blob/e8970e26b91f6f8dfe3bd8bffcaf8f181449870b/tests/test_m31a_coupled_physical_family.py#L122-L138)).
- **P4 newly added gravity + electric source:** independently calculated acceleration **(0.018, -2.995, 0) m/s²**, electric force `(1.8e-7,5e-8,0) N` and gravitational force `(0,-3e-5,0) N` from stated inputs. CI tests sample these ([lines 140–159](https://github.com/physicsvigilante/conductor_sim/blob/e8970e26b91f6f8dfe3bd8bffcaf8f181449870b/tests/test_m31a_coupled_physical_family.py#L140-L159)).
- **Refusal stages in actual transfer ZIP:** `bad-structure → skipped-structural-model` with null accepted parent inventory; `missing-id → rejected-coupled-edit` with real original parent preserved; `invalid-plane → rejected-physical-model` with real reassembled parent and no invented child trajectory; two other genuine coupled siblings both `complete`. Verified directly from raw JSON and corresponding reason strings, not solely the developer's summary.
- **P6 guards:** reviewed source implementation and passing source CI test for exact saved times and conditional guard censoring; I did **not** independently run a new censored case or reconstruct a censored native trace. Neither the historical Chromium ZIP nor this transfer ZIP adds M31a-specific source-guard visual evidence.
- **Typed plan:** 1–5 hypotheses, each 2–4 edits and <=16 total; exact native dataclass types, immutable edit tuples, stable source IDs, no Booleans/nonfinite values, unchanged M28a physical allowlist and shape tests, M20b single atomic revision, original M29a full-world integration and no numerical-control/member edits. The new returned *result* object validation gap is F-01, and does not negate these plan-admission checks.
- **Historical first failure:** the earlier wrong expected error text for one valid physical rejection was preserved, corrected by an M31a test-only change; final pinned head passed exact-head CI. Do not describe early failure as an original first-run pass.

## Separate scope judgments

| Dimension | Judgment | Basis |
| --- | --- | --- |
| Source interpretation fidelity | PASS (bounded) | Teacher-authored source facts explicitly marked assertions; original and structural source IDs, labels, kinds and hashes checked |
| Physical and numerical correctness | PASS for examined traces | Closed-form finite-rod field + point charges, gravity and separate DOP853 match 404 actual source-run samples at reported tight errors |
| Native simulation and observable coverage | PASS for tested support; residual unknowns | Four real retained native trajectories, exact clock and 3D force observations; separate source CI covers translation, examples, guards; no fresh native engine rerun by reviewer |
| Evidence integrity / result-validation contract | **FAIL: F-01** | Manually constructed public `CoupledPhysicalRun` can accept non-native or unknown-termination trajectory and invented comparison rows |
| Teacher-facing usefulness / composability | PASS (engine/JSON scope) | New named atomic coupled hypotheses on genuine independently reassembled source worlds; no per-case production solver; no claim of new renderer or conductor response |
| Textbook-answer completeness | N/A | No specific text problem's answer/completeness is asserted |

## Release decision and smallest next step

**CHANGES-REQUESTED** on the result-evidence validation contract only. Keep source PR #71 **DRAFT and UNMERGED**. The independent numerical physics evidence supports genuine atomic composability and shows no demonstrated solver/field-law defect. However 16/16 exact-head CI does not certify the negative forgery/status cases identified here.

Make one narrow correction to the M31a public result/status binding and add the three focused negative regressions; keep actual M20b/M22a/M28a/M29a source and integrator semantics unchanged. Run exact new-head full CI, then obtain **targeted independent re-review** of F-01. Any change to physical/numerical logic beyond this scope requires appropriately wider re-review. No source approval, merge or postmerge claim is made by this report.
