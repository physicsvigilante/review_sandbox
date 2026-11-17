# Opticsim PR #110 — independent Chat B R2 physics/geometry/code review

**Review date:** 2026-11-17  
**Verdict: INSUFFICIENT EVIDENCE**  
**Source candidate reviewed:** [physicsvigilante/opticsim PR #110](https://github.com/physicsvigilante/opticsim/pull/110), exact authored HEAD **610d748e91f25f6233fb057932cabe6a62ed2a1a**.  
**Reviewed dependency base:** v14 **fe3a030be7bfba8e5808e4e1e2e66d6815e7add7**, PR #107 still draft/unmerged.  
**Pinned native upstream:** [PhyDemo/ray-optics 811f508d2b070898c241a568b0c167dcb8645251](https://github.com/ricktu288/ray-optics/tree/811f508d2b070898c241a568b0c167dcb8645251).  
**Scope:** physical correctness, geometry admission, native observer, evidence and numerical reliability of isolated schema v15 native-thick-lens-tracing. This is not a textbook-interpretation, educational-outcomes or complete-image review.

## Executive disposition

The baseline two-lens geometry and four spherical-interface refractions independently agree with source CI to numerical precision. The sign convention, biconvex surfaces, four outward-normal formulas and dependence on the *unchanged* pinned SphericalLens/Glass ray tracer are technically coherent on source inspection. The new schema is isolated from versions 1–14, and incomplete Fresnel tracing correctly withholds all requested results instead of treating omitted branches as zero.

However, the current source test suite and recorded native traces do **not** exercise three essential claims over the admitted domain: actual top/bottom rim impacts, right-to-left illumination (reversing an array of components is not reversing light), and a controlled near-critical/TIR native event with per-face/index/direction checks. Boundary-thickness and extreme-radius/coordinate probes also remain missing. I could calculate adversarial reference cases independently, but I could **not** run a separate pinned-native Node 24 suite in this review environment. These are gaps in the release evidence, **not demonstrated errors in the implementation**. The requested adversarial R2 release gate is therefore not discharged.

**Do not merge #110 on this review.** Retain draft, obtain bounded native adversarial evidence at the exact candidate tree, and request a narrow re-review. PR #107 requires its own owner release decision first. No files or PR state in opticsim were changed by this reviewer.

## 1. Source, dependency and CI provenance

I read the exact candidate source, especially [src/spherical-lens.js](https://github.com/physicsvigilante/opticsim/blob/610d748e91f25f6233fb057932cabe6a62ed2a1a/src/spherical-lens.js), [src/composition-profiles.js](https://github.com/physicsvigilante/opticsim/blob/610d748e91f25f6233fb057932cabe6a62ed2a1a/src/composition-profiles.js), src/contract.js, src/adapter.js, src/planar-media.js, src/observables.js, src/authoring.js, src/app.js, [native test](https://github.com/physicsvigilante/opticsim/blob/610d748e91f25f6233fb057932cabe6a62ed2a1a/test/native-thick-lens-v15.test.mjs), [browser script](https://github.com/physicsvigilante/opticsim/blob/610d748e91f25f6233fb057932cabe6a62ed2a1a/scripts/native-thick-lenses-browser.mjs), fixture and scope document. I also read the pinned upstream [SphericalLens](https://github.com/ricktu288/ray-optics/blob/811f508d2b070898c241a568b0c167dcb8645251/src/core/sceneObjs/glass/SphericalLens.js), [Glass](https://github.com/ricktu288/ray-optics/blob/811f508d2b070898c241a568b0c167dcb8645251/src/core/sceneObjs/glass/Glass.js), [BaseGlass](https://github.com/ricktu288/ray-optics/blob/811f508d2b070898c241a568b0c167dcb8645251/src/core/sceneObjs/BaseGlass.js), and geometry/Simulator sources. The v14-to-v15 GitHub compare is **17 commits ahead, 0 behind**, with 17 changed files and **no upstream/vendored native source changes**. Contract UPSTREAM and upstream-pin.json agree on the exact SHA; the setup/build scripts reject a mismatched or modified vendor checkout.

Source CI, not reviewer execution: [unified run 44031360120](https://github.com/physicsvigilante/opticsim/actions/runs/44031360120) passed **812/812 Node tests**; [planar/Chrome run 44031360021](https://github.com/physicsvigilante/opticsim/actions/runs/44031360021) passed, including **nine** native-thick-lenses-browser checks on Chrome 157. Both job logs show the pinned upstream checkout. Both initially checked out synthetic merge **3118194752bbf1b13068c1acaa3a95bae608ea4a**, whose parents were main d3509e82... and source HEAD 610d748...; after retarget, the dependency merge is **b0bb292388012cad0dc94f2dce5147171ef3344d** with parents v14 fe3a030... and the same HEAD. I checked via GitHub commit objects that **both merge commits and source HEAD have the identical tree b28be7f56afde543c3ca385166636e90255a69c2**. Thus the successful checkout exercised identical source *contents*, despite the earlier workflow base. This does not constitute a new post-retarget workflow run or an independent native reproduction.

I downloaded and inspected the retained [planar/Chrome evidence artifact](https://github.com/physicsvigilante/opticsim/actions/runs/44031360021/artifacts/14304848663), including report.json and two screenshots. The report records **9/9 passed**, no errors, native ray rendering, separate L2 material edit, export/reopen, overlap refusal and a genuine miss. The images visibly show two finite lens bodies and a bent ray in the positive fixture, then a ray missing both lenses. This is useful browser and coherence evidence, **not** separate verification of curved-surface physics. The Chrome evidence explicitly marks physicsIndependentlyCertified=false.

## 2. Independent biconvex geometry proof and native convention

Write a=apertureHeight/2, d=centerThickness, L=x−d/2, H=x+d/2, and s(R,a)=a²/(R+sqrt(R²−a²)). The front physical surface at height h relative to lens centre is

**x_front(h) = L + R_front − sqrt(R_front²−h²)**,

and the back physical surface is

**x_back(h) = H − R_back + sqrt(R_back²−h²)**,

for −a ≤ h ≤ a. Every admitted R ≥ a+1 is real and nonzero. Each sag grows with |h|, so the minimum separation is at the aperture ends and equals **d−s_front−s_back ≥ 1 mm**. Consequently the two curved faces do not cross, and the top and bottom straight rims have positive 1 mm minimum lengths in *exact arithmetic*. Every lens is completely enclosed by its validated [L,H] x extent and y±a. The two-lens x-separation test therefore also prevents body overlap.

Pinned SphericalLens.createLensWithDR1R2 constructs path[0]/[1] at the upper rim, path[2] as the right curved vertex, path[3]/[4] at the lower rim and path[5] as the left curved vertex. With native y downward and authored p1 above p2, **r1=+R_front and r2=−R_back** generate exactly the intended front-left and back-right biconvex arcs. Glass.checkRayIntersects tests native finite arcs and straight rim segments, not a model-authored surface itinerary. This signed construction is consistent with the candidate compiler.

Outward normals on all four smooth face classes are likewise geometrically correct: front **(P−C_front)/R_front**, back **(P−C_back)/R_back**, top **(0,+1)** and bottom **(0,−1)** in y-up coordinates. Taking dot(incoming, outward)>0 as glass-to-exterior and <0 as exterior-to-glass assigns the intended absolute indices for forward and reverse travel. The observer uses actual callback points and flags zero/ambiguous/nonfinite normals; error collection prevents these measurements from qualifying. **This is a code/math check, not four-way native-event verification.** At a corner the normal is not unique; the 0.01 mm refusal of observed corner events is appropriate.

Baseline numerical geometry (a=50, R_front=R_back=100, d=30 mm): **s=13.397459621556 mm**, front rim x=−1.602540378444, back rim x=+1.602540378444, and **rim thickness=3.205080756888 mm**. No surface crossing occurs.

## 3. Independent ray/circle/Snell calculation versus source-native evidence

I independently intersected directed lines with the *physical finite-circle branches*, selected the first forward intersection, applied vector Snell refraction using the incident/outgoing media, and repeated from one surface to the next. This calculation does **not** call Opticsim or PhyDemo. Reference input is the exact synthetic fixture: S1=(−200,10) mm, direction (1,0), L1 centred x=0 with n=1.5, L2 centred x=150 with n=1.3, exterior n=1; a=50 mm, d=30 mm, both radii 100 mm.

| Physical encounter | Independent (x,y) mm | x from pinned-native CI | Incident → transmitted angle (deg) | Medium |
| --- | --- | --- | --- | --- |
| L1 front | (−14.498743710662, 10.000000000000) | −14.49874371066197 | 5.73917048 → 3.82255373 | 1 → 1.5 |
| L1 back | (+14.591776274279, +9.026521951111) | +14.591776274279326 | 7.09548190 → 10.67773952 | 1.5 → 1 |
| L2 front | (+135.032985219349, −2.568259302540) | +135.0329852193489 | 6.97054037 → 5.35653646 | 1 → 1.3 |
| L2 back | (+164.894324430509, −4.596079478455) | +164.89432443050868 | 1.25058289 → 1.62584686 | 1.3 → 1 |

The positional differences are at floating-point rounding scale; no discrepancy was found in these four *ordinary* curved-face encounters. My final outgoing direction is approximately **(0.997237061259, −0.074284881720)**, predicting a ray at detector x=350 with y approximately **−18.3847298903 mm**. Source CI independently records **one native detector crossing**, not a directly checked detector y coordinate; the predicted y must not be presented as an observed native value. The native logs also report exactly the front-arc/back-arc count pattern (one of each per lens) and first-face Snell values. The analytic construction does not impose that route on the engine.

With exterior index 1.2 instead of 1 and unchanged inside indices, the correct interface invariant is **n_in sin(theta_in)=n_out sin(theta_out)** using each lens's absolute pair. The compiled relative-index ratios insideIndex/outsideIndex implement that telescope correctly in an otherwise unmodelled shared homogeneous background. Source test confirms this non-air material case; I did not separately run it in the native engine.

## 4. Polarisation-aware Fresnel and truncation

From independent incidence/transmission angles above, the lossless planar-interface Fresnel **power** reflectance (s, p, unpolarised mean) for the four actual curved local tangent planes is:

| Encounter | R_s | R_p | mean R |
| --- | ---: | ---: | ---: |
| L1 front | 0.040538867 | 0.039464440 | 0.040001653 |
| L1 back | 0.041897710 | 0.038142683 | 0.040020197 |
| L2 front | 0.017405457 | 0.016625325 | 0.017015391 |
| L2 back | 0.017034323 | 0.016992155 | 0.017013239 |

The pinned BaseGlass.refract equations and relative index map agree with the standard s/p Fresnel formula on source inspection. **partialReflection=false** explicitly sets R_s=R_p=0 for partial reflections while retaining total internal reflection; this is an approximation, not a physically complete Fresnel tree.

The actual source native Fresnel-on CI reports **native status=incomplete**, total weak-branch truncation **0.016327373393958983**, and **all five** requested measurements **suppressed**. The candidate's classifyRun and SHA/execution gates enforce that result. It would be false to report zero missing power, complete detector coverage or a qualified multi-branch Fresnel outcome. One complete-run physics certification of Fresnel power is not available in this evidence; branching source observations can be checked diagnostically without weakening the strict measurement gate.

## 5. Severity-ranked findings and adversarial controls

### R2-01 — HIGH release-evidence gap: four physical face classes and reverse native incidence

The six focused v15 tests assert front/back counts in the baseline case, non-air exterior, a miss, reversed **component-list order**, geometric rejection and suppression. Neither test nor the nine Chrome checks verifies **an actual rim callback** or **illumination entering from the right**. The code's top/bottom normals and reverse-index logic look mathematically right but are not empirically established in the pinned engine. **Required before clearance:** direct native event tables for at least one top-rim and one bottom-rim hit, one right-to-left two-lens trace, and inside-to-outside events with verified faceId, point, outward normal, from/indices, Snell/reflection direction, and native completion/withholding state. These must use the same unmodified upstream pin and exact reviewed tree.

Independent reference example for reverse illumination: S=(400,10), direction 180°, standard two-lens fixture, Fresnel off. Geometric/Snell prediction is **L2 back x≈164.498743711; L2 front x≈135.435871918; L1 back x≈14.973863408; L1 front x≈−14.996035356**, in that chronological order. **These values are predicted, NOT native-tested here.**

Independent near-minimum-rim example: a=50, R_front=R_back=100, **d=27.794919243112 mm** gives **1.000000 mm** rim. From S=(−200,+55), choose the direction exactly toward P=(0,+50). An unambiguous mathematical first incidence at the **top rim** has normal (0,+1), exterior-to-glass angle ≈**88.567904°**, transmitted angle ≈**41.794310°** when indices are 1→1.5. Reflect the y coordinates to test the **bottom rim** with normal (0,−1). Inspect any subsequent internal TIR/edge events; do not require or hard-code a prescribed sequence. Verify the validator admits these off-corner candidates before native assertions. The source forward-ray corner guard protects only initial rays, not subsequent refracted/reflected approaches, so runtime ambiguity gating must be exercised.

### R2-02 — MEDIUM release-evidence gap: numerical extremes and false-admission/refusal boundaries

The exact geometric bounds guarantee a positive theoretical body, **not** native binary64 conditioning. Native construction computes each sag as R−sqrt(R²−a²) and reconstructs circle centres from three points; native Glass ray intersection and inside/outside testing also use floating arithmetic and a perturbed parity test ray. The validator uses a more stable algebraic sag and 0.01 mm clearances. This is a plausible numerical sensitivity at extremely flat curvatures, distant coordinates, almost grazing incidence and 0.01 mm inter-body gaps. I found **no demonstrated nonfinite arc or wrong normal**, but the test fixture alone does not establish safety throughout the admitted [1,10000] mm parameter range.

**Required probes:** R_front and R_back at the admitted **a+1 mm** boundary; thickness giving **1 mm** and just-below-1 mm rims; near-maximum R with small aperture at x≈0 and near ±10000 mm; two whole-body extents separated by 0.01 mm and rejected at <0.01 mm; a source/detector on or just off the x-clearance boundary; genuine finite lens misses; and near-corner angles just inside/outside the conservative refusal band. Compare the native instantiated path with independently computed endpoints and enforce finite path coordinates and explicitly withheld uncertain events. Do **not** silently adjust numerical thresholds or repair user geometry.

For illustration, a=2, R=10000, d=2 is geometrically admitted with sag≈0.000200000002 mm and rim≈1.999600 mm. Native three-point circle reconstruction can be ill-conditioned at large coordinate offsets; an analytic body-validity proof by itself does not certify the ray solver there.

### R2-03 — MEDIUM release-evidence gap: near-critical/TIR and full-Fresnel event-level proof

The upstream TIR path and Opticsim's observer are coherent on inspection, but no new v15 near-critical native case demonstrates that rim or curved-face **inside-to-outside** incidence is labelled with correct indices/outcome and has no fabricated transmitted branch. Also absent is a checked per-polarisation native reflected/transmitted event against the independent R_s/R_p table above. **Required:** at least one stable TIR and one just-subcritical case with incident/reflected/transmitted vectors, plus a Fresnel-on first-interface event-power check. Preserve source truncation/depth limits and suppress all affected requested measurements whenever the overall run is incomplete. Do not reclassify an incomplete run as complete to make this test pass.

### R2-04 — LOW documentation/interpretation caveat, not a blocker

The user-facing text correctly distinguishes sample counts from continuous throughput, native rays from ideal images, relative ray brightness from optical watts, Fresnel-off approximations from complete reflection trees, and browser functionality from physics certification. Retain these warnings. If a release summary is written, explicitly say that the available native reference uses a *synthetic* geometry, not a solved textbook exercise; simulation coverage and educational usefulness are distinct decisions.

## 6. Gate/compatibility assessment

- **Correctly implemented on inspected source:** v15-only cardinalities, explicitly authored positive independent radii, homogeneous indices and boolean Fresnel mode; right/back native radius sign; no new propagation solver; read-only callback delegation exactly once; per-body/per-face sampled counters; finite x separation; restricted source/detector locations; revision/qualified-export identity; strict suppression of stale, incomplete, stopped, undefined or malformed observation evidence.
- **Compatibility evidence:** profile catalogue extends v1–v14 without converting saved old scenes. Version-rejection tests and ordinary 812-test/Chrome jobs passed. The historical frozen R1 provenance file is not rewritten; a new append-only v15 app-source provenance fixture was added. I did not independently rerun every historical scene or rehash all freeze artifacts.
- **Ordinary geometry confidence:** HIGH for the reference's four curved surfaces, directions, signs and Snell equations; no discrepancy between my independent calculation and source-native coordinates.
- **Rim/reverse/critical confidence:** MATH/STATIC INSPECTION ONLY; no independent native outcome established.
- **Full Fresnel measurement confidence:** source evidence establishes **non-completion and correct withholding**; it does not establish an accepted complete Fresnel power tree.
- **Native tooling limitation:** I performed independent arithmetic and read GitHub/native/CI source and retained artifacts. The local runtime here was not the project's Node ≥24.19 pinned-native setup, and I did **not** execute a separate native PhyDemo suite. Do not count this report as an independent native execution.

## 7. Disposition and narrowly bounded next step

**VERDICT: INSUFFICIENT EVIDENCE** — no confirmed release-blocking geometry/optics defect in the inspected ordinary fixture, but the explicit R2 adversarial evidence gate is still open.

Have the builder add a **small, auditable set of native tests** for the R2-01/R2-02/R2-03 cases, printing actual callback points, face IDs, outward normals, indices, unit directions, TIR/branch powers, event status and truncation. Compare with separate deterministic spherical/Snell/Fresnel references. Include rejected-neighbor tests for geometrically ambiguous cases. Re-run exact-head Node/real-Chrome workflows and preserve native logs with tree and pin identity. Then request an **independent narrow review** of those added tests and outcomes; do not reopen architecture or replace pinned propagation. A clean run may support **CLEARED FOR OWNER DECISION** on a later reviewed HEAD, subject to owner approval and separate v14 release sequencing.

**No merge, source edit, branch update or CI rerun was performed by this reviewer.** This AI-assisted source/numerical review is not a human optics expert endorsement.