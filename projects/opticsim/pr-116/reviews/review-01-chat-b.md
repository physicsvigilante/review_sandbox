# Opticsim PR #116 — independent Chat B R2 physics and numerical review

**Date:** 2026-11-17  
**Reviewer:** Separate-context AI-assisted Chat B reviewer  
**Verdict: CLEARED FOR OWNER DECISION**  
**Release status:** NOT MERGED; NO OWNER APPROVAL IMPLIED.  
**Scope:** Draft v17 native two-thick-lens plus finite-mirror authoring and numerical-depth contract. This is a bounded software/physics review, not expert certification, an exhaustive optical-error assessment, or a claim that JEE problems can all be answered.

## 1. Reviewed, immutable identities

- Source: [Opticsim PR #116](https://github.com/physicsvigilante/opticsim/pull/116); draft, open, unmerged when inspected.
- **Reviewed final source HEAD:** 9157c7a9ba7b21d6c9fe816897612537e45e6b30
- **Reviewed Git tree:** 6b4e0f1654df6d0c1be68762f57f36b2c542f921
- Synthetic main-target CI merge: 90e201cc429c2859c39789d5514d8e43f847578e
- Independently fetched both actual Git commit objects from GitHub's Git-object API. Their tree SHAs **match exactly**. The synthetic merge has parents d3509e82fb65d81aabe336666851f8f2962623f4 and the stated source HEAD; the PR itself now targets its intended unreleased v16 dependency, not main. This is a source identity match, not an assertion that source CI ran a checkout of the literal source commit rather than the identical-tree synthetic merge.
- PR #113 v16, #110 v15, and #107 v14 are each independently observed draft/open/unmerged. They remain ordered owner-controlled release prerequisites.
- Pinned PhyDemo source: 811f508d2b070898c241a568b0c167dcb8645251, as checked against both the exact-head upstream-pin file and source-CI setup logs. Native pin, propagator, brightness cutoff and optical solver were not modified in the PR file inventory.

Authoritative source references: [v17 contract](https://github.com/physicsvigilante/opticsim/blob/9157c7a9ba7b21d6c9fe816897612537e45e6b30/docs/NATIVE-TWO-THICK-LENS-MIRROR-V17.md), [v17 admission](https://github.com/physicsvigilante/opticsim/blob/9157c7a9ba7b21d6c9fe816897612537e45e6b30/src/two-thick-lens-mirror-composition.js), [authoring](https://github.com/physicsvigilante/opticsim/blob/9157c7a9ba7b21d6c9fe816897612537e45e6b30/src/authoring.js), [canonical validation](https://github.com/physicsvigilante/opticsim/blob/9157c7a9ba7b21d6c9fe816897612537e45e6b30/src/contract.js), [whole-system profiles](https://github.com/physicsvigilante/opticsim/blob/9157c7a9ba7b21d6c9fe816897612537e45e6b30/src/composition-profiles.js), [native adapter](https://github.com/physicsvigilante/opticsim/blob/9157c7a9ba7b21d6c9fe816897612537e45e6b30/src/adapter.js), [native observations](https://github.com/physicsvigilante/opticsim/blob/9157c7a9ba7b21d6c9fe816897612537e45e6b30/src/observables.js), [v17 source tests](https://github.com/physicsvigilante/opticsim/blob/9157c7a9ba7b21d6c9fe816897612537e45e6b30/test/native-two-thick-lens-mirror-v17.test.mjs).

## 2. Methods and explicit execution limitation

I read the reviewer request, the exact source tree, the modified tests and browser script, relevant unchanged v15 geometry and event observers, and the pinned upstream PhyDemo native SphericalLens, Glass, BaseGlass, Mirror, Detector, SingleRay and Simulator sources. I directly fetched source/merge Git commit objects, CI run/job metadata and complete job log text.

**Independent reference calculation** was performed separately using Python 3: direct parametric line–circle quadratic roots; constrained finite front/back circular arcs and straight rim segments; nearest positive intersection; finite straight-segment mirror/detector tests; vector-form Snell's law, total-internal-reflection condition and specular reflection. No Opticsim module, generated native trace, prescribed path list, or native simulator was used to *compute* the reference rays. Sources and lenses were kept as explicitly authored; no intended itinerary was supplied to the calculation. The reference has no ray-branch sampling, native cutoff or exact-native-float error guarantee.

**I did NOT execute a second independent pinned-native build, Node 24 test run or Chrome session.** The review environment does not provide the project's supported Node >=24.19 checkout/build environment. All statements about actual native callback logs, 841 Node tests and 10 Chrome checks are independently inspected **source-CI observations**, not reviewer-native replication.

## 3. Independent finite geometry and Snell references

Fixture in [examples/native-two-thick-lens-mirror-v17.json](https://github.com/physicsvigilante/opticsim/blob/9157c7a9ba7b21d6c9fe816897612537e45e6b30/examples/native-two-thick-lens-mirror-v17.json):

- S1=(-200,0) mm with explicit direction 0 degrees, brightness 0.5.
- L1 centered at (0,0), L2 at (150,0) mm. Each is a 100 mm full-height, 30 mm center-thick biconvex body with front/back radius magnitudes 100 mm. L1 inside index=1.5; L2 inside index=1.3; shared outside index=1. Both explicitly disable partial Fresnel reflection.
- M1 finite vertical segment x=300, y in [-200,200] mm. D1 finite vertical segment x=-100, y in [-200,200] mm.

For half aperture a=50 and radius R=100 mm, spherical sagitta s=R-sqrt(R^2-a^2)=13.397459621556136 mm. The finite edge/rim thickness is 30-2s=3.205080756887728 mm, greater than the required 1 mm. L1 full x envelope is [-15,15] mm; L2 is [135,165] mm. L1 to L2 full-body clearance is 120 mm. The finite mirror is at least 135 mm horizontally beyond L2's full envelope. All fit the explicit geometry contract.

The axial ray meets the following independently computed finite intersections:

| Sequence | Element and surface | Point (mm, x/y) | Material transition |
|---|---|---|---|
| 1 | D1 outbound | (-100, 0) | passive crossing |
| 2 | L1 front curved arc | (-15, 0) | 1 -> 1.5 |
| 3 | L1 back curved arc | (15, 0) | 1.5 -> 1 |
| 4 | L2 front curved arc | (135, 0) | 1 -> 1.3 |
| 5 | L2 back curved arc | (165, 0) | 1.3 -> 1 |
| 6 | M1 finite vertical mirror | (300, 0) | reverse x direction |
| 7 | L2 back curved arc | (165, 0) | 1 -> 1.3 |
| 8 | L2 front curved arc | (135, 0) | 1.3 -> 1 |
| 9 | L1 back curved arc | (15, 0) | 1 -> 1.5 |
| 10 | L1 front curved arc | (-15, 0) | 1.5 -> 1 |
| 11 | D1 return | (-100, 0) | passive crossing |

Thus the independent path has eight lens interface callbacks, one mirror reflection and two detector crossings: D1,L1,L1,L2,L2,M1,L2,L2,L1,L1,D1. At these axial surfaces the exact local incidence/refraction angles are both zero; the left/right outward arc normals are respectively (-1,0)/(1,0). This prediction matches exact-head source-CI V17_NATIVE_DEEP_RETURN positions, order, face IDs, lens-specific index transitions and counts. The observed return is a *result*, not an authoring instruction.

For a nontrivial off-axis reference ray emitted from (-200,2) mm due right, my independent finite-arc/Snell calculation gives:

| Event | Independent x (mm) | Independent y (mm) |
|---|---:|---:|
| L1 front | -14.979998000 | 2.000000000 |
| L1 back | 14.983794901 | 1.800210300 |
| L2 front | 135.001158310 | -0.481311380 |
| L2 back | 164.996069960 | -0.886562238 |
| M1 | 300.000000000 | -2.898684821 |
| L2 back return | 164.879261455 | -4.912548339 |
| L2 front return | 135.120898025 | -4.915789727 |
| L1 back return | 14.950134203 | -3.157637229 |
| L1 front return | -14.967461501 | -2.550811837 |
| D1 return | -100.000000000 | 1.125407029 |

This off-axis numerical table is **independent prediction**, *not* a claim that source CI disclosed matching v17 per-event coordinates. The exact-head source CI does independently log that this off-axis arrangement encounters all eleven same-named objects in the same order and that the reversal of canonical object ordering does not alter its intersections.

An additional independent nonaxial y=10 mm pass yields its four outbound arc points:
- L1 front=(-14.498743710662, 10)
- L1 back=(14.591776274279, 9.026521951111)
- L2 front=(135.032985219349, -2.568259302540)
- L2 back=(164.894324430509, -4.596079478455)

Each agrees to displayed precision with **separately logged previously reviewed v15 thick-lens native CI** V15_NATIVE_THICK_LENSES at the final-head checkout. This cross-check exercises finite curvature and nonzero Snell deflection, not merely the axial normal-incidence fixture; it is not a new v17 reviewer-native experiment.

The native upstream [BaseGlass refraction implementation](https://github.com/ricktu288/ray-optics/blob/811f508d2b070898c241a568b0c167dcb8645251/src/core/sceneObjs/BaseGlass.js) uses relative material indices, vector Snell/TIR and optional Fresnel branches. The v17 adapter passes positive front and negative back native radii, plus each lens's inside/outside index ratio, consistent with these independent geometry and refraction references.

## 4. Adversarial topology and geometry checks

Independent finite-geometry predictions compared with **exact-head source-CI** emitted native sequences:

| Variation | Independently predicted encounter order | Source CI |
|---|---|---|
| Mirror between lenses, x=75 | D1,L1,L1,M1,L1,L1,D1; L2 genuinely unhit | matches |
| S1 points left to mirror x=-250, then right through both lenses | M1,L1,L1,L2,L2,D1 | matches |
| S1 y=80, above both finite lenses | D1,M1,D1; zero lens encounters | matches |
| Source right of the lenses, directed left; mirror on left | D1,L2,L2,L1,L1,M1,L1,L1,L2,L2,D1 | matches |
| Two explicit sources, center and y=2 | Two independent emitted rays; per-object counts aggregate, not source attribution | CI reports emitted 1+1, lens counts 8 each, mirror 2, detector 4 |

The source v17 tests also distinguish a mirror at x=165.009 (0.009 mm outside L2 envelope, rejected) from x=165.011 (0.011 mm outside, accepted). In code, each of the mirror segment's endpoints must be to **the same x side** of each lens envelope by at least 0.01 mm; hence a rotated segment cannot bypass the separation by keeping its center outside. The v15 validator separately checks full lens envelope disjointness, rim thickness, common outside material and detector/source separation. These checks conservatively reject some otherwise valid layouts and establish an admission margin, **not** a numerical accuracy theorem at 10 micrometers.

Beyond the named controls, near-grazing rays, secondary rim hits, almost coincident contacts, close-clearance configurations and almost-critical angles remain under-sampled physical/numerical cases. Their failure modes could depend on upstream's minimum-segment and random probe conventions. The project explicitly does not assert a broad accuracy certificate for those configurations.

## 5. Run depth, Fresnel physics and suppression

At normal incidence, the independent Fresnel reflected fractions per face are:

- L1 at 1 vs 1.5: R1=[(1.5-1)/(1.5+1)]^2=0.04000000000000001.
- L2 at 1 vs 1.3: R2=[(1.3-1)/(1.3+1)]^2=0.0170132325141777.
- Product along the principal *unbranched* eight-interface transmitted route: (1-R1)^4(1-R2)^4=0.7930044393334514 of initial intensity, **not** an estimate of total energy returned or measured by the finite detector. Other reflected paths, cutoffs and absorption of truncated branches matter.

For the supplied fixture Fresnel is deliberately OFF, so the single principal refracted ray is retained without partial reflected branches; total internal reflection is still a native possibility at sufficiently oblique internal incidence.

The pinned upstream [Simulator](https://github.com/ricktu288/ray-optics/blob/811f508d2b070898c241a568b0c167dcb8645251/src/core/Simulator.js) increases per-ray interaction depth on optical hits. If its depth exceeds the permitted scene maximum, the remaining brightness is accumulated as truncation; a processed-ray limit can stop the simulation. [Authoring](https://github.com/physicsvigilante/opticsim/blob/9157c7a9ba7b21d6c9fe816897612537e45e6b30/src/authoring.js) exposes the depth-16 policy **only for new v17 authoring by default** and [canonical validation](https://github.com/physicsvigilante/opticsim/blob/9157c7a9ba7b21d6c9fe816897612537e45e6b30/src/contract.js) rejects depth greater than 8 in all previous saved versions. Explicit v17 preview-v1 keeps depth 8; the exact-head CI shows native incomplete/truncation=0.5, not falsely successful 11-hit return. Depth16 is an execution ceiling, not the minimum depth for all possible scenes.

For the fixture with both lenses' Fresnel flags ON, exact-head native CI reports native status=incomplete, truncation=0.06506578033327412, undefinedBehavior=0; **all six public observable values suppressed**. This is the correct conservative classification for a non-negligible missing reflected tree; the unbranched transmittance above must not be marketed as measured total detector power.

[Native adapter](https://github.com/physicsvigilante/opticsim/blob/9157c7a9ba7b21d6c9fe816897612537e45e6b30/src/adapter.js), [run classification](https://github.com/physicsvigilante/opticsim/blob/9157c7a9ba7b21d6c9fe816897612537e45e6b30/src/adapter.js) and [observable evaluator](https://github.com/physicsvigilante/opticsim/blob/9157c7a9ba7b21d6c9fe816897612537e45e6b30/src/observables.js) preserve original native rays, per-lens first-event/face counts and global native errors/truncation/undefined behavior. The public evaluator clones the scene/execution inputs before asynchronous hash checking and requires matching canonical SHA, successful complete native run and applicable component/observable scope. Failed, stopped, truncated, stale or undefined runs must not produce qualified requested measurements. Source-provenance and complete image synthesis are explicitly not inferred for v17.

## 6. Source implementation and compatibility

- The **new isolated v17 composition profile** has exactly two physical spherical lenses, exactly one plane mirror, 1–4 explicit single rays and 0–2 passive detectors; additional optical types/third lens are disallowed.
- Whole-system validation first calls the **unchanged v15 full spherical train validator** on a read-only no-mirror subset, then checks the entire finite mirror against both lens x envelopes, followed by the established general-optical source/mirror and passive detector validators on their appropriate validation-only subsets. No subset is substituted into the canonical/native lists.
- The native scene compiler maps each authoritative component in its original order to the pinned native SingleRay, SphericalLens, Mirror or Detector. It does not supply a ray itinerary or add a solver.
- v15/v16 existing saved schemas remain unchanged and reject v17 mixtures or fabricated deeper limits. New authoring selects v17 on two lenses plus mirror. Structural revisions preserve the currently selected family instead of silently migrating.
- Sources are separately emitted; interface/mirror/detector counts are aggregated by their actual native object identities, not attributed to a particular source or paired into a path.
- UI exposes both lens parameter editors, the mirror editor and the v17 depth disclaimer; Chrome tests verify invalid edits clear previous results, qualified export/reopen preserves both physical lenses and maxRayDepth 16, and reruns use fresh native tracing.
- Historic frozen data are not rewritten: the browser UI's new hash is appended in its own v17 post-freeze fixture.

This does **not** establish arbitrary optical composability across mixed component families. Admitted capability is the explicitly constrained whole-system profile, with new arrangements authored within it.

## 7. CI evidence audit and failure history

I independently queried the GitHub workflow-run collection by final source HEAD. All **11/11 standard workflow runs** dated 2026-11-17 09:07 UTC were completed with conclusion success; run records point to exactly 9157c7a9ba7b21d6c9fe816897612537e45e6b30. The unified and planar workflows checked out the identical-tree synthetic merge 90e201c. Job logs confirm supported Node **24.19.0**, original PhyDemo checkout/pin **811f508...**, source test-core and Chrome viewer builds.

- [Unified run 44052685694](https://github.com/physicsvigilante/opticsim/actions/runs/44052685694): **841/841** Node tests passed; includes logged V17_NATIVE_DEEP_RETURN, default/preview depth gate, authentic missed mirror, two-source counts, full-Fresnel suppression, mirror-between, mirror-first, lens-miss and right-to-left cases.
- [Planar/Chrome run 44052685718](https://github.com/physicsvigilante/opticsim/actions/runs/44052685718): native test suite passed and the new real Chrome v17 script logged **checks-passed, 10**. Source script asserts genuine canvas rays, both lens editors, depth-disclosure, mirror misses, L2 material edits, qualified export/reopen, stale-result clearing on invalid overlap, all-ray miss and absence of external HTTP requests. These are actual CI Chrome browser checks, not an independent screen audit.

The earlier failing PR-head runs remain accessible. In particular, [run 44051371024](https://github.com/physicsvigilante/opticsim/actions/runs/44051371024) logged historical v15/v16 negative authoring assertions that became false when an explicitly new v17 authoring profile was added; those tests were amended to require fresh v17 admission **while old saved models still reject it**. [run 44051715271](https://github.com/physicsvigilante/opticsim/actions/runs/44051715271) also exposed a test-helper ReferenceError (prepare vs prep), subsequently corrected. The final exact-head 841-pass record resolves these known test failures; this audit does not erase their history or call earlier failures successful.

## 8. Severity-ranked findings and limits

| Severity | Finding | Required before a v17 owner release decision? |
|---|---|---|
| **P0/P1 — blockers** | **None found** in inspected bounded scope. No unsupported optical route is injected, no deep policy spills into older formats, no demonstrated bypass of incomplete/stale measurement suppression. | No source correction identified. |
| **P2 — coverage limitation** | No reviewer-native run was executed, although full final-head source CI and pinned native/Chrome metadata were independently inspected. Source CI tests off-axis Snell geometry and published prior v15 nonaxial numeric points; an additional independent reviewer-native nonaxial v17 sweep would strengthen confidence. | Recommended additional confidence, not a proven software defect; reviewer-native execution is explicitly optional where runtime is unavailable. |
| **P2 — numerical edge regime** | 0.01 mm full-envelope margin is an admission guard, not a proof of finite-arc intersection accuracy near corners, grazing, criticality or repeated close hits. Upstream uses binary64 numerical intersections and a minimum ray segment length; adversarial families may show error not captured in the synthetic suite. | Keep limitation explicit; consider later targeted native perturbation/close-contact tests. |
| **P2 — Fresnel/depth limitations** | Native per-ray 16-depth and 10k processed-ray limits can truncate a branching tree; upstream has a weak-ray cutoff. Exact-head Fresnel fixture **correctly suppresses** measurements; 16 is no universal completeness certificate. | Preserve the explicit qualification rule; do not claim complete Fresnel flux or power. |
| **P3 — interpretation** | Multiple-source interface/detector counts are aggregate callbacks. A completed sampled run does not establish continuous imaging, source-to-detector path ownership, radiometric power in watts, or a JEE textbook answer. | Retain caveats in UI/documentation. |
| **P3 — conservative scope** | Mirror/other surface x-envelope separation refuses physically valid tilted/interleaved geometries; this is intentional restricted authoring, not arbitrary optics support. | No requested change. |

I found no independent evidence of a new physics defect requiring PR changes. These limitations do not turn synthetic CI success into a mathematical certificate, and the native source itself—not our calculations—is still authoritative for emitted branches and ray intersections.

## 9. R2 decision and gates

**VERDICT: CLEARED FOR OWNER DECISION**, strictly for **PR #116 at source SHA 9157c7a9ba7b21d6c9fe816897612537e45e6b30 and tree 6b4e0f1654df6d0c1be68762f57f36b2c542f921**.

Reason: independently verified source/synthetic merge identity, exact-head pinned-native CI and actual Chrome provenance, source-level strict admission and results withholding, independent finite-arc/Snell/Fresnel references matching available native optical outcomes, valid alternate topology/miss controls and explicit noncertifying limitations. This is not a claim that an independently executed native simulator passed in this review environment.

Do **not** merge PR #116 on the strength of this review alone; the project owner's separate explicit authorization is required, and unreleased dependency branches #107 (v14), #110 (v15), #113 (v16) remain independently gated and must be dealt with in the intended order. If the candidate tree changes, this exact-head verdict does not automatically transfer.

**Repository changes made by this reviewer:** publication of this review file in review_sandbox only. No Opticsim files, branches, commits, PR statuses or upstream sources were modified by this review.