# Independent R2 physics review — Opticsim PR #120 (Chat B)

**Review date:** 2026-11-17  
**Reviewer:** separate-context AI-assisted technical review; not the implementer and not a human optics expert.  
**Source:** https://github.com/physicsvigilante/opticsim/pull/120  
**Scope:** bounded, unreleased v18 native thick-lens / mirror / centered-gap aperture composition. **No source edits, merges, release, or authorization.**

## 1. Identity, method, and evidence boundary

I independently fetched the PR metadata, Git commit objects, v18 source, v17 inherited validators, tests, workflow steps and native job logs; downloaded and inspected retained source-CI CLI reports and all four real-Chrome screenshots; and independently recomputed geometry and clearances from fixture parameters. I did **not** independently install or execute pinned native PhyDemo, run Node tests, or launch Chrome. All native events and browser results below are **reviewed source-CI evidence, not reviewer-executed native experiments**.

- Actual draft PR HEAD: **1c566103842cc6c4841aa97360cc893b0ed710c4** (open, draft, not merged).
- Actual Git tree (verified from the Git commit object): **d811ad8d026eacf8e15a8403bfc415bca41e2208**.
- Temporary GitHub synthetic main-target CI merge **2447215b1776cdbf72b344d26693a77ccdc4a3ad** has **the identical tree d811ad8d026eacf8e15a8403bfc415bca41e2208**. Its parents are main **d3509e82fb65d81aabe336666851f8f2962623f4** and actual PR HEAD; identity of *tree* does not mean PR #120 was merged.
- Correct current dependency base is held, unreleased v17 PR #116 commit **9157c7a9ba7b21d6c9fe816897612537e45e6b30**. Comparison reports 21 commits ahead, 0 behind, 16 changed files.
- Pinned upstream constant remains **811f508d2b070898c241a568b0c167dcb8645251**. The 16-file source diff changes no vendor/native solver, adapter, observation arithmetic, historical v17/v4 validation module, scene execution core, or source-to-ray controller.

