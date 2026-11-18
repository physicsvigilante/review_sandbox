# Conductor_sim PR #89 — independent Chat B targeted R4 review #04

**Verdict: CHANGES REQUESTED (P2, locally decidable scientific-export integrity defect).** The specific R3 invented `t=0` turning-point acceptance is fixed, but a **new counterexample** at a coincident saved timestamp remains accepted by the standalone M37a JSON validator. The candidate is **not ready for an owner merge decision** despite terminal green production CI. This is a bounded export-validation finding, **not** a renewed Kelvin/M16a/FEMM scientific audit or a finding against the unchanged public typed observer.

**Reviewer:** independent Chat B, 18 November 2026. Actual source-pinned GitHub Actions execution, not a static reading of developer tests. The R2/R3 reviewer-authored harnesses were reused with source pins and the standard-library `bisect` import allowance updated; new R4 adversarial cases were independently authored. Production was never modified, merged or marked ready.

## 1. Source gate verified

| Gate | Actual observed |
| --- | --- |
| [Production PR #89](https://github.com/physicsvigilante/conductor_sim/pull/89) | Live **OPEN / DRAFT / UNMERGED**; head remained unchanged during review |
| Exact production HEAD | `d843a981a2b5ba4591f1c1afd169fd49bca7083f` |
| Native Git TREE | `77afef9445a3ac65d228dfe029bb7c0d5b67ba10` |
| Prior independently reviewed R3 | `630f6d320a1b4cb00bf7bb0780cd3deca4ec0f7e` / tree `796f319edf5829455e842d9bad63b770d17ff9fa` |
| Exact R3→R4 changed files | `tools/m37a_ground_wire_reference.py`; `tests/test_m37a_grounded_wire_current.py`; `docs/m37a.md` **only** |
| Original PDF blob | `90d8869b0f01cc2ea13f83721985a5d8419f1d0e`, unchanged |
| Original PDF SHA-256 | `9dff3c02a9f1848d2c3d99cb1a6e7a44dc7f5a51f7a3a2b8cc92d10ce1fbca5d`, unchanged |
| Source worktree after test | Clean: no tracked production changes |

The independent Ubuntu runner asserted actual `git rev-parse HEAD`, `HEAD^{tree}`, the exact diff, workbook blob/hash, live PR state and source-clean status, using `set -euo pipefail`. No production physics, public M37a observer, M16a integrator, Kelvin solver, FEMM, renderer or original workbook changed in the R3→R4 delta. The historical source interpretation and physics evidence can therefore be retained without another broad scientific audit.

## 2. Genuine independent executions, including first red evidence

- [First R4 run #44325743876 — FAILURE](https://github.com/physicsvigilante/review_sandbox/actions/runs/44325743876): source gate passed; the unchanged reviewer-owned R2 replay passed **99/99**; 54 R4 observations produced 2 red entries. One was a **reviewer matcher error**: a fabricated terminal turning event was correctly rejected as `turning-point event has no later velocity witness`, while its expected regex did not yet accept that valid, specific scientific reason. The other was a **genuine unexpected acceptance** of the coincident-time position forgery below. The full first-attempt run and data are retained, never reclassified as green.
- [Corrected reviewer matcher run #44326169759 — FAILURE](https://github.com/physicsvigilante/review_sandbox/actions/runs/44326169759): only the reviewer regex and discrepancy assertion were tightened; **the production source remained identical**. R2 replay **99/99**. R4: **54 observations**, including 3 genuine accepted histories, 1 native-turning-bracket positive, 1 separately documented proof-ceiling probe and **49 hostile cases**; **48 hostile cases rejected as intended**, **1 hostile case unexpectedly accepted**, **zero reviewer matcher/setup failures**. The failure is the same physical defect isolated in the first run.
- The reviewer source checker import AST contains only `__future__`, `argparse`, `bisect`, `json`, `math`, `pathlib`, all Python standard library. There is **no imported production physics**. The real native histories were newly generated and serialized/deserialized before hostile verification.

Immutable R4 evidence, including both first attempts, is preserved in [reviewer branch `4c04f3ba`](https://github.com/physicsvigilante/review_sandbox/tree/4c04f3baed3c78d9961ab46bc780b521cfea8969/projects/conductor_sim/pr-89/reviews). See [reviewer-owned R4 suite](https://github.com/physicsvigilante/review_sandbox/blob/4c04f3baed3c78d9961ab46bc780b521cfea8969/projects/conductor_sim/pr-89/reviews/challenge_r4_turning.py), [final R4 results](https://github.com/physicsvigilante/review_sandbox/blob/4c04f3baed3c78d9961ab46bc780b521cfea8969/projects/conductor_sim/pr-89/reviews/evidence/r4-run-44326169759-attempt-1/f4/r3-f4-results.json) (legacy R3-style results filename), and [inherited R2 result file](https://github.com/physicsvigilante/review_sandbox/blob/4c04f3baed3c78d9961ab46bc780b521cfea8969/projects/conductor_sim/pr-89/reviews/evidence/r4-run-44326169759-attempt-1/r2-replay/independent-results.json).

### What passed

| Challenge | Actual R4 result |
| --- | --- |
| **Original R3 invented first-sample turn:** `t=0`, saved `v=-0.05 m/s` | **REJECTED AS INTENDED:** `turning-point event cannot occur outside the sampled interior` |
| False interior coincident turn with nonzero saved velocity | **REJECTED:** `contradicts nonzero velocity at same saved timestamp` |
| False off-grid turn without velocity sign reversal | **REJECTED:** missing physical outward→inward reversal |
| Physically forbidden inward→outward reversal | **REJECTED:** missing outward→inward reversal |
| Duplicate genuine turns | **REJECTED:** one attractive sphere cannot produce multiple turns |
| False local radial maximum | **REJECTED:** not a radial-distance maximum |
| False non-axial exact-sample event, bad time types, bool time | **REJECTED** for intended geometry/finite-SI-time reasons |
| Original F4 trio: fabricated energy maximum, negative guard, spurious guard event | **REJECTED**, including via inherited R2 replay |
| Sampled F1/F2/F3 SI units, state, identity and provenance attacks | **REJECTED**, inherited R2 replay 99/99 |
| Authentic duration example | **ACCEPTED**, 6 samples |
| Authentic M16a off-grid turning history | **ACCEPTED**, 71 samples |
| Authentic real near-surface guard termination | **ACCEPTED**, 9 samples |

The independently regenerated authentic turning event was at `t=0.1316369937419222 s`, between sampled times `0.130 s` and `0.135 s`; its **outward then inward** signed radial velocities were respectively `+0.00012393782249118274` and `−0.0002546157385619742 m/s`. Its event radius `0.23065707446869868 m` exceeded both bracketing sampled radii. This genuine off-grid history passed.

## 3. New blocker — event and sample disagree on position at *exactly the same time*

**Case:** `novel/exact-sample-zero-velocity-but-different-event-position`. This is an independently generated, locally checkable contradiction, not an assertion that exported JSON proves exact ODE integration.

Start with the **real** 71-sample native turning history just described. Copy the document, retaining its actual saved positions, charges, forces and conductor geometry. Replace the event's time with the *existing* next saved sample's time `t=0.135 s`. Set that saved sample's signed velocity to exactly zero, and consistently recompute its SI velocity vector, Kelvin current/rate, kinetic energy, total mechanical energy, energy drift and overall maximum drift. **Keep the event's physically axial position at the originally reported maximum**. The event is still inside the history, has outward→inward witnesses on its adjacent rows, lies outside the guard and passes the radial-maximum check.

Yet the two simultaneously saved positions are different:

| Field at `t=0.135 s` | Saved JSON |
| --- | --- |
| Sample signed velocity | `0.0 m/s` |
| **Turning event** `position_m` | `[0, 0, 0.23065707446869868]` m |
| **Same-time sample** `position_m` | `[0, 0, 0.2306566463320074]` m |
| Event minus sample displacement | `+4.2813669129805436e-7 m` |
| Euclidean same-time position discrepancy | `4.281366912939344e-7 m` |

The standalone `validate_examples()` **returned normally (unexpected acceptance)**. The two positions differ by ~0.428 micrometres. Both event and sample independently satisfy the authored axis relation, but no single particle can occupy two different positions at the **same exact saved time**. This is locally decidable from one JSON record: it needs **no ODE propagation, source authenticity trust or off-grid root inference**.

[Exact hostile JSON from the second independent run](https://github.com/physicsvigilante/review_sandbox/blob/4c04f3baed3c78d9961ab46bc780b521cfea8969/projects/conductor_sim/pr-89/reviews/evidence/r4-run-44326169759-attempt-1/f4/hostile/novel--exact-sample-zero-velocity-but-different-event-position.json).

**Required bounded correction:** when a saved `turning-point` event has **exactly the timestamp of an interior saved sample**, require its signed displacement and physical position to agree with that **same** row to a documented, tight floating-point tolerance. Enforce alongside the existing near-zero same-time velocity, allowed outward→inward bracketing and radial-max checks. Preserve authentic **off-grid** M16a turning events and the existing F1–F4 and guard positives. Add this exact hostile mutation as a production regression test; a corrected source requires a new exact-HEAD/TREE and focused independent replay. **Do not expand the task to a fourth broad Kelvin/induction review.**

## 4. Proven limits and exact-HEAD CI

A separate JSON-consistent **retiming** of a physical trace and an elided guard event with a duration label remain document-only proof limits: the checker does not export the original requested duration and does **not** independently re-integrate M16a. The R4 `proof-limit/stripped-guard-claimed-duration` was accepted and **explicitly counted as a documented limitation**, not hidden as a pass or treated as the new blocker. The unchanged public typed observer's genuine M16a reintegration is a separate stronger evidence boundary.

**Terminal production CI on the exact reviewed HEAD: 25/25 SUCCESS**, 23 pull-request workflows + 2 branch-push workflows, none pending, failing or cancelled. Checks included Python, both dedicated M37a Python 3.10/3.12, historical Chromium/source integrity, and actual FEMM 5. Independently captured [exact SHA CI inventory](https://github.com/physicsvigilante/review_sandbox/blob/4c04f3baed3c78d9961ab46bc780b521cfea8969/projects/conductor_sim/pr-89/reviews/evidence/r4-run-44326169759-attempt-1/ci-live-summary.txt). CI green does **not** override a demonstrated export-validity failure.

Historical red R1/R2/R3 reports and R3 [first failed reviewer run #44320918820](https://github.com/physicsvigilante/review_sandbox/actions/runs/44320918820) remain unchanged. The new R4 first failed run also remains explicitly red.

## 5. Disposition

**CHANGES REQUESTED**, for precisely the same-timestamp position mismatch accepted by the standalone exported-JSON checker. The earlier R3 t=0 blocker is corrected; genuine M16a duration/turning/guard and the inherited independent SI battery pass; no broader physical-system defect has been shown in the unchanged production code.

**Leave production PR #89 DRAFT and UNMERGED.** No production edits, GitHub review approval, mark-ready, merge, historical evidence rewrite or postmerge claims were performed. A later independent targeted PASS on corrected exact HEAD/TREE with all exact-source production CI green would permit **asking the owner** for a separate explicit merge decision; it is not itself merge authorization.
