# Opticsim PR #193 — Final JEE J11 builder verification and ONE focused Chat B independent review

**20 November 2026 (IST).** This is an exact-source BUILDER report, **not** an independent physics review, original JEE answer, native 3D simulator, physical image observation, or merge authorization.

**PR #193 remains draft and unmerged.** The request is ONE focused review of the new J11 **3D conditional analytical geometry and 2D native research nonclaim**. No re-review of unchanged PhyDemo v5 Snell/TIR physics or previously independently reviewed J08/J13/J14 mirror/prism/lens systems.

## 1. Exact source, protocol and CI identity

- [Draft PR #193](https://github.com/physicsvigilante/opticsim/pull/193), final tested feature source commit **`0578fa68fed5ba1f07abedb341423e33da8f694f`**.
- Exact HEAD Git tree **`93e21f3f6ce316f00c4170326b53a467dcf8a2dd`**. GitHub synthetic CI-tested merge commit **`9d9345350fc003d8d2d45180db4845b58c529660`** independently fetched by builder, **identical tree `93e21f3f6ce316f00c4170326b53a467dcf8a2dd`**, ordered parents [stable production main `2a529aeca8cf4960f3c7f285e635c55ae5a130b9`, exact feature head `0578fa68fed5ba1f07abedb341423e33da8f694f`]. Production main was rechecked and unchanged at the time this packet was produced.
- Original source/model/nine prospective frozen cases committed **before the implementation/test** at **`bbb40ee6be4d62f910e9e3eefab3d198cd3d4873`**, `evaluation/jee-j11-escape-disc-v1/frozen-protocol.json`, Git blob **`c863e1398f4d714a4ab9677159c5132eb1e1b85d`**, byte-identical at final source head.
- Base main `2a529aeca8cf4960f3c7f285e635c55ae5a130b9` is independently reviewed PR #192 release, with **11/11 production post-merge CI passed**.
- Pinned upstream PhyDemo remains **`811f508d2b070898c241a568b0c167dcb8645251`**, completely unchanged.
- Base-to-HEAD compare: exactly **9 added files**, **0 modified/deleted existing files**: frozen protocol; three J11 examples (symbolic, synthetic explicit numeric, numeric missing exterior); pure analytical `src/axisymmetric-escape-disc.js`; strict original-byte `scripts/axisymmetric-escape-disc-query.mjs`; J11 analytical/CLI and native cross-section tests; and `docs/JEE-AXISYMMETRIC-ESCAPE-DISC.md`. No canonical scene profile/schema, renderer, existing native physical algorithm, 2D blocker, historical first attempts, previous tests or workflow modified.

## 2. Original JEE J11 source and strict provenance boundary

- Historical frozen 20-case JEE sample case **J11**: `08_Ray_Optics_Explanations/04_Total_Internal_Reflection_TIR/Problems/005.png`; frozen source-review `evaluation/jee-post164-coverage-v1/source-review.json` at held PR #165 source `6a72bd67e58e9a3fd94a6bf33d88d1f20295b4c2`.
- The source audit says: an **isotropic point source** at symbolic depth `h` under water, symbolic water index `mu`, and a **floating opaque disc** that should hide it; determine its minimum radius. The audit did **not** find numeric h, water index, upper/exterior index, disc/observer apparatus, emission brightness or finite interface dimensions.
- Original Ray Optics source archive historical SHA-256: **`03fa29dc8a09f157692ea389354bc7393a96e49f792b60329164c03e56bc5939`**. The older source-collection [run 44360693719](https://github.com/physicsvigilante/opticsim/actions/runs/44360693719) and artifact **14454755556** contain original J11 **Problems** PNG for reviewer. Builder used frozen audit, **did not re-download or visually reread original J11 in this build**, and did not open Solutions.
- REVIEWER should independently inspect **Problems image only**, check the disc placement and whether any exterior medium is specified (not assume air from common convention). This result is source-conditional and not an independent textbook-answer completeness score.

## 3. Independently reviewable mathematical physics and scope

**Model:** one infinite horizontal planar interface, point source at `(0,0,-h)`, homogeneous isotropic index `n1` below, index `n0` above, **centered perfectly opaque circular disc** at the interface plane, no other optical paths or diffraction. The source emits all azimuths and upward polar incidence angles `theta` from the surface normal.

Surface intersection at azimuth `phi`: `(x,y)=(h*tan(theta)*cos(phi),h*tan(theta)*sin(phi))`; radius `rho=h*tan(theta)`. If **n1>n0**, direct transmitted rays have `theta<theta_c=asin(n0/n1)`. The strictly transmitting surface intersections form a circular footprint with limiting radius

```
R_min = h*tan(theta_c)
      = h*n0/sqrt(n1^2 - n0^2)
```

A centered opaque disc radius `R>=R_min` covers **every directly upward-transmitting geometrical ray** in the stated ideal model. Any smaller disc radius admits some `theta<theta_c` and `phi` whose surface intersection is outside the disc. **At exact critical incidence, do NOT invent a propagating grazing external ray**; this is a supremum of a strictly transmitted set. If **n1<=n0**, near-grazing incidence can transmit and have unbounded surface intersection radius, so **no finite disc** covers the infinite-plane geometrical escape set.

**This is 3D mathematical rotational symmetry, NOT a 3D PhyDemo simulation or measured human visibility.** Real disc edge scattering, diffraction, partial reflection/power, other escape routes, finite surface, 3D eye/pupil, path-specified visibility and source authenticity are OUT OF SCOPE. A 2D line blocker or native detector's zero would NOT prove the 3D statement.

The original source-only symbolic example `examples/jee-j11-escape-disc-symbolic-v1.json` requires literal `h,mu,n_outside` variables and returns:

```
minimumRadiusExpression: h*n_outside/sqrt(mu^2-n_outside^2)
domain: h>0 and mu>n_outside>0
numericalRadius: null
native.status: not-run
```

No numerical exterior index or source parameters are invented. The explicit **synthetic** numeric teaching example supplies h=100 mm, n1=1.5, n0=1 and returns `theta_c≈41.81031489578°` and `R_min≈89.44271909999158 mm`; NOT a source-original numeric answer. A numeric example lacking `outsideIndex` returns `needs-information / MISSING_EXTERIOR_INDEX`, never a guessed n0=1.

Numeric domain: explicitly supplied depth 1–10000 mm with mm/cm/m units, absolute indices in [1,4], relative near-equal-index guard `1e-8`, radius reporting cap 1,000,000 mm. Exact equal or reverse index returns `no-finite-coverage`; near equal or excessive/poorly conditioned radius `numerically-indeterminate`. Malformed, extra, unsupported/nonnumeric and inconsistent symbolic fields are rejected. These are conservative policies, **not universal physical/roundoff error proofs**. Numeric reference tests independently use trigonometry for dozens of media/depths, actual 3D azimuthal ray directions, an uncovered counterexample for any undersized disc, unit conversions and refusal controls.

## 4. Separate REAL pinned native PhyDemo **2D meridional only** witness

`test/jee-j11-escape-disc-meridional-native.test.mjs` uses real public v5 `SingleRay + PlaneGlass` with fully added synthetic depth 100 mm, interior index 1.5, outside index 1, brightness .08, `partialReflection:false`, and an **infinite 2D planar interface**. This is a **cross-section** of the ideal geometry, not a 3D disc or original source apparatus. All actual callbacks are delegated to native once, observed, and saved with input/report hashes. No expected path or ray is injected.

[Exact final-head optical composition CI run 44700432540](https://github.com/physicsvigilante/opticsim/actions/runs/44700432540) and quasi-static native logs confirm **12 executed cross-section controls** (nine prospectively frozen source/case concepts and additional explicit sign/translation/numeric stop controls), with **7 safe native transmission witnesses**, **2 safe native TIR witnesses**, **3 unqualified**:

| Native angle/control | True native result | Qualification boundary |
| --- | --- | --- |
| 0°, 15°, 30°, 41° from upward normal | completed; native transmits | native **2D** safe only |
| theta_c−0.0001° | completed; transmission at surface x≈89.44240494 mm | 2D safe only, distinct from exact critical |
| theta_c | raw native `total-internal-reflection`, x≈89.44271910 mm | **WITHHELD**: exact critical sine uncertainty |
| theta_c+0.0001°, 50° | completed; genuine native TIR | native **2D** safe only |
| −30° azimuthal cross-section | transmission at x≈−57.7350269 mm | 2D safe only, not a 3D azimuth sweep |
| translated 30° | transmission at x≈257.7350269, y=−75 mm | 2D safe only |
| native max depth 0 | native `incomplete`, truncation 0.08 | withheld |
| processed limit 1 | native `stopped` despite a partial interface callback | withheld |

No 3D disc, actual opaque physical coverage, continuous irradiance, eye visibility, image or original-source 'hidden' measurement is claimed. The symbolic/numeric standalone API always returns `native:{status:'not-run'}` even if separate native research completes successfully. The exact-critical result is **one raw pinned execution**, not a universal exact-critical physical verdict; it remains withheld regardless of raw callback status.

## 5. Exact final-head CI and archived evidence provenance

**11/11 final-source PR workflows SUCCESS**, including older genuine native/Chrome regressions. Node24 logs on [optical composition CI 44700432540](https://github.com/physicsvigilante/opticsim/actions/runs/44700432540), job **136167191567**, and [deterministic angular CI 44700432501](https://github.com/physicsvigilante/opticsim/actions/runs/44700432501), job **136167190939**, report **1,116 Node tests, 1,116 PASS, 0 FAIL**. No dedicated J11-specific 3D browser/scene, real optical disc or eye detector was executed.

- Quasi-static source motion checks — run 44700432744: success
- Deterministic planar angular query checks — run 44700432501: success
- Numerical ray reliability diagnostics — run 44700432460: success
- Curved mirror checks — run 44700432415: success
- Parameter experiment checks — run 44700432486: success
- Original refraction problem pair — run 44700432376: success
- Plane-mirror angular inverse checks — run 44700432347: success
- Qualified authoring checks — run 44700432609: success
- Optical composition checks — run 44700432540: success
- Planar refraction checks — run 44700432447: success
- Unified problem workflow checks — run 44700432490: success

Official GitHub Actions uploaded (optical composition run `44700432540`):
- `llm-authoring-evidence` artifact ID **14612681859**, GitHub metadata SHA-256 **`1d56d5fa3b665f25240d804a7477fbe6247d913a8701b0b9682ba529f4ebc812`**.
- `browser-acceptance-evidence` ID **14612303868**, metadata SHA-256 `04afea1e266bd03c897d6a165859cd8140ca20a532eb118d8ed1827d62078eca`.
- `hosted-browser-evidence` ID **14612228947**, metadata SHA-256 `9ba4fab3109b892af4fd9bc461f0c9c1227769df43873b7311ec6306b16467ec`.

**Builder integrity boundary:** GitHub Actions artifact names and digests and actual job logs were checked; builder **did not independently download and hash these final ZIP bytes or raw internal members**. Reviewer should independently download and compare ZIP SHA/CRC plus the original source J11 PNG and the source-bound per-case input/report hashes where possible.

The standalone CLI stores original input bytes and SHA-256 before parsing, returns separate symbolic/conditional/missing-information/no-finite/refusal reports, and never creates a qualified native scene. Its shared output helper retains prior hostile-concurrent-filesystem race limits and ordinary `JSON.parse` permits duplicate JSON object keys; no security/canonicalization promise is asserted.

## 6. One focused independent Chat B review required

**Chat B:** independently visually read original J11 Problems image (not Solutions), inspect literal symbolic parameters/unknown exterior index and source geometry; derive the all-azimuth 3D Snell escape-cone and disc coverage theorem including strict critical boundary, reverse-index no-finite case and counterexample to a too-small disc. Independently review source and numeric range/refusal policy; make sure the '3D' assertion belongs only to mathematical symmetry, **not native simulator, physical disc, 2D detector or eye**. Inspect real pinned-native PlaneGlass meridional events against 2D Snell and TIR, including exact-critical withholding and numerical stops, with no false image result. Verify CLI raw bytes and hashes, production untouched, protocol frozen first, final HEAD tree == tested merge tree, all eleven CI workflows and relevant original J11/source/member archive integrity. Report what was independently calculated/executed versus relied on CI.

**Do NOT:** re-review already independently verified v5 Glass, old TIR algorithms, J08 prism/mirror, new unrelated Fresnel-on scope, or earlier historical textbook outputs. Do not merge/deploy/alter source or original sample.

Publish the **single complete independent focused review report** on default branch of `physicsvigilante/review_sandbox` at:

`projects/opticsim/pr-193/reviews/review-01-chat-b.md`

The report must name exact source **`0578fa68fed5ba1f07abedb341423e33da8f694f`**, Git tree **`93e21f3f6ce316f00c4170326b53a467dcf8a2dd`**, tested synthetic merge **`9d9345350fc003d8d2d45180db4845b58c529660`**, source limitations, independent numerical/physical findings, blockers if any, and final explicit verdict **CLEARED FOR OWNER DECISION** or **CHANGES REQUESTED**. Read back committed review, return immutable review commit SHA and URL. Chat-only verdict cannot satisfy release gate. **Keep PR #193 DRAFT/UNMERGED** until this one focused independent review is verified for the unchanged final source, followed by standing owner release decision. No original JEE solved percentage rewritten.
