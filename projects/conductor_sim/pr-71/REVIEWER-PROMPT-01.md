# Fresh independent Chat B R2 review — conductor_sim M31a PR #71

**The candidate is 16/16 exact-head CI green, but NOT eligible for merge until YOUR independently authored source-pinned PASS. This is a developer handoff, not a reviewer verdict.**

Read the [full exact-source M31a REQUEST](REQUEST.md), [central protocol](../../../PROTOCOL.md), [R2 risk policy](../../../REVIEW-RISK-POLICY.md), [report template](../../../REVIEW-TEMPLATE.md), exact-source [frozen preimplementation charter](https://github.com/physicsvigilante/conductor_sim/blob/e8970e26b91f6f8dfe3bd8bffcaf8f181449870b/docs/m31a_charter.md) and [physical/JSON contract](https://github.com/physicsvigilante/conductor_sim/blob/e8970e26b91f6f8dfe3bd8bffcaf8f181449870b/docs/m31a.md). Inspect accepted M20b/M22a/M28a/M29a/M30a/M30b physical/model contracts and source-root AGENTS.md if it exists.

**Source PR:** https://github.com/physicsvigilante/conductor_sim/pull/71

**EXACT SOURCE HEAD:** **e8970e26b91f6f8dfe3bd8bffcaf8f181449870b**

**Actual SOURCE Git tree:** **15e658dfae00289e27a577f5f1df1c340e8e1c72**

**Base/main reviewed M30b release:** **293d4b22a6eeb4bc56a5598d8b6935ef91f19826** (16/16 postmerge green).

Source PR was DRAFT, UNMERGED at handoff. Recheck live head/tree and CI before judging; stale evidence must not produce PASS for a moved source.

## What to challenge scientifically

M31a does **not** implement new Coulomb/rod/gravity field laws, FEMM conductor equilibrium, root finder, RK integrator or 3D scene graph. It exposes a **bounded typed way to apply 2..4 coordinated physical property changes ATOMICALLY** to the real original or independently reassembled fixed-source world, using unchanged M22a/M29a source composition, M28a physical-target/shape allowlist and one existing M20b revise_scenario call for complete-world qualification, then the original native particle integrator. It enables teachers to ask new physically valid coupled what-if questions without reauthoring per-case solver code. One scenario is fixed throughout a run; no source moves during time.

**Independently review:**

1. Trace one physical model original→genuine M22a source inventory→one M20b atomic **two-property grandchild**, verifying source ID/name/type, original/structural/grandchild SHA and immediate parent_revision_id, immutable original and real native SI trajectory. New/replaced source IDs can be changed, old retired IDs must not be resurrected.
2. **Critical atomic-admission test:** original M29a point-replace has a held point at (0.2,0,0) and a probe initially (0,0.1,0), with genuine xy-plane motion. Unilaterally moving EITHER one point along +z by .05m is physically refused by the preexisting fixed-point reflection/plane qualifier. Moving BOTH together in ONE M20b revision must be admitted, preserving original relative motion/force exactly under a +0.05m z translation. Check actual samples and qualification, not merely declarations.
3. Independently calculate new-source + probe-mass/launch kinematics and added-gravity + held-E kinematics against real accepted numerical samples, including F=qE+mg and units, not an existing production field evaluation. Challenge invalid full-world edits and source guards. If possible author your own unfamiliar tilted finite rod + signed points/gravity and newly added held point, with a **coupled source charge + probe mass** change, using independent analytical Coulomb/rod quadrature + SciPy DOP853.
4. Verify **stage-specific refusals**: structurally invalid world → no accepted inventory; admitted structural model but absent/retired/gauge/no-op/wrong-shaped target → rejected-coupled-edit retaining true parent inventory; individually valid edits but inadmissible **joint physical model** → rejected-physical-model with no invented trajectory; admitted grandchild but recognized integration error → integration-failed; real completed or source-guard-censored native histories. Unrelated sibling must remain independently evaluated, no state after guard or interpolation.
5. Check typed bounded plan: 1..5 named hypotheses, 2..4 edits each/max16, one whole scalar or 3-vector physical SI value per existing M28a-allowlisted target, stable IDs not array indices, no Boolean/nonfinite values or imported arbitrary JSON impersonating native objects. No numerical step/tolerance, guard, duration, source MEMBERSHIP or analysis plane changed by a property patch; preserve intentional teacher hypothetical provenance.
6. Audit honest comparisons: original M28a _shared_rows on literal matching saved physical times **relative to the ACTUAL selected physical parent**, not against unrelated original or by array position; no derivative, source movement/contact, cross-inventory ΔU interpreted as work or implied conductor response.

## Source-pinned developer evidence — NOT independent PASS

- Exact-current-head **16/16 workflows SUCCESS**.
- [Python 3.10 and 3.12 #43920210856](https://github.com/physicsvigilante/conductor_sim/actions/runs/43920210856): **1,886 passed per interpreter, 97 actual-FEMM-only skipped, 16 warnings**, all **10** new M31a native tests passed.
- [Actual FEMM5 #43920210710](https://github.com/physicsvigilante/conductor_sim/actions/runs/43920210710): **97 passed historical conductor regressions**, not an independent nested-source physical reference.
- [Real Chromium/retained visualization #43920210929](https://github.com/physicsvigilante/conductor_sim/actions/runs/43920210929): PASS, **no new M31a-specific HTML**. [Historical visualization artifact #14253092476](https://github.com/physicsvigilante/conductor_sim/actions/runs/43920210929/artifacts/14253092476): GitHub-reported ZIP SHA256 **63300d2c64945872fda47f0bdeae639ab1242cefa8bc6e0caa16ef27b83bb2eb**, not independently rehashed by developer. Distinguish synthetic PR merge commit.txt from the real reviewed source SHA/tree.
- [Developer-authored novel genuine source + mass transfer harness](https://github.com/physicsvigilante/review_sandbox/blob/4dbf30e06e0b6b898b19c47b61e63ea089ce25c5/projects/conductor_sim/pr-71/transfer/run_transfer.py), [successful exact-source CI #43920562002](https://github.com/physicsvigilante/review_sandbox/actions/runs/43920562002). Noncanned tilted +2.8nC rod, two original signed held point charges, gravity g=(0,-.08,0) m/s², +0.8nC probe initially mass 9e-6 kg with source-added +1.5nC point, then TWO atomically coupled property grandchildren changing the **new source** to +2.4nC and mass 1.5e-5 kg, or +0.6nC and mass 1.1e-5 kg. Four genuine native physical trajectories each 101 original saved states, compared against independently CODED 96-node SI rod Gauss–Legendre Coulomb + SciPy DOP853, all passed, max absolute 3D position error below **7e-15m**. Correct source SHA/tree, two-edge lineage, only original native exact-time comparisons, structural-vs-target-vs-whole-model refusals. Developer-authored harness PASS is NOT independent Chat B scientific attestation.
- [Original native JSON/receipt artifact #14253131868](https://github.com/physicsvigilante/review_sandbox/actions/runs/43920562002/artifacts/14253131868), GitHub-reported SHA256 **207c779839324dd4d4ab581259928ba16233254c32c3c1a0ac9595ceb79c5397**, NOT independently rehashed by developer. Download, hash, reconstruct model SHA/independent physical references and state what you independently performed.
- **Historical first failure preserved:** earlier test-bearing commits had ONE test-only wrong expected error message for the genuinely refused individually off-plane fixed point; **1 failed/1,885 passed** on first candidate. Latest source corrects only test expectation and received fresh 16/16 full current-head CI. This does not constitute a production-code bug or a first-run pass.

## Report your actual independent verdict

Create a NEW, separately authored file on **physicsvigilante/review_sandbox/main**:

**projects/conductor_sim/pr-71/reviews/review-01-chat-b.md**

Include exact source HEAD/tree, independently executed/recalculated tests and error tolerances, downloaded artifact hashes, source-provenance/whole-world qualification/physical and numerical truth, explicit release findings with path/line and any unknowns, and **PASS / CHANGES-REQUESTED / INSUFFICIENT-EVIDENCE**. Do not claim unperformed tests passed. A separate ChatGPT context is not a different-model guarantee or independent human certification.

**Do not edit, mark ready, approve on GitHub, or merge source PR #71.** Owner standing direction allows routine merge ONLY after a fresh independent R2 PASS without blockers and exact unchanged source HEAD/tree + full CI, using expected-head merge lease, followed by postmerge verification. Otherwise publish a precise blocker and request targeted correction/re-review.
