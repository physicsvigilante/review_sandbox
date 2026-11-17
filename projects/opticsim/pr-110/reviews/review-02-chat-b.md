# Opticsim PR #110 — Chat B targeted independent R2 re-review (report 02)

**Review date:** 2026-11-17  
**Verdict: CLEARED FOR OWNER DECISION** — for the **bounded v15 native biconvex thick-lens capability only**.  
**Exact candidate source HEAD:** [`80fec0bb05200ad6034bf55a00c6e522740b27e1`](https://github.com/physicsvigilante/opticsim/commit/80fec0bb05200ad6034bf55a00c6e522740b27e1), [draft PR #110](https://github.com/physicsvigilante/opticsim/pull/110).  
**Original reviewed source:** `610d748e91f25f6233fb057932cabe6a62ed2a1a`; **dependency:** v14 [draft PR #107](https://github.com/physicsvigilante/opticsim/pull/107) at `fe3a030be7bfba8e5808e4e1e2e66d6815e7add7`; **upstream pin:** PhyDemo `811f508d2b070898c241a568b0c167dcb8645251`.  
**Review separation:** This is a *new* independent follow-up. [Review 01](review-01-chat-b.md) remains unchanged, with its original verdict **INSUFFICIENT EVIDENCE** at the old HEAD. This report evaluates whether new *test-only* native evidence closes its specific R2-01/02/03 release-evidence gaps; it does not reinterpret that prior verdict.

## Executive disposition and provenance limits

**The material R2-01, R2-02 and R2-03 evidence gaps have been sufficiently closed for an owner decision on the explicitly bounded v15 capability.** The new CI records true pinned-native face callbacks for reverse incidence, top and bottom rims, near-critical/TIR rays, tight-clearance rays, and s/p-separated Fresnel power. I independently recomputed line/circle intersections, finite rim intersections, Snell/reflection directions, clearance geometry, and Fresnel coefficients with a standalone Python calculation that did **not** import Opticsim or PhyDemo. The numerical comparisons agree to floating-point scale in the reported cases. No reproducible new production implementation defect was identified.

**Reviewer's own native execution: NONE.** The available local Node was `v22.16.0`, below the project's pinned `>=24.19` requirement; I did not install the native checkout, run the pinned simulator or execute Chrome. **Native events described below are actual events recorded by source GitHub Actions CI, not my independent native reproduction.** I inspected the exact-head workflow metadata, the native console evidence in two independent GitHub Actions jobs, original production and upstream source, and the new test's callback instrumentation. I did not inspect new screenshots and do not claim browser visual certification.

This verdict **does not approve merging**. PR #110 remains **draft/unmerged** and its separate v14 dependency PR #107 is also **draft/unmerged**; the owner must decide their release order separately. It does not certify arbitrary optical arrangements, complete image formation, textbook interpretation, original problem images, or all near-grazing binary64 configurations.

## 1. Independent change isolation, CI, and test trust boundary

- GitHub comparison [`610d748e...` to `80fec0bb...`](https://github.com/physicsvigilante/opticsim/compare/610d748e91f25f6233fb057932cabe6a62ed2a1a...80fec0bb05200ad6034bf55a00c6e522740b27e1) is **six commits ahead, zero behind**, and changes **exactly one file:** [`test/native-thick-lens-r2-review-regressions.test.mjs`](https://github.com/physicsvigilante/opticsim/blob/80fec0bb05200ad6034bf55a00c6e522740b27e1/test/native-thick-lens-r2-review-regressions.test.mjs), **411 insertions, zero deletions**. No v15 production file, native vendor source, cutoff, admission guard, or original frozen fixture changed relative to reviewed source SHA. The history includes an R2 test merge and an attestation commit; neither altered production.
- The actual [unified run 44036232902](https://github.com/physicsvigilante/opticsim/actions/runs/44036232902) and [planar/Chrome run 44036233039](https://github.com/physicsvigilante/opticsim/actions/runs/44036233039) have status **completed/success** at precise `head_sha=80fec0bb...`; both job logs show **Node v24.19.0**, **820 tests, 820 pass, 0 fail**, and identical `V15_R2_*` event records. All **11/11** standard workflow runs indexed for that head concluded **success**. The relevant planar/Chrome job step also concluded success; this is CI evidence, not a separately inspected screenshot.
- I fetched Git commit objects rather than accepting the PR description's merge-tree claim. Main-target synthetic merge `60382941576743270a6cd575cb9a240941d523de` has parents **main `d3509e82...`** and **exact source HEAD `80fec0bb...`**. Both this merge and the source HEAD have **identical Git tree `fb4108913d5c711ea38c960b5c6d02b1305bc590`**. Therefore the workflow's synthetic-merge checkout represented the exact reviewed contents; it does not imply that v14 or v15 was actually released on main.
- The new tests edit **authored inputs** (source position/direction, lens physical parameters, detector position), then use `prepareScene`, the real `core.loadDocument`/`core.Simulator`, and existing `evaluateDocument` or `inspectNative`. The [inspection helper](https://github.com/physicsvigilante/opticsim/blob/80fec0bb05200ad6034bf55a00c6e522740b27e1/test/helpers/native-composition-inspection.mjs) wraps each `onRayIncident`, invokes its saved original **once** with original arguments, and logs returned rays. The new optional s/p test similarly reads native `brightness_s`/`brightness_p` before/after the genuine callback. Expected points are *post-execution assertions*, not injected ray endpoints or a prescribed optical route.
- I examined the unmodified `src/spherical-lens.js`, `src/planar-media.js`, `src/contract.js`, `src/observables.js`, `src/adapter.js`, [pinned upstream SphericalLens](https://github.com/ricktu288/ray-optics/blob/811f508d2b070898c241a568b0c167dcb8645251/src/core/sceneObjs/glass/SphericalLens.js), and [Glass](https://github.com/ricktu288/ray-optics/blob/811f508d2b070898c241a568b0c167dcb8645251/src/core/sceneObjs/glass/Glass.js). `SphericalLens.createLensWithDR1R2` produces a six-point native path with two arcs and two straight rims. `Glass.checkRayIntersects` determines actual nearest eligible arc/segment events; `Glass.onRayIncident` delegates the material interaction to native refraction. The Opticsim observer classifies the point after the hit; it is not a second production ray tracer.

**Historical CI failure is preserved, not rewritten:** the original test-only candidate `3c8ef6f...` produced a genuinely failed [unified run 44034839428](https://github.com/physicsvigilante/opticsim/actions/runs/44034839428), **817 pass / 1 fail**, at the R2-02 near-corner boundary assertion. The subsequent `7abc148...` commit corrected the *positive control's geometric assumption*; the `0.02 mm` horizontal aim shift does not equal a `0.02 mm` perpendicular clearance. No production geometry guard was weakened. The final green runs do not retroactively make the initial run green.

## 2. Independent reference method (distinct from source-native traces)

Coordinates below are **millimetres, x right/y up**. For each physical lens with half-aperture `a`, centre thickness `d`, centre x `c`, and curved-face radii `Rf,Rb`, I used the stable sag formula

`s(R,h) = h²/(R + sqrt(R²-h²))`, with `L=c-d/2`, `H=c+d/2`;

`x_front(y) = L + s(Rf,|y|)` and `x_back(y) = H - s(Rb,|y|)` (for the aligned, y=0 fixtures).

A standalone forward-ray solver evaluated both quadratic ray/circle intersections on the finite front/back branches, plus both finite horizontal rim segments, discarded negative or zero-distance intersections, and selected the **nearest positive hit among all lenses**. The outward normal on an arc was `(P−C)/R` and on the rims was `(0,+1)` or `(0,−1)`. For each hit it assigned `ni,nt` from the sign of incident-direction dot outward normal, preserved `ni * tangent(incident) = nt * tangent(transmitted)`, and used specular reflection when no real transmitted normal component exists. This Python construction never calls the native simulator or chooses a fixed sequence of face IDs in advance. It is an **independent reference**, not an independent native run or a proof over a continuous parameter domain.

## 3. R2-01 — reverse illumination, actual rim faces, and outward media

### Reverse, two biconvex lenses

I independently propagated **S=(400,10)** with direction **180°** through L1 at x=0 (n=1.5) and L2 at x=150 (n=1.3), each with `a=50,Rf=Rb=100,d=30` and common exterior n=1. The solver independently selected four hits, in precisely the order logged by source CI:

| Hit | Independent ray/circle (x,y), mm | CI-recorded x, mm | Refractive transition |
| --- | --- | ---: | --- |
| L2 back-arc | (164.498743710662, 10.000000000000) | 164.498743710662 | 1 → 1.3 |
| L2 front-arc | (135.435871918369, 9.326542732686) | 135.435871918369 | 1.3 → 1 |
| L1 back-arc | (14.973863408410, 2.286183543962) | 14.973863408410 | 1 → 1.5 |
| L1 front-arc | (−14.996035356364, 0.890456629347) | −14.996035356364 | 1.5 → 1 |

The source-CI test verified the real native sequence, per-face observer normals, entry/exit index pairings, Snell/reflection invariants, **completed** classification and **one native detector crossing**. The independent outgoing ray predicts y≈**−12.8828755102 mm** at detector x=−200; this *coordinate is calculated*, not a logged detector-hit position. It lies inside the authored 400 mm detector. Reversing list order alone would not test this; here the ray itself really travels right to left.

### Top/bottom rims

For `d = 2 s(100,50)+1.02 = 27.814919243112...` mm, the finite straight rims are **1.02 mm** long. From source `(−200,+55)`, aiming at `(0,+50)`, the nearest physically eligible intersection is the **top rim at (0,+50)** with outward normal **(0,+1)**. Reflection across y=0 gives a bottom-rim first hit `(0,−50)` and outward normal **(0,−1)**, with no authored post-entry route.

Independent line-normal calculation gives **incidence 88.567903815835°**; Snell for `1→1.5` gives **transmission 41.794309740763°**. The exact-head native logs show both observed first callbacks at x≈0 and y=±50, face IDs `top-rim`/`bottom-rim`, the correct normals, `outside→inside`, identical angles, **five total native lens events per case**, completed status, zero truncation and both sampled requests **qualified**. Later native interactions are not replaced with a conjectural route. **R2-01 closed** for the demanded representative reverse/rim controls.

## 4. R2-02 — extreme geometry, tight clearances, and corrected corner control

### Independently calculated finite extreme paths

The original native `SphericalLens` six-point path contains arc flags `[false,false,true,false,false,true]`. Source CI logged finite path points, an actual front-arc callback, `processed=3`, zero truncation and `completed` native status for each case. My stable-sag calculation gives:

| Admitted case | Independent front hit x at logged y (mm) | Source-native first hit x (mm) | Calculated minimum rim thickness |
| --- | ---: | ---: | ---: |
| `a=50,Rf=Rb=51,d=90,y=10` | −44.009999000200 | −44.009999000200 | 8.099751242242 mm |
| `a=2,Rf=Rb=10000,d=2,c=0,y=0.5` | −0.999987500000 | −0.999987500001 | 1.999600000000 mm |
| Same flat lens with `c=9998` | 9997.000012500001 | 9997.000012500000 | 1.999600000000 mm |
| `a=50,Rf=Rb=100,d=2s(100,50)+1.0001,y=10` | −13.396253332218 | −13.396253332218 | 1.000100000000 mm |

The `~1.2×10⁻¹² mm` flat-at-origin discrepancy reflects binary64 circle/sag evaluation order, not a demonstrable erroneous face in this control. The test asserts the actual six native path vertices against separate finite geometry; it **does not exhaustively check every possible extreme-ray interaction**. Do not interpret these finite points as a guaranteed global precision bound.

### Admission/clearance controls

The exact-head tests report **0.011 mm interlens x-gap**, **0.011 mm source-to-first-vertex x-clearance** and **0.011 mm exit-to-detector x-clearance** as admitted, natively completed traces. The first has two actual interactions on each lens; the latter two have two on the single lens; **each case logs one real detector crossing**. Neighboring `0.009 mm` gaps/clearances refuse authoring before a native run. Rim thickness just **above** `1.0000` mm admits; just **below** refuses. These are validated *admission thresholds*, not a universal `0.01 mm` bound on numerical ray errors.

For source `(−200,55)` aiming toward the upper front corner's x plus horizontal shift `δ`, I separately calculated the *perpendicular* ray-to-corner distances:

| Horizontal target shift δ | True perpendicular clearance | Expected admission / CI |
| --- | ---: | --- |
| 0.005 mm | 0.000125967 mm | refused |
| 0.020 mm | 0.000503828 mm | refused |
| 0.500 mm | 0.012565321 mm | admitted |

The admitted `δ=0.5` control actually hits the **top rim** at native **(−1.102540378443,+50)**, completed with qualified sampled events. The previous failed `δ=0.02` positive assumption was correctly fixed in the **test only**. **R2-02 closed** for the required adjacent-admission and finite extreme tests.

## 5. R2-03 — near-critical direction checks and polarization-resolved Fresnel power

### Separate subcritical and TIR paths

For a single `a=50,R=100,d=30,ninside=1.5,noutside=1` lens, I independently solved the directed ray from x=−200 to the front curved-face point `(−6.651513899117,+40)`, refracted it, then intersected the back **finite** circle. The two source angles and native/reference outcomes are:

| Authored source direction | Independent back-arc (x,y) mm | Independent inside incidence | Source CI observed |
| --- | --- | ---: | --- |
| −21.3° | (9.193713659301, 33.578926532420) | 41.680155112049° | Transmitted at 85.913470921047° |
| −22.0° | (9.256539871496, 33.402165969486) | 42.039189973427° | **TIR**, reflected direction (−0.476357191463, −0.879251855921) |

The independently calculated critical angle is **asin(1/1.5)=41.810314895779°**. Thus the first case is genuinely subcritical and the second genuinely supercritical by margins well larger than the logged rounding error. Actual native events report front **outside→inside (1→1.5)** then back **inside→outside (1.5→1)**, physically matching normals, completed status and zero truncation. The TIR event has a reflected direction satisfying the vector reflection law and **no transmitted native branch**. The other event satisfies Snell with a real outgoing branch. No route was injected or fitted to the expected back point.

### Actual s/p brightness, not merely an average

At the actual first front-arc incidence **5.739170477267°** with `n1=1,n2=1.5`, my independent Fresnel formula yields

`Rs=0.04053886672369661`, `Rp=0.039464440142489655`; unpolarized mean `R=0.04000165343309313`.

With recorded *incoming* native brightness **s=0.25, p=0.25**, the reference and actual instrumented `onRayIncident` values agree separately:

| First native branch | Independent s power | Native s power | Independent p power | Native p power |
| --- | ---: | ---: | ---: | ---: |
| Reflected | 0.010134716680924152 | 0.010134716680924152 | 0.009866110035622414 | 0.009866110035622414 |
| Transmitted | 0.23986528331907586 | 0.23986528331907586 | 0.2401338899643776 | 0.2401338899643776 |

Each polarization sums to its original `0.25`. This new callback instrument does not replace or direct the returned branches. **The entire Fresnel tree is still incomplete**: source CI logs total truncation **0.0007811854515818064**, and the full requested public measurements remain **suppressed** (both requests in this focused test; the older multi-lens Fresnel control also withholds all five). Truncation is **missing/omitted optical power**, not physically zero intensity; the correct outcome is diagnostic evidence without a qualified full-tree measurement. **R2-03 closed** for near-critical and first-interface s/p physics, not for complete branching or intensity imaging.

## 6. Severity assessment and residual limits

**Confirmed production defects: none in the reviewed R2-01/02/03 cases.** Test-only changes do not establish a production fix, and the original "INSUFFICIENT EVIDENCE" at the earlier HEAD is not revised.

**Residual numerical / scope limitations (not blockers to this bounded clearance):**

1. The finite probes do **not** certify exact-critical `θ=θcritical`, nearly coincident rim/arc intersections, higher-order reflected/refracted re-hits near corners, arbitrary near-grazing rays, all possible radius/aperture/coordinate tuples, or globally correct binary64 event order. In particular, a validator's 0.01 mm geometry guard is **not** a theorem of 0.01 mm native intersection accuracy. An initial-ray guard and observed-hit ambiguity check cannot exclude every unobserved near-miss in all future multi-bounce paths.
2. Extreme-case tests visibly prove finite six-point native construction, first curved-face event and completed runs, but are *representative* rather than an independent numerical enclosure of every native callback. Any newly reproducible unsafe admission should reopen the gate with its concrete authored fixture, raw native event/status and an independent geometry comparison; do not relax guards on speculation.
3. `partialReflection:false` deliberately omits ordinary Fresnel partial reflections (native TIR remains); `partialReflection:true` can truncate and correctly withhold measurements. Neither mode supplies certified complete energy accounting for all possible paths. Public observables are sampled native events and crossing counts, not continuous field intensities or source-attributed histories.
4. Native execution here is from **source CI**; the reviewer supplied independent physics recomputation, source/test inspection and CI provenance verification but **did not** perform a fresh reviewer-controlled pinned-native run or visually inspect Chrome evidence. This limits independence, but does not leave the specific R2 evidence gaps materially unsupported at the exact tree.
5. The capability remains isolated: **one or two nonrotated biconvex lenses, bounded directed single rays, common exterior index, external detectors**. Concave/tilted/mixed elements, inferred images, illustration interpretation and arbitrary optical combinations remain unreviewed.

## Final gate recommendation

**CLEARED FOR OWNER DECISION** for the exact **`80fec0bb...`** bounded v15 source and its demonstrated native-trace/qualification behavior. R2-01, R2-02, and R2-03 now have CI-observed *actual* native events accompanied by distinct independent geometry/optics calculations; no material contradiction or reproducible unsafe admission was identified. The earlier failing test is documented as a corrected test-assumption failure, not an engine repair.

**Do not merge or mark released as a consequence of this review.** Keep [#110](https://github.com/physicsvigilante/opticsim/pull/110) draft/unmerged; prerequisite [#107](https://github.com/physicsvigilante/opticsim/pull/107) still needs its separate owner decision. Preserve original reviewer report, test history, frozen evidence, native pin, source hashes and suppression limitations. This report creates no certification of original textbook problems, image reading, educational correctness or other v15 scope expansions.
