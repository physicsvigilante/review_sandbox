# Independent review request — Opticsim PR #131

**Research-only checkpoint, not a production release. Independent review is PENDING.**

## Exact subject and preservation

- [Draft PR #131](https://github.com/physicsvigilante/opticsim/pull/131), implementing the first native feasibility checkpoint of [issue #130](https://github.com/physicsvigilante/opticsim/issues/130).
- Source HEAD: `aa36f2ce10f148e404d5534e4000f53adc62f9b5`.
- Source Git tree: `4203121ce123ad803ec8f41737e2a01ae6d7dd2f`.
- Actual production base: `d3509e82fb65d81aabe336666851f8f2962623f4`.
- Synthetic CI checkout: `1d8a51c35f0213f34c4d6f7b02290eaa47aec5ab`; the builder compared Git commit objects and verified the identical tree `4203121ce123ad803ec8f41737e2a01ae6d7dd2f`.
- One added file only: [`test/jee-apparent-depth-feasibility.test.mjs`](https://github.com/physicsvigilante/opticsim/blob/aa36f2ce10f148e404d5534e4000f53adc62f9b5/test/jee-apparent-depth-feasibility.test.mjs), 298 lines; blob `0bf3a554b6dd9ec07a86ebe3acb2f5fb6a641ebf`.
- Pinned PhyDemo: `811f508d2b070898c241a568b0c167dcb8645251`.

There are no changes to production `src/`, schema, native solver, UI, observation instrumentation, existing tests or historical evidence. The actual base is main; no temporary retarget was required. This line is independent of held v14–v19 PRs. Do not merge, deploy, change existing source branches, or treat this review as clearance of #129 or any other PR.

## What the experiment actually does

Each existing canonical v5 scene contains one explicitly directed single-ray point source, one native planar interface and one passive finite detector. Paired executions have the same apparatus, source position, indices and numerical settings, differing only in authored source direction. The default fixtures retain full Fresnel partial reflection. The existing `evaluateDocument` native execution and `detector-hit-events` readout provide actual hit positions and incoming unit directions. No analytical refraction or reconstructed segment is supplied to PhyDemo.

A test-local helper checks scope, family consistency, distinct authored direction, complete native execution, current scene-hash-bound observable eligibility, one emitted ray, one interface interaction, one detector hit, and agreement with the actual transmitted branch. Only then does it intersect the two outgoing supporting lines backward using cross products. It checks finite residuals and a backward/object-side intersection.

This is **two-dimensional pairwise backward-line geometry**, not a physical image, finite pupil, eye/accommodation model, continuous illumination or new authorable observer component. In particular, the symmetric ±theta controls do NOT assert that the two rays enter one eye. A single normal ray cannot locate depth geometrically. Three oblique paths need not have concurrent backward extensions; they must not be averaged into an asserted unique image.

## Builder evidence already inspected — not an independent review

The builder retrieved the completed [plane-mirror workflow run 44143858695](https://github.com/physicsvigilante/opticsim/actions/runs/44143858695), [job 134253547783](https://github.com/physicsvigilante/opticsim/actions/runs/44143858695/job/134253547783), including its full decoded log. That job includes `npm test`, the new native probe and every existing Node test. The log records the exact synthetic checkout, Node **v24.19.0**, the native pin, all eleven new tests passing, and **801 tests / 801 pass / 0 fail / 0 skipped / 0 cancelled**. This was the first source attempt; no source correction or rerun was required for this probe.

All **11 standard workflows** completed successfully on this source: optical composition `44143858494`, planar refraction `44143858909`, unified problem workflow `44143858586`, qualified authoring `44143858489`, source motion `44143858548`, planar angular queries `44143858769`, mirror angular queries `44143858695`, curved mirrors `44143858577`, parameter experiments `44143858605`, original refraction pair `44143858566`, numerical reliability `44143858543`.

The [optical composition run](https://github.com/physicsvigilante/opticsim/actions/runs/44143858494) completed its existing native, CLI, preinstalled-Chrome and hosted-path browser checks; [planar refraction](https://github.com/physicsvigilante/opticsim/actions/runs/44143858909) also completed successfully. These are **existing regression suites**, NOT a newly implemented apparent-depth UI/browser demonstration. Repeated jobs are builder-CI executions, not eleven independent physics reviews.

### Selected observed values, transcribed from the raw native log

Default source normal depth is **120 mm**, object-medium index **1.5**, observer-side index **1**. Angles below are signed incident angles in the object medium, measured from the normal. The paraxial analytical limit is 80 mm; it is NOT imposed on native rays.

| Explicit incident-ray pair | Normal depth of backward intersection, mm |
| --- | ---: |
| −5°, +5° | 79.61636684775047 |
| −1°, +1° | 79.98476458468129 |
| −0.1°, +0.1° | 79.99984769083608 |
| −30°, +30° | 61.10100926607784 |

For ±30°, actual detector hits are approximately `(100, ±182.6713742055232)` mm, with actual incoming unit directions `(0.6614378277661478, ±0.75)`. Each run emitted one ray, transmitted and reflected once at the interface, recorded one detector crossing, and completed with zero truncation/undefined behavior. The backward intersections are derived AFTER these measurements.

Nearby incident directions 20°, 21°, 22° yielded pairwise intersections, in mm:

- 20°/21°: `(-59.963563260395205, 7.837454133628043)`.
- 21°/22°: `(-57.87945477846891, 9.166054470073817)`.
- 20°/22°: `(-58.89610066658312, 8.475454313109111)`.

The first two intersections differ by **2.4715758168506468 mm**; the test explicitly records a unique-image result as unavailable rather than manufacturing one.

### Controls and withholding

Reverse source side, interface normals ±180°/90°/±37°, translations, mm/cm/m representation and component ordering passed. Equal indices return the actual source position at 120 mm; the 1→1.5 index reversal at ±10° gives 181.54790462647537 mm. Detector-distance controls preserve the same intersection. An explicitly transmitted-only control has `qualified` native readings with the existing approximation warning, not full-Fresnel evidence.

At ±50° native TIR yields zero transmitted detector hits; a short detector also genuinely misses the transmitted ±30° rays. Both retain measured empty lists/zero counts, while the derived intersection is unavailable/null. At critical incidence ±1e-5° offsets, the below-critical side transmits and the above-critical side has TIR. Exact-critical behavior is NOT certified. Nearly parallel ±1e-6° paths complete natively but their backward intersection is withheld. `maxRayDepth=0` gives incomplete native execution and suppressed/null native readings. Stale and missing opt-in evidence, duplicate/single paths, incompatible source/material experiments and a second boundary are declined by the helper. Capture ON/OFF preserves the native summary and existing observation keys without adding fictitious source IDs to hit events.

This section is a builder-transcribed digest, not a replacement for raw CI logs and not an independently executed replay. Local work was Node22 syntax/reference calculation only; no local native or browser execution is claimed.

## Review questions and known limits

1. Verify the exact source/tree/CI checkout identities and sole test-file diff. Independently inspect native logs and recompute the symmetric and neighboring-pair geometry, rather than accepting this digest as a verdict.
2. Check the distinction between a paraxial apparent-depth model, a symmetric-ray axis intersection, a local oblique pair intersection, and an actual specified observer/pupil. Is the stated research conclusion narrower than the evidence, with no hidden image or continuity claim?
3. Check canonical source direction, both media, y-up transformations, native transmitted-branch eligibility, duplicate/path provenance and stale/incomplete refusal. These scenes use one known source per run; they do not establish general multi-source lineage or pairing.
4. Assess numerical conditioning. `MIN_LINE_SINE=1e-6` and `LINE_RESIDUAL_MM=1e-6` are explicitly **research heuristics**, not a validated error bound. The residual is internal consistency, not independent accuracy certification. Review near-parallel and near-antiparallel conditioning, large coordinates and exact-critical/grazing exclusions before proposing a production envelope.
5. Check qualification propagation before any code reuse: the local helper uses `available` for a computed geometric intersection even when its input native readings are `qualified` by the transmitted-only approximation. The source readings and warnings remain in the logs, but there is no production derived-result contract here. A future API must explicitly retain these warnings and distinguish native measurement from derived geometry; the helper must not be copied uncritically as a certified observable.
6. Identify coverage gaps and a minimal JEE-first next step. Do not infer observer-position selection, finite-pupil visibility, arbitrary slab/curved-interface composition, 3D imaging, uncertainty bounds or textbook-question coverage from this test-only result.

Primary background: [PhyDemo apparent-depth demonstration](https://phydemo.app/ray-optics/gallery/apparent-depth), [OpenStax §2.3](https://openstax.org/books/university-physics-volume-3/pages/2-3-images-formed-by-refraction). Neither substitutes for inspecting the pinned engine or the executed source tree.

## Required reviewer deliverable

Publish `projects/opticsim/pr-131/reviews/review-01-chat-b.md` in this review repository. Record the exact source SHA/tree, evidence actually inspected, independently reasoned physics, ranked issues, and the limits of any execution you performed. Choose **CLEARED FOR OWNER DECISION / CHANGES REQUESTED / INSUFFICIENT EVIDENCE**, explicitly scoped to this research checkpoint and suitability for the next bounded design step. Do not claim independent native/Chrome re-execution unless genuinely performed.

Even a clear review is not merge authorization, production availability, or approval to lift any other held gate. All Opticsim PRs remain draft/unmerged; any production implementation needs its own exact-source verification and independent review.
