# Opticsim PR #193 — Independent focused Chat B review 01

**Review date:** 20 November 2026 (IST)  
**Final verdict: CLEARED FOR OWNER DECISION**  
**Scope:** J11 conditional **3D analytical escape-disc geometry**, conservative numerical/CLI policy, and separately bounded genuine **2D pinned-native meridional research evidence**. This is **not** a review of unchanged v5 PhyDemo Snell/TIR physics, previously accepted J08/J13/J14 optics, or unrelated new functionality. **No merge or deployment authorization.**

## 1. Exact source and frozen-protocol identity — VERIFIED

- PR: https://github.com/physicsvigilante/opticsim/pull/193
- Feature HEAD independently read: **0578fa68fed5ba1f07abedb341423e33da8f694f**.
- Feature Git tree independently fetched: **93e21f3f6ce316f00c4170326b53a467dcf8a2dd**.
- Synthetic CI merge independently fetched: **9d9345350fc003d8d2d45180db4845b58c529660**. Its Git tree is **identical**, **93e21f3f6ce316f00c4170326b53a467dcf8a2dd**, with parents [production main **2a529aeca8cf4960f3c7f285e635c55ae5a130b9**, exact feature HEAD **0578fa68fed5ba1f07abedb341423e33da8f694f**].
- PR status checked independently: **DRAFT, OPEN, UNMERGED**; the production main branch still pointed to the above base when checked.
- Base-to-HEAD GitHub compare: **9 added files, zero modified or deleted pre-existing files**. The new files are one frozen protocol, three examples, one pure analytical module, one CLI, two tests and one explanatory document. No pre-existing renderer, native physics, blocker, schema, CI workflow, historical JEE record or upstream pin is modified.
- Prospective protocol at **bbb40ee6be4d62f910e9e3eefab3d198cd3d4873** has production main as its direct parent and **only the frozen-protocol JSON added**. Its blob SHA **c863e1398f4d714a4ab9677159c5132eb1e1b85d** matches the final HEAD. Its nine prospective cases therefore predate new implementation and tests.
- Native v5 pin **811f508d2b070898c241a568b0c167dcb8645251** is retained in the frozen protocol and in the archived native input's upstreamCommit field.

## 2. Original JEE J11 Problems image — INDEPENDENTLY INSPECTED

I downloaded GitHub Actions original coverage artifact **14454755556** from run **44360693719**, independently hashed its complete ZIP (SHA-256 **ec95794b8becfcb10a3819c39063c8c4673cf43f58cb3b6cce3ee523cd755f97**) and verified all member CRCs. I extracted and **visually read** the **Problems** member **jee-post164-coverage-v1/sources/J11.png**, not any Solutions image. Its independent SHA-256 is **80dc5c054c8bfe0667e1125cb68ad3dd02c28c71d155d826437084980de819b9**, exactly the archived source-manifest J11 image hash and mapped original path **08_Ray_Optics_Explanations/04_Total_Internal_Reflection_TIR/Problems/005.png**.

Actual image content: an *isotropic point source* at symbolic depth **h** below a water surface, a floating *opaque disc* placed on the water surface, the requirement that the bulb not be visible **from the surface**, and the water's index **μ**; it asks for minimum disc radius. The image does **not literally state** a numerical depth, numerical water index, numerical index for the upper medium, a particular observer/pupil, or finite interface apparatus. Treating exterior index 1 as a *declared water–air convention* would be a further assumption, not an observed numerical source field. The author's centered, infinitely thin disc in the exact interface plane is an explicit idealization, not an imaged apparatus. Thus the model correctly refrains from claiming an original-source complete numerical solution or actual eye visibility. The historical underlying source-archive SHA-256 recorded in the manifest was **not independently rehashed from the underlying source archive**; the relevant **J11 PNG itself and its archive member** were independently checked.

## 3. Independent all-azimuth mathematical derivation — PASS

For source position **(0,0,−h)** with **h>0**, upward polar angle **θ** and arbitrary azimuth **φ**, the straight-line interface hit is

**(x,y) = (h tanθ cosφ, h tanθ sinφ)**, hence **ρ=h tanθ** for *every* azimuth. If **n1>n0>0**, Snell's law permits strictly propagating direct transmission for **0≤θ<θc**, where **θc=asin(n0/n1)**. The union of interface hits is the open disk **ρ<Rlim**, with

**Rlim = h tanθc = h n0 / sqrt(n1²−n0²)**.

