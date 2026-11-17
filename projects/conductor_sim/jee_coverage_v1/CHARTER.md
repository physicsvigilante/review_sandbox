# JEE-30 v1 — Frozen problem-family coverage evaluation charter

**Purpose:** Shift `conductor_sim` evaluation from software feature counts to **actual JEE-relevant physical problems**. This is independent benchmark planning against released M34b `main` and does not change or imply release of draft M35a PR #81. Benchmark materials live in `review_sandbox` so ongoing source R2 review stays source/tree-pinned and unchanged.

## Provenance and educational scope

- The initial 30 cards in `cases.json` are **new, synthetic, teacher-style prompts**, not copied from JEE papers or the user's PDFs. These probe JEE-relevant principles, but must **never** be reported as 30 actual past-year questions or as a scored blinded benchmark before evaluation. Numerical values are explicitly invented for assessment; do not attribute them to a book.
- Topic anchor is the officially published [JEE Advanced 2026 Physics syllabus](https://jeeadv.ac.in/documents/jee-advanced-2026-syllabus.pdf), plus the repo's own [evaluation contract](https://github.com/physicsvigilante/conductor_sim/blob/a5113fa4cc924ac10cbb35b2f2d7ac80e11f1bde/docs/evaluation_contract.md). The JEE Advanced 2027 syllabus webpage was not yet populated on 17 Nov 2026; do not imply all 2027 content is final.
- Separately retain verified original source-anchored workbook exercises (M13c/M21b), but **do not** quietly substitute illustrative parameters for textbook-provided givens. A later hold-out should use the actual source PDFs/diagrams only after explicit visual transcription/provenance checks.
- Freeze original cards before attempts. New or corrected cards require a versioned amendment, not retrospective edits to improve apparent success. Reviewer should select unknown variations and use independent formulas/reference methods rather than production field callbacks as an oracle.

## 30 original cards: six equally represented physical regimes

| Family | Cards | Classroom phenomenon |
| --- | --- | --- |
| F — Electric field and potential | F01–F05 | superposition, zero E vs zero V, finite rod, rings, axial disk |
| C — Conductors and boundary conditions | C01–C05 | grounded/isolated induction, cavities, nested shells, wired redistribution |
| W — Work, energy and dipoles | W01–W05 | potential/work, transverse forces, induction energy, static conductor energy, dipole torque |
| M — Genuine motion/events | M01–M05 | plate deflection, turning, ring axis, Coulomb orbit, time-dependent/moving-source limitation |
| X — Model exploration | X01–X05 | mass sweeps, new sources, new detectors, sibling source IDs, iterative forks |
| R — Limits/refusals/discontinuities | R01–R05 | surface jumps, off-axis disk, nonaxisymmetric conductors, nonplanar force, drag |

**Provisional support classifications** in cards are research hypotheses only, not measured results. Each card must receive actual baseline admission/execution proof or a typed refusal and independently justified domain assessment. Correct scope/refusal is separately graded; an unsupported case cannot be counted as a simulated success.

## Non-negotiable five-dimensional grading (reuse normative contract)

1. Interpretation fidelity: original physical objects, charge signs, source motion, apparatus geometry, constraints, original vs illustrative values; `pass/partial/fail/not_evaluated/not_applicable`.
2. Physical correctness: qualified equations, SI units, independent analytic/quadrature references or convergence/limit study; same status set.
3. Simulation coverage: `supported/partially_supported/unsupported/not_evaluated`, with represented and excluded phenomena. A correct refusal is **not** a successful simulation.
4. Educational usefulness: actual source geometry/readouts, E/V graphs, energy or true-time playback as appropriate; same statuses and real browser checks if claiming usability.
5. Textbook-answer completeness: `not_attempted/complete/partial/mismatch/not_applicable`, optional; not a gate for verified simulations.

Do not collapse these into one ambiguous score. Report **distinct denominators**: 30 preregistered cards, interpreted, correctly admitted, full simulations executed, independent-physics verified, faithful partials, justified refusals, student-usable visualizations and optional complete written solutions. Keep unrun cases as **not evaluated**, never guessed PASS.

## Reproducible phased execution

- **Phase 0 (this charter + card bank):** version and validate 30 original cards, each with givens/observable/reference/viewer and expected scope. No baseline coverage score is asserted.
- **Phase 1:** independent, literal M34b source HEAD/TREE fixture-run for at least 6 *new* synthetic problems (field/potential, motion/event and honest refusals), computing separate SI analytic results. Record each actual physical result/valid refusal and status; this is not a full 30/30 evaluation.
- **Phase 2:** all 30 candidates on released baseline and afterward a separately R2-reviewed M35a if merged. Freeze authoring attempts, measure success by strata and evidence type; compare physics and visualization separately. Do not implement a custom per-card source law.
- **Phase 3:** at least 10 unseen problems from source-verified worksheets or official JEE problems and a fresh independent reviewer. Publish which expected phenomena are missing and prioritize *reusable* source/constraint/visual primitives that unlock multiple cards.

## Release and trust rules

An external benchmark runner may test released `main`; it does not grant permission to merge M35a, bypass original source/tree-pinned Chat B R2 or change the candidate. The in-process native receipts are evidence consistency checks, not external cryptographic authentication. Real FEMM and Chromium checks must remain distinct. No future work should be called complete without actual completed execution/evidence. Legacy sweep export weakness [issue #80](https://github.com/physicsvigilante/conductor_sim/issues/80) remains a separate high-priority defect and must not be hidden by benchmark scores.
