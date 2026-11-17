# Chat B — independent review: Opticsim PR #131 apparent-depth native feasibility

**Date:** 2026-11-17  
**Verdict:** **CLEARED FOR OWNER DECISION — research checkpoint only.**  
**Scope:** Exact, test-only feasibility source below. This does **not** approve a production apparent-image feature, a general observer model, merging PR #131, or lifting PR #129 / other held source, review or release gates.

## 1. Independently verified identity and evidence

| Item | Verified value |
| --- | --- |
| Reviewed PR | [opticsim #131](https://github.com/physicsvigilante/opticsim/pull/131), open, draft, unmerged |
| Production base | `d3509e82fb65d81aabe336666851f8f2962623f4` |
| Reviewed source HEAD | `aa36f2ce10f148e404d5534e4000f53adc62f9b5` |
| Reviewed source Git tree | `4203121ce123ad803ec8f41737e2a01ae6d7dd2f` |
| CI PR-merge checkout | `1d8a51c35f0213f34c4d6f7b02290eaa47aec5ab` |
| CI checkout Git tree | `4203121ce123ad803ec8f41737e2a01ae6d7dd2f` — **identical** to source tree |
| Only diff | Added `test/jee-apparent-depth-feasibility.test.mjs`, 298 lines, blob `0bf3a554b6dd9ec07a86ebe3acb2f5fb6a641ebf` |
| Native pin | PhyDemo `811f508d2b070898c241a568b0c167dcb8645251` |
| Native Node log | [run 44143858695 / job 134253547783](https://github.com/physicsvigilante/opticsim/actions/runs/44143858695/job/134253547783) |

I independently fetched the actual Git commit objects for the base, source HEAD and CI checkout, rather than accepting the PR description's identity claims. The HEAD has the stated base as its sole parent; the synthetic CI commit has the stated base and source HEAD as parents, and its tree is exactly the source HEAD tree. GitHub's base-to-head comparison reports exactly one addition (298 lines, zero deletions). No `src/`, solver, source pin, schema, existing test or UI diff is present. I read the complete [new test](https://github.com/physicsvigilante/opticsim/blob/aa36f2ce10f148e404d5534e4000f53adc62f9b5/test/jee-apparent-depth-feasibility.test.mjs) and relevant existing `src/observables.js`, `src/native-observations.js`, `src/planar-media.js`, `src/authoring.js`, and `scripts/author-scene.mjs` code at this exact ref.

I retrieved and parsed the **actual 305,182-character / 1,156-line native job log**. It shows Node **v24.19.0**, checkout `1d8a51c...`, pinned PhyDemo build, **801 tests, 801 passed, zero failed/skipped/cancelled**, and the logged native `[apparent-depth-feasibility]` executions and derived results (88 structured log entries, including the eleven new passing tests). I also independently queried **all eleven** linked workflow-run records: all have source HEAD `aa36f2c...`, `run_attempt=1`, `completed/success`. The [optical composition run 44143858494](https://github.com/physicsvigilante/opticsim/actions/runs/44143858494) and [planar refraction run 44143858909](https://github.com/physicsvigilante/opticsim/actions/runs/44143858909) have successful existing native/browser regression job steps, including preinstalled Chrome. **These are existing regression checks, not an apparent-depth browser feature.**

**Execution limits:** I did **not** independently run PhyDemo, Node24 tests, or Chrome. I independently recomputed the geometry using Snell's law and separately re-intersected the detector hit coordinates/directions retrieved from the real native log. The 11 successful CI workflows are builder-run CI, not 11 independent physics reviews.

## 2. Physics and geometry — independent checks

The default logged fixture has one canonical v5 single-ray source at `(-120,0)` mm, one native plane at `x=0`, an observer-side finite detector at `x=100` mm, object index `n_o=1.5`, observer-side index `n_v=1`, and **full Fresnel partial reflection**. Each of the two separate executions uses the same source position/apparatus/numerical policy, changing only the explicitly authored source direction. Native evidence for the ±30° cases reports one emission, one interface encounter, **one transmitted and one reflected branch**, one actual detector hit, no native warnings, no truncation and no undefined behavior. The recorded transmitted direction `(0.6614378277661478, ±0.75)` agrees with Snell refraction `sin(t)=1.5 sin(30°)=0.75`; detector hits are `(100, ±182.6713742055232)` mm. The hit direction matches the measured native transmitted branch.

For an incident angle `i` from the normal, Snell's law gives `t=asin((n_o/n_v)sin(i))`. The plane crossing is `(0,120 tan(i))`. Its **outgoing native line**, after independently verified refraction, has equation `y=120 tan(i)+x tan(t)`. The backward intersection of a symmetric ±i pair is therefore at `x=-120 tan(i)/tan(t)`, `y=0`; the normal depth is `d_pair=120 tan(i)/tan(t)`. The **conditional limit** as `i→0` is `120(n_v/n_o)=80` mm. This is a paraxial estimate, **not** a 30° image-depth rule or an engine-generated image.

| Signed incident pair | Independent Snell calculation, mm | Independent intersection of logged native detector lines, mm |
| --- | ---: | ---: |
| ±5° | 79.61636684775050 | 79.61636684775047 |
| ±1° | 79.98476458468085 | 79.98476458468129 |
| ±0.1° | 79.99984769083582 | 79.99984769083608 |
| ±30° | 61.10100926607787 | 61.10100926607784 |

These data establish the expected angle dependence, not a single stigmatic image. For two **different positive** angles `a,b`, independently solving the outgoing line equations gives `x=120(tan(b)-tan(a))/(tan(t_a)-tan(t_b))` and `y=120 tan(a)+x tan(t_a)`. Calculating from the native hit lines yields: 20°/21° `(-59.963563260395205, 7.837454133628043)` mm; 21°/22° `(-57.87945477846891, 9.166054470073817)` mm; 20°/22° `(-58.89610066658312, 8.475454313109111)` mm. The first two are **2.4715758168506468 mm apart**. The test correctly logs that no **unique image** follows. Note that the `singleImage: unavailable` message here is a **test-local assertion/log**, not a general multi-ray image API.

The observed reverse-side and rotated/translated controls are consistent with the normal/tangent geometry. Equal indices produce 120 mm, not an artificial virtual displacement. The native 1→1.5 case at ±10° produces **181.54790462647537 mm**; independent Snell calculation agrees. Changing detector distance from 50 to 150 mm changes actual hit coordinates, not the backward intersection. The transmitted-only control retains native `qualified` readings and an explicit Fresnel-omission warning.

At ±50° (critical angle `asin(1/1.5)≈41.81031489578°`) native output reports TIR, **zero transmitted detector hits** and an unavailable intersection. A detector deliberately too short for ±30° shows actual transmission but **zero crossings**; again no intersection is invented. At critical ±0.00001° offsets, the below-critical case transmits with a near-grazing outgoing direction and an intersection about **0.0670513 mm** from the interface; above-critical reports TIR. This does **not** validate exact-critical or grazing robustness. Native near-parallel ±0.000001° paths complete but the postprocessor withholds the intersection. Setting **`simulation.maxRayDepth=0`** (the test label “depth-zero”) produces incomplete native runs and null/suppressed observations; this is **not** a geometric zero-object-depth test. The tests also explicitly decline single/duplicate directions, stale/missing hash-bound capture, incompatible experiment families and a second boundary.

## 3. Ranked review findings

### P1 — Production design requirements, not blockers to this test-only experiment

**P1-A. Native qualification is not propagated into the derived geometry status.** In [test lines 87–141](https://github.com/physicsvigilante/opticsim/blob/aa36f2ce10f148e404d5534e4000f53adc62f9b5/test/jee-apparent-depth-feasibility.test.mjs#L87-L141), `usable` accepts both `available` and `qualified` native detector readings; then `backprojectPair` can return `status:'available'` **without the input warnings**. This occurs in the logged `partialReflection:false` test: both native hit readings are `qualified` with the transmitted-only/Fresnel-omission warning, but the derived result says `available`. Current [observable qualification](https://github.com/physicsvigilante/opticsim/blob/aa36f2ce10f148e404d5534e4000f53adc62f9b5/src/observables.js#L71-L93) and [hit-event results](https://github.com/physicsvigilante/opticsim/blob/aa36f2ce10f148e404d5534e4000f53adc62f9b5/src/observables.js#L142-L154) correctly carry hash eligibility and warnings; the local postprocessor does not. **Required before any production reuse:** versioned derived-result contract that preserves *each* source observable's status, warning, run/scene identity and native-vs-derived method, with no unconditional promotion from `qualified` to `available`. No retroactive production qualification is implied by this test.

**P1-B. There is no specified observer or finite-pupil selection.** Two separate single-ray scenes with a common source and apparatus do not demonstrate two actual rays entering the **same eye/pupil**; a finite detector records crossings, not visibility or accommodation. The backward intersection is a valid **pairwise 2D geometric construction**, but its depth is conditional on the selected directions. The next bounded design must either explicitly admit only a *conditional paraxial analytical estimate*, or define a physical observer/detector aperture and ray-selection/visibility rules before asserting an observer-dependent virtual location. It must never convert the construction into a native propagated ray or claim a real image.

### P2 — Evidence and numerical generalization limits

**P2-A. Conditioning thresholds are heuristics, not an error budget.** `MIN_LINE_SINE=1e-6` and `LINE_RESIDUAL_MM=1e-6` (test lines 83–86, 123–136) are transparent research filters. The two-line reconstruction divides by the cross product of outgoing directions, so small angular separation, **near-antiparallel near-grazing directions**, uncertain hit coordinates/directions and very large translated coordinates can amplify error. A tiny two-line residual only tests self-consistency of the *same input lines*; it cannot certify optical accuracy, native angular resolution or any physical-image position. Validate perturbation sensitivity, numerical scale, forward geometry and a documented validity envelope before using this to answer JEE questions.

**P2-B. The experiment does not prove general ray lineage or pairing.** Its exclusivity checks (one S1, one I1, one D1, one emitted ray, one interaction, one detector hit, hit direction matching the transmitted branch) are persuasive for **these isolated fixtures**. The existing detector-hit event explicitly has no source/ray ID or complete optical path; the test does not prove that multiple sources, multiple reflections, merged branches or two detector hits can be attributed or paired reliably. Extend only through a separately reviewed provenance/association design; do not assume the native hit list's order or pair runs from unrelated scenes.

**P2-C. Nonconcurrence and refusal remain bounded harness assertions.** The three-oblique-ray spread is explicitly tested, but no generic native/user-facing `uniqueImage` evaluator exists. Refusals are deliberately local to exactly one plane and one path per run. Multiple planes/slabs, curved optics, 3D, exact critical incidence, finite pupil and general textbook-problem coverage still need separate feasibility; the test must not be cited as proof of any of them.

### P3 — Minor documentation clarity

**P3-A.** Describe the “depth-zero” suppression control as **ray-depth-budget zero** (`maxRayDepth=0`), not an object placed at the interface. Keep the test-local terms “backprojection available” and “no unique image” visually distinct from any future engine-native result. This clarification is worthwhile but need not modify the frozen research source.

## 4. Conclusion and next bounded step

**CLEARED FOR OWNER DECISION, exclusively as the completed native feasibility research checkpoint.** Exact source/CI tree identity, a sole test-file addition, raw native detector/branch evidence, independently recomputed Snell geometry, finite-angle nonconcurrence, important refusal controls and successful existing CI support that narrow finding. There is **no newly released image/observer API or apparent-depth browser feature** and there has been **no independent native/Chrome replay by this reviewer**.

A sensible next independently reviewed **design-only** step is a bounded v1 one-planar-interface observer/apparent-depth contract: define an explicit observer-aperture or documented conditional paraxial mode, input/path eligibility and cross-run provenance, native-measurement vs derived-geometry status/warning propagation, a numerical conditioning/uncertainty policy, and hard refusals for nonconcurrent or unsupported arrangements. Retain a future separate implementation, native/browser verification and owner release gate. **Do not merge or change PR #131, #129, any other held Opticsim PR, or production main on this review's authority.**

**Reviewer independence declaration:** Evaluated the prompt, request, actual source, Git object/tree identity, actual CI log and native event records, independent trigonometry and detector-line recomputation; no modifications to Opticsim, no dependency installation, no independent native/Chrome execution.
