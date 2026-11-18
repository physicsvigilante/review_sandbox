# Independent R1 review request — Opticsim PR #143 apparent-depth feasibility

**RESEARCH ONLY / DO NOT MERGE.** Please independently inspect the native evidence and physics interpretation. This request is not a claim that Opticsim has a new released observer or image capability.

## Exact identity and ancestry

- [Draft Opticsim PR #143](https://github.com/physicsvigilante/opticsim/pull/143) (independently based on current production main).
- HEAD: `2ec38c431b7c191d1fed225eaa8db6ae1115caeb`.
- Git tree: `b71a840d9a14b85749fe0a587e65bbb115886243`.
- Base main: `d3509e82fb65d81aabe336666851f8f2962623f4`.
- PR synthetic test merge: `22477a0c70c2fd01ec24df8205b93aafa5483633`; its Git tree was checked to be identical to HEAD `b71a840d9a14b85749fe0a587e65bbb115886243`, and its parents are exactly production main and research HEAD. Verify these independently from Git commit objects.
- Only two added files: `test/jee-apparent-depth-native-feasibility.test.mjs`, `docs/JEE-APPARENT-DEPTH-RESEARCH.md`. **No production code, schema, adapter, native PhyDemo source, validation or browser code changed.**

## Why this matters for JEE Ray Optics

JEE frequently discusses apparent depth of an object observed across a planar interface. In the paraxial approximation, `d_app≈d*n_observer/n_source`. A refracted ray's backward extension to the axis is an **analytical inference**, not a physical ray traveled backward, a reconstructed optical image or a native detector observation of a virtual object. At finite angles, the axis intercept depends on viewing angle. Treating all finite-angle rays as though they share a single image point would be physically misleading.

Existing native v5 `point-source` SingleRay and `planar-interface` PlaneGlass, opt-in native detector-hit-events, and interface-first-event direction records are enough to study this boundary without implementing new optics or observer logic. Verify the experiment uses exactly these pinned native facilities.

## Geometry and independent reference

- World x-right, y-up. Interface at x=0 with normal +x; all dimensions mm.
- One source at (-60,0), emitting one explicit ray per independent run at 2°, 5°, 12°, 25°, 30°, with +5°/−5° symmetry control. No non-native multi-ray bundle or reconstructed source is inserted.
- Source-side negativeIndex=1.5; observer-side positiveIndex=1; explicit `partialReflection:false` (transmitted-only approximation; native TIR still active); source brightness=1.
- One vertical native detector centered at (100,0), orientationDeg 90°, length 400 mm (whole detector in observer medium).
- Requests opt-in `interface-first-event`, `detector-hit-events`, `detector-crossings` and `source-emissions`. No detector-source pairing is inferred; the fixture has exactly one source and ray.

Let `i` be incidence from interface normal, `t=asin((n_source/n_observer)sin(i))` when transmitted. An independent finite-angle reference is `d_app(i)=60*tan(|i|)/tan(t)`; the paraxial limit is 40 mm (for index 1.5→1), not 40 mm at all finite angles. Backward-axis intercept from native hit (x_D,y_D) and native measured outgoing unit (u_x,u_y) is `x_virtual=x_D−y_D*u_x/u_y`, only when u_y is nonzero and the actual native transmitted hit is complete. This backward extension is performed **after** native execution, outside the solver. It does not add rays or force the native trajectory.

Native builder CI for finite-angle source index 1.5 / observer 1 yielded apparent depths (mm):
- 2°: `39.969501869753245`
- 5°: `39.80818342387525`
- 12°: `38.85407850125944`
- 25°: `34.13377119352626`
- 30°: `30.550504633038912`

Checks also cover +5°/−5° symmetry; 1→1 equality (60 mm) and 1→1.5 observer denser (90.19115365768965 mm at 5°); at i=50° the high→low native ray is TIR with zero transmitted detector hits (no virtual inference); at i=0° one native hit exists but no **single-ray determined** virtual intercept; deliberate maxRayDepth=0 yields `incomplete` with all requested measurements suppressed.

## CI and independence boundaries

At HEAD `2ec38c...`: **11/11 standard Actions workflows SUCCESS**. [Optical composition native job run #44272676234](https://github.com/physicsvigilante/opticsim/actions/runs/44272676234), job `134692924534`, logs **796/796 Node tests** and exact named `JEE_APPARENT_DEPTH_NATIVE_FINITE_ANGLE`, `JEE_APPARENT_DEPTH_NATIVE_INDEX_CONTROL`, `JEE_APPARENT_DEPTH_NATIVE_INCOMPLETE` records. Existing v4/v5 test suite and browser checks passed on the exact source tree. Source CI is builder execution. **Do not claim independent PhyDemo/Node/Chrome runs unless genuinely performed.** No general JEE problem-solving or human observation/PSF capability has been established.

## Focused reviewer tasks

1. Independently verify HEAD/merge tree and git parent identity, patches and actual CI logs (not PR prose).
2. Inspect the native readout provenance: actual transmitted branch and hit, complete scene-hash-bound reporting, no fabricated backwards physical ray, no hidden native input override.
3. Check Snell reference and finite-angle apparent-depth values, including reversed index, i=0 singularity, symmetric ± angle, and the TIR case. Consider numerical tolerances, detector placement and geometrical constraints.
4. Check how the tests avoid mislabelling source-specific arbitrary ray histories or actual image detection, and whether incomplete measurements could leak.
5. Identify serious P0/P1 errors, missing controls or material omissions, and recommend a **bounded next engine step** (if feasible) instead of claiming general observers or images. Keep assumptions and limitations explicit.
6. Keep this test-only R1 review separate from the independently reviewed (but unreleased) v19 beam fix #141, held v14-v18, and branch-protection issue #123.

Publish to `projects/opticsim/pr-143/reviews/review-01-chat-b.md` with exact commit/tree, independent numerical reasoning, actual evidence provenance, issue ranks, limitations and verdict **CLEARED FOR NEXT SCOPED DEVELOPMENT / CHANGES REQUESTED / INSUFFICIENT EVIDENCE**. Do not merge, modify production source, approve as the builder or retroactively edit earlier reviews.
