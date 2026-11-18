# Independent R1 review request — Opticsim PR #145, observer-anchored native refraction feasibility

**RESEARCH ONLY — DO NOT MERGE.** This is a **test-only** study on production main, not a released observer, inverse tracer, image detector, or modification to reviewed PR #144. Independent physical and evidence scrutiny is required before designing the next authorable JEE engine capability.

## Source identity and build provenance (verify independently)

- [Draft PR #145](https://github.com/physicsvigilante/opticsim/pull/145), true production base `d3509e82fb65d81aabe336666851f8f2962623f4`.
- HEAD `a2d0adfe692bc837656a4dd09edc84ab4f490d2f`, Git TREE `c9333564591b165c22246f67fbc4fa47c5462d11`.
- GitHub Actions synthetic merge `e1a2f163efd1d121912c84c71a874cb878914930`; independently check that its Git tree is **exactly identical** to source and parents are [production main, exact research HEAD].
- Only added files: `test/jee-observer-native-feasibility.test.mjs` and `docs/JEE-OBSERVER-REFRACTION-NATIVE-RESEARCH.md`. **No** production engine, PhyDemo, canonical scene schema, adapter or browser changed. PRs #141, #143 and #144 remain frozen/reviewed but unreleased; this study is not stacked on them.

## What question this tests

The reviewed [PR #143](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-143/reviews/review-01-chat-b.md) native apparent-depth study and [PR #144](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-144/reviews/review-01-chat-b.md) typed analytical module require an author-specified **incident angle**. A JEE teaching problem may instead give the **source and observer positions** on opposite sides of a plane refracting interface. This tests the narrower feasibility of obtaining a physically consistent incident direction from those declared coordinates and verifying that a **single native ray** really reaches an observer-side detector.

The test-only oracle computes the stationary optical path **outside PhyDemo**, using an explicit source `S`, observer point `O`, oriented infinite plane point `P`, source-to-observer unit normal `n`, its CCW tangent `t`, source and observer normal distances `d_s,d_o>0`, source/observer tangent offsets `u_s,u_o`, and stated homogeneous refractive indices `n_s,n_o`. It numerically brackets `q` between `u_s` and `u_o` and solves by bisection:

`n_s (q-u_s)/sqrt[d_s²+(q-u_s)²] = n_o (u_o-q)/sqrt[d_o²+(u_o-q)²]`.

The derivative difference is strictly increasing when the normal distances are strictly positive, giving one stationary crossing `Q=P+q*t` for this **one ideal infinite interface and fixed endpoints**. The oracle then **explicitly authors** the single source initial heading from `S` to that reference `Q`. This is **not native discovery of a missing source angle** and does not force a native ray itinerary; the unmodified pinned PhyDemo `SingleRay` / `PlaneGlass` / `Detector` independently propagates that real declared ray.

A finite detector centered exactly at the given `O` is aligned parallel to the interface and wholly within the observer medium. It is a sampled arrival witness, **not a real eye or image detector**. Native result qualification is via existing `evaluateDocument` + `evaluateObservables`, with fresh canonical SHA, native `completed`, one emission, one native interface transmission, exactly one native detector hit, actual outgoing direction, complete count-matched hit list, explicit Fresnel-off warning, and method labels.

There is no native planar interface `pointMm` field here. A crossing inferred by mathematically back-extending an observed detector ray to the plane is **derived**, not a recorded native incident coordinate, and the test documents that limitation.

## Builder CI and concrete data (verify logs, do not assume)

- **11/11 standard workflows SUCCESS** at exact research HEAD; [optical composition run #44282456676](https://github.com/physicsvigilante/opticsim/actions/runs/44282456676) and [planar-angular run #44282456397](https://github.com/physicsvigilante/opticsim/actions/runs/44282456397).
- **797/797 Node tests** passed on exact-head Git tree including all seven research-only tests; pinned native adapter and browser checks use builder CI.
- Named log `JEE_OBSERVER_NATIVE_ARRIVAL`: source `(-60,0) mm`, plane `x=0` normal +x, `n_s=1.5`, `n_o=1`, observer/detector `(100,40) mm`; independent root/reference crossing `Q=(0,11.246155771209231)`, source heading/incidence `10.616108941304955°`, native refracted angle `16.041977708350927°`. Actual native detector hit `(100.00000000000001,40) mm`, conditional apparent depth `39.111833818549506 mm`, `nativeImageDetected:false`.
- Positive/negative observer offsets ±40 mm, indices 1→1, 1→1.5 and 1.5→1, rotated 90°/180°, translated laterally-offset scene, true axial hit without unique virtual-depth inference, wrong-side/near-interface rejection, deliberately stale scene and maxRayDepth0 incomplete suppression all pass their named tests.
- All Node/PhyDemo/Chrome executions remain **builder CI**, not reviewer-independent native execution.

## Reviewer questions

1. Independently rederive the stationary optical path equation, uniqueness in this narrow geometry, sign conventions, 2D rotation invariance and numerical bisection stability. Are exactly opposite medium-side conditions and source-position inputs enforced by the **test reference**? Does this support a narrowly scoped later typed source-observer query?
2. Recompute the example independently using physical Snell's law; verify source heading, refracted direction, observer hit, and apparent-axis depth. Inspect the code for mistakenly using a scripted crossing as native evidence.
3. Inspect actual native observation fields, status/warnings/hashes, detector endpoint clearance, reverse-index/normal orientations and incomplete/stale withholding; check if tests overclaim direct interface hit measurement, ray ancestry or human perception. Source identity is safe only for this one-source/one-ray fixture, not arbitrary optical systems.
4. Check edge cases: observer/source same tangent (axial indeterminacy), observer at nearly tangent view and near-critical, very small source/observer distance, inadmissible sides/indices, numerical cancellation and nonfinite geometry. Distinguish missing **research test coverage** from an actual physics defect in the stated bounded experiment.
5. Verify Git trees, actual CI run logs, exact source scope, and absence of modifications to production or the held reviewed branches. Assign P0/P1 and concrete nonblockers; propose the next bounded typed contract without suggesting that the native solver itself solved an inverse problem.

Publish `projects/opticsim/pr-145/reviews/review-01-chat-b.md` with exact source SHA/tree, independent reasoning, evidence limits and one verdict **CLEARED FOR NEXT SCOPED DEVELOPMENT / CHANGES REQUESTED / INSUFFICIENT EVIDENCE**. Do not modify source, merge, authorize release, or silently inherit approval from #143/#144. Branch protection issue #123 and separate owner merge decisions remain outstanding.
