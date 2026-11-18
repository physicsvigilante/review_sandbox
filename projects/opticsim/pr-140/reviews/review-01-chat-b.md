# Chat B — independent numerical/physics review: Opticsim PR #140

**Review date:** 2026-11-18  
**Verdict: CLEARED FOR OWNER DECISION — RESEARCH ONLY.**

This is clearance of a bounded, **test-only** native feasibility/sensitivity study, **not** clearance to merge, deploy, expose B1b numerical coordinates, accept a native precision bound, or claim a physical eye, pupil, or unique perceived image. PR #140 must remain draft/unmerged unless separately authorized by the owner. The held B1a PR #138 continues to return public geometry as withheld/null.

## 1. Exact source identity, scope and chronological provenance

| Object | Independently verified evidence |
| --- | --- |
| PR | [Opticsim #140](https://github.com/physicsvigilante/opticsim/pull/140), open, draft, unmerged at final source check |
| Production baseline | Commit **d3509e82fb65d81aabe336666851f8f2962623f4**, tree **45ff3bcd9093a527652f13f76c3cc0b02826642f** |
| Authored and reviewed HEAD | **713dfcf083baed4743e3c94cca703bf58c9a49d9** |
| Authored HEAD tree | **a2308fe2c5baf7570b8d692c8595084eae001e37** |
| Tested synthetic PR merge | **122c7787dce613e063d4cef40a167adf2b9a05e4**; fetched raw Git commit has **identical tree a2308fe2...**, with parents production main **d3509e8...** and reviewed source **713dfcf...** |
| Source scope | Exactly **one added test file**, **test/jee-b1b-native-numerical-stress.test.mjs**, 798 inserted lines, blob **4176cd409f13ff0ed826f601ac622a4edf9b3fed**; no changed production/native/schema/CLI/browser/workflow file |
| Reused native fixture | The **555 non-heading original fixture body lines** are byte-for-byte identical to [PR #135 R2](https://github.com/physicsvigilante/opticsim/blob/d6aff4e388aef982c3fc1b88039d4ac6951b4fca/test/jee-finite-detector-window-feasibility.test.mjs), original blob **1a57c562bdf8eb00ebbc5e21569cc2cd179f9876**. Only opening comments differ before the separate B1b extension. |
| Last revision | Prior source **4742462e17db672d02e25dcf9e38ea0ff3cb54ad** to final HEAD changes exactly **three log payload keys** from label to caseLabel, not the source ray inputs, geometry arithmetic or assertions; verified against the actual final commit patch. |

[Preregistration issue #139](https://github.com/physicsvigilante/opticsim/issues/139) was created at **08:05:14 UTC**, before the first-source B1b CI jobs began at **08:07:41 UTC** on 18 November 2026. The 11 original-source workflows are retained and each concluded successfully. The final-source 11 workflows began at **08:13:38 UTC**. The issue body was subsequently appended with results; its present contents and creation timestamp establish prior issue creation but do not constitute a cryptographically immutable snapshot of every original preregistration sentence. The executed A–J/negative/sensitivity matrix matches the declared matrix in the reviewed issue and test source; this audit limitation is recorded under P3.

## 2. What was independently checked numerically

I fetched and parsed the **raw 663,960-character / 1,315-line** builder [Node24/pinned-native job #134667781481](https://github.com/physicsvigilante/opticsim/actions/runs/44265168150/job/134667781481), not merely the PR description. The log includes **195** research events, of which **19** are B1B_TEST_ONLY_STRESS, **6** B1B_TEST_ONLY_NEGATIVE, **2** B1B_TEST_ONLY_SENSITIVITY, and **114** native invocation records (including reused #135 controls). The final-source structural event names are parsed correctly.

Each positive case has two actual *separate* pinned native single-ray executions. I extracted logged **detector-hit-events pointMm and incomingUnit**, the associated finite detector length/endpoint distance, **detector-crossings**, per-ray canonical scene SHA-256, completed native status, first interface incident/destination indices, the first transmitted/reflected branches and directions, and raw/qualified warnings. For each of the **19 positive cases**, there are two distinct source scene hashes, one emitted native ray, one first interface transmission, **one selected real finite detector hit per run**, unit incoming vectors, and native outgoing hit directions **exactly equal** to the selected transmitted-branch directions in the logged JSON.

**Independent calculation method:** In the actual plane-centred oriented normal/tangent frame let the two *measured* detector positions be `(a₁,t₁)`, `(a₂,t₂)` and the two *measured* directions be `(uₐ₁,uₜ₁)`, `(uₐ₂,uₜ₂)`. Write `m₁=uₜ₁/uₐ₁`, `m₂=uₜ₂/uₐ₂`, and solve the **slope/intercept** equation
`a* = (t₂-t₁ + m₁ a₁ - m₂ a₂)/(m₁-m₂)`,
then `t*=t₁+m₁(a*-a₁)`. This separate arithmetic does not call or copy the candidate's determinant-intersection function. I checked source-side sign, both backward line parameters, both endpoint distances, coordinate transform, cross product magnitude, outgoing-vector unit norms, actual branch direction and `L = |source normal distance| + |detector normal offset|`. I separately computed the conditional finite-angle Snell symmetric-pair formula only as a **post-native** benchmark, never as an input to PhyDemo.

| Actual pinned-native pair | Independent derived normal depth (mm) | Positive native hit | Line sine / significant observation |
| --- | ---: | --- | --- |
| 1.5→1, 120/40, ±0.5°, 5 mm | **79.99619199829816** | y=±1.5708611274685678 mm | 0.02617736355; both backextensions ≈120.006474 mm; finite endpoint minimum 0.929139 mm |
| Equal 1→1 and 1.5→1.5 | **120.00000000000078**, each | y=±1.396298846521404 mm | 0.01745240644; zero native reflected branches |
| 1→1.5, ±0.5° | **180.00380787079325** | y=±1.2799356863361775 mm | Real one-hit transmissions |
| 1→4, ±0.5° | **480.0171352939742** | y=±1.1344896975464134 mm | 0.00436325737; max backward extension / L **3.25011483** |
| 4→1, ±0.2° | **29.997258295669422** | y=±0.9774393976049623 mm | Actual transmitted directions ±0.0139626056609 transverse |
| 2 mm window, ±0.2° | **79.99939075789197** | y=±0.6283226776980592 mm | Smallest positive endpoint clearance across positives **0.3716773223 mm** |
| 10 mm window, ±1° | **79.98476458468133** | y=±3.1421111764431533 mm | Both rays within finite 10 mm endpoints |
| Long 1000/500, ±0.05° | **666.6663493566427** | y=±1.5271637946808416 mm | 0.00261799130; negative backextensions ≈−1166.667349 mm |
| 10 side/normal/unit/translation variants | **79.996191998297–79.996192163460** | Native coordinate-rotated/translated finite hits | reversed source side, ±90°, ±180°, ±37°, 6500/−5200 mm, cm/m, component order |

The last row covers **10 independent H/I configurations**, giving **19 total positives** with the nine A–G fixtures above. All 19 meet the preregistered **0.02 mm moderate** or **0.1 mm long-range** *engineering alarms*, and each has the correct source-side and negative backward signs. Recomputed depth versus the test-local reported depth differs by **at most 2.2737367544×10⁻¹³ mm**. The largest observed independent depth versus conditional Snell reference discrepancy is **1.651623478×10⁻⁷ mm** in the large-coordinate cm/order variant, still below its test alarm. The maximum local-to-world reconstructed point difference from the recorded test diagnostic is approximately **9.1×10⁻¹³ mm**; logged native outgoing unit norm error ≤**1.11×10⁻¹⁶**, with branch direction difference **0** for the 19 positive pairs.

These very small differences are **consistency of algebra and those native samples**, emphatically **not a calibration or bound on upstream native physical/numerical error**. The two line algorithms are correlated because they use the *same measured positions/directions*. A vanishing two-line residual is tautological for intersecting infinite supporting lines.

## 3. Real refusals, warnings and separate perturbation sensitivity

All **six** separately logged negative trials preserve their two actual scene hashes and report a **null** test-local point:
- 1 mm and 2 mm finite detectors: measured crossings **[0,0]** each.
- Shifted receiving detector: **[0,1]** (the second hit is retained, not dropped).
- Native TIR at ±50°: **[0,0]**, actual first outcome total-internal-reflection, **zero transmitted and one reflected** branch per run.
- Just below the critical angle: **[0,0]** despite **one actual transmitted** outgoing branch per run. The near-grazing outgoing ray misses the finite receiving window, not a claim of zero transmission.
- ±0.000001° near-parallel pair: actual crossing counts **[1,1]**; hit positions ±0.00000314159265359 mm and incoming transverse components ±2.61799387799×10⁻⁸. The line sine falls below the research conditioning gate, so the point is withheld. The antiparallel control is explicitly **synthetic algebra**, not a native antiparallel event.

The reused #135 tests additionally verify mismatched apparatus/family, duplicate direction, stale and non-opt-in capture, incomplete ray budget and suppression. These are **builder CI** tests whose source and passing lines I inspected, not independent fresh native executions. The old metadata warning-injection test is synthetic provenance plumbing, not a warning emitted by PhyDemo.

Full-Fresnel positive native experiments retain native reflection/transmission observations; in the equal-index controls, reflection is **actually zero**. In the **partialReflection:false** control, actual native transmissions are detected with zero reflected branches, but each run's detector/interface observables remain **qualified** with the explicit *omits Fresnel partial reflections* warning. Both invocation identities and warnings survive the pair-level qualified result. This does not imply full physical power or continuous visibility.

I independently recomputed the post-native hypothetical ±**0.0001 mm** transverse hit-position / ±**0.000001 rad** direction perturbations using the recorded native hit positions and vectors:

| Fixture | One-ray derived-point shift | Paired-ray derived-point shift |
| --- | ---: | ---: |
| Baseline 120/40 mm, ±0.5° | 0.0007646226135 mm | **0.0015291726269 mm** |
| Long 1000/500 mm, ±0.05° | 0.4075930370 mm | **0.8154969919 mm** |

The long-range paired-ray result is **533.29×** as sensitive *under these particular arbitrary post-native perturbations*. These inputs were **chosen hypothetically**, **not measured native coordinate/direction errors**, not uncertainty bars, not a probability distribution and not a physical image blur. An error budget would need independent native-error characterization and appropriate scene-conditioned propagation.

## 4. Exact-head CI and compatibility gates

I enumerated GitHub Actions workflows filtered by the **exact authored SHA**; all **11** final-source pull-request runs are **completed / success / attempt 1**. The synthetic checkout shown in raw Node and Chrome logs is **122c7787**, which was separately verified to have the same tree as authored HEAD.

| Workflow | Final-source run | Conclusion |
| --- | --- | --- |
| Original refraction problem pair | [44265168150](https://github.com/physicsvigilante/opticsim/actions/runs/44265168150) | SUCCESS |
| Planar refraction checks | [44265168184](https://github.com/physicsvigilante/opticsim/actions/runs/44265168184) | SUCCESS |
| Optical composition checks | [44265167963](https://github.com/physicsvigilante/opticsim/actions/runs/44265167963) | SUCCESS |
| Curved mirror checks | [44265168183](https://github.com/physicsvigilante/opticsim/actions/runs/44265168183) | SUCCESS |
| Deterministic planar angular query checks | [44265168057](https://github.com/physicsvigilante/opticsim/actions/runs/44265168057) | SUCCESS |
| Quasi-static source motion checks | [44265167973](https://github.com/physicsvigilante/opticsim/actions/runs/44265167973) | SUCCESS |
| Unified problem workflow checks | [44265167988](https://github.com/physicsvigilante/opticsim/actions/runs/44265167988) | SUCCESS |
| Qualified authoring checks | [44265167978](https://github.com/physicsvigilante/opticsim/actions/runs/44265167978) | SUCCESS |
| Parameter experiment checks | [44265168113](https://github.com/physicsvigilante/opticsim/actions/runs/44265168113) | SUCCESS |
| Numerical ray reliability diagnostics | [44265167970](https://github.com/physicsvigilante/opticsim/actions/runs/44265167970) | SUCCESS |
| Plane-mirror angular inverse checks | [44265167972](https://github.com/physicsvigilante/opticsim/actions/runs/44265167972) | SUCCESS |

The actual [original-pair raw job](https://github.com/physicsvigilante/opticsim/actions/runs/44265168150/job/134667781481) reports **Node v24.19.0**, pinned PhyDemo **811f508d2b070898c241a568b0c167dcb8645251**, built 1,164 headless native modules, and **807 tests / 807 pass / 0 fail / 0 cancelled / 0 skipped**. The 12 copied #135 B research tests plus the **five** new B1b tests have explicit passing lines. The [planar job](https://github.com/physicsvigilante/opticsim/actions/runs/44265168184/job/134667781742) independently repeats its own native/Node24 regression execution, with the same pin/merge identity and **807/807** results.

I inspected actual raw [optical composition/Chrome job #134667780902](https://github.com/physicsvigilante/opticsim/actions/runs/44265167963/job/134667780902): native suite again **807/807**; the existing browser check reports **27 checks / 15 screenshots / Google Chrome 157.0.8103.50**, and existing hosted smoke **5 checks / one screenshot**, both PASS. The separate planar native/browser regression log also has passing planar, circular, prism, polygon and composition checks. These are **unchanged app/browser compatibility regressions**, **not** a B1b numeric visualization or eye-observer UI.

The original first-source 11 workflow conclusions were also independently queried and were **successful on first attempt**; the original 807/807 results remain preserved. There is no hidden final-source failed/queued run to ignore or successful retry to cherry-pick.

## 5. Ranked findings

### P0 — None identified

No critical regression, mismatched tested tree, fabricated native hit or unauthorized product change found within this bounded study.

### P1 — No outstanding blocker for a research-only owner decision

The preregistered 19 positives, 6 negatives and 2 perturbation records are present in actual final-source native CI; the independent calculations from measured hits and outgoing directions agree for all 19 positives. The initial log-label collision was transparently preserved and corrected in a three-line source revision, with new exact-head CI.

### P2 — Nonblocking research limitations; blocking any *future production inference* if unresolved

1. **Numerical error is not calibrated.** Conditional symmetric-pair Snell predictions, slope and determinant intersections, and near-zero line residuals operate on a highly constrained common-data geometry. They validate these cases' arithmetic, not the accuracy of PhyDemo's upstream coordinates/directions nor universal 2D optical images. The 0.02/0.1 mm alarms are *engineering test alarms only*; no statistical/physical confidence interval can be inferred.
2. **The candidate admission domain is not established.** The 1→4 case has backextension/L ≈**3.25**, beyond an earlier speculative unvalidated **2×** public threshold; the 1000/500 mm case exhibits **533×** the chosen perturbation sensitivity. The TIR/near-critical controls only prove appropriate refusals/misses, not reliable **near-critical accepted pairs**. A future contract should separately test asymmetrically sampled outgoing rays, near-equal-index conditioning, actual near-critical *finite detected* rays where physically possible, endpoint-near hits, larger transform magnitudes and validated native-error propagation — or withhold public points. The current research gate **does not authorize** earlier proposed 0.01 line-sine, 0.5 mm clearance or 2× extension display cutoffs; nor is its 1e-4 line-sine / 0.05 mm / 10× research gate a release policy.
3. **Standalone localFrameIntersection() is not a release-ready guard.** Within these tests it is called after validated `nativePair()/derivePair()` or with explicit Fresnel qualification checks, but the helper itself mostly assumes two accessible hit readings and checks nonzero endpoint margin; it does **not** independently revalidate pair/family/qualification, complete native provenance, branch identity or the upstream research 0.05 mm clearance. It is correctly labelled **test-only**. Any production reuse would need unified fail-closed guards and independent review.

### P3 — Evidence hygiene and interpretation

- The issue's **creation** predates CI, but the issue body was updated after CI; the present body is not an immutable original-text snapshot. Source/CI history and the executed matrix are visible. For future preregistration, commit a frozen matrix or link an immutable snapshot before first native run.
- The reused #135 test labels its second suppressed synthetic warning run “complete-other” even though it also sets maxRayDepth=0 (incomplete); a labelling nit, not a physics failure.
- The earlier #135 test harness and the new test-local mathematics have no simultaneous detector/observer or ray-bundle certification. Distinct separately simulated rays passing a **finite segment** prove neither a real eye/pupil nor a unique stigmatic image, 3D depth, viewing comfort, continuous power or textbook solution completeness.
- The zero native crossings are **measured finite detector zeros**, not a proof of globally absent light.

## 6. Independent reviewer versus builder actions

**Independently performed here:** GitHub source/blob/commit/tree/merge/source-scope comparison; full reviewed test source and preserved #135 fixture comparison; preregistration chronology check; reading/parsing exact-source Node24/pinned-native original-pair log and other native/browser raw logs; checking all 11 workflow conclusions; independent plane-local **slope-based** reconstruction from all 19 pairs of *logged actual* native hit positions/directions; independent source-side/backward/endpoint/branch/normal/unit and Snell comparison; recomputation of both baseline and long-range artificial perturbation shifts; inspection of negative native first branches and Fresnel qualification warnings.

**Not independently executed:** any PhyDemo simulation, new Node24 job, local installation/build, fresh browser/Chrome test, non-symmetric optical experiment, physical pupil/eye model or independent error calibration. All **807/807**, **11/11**, and real Chrome results are **builder GitHub CI evidence independently inspected**, not independently rerun by this reviewer.

**Gate consequence:** The owner may decide whether to retain/accept the **research-only** results of #140 and commission a **separate narrowly scoped B1b numerical-admission/refusal design**. This report **does not approve merging #140 or any held PR, public B1b coordinates, B1a geometry changes, physical image claims, native solver changes, a release, or a bypass of [main protection issue #123](https://github.com/physicsvigilante/opticsim/issues/123)**. If the source HEAD or its tested tree changes, obtain new exact-head CI and independent review.
