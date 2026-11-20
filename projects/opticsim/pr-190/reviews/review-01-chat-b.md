# Opticsim PR #190 — independent Chat B review 01

**Date:** 2026-11-20 (IST)  
**Verdict: CLEARED FOR OWNER DECISION** — no release-blocking defect found in the scoped additive analytical query, test-only native witness, original-source interpretation, or evidence integrity. This is **not** approval to merge, deployment authorization, a textbook answer certification, or independent reproduction of PhyDemo execution.

## Exact review identity and release boundary

- Source PR: https://github.com/physicsvigilante/opticsim/pull/190 — **draft, open, unmerged** at the time of review.
- Exact reviewed feature HEAD: **cbf96405ac7a63da4eead04fb8b0d5974fa7ca06**.
- Exact feature Git tree: **25efbe0ed82c3b3ab6d11cf7e37815b12925d3f4**.
- GitHub synthetic merge: **116315dff20573961cd3dcd821dad9d53153d0cf**; independently queried Git data confirms **the identical tree 25efbe0ed82c3b3ab6d11cf7e37815b12925d3f4** and ordered parents **c4e436fca34c01b3ce63bd426dc71bd0daf1daa9** (production main) and the exact feature HEAD. The main branch was also read independently at the stated base SHA.
- Original pre-execution protocol commit: **6fb6625453eb62c24d9d7b40d929b9cfb75d5596**. Its protocol blob **e8efe248e64c3a5e9329c9a3d69e73262eeb58ea** is identical at the reviewed final head. The frozen protocol is the first of the nine feature commits.
- Pinned PhyDemo: **811f508d2b070898c241a568b0c167dcb8645251**, read from unchanged `upstream-pin.json`. GitHub compare of the base to feature head confirms **exactly eight added files, no changed/deleted prior files** (867 additions), so no old v8/v22/refraction algorithm, shared native schema, workflow, upstream pin, or prior source data changed.

## 1. Direct original J13 Problems-source review — PASS

I downloaded historical source-collection GitHub Actions **artifact 14454755556** (run **44360693719**) and independently extracted and **visually inspected** `jee-post164-coverage-v1/sources/J13.png` **without opening Solutions**. Its SHA-256 is **d78adec66991f13c049d087f46c3e23a24da5bcbe0c2c16268741d2820aa2df3**, matching the source manifest's J13 path `08_Ray_Optics_Explanations/05_Prism/Problems/001.png`. The downloaded source-collection artifact ZIP hashed locally to **ec95794b8becfcb10a3819c39063c8c4673cf43f58cb3b6cce3ee523cd755f97**, matching GitHub's stated historical artifact hash. The *underlying original repository ZIP* itself was not re-downloaded/rehashed; the original-archive hash in the frozen protocol remains a historical provenance claim, not a new independent byte check.

The actual Problems image says **equilateral prism**; first refraction at **AB**; incidence on **AC** at an angle **slightly greater than** the critical angle, followed by total internal reflection; refraction and exit at **BC**, with the emergent ray at **30° to the BC normal**. It asks for first incidence `i` and the prism refractive index. **It does not state an exterior absolute refractive index**, specify a numerical difference above critical, source position, finite side length, or illumination/detector conditions.

The drawing labels **A at the top, B lower left, C lower right**. The synthetic native triangle sets **A=(0,+70), B=(0,-70), C=(70√3,0)** mm. Rotating that triangle rigidly **30° clockwise** yields the source's orientation with BC horizontal and preserves all three face identities, incidence angles, and route topology. In the original source orientation, the outgoing branch at BC is to the lower-left of the outward normal, as required. The drawing's approximate ray slopes and pixel lengths are not independent numerical facts; they are not used as fitted inputs.

**Interpretation:** “slightly greater” implies **strictly greater** than critical. It does **not** provide a numerical epsilon or license to replace a strict inequality with critical equality. A unique numerical glass index is **not determined by the literal facts**. A conventional textbook approximation might choose a limiting-critical relation, but that must not be advertised as a source-exact, uniquely certified answer. The explicit “conditional / not textbook graded” API policy is appropriate.

## 2. Independent signed ray geometry and algebra — PASS