The user-specified [REQUEST](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-120/REQUEST.md) and [v18 scope](https://github.com/physicsvigilante/opticsim/blob/1c566103842cc6c4841aa97360cc893b0ed710c4/docs/NATIVE-THICK-LENS-APERTURE-V18.md) were read in full. Review assumes the explicitly restricted 2-D geometrical ray scope, **not** wave optics, energy calibration, image detection or full physical optical verification.

## 2. Independently computed geometry (mm)

From [the fixture](https://github.com/physicsvigilante/opticsim/blob/1c566103842cc6c4841aa97360cc893b0ed710c4/examples/native-thick-lens-aperture-v18.json), aperture A1 is at x = −150, total length 100, centered opening 20, orientation +90°:

| State | Outer endpoint y | Gap endpoint y | Opaque arm intervals y | Right-going S1 ray y = 0 |
|---|---|---|---|---|
| A1 center (−150, 0) | −50, +50 | −10, +10 | [−50, −10] and [+10, +50] | Through open gap |
| Only A1 center moved to (−150, +30) | −20, +80 | +20, +40 | [−20, +20] and [+40, +80] | Absorbed at (−150, 0) |

At orientation −90° the endpoint ordering reverses (outer +50, −50; inner +10, −10 for y=0), but the **same two physical arms and central opening** remain; no new ray physics is implied. The independent forward-line intersection S1=(−200,0), direction (1,0) with x=−150 is exactly (−150,0). This supplies an expected crossing/absorption location only; I have **not constructed or substituted any ray path** for PhyDemo.

Both lenses have 100-mm aperture height, 30-mm center thickness, radii 100 mm. Independent stable sagitta calculation gives 2500/(100 + sqrt(7500)) = **13.3974596215561 mm** per face, hence finite edge thickness **3.20508075688773 mm**, greater than 1 mm. Whole-body x envelopes: **L1 [−15,+15]**, **L2 [+135,+165]**, separated by **120 mm**. The baseline stop is 135 mm to the *near edge* of L1 and 285 mm to the near edge of L2. A1 x-plane to D1 (x=−100) is 50 mm; to vertical mirror M1 (x=+300) is 450 mm; S1 is 50 mm from the stop plane. All comfortably exceed 0.01 mm. Lenses have explicitly common exterior n=1; their unequal interior indices 1.5 and 1.3 do not violate that rule. A straight on-axis incidence is normal to spherical center vertices; an eventual retroreflection is physically plausible without supplying any itinerary.

## 3. Source code admission / isolation assessment

I inspected [new v18 validator](https://github.com/physicsvigilante/opticsim/blob/1c566103842cc6c4841aa97360cc893b0ed710c4/src/thick-lens-aperture-composition.js), [composition registry](https://github.com/physicsvigilante/opticsim/blob/1c566103842cc6c4841aa97360cc893b0ed710c4/src/composition-profiles.js), contract and authoring modules, inherited v17/v15/v4 finite geometry, PhyDemo adapter, native observations and qualification/evaluation pipeline.

**Verified in source:**

1. **Whole-system admission:** v18 requires exactly 2 spherical lenses, 1 plane mirror, 1 finite aperture, 1–4 native single-ray sources and 0–2 detectors. Other optics, extra stops, a third lens, tilted stop and mismatch of exterior media fail. Version-selection precedence does not silently relax this by falling back to v17. v18 only admits aperture as an explicitly version-whitelisted type; old saved v17 does not.
2. **Validation-only views:** v18 strips the stop **only in the argument to** unchanged v17 validator; v17 strips mirror **only in the argument to** unchanged v15 full lens-train validator. The general-optical rule is dispatched on a lens-excluded subset and checks the original finite-aperture arms/mirror/source rules. The original detector rule still checks sources, optical surfaces and detectors. None of these filters changes the authoritative canonical component list or native compilation.
3. **Whole-body x separation:** all four actual stop endpoints must be finite and within ±10000 mm. The stop must be entirely left or right of each spherical-lens x envelope by at least 0.01 mm. Every endpoint of mirror/detector full finite segments must lie on one side of x=A1.x by at least 0.01 mm (even with remote y). Test examples x=−15.005 against L1 left −15, source x=−150.005, and mirror/detector x=−150.005 at remote y are rejected; stop x=−15.011 is geometrically admitted, without claiming any numerical ray certificate.
4. **Initial-ray guards:** sources require at least 0.01 mm stop-plane separation. A source's initial forward ray is rejected when its perpendicular distance to any of four actual arm/gap endpoints is ≤0.01 mm and forward dot product is positive. Near-vertical initial rays with |cos(direction)| ≤ 1e−8 are refused. This is deliberately *not* a check on second/later refracted rays, and 0.01 mm is not a binary64 accuracy proof. ±90° produces the same physical stop geometry and different endpoint ordering.
5. **Native ownership:** the unchanged adapter compiles the stop as one native **Aperture** with p1/p2 outer and p3/p4 inner points, plus unchanged native **SphericalLens**, **Mirror**, **Detector**, **SingleRay**. The reused native blocker wrapper delegates to original onRayIncident exactly once, counts only returned isAbsorbed=true and records invalid reports as errors. No validation module injects an intersection, manufactured endpoint, route or absorption.
6. **Budget and results:** v18 defaults to explicit native-deep-v18 (density 0.2, depth 16, ray limit 10000); v17 native-deep-v17 is nontransferable and older v1–v16 depth remains capped at 8. Source-native diagnostics and same-scene hash + executionPassed + completed-status result gate withhold requested measurements on stale, stopped, failed, truncated, undefined or otherwise incomplete runs. Detector hits/callback order remain sampled observations without a guaranteed source ancestry or image.

**Adversarial static review:** The whole-plane exclusion catches stop/lens overlaps even when aperture y is moved far away; similarly it blocks a mirror/detector segment with separated y but x near the stop. An initial ray through y=+10 (opening corner), a nonvertical 45° stop, a source nearly on the stop x-plane, an extra stop/lens, and a nonshared exterior medium are rejected by the relevant paths. A right-going on-axis ray through the gap and the −90° reversal are admitted. I found **no confirmed physically unsafe admitted counterexample** within the documented v18 bounded geometry from this source inspection. This statement is not a proof for all admissible binary64 scenes or all secondary ray/corner encounters.

## 4. Actual source-CI evidence, not independent re-execution

The pinned-head GitHub Actions query returned **all 11 standard workflows completed successfully**. The three required log/run IDs were checked:

| Evidence | Directly inspected outcome |
|---|---|
| [Unified CI 44081491509](https://github.com/physicsvigilante/opticsim/actions/runs/44081491509), job 134032930678 | 852 tests / 852 passed / 0 failed; native transparent and absorbing event logs |
| [Optical composition 44081491553](https://github.com/physicsvigilante/opticsim/actions/runs/44081491553), job 134032931215 | 852 passed; v18 public CLI logged **6/6** cases passed |
| [Chrome / planar 44081491729](https://github.com/physicsvigilante/opticsim/actions/runs/44081491729), job 134033079106 | 852 passed; browser v18 script logged **13/13** checks passed |

Other eight successful source-head workflows cover original refraction, mirror angular inverse, source motion, curved mirrors, numerical reliability, parameter experiments, deterministic angular queries and qualified authoring. No observed non-success result was relabelled success.

**CLI artifact inspection:** downloaded source-CI artifact **llm-authoring-evidence** (artifact 14326194911); read six input/report/native-evidence entries and the acceptance manifest. They show, respectively:

| Fixture case | Native | Emitted / processed | Truncation | Seven requested results |
|---|---|---|---|---|
| clear-opening | completed | 1 / 12 | 0 | qualified; L1=4, L2=4, M1=1, D1=2, A1=0; two face-event objects |
| opaque-arm (A1.y=30 only) | completed | 1 / 1 | 0 | qualified; L1=0, L2=0, M1=0, D1=0, A1=1 |
| all-objects-missed (S1 direction=80°) | completed | 1 / 1 | 0 | qualified sampled zero observations |
| depth8-incomplete | incomplete | 1 / 9 | 0.5 | **all seven suppressed, value=null** |
| full-fresnel-incomplete | incomplete | 1 / 32 | 0.06506578033327412 | **all seven suppressed, value=null** |
| aperture-inside-glass | not-run | 0 native calls | n/a | seven unavailable; no portable scene |

The native clear test log contains event IDs **D1,L1,L1,L2,L2,M1,L2,L2,L1,L1,D1**, while opaque-arm log contains native event **A1** at **(−150,0)** with **outgoing: []**. Source-CI diagnostics recorded truncation=0, undefinedBehavior=0 and no native errors for both completed examples. These sequences come from retained native event evidence; the independent geometry calculation above does **not** generate or assert a ray route. Incomplete CLI cases still retain a **scene/assumptions-only qualified-scene package**, but have no qualified measurement values; the distinction is important.

**Browser artifact inspection:** downloaded [planar / Chrome run](https://github.com/physicsvigilante/opticsim/actions/runs/44081491729) artifact **planar-refraction-evidence** (14327677064); inspected the v18 report, qualified JSON export/reopen and **all four actual screenshots**: two-thick-lenses-aperture-clear, aperture-stops-before-lenses, aperture-mirror-miss, aperture-lenses-all-miss. Report records real Chrome **13 passing checks**, no runtime errors, source/lens/mirror/aperture edits, invalid glass overlap hiding previous values, real native retracing, qualified export/reopen retaining edited L2 inside index 1.4 and A1 opening length 30, and no nonlocal HTTP(S) requests. Screenshots show the expected qualitative on-axis passage, stop absorption, mirror miss, and all-object miss. They cannot certify geometrical intersection accuracy or a PSF/image.

**Test quality / scope:** the feasibility probe adds a native Aperture to a *test-only* v17 scene and verifies old v17 canonical admission still refuses it. Final v18 test exercises no-path, off-axis miss, two simultaneous sources (one blocked / one through), −90° reversal, stop between lenses, near-margins, invalid extra objects and deep-policy isolation. The public CLI uses the normal runProblemEvidence path, an actual native executor and preserved input hashes, with no repairs or external model calls. The browser script uses Chrome DevTools over a local origin rather than a mocked page.

## 5. Historical failure and freeze provenance

The original failures are real and retained, rather than silently replaced by only the final green run:

- Commit **8b32ebf8c98932b4c75b8872bccb42739035b6d9**, [unified run 44080987055](https://github.com/physicsvigilante/opticsim/actions/runs/44080987055): **844/852 passed, 8 failed**. Causes included missing v18-specific aperture type admission and the old frozen v17 viewer SHA assertion.
- Commit **4f6c2f115391b54b9df699fc960e59a115c05113**, [optical run 44081294321](https://github.com/physicsvigilante/opticsim/actions/runs/44081294321): **850/852 passed, 2 failed**. The historical viewer SHA check and a test-side wrong inspector field remained.
- Commit **6d4a69ae27c2102b682da5d79b630a059c7a5835**, [unified run 44081375622](https://github.com/physicsvigilante/opticsim/actions/runs/44081375622): **851/852 passed, 1 failed**; the old test-side use of absent absorbed property persisted until final commit switched to **outgoing: []**. This additional near-final failed attempt is also preserved.
- At final HEAD all 852 pass; the original independent source-CI native absorption observations predate the final test fix, so they were not invented by its corrected assertion.

Original **test/fixtures/detector-hit-transfer-freeze.json** has identical Git blob **d7aee36a9047330f1227b992dc75cf0b491ba7da** at v17 base and v18 HEAD. The prior **two-thick-lens-mirror-app-postfreeze-v1.json** has identical blob **1458bc01eaf13ab3a110fe859fe777f33c79c6d8** at both. The v17 app blob **9d447af4c8fc59ec1e8fdcfbcec0c4d739fc477f** and new v18 app blob **cfbea455df3f7ea7a30002d0139730c25b235d32** match the added postfreeze manifest. Its v18 app SHA-256 is **99329f4e3ce49a8b4c6b3bba4343f9d7e519e2eaab3374af9105b688c01cae7b** and is checked by source-CI. The previous freeze input and prior postfreeze record were **not rewritten**. This v18 extension is post-exposure test evidence, not an independently blind reproduction.

## 6. Findings ranked by decision impact

**Blocking defects: none confirmed** in the reviewed, isolated v18 source/contract and retained evidence. Clearance below is scoped to an owner's decision, not an authorization or certification of every possible ray geometry.

**N1 — Nonblocking coverage / independent replication limit (medium).** No fresh reviewer-executed pinned PhyDemo or Chrome. The verified native and browser outcomes are builder/source-CI; my independent work is code/artefact scrutiny and scalar recomputation. For more physical confidence, independently rerun the six public cases and one browser edit cycle on the exact commit, retaining new evidence under a separate reviewer identity. This is an evidentiary limitation, not a newly observed physics failure.

**N2 — Nonblocking secondary-ray boundary coverage (medium).** A source's initial ray near all four stop endpoints is guarded, but a later refracted/reflected ray can approach a gap or arm endpoint at extremely small clearance, and the 0.01-mm admission distance is not a proven upstream intersection uncertainty bound. Reproducible follow-up: add a deliberately off-axis source aimed through L1 at a stop **between** the lenses; sweep its direction so the *native-returned* refracted ray approaches each inner corner from both directions. Verify terminal status and suppress any undefined/truncated observations rather than deciding passage in the validator. Repeat at ±90° stop orientation and near ±10000-mm coordinates. This is explicitly out of the current universal-certification claims, not a demonstrated admitted wrong ray.

**N3 — Nonblocking sampling/extrapolation coverage (low-to-medium).** On-axis complete return, simple two-source mixture, and four screenshots do not establish all 1–4-source possibilities, Fresnel branch power completeness, diffraction or an image. Reproducible next tests: 3–4 sources at distinct launch angles, both lens indices changed, stop at several admissible x locations, 0/2 detector configurations, near outer rim and gap edges, and both full-Fresnel and transmitted-only modes. Assert event/callback provenance and withholding when incomplete; never assert a route that the native solver has not chosen.

**N4 — Nonblocking editorial ambiguity (low).** The v18 example's interpretation assumptions still contain the historical sentence about **native-deep-v17**, alongside the correct v18 sentence. It is not active simulation input, and it did not cause a false result, but should be clarified to avoid teaching the wrong policy. Fix only in a separately reviewed follow-up, without altering frozen evidence.

**N5 — Nonblocking handoff wording (low).** The CLI writes a qualified *scene bundle* before an incomplete native run and correctly suppresses all requested measurements afterward. The word “qualified” in a saved scene filename could be misconstrued as a qualified optical result by external consumers. Document explicitly that bundle integrity/scene provenance is **not** native-result qualification. No false measurements were observed in the stored depth8 or Fresnel reports.

## 7. Numerical and educational limits

The 0.01-mm x, corner and endpoint thresholds are **admission rules**, not machine-precision error estimates. Native binary64 intersection near later corners, rims, tangencies, high-index critical angles and simultaneous encounters is not universally proven by the tested fixtures. The 16-depth budget permits the sampled mirror return, not arbitrary Fresnel-tree or all-power completeness. Transmitted-only partialReflection=false is a qualified approximation; native TIR can still occur. Detector counts and signed-relative-power samples are neither watts nor a continuous footprint and have no individual source attribution for this model. A count of zero is **not** a continuous shadow or proof of zero light. No PSF, wave diffraction, image plane, image reconstruction, unique source-to-detector ray route or original textbook-answer correctness is certified.

## 8. Verdict

**CLEARED FOR OWNER DECISION**

Basis: expected source/tree and prerequisite identities were independently verified; geometry checks and version isolation are coherent; source diff delegates all actual intersections and absorption to unchanged pinned PhyDemo; all specified source-CI logs, raw six-case report outcomes, Chrome report and four screenshots agree; historical failures and frozen provenance are preserved; no confirmed blocking defect was found in the bounded v18 scope. This is a **limited AI-assisted independent review** based on source and retained CI, **not** independently rerun native/Chrome physics, not a claim to be a human optics specialist, not a PSF/image certificate and **not permission to merge or release**.

Held v14 **#107**, v15 **#110**, v16 **#113**, v17 **#116**, research-only **#119**, independent detector-footprint **#118** and candidate **#120** remain unmerged unless the owner separately authorizes the relevant dependencies and release gates.
