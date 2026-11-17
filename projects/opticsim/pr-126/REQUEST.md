# Independent physics review request — Opticsim PR #126

## Purpose and frozen source identity

Review the **native parallel-beam feasibility evidence**, not a released authoring feature. [Draft PR #126](https://github.com/physicsvigilante/opticsim/pull/126) is directly based on production main `d3509e82fb65d81aabe336666851f8f2962623f4`, with exact source HEAD **`2632efa3d1e2187e4cd793eb80a505b7302919c7`** and tree **`604e69cfd195ade6968ca6df3ddb557ad9e9337e`**. Its CI synthetic merge **`87fdee7377c1d417bc20e4bcabbf966c4823452f`** has the identical Git tree. Verify these identities yourself.

Only two paths are added: `test/jee-native-parallel-beam.test.mjs` and `docs/JEE-FIRST-DRAFT-NEXT-STEPS.md`. No `src/`, original tests, workflows, schema, native cutoff, upstream pin, optical solver, historic evidence or browser implementation is changed. The JEE-first plan follows the owner's newly approved priority; the older Atlas's beam deferral is historical and remains untouched.

## Critical distinction: parallel beam versus point fan

The prior #121 `AngleSource` research involved rays from one point with different angles. This candidate instead uses pinned PhyDemo **`Beam`**, emitting rays at different positions with one common direction. It does not place a fictitious source at infinity, synthesize ray arrays, prescribe encounter order or implement a second ray tracer.

Inspect the exact pinned upstream source `ricktu288/ray-optics@811f508d2b070898c241a568b0c167dcb8645251`, `src/core/sceneObjs/lightSource/Beam.js`, together with Opticsim's unchanged native adapters and observations. For direction theta in project y-up, the beam's ordered tangent is `(sin(theta),-cos(theta))`; endpoint construction then converts y to native y-down. Confirm that the native generator emits along the intended direction from the finite source segment. Width, position, direction and brightness are explicit; divergence is zero, randomness and Lambertian options are false.

## Research harness boundary

The test first prepares an already-supported optical arrangement using its existing point-source contract, then substitutes **only the native source object** with `Beam`. Every other compiled native object is asserted unchanged. This is a deliberate **test-only bypass of source admission**, not validated public beam authoring. The old canonical document's source-centre validation does not certify the entire finite emitting segment. The test must never pass its substituted scene through public result qualification using the old hash or export a purportedly qualified beam scene. The canonical authoring/compiler must still reject `parallel-beam`.

The native source-start wrapper snapshots actual emitted positions/directions before tracing and delegates exactly once. Incident wrappers record actual native arguments and returned outgoing directions without overriding them. Original detector/interface/blocker observers and native completeness gates remain authoritative. The test's direct analytical calculations are references to compare after native simulation, never inputs to ray propagation. Bounded evidence overflow must fail the test, never silently clip evidence.

## Independently recompute the physical controls

1. **Free space:** width40 mm, source centre(-100,0), propagation+x, native density0.2. Expected eight midpoint samples at y=17.5,12.5,7.5,2.5,-2.5,-7.5,-12.5,-17.5 mm; common direction(+1,0). Check actual source-start evidence rather than a manually emitted list.
2. **Converging ideal lens:** f=+100 mm at x=0. All eight parallel samples cross detector at (100,0). Reversed source at x=+100, direction180 degrees should cross(-100,0). This tests the *ideal* lens model, not a material-lens PSF, physical zero-width image or full finite-angle image theorem.
3. **Diverging ideal lens:** f=-100, detectorx=+100. Observed downstream y should be twice its incoming height (extreme +/-35 mm). There is no detector placed at a virtual focus and no detected virtual-image claim.
4. **Aperture clipping:** aperturex=-50, y=0, vertical total length100, gap12 mm before converging lens. Only two samples at y=+/-2.5 pass; six strike native opaque arms. Require two actual lens encounters and detector crossings, not just an aggregate ray count.
5. **Slab:** boundariesx=0,60 mm, outside n=1, interior n=1.5 and separately1.8; beam direction30 degrees. Recompute r=asin(sin(30 degrees)/n), native exit parallelism, each detector intercept atx=120, and perpendicular lateral displacement `60*sin(i-r)/cos(r)`. Builder reference values are ~19.4712206345 degrees /11.6288269291mm for1.5, and16.1276202132 degrees /14.9749373259mm for1.8. Check them independently. Both slab interfaces omit partial Fresnel reflection explicitly in these transmitted-only controls.
6. **TIR:** high-to-low1.5->1 plane atx=0, incidence60 degrees. Critical angle ~41.8103148958 degrees; all eight incident samples should reflect with direction(-1/2,sqrt(3)/2). Detector atx=-150, y=400, length400 must encounter the reflected rays. Inspect full emitter segment's actual starting region for this fixed fixture.
7. **Sampling:** density0.4 produces16 samples for the40mm beam, preserving parallelism and ideal focal plane; repeat the same native run and compare actual emitted/incident evidence for deterministic equality. This is not continuous irradiance convergence or calibrated power.
8. **Incomplete/stop:** full-Fresnel slab at existing depth8 produces an incomplete tree; source-CI reported truncation0.006030001375125609 and zero undefined behavior. Native raw counters may still exist for research diagnosis, but the complete detector-position list must be null. Processed-ray limit1 produces stopped/incomplete status, also with no accepted position list. No budget increase to force success.

## CI and independence

The first source-CI Node runs passed **798/798 tests**, including all8 new tests. This is a main-based tree (790 pre-existing main tests plus8), not a reduction of the distinct 866-test held integration stack. Direct native logs are available in [curved workflow44125543968](https://github.com/physicsvigilante/opticsim/actions/runs/44125543968), job134188196653, as well as the [optical workflow44125544838](https://github.com/physicsvigilante/opticsim/actions/runs/44125544838) and [planar workflow44125545198](https://github.com/physicsvigilante/opticsim/actions/runs/44125545198).

**Preserve the failure record:** [qualified-authoring workflow44125544327](https://github.com/physicsvigilante/opticsim/actions/runs/44125544327), first job134188198748, passed all798 tests and existing CLI acceptance but then failed before browser validation with `Chrome/Chromium unavailable; no browser validation performed`. The unchanged job has been requested for rerun; consult STATUS.md and actual run attempts for its final result. Do not infer optical failure from missing Chrome, or erase the infrastructure failure when reporting a retry. Existing Chrome regression success does **not** establish a new browser Beam authoring path; none was implemented.

## Next-design requirements, not claims established here

A real source contract must validate the **entire emitting segment**: finite bounds; no optical surface intersection or ambiguous starting medium; clearance from corners, rims and grazing cases; explicit brightness/sampling semantics; old-version isolation; and complete native qualification. It needs public CLI authoring, revisions, save/reopen and real Chrome tests before claiming LLM-authorable beams. Finite prism, curved glass, arbitrary oblique lenses, multiple beams, divergence/randomness, source attribution, observer images and continuous radiometry are not established by this bounded experiment.

## Report

Publish `physicsvigilante/review_sandbox/projects/opticsim/pr-126/reviews/review-01-chat-b.md` with exact source/tree verification, independently computed references, ranked findings, explicit evidence limitations and one verdict: **CLEARED FOR NEXT DESIGN STEP**, **CHANGES REQUESTED**, or **INSUFFICIENT EVIDENCE**. State whether you actually ran pinned PhyDemo/Node/Chrome independently or inspected builder CI and recalculated scalars. Do not claim to be a human optics expert. Never merge PR #126 or any held feature/research prerequisite. The verdict supports research/design only, not production admission or release.
