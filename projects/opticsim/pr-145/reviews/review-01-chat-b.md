# Independent R1 — Opticsim PR #145: observer-anchored native refraction feasibility

**Review date:** 2026-11-18  
**Reviewer:** Chat B — independent exact-Git-object, source, physical-equation and builder-CI-log inspection  
**Verdict: CHANGES REQUESTED** — one reproducible **P1 numerical-reference robustness defect** in the test-only bisection helper. The demonstrated optical sample and native-forward feasibility are valid; this is **not** a discovered PhyDemo optics defect or a request to change released production code. No merge or release is approved.  
**P0:** none. **P1:** R1 below. **Nonblocking:** N1–N4.  
**Execution provenance:** I independently evaluated the scalar mathematics with Python/SciPy and high precision, and reproduced the floating-point edge with a small standalone Node.js calculation. I **did not** run the Opticsim test suite, pinned PhyDemo simulator, or Chrome independently. All native/browser test executions cited below are **builder GitHub Actions**.

## 1. Pinned identity and untouched production scope — VERIFIED

- [Draft Opticsim PR #145](https://github.com/physicsvigilante/opticsim/pull/145) is **open, draft, unmerged** at review.
- Production-main base: `d3509e82fb65d81aabe336666851f8f2962623f4`.
- Exact research HEAD: `a2d0adfe692bc837656a4dd09edc84ab4f490d2f`.
- Exact HEAD **Git tree**, read from Git commit object: `c9333564591b165c22246f67fbc4fa47c5462d11`.
- Synthetic CI merge commit `e1a2f163efd1d121912c84c71a874cb878914930` has **the same Git tree**, and exact parents **in order** `[d3509e82fb65d81aabe336666851f8f2962623f4, a2d0adfe692bc837656a4dd09edc84ab4f490d2f]`. Verified from the Git *commit objects*, not PR description.
- GitHub comparison is **2 ahead, 0 behind**, merge base equals production main. Diff contains exactly **two additions, 270 lines and zero deletions**: [test/jee-observer-native-feasibility.test.mjs](https://github.com/physicsvigilante/opticsim/blob/a2d0adfe692bc837656a4dd09edc84ab4f490d2f/test/jee-observer-native-feasibility.test.mjs) (221 lines), and [docs/JEE-OBSERVER-REFRACTION-NATIVE-RESEARCH.md](https://github.com/physicsvigilante/opticsim/blob/a2d0adfe692bc837656a4dd09edc84ab4f490d2f/docs/JEE-OBSERVER-REFRACTION-NATIVE-RESEARCH.md) (49 lines).
- **No** production `src/`, canonical schema, pinned `vendor/`, adapter, browser, CLI, or already-reviewed held PR files changed. PR #144's separately reviewed explicit-angle analytical feature is not stacked into #145 and its approval is not inherited.

Reviewed these two added files and the unchanged underlying `src/adapter.js`, `src/planar-media.js`, `src/native-observations.js`, `src/observables.js`, `src/contract.js`, `src/authoring.js`, `scripts/author-scene.mjs` and `skills/sim-ro-image-to-scene/scripts/check-scene.mjs` at the HEAD.

## 2. Independent optical calculation — sample CONFIRMED

For a plane represented by point `P`, source-to-observer unit normal `n`, CCW tangent `t=(-n_y,n_x)`, source `S` on the **negative** side and observer `O` on the **positive** side, let `d_s=-(S-P)·n>0`, `d_o=(O-P)·n>0`, `u_s=(S-P)·t`, `u_o=(O-P)·t`, and `Q=P+q t`. The optical length is

`L(q)=n_s hypot(d_s,q-u_s) + n_o hypot(d_o,u_o-q)`.

The stationary condition is

`F(q)=n_s (q-u_s)/hypot(d_s,q-u_s) - n_o (u_o-q)/hypot(d_o,u_o-q)=0`.

`F'(q)=n_s d_s²/[d_s²+(q-u_s)²]^(3/2) + n_o d_o²/[d_o²+(u_o-q)²]^(3/2)>0` for positive distances and indices. Endpoint signs bracket exactly one root between `u_s` and `u_o`, including the collapsed `u_s=u_o` axial case. This proves **one stationary path for one infinite planar boundary and two finite points**; it says nothing about several interfaces, obstacles or visibility. The construction is rotation/translation invariant because it uses projections onto `n,t`.

Independent SciPy root and direct trigonometry for `S=(-60,0)` mm, `P=(0,0)`, `n=(1,0)`, `O=(100,40)` mm, `n_s=1.5`, `n_o=1`:

| Quantity | Independently recomputed |
|---|---:|
| `q = Q_y` | `11.24615577120923 mm` |
| Initial source heading / incidence | `10.616108941304953°` |
| Refracted angle | `16.041977708350927°` |
| `1.5 sin(i) = sin(r)` | `0.27634154941118017` |
| Forward intersection at `x=100` | `(100,40) mm` |
| Conditional axis depth `(q-u_s)d_o/(u_o-q)` | `39.11183381854949 mm` |

These agree with the recorded builder-native first-event angles and detector hit `(100.00000000000001,40)` mm. With the sole observed nonaxial outgoing direction, this depth is the **mathematical intercept of a backward-extended ray with the source-normal axis**, not a real optical image. For exactly axial `u_o=u_s`, the code correctly returns `null` for one-ray depth inference; the separate paraxial limit would be `d_s n_o/n_s=40 mm` for these indices, not an observed image.

The ±40 mm observer offset, 1→1 and reverse 1→1.5 contrast, 90°/180° rotation, and translated/tangentially shifted case use consistent oriented-normal signs. The documented shifted plane representative point differs in tangent coordinate from the source/observer translation, which is legitimate for an **infinite** plane: moving `P` along `t` does not change the physical interface.

## 3. Native evidence — actually measured vs derived

The test-only solver computes `Q` and **explicitly authors** `directionDeg=atan2((Q-S)_y,(Q-S)_x)` into canonical **v5** `single-ray` source `S1`. The standard adapter compiles it to pinned native `SingleRay`; `I1` is native `PlaneGlass` with positive/negative material index ratio, and `D1` is native passive finite `Detector`. Native PhyDemo is then responsible for all forward ray propagation; the test does **not** prescribe a native ray itinerary, send a reverse ray, or run an image solver.

The verified test assertions check `native.status=completed`, `executionPassed=true`, zero truncation and undefined behavior, a fresh canonical scene SHA on `evaluateObservables`, exactly **one emitted ray**, **one detector crossing**, one count-matched complete native detector hit list, a first-interface **transmission** with stated incident/destination indices and exactly one native transmitted branch. The first-event method is `native-observation`; the detector position and incoming unit direction come from `native-hit-event-observation`. The detector callback snapshots the real native intersection point **before** calling the original native `Detector.onRayIncident` exactly once; no reported position comes from the reference `Q`.

The detector is 20 mm long, tangent to the interface, centered at O, with the observed hit at its center, **10 mm from either endpoint**, far exceeding the existing 0.01 mm endpoint refusal. `partialReflection:false` deliberately removes Fresnel partial reflection, and the qualified hit carries the explicit **Fresnel omission warning**; native total internal reflection remains a distinct behavior. In this finite source-to-observer one-interface problem the stationary transmitted ray is below critical for finite positive distances.

**Important limitation:** planar `interface-first-event` does **not** contain a native interface `pointMm`. The test's `inferredCrossing` is the measured detector position minus a *mathematical back-extension* of the measured native outgoing direction to the plane. It is **not** a directly recorded native plane-hit coordinate. The only direct position evidence here is the detector hit. In a one-source/one-ray fixture attribution is controlled by isolation, not proven for arbitrary multi-source optics.

Wrong-side or less-than-0.01 mm normal separation is refused before native work. Deliberate source-angle revision with a stale run hash suppresses all requested readouts. A `maxRayDepth=0` incomplete native run has `observations:null` and suppressed readouts. No claim of a human eye, source image, full field of view, complete ray ancestry, irradiance, actual image detection, or native inverse-optical solution is supported.

## 4. Builder CI — independently inspected records, NOT reviewer reruns

The GitHub Actions run-list API reports **11/11 workflows completed successfully** with exact source `head_sha=a2d0adfe692bc837656a4dd09edc84ab4f490d2f`, all `pull_request` events. I inspected the **actual downloaded job logs**, not only badges:

- [Optical composition run #44282456676](https://github.com/physicsvigilante/opticsim/actions/runs/44282456676), job `134726413536`: named `JEE_OBSERVER_NATIVE_ARRIVAL` log has the expected `Q`, outgoing-angle, exact center detector hit and `nativeImageDetected:false`. All **seven** new research test names report passes; stale/incomplete suppression marker appears. Test summary **797 tests, 797 pass, 0 fail, 0 skipped**. Build, native/boundary checks, browser acceptance steps succeeded.
- [Planar-angular run #44282456397](https://github.com/physicsvigilante/opticsim/actions/runs/44282456397), job `134726412403`: independently checked the matching named native sample and **797/797** test summary; angular/native and browser workflow steps succeeded.

These are two executions of builder-controlled CI on the matching source/tree, **not reviewer-independent PhyDemo, Node suite, or Chrome reruns**. The provenance supports the fixed-fixture findings but does not repair the numerical-reference defect below.

## 5. Findings

### P0 — None

No demonstrated physical law reversal, false native detector-coordinate provenance, source-branch contamination, new production behavior, or release change in the two-file study.

### P1 / R1 — Absolute-coordinate bisection plus fixed residual can reject a valid bounded geometry

The helper bisects directly on large world-tangent coordinates `q ∈ [u_s,u_o]` for **110 iterations**, computes `mid=(low+high)/2`, then asserts the **unscaled** Snell sine-residual error is at most `1e-12`. When the two points lie close to the interface while sharing a large tangent-coordinate offset, binary64 has insufficient spacing to achieve that residual. The bisection stagnates at neighboring representable `q` values; further iterations cannot improve it.

Concrete counterexample **within stated world coordinate bounds and normal clearances**: `P=(0,0)`, `n=(1,0)`, `S=(-0.02,9000)` mm, `O=(0.02,9000.01)` mm, `n_s=1.5`, `n_o=1`. The detector centered at `O` with length 20 mm also stays within ±10000 mm. A standalone Node.js evaluation of the *same 110-step scalar loop* returns `q≈9000.00394046383` and `F(q)≈+1.6708451289204618e-10`, **167× larger than the hard-coded 1e-12 assertion**. Independent high-precision root using plane-local `q-u_s` gives `q=9000.00394046382853602898…`; Snell has a valid physical root. Thus `shootingReference` would throw before native evaluation for this admissible case. I did **not** execute Opticsim or native PhyDemo on this new edge case.

**Required correction before accepting the test-only reference as a reusable basis for the next typed source–observer capability:** solve in a *local* tangent variable `v=q-u_s`, bracket between `0` and `u_o-u_s`, use a convergence/uncertainty criterion appropriate to geometry, distance and floating-point scale, and return an explicit **numerically indeterminate/unstable** status rather than hard-failing a valid physical geometry. Handle zero span separately. Add a regression for the above translation-cancellation case and one near-critical/grazing case. This issue concerns the numerical reference/oracle, **not** native Snell propagation. The fixed sample and seven passing tests are unaffected, but the central inverse-coordinate calculation must not yet be assumed robust across the admissible input envelope.

### Nonblocking N1 — Near-critical, grazing and close-interface behavior not yet tested natively

The tested 10.616° incidence is far from the `asin(1/1.5)≈41.810315°` critical angle. A valid opposite-side point `O=(100,9000)` mm (same S and indices) has a mathematical stationary path at approximately `i=41.807114°`, `r=89.359588°`: a severe numerical-conditioning case for the outgoing line and inferred crossing. Add bounded statuses, ray-hit verification or principled withholding; do not claim this scenario has passed native execution. At finite positive source/observer distance, a stationary *transmitted* path exists; this does **not** establish arbitrary near-critical forward-ray reliability.

### Nonblocking N2 — Axial tolerance mixes exact indeterminacy with near-axial conditioning

`Math.abs(q-u_s)<1e-10 || Math.abs(u_o-q)<1e-10` sets `apparentDepth:null` using an **absolute millimetre** threshold, even when the geometry is mathematically nonaxial. Conservative withholding is preferable to a fabricated image, but future typed results should distinguish `exactly-axial/not-identifiable-from-one-ray` from `near-axial/numerically-unstable`; report any separate paraxial limit as an explicit analytical mode.

### Nonblocking N3 — New typed-contract input validation remains unwritten

The fixture/reference explicitly validates indices within [1,4] and positive opposite normal-side distances at least 0.01 mm. It does **not** itself implement a closed, externally inputtable contract with per-coordinate finiteness, units, orientation, magnitude and overflow checks. Existing `prepareScene` validates the authored native scene but does not turn the research helper into a public inverse-query API. A future contract must enforce all these facts *before* arithmetic and distinguish invalid geometry, inadmissible direction, root-conditioning failure, and native-unavailable.

### Nonblocking N4 — Native provenance claims must remain narrow

`interface-first-event` and `detector-hit-events` do not certify ray history or multi-source attribution; the transmitted-only Fresnel approximation is labelled, and the detector is a geometrical arrival witness, not an eye/image. Keep the phrase **native measured detector hit** separate from **independently predicted or reconstructed interface crossing**, and retain no-image and non-visibility caveats in any next public contract.

## 6. Next bounded step (after R1 is corrected)

Design a **separately typed** source–observer–single-infinite-plane analytical query rather than change PhyDemo's ray solver or silently extend PR #144's *explicit-incident-angle* query. Require explicit S, O, plane point, directed unit normal/orientation, source and observer material indices, physical units, and finite bounded coordinate/clearance policy; return signed initial direction, stationary crossing **as mathematical prediction only**, transmitted direction, finite-angle conditional axis intercept when identifiable, and clear numerical statuses (including exactly axial and near-critical/grazing). Use a translation-stable local-coordinate root and independent forward Snell residual checks.

Optional native consistency validation is a **separate opt-in**: require a fully authored, fresh single source, single ray, one interface, finite detector, explicit Fresnel/sampling policies and native completion; report only actually qualified detector positions/directions with methods and warnings. No synthetic native point of incidence, reverse tracing, arbitrary ray ancestry, image or user perception. Do not merge PR #145 as research or approve PR #143/#144/#141 through this review. [Branch-protection issue #123](https://github.com/physicsvigilante/opticsim/issues/123) was **open** when checked; release and other held-PR owner decisions remain separate.

**Final verdict: CHANGES REQUESTED** — the physics feasibility demonstration is credible and CI provenance is sound, but fix and regression-test **P1/R1** in the test-only inverse reference before marking this review gate cleared for next scoped development. No source, PR, or previous review was modified by the reviewer.