A centered perfectly opaque disc of **R≥Rlim** covers every strictly transmitting direct geometric ray. For any **R<Rlim**, choose **ρ** strictly between R and Rlim and **θ=atan(ρ/h)**; then θ<θc, transmission is allowed, and its hit lies *outside* the disc. An off-center smaller disc cannot cover the full open footprint either: two near-diametrically-opposite footprint points force enclosing radius arbitrarily close to Rlim. No finite disc is sufficient when **n1≤n0** on an infinite plane because incidence directions approaching **θ=90°** are transmissible and have **ρ→infinity**. These conclusions concern *single-interface geometric direct transmission only*, not physical disc-edge diffraction or observer detection.

At **exact critical incidence** the formula gives the *supremum* of strictly transmitted hits; **no grazing propagating exterior ray is asserted**. The code, tests and docs preserve this boundary distinction. I independently checked the necessity counterexample for **h=100 mm, n1=1.5, n0=1**: **Rlim=89.44271909999159 mm**; a disc radius **0.8 Rlim=71.55417527999327 mm** fails at **ρ=0.9 Rlim=80.49844718999243 mm**, where **θ≈38.8335251°**, and **n1 sinθ≈0.94058957<1**.

Independent trigonometry also reproduces the frozen examples: **h=60 mm, n1=4/3, n0=1 → 68.0336051416609 mm**; **h=100 mm, n1=2, n0=1.5 → 113.38934190276817 mm**. The explicit synthetic **100 mm, 1.5, 1** case gives **θc=41.810314895778596°** and **Rlim=89.44271909999159 mm**. No synthetic number is attributed to original J11.

## 4. Source/API/CLI review — PASS WITH DISCLOSED LIMITATIONS

I inspected all nine HEAD files. The analytical API requires exact version/model/geometry/emission and literal symbolic **h, mu, n_outside** or explicitly supplied numeric material indices. It rejects unsupported/extra fields, nonfinite or nonnumeric values, depths outside **1–10000 mm**, indices outside **[1,4]**, and unsupported units. The missing numeric outside index returns **needs-information / MISSING_EXTERIOR_INDEX**, not air assumed; **n1≤n0** returns **no-finite-coverage**; positive relative index contrast **≤1e−8** returns **numerically-indeterminate**; and radii exceeding **1,000,000 mm** are also withheld. The stable difference-of-squares implementation uses **(n1−n0)(n1+n0)**, avoiding an avoidable near-equal cancellation. These guards are conservative admission limits, **not formal floating-point or physical-visibility error certification**.

I inspected the CLI's raw-Buffer input preservation and SHA-256-before-JSON-parsing path. From the final archived artifact I independently recomputed the **exact input-byte SHA-256 for all five J11 CLI evidence directories** (symbolic, explicit numeric, missing exterior, inverse-index, malformed). They matched every report; all four successful analytical cases also had consistent analytical-result input hashes; all outcomes report **native:not-run**, **originalJeeSolved:false** and no fabricated 3D source/detector. The malformed JSON report retained original input bytes and correctly rejected it. The implementation uses normal JavaScript **JSON.parse**, which does not reject duplicate keys, and inherits the pre-existing shared filesystem helper's concurrent-hostile-path limitations. Neither a duplicate-key canonicalization/security guarantee nor absolute race safety is claimed; these are **disclosed, nonblocking limits** within this task.

## 5. Independent archive-level native 2D assessment — PASS, strictly non-3D

The actual saved native scene is **ray-optics-2d schema v5** with original pinned upstream ID, a **single** upward synthetic ray at **(0,−100 mm)**, interface at **y=0**, **negativeIndex=1.5**, **positiveIndex=1**, **partialReflection=false**, brightness **0.08**, and no physical disc, detector, 3D source or eye. The test's event observer delegates to the real native **onRayIncident** once and records pre/post ray vectors; it does not inject a ray path. These are archived genuine **2D** native callback records, not my own newly executed native simulation.

I independently parsed and verified the **12 input/report pairs**, their recorded per-member byte lengths and SHA-256 digests against the aggregate, the aggregate counts, the recorded actual hit points, signed incident directions, refracted/reflected vector directions and safe-witness status. All qualified cases agreed with independent trigonometry and Snell law: largest observed hit-coordinate discrepancy **≤5.7×10⁻¹⁴ mm**, independent transmitted-angle discrepancy **≤6.5×10⁻¹²°** across the checked cases. Results:

