# Chat B independent JEE planar + native v19 integration review — Opticsim PR #164

**Date:** 18 November 2026  
**Verdict: CLEARED FOR OWNER DECISION**, strictly for the **review-only, draft, unmerged** PR #164 candidate below. **P0: none identified. P1: none identified.** Two nonblocking regression-hardening opportunities and a mandatory release-safety hold are recorded below. **Do not merge, deploy or release.**

This is a scoped independent review of the **new combined-tree integration boundary**, not a fresh re-review of unchanged source families. I inspected GitHub Git objects and source/tests, decoded exact-checkout builder CI logs, and independently recomputed optical geometry. **I did not execute Node, pinned PhyDemo or Chrome locally and did not inspect the browser PNGs.** The builder's genuine native results are attributed to its CI, not to an independent reviewer execution.

## 1. Frozen identity, ancestry and literal source-blob comparison

- [Draft Opticsim PR #164](https://github.com/physicsvigilante/opticsim/pull/164) HEAD **`58ec0c237950d71e7b93b9b1639a52ada243e262`**, Git source tree **`f371366765c8aa96029a0b29d6ae3f770e9b0eb2`**.
- Independently fetched the Git **commit** object, which has **one parent**, production main **`d3509e82fb65d81aabe336666851f8f2962623f4`**. This is not a merge of either held original PR.
- Independently fetched GitHub Actions synthetic merge **`fae01061165da6f9c1113caeff0d9404595da1df`**: **identical** source tree `f3713667...`, ordered parents **[production main `d3509e82...`, exact PR164 HEAD `58ec0c23...`]**. Both inspected CI checkout logs explicitly fetched/checked out `fae01061165da6f9c1113caeff0d9404595da1df`, not an unrelated branch head.
- Fetched full nontruncated **recursive raw Git trees** for combined, reviewed planar, reviewed native beam and production base: respectively **653, 641, 638 and 628 entries**. Comparing *blob SHAs* relative to the same base established:
  - [PR #161](https://github.com/physicsvigilante/opticsim/pull/161), HEAD `09ad081a34ced0fa969affc1bf54766cabffb04a`, reviewed source tree **`1b2caf6186c8eaf678963238d2292001b2fa9667`**: **13/13 changed-file blobs identical** in PR164.
  - [PR #141](https://github.com/physicsvigilante/opticsim/pull/141), HEAD `6d6d6b213fedb6f028cd1ffef241aef239d37c62`, reviewed source tree **`39884a78ec265a77dc18877a838b937103998160`**: **18/18 changed-file blobs identical** in PR164.
  - **31/31 unchanged**, **zero common changed paths** between the sources, zero missing source paths. Exactly two extra paths: `docs/JEE-PLANAR-PARALLEL-V19-REHEARSAL.md` (blob `802d7bdac46a7bb90d9152a16dc0de628dcc6c68`) and `test/jee-planar-parallel-v19-integration-rehearsal.test.mjs` (blob `fda9d37120dc041c92a1580e335b561fd12b4a35`).
  - Main-to-PR164: exactly **33 changed paths, 25 additions, eight existing modifications, zero deletions**. The eight existing changes are precisely `.github/workflows/opticsim-ci.yml`, `src/adapter.js`, `src/app.js`, `src/authoring.js`, `src/composition-profiles.js`, `src/contract.js`, `src/observables.js` and `test/composition-profiles.test.mjs`; all eight are byte-identical to reviewed PR141.

The preceding independently cleared source reviews remain separately scoped: [planar PR161 review](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-161/reviews/review-01-chat-b.md); [native v19 PR141 review](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-141/reviews/review-01-chat-b.md). Old adverse verdicts on older SHAs remain accurate.

## 2. Cross-feature versions, admission and evidence isolation

Inspected `src/composition-profiles.js`, `src/contract.js`, `src/authoring.js`, `src/adapter.js`, `src/observables.js`, `src/app.js` and their changed patches on the **combined** tree.

- The new v19 composition profiles accept **exactly one `parallel-beam`** in a bounded lens/aperture **or** planar-slab model. Profile selection checks Beam first, but actual whole-system count/rule validation rejects unsupported mixing, including point sources and cross-family lens/media combinations. The type gate allows Beam only at schema v19. v5 SingleRay/PlaneGlass and its native witness are **not reinterpreted as Beam**; v14–v18 remain separate/held.
- Authoring adds Beam width and explicit heading, and browser labelling distinguishes deterministic native parallel emission. Existing older source emission modes are not broadened. `src/adapter.js` registers `compileParallelBeam` while keeping the original point-source compiler; source sampling instrumentation now counts actual emission for either allowed source type.
- `src/observables.js` permits `source-emissions` for either `point-source` or `parallel-beam` without changing the result kind. Results are tied to a canonical scene digest, successful execution and completed native state. A missing/unmatched detector hit-event list is unavailable, not manufactured; native callback positions have count matching, finite geometry and an event-list bound. Native warnings qualify readings rather than silently proclaiming unqualified evidence; incomplete, stale and error cases do not become complete hits.
- The two **standalone planar analytical** modules/CLIs are unchanged source blobs; their native field is always `{status:'not-run',observations:null,...}`, and virtual-axis points are conditional calculations. They have no implicit adapter invocation or common v19 observable record that could promote predictions to measurements.
- The **separately authored** v5 native SingleRay witness (unchanged and executed by builder CI on the combined tree) still reported `JEE_OBSERVER_NATIVE_WITNESS` with real measured detector arrival at approximately **(100,40) mm**. Exact-source builder logs also include `JEE_OBSERVER_NATIVE_REAL_ZERO_CONTROLS` (two *other* genuinely run scenes) and distinct synthetic/injected event-integrity matrices; the latter do **not** constitute native optical observations.
- The integrated test does **not** construct a single physical system containing both the v5 SingleRay and v19 Beam. This is correctly a **codebase coexistence** and evidence-isolation check, not certification of an arbitrary mixed apparatus or a native image.

**Conclusion:** no source-to-observable contamination or new v5/v19 schema admission conflict was identified.

## 3. Genuine native Beam evidence, not an artificial route

The v19 compiler [`src/parallel-beam.js`](https://github.com/physicsvigilante/opticsim/blob/58ec0c237950d71e7b93b9b1639a52ada243e262/src/parallel-beam.js) maps the explicitly authored finite width and direction to a PhyDemo **`type:'Beam'`**, converting the world y-up endpoints to native y-down. Its deterministic `parallelBeamSamples` computes only expected *initial emission positions for admission/endpoint safety*; it does **not** synthesize propagated rays or detector crossings. The actual emitter, lens encounters, finite-aperture absorption and detector incidents are delegated to pinned native PhyDemo.

The new combined test loads `examples/jee-parallel-lens-v19.json`: Beam at x=−100 mm, width 40 mm, native density 0.2, finite 12-mm opening at x=−50 mm, ideal f=+100 mm lens at x=0 mm and passive detector at x=+100 mm. The deterministic eight initial transverse midpoint positions are **±17.5, ±12.5, ±7.5 and ±2.5 mm**. At the upstream stop only ±2.5 mm lies inside its ±6-mm central opening. Thus **eight emitted, six absorbed, two surviving detector crossings** is a physically consistent forward test. For the ideal thin lens, the two surviving parallel rays converge to y≈0 at x=100 mm.

Crucially, the combined test reads `evaluateDocument` on the prepared v19 canonical scene, obtains **native status completed**, and reads `evaluateObservables` with `detector-hit-events`. It checks **two finite real native callback positions** at (100,0) mm and `method:'native-hit-event-observation'`, matching detector crossing counters. The native detector observer snapshots inputs *before* calling the original native callback, delegates exactly once and does not relocate any light ray. Observed native hits are not per-source ray ancestry, a continuous irradiance measurement, a PSF or a physical/eye-perceived image.

The new test independently invokes an observer-side *analytical* query and confirms that this query remains `native.status='not-run'`, with no native observations or image detection. A genuine Beam detector hit must never be re-used as native evidence for that unrelated calculation.

## 4. Signed-angle A→B comparison and independent calculation

The [new rehearsal test](https://github.com/physicsvigilante/opticsim/blob/58ec0c237950d71e7b93b9b1639a52ada243e262/test/jee-planar-parallel-v19-integration-rehearsal.test.mjs) covers **5 oriented normals** (0°, +90°, −90°, 180°, 37°), **both tangent signs** and **three units** (mm, cm, m), giving **30 explicit comparisons**. It passes the source-to-observer contract B's **signed** incident angle into standalone contract A's finite-angle query and checks first mathematical crossing, transmitted angle, conditional apparent depth and world-frame axis intercept. Both outputs remain **analytical not-run** and `nativeImageDetected:false`. The original input is asserted unchanged.

I independently solved the stationary-path Snell equation in a local normal/tangent frame for source depth 60 mm, observer normal distance 100 mm, **negative** transverse offset −40 mm, n_source=1.5 and n_observer=1.0, then rotated the frame by 37°:

- Local negative crossing tangent coordinate **−11.246155771209231 mm**; local Snell residual approximately **−5.55 × 10⁻¹⁷**.
- **Incident angle −10.6161089413°**, **transmitted angle −16.0419777084°**.
- Rotated actual *mathematical crossing*: **(6.7681054958, −8.9815793504) mm**.
- Conditional apparent-axis depth **39.11183381855 mm**; world apparent point **(−31.2360993506, −23.5380891750) mm**.
- Distinct paraxial-limit depth **40 mm**, which must not be substituted for the finite-angle result.

For the positive transverse sign the angles and signed crossing reverse while the apparent depth and normal-axis virtual point stay invariant. This independently supports the claimed cross-contract equality; it is **not** a native ray or image reconstruction. The 30 fixtures test shared inputs and one index/depth family; they do not establish universal inverse-geometry coverage.

## 5. Strict post-lens aperture refusal and signs

The retained corrected native validator refuses a stop **downstream of an ideal lens that is forward of the beam** when the three authored signed separations are strictly positive:

`(lens.x-source.x)*direction.x > 0`; `(stop.x-source.x)*direction.x > 0`; `(stop.x-lens.x)*direction.x > 0`.

This uses topology sign **>0**, not **>0.01**, because the separate physical-clearance checks admit their 0.01-mm equality. A source at x=0, lens at x=+0.01, stop at x=+50, rightward Beam satisfies every signed check. For reverse +180° or −180°, a translated source x=64, lens x=63.99, stop x=14, direction.x=−1 also gives all three **positive** signed products; translating avoids a separate binary64 endpoint-jitter clearance artefact near ±π. An upstream aperture has negative stop-to-lens signed separation and is not incorrectly refused.

Independent physical counterexample: an initial sample at y=17.5 mm encounters a forward ideal lens at x=0.01 mm with f=100 mm. Its thin-lens downstream height at x=50 mm is `17.5*(1-49.99/100)=8.75175` mm, **exactly** the half-opening of a 17.5035-mm post-lens stop. The emitted straight sample at y=17.5 mm is not at that corner. Consequently initial-sample clearance alone does **not** qualify the downstream refracted corner, and conservative unconditional rejection is appropriate. The combined test directly checks post-lens rejection; the unchanged v19 secondary-route tests exercise 17.46/17.50/17.54-mm openings, source/lens and lens/stop around 0.009/0.010/0.011 mm, reverse headings and positive native **pre-lens** controls.

**Conclusion:** no new gap in the reviewed conservative post-lens policy was found.

## 6. Exact combined builder CI provenance and limits

Queried exact HEAD's workflow runs and decoded job logs. **Eleven distinct workflows, all completed SUCCESS**. Both examined jobs checked out the verified synthetic merge **`fae01061...` with the identical Git tree**:

- [Optical composition run #44344350702](https://github.com/physicsvigilante/opticsim/actions/runs/44344350702), job **134942601780**: **860 Node tests, 860 passed, zero failed**; actual `JEE_PARALLEL_BEAM_PUBLIC_ACCEPTANCE` **7/7** cases with **4 completed pinned-native runs**, one intentionally incomplete and two refused; **real-Chrome v19 11 checks/6 screenshots**; standard browser acceptance **27 checks/15 screenshots** and hosted smoke **5 checks/1 screenshot**, Chrome **157.0.8103.50**. Browser evidence artifacts were uploaded; I did not inspect their PNG contents.
- [Plane-mirror run #44344351018](https://github.com/physicsvigilante/opticsim/actions/runs/44344351018), job **134942602796**: exact merge checkout, **860 Node tests**, passing markers `JEE_PLANAR_V19_ANALYTIC_CROSS_CONTRACT` (**30**) and `JEE_PLANAR_V19_NATIVE_COEXISTENCE` (**8 emitted/6 absorbed/2 actual native detector hits**); `V19_POST_LENS_STOP_REFUSAL` and `V19_PRE_LENS_STOP_ALLOWED`. Native SingleRay positive and separately genuine zero controls remain present.
- [Planar refraction run #44344350795](https://github.com/physicsvigilante/opticsim/actions/runs/44344350795) also SUCCESS, as did the other eight workflows. Separate PR161 and PR141 CI histories were **not** substituted for combined-tree evidence.
- Workflow source comparison shows the v19 native acceptance and real-Chrome steps added to the optical-composition workflow; older required Node, browser, smoke and other optical acceptance steps were retained. The held CI-trigger PR #162 was not incorporated.

**Provenance qualification:** A complete matching scene digest ties the observation to its authored canonical source and run; it does not cryptographically prove real-world light or turn fabricated negative-case records into native evidence. The actual native detector-hit control is distinguishable from classifier mutation tests. This reviewer relied on the builder's pinned-native/Chrome executed CI and **did not independently rerun that environment**.

## 7. Findings, nonblocking opportunities and mandatory hold

- **P0: none identified.**
- **P1: none identified.** No source collision, incorrect schema promotion, fabricated detector evidence, mixed v5/v19 apparatus admission or corner-refusal bypass was identified for this exact bounded integration.
- **N1 (nonblocking, integration regression hardening):** Add a single explicit combined-tree negative test that a v19 Beam cannot be used as the v5 native witness's SingleRay/point-source apparatus, plus a positive v5 witness status assertion adjacent to the v19 coexistence assertion. Existing separate v5 and v19 tests already passed together; this is to make the future isolation intent even more visible, not to repair an observed failure.
- **N2 (nonblocking, mathematical regression breadth):** The new 30-case cross-contract matrix rotates/sign-flips/rescales one fixed geometry and index pair. Future bounded tests could vary indices, normal distances, translation and near-axis/critical-boundary withholding. This is optional hardening; it does not undermine the present independent signed-arithmetic cross-check.
- **Mandatory release hold (not a newly found code P1):** Queried production [`main`](https://github.com/physicsvigilante/opticsim/tree/main), still at **`d3509e82fb65d81aabe336666851f8f2962623f4`** with GitHub `protected:false`; [release-safety issue #123](https://github.com/physicsvigilante/opticsim/issues/123) remains **OPEN**. PR #141 and PR #161 were directly checked **open, draft and unmerged**. An explicit **separate owner decision and effective release/branch-safety controls** remain prerequisites to *any* production integration. The synthetic CI merge is not a production merge.

**Final verdict: CLEARED FOR OWNER DECISION**, for **PR164 HEAD `58ec0c237950d71e7b93b9b1639a52ada243e262` / tree `f371366765c8aa96029a0b29d6ae3f770e9b0eb2` only**, as an **isolated review-only rehearsal**. It does **not** authorize merging PR #164, #161, #141 or any related held PR; certify v14–v18, detector footprint, perceived image/continuous light, or arbitrary mixed systems; or change any earlier review's historical verdict. No Opticsim source, PR, deployment or release was altered by this review.
