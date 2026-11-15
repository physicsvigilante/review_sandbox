# conductor_sim PR #61 — M26a R2 independent review request

**Status: awaiting separate Chat B review; source PR remains DRAFT and UNMERGED.** This document is authored by Chat A (implementer), not a reviewer verdict.

| Pin | Immutable value |
|---|---|
| projectId | `conductor_sim` |
| sourceRepo | [physicsvigilante/conductor_sim](https://github.com/physicsvigilante/conductor_sim) |
| sourcePR | [Draft PR #61](https://github.com/physicsvigilante/conductor_sim/pull/61) |
| baseSha | `c5cc9bf818f1c8d83901bcadef745cc29f6d1675` (verified M25a main) |
| **headSha to review** | **`e0ea76e80aca4b05cea7f16a12549c13670108d2`** |
| **head sourceTreeSha** | **`98b5b18fe3dedb6e0d3fb744c3732e812bb188fc`** |
| riskClass | **R2**: new structural admission of physical models and provenance across M22a/M24b, even though existing physical laws and integrators do not change |
| reviewScope | Cross-layer source/force qualification; stable identities and ancestry; numerical-reference and browser-evidence integrity; refusal preservation |
| reportDestination | **`projects/conductor_sim/pr-61/reviews/review-01-chat-b.md`**, authored by Chat B only |

Read the [central review protocol](../../../PROTOCOL.md), [risk policy](../../../REVIEW-RISK-POLICY.md), [review report template](../../../REVIEW-TEMPLATE.md), and [source composability contract pinned at head](https://github.com/physicsvigilante/conductor_sim/blob/e0ea76e80aca4b05cea7f16a12549c13670108d2/docs/composability_contract.md). Inspect any source-repo AGENTS.md guidance if present; do not assume one exists.

## Physical/architectural question

M22a already atomically adds/removes/replaces built-in nonresponding held electrostatic sources and optional uniform gravity in an immutable `PrescribedScenario`. M24b already composes that scenario with stationary-medium linear drag and piecewise-constant externally prescribed E, and validates **every** scheduled phase. But the author lacked a stable-identity *structural* revision API for an existing retained `DrivenModel` without disguising source additions as property patches.

M26a adds **only** `src/conductor_sim/driven_reassembly.py`, a typed opt-in `reassemble_driven_model` bridge and immutable `DrivenReassembly` audit record. It delegates source/whole-system qualification to M22a, then builds an ordinary new M24b `DrivenModel` to check all applied phases. The exact old drag and schedule objects are retained, as are actual base and driven parent models, source provenance and the supplied structural chain. Child origins are teacher hypotheticals, not source-given facts. Analysis planes, initial physical state, medium, numerical settings, source laws and event questions do not change implicitly.

Seven PR files: one added production module, one added physics/refusal test module, one added example, one added actual-Chromium checker, two added docs (including the frozen acceptance charter), and **one narrow step added to the existing visualization workflow**. No existing production force law, integrator, source geometry or viewer file is modified. [PR source diff](https://github.com/physicsvigilante/conductor_sim/pull/61/files) · [exact head tree](https://github.com/physicsvigilante/conductor_sim/tree/e0ea76e80aca4b05cea7f16a12549c13670108d2).

Preimplementation charter committed **before implementation** at [`d1d6a254`](https://github.com/physicsvigilante/conductor_sim/commit/d1d6a25489de4ed3f6f43ac18491f0f19d089183). See [M26a charter](https://github.com/physicsvigilante/conductor_sim/blob/e0ea76e80aca4b05cea7f16a12549c13670108d2/docs/m26a_charter.md), [technical docs](https://github.com/physicsvigilante/conductor_sim/blob/e0ea76e80aca4b05cea7f16a12549c13670108d2/docs/m26a.md) and [new tests](https://github.com/physicsvigilante/conductor_sim/blob/e0ea76e80aca4b05cea7f16a12549c13670108d2/tests/test_m26a_driven_reassembly.py).

## Current exact-head CI evidence (Chat A observed, not independent Chat B results)

**All 16/16 applicable PR workflows successfully completed** at exact head `e0ea76e80aca4b05cea7f16a12549c13670108d2`.

| Gate | Verified GitHub evidence |
|---|---|
| Python 3.10/3.12 | [run 43733873897](https://github.com/physicsvigilante/conductor_sim/actions/runs/43733873897), **1,742 passed, 97 real-FEMM-dependent skipped, 8 warnings on each** Python version. No failures. A second Python PR workflow [43733869007](https://github.com/physicsvigilante/conductor_sim/actions/runs/43733869007) also succeeded. |
| Real FEMM | [run 43733873703](https://github.com/physicsvigilante/conductor_sim/actions/runs/43733873703), **97 passed**, no skips. This is conductor **nonregression**, not numerical verification of the M26a prescribed-field composition. |
| Visualization and real Chromium | [run 43733873904](https://github.com/physicsvigilante/conductor_sim/actions/runs/43733873904), success; existing visual checks and new step **"M26a structural driven source Chromium acceptance"** passed. |
| New source/browser artifact | [artifact 14169552582](https://github.com/physicsvigilante/conductor_sim/actions/runs/43733873904/artifacts/14169552582). GitHub reports ZIP digest `sha256:a8796276d7fb2564d5a8f434868712c46f448ae2311f841db3397be886510599`. **This digest is provider metadata; Chat A did not independently rehash the downloaded ZIP.** The uploaded artifact contains the new saved HTML/JSON and wide/mobile screenshots in `m26a/`, plus retained visualization evidence. |

The 23 new tests and public example are developer-authored. Their independent Coulomb, Gauss-sphere, axial-ring, mirror-symmetry and qE/m-plus-gravity/drag expressions are external calculations coded into tests, **not a blinded independent-LLM test** or an independently reintegrated numerical trajectory. Browser checks verify saved time, true source identity, switch state, offline behavior and viewport, not alternative physics.

### Failure history preserved, not retroactively relabelled

- Initial source [`f8eea589`](https://github.com/physicsvigilante/conductor_sim/commit/f8eea58921a6fbd2ff8f0e7939eef05635a19281) and later [`ffd60d90`](https://github.com/physicsvigilante/conductor_sim/commit/ffd60d90b6d6aa5b9b8bc8c10a60deee90e2a326) were **not passing final candidates**. [Python failure 43733209183](https://github.com/physicsvigilante/conductor_sim/actions/runs/43733209183) and [visualization failure 43733266105](https://github.com/physicsvigilante/conductor_sim/actions/runs/43733266105) are retained.
- The new P3 independent test erroneously treated the applied electric field in V/m as acceleration in m/s²; the physically correct contribution is **qE/m**, added to gravity. The simulation already produced the q/m-consistent velocity. This incorrect *test reference* was corrected at [`78d64c04`](https://github.com/physicsvigilante/conductor_sim/commit/78d64c04f6c71da500c7128579e82b6e34d7953d), with no solver/formula change.
- A separate negative-test harness incorrectly constructed a different parent with new drag/schedule objects, so it failed at the earlier object-preservation guard rather than testing forged ancestry; [`ffd60d90`](https://github.com/physicsvigilante/conductor_sim/commit/ffd60d90b6d6aa5b9b8bc8c10a60deee90e2a326) corrected that fixture.
- Final [`e0ea76e8`](https://github.com/physicsvigilante/conductor_sim/commit/e0ea76e80aca4b05cea7f16a12549c13670108d2) added the separately checked real Chromium example/workflow. Neither early failure is claimed as a physical-engine regression or a successful first run.

## Adversarial reviewer tasks (no predetermined verdict)

1. Inspect new `DrivenReassembly` and the reused M22a/M24b validators at **pinned SHAs**. Can an invalid source inventory, off-plane mirror asymmetry, axial ring with a later transverse scheduled phase, invalid drag or unqualified gravity reach `investigate_driven_motion` without full requalification? Can the source-only structural operation silently modify initial conditions, particle, medium, clock or work policy?
2. Challenge stable identities: duplicate/colliding source or driven IDs, retired-ID reuse across 2+ structural generations, forged parent, edited source labels, source replacement of the same physical ID, identity alias with the scheduled-field/drag roles. Are exact ancestry and hashes merely author records (as documented), rather than misleading trust claims? Consider clone/equal-value but distinct-object cases and constructor tampering.
3. Independently check at least one **novel qualifying** source+schedule+drag physical input, ideally rederive its qE + mg − b v and work balance without using production's reference calculation. Use a different integration method if feasible, and distinguish numerical run completion from a source guard or unresolved event. Inspect the historical correction to qE/m.
4. Examine actual HTML/JSON Chromium evidence and, if possible, replay `python -m tools.check_m26a_browser --output ...`. Verify that browser UI uses retained saved physical time/geometry, does not solve fields/events in JavaScript, and source omission does not remove the physical field.
5. Verify unchanged historical APIs/data contracts, 97 real-FEMM nonregressions, and that source-given vs teacher-hypothetical provenance and no-impulse schedule semantics remain physically honest.
6. Separately assess teacher-facing usefulness/coverage and open gaps. Do not treat a passing curated trial as unbiased JEE coverage.

Known limits: only M22a built-in nonresponding prescribed sources plus supported optional gravity; linear drag in stationary medium; M24b piecewise spatially uniform applied fields. No induction, conductor source-response, off-axis ring E/V, free 3D particle motion, mechanical collisions, Maxwell switching fields, generic scene graph, arbitrary callbacks, PDF ingestion or authenticated trusted imports.

**Required output:** Chat B authors a new report at `projects/conductor_sim/pr-61/reviews/review-01-chat-b.md` under **physicsvigilante/review_sandbox**, directly or via review-only PR, using the central template. State pass / changes-requested / insufficient-evidence, observed vs unexecuted checks, exact SHA, any concrete findings and smallest correction. **Do not modify source PR or merge it.** Chat A will fetch and triage the report after the owner says "Review complete"; merge needs separate explicit owner approval.