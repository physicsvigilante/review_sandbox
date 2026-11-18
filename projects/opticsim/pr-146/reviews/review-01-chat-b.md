# Independent R2 — Opticsim PR #146: observer local-root numerical repair

**Review date:** 2026-11-18  
**Reviewer:** Chat B — independently inspected pinned Git objects, source/diff, exact-head builder CI logs, and reproduced independent binary64 and high-precision scalar optics.  
**Verdict: CHANGES REQUESTED.** The original PR #145 P1 (large-world-coordinate absolute-`q` stagnation) is corrected by the local-root/withholding change, **but a separate reproducible P1 remains**: a highly grazing **incoming** ray can be designated `available` even though the rounded authored heading fails the observer-point positional tolerance under independently computed forward Snell propagation. **P0: none; P1: R2-1 below.** No source or release merge is approved.

## 1. Exact identity and scope — VERIFIED from Git objects

- [Draft research PR #146](https://github.com/physicsvigilante/opticsim/pull/146): **open/draft/unmerged** when reviewed; base is frozen #145 head `a2d0adfe692bc837656a4dd09edc84ab4f490d2f`, not production main.
- Source HEAD `2621c08812eb389b70a3e4fa246537ca50b3bc4d` has Git tree **`c8c682f6fbc4f1dcb5827f82fe9768f3f11683d9`**.
- [CI-only PR #147](https://github.com/physicsvigilante/opticsim/pull/147) synthetic merge `e1ed85400bf9a0f34c648e0781bf34e56e3704aa` has **the same tree**, verified via the actual Git commit objects. Its ordered parents are `d3509e82fb65d81aabe336666851f8f2962623f4` (production main) and the exact corrected source HEAD. #147 is **closed unmerged**.
- GitHub compare from frozen #145 to #146 is 3 commits ahead, none behind. Exactly two files changed: [test/jee-observer-native-feasibility.test.mjs](https://github.com/physicsvigilante/opticsim/blob/2621c08812eb389b70a3e4fa246537ca50b3bc4d/test/jee-observer-native-feasibility.test.mjs) (+113/−17) and [docs/JEE-OBSERVER-REFRACTION-NATIVE-RESEARCH.md](https://github.com/physicsvigilante/opticsim/blob/2621c08812eb389b70a3e4fa246537ca50b3bc4d/docs/JEE-OBSERVER-REFRACTION-NATIVE-RESEARCH.md) (+16/−1). No production `src/`, native engine, adapter, canonical schema, browser or other held feature changes.
- The [independent #145 R1 review](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-145/reviews/review-01-chat-b.md) remains **CHANGES REQUESTED** for its *different* head/tree. Neither that verdict nor the held #141/#144 reviews is superseded.

## 2. Mathematical verification — original P1 repair substantially works

With plane point `P`, oriented unit normal `n` from source to observer and tangent `t=(-n_y,n_x)`, put `d_s=-(S-P)·n>0`, `d_o=(O-P)·n>0`, `u_s=(S-P)·t`, `u_o=(O-P)·t`, `span=u_o-u_s`, and **`v=q-u_s`**. The physical stationary condition is

`F(v)=n_s v/hypot(d_s,v) - n_o (span-v)/hypot(d_o,span-v)=0`.

Its derivative is strictly positive:

`F'(v)=n_s d_s²/(d_s²+v²)^(3/2) + n_o d_o²/(d_o²+(span-v)²)^(3/2)>0`.

The ordered bracket `[min(0,span),max(0,span)]` therefore works for both signs of `span`; at exactly zero span, `v=0` is the stationary axial ray. Source and outgoing vectors formed from local normal/tangent components have the correct signs. The updated binary64 midpoint loop detects when no representable midpoint lies strictly inside the bracket and withholds with `LOCAL_ROOT_UNRESOLVED` if its local residual is not qualified. This is a real improvement over 110 repeated stalled *absolute* world-coordinate iterations.

Independent high-precision verification of the bounded R1 case `P=(0,0), normal=0°, S=(-0.02,9000), O=(0.02,9000.01), n_s=1.5, n_o=1` finds a unique physical solution. For the *binary64-represented* tangent span `0.010000000000218278728...`, the high-precision local offset is `v≈0.0039404638286194626653` mm. Standalone Node.js binary64 arithmetic reproduces `local residual=0`, `represented world residual≈−4.1488867896788406e−11`, and correct `WORLD_COORDINATE_ROUNDING` withholding with **no `Q`, incoming heading, apparent point or native ray authored**. Thus the *original* P1's generic assertion failure has been corrected on the child source.

For the original nonaxial control `S=(-60,0), O=(100,40), n_s=1.5, n_o=1`, independently recomputed `q=11.246155771209230...` mm, incidence `10.616108941305°`, transmission `16.041977708351°`, and conditional axis intercept depth `39.11183381854949...` mm agree with builder data. Reflecting the observer to `(100,-40)` produces `q=-11.246155771209230...` and the same positive depth, validating reversed tangent sign. Exact axial `span=0` keeps a true ray with null one-ray depth; nonzero near-axial `O_y=10^−11` mm produces `NEAR_AXIAL_INFERENCE`.

For the near-critical 1.5→1 control `S=(-60,0), O=(100,9000)`, the unique stationary solution has incidence `≈41.8071138252°`, refracted angle `≈89.3595884921°`, and transmitted normal cosine `≈0.01117705665`; the stated exploratory `<0.02` **outgoing** grazing guard correctly withholds `NEAR_GRAZING_EXIT`. The physical critical incidence `asin(1/1.5)≈41.8103148958°` is a different criterion. These numerical guards are research admission rules, not new physical laws.

## 3. P1 / R2-1 — outgoing-only grazing admission misses ill-conditioned *incoming* shooting angle

**A separate bounded counterexample survives every new local and world Snell residual check and is marked `available`.** All coordinates below are millimetres; the infinite plane is through `P=(0,0)` with normal `135°`, `n_s=1`, `n_o=2`:

- `S=(9758.080722152847, 9758.066438595866)`
- `O=(-9616.652224137046, -9475.230867899736)`

All coordinates are within ±10000 mm; source and observer are on correct opposite sides, with independently high-precision normal clearances `d_s≈0.010100000000337` mm and `d_o≈100` mm. The 20-mm tangent detector centered on O also lies within world bounds; this is not invalid apparatus or a critical-angle/TIR example.

A **standalone Node.js binary64 implementation** of the same scalar reference arithmetic, without importing or running Opticsim, gives:

| Check | Independently obtained |
|---|---:|
| Signed tangent span | `+27300` mm |
| Local root `v` | `27242.264973081044` mm |
| Local Snell residual | `+1.5765166949677223e−14` |
| Represented-world Snell residual | `+3.4638958368304884e−14` |
| Reference status | **`available`** |
| **Incoming** normal cosine | `≈3.7074744e−7` |
| **Outgoing** normal cosine | `≈0.86602540378446` |
| Authored heading | `−135.00002124226356°` |

The current guard checks **only** `dot(outgoing,n)<0.02`; it does not withhold the effectively tangent *incoming* ray. The world residual checks the reconstructed ideal crossing `Q`, **not the forward arrival after `incidentHeading` is rounded to a binary64 angle and used as a native source parameter**.

Independently forward-propagating the *rounded authored heading* from the exact represented source, intersecting the infinite plane, applying Snell's law (1→2), and intersecting the observer's tangent supporting line yields, at 90-digit precision, approximately **`(-9616.652243921985, -9475.230887684675)` mm**, missing O by **`2.7980128787e−5` mm** (each Cartesian coordinate misses by ≈`1.98e−5` mm). The test's `approxPoint(hit.pointMm,observer,1e−5)` requires each coordinate error ≤`1e−5` mm. An independent binary64 forward computation using the authored angle gives a still larger miss, ≈`5.93e−5` mm. **Neither calculation ran PhyDemo:** they demonstrate that `available` is not sufficient to certify the reference's prescribed targeting precision, and make no claim about the exact native hit or native solver correctness.

This is severe angular conditioning, not a failure of Fermat's unique physical solution. Incoming normal cosine `~3.7e−7` amplifies a tiny heading perturbation over `~27,000` mm of near-tangential travel. The residual of the *constructed* world crossing can be excellent while the emitted direction is too coarsely represented to realize that crossing. The corrected P1/R1 test for `y≈9000` does not cover this second failure mode.

**Required before R2 clearance:** explicitly fail closed for ill-conditioned **incoming** grazing (e.g. a separately documented exploratory `NEAR_GRAZING_INGRESS` guard) or provide a stronger quantitative, angle-quantization-aware forward-reachability/uncertainty certificate; do not conflate the guard with a physical Snell critical angle. Add the exact counterexample, with `status:'numerically-unstable'`, null authored heading/Q/apparent point, and no native ray, plus a reflected/reversed-span or rotated control and ordinary positive controls. Numerical admission and status precedence should be clear: a valid physical root can exist even when a representable native shooting direction is withheld. A test of the actual pinned native ray is desirable for boundary qualification but is not claimed as completed here.

## 4. Source/native-interface and provenance audit — PASS within declared limits

The [research test at exact HEAD](https://github.com/physicsvigilante/opticsim/blob/2621c08812eb389b70a3e4fa246537ca50b3bc4d/test/jee-observer-native-feasibility.test.mjs) still calls `prepareScene` for a genuine canonical **v5** point-source `single-ray`, one `planar-interface` and a **finite passive** `ray-detector`. It inserts the independently calculated *initial source heading* only, **not a prescribed native route**. The unchanged [planar adapter](https://github.com/physicsvigilante/opticsim/blob/2621c08812eb389b70a3e4fa246537ca50b3bc4d/src/planar-media.js) uses native `PlaneGlass` and delegates its ray incident callback once; [detector capture](https://github.com/physicsvigilante/opticsim/blob/2621c08812eb389b70a3e4fa246537ca50b3bc4d/src/adapter.js) takes actual native intersection-point coordinates before delegating to `Detector.onRayIncident`.

The unchanged [observable contract](https://github.com/physicsvigilante/opticsim/blob/2621c08812eb389b70a3e4fa246537ca50b3bc4d/src/observables.js) checks canonical-scene hash, completed native status, count-matched complete detector events and Fresnel-omission warning. Test assertions check one emitted ray, one detector crossing, actual transmitted event and direction, finite native detector hit, zero truncation/undefined behavior, and suppression of stale or incomplete results. The original detector hit `pointMm` is measured, whereas the interface `Q` is computed analytically; the back-extension of a measured outgoing line to the interface is explicitly a **derived consistency check**, not a native measured interface coordinate.

No source eye, perceived image, source ancestry, multi-interface visibility, power/irradiance, general inverse solver or unconditional native shooting success is established. Withheld references do not execute a native witness. The unchanged reader limitations remain appropriate.

## 5. Builder CI records — VERIFIED, not independent native reruns

GitHub Actions run listing for exact source HEAD returns **11/11 `pull_request` workflow runs, all `completed/success`**. The two actual downloaded job logs show **799 tests / 799 pass**, no reported Node test failures:

- [Optical composition #44289842505](https://github.com/physicsvigilante/opticsim/actions/runs/44289842505), job `134751896241`: pinned PhyDemo `811f508d2b070898c241a568b0c167dcb8645251`; `JEE_OBSERVER_NATIVE_ARRIVAL` shows a detector hit at `(100.00000000000001,40)`, predicted Q `(0,11.246155771209231)`, and `nativeImageDetected:false`. Both new R2 tests pass; `JEE_OBSERVER_LOCAL_ROOT_WITHHELD` records `WORLD_COORDINATE_ROUNDING`, `localResidual:0`, `worldResidual:-4.1488867896788406e-11`, `nativeRayAuthored:false`. Stale/incomplete `JEE_OBSERVER_NATIVE_SUPPRESSION` passes. Browser acceptance logs 27 checks/15 screenshots in Chrome 157 and hosted smoke 5 checks/1 screenshot. All relevant job steps succeeded.
- [Plane-mirror angular #44289843134](https://github.com/physicsvigilante/opticsim/actions/runs/44289843134), job `134751899142`: matching original native-arrival, both named R2 regressions, suppression marker and 799/799 passing tests.

**Provenance boundary:** CI Node, native PhyDemo, Chrome and browser acceptance were **builder-run**, not independently rerun in this review. The independent reviewer performed Git-object/source/log inspection, standalone Node.js binary64 reference and forward sensitivity calculations, and separate high-precision optical calculations only. The new P1 counterexample was **not** executed in pinned PhyDemo or Chrome.

## 6. Nonblocking items and next gate

- **N1 — Typed contract still pending.** The test helper is not a public API and does not itself provide fully closed input validation for arbitrary source/observer coordinates, finite frame/units, normal, indices and magnitude. Require this in the later typed source–observer query.
- **N2 — Distinguish observability.** Keep `WORLD_COORDINATE_ROUNDING`, `LOCAL_ROOT_UNRESOLVED`, `NEAR_GRAZING_EXIT`, `NEAR_AXIAL_INFERENCE` and the proposed ingress-conditioning state separate from invalid geometry, missing native evidence and physical nonexistence. The arbitrary numerical grazing thresholds must not be presented as Snell/TIR laws.
- **N3 — Broaden independent boundary regressions.** Include rotated frames, signed negative tangent spans, extreme index ratios and ordinary moderate-angle positive controls. The checked source's existing reflection/equal-index/reversed-index tests provide useful anchors, but do not certify the full coordinate envelope.

**Release/branch boundary:** PR #146 remains draft and held; PR #145 retains its frozen **CHANGES REQUESTED** verdict; #147 is already closed unmerged. Reviewed #144 and v19 #141 remain independently held. [Branch-protection issue #123](https://github.com/physicsvigilante/opticsim/issues/123) was **open** when checked. Do not merge, deploy, edit source, change prior reviews or authorize release through this R2 review.

**Final verdict: CHANGES REQUESTED** — the R1 large-coordinate bisection failure is genuinely improved, and exact-head builder CI is green, but the newly demonstrated incoming-grazing direction-conditioning problem is **P1** until a fail-closed admission guard/certificate and regression are added on a new reviewed source head.
