# M31a PR #71 — targeted independent R2 re-review 03, residual F-01-R

**Source candidate is ready for a NARROW, separate-context independent review. The two prior CHANGES-REQUESTED reports remain valid at their original pins. This is a developer-authored packet, NOT independent PASS and NOT merge authorization.**

Read [review-01](reviews/review-01-chat-b.md), [review-02](reviews/review-02-chat-b.md), [original REQUEST](REQUEST.md), [central PROTOCOL](../../../PROTOCOL.md), [R2 policy](../../../REVIEW-RISK-POLICY.md), [report template](../../../REVIEW-TEMPLATE.md), and exact-source [frozen M31a charter](https://github.com/physicsvigilante/conductor_sim/blob/7095341fcec78fd78aa4fe784e5820ec22dee059/docs/m31a_charter.md).

**Source PR:** https://github.com/physicsvigilante/conductor_sim/pull/71  
**New exact SOURCE HEAD:** **7095341fcec78fd78aa4fe784e5820ec22dee059**  
**Actual source Git TREE:** **c1b1ca2eccd8a18d9f28e3dbc5a1a67cee60af2c**  
**Base/main:** **293d4b22a6eeb4bc56a5598d8b6935ef91f19826** (released M30b, post-merge green).
**Original reviewer #01 source pin:** e8970e26b91f6f8dfe3bd8bffcaf8f181449870b (review-01 CHANGES-REQUESTED).
**Original reviewer #02 source pin:** c190e0929e727d35db2337efc366cf9676fc36f3, tree df48e1eb10536285818abfafd3f0628436247882 (review-02 CHANGES-REQUESTED).

Verify live source PR HEAD, actual Git tree and remaining draft/unmerged status before reviewing. If the source head has moved, mark this request stale rather than inspecting floating main.

## Narrow blocker to close

Independent review #01 challenged forged nonnative TestChargeMotionResult-like objects, unknown termination, and invented saved-time comparisons. The first correction at c190e092 addressed those cases, but independent review #02 found a residual **F-01-R**: Python considers False == 0.0, so an altered in-memory comparison row could replace an SI timestamp 0.0 with Boolean False while ordinary dict equality still succeeded; detached JSON then emitted false rather than the real numeric 0.0. A custom numeric/dict equality subclass was another bypass. **No physical-law or genuine numerical-trajectory defect was identified.**

Two bounded commits after review #02 correct only this typed comparison-evidence issue:

1. **ab0ee397ace59958fb1ff0f8bac728938bed2f9e** — source src/conductor_sim/coupled_physical_family.py introduces type-faithful recursive comparison of actual native M28a _shared_rows results. Exact built-in dict / tuple / str / int / float types are required. Floats must be finite and have identical float.hex() representations, so Boolean 0.0, overridden equality on float/dict subclasses, altered nested vector values, and +0.0 versus -0.0 cannot pass merely because Python ordinary equality says they are equal. CoupledPhysicalRun remains the result validation boundary and repeats validation before JSON export. Three new adversarial/positive-control tests and a documentation clarification are added. Original field, force, M22a/M20b model qualification, RK and _shared_rows algorithm are unchanged.
2. **7095341fcec78fd78aa4fe784e5820ec22dee059** — corrects ONLY a new positive-control test, whose first version erroneously compared native in-memory 3-vector tuples with the JSON-exported arrays. The test now compares normalized JSON representations. Preserve the intermediate failed run at ab0ee397 as a **test expectation failure**, not a first-run PASS; no solver implementation was changed by this second commit.

[Exact review-02 pin → current corrected HEAD diff](https://github.com/physicsvigilante/conductor_sim/compare/c190e0929e727d35db2337efc366cf9676fc36f3...7095341fcec78fd78aa4fe784e5820ec22dee059)

## Independently challenge the correction

1. **Reproduce the built-in Boolean bypass:** create one genuine CoupledPhysicalRun from a valid M31a plan, substitute False for the original first comparison time_s 0.0 in a dataclasses.replace entry, and check that new CoupledPhysicalRun construction rejects it. Repeat by mutating the already constructed tuple-held dict and then calling as_dict; it must reject before detached JSON export. Numeric 0.0 remains admitted and exports as JSON number, not false.
2. **Adversarial object equality:** a float subclass with __eq__ returning True and actual 9999.0, or a dict subclass overriding __eq__, must be refused even though ordinary Python dict/tuple equality might report a match. Try a fake -0.0 for a native +0.0 sample, altered nested delta-position component, missing/extra keys, or nonfinite float; reject non-native comparison evidence while keeping true native rows valid.
3. **Native controls:** original full M31a paired/atomic physical revision still emits a complete genuine trajectory with correct two-stage SHA and exact literal-time deltas. A real source-guard run retains source-guard and censored status with true last SI sample, and the jointly translated held point + probe remains physically admitted. Do not silently reject legitimate M28a _shared_rows tuples, or replace source-authored values with another field law.
4. **Trust-boundary scope:** these checks authenticate public typed-result evidence within normal built-in Python value semantics, not cryptographic protection against deliberate modification of every internal native object. Verify no physics law, physical constraints, numerical integration or historical model identity was changed; old reviewer #01's independent SI numerical physics remains valid only for its original source pin.
5. **CI / provenance:** verify CURRENT exact source HEAD and tree, 16/16 exact-head completed successful workflows, direct push head versus PR synthetic merge checkout, real FEMM regression, historical Chromium and new test outcomes. Do not confuse developer CI with independent reviewer execution.

## Current exact-head CI evidence (developer, not independent PASS)

**16/16 complete GitHub workflow successes at 7095341fcec78fd78aa4fe784e5820ec22dee059:**

- [Python 3.10 / 3.12 PR workflow #43932507098](https://github.com/physicsvigilante/conductor_sim/actions/runs/43932507098): **1,894 passed, 97 FEMM-only skipped, 16 warnings on each interpreter**, including three new F-01-R tests and the retained five F-01 tests.
- [Direct source push Python workflow #43932498089](https://github.com/physicsvigilante/conductor_sim/actions/runs/43932498089): independently completed success, same 1,894 passing per interpreter.
- [Real FEMM 5 #43932506967](https://github.com/physicsvigilante/conductor_sim/actions/runs/43932506967): SUCCESS, historical 97 physical conductor regressions (not an M31a source/property numerical reference).
- [Historical Chromium/visualization #43932507015](https://github.com/physicsvigilante/conductor_sim/actions/runs/43932507015): SUCCESS; M31a has no new HTML. [Historical visualization artifact #14259896926](https://github.com/physicsvigilante/conductor_sim/actions/runs/43932507015/artifacts/14259896926) provider-reported ZIP SHA-256 **eec2ac87a00f62e8f8433c568a2db0d1b579806bdb98abb3e80bc8a606c84816**, NOT independently downloaded/rehashed by developer.

Prior novel tilted rod/signed points/gravity atomic source-charge + probe-mass transfer and independent DOP853 physical references were produced for original M31a source head e8970e26. This remains historical scientific evidence, NOT an assertion that the unchanged physical cases were independently rerun after the evidence-validator-only changes. The current-head full Python/FEMM/Chromium suite was separately rerun and passed.

## Required new independent report

Write an independently authored NEW report, preserving both earlier reviews, to **physicsvigilante/review_sandbox/main** at:

**projects/conductor_sim/pr-71/reviews/review-03-chat-b.md**

Include exact source SHA/tree, which adversarial probes you executed versus inspected, source paths and explanations, authentic native guard/translation controls, concise original F-01 and F-01-R closure judgment, and explicit **PASS / CHANGES-REQUESTED / INSUFFICIENT-EVIDENCE**, with any remaining blockers. Do not claim unperformed source execution. A separate ChatGPT context is not independent human expert certification or necessarily different underlying model weights.

**Do NOT modify, mark ready, approve or merge production PR #71.** Owner standing authorization permits an expected-HEAD merge only after a fresh independently authored PASS with no blockers, still-green exact HEAD CI and release verification on main. Any new blocker requires another *targeted* correction/re-review; preserve all earlier negative results.
