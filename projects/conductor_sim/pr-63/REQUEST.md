# conductor_sim PR #63 — M27b independent R2 physics/motion review request

**Status: AWAITING SEPARATE CHATGPT REVIEW. Source PR is DRAFT and UNMERGED.** Author of this request: Chat A (implementer), NOT an independent reviewer. Owner approval to begin M27b was not permission to merge.

| Pin | Exact value |
| --- | --- |
| projectId | `conductor_sim` |
| sourceRepo | [physicsvigilante/conductor_sim](https://github.com/physicsvigilante/conductor_sim) |
| Source PR | [draft #63](https://github.com/physicsvigilante/conductor_sim/pull/63) |
| baseSha | `4a967f469df999bc4a97c434dfdd6b69f49893ba` (exact verified M27a merge on main) |
| **exact review headSha** | **`08ad6ea0a30d440f70f83f89e865a87fe9a0f96f`** |
| **source tree SHA** | **`2affa61b9efd44f5949f5c6e8136f8ad179e893b`** |
| riskClass | **R2** — physical motion-plane admission, new charged-wire numerical guard, source-geometry evidence |
| reportDestination | `projects/conductor_sim/pr-63/reviews/review-01-chat-b.md` (authored by Chat B, not Chat A) |

Read [protocol](../../../PROTOCOL.md), [risk policy](../../../REVIEW-RISK-POLICY.md), [report template](../../../REVIEW-TEMPLATE.md), exact-head [source composability contract](https://github.com/physicsvigilante/conductor_sim/blob/08ad6ea0a30d440f70f83f89e865a87fe9a0f96f/docs/composability_contract.md) and [teaching evaluation contract](https://github.com/physicsvigilante/conductor_sim/blob/08ad6ea0a30d440f70f83f89e865a87fe9a0f96f/docs/evaluation_contract.md). Verify whether source AGENTS.md exists rather than assuming one.

## Physical model and changed relationships

M27a already added a thoroughly reviewed static 3D off-axis E/V law for an ideal, **fixed nonconducting** charged ring, `UniformRingField`. M27b **does not change that field law, RK4 integrator or core F=qE + mg force model**. Instead it admits the new source type to genuine planar particle dynamics where a **global spatial symmetry** proves the proposed motion plane is invariant.

The new, bounded [`ring_motion_symmetry.py`](https://github.com/physicsvigilante/conductor_sim/blob/08ad6ea0a30d440f70f83f89e865a87fe9a0f96f/src/conductor_sim/ring_motion_symmetry.py) certifies each full ring independently:
- **Meridian:** plane contains ring centre and its true axis; plane normal orthogonal to ring axis.
- **Equatorial:** plane is ring's own circular plane through centre; plane normal parallel to ring axis.
- Centre location is checked against actual ring/world geometric representation and ulps, not expanded by arbitrary numerical `length_scale_m`.
- Full fixed-source inventory, initial position/velocity, optional gravity and every applied scheduled-E phase must maintain that same physical plane. A single initial local transverse-force cancellation is not a valid global certificate. M21c/M22c point/rod mirror symmetry remains separate and retained. Paired off-plane full-ring collective symmetry is **NOT** newly certified.
- Mixed new full 3D ring with old axis-only `UniformRingAxisField`/`UniformDiskAxisField` in time integration is explicitly refused instead of evaluating those old types outside their mathematical domain. Pure historical axis-only motion remains unchanged.
- Physics preserves full world-vector E/F and K+qV(+Ug). The existing runtime normal-force, nonrelativistic, energy and source-safety checks remain active. No fictitious particle guide or 3D projection of transverse force.

The new ideal-wire guard extension in [`prescribed_motion.py`](https://github.com/physicsvigilante/conductor_sim/blob/08ad6ea0a30d440f70f83f89e865a87fe9a0f96f/src/conductor_sim/prescribed_motion.py) reuses existing per-stage `UniformRingField.clearance_at(p)` (3D distance to the ideal circular charged wire, **not physical contact**). Additionally, for every tentative RK **chord** a conservative 1-Lipschitz lower bound `max(0, clearance(midpoint)-chord_length/2)` refuses/subdivides any chord insufficiently separated from a singular ring wire. Accepted steps must not leap over this geometric guard; tests distinguish source-guard censored trajectories from duration-complete integration and do not call the straight chord the true curved solution. No contact, rebound, absorption, charge transfer or guaranteed global ODE error bound is claimed.

The [shared M25a source geometry](https://github.com/physicsvigilante/conductor_sim/blob/08ad6ea0a30d440f70f83f89e865a87fe9a0f96f/src/conductor_sim/source_geometry.py) now displays the new full ring as a genuine 3D orthographic rim projection with source identities, axis and `motion_symmetry_mode` (meridian/equatorial), in already existing [event](https://github.com/physicsvigilante/conductor_sim/blob/08ad6ea0a30d440f70f83f89e865a87fe9a0f96f/src/conductor_sim/motion_event_viewer.py) and [driven](https://github.com/physicsvigilante/conductor_sim/blob/08ad6ea0a30d440f70f83f89e865a87fe9a0f96f/src/conductor_sim/driven_viewer.py) saved-state viewers. **Old M19b standalone prescribed viewer** explicitly refuses full-ring motion rather than omit/redraw its physical source. The existing M27a static E/V observer remains separately available. No browser ODE, inferred field line, new 3D engine, induced conductors or arbitrary force callback.

## Teaching cards and provenance

The actual workbook `02_conductors_half_size.pdf`, physical page 12 linked Q40–41, gives:
- Ring A +10 µC, Ring B -20 µC, both radius 0.30m, x-separated by 0.40m and both oriented along true world-x;
- prescribed uniform external +world-y E = 100,000 V/m.

The source's Q41 particle mass is symbolic, **not** a supplied numerical mass. [`examples/m27b_offaxis_motion.py`](https://github.com/physicsvigilante/conductor_sim/blob/08ad6ea0a30d440f70f83f89e865a87fe9a0f96f/examples/m27b_offaxis_motion.py) explicitly labels **teacher-hypothetical** numeric test probe charge +10µC, mass 0.01kg, start x=.2m, initial vx=.1m/s, duration .015s and plane world xy normal -z, so the genuine +y external E produces a curved real trajectory (not a fabricated 1D axial guide). The separate teacher `driven-switch` variation adds stationary-medium drag and an *additional* +y 20kV/m applied phase at .008s, while keeping the original source-given held +y E intact. Other development cases: meridian, equatorial, gravity, M26a structural source additions, events, rotation, surface guard.

The frozen [M27b initial charter](https://github.com/physicsvigilante/conductor_sim/blob/08ad6ea0a30d440f70f83f89e865a87fe9a0f96f/docs/m27b_charter.md) was committed at `7e4bff57079dd0285d4f9e53c0de6f79449827f3` BEFORE new source implementation. A separate [reserved two-ring card](https://github.com/physicsvigilante/conductor_sim/blob/08ad6ea0a30d440f70f83f89e865a87fe9a0f96f/docs/m27b_reserved_card.md) was committed at `013d20783c1aa3847ed9e36e8a51e784223f510f` BEFORE first reserved execution. It uses a novel noncoaxial two-ring configuration whose two distinct axes both lie in a common xz meridian plane; it includes held E and g. A separate test-only 512-element-per-ring direct Coulomb force and **700-step velocity-Verlet** compare with production vector RK4. This reserved transfer is developer-exposed, **NOT blinded** or independently authored by Chat B.

## Original failures preserved / correction history

1. Initial implementation `edbe1d2ea30e27e36ce3c80f4cea310d05e678b0` passed new M27b tests but earlier M27a test incorrectly still required **all** ring motion to refuse. [First focused failure 43755539988](https://github.com/physicsvigilante/conductor_sim/actions/runs/43755539988) and Python/visualization failures were NOT accepted. The old test was adapted to permit proven meridian motion and refuse truly oblique physical planes. A first negative-test setup erroneously checked an off-plane ring centre instead of only an oblique axis; corrected on `c76eb6f5`. Neither of these was a failed new production force relation.
2. [First reserved R1 execution 43755933184](https://github.com/physicsvigilante/conductor_sim/actions/runs/43755933184) at `c76eb6f5e7774b201b9ca115f1eb64aca8969392` PASSED BEFORE later browser harness fixes: full duration, final position max component difference **2.701705525964826e-11 m**, velocity max component difference **8.053874234192904e-11 m/s**, energy drift max **4.179516160561997e-20 J**. These are case-specific, not universal error guarantees. Final-head focused rerun is a **regression**, not a new first run.
3. [Browser first failure 43755933109](https://github.com/physicsvigilante/conductor_sim/actions/runs/43755933109) reached actual Chromium and loaded the first event viewer; the second viewer timed out. A follow-up [diagnostic run 43756841708](https://github.com/physicsvigilante/conductor_sim/actions/runs/43756841708) captured the real browser error: **`Identifier 'data' has already been declared`**, because the browser test used `page.set_content()` twice in the **same** Chromium page/global lexical JS realm. This is a **test harness isolation defect**, not production physics or viewer failure: both standalone viewers correctly define their own `const data`. The final `tools/check_m27b_browser.py` creates a *fresh Chromium page* per standalone viewer; its new real browser acceptance passed. The final visualization workflow runs this M27b step early (fail-fast). No numerical field law, integrator or production rendering was changed by these harness fixes.
4. **Final exact source head for review** `08ad6ea0a30d440f70f83f89e865a87fe9a0f96f` (tree `2affa61b9efd44f5949f5c6e8136f8ad179e893b`). All original incorrect first attempts remain retained in GitHub CI history and are not reclassified as successful first runs.

## Exact-final-head GitHub CI, independently checkable (not a Chat B verdict)

**18/18 applicable PR workflows PASS at exact head.**

| Gate | Exact CI proof |
| --- | --- |
| Python 3.10/3.12 | [run 43757091625](https://github.com/physicsvigilante/conductor_sim/actions/runs/43757091625), **1,807 passed, 97 real-FEMM-dependent skipped, 9 warnings on each** |
| Real FEMM 5 | [run 43757091501](https://github.com/physicsvigilante/conductor_sim/actions/runs/43757091501), **97 passed**, conductor-domain *nonregression*, not a ring-ODE reference |
| Focused new physics and reserved | [run 43757091565](https://github.com/physicsvigilante/conductor_sim/actions/runs/43757091565), **160 focused tests passed, 1 warning**; noncoaxial reserved **PASS**; event and driven Ring A/B teacher examples exported |
| Real offline Chromium and retained visual checks | [run 43757091497](https://github.com/physicsvigilante/conductor_sim/actions/runs/43757091497): **PASS**, both actual event and driven viewers, saved physical time, proper source geometry, path controls, real world xy motion, 390px responsive display, zero browser/page/network errors |
| Visual artifact | [artifact 14178987218](https://github.com/physicsvigilante/conductor_sim/actions/runs/43757091497/artifacts/14178987218), **GitHub-reported** ZIP digest `sha256:b66596099530c70348292a858426b35f295454734c7534aca71f81680a2fa033`. Not independently downloaded/rehashed by Chat A. |
| Focused/artifact | [artifact 14178333560](https://github.com/physicsvigilante/conductor_sim/actions/runs/43757091565/artifacts/14178333560), **GitHub-reported** digest `sha256:861a19c4d0351f60c9ad2d58186b994a042aa67138ea9599828712374a76e4de`. Not independently rehashed. |

The historical M27a source field itself was separately reviewed against high-precision off-axis E/V references. M27b's novel qualification and trajectory/guard correctness still requires independent R2 scrutiny; CI passing does not automatically certify the physical semantics. The 97 real-FEMM tests are **only conductor nonregression**.

## Reviewer tasks (adversarial, no predetermined verdict)

1. **Source physics and invariant-plane proof.** Examine `certify_ring_motion_plane`: for arbitrary 3D world ring orientation, do the meridian and equatorial criteria establish reflection invariance of each ring and of the complete forces? Challenge off-plane centres, near-oblique normals within tolerance, gravity, phase switches, mixing with legacy axis-only rings/discs, point/rod mirror pairs and rotation/translation covariance. No local cancellation or screen projection may be promoted to a global guarantee.
2. **Singular-wire and numerical step safety.** Examine the exact `_FixedDomain` clearance, new 1-Lipschitz lower bound on every accepted RK chord, stage checks, fallback halving, event monitor's substeps and termination semantics. Create novel near-miss/crossing configurations, especially a chord whose endpoints are safe but interior passes near ring wire. Can a computed trajectory cross an ideal wire guard undetected or mislabel a source-guard as a duration success? Distinguish safe numerical chord checks from proof of exact unsampled motion.
3. **Independent numerical dynamics.** Author at least one *fresh* noncoaxial/rotated/nonuniform source+launch arrangement if tooling permits. Independently evaluate ring E from direct circular Coulomb integration rather than production Carlson, and integrate with another method (or check energy/work with quadrature). Quantify actual position, velocity, full force, conserved K+qV+Ug or dissipated work/schedule switch error; do not call the developer's reserved R1 blinded. Distinguish native production execution vs a standalone transcription/integrator.
4. **Physical-data and presentation fidelity.** Inspect actual source geometry metadata, 3D rim projections, stable IDs, meridian/equatorial qualification, event/driven viewer playback from saved *physical-time* states, full force/energy, true upward world-y deflection in workbook case, and first browser failure/correction. Confirm the browser does NOT create a new ODE, fictitious guide or unsolved state. If possible use real Chromium; if not, describe which evidence was inspected.
5. **Unchanged/history boundaries.** Verify old M19b standalone path rejects new full-ring source, old axial-only source histories remain intact, no responding conductor or arbitrary 3D solver is introduced. Check actual model/source provenance (symbolic Q41 mass never silently assigned), teacher choices and scopes.
6. **Evidence authenticity and educational usefulness.** Inspect exact head/tree, job logs and (if possible) downloaded artifacts. Distinguish source interpretation, physical/numerical correctness, real executed simulation coverage, trustworthy visual evidence, teacher usefulness and optional textbook answer completeness, including known limits.

## Required output and release gate

Chat B authors its OWN NEW append-only report `physicsvigilante/review_sandbox/projects/conductor_sim/pr-63/reviews/review-01-chat-b.md` (or review-only PR), following the [template](../../../REVIEW-TEMPLATE.md). Preserve source code, initial frozen charter/card, first CI failures and reserved R1 first results; do NOT write a reported PASS on Chat A's behalf. State exactly reviewed SHA/tree, novel tests attempted, outcomes and unexecuted checks, and **PASS / CHANGES-REQUESTED / INSUFFICIENT-EVIDENCE** with concrete source references and severity. **Do not merge PR #63.** Even a PASS requires separate explicit owner merge approval. When complete, owner tells Chat A **"Review complete"**, and Chat A retrieves and triages the actual report.
