# Opticsim PR #192 — independent Chat B focused review 01

**Date:** 20 November 2026 (IST)  
**Verdict: CLEARED FOR OWNER DECISION** — limited to the new **conditional J08 mirror-backed slab analytical API**, its **separate synthetic pinned-native/public-v5 illustration**, and the **test-only J02 numerical regression**. This is **not** an unconditional solution of original JEE J08, a new native optical solver, Fresnel/radiometric qualification, a detected optical image, a new J08 Chrome UI acceptance, or permission to merge.

## 1. Exact candidate identity and scope

- **Reviewed Opticsim PR:** [draft PR #192](https://github.com/physicsvigilante/opticsim/pull/192), source HEAD **b4eef0bf4be2ad46eb007573ff994e14e147d595**.
- **Reviewed source Git tree:** **cb7b75df5ac4a2e4e6b1dc7283887da49135db47**.
- **CI-tested GitHub synthetic merge:** **60ea446db3ffcdadf999a4716bd62c85358ae2fd**, independently fetched tree **cb7b75df5ac4a2e4e6b1dc7283887da49135db47**. Ordered merge parents independently checked as production main **cf0366d2b46a0cb88e97bc8d9ec94a29e556ed83** and exact PR head **b4eef0bf4be2ad46eb007573ff994e14e147d595**.
- **Frozen-before-implementation protocol commit:** **20f0a67a348c554c4d5ede4cc6aa882e05469e6c**, directly parented by the above production main. The protocol blob **40187325c1b05a4c96880f7b4e59290aa9af1149** was independently fetched at both the freeze commit and final reviewed HEAD and is unchanged.
- GitHub compare and the PR file list independently identify **11 added files, zero modifications or deletions** (1,006 additions): frozen protocol, three examples, pure analytical module, byte-bound CLI, three J08 test files, one J02 test file and documentation. This change does **not** edit the existing PhyDemo engine, public authoring schema, native algorithm, renderer, historical JEE attempts, workflows, or original source material.
- The authored native documents and protocol specify pinned upstream **811f508d2b070898c241a568b0c167dcb8645251**. No pre-existing pin-bearing files changed in this PR.
- GitHub was rechecked before report publication: PR open, draft and unmerged, with the same head/base/merge identities. This review made no edits to the opticsim repository, no release or deployment, and no change to original JEE solved-question scoring.

## 2. Independently inspected original J08 Problems image

Downloaded historical [run 44360693719](https://github.com/physicsvigilante/opticsim/actions/runs/44360693719) artifact **14454755556** (llm-authoring-evidence) and directly inspected the **Problems-only** image saved within it as **jee-post164-coverage-v1/sources/J08.png**. Its SHA-256 was independently computed as **f851ad695d026000a1310261e00e4a5e1c85e65d3b1a39121cdde2508a5fb572**, an exact match to the archived J08 source manifest. That manifest binds the original path to **08_Ray_Optics_Explanations/03_General_Refraction/Problems/006.png**. The independent image reading agrees with the held [PR #165 audit](https://github.com/physicsvigilante/opticsim/pull/165):

- A plane-parallel plate has refractive index **1.8** and thickness **6 cm**, rests on a plane mirror, and receives a ray at **60 degrees from the upper-face normal**.
- The figure labels entrance **M**, emergence **N**, and the plate-backed mirror; it depicts the two slab traversals and asks their entrance-to-emergence separation.
- **Neither the words nor the figure state a numeric exterior refractive index**. No finite widths, source launch coordinates/brightness, detector or intensity policy are given. Geometry must not be calibrated from the illustration.
- **No Solutions file/image was opened.** Original J08 remains an underspecified numerical input under this project's source-fidelity policy, not an automatically scored solved original problem.

The original upstream archive SHA-256 **03fa29dc8a09f157692ea389354bc7393a96e49f792b60329164c03e56bc5939** comes from the frozen source manifest; I did **not** independently download/re-hash that upstream archive. The separately downloaded historical CI artifact ZIP was independently hashed (section 7).

## 3. Independent physical derivation and mathematical/numerical review

Set the entrance plane at x=0, the ideal contacting mirror at x=t, the slab normal +x, and the incident ray's transverse component +y. If the exterior absolute index is explicitly **n0**, slab index **n1**, and incident angle **i**, entry Snell gives **n0 sin(i) = n1 sin(r)**. A transmitted ray travels from x=0 to x=t with +y change **t tan(r)**. A specular reflection in the x=t plane reverses its x component and leaves the +y component unchanged; its return adds another **t tan(r)**. On exiting into the original medium, Snell returns angle magnitude i and the heading **180 degrees − i** from +x. Thus:

**D = 2 t tan(r) = 2 t n0 sin(i) / sqrt(n1² − n0² sin²(i))**,

for the admitted propagating, non-near-critical branch. D is the **front-surface M-to-N separation**, not detector-to-detector spacing.

For the **separately declared synthetic n0=1**, n1=1.8, t=60 mm and i=60 degrees, independent scalar/vector computation gives **r = 28.7589180039507 degrees** and **D = 65.85855599381419 mm = 6.58585559938142 cm**. The reflected exterior heading is **120 degrees**. This is **only a conditional illustration**, not an original-source unconditional numeric solution.

Independent controls also give **99.92384697865627 mm** for explicit n0=1.33, **32.9292779969071 mm** for t=30 mm at n0=1, and zero front-face displacement at normal incidence. Doubling thickness doubles D; converting mm/cm/m does not alter the physical distance. If n0 sin(i) > n1, entry total internal reflection precludes the requested transmitted mirror return.

The new pure implementation was read in full. It requires exact format, kind, plate/mirror model, single-branch convention, coordinate convention, and length unit; only outsideIndex may be absent. It validates positive finite thickness **1–10,000 mm**, absolute indices **[1,4]**, and incidence **[0,89] degrees** and rejects unrecognized assertions/fields and nonfinite numbers. Absent outsideIndex returns **needs-information / MISSING_OUTSIDE_INDEX / value:null**; it does not assume air. Beyond critical by the **1e−7 sine-ratio margin**, it returns **unavailable** for TIR; within that margin it returns **numerically-indeterminate** and no finite displacement. The **100,000-mm absolute displacement cap**, finite-value check and round-trip residual check fail closed. The near-critical margin is an engineering admission policy, **not a validated universal numerical error bound**. The analytical result always declares **native:not-run**, and never fabricates native face points, detected images or original-source success.

## 4. Raw-byte CLI provenance and refusal review

The standalone scripts/mirror-backed-slab-query.mjs reads and bounds the original JSON bytes (nonempty, at most 1 MiB), reserves an exclusive new output directory through the existing shared authoring helper, writes input.json before parsing, hashes those exact bytes with SHA-256, and separately writes an analytical result or a refusal report. It neither imports PhyDemo nor produces a qualified native scene. Malformed JSON exits rejected rather than pretending to complete.

From the **downloaded exact-head artifact**, independently checked **four J08 standalone input.json → report.json SHA-256 bindings**: missing exterior index, explicit-index conditional result, TIR unavailability and malformed-input rejection. For the three parsed cases, analytical-result.json and report.json agree on the original-input hash and analytical result; every case retains native:not-run. **Zero input-hash or result-consistency discrepancies found.**

Documented limits remain: standard JSON.parse does not reject duplicate JSON keys, and the reused shared output helper is not a new guarantee against hostile concurrent-filesystem races. The new code does not advertise those as security guarantees.

## 5. Actual pinned-native research witness — separate synthetic apparatus

Reviewed test/jee-j08-slab-native-witness.test.mjs, its independently authored canonical v5 input and the exact-head archived research reports. The witness uses real pinned **SingleRay, PlaneGlass, finite Mirror and passive Detector** objects; the test intercepts existing native onRayIncident callbacks, delegates to the original native methods, then records real before/after directions and intersection points. It does not prescribe a callback route or steer rays. Synthetic additions include exterior n0=1, a source at (-100, -173.20508) mm, brightness 0.08, a 420-mm mirror at x=60 mm, a 420-mm detector at x=-10 mm, and **partialReflection:false**. That policy omits Fresnel partial branches but retains native TIR; neither optical power nor an image is certified.

For the baseline completed report the observed order is **Detector → glass entry → Mirror → glass exit → Detector**. Measured interface face points are **(0,0)** and approximately **(0,65.85855599381424)** mm; mirror hit **(60,32.92927799690711)** mm; detector hits have y approximately **−17.320508075688764** and **83.17906406950294** mm. The mirror flips the x direction and preserves the y direction. Status is completed, truncation 0, undefined behavior 0, errors empty.

Independently reconstructed intersection positions and Snell/specular before/after direction vectors **from each archived authored scene's physical inputs**, without choosing intersections from callback reports. For all **27 reported callbacks in the six completed native cases**, the maximum absolute coordinate/direction difference from this independent reconstruction was approximately **1.15e−12**; hits fall within finite declared mirror/detector extents. The five round-trip completions (baseline, translated, explicit 1.33 exterior, half thickness, normal incidence) all follow the actual complete five-event route. The separate no-mirror control completes with only Detector → entry and **no return**. The forced depth-zero case has zero qualified path, native status incomplete and **truncation 0.08**. The one-ray processing-limit case stops after Detector → entry and **is not complete**, despite truncation field 0.

Independently verified SHA-256 for **all eight archived native authored input files** against their respective native report inputSha256 fields, with no mismatches. This cross-check validates archival consistency and real CI-reported callbacks, **not a fresh personal run of the upstream PhyDemo simulator**. The research reports appropriately keep the original question sourceFullySimulated false and nativeImageDetected false.

## 6. Existing public v5 authoring and J02 test-only follow-up

The new fully explicit **examples/jee-j08-mirror-backed-slab-native-v1.json** and test/jee-j08-slab-public-native.test.mjs invoke the unchanged **prepareScene → evaluateDocument → evaluateObservables** route with actual v5 physics components and sampled results. The passing CI test asserts schema/adapter v5, correct genuine compiled object types, a completed native run with no truncation or undefined behavior, save/reopen equality, **two actual glass interactions, one mirror reflection, two detector crossings**, and **two qualified native detector-hit events**. The warnings identify the transmitted-only approximation. Missing exterior index fails authoring; removing the mirror eliminates the return; a stale physical hash suppresses observables. This public-API evidence is supported by inspected test code and CI logs; the new J08 raw research archive is **not** falsely presented as a separate public-observable report file.

The detector is **10 mm outside the slab front face**. Its two hit y positions differ by **D + 20 tan(60 degrees) = 100.49957214519173 mm**, not **D = 65.85855599381419 mm**. The new public test explicitly asserts this distinction. A detector crossing is not a detected virtual image or a measured physically complete power distribution. There is **no new J08-specific browser screenshot claim**.

The only J02 change is test/jee-j02-centroid-median-review-followup.test.mjs. It uses the **unchanged independently reviewed** formal supporting-line reflection orbit and synthetic equilateral L=140 mm fixture. The test covers the exact centroid **(40.4145188432738,0)** mm, two 1e−5-mm perturbations, a point on the horizontal median and another interior point. For each it tests the same nonzero formal translation **(70 sqrt(3),210)** mm (length **140 sqrt(3) = 242.4871130596428 mm**) and refuses to translate this formal unbounded orbit into any native visibility/image-count claim. This addresses PR #191 reviewer note N1 at test level. The old J02 physics and all earlier v5/native/refraction optics were **not re-reviewed**.

## 7. CI, artifact integrity and evidence limits

Independently queried workflow runs bound to exact source HEAD and found **11/11 completed successful PR workflows**: parameter experiments; plane-mirror angular inverse; deterministic planar angular queries; numerical ray reliability; curved mirrors; original refraction pair; unified problem workflow; qualified authoring; quasi-static source motion; optical composition; and planar refraction. Source identity of the CI run is strengthened by direct inspection of [optical-composition job logs](https://github.com/physicsvigilante/opticsim/actions/runs/44693880676) and [angular job logs](https://github.com/physicsvigilante/opticsim/actions/runs/44693880613): both check out synthetic merge **60ea446db3ffcdadf999a4716bd62c85358ae2fd**, whose exact Git tree equals the final reviewed source. Both report **1,105 Node tests, 1,105 passed, zero failed**; the logs include all eight genuine J08 native witness outcomes. Browser and build steps in the optical-composition workflow were successful. No local full-suite rerun was performed by this reviewer.

Downloaded and independently SHA-256 hashed all four relevant ZIP artifacts; all match GitHub's declared digests, and ZIP internal CRC checks showed no damaged member:

| Artifact | ID | Independently verified ZIP SHA-256 |
| --- | --- | --- |
| Historical J08 Problems-source llm-authoring-evidence ([run 44360693719](https://github.com/physicsvigilante/opticsim/actions/runs/44360693719)) | 14454755556 | ec95794b8becfcb10a3819c39063c8c4673cf43f58cb3b6cce3ee523cd755f97 |
| Exact-head llm-authoring-evidence ([run 44693880676](https://github.com/physicsvigilante/opticsim/actions/runs/44693880676)) | 14610375926 | a19fc643615f683bde66b52053807bac23e335618e232a60f5e105501a20cfee |
| Exact-head browser-acceptance-evidence | 14609383953 | 544128fe3c575471b66861d9111c264920c47ce4bd5dc06704540afc75775227 |
| Exact-head hosted-browser-evidence | 14610375897 | 42cf910e0880004a7b9443bbb92ba68d239a4c5e6de51cd7ad540ade974bf187 |

The browser artifacts are **existing regression evidence**, not proof of a dedicated new J08 Chrome scene. The historical source archive hash recorded by the manifest is not independently recomputed in this review. Original source remains unsolved in the frozen metric.

## 8. Findings and final disposition

**Blocking findings: none** within the exact review scope.

**Non-blocking follow-ups / precise limits:**
1. The implementation's human-facing assumptions phrase **“lower-index-UNSPECIFIED exterior”** is misleading: the numerical API also permits n0 > n1 and correctly treats TIR. In a future documentation-only cleanup, prefer **“exterior of unspecified absolute refractive index.”** This does not change the computation or status contract.
2. Keep the 1e−7 critical sine guard and displacement cap identified as conservative **admission policies**, not universal floating-point reliability proofs. If future use expands close to critical, quantify accuracy separately before widening the domain.
3. If later claiming source-complete original J08 simulation, require additional source-authorized exterior medium/apparatus or an explicitly labelled teaching assumption, not inferred “air.” If later claiming physically complete Fresnel power, detected images or a J08-specific browser UI, require a **separate** milestone and evidence. Preserve no-original-solved-score-change policy.
4. Treat existing shared output-helper race and JSON duplicate-key behavior as **known**, not new promises. These do not block this bounded teaching/analysis capability under the stated use policy.

**FINAL VERDICT: CLEARED FOR OWNER DECISION**, for this **exact source HEAD b4eef0bf4be2ad46eb007573ff994e14e147d595 / tree cb7b75df5ac4a2e4e6b1dc7283887da49135db47 / CI merge 60ea446db3ffcdadf999a4716bd62c85358ae2fd**. This is one focused independent review of new analytical/native evidence and test-only J02 follow-up, **not** an unconditional original J08 solution or a release authorization. **Keep PR #192 draft/unmerged until the owner explicitly applies the standing release gate.**

### Evidence anchors

- [Exact-source builder-verification packet](https://github.com/physicsvigilante/review_sandbox/blob/3b45558662b084a378d5735b73fc1fdfc1509705/projects/opticsim/pr-192/BUILDER-VERIFICATION-01.md)
- [Draft Opticsim PR #192](https://github.com/physicsvigilante/opticsim/pull/192)
- [Final reviewed commit](https://github.com/physicsvigilante/opticsim/commit/b4eef0bf4be2ad46eb007573ff994e14e147d595)
- [Frozen protocol commit](https://github.com/physicsvigilante/opticsim/commit/20f0a67a348c554c4d5ede4cc6aa882e05469e6c)
- [CI optical-composition run](https://github.com/physicsvigilante/opticsim/actions/runs/44693880676)
- [CI angular run](https://github.com/physicsvigilante/opticsim/actions/runs/44693880613)
- [Previously cleared J02 PR #191 independent review](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-191/reviews/review-01-chat-b.md)
