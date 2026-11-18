# Independent R1 — Opticsim PR #143 JEE apparent-depth native feasibility

**Review date:** 2026-11-18  
**Reviewer:** Chat B (independent source/physics/CI inspection; read-only Opticsim review)  
**Verdict: CLEARED FOR NEXT SCOPED DEVELOPMENT — research only, NOT merge/release approval.**  
**Blocking findings:** P0 none; P1 none. **Nonblocking hardening:** N1–N4 below.

## 1. Exact review boundary and identity

- Draft [Opticsim PR #143](https://github.com/physicsvigilante/opticsim/pull/143), still open and unmerged at inspection.
- Production base main: `d3509e82fb65d81aabe336666851f8f2962623f4`.
- Research HEAD: `2ec38c431b7c191d1fed225eaa8db6ae1115caeb`.
- HEAD Git tree: `b71a840d9a14b85749fe0a587e65bbb115886243`.
- HEAD parent `2f99f7eacaef5f63278ead5ac1fd6a3dca926e0b`, whose parent is exactly production base `d3509e82fb65d81aabe336666851f8f2962623f4`; compare reports **2 ahead / 0 behind** and merge base = production base.
- GitHub synthetic merge `22477a0c70c2fd01ec24df8205b93aafa5483633` has **the identical Git tree** `b71a840d9a14b85749fe0a587e65bbb115886243` and parents in order [production base, research HEAD]. These facts were read from the actual Git commit objects, not inferred from PR prose.
- Independently inspected the exact HEAD versions of [test/jee-apparent-depth-native-feasibility.test.mjs](https://github.com/physicsvigilante/opticsim/blob/2ec38c431b7c191d1fed225eaa8db6ae1115caeb/test/jee-apparent-depth-native-feasibility.test.mjs) and [docs/JEE-APPARENT-DEPTH-RESEARCH.md](https://github.com/physicsvigilante/opticsim/blob/2ec38c431b7c191d1fed225eaa8db6ae1115caeb/docs/JEE-APPARENT-DEPTH-RESEARCH.md).
- Diff is **two added files only**: 165 new test lines + 47 new research-document lines, **212 additions / 0 deletions**. No `src/`, native vendor, adapter, public authoring contract, browser or release files were changed.

This R1 is confined to feasibility evidence. Do **not** interpret it as release clearance, acceptance of held v14–v19 work, reopening or approval of PR #141, or resolution of branch-protection issue #123.

## 2. What the native run actually does (and does not)

The fixture clones only the `request` in `evaluation/planar-refraction-v1/first-request.json`; that baseline request contains a single point source (`S1`) and a single planar interface (`I1`), not a hidden ray fan. Each trial explicitly sets:

- World: x-right, y-up, mm. Source `S1=(-60,0)`, brightness 1, `single-ray` emission at the trial incidence angle.
- Interface `I1` at `x=0`, normal `+x`, negative/source index 1.5 and positive/observer index 1.0 in the principal trials; `partialReflection:false`.
- Finite detector `D1` centered at `(100,0)`, vertical (`orientationDeg:90`), length **400 mm**, entirely in the observer medium.
- Requests: `interface-first-event`, `detector-hit-events`, `detector-crossings`, `source-emissions`.

`prepareScene` canonicalizes the given fields to mm and selects schema v5 / `planar-media-tracing`; its inactive source-angle default does not alter explicit `single-ray` direction. The [native adapter](https://github.com/physicsvigilante/opticsim/blob/2ec38c431b7c191d1fed225eaa8db6ae1115caeb/src/adapter.js) compiles that source into pinned native `SingleRay`, the interface into native `PlaneGlass` (using the explicit index ratio and expected axis orientation), and the detector into native `Detector`. No new Snell ray tracer or physical reverse ray is introduced.

Crucially, [`checkCandidate`](https://github.com/physicsvigilante/opticsim/blob/2ec38c431b7c191d1fed225eaa8db6ae1115caeb/skills/sim-ro-image-to-scene/scripts/check-scene.mjs) loads the canonical scene into the pinned native `Simulator`. Native observations wrap source emission, interface incident callbacks and detector incident callbacks with **one delegation to the original native handler**. [`src/planar-media.js`](https://github.com/physicsvigilante/opticsim/blob/2ec38c431b7c191d1fed225eaa8db6ae1115caeb/src/planar-media.js) derives direction and transmitted/reflected branch labels **from returned native rays**, not its own Snell solution. [`src/adapter.js`](https://github.com/physicsvigilante/opticsim/blob/2ec38c431b7c191d1fed225eaa8db6ae1115caeb/src/adapter.js) captures actual ray position/direction just **before** the native detector callback mutates the ray, then calls the original detector callback exactly once.

The test's `conditionalAxisIntercept(hit)` computes a **post-native, read-only line extension** `x_virtual=x_D-y_D*u_x/u_y`. It adds no scene component, never drives native propagation, and returns `null` for absent hit or near-zero vertical direction. `checkTransmitted` requires native `completed`, `executionPassed`, one emission, one crossing, exactly one qualified/available hit, a native transmission outcome, one actual transmitted branch, hit x=100, agreement of measured hit direction with that native transmitted branch, native incidence and refracted angle consistency, and the independent Snell/back-projection reference. This restricts its inference to the intentionally isolated one-source/one-ray experiment, **not** general detector-to-source attribution.

[`evaluateDocument`](https://github.com/physicsvigilante/opticsim/blob/2ec38c431b7c191d1fed225eaa8db6ae1115caeb/scripts/author-scene.mjs) snapshots opt-in native hit observations only for completed native output. [`evaluateObservables`](https://github.com/physicsvigilante/opticsim/blob/2ec38c431b7c191d1fed225eaa8db6ae1115caeb/src/observables.js) clones inputs, rehashes the canonical scene, and suppresses all results when the hash mismatches or the run is not complete and passed. Hit events require a complete, count-matched native list (maximum 32; uncertain endpoints withhold the list), and `partialReflection:false` adds a qualified-approximation warning. Thus the observed geometry has good **native-result provenance**, but a hash is a freshness guard, **not** an independent attestation of physical truth or per-source path provenance.

## 3. Independent physics and numerical audit

For `d=60 mm` and a ray incident from refractive index `n_s` onto an ideal plane with observer index `n_o`:

`t=asin[(n_s/n_o) sin(i)]` when transmission exists;  
`d_app(i)=60 tan(|i|)/tan(|t|)` for nonzero noncritical angles.  

The actual native hit should satisfy `y_D=60 tan(i)+100 tan(t)` for positive `i`; its backward line intersects y=0 at `x_D-y_D u_x/u_y=-d_app`. The usual `60*(1/1.5)=40 mm` is strictly the **paraxial limiting** depth, not a common finite-angle virtual point.

I calculated the ideal refraction, detector y and conditional depth separately using standard math functions, **without running Opticsim or PhyDemo**:

| Incident i | Refracted t | Expected native detector y (mm) | Independent conditional depth (mm) | Depth in builder's native log (mm) |
| ---: | ---: | ---: | ---: | ---: |
| 2° | 3.000762438° | 7.337358459 | 39.969501869753 | 39.969501869753245 |
| 5° | 7.511987115° | 18.435854238 | 39.808183423875 | 39.80818342387525 |
| 12° | 18.171812994° | 45.577216043 | 38.854078501260 | 38.85407850125944 |
| 25° | 39.340476504° | 109.945551056 | 34.133771193526 | 34.13377119352626 |
| 30° | 48.590377891° | 148.030358054 | 30.550504633039 | 30.550504633038912 |

Independent ideal depth and builder-logged native-derived depth agree to approximately binary64 rounding (largest absolute difference under `1e-12 mm` on this dataset); the logged hit y values likewise agree. The 400-mm detector spans y=−200 to +200 mm; **all five transmitted hits are safely on its finite segment**. At 30°, the closest tested positive hit is approximately **51.97 mm from the upper endpoint**, not a marginal detector miss. The test's `1e-5 mm` axis-depth tolerance, `1e-6 degree` outgoing-angle tolerance, and `1e-8` unit-vector comparison are satisfied here; near-critical numerics need separate guards in a future general query.

**Control cases checked against source assertions and actual named CI tests:**

1. **±5°:** odd-symmetric y hits, symmetric depth; the test requires both.
2. **1→1 at 5°:** independent depth 60 mm; builder's log gives `60.00000000000004 mm`.
3. **1→1.5 at 5°:** independent depth `90.19115365768965 mm`; builder's logged value matches. This is index reversal with observer denser, not the high-to-low principal case.
4. **1.5→1 at 50°:** critical incidence is `asin(1/1.5)=41.810314896°`. 50° exceeds it, so no real transmitted detector ray exists. The test requires native TIR outcome, no transmitted branch, zero crossings/hits and a null intercept; the named CI test passed.
5. **Normal incidence (0°):** one actual hit but `u_y=0`, so a *single axial ray* cannot yield a unique virtual point; the null result is correct even though the limiting paraxial ratio is 40 mm.
6. **`maxRayDepth=0`:** native execution is `incomplete`, `executionPassed=false`, raw observations null and **all four qualified requests suppressed**; the named CI test passed.

No backward extension is mistaken for a native backward ray. No point-spread function, image detection, continuous irradiance, bundled-ray reconstruction or observer perception is demonstrated.

## 4. CI evidence and independence boundary

Independently queried the exact HEAD's associated Actions runs: **11 of 11 standard workflows** completed with `success`. In particular, [Optical composition workflow run #44272676234](https://github.com/physicsvigilante/opticsim/actions/runs/44272676234) is `pull_request`/`completed`/`success` at the claimed HEAD and job [#134692924534](https://github.com/physicsvigilante/opticsim/actions/runs/44272676234/job/134692924534) succeeded.

I fetched and examined the actual **job logs** (not only checks or PR claims). They show:

- Setup line: `Pinned PhyDemo ready: 811f508d2b070898c241a568b0c167dcb8645251`.
- `npm test` completion: **796 tests, 796 pass, 0 fail**.
- `JEE_APPARENT_DEPTH_NATIVE_FINITE_ANGLE` with the five exact native-derived values and hit y coordinates in the table.
- `JEE_APPARENT_DEPTH_NATIVE_INDEX_CONTROL` with equal and observer-denser values.
- `JEE_APPARENT_DEPTH_NATIVE_INCOMPLETE` with `status=incomplete` and suppression.
- Individually passing named test lines for symmetry, TIR and normal incidence, as well as the build and browser-related job steps reporting success.

The GitHub synthetic merge running CI has the same Git tree as inspected HEAD, so this is exact-tree builder evidence. **I did not independently install PhyDemo, rerun Node, execute native ray traces, run Chrome, or regenerate published screenshots/references.** The workflow log and source review support the narrower claims above, not independently reproduced runtime results or released functionality.

## 5. Findings by priority

### P0 — none

No security/physics-integrity issue in the two added, unreleased test/documentation files that would prevent continuing a strictly scoped research track.

### P1 — none

No material numerical error, wrong index orientation, fabricated trajectory, silently substituted source bundle, falsely admitted incomplete measurement or false image-detection claim found within this declared experiment.

### Nonblocking (N1–N4)

**N1 — Future source attribution must not inherit this shortcut.** The test compares the event's transmitted direction to the detector hit's incoming direction but does **not** prove full ray identity, ancestry or all intervening interactions. Its single-source/single-ray/two-optical-component fixture makes this sufficient **here**. A multiple-ray/multiple-source engine feature must require explicit native parentage/route qualification and must not infer identity from direction agreement or callback order.

**N2 — Tighten the feasibility assertions before depending on a public API.** The test accepts `qualified` *or* `available` hit status instead of explicitly checking the transmitted-only warning, hit `method=native-hit-event-observation`, event `method=native-observation`, count matching and canonical SHA at the test site. Current shared implementation enforces the relevant gates, so this is regression-hardening rather than a current blocker. Add a deliberate stale-scene/mismatched-execution negative control in the next contract tests.

**N3 — Conditioning/visibility outside the sampled range is not established.** Only five positive finite angles up to 30° and ±5° symmetry are tested. As `t→90°`, a finite detector may miss the ray; as `i→0`, `u_y` makes the intercept ill-conditioned or formally indeterminate for an individual axial ray. A future query needs typed `no-transmitted-hit` / `not-identifiable` / `numerically-unstable` outcomes, a nonfictitious detector reachability check when native evidence is required, and near-critical cases. The present sample hits have ample endpoint margin.

**N4 — Do not silently elevate geometry to observability.** A post-native axis intercept is conditional on a **chosen source axis, incidence and explicit single native ray**, not proof of a stigmatic perceived point or actual image. Retain `nativeImageDetected:false`, per-angle results and visible approximation labels in any eventual teaching UI. A general virtual-object location claim would need a separate, explicitly qualified multi-ray/observer contract.

None of N1–N4 requires editing this research-only branch to proceed with **next scoped design**. They become design/acceptance requirements before extending the public engine.

## 6. Bounded recommended next step

**Design and independently review** a separate typed `planar-apparent-depth-query-v1` contract, without modifying PhyDemo or pretending there is a native image observer. Start with one known point source, one planar boundary, explicitly ordered homogeneous indices, known boundary frame/normal and a declared observation/incidence angle (or a clearly labelled paraxial-limit request). Return:

- `conditional-axis-intercept` or `paraxial-limit` with units and exact assumptions; angle-indexed results, never an unqualified universal image point.
- `conditional` / `not-identifiable` / `TIR-no-transmission` / `native-hit-unavailable` / `incomplete-or-stale` / `numerically-unstable` outcomes with explicit reasons.
- Separate **analytical Snell** evidence from optional **native-observed** measured hit/direction evidence, using complete, fresh hash-matched native records only; never manufacture missing rays, dimensions or observer fields.
- Refuse unknown source-interface ordering, ambiguous side/normal, missing or invalid indices, axial single-ray inversion, impossible refracted angle, ill-conditioned near-critical extrapolation and unqualified source pairing.
- Acceptance fixtures: translate/rotate interface and source axis; ± angles; equal/reversed indices; close-to-critical/missed finite detector; normal incidence and paraxial convergence; stale/incomplete; explicit evidence method and warning checks.

Keep a *separate later milestone* for multiple native rays from one source in a single authored scene and a qualified detector-parentage study. Even then, do not market an actual image/observer/PSF without additional independent physical and provenance evidence.

## 7. Disposition

**CLEARED FOR NEXT SCOPED DEVELOPMENT.** The source, Git-tree and builder CI identities check out. The tested conditional Snell/back-projection geometry is correct within the stated ideal model; the controls and suppression are appropriate for a **test-only feasibility demonstration**. This is **not a PR merge recommendation**, not a production feature, not an independently rerun native experiment, and not a release gate for any held v14–v19/PR #141 work. Issue #123 remains outstanding.

**Publication boundary:** this report is the only authorized new review artifact; no Opticsim source modifications, native runs, merge, release or PR approval were performed by this reviewer.