Use the **orientation of the original image**, BC horizontal, x right/y up. The inward AB normal is oriented **−30°** from +x, AC outward normal **+30°**, and BC outward normal **−90°**. For the stated principal ray branch let `i` be external incidence, `r` the internal entry refraction angle from AB's inward normal, and `e` the exterior BC emergence magnitude from its outward normal, with `m=n_inside/n_outside>1`.

- After entering AB the internal ray direction is **−30°+r**. Its AC incidence magnitude is **60°−r**.
- Reflection about the AC tangent, direction −60°, gives the ray direction **−90°−r**. It therefore reaches BC with internal incidence magnitude **r**, *if* the finite three-face route is attained.
- Refraction at AB and BC gives **sin(i)=m sin(r)=sin(e)**, hence **i=e** on the declared principal external half-plane. At J13 **e=30°**, this means **conditional i=30°**, independently of a numerical index.
- Genuine TIR at AC requires **m sin(60°−r)>1**, with **r=asin(sin(e)/m)**. Since **m sin(60°−r)=[√3√(m²−sin²(e))−sin(e)]/2**, algebra gives the strictly open bound

    **m > (2/√3)√(1+sin(e)+sin²(e)).**

At **e=30°**, this is **n_inside/n_outside > √(7/3) = 1.5275252316519468…**. Equality is the *critical boundary*, not TIR, and unknown `n_outside` prevents an absolute glass-index result. This derivation is independent of the PR's implementation and preserves the signed face ordering.

I independently recalculated candidate thresholds in Python, using a separate Snell residual rather than the implementation's returned result:

| Emergence e | Strict minimum m (excluded) |
| ---: | ---: |
| 0.1° | 1.155709522061089 |
| 1° | 1.164907431474127 |
| 5° | 1.208167684962952 |
| 10° | 1.266913239478261 |
| 20° | 1.394751075409124 |
| 30° | 1.527525231651947 |

For each e the TIR residual at that bound was zero within floating precision; at e=30° the residual for **m=1.6** is **+0.06624465810881808** and for **m=1.5** is **−0.02525512860841106**. For `m=√(7/3)±0.0001` the corresponding residuals are about **+9.165115×10⁻⁵** and **−9.165187×10⁻⁵**, safely outside the adopted **1e−5** uncertainty band. That band is an explicitly conservative **numerical admission policy**, not a physical tolerance, an exact error estimate, or an interpretation of “slightly”.

## 3. Analytical contract, index refusal, and raw-byte CLI — PASS with noted scope

Reviewed the complete exact-head contents of `src/three-face-prism-tir-bound.js`, `scripts/three-face-prism-bound-query.mjs`, `examples/jee-j13-reflected-prism-bound-v1.json`, the two new test files, and both new documentation files.

- Required `format`, `kind`, `model`, `branchConvention`, `angleUnit`, emergence angle, and `criticalRelation:'strictly-above'` are enforced. Unknown input keys and non-number/nonfinite indices or angles are refused. The intentional principal 2D e domain **[0.1°,30°]** is narrower than all possible prisms; absolute indices **[1,4]** are a declared query policy, **not** a statement of a universal physical domain.
- With original source-only inputs, `status:'conditional'` reports the strict **relative** lower bound, **`conditionalIncidentAngleDeg:30`**, `outsideIndex:null`, `insideIndexLowerBoundExclusive:null`, `uniqueIndexInferred:false`, and **`native.status:'not-run'`**. The code never invents n_outside=1, never constructs a scene, and never promotes the separate research witness into the query's status.
- An explicit exterior index only scales the *open* minimum inside-index bound. If that leaves no index in [1,4], the query returns `unavailable`. A supplied candidate inside index requires an explicit exterior index, must be higher, and must have **m sin(60°−asin(sin e/m))−1 > 1e−5** to be admitted as *angularly TIR-consistent*, **not finite-route certified**. Critical equality, near-critical, and below-critical examples are withheld/refused.
- The standalone CLI reserves a fresh bounded directory, saves original **input bytes** unchanged, calculates SHA-256 before parsing, and preserves `native:not-run` for conditional, unavailable, and rejected reports. From the downloaded final CI artifact I independently compared three J13 standalone report hashes to their raw `input.json` bytes: conditional original, unavailable m=1.5, and malformed JSON; **all 3 match**. No J13 standalone native scene or native summary was emitted.
- The pre-existing `reserveAuthoringOutput` helper's concurrent hostile-filesystem TOCTOU caveat remains. The code uses standard `JSON.parse` (which does not reject duplicate JSON property names by itself), so do not market this CLI as a cryptographically canonical, duplicate-key-rejecting JSON format. These are **non-blocking documented/future-hardening boundaries**, not evidence of a native/physical claim escape in the present strict enum and schema gates.