- **7 qualified meridional transmissions**: 0°, 15°, 30°, 41°, θc−0.0001°, −30° cross-section, and translated 30°. The near-below hit is **x≈89.44240494 mm**.
- **2 qualified meridional TIR events**: θc+0.0001° and 50°; saved reflected direction correctly reverses the normal component.
- **3 correctly withheld controls**: at exactly θc, one raw native **TIR** callback is explicitly *not* promoted because the sine boundary is unresolved; depth limit 0 yields **incomplete** with truncation **0.08**; processed-ray limit 1 yields **stopped** even though an interface transmission callback exists.

No 2D trace or detector miss is used to certify a 3D circular disc, continuous light coverage, an observer's visibility, or the original JEE apparatus. The source-only model's **native.status=not-run** is accurate.

## 6. CI and artifact provenance — VERIFIED FROM GITHUB, NOT LOCALLY RERUN

All **11** GitHub Actions workflow records independently checked were **completed/success**, each attached to PR #193 and exact feature head **0578fa68fed5ba1f07abedb341423e33da8f694f**:

| Workflow | Run |
| --- | --- |
| Quasi-static source motion | 44700432744 |
| Deterministic planar angular query | 44700432501 |
| Numerical ray reliability | 44700432460 |
| Curved mirror | 44700432415 |
| Parameter experiment | 44700432486 |
| Original refraction problem pair | 44700432376 |
| Plane-mirror angular inverse | 44700432347 |
| Qualified authoring | 44700432609 |
| Optical composition | 44700432540 |
| Planar refraction | 44700432447 |
| Unified problem workflow | 44700432490 |

I retrieved **actual job logs** for optical composition job **136167191567** and deterministic angular job **136167190939**; *each* reports **1,116 tests, 1,116 pass, 0 fail** and the same 12 named native J11 event lines. The log step records also show passed existing native/Chrome/build tests; no J11-specific 3D Chrome scene is asserted.

I downloaded and independently verified full GitHub ZIP SHA-256 **and every ZIP member CRC** for these final optical composition artifacts:

| Artifact | ID | Verified ZIP SHA-256 |
| --- | ---: | --- |
| llm-authoring-evidence | 14612681859 | 1d56d5fa3b665f25240d804a7477fbe6247d913a8701b0b9682ba529f4ebc812 |
| browser-acceptance-evidence | 14612303868 | 04afea1e266bd03c897d6a165859cd8140ca20a532eb118d8ed1827d62078eca |
| hosted-browser-evidence | 14612228947 | 9ba4fab3109b892af4fd9bc461f0c9c1227769df43873b7311ec6306b16467ec |

All match GitHub artifact metadata. The first of these supplied the 12 native pairs and five CLI cases independently checked above. No local Node24 full-test run, fresh PhyDemo execution, original source-document archive reconstruction, or J11-specific browser run was performed in this review. Those distinctions are **evidence limits, not hidden independent experiments**.

## 7. Findings, blockers and release gate

**Blocking findings:** **None** in the newly scoped J11 conditional mathematical model, conservative API/refusal logic, preserved exact-source identity, or archived 2D native nonclaim.

**Nonblocking limitations/owner notes:** (1) Original wording says **“from the surface”** and does not numerically state the exterior index or a precise observer; preserve the **conditional geometric** claim and do not rewrite original JEE completeness. (2) The disc is an explicit ideal *centered, interface-plane* surface model; no true 3D simulator or photometric/eye model exists. (3) The exact-critical native callback must remain **withheld** regardless of raw TIR label. (4) Existing JSON duplicate-key and concurrent-filesystem security boundaries are outside this one-file-family physics review. (5) A full native rerun and original entire source-archive rehash were not conducted by Chat B; raw logged events, original image, and final ZIP/member hashes **were** independently inspected.

**Final verdict: CLEARED FOR OWNER DECISION** for exact **HEAD 0578fa68fed5ba1f07abedb341423e33da8f694f**, exact **tree 93e21f3f6ce316f00c4170326b53a467dcf8a2dd**, and tested synthetic merge **9d9345350fc003d8d2d45180db4845b58c529660**, **subject to unchanged exact-source identity and the separate standing owner release decision**. Keep [PR #193](https://github.com/physicsvigilante/opticsim/pull/193) **DRAFT/UNMERGED** until that decision. This review grants **no** authority to merge, deploy, rewrite earlier JEE solved percentages, or treat analytical geometry as a native 3D visibility measurement.