## 4. Genuine pinned-native 3-face evidence — PASS for test-only witness

Downloaded final-head **`llm-authoring-evidence` artifact 14603633871** from [optical composition run 44680367615](https://github.com/physicsvigilante/opticsim/actions/runs/44680367615). Local ZIP SHA-256 **6c9e82236dc3651d399015d3f44f9b9496ba857c3e2129dbae2d30a7f34f544f** matches the GitHub-declared digest. I read the **nine raw input JSON files, nine per-case full callback reports, and aggregate report**, independently recomputed raw input/report SHA-256 against the aggregate entries, and cross-checked the source input hash in each per-case report. **All case hashes and summary records matched.** This is inspection and cryptographic consistency validation of *recorded native execution*, not an independent rerun of PhyDemo.

| Frozen research case | Archived actual Glass callback route | Native qualification |
| --- | --- | --- |
| m=1.6 | face-12 → face-31 **TIR** → face-23 transmitted, exit 30.000000000000004° | **qualified test-only witness** |
| m=1.5 | face-12 → face-31 **transmitted outward** | not qualified |
| m=√(7/3)+0.0001 | face-12 → face-31 **TIR** → face-23, exit 30° | **qualified test-only witness** |
| m=√(7/3)−0.0001 | face-12 → face-31 **transmitted outward** | not qualified |
| exactly critical | extra/repeated AC callback, no safe BC exit | **not qualified** |
| m=√(7/3)+1e−8 | face-12 → face-31 TIR → face-23; residual only ~9.17e−9 | **withheld despite raw completion** |
| translated m=1.6 | face-12 → face-31 TIR → face-23, exit ~30° | **qualified test-only witness** |
| maxRayDepth=0 | no qualifying route, `incomplete`, truncation **0.08** | not qualified |
| processedRayLimit=1 | only AB/AC partial route, `stopped` | not qualified |

Aggregate artifact totals: **9 attempted, 3 qualified, 6 unqualified**, with **6 rawComplete** in this artifact. For the strongest m=1.6 positive case, actual archived native hit coordinates are **(0,20)** on AB, **(55.1677802067,38.1488672471)** on AC and **(69.3805844687,−29.9431008804)** on BC, in mm/y-up. I checked these values independently against the three finite line equations. Recorded incidence angles are **30°** on AB, **41.790043°** on AC, **18.209957°** on BC; exit is 30°. The AC angle exceeds **asin(1/1.6)≈38.682°**. Actual outgoing direction vectors support reflection/refraction and are not fabricated by the route predicate. The test wraps the existing Glass callback, delegates to the original, then observes resulting points/flags; it does **not** force a route.

**Non-blocking numerical observation N1:** On the **same final source HEAD**, the [quasi-static job 136102029656](https://github.com/physicsvigilante/opticsim/actions/runs/44680367482) logs the *exact-critical* control with native status `completed` and route AB→AC→AC, while the [optical-composition job 136102026291](https://github.com/physicsvigilante/opticsim/actions/runs/44680367615) and its artifact record `failed` with an extra invalid callback after AB→AC→AC. The raw terminal handling therefore differs at the singular critical boundary. **Both reports set qualifiedResearchWitness=false**, so the release-facing classification remains correctly fail-closed. This difference should remain visible in any future regression narrative, not represented as invariant exact-critical raw execution.

The initial research test at **f31dbfd1a4e7b1dde86e73e8e6ba3b4efea66342** failed because an omitted `invalid` face-observer property was treated as invalid. Commit **2abdc96fc3bfd47e1cf3c2099799e7b9c64d1809** corrected this to `hit.invalid===true`. The complete GitHub PR commit history places the frozen protocol before that correction and subsequent analytical implementation. The final success **must not be described as first-attempt-clean**.

All triangle side lengths, ray launch/brightness, exterior 1, selected interior material indices, and numerical stop controls are **explicit synthetic apparatus**. These results demonstrate existing pinned PhyDemo's physical capacity for a chosen three-face path, **not original-source native simulation, native visual detection, textbook answer grading, or new general-purpose authored three-face propagation**.

## 5. Final CI and broader evidence — PASS within scope

I independently requested metadata for all **11 pull-request CI runs** and confirmed each had `head_sha=cbf96405ac7a63da4eead04fb8b0d5974fa7ca06`, `event=pull_request`, `status=completed`, and **`conclusion=success`**. These are the parameter experiment, plane-mirror angular, numerical ray reliability, planar refraction, original refraction pair, quasi-static source motion, curved mirror, deterministic angular query, qualified authoring, unified workflow, and optical composition workflows. The exact-head quasi-static and optical composition job logs each report **1,079 Node24 tests, 1,079 passed, 0 failed**; no skipped tests were reported. Source verification is against both the PR feature tree and an identical GitHub synthetic merge tree.

The optical-composition run also lists `browser-acceptance-evidence` **14603084624** and `hosted-browser-evidence` **14603459036** with successful run metadata. I inspected **their GitHub metadata only** and did **not** download/re-hash these two browser artifacts, nor independently launch Chrome. Their success supports unchanged historical browser regression, **not a new J13-specific browser/visual usability assertion**.

I did **not** run native PhyDemo or Node tests locally; independent work here comprised original-image visual inspection, separate signed physics derivation/numerical calculations, line-geometry checks of raw callbacks, Git identity/diff verification, CI log inspection, and actual artifact SHA-256/input/report hash validation. No Solutions files, unrelated PR #188 work, or unchanged v8/v22 algorithms were reviewed, and no source repository files or branches were altered.

## 6. Findings, disposition and owner decision

- **Blocking findings: none.** The added module answers only what the source mathematically justifies and refuses unsupported material/critical conclusions.
- **N1 — numerical observation, non-blocking:** exact-critical native terminal behavior differs between two successful final-head runs, but is consistently **unqualified**. Preserve both evidence variants when discussing numerical robustness; never infer universal exact-critical native stability.
- **N2 — scope disclosure, non-blocking:** the 1e−5 critical band, [1,4] indices, and restricted 0.1°–30° emergence domain are **conservative contract limits** and cannot be generalized to a complete prism solver.
- **N3 — source and UI disclosure, non-blocking:** no absolute exterior index, quantified “slightly”, source-defined finite geometry, original J13 native rendering, or graded numerical textbook index is available. This is a conditional 2D analytic inverse **plus a separate synthetic native witness**.
- **N4 — CLI hardening, optional:** shared output-helper hostile-process race and ordinary JSON duplicate-key parsing remain outside the scope of this source-bound evidence contract. Avoid broader security/canonicalization claims without additional work.

**Final verdict: CLEARED FOR OWNER DECISION** for **exact head cbf96405ac7a63da4eead04fb8b0d5974fa7ca06 and tree 25efbe0ed82c3b3ab6d11cf7e37815b12925d3f4 only**. This review does **not** merge, deploy, mark ready, revise any original 20-question score, authorize Fresnel-on work, or supersede the owner's release gate. Keep [PR #190](https://github.com/physicsvigilante/opticsim/pull/190) draft/unmerged until the owner decides. If the source/head or its qualification policy changes, review applicability must be reevaluated.

## Primary immutable/CI evidence links

- [Exact source commit](https://github.com/physicsvigilante/opticsim/commit/cbf96405ac7a63da4eead04fb8b0d5974fa7ca06)
- [Frozen protocol original commit](https://github.com/physicsvigilante/opticsim/commit/6fb6625453eb62c24d9d7b40d929b9cfb75d5596)
- [Final native CI run](https://github.com/physicsvigilante/opticsim/actions/runs/44680367482)
- [Final artifact-producing CI run](https://github.com/physicsvigilante/opticsim/actions/runs/44680367615)
- [Source-collection historical run](https://github.com/physicsvigilante/opticsim/actions/runs/44360693719)
- [Pinned builder verification packet](https://github.com/physicsvigilante/review_sandbox/blob/0154c21a40526cfaadf05202b6a06e78ede8fa4e/projects/opticsim/pr-190/BUILDER-VERIFICATION-01.md)
