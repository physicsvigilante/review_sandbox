# Chat B — Opticsim PR #161 combined planar integration + R5 evidence-safety review

**Date:** 18 November 2026  
**Verdict: CLEARED FOR OWNER DECISION** — only for the exact draft integration candidate below. **P0: none identified. P1: none identified.** Two nonblocking follow-ups are documented. This is **not** permission to merge, release, deploy, or clear any other held branch. The outstanding branch-protection issue #123 remains unresolved.

## 1. Identity, source ancestry, and unchanged-blob proof

Reviewed [Opticsim draft PR #161](https://github.com/physicsvigilante/opticsim/pull/161), exact HEAD **09ad081a34ced0fa969affc1bf54766cabffb04a**, actual Git tree **1b2caf6186c8eaf678963238d2292001b2fa9667**. At review, the PR was open, draft, mergeable and unmerged, and production main remained **d3509e82fb65d81aabe336666851f8f2962623f4**. I checked GitHub's raw Git commit objects, raw recursive Git trees, base/HEAD comparison, live PR state and main branch, rather than accepting the PR description as proof:

- Original production main: Git tree **45ff3bcd9093a527652f13f76c3cc0b02826642f**.
- First integration commit **b43607e5d6af0d72d9c20657884d2e9d2cf99c12**, single parent **d3509e82...**, Git tree **292e5ff46bd041dfbd94f898108fcb5841af80ba**.
- Final audit-document commit **09ad081a...**, single parent **b43607e5...**, Git tree **1b2caf61...**.
- Synthetic GitHub Actions merge **2583730832daa310bef1dcaa1fcfecffb3e58c5a**, Git tree **1b2caf61...**, ordered parents **[d3509e82..., 09ad081a...]**. Its tree is **identical** to the exact review candidate, not merely similar.
- The main-to-HEAD comparison is **two commits ahead, zero behind**, exactly **13 added paths**, **zero existing files modified/deleted**. The production-base tree has none of these 13 paths.

I compared the **actual Git blob IDs** of every source file in the integrated tree against the declared frozen source trees, not merely the path names:

| Group | Integrated path | Exact blob SHA | Origin; identical |
| --- | --- | --- | --- |
| A | src/planar-apparent-depth-query.js | 7ef2ebf2f203ed7cf5d9965a2cded5ee4aab91c9 | PR #144; yes |
| A | scripts/planar-apparent-depth-query.mjs | 5b3f6d9407b3ba6d25d5d68de84187000a4bad0f | PR #144; yes |
| A | test/jee-apparent-depth-query-v1.test.mjs | 45bd176f053ff5f952b21edec5010d699091bae9 | PR #144; yes |
| A | docs/JEE-PLANAR-APPARENT-DEPTH-QUERY-V1.md | ed1b6d59d8c0abe5e1611840a57e2e489d5f3282 | PR #144; yes |
| B | src/planar-observer-point-query.js | 19697ec4223a08dbb4b334d84ff164b745ff2c1c | PR #150; yes |
| B | scripts/planar-observer-point-query.mjs | 0456ae2e7b8125dcc30bd6879ffaa0d836c62339 | PR #150; yes |
| B | test/jee-observer-point-query-v1.test.mjs | 46d571c7f31d6f49b749101ddf5f0d700582f9ac | PR #150; yes |
| B | docs/JEE-OBSERVER-POINT-QUERY-V1.md | b4734f042d728ad0310eb93441a341717fdbe399 | PR #150; yes |
| C | scripts/jee-observer-native-witness.mjs | 9b3ceae21656f55351862a25bff634a5b728145e | PR #159 final R5; yes |
| C | test/jee-observer-native-witness-v1.test.mjs | fadc858ec31e2935f460df153d58e73cd5d8fd45 | PR #159 final R5; yes |
| C | examples/jee-observer-native-witness-v1.json | 17896e0db7daaef546dc0aa8ad0dede6ac738797 | PR #159 final R5; yes |
| C | docs/JEE-OBSERVER-NATIVE-WITNESS-V1.md | ef90b75165ad76a4102557ed2b49b9de980fb1f5 | PR #159 final R5; yes |

The thirteenth path is **docs/JEE-PLANAR-INTEGRATION-CANDIDATE-V1.md**, new audit-only document, blob **ffc2bfd1473bddfe9f1ae34474d353f00b805326**. Sources were independently compared to PR #144 HEAD **aea25a9b480260e2498229d80f7f6cbe3d4ac574** / tree **e1fe378b7070ef6be53f34faa798e75774f877a5**, PR #150 HEAD **0fb738f69b3257113c73dbf9d1f2917037daa5cc** / tree **8cd6b5df7cceaf68d04deca4926eb91245986216**, and PR #159 HEAD **70ff5d34140e0d29c6a22c70897322d8459db0e8** / tree **c6bb20d8fa6c0678731ca8bf237a559cfcac4455**. **12/12 matches.**

No production native adapter, native PhyDemo, canonical schema, authoring, observation projector, browser, existing CI workflow, or other existing source file was altered. In particular there is no modification to src/adapter.js, src/contract.js, src/authoring.js, src/observables.js, or src/planar-media.js.

## 2. Independent R5 correction review — R4 P1 is cleared

This is a **new source review of integrated C/R5**, not an inherited approval from the held PR #159. Frozen [PR #157 R4 review](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-157/reviews/review-01-chat-b.md) correctly requested changes at its own historical SHA **c1bcf2b5537767e6c0bd710590f9a763b0db40d7**: the reflected direction was dereferenced before checking its shape and could throw, losing the structured final report. The R4-to-final-R5 comparison changes only the witness script, witness tests and witness documentation (eight commits ahead, none behind).

**Source check:** [integrated witness script, lines 165–198](https://github.com/physicsvigilante/opticsim/blob/09ad081a34ced0fa969affc1bf54766cabffb04a/scripts/jee-observer-native-witness.mjs#L165-L198) now executes **if (!finiteUnit(r.direction)) return false** before the first access to reflected direction x/y in the specular-distance calculation. The finite-unit predicate requires a non-array object, finite x and y, and unit norm within 1e-7. Consequently omitted, null, primitive, array, empty, partial, NaN/infinite and nonunit direction shapes return false before the original R4 fault location. Both positive-hit and one-interaction measured-zero cases route this false value to **native-evidence-unavailable**, with a null accepted hit/direction and exit 2; the final report is saved ([lines 206–347, 423–463](https://github.com/physicsvigilante/opticsim/blob/09ad081a34ced0fa969affc1bf54766cabffb04a/scripts/jee-observer-native-witness.mjs#L206-L463)).

**Separate report-preservation boundaries:** execution or observable-projection exceptions are caught at **lines 411–422**, yielding **native-infrastructure-error**, exit 2, a saved report and no accepted native hit. Unexpected errors *during classification* are caught at **lines 427–443**, producing **native-evidence-unavailable / NATIVE_RESULT_QUALIFICATION_EXCEPTION** and a null actual detector hit; the malformed raw readings are not serialized again. The deliberate thrown getter in the test triggers the **earlier projection boundary**, not the latter classifier catch. Its saved infrastructure-refusal result is correct; it is not evidence of a PhyDemo-produced bad ray. The latter catch is source-inspected but not independently exercised by that getter test.

**Physical sign check:** For source-to-observer oriented unit normal n, tangent t=(-n_y,n_x) and the one explicitly **authored** incident direction d_i=cos(alpha)n+sin(alpha)t, the required reflected vector is

> d_ref = d_i - 2(d_i · n)n = -cos(alpha)n + sin(alpha)t.

It **must preserve the signed tangent**, not just the unsigned angle or backward normal sign. At normal 0° and the native witness's analytical heading near **+10.61610894°**, the physically expected reflected vector is approximately **(-0.98288359,+0.18422770)**; flipping tangent gives **(-0.98288359,-0.18422770)**, about **0.3684554** apart in vector norm, far outside the fixed 1e-7 specular limit. I independently recomputed this formula and its invariance for normals 0°, ±90°, 180°, 37° and an additional 123°, for both tangent signs. At ±18.5° the signed-tangent flip gives Euclidean vector error approximately **0.63460931** in each rotated frame. The script also verifies reflected normal sign, reflected-branch angle, native first-incidence angle and authored incident-angle magnitude against independent 1e-5° / 1e-7° constraints. This authored SingleRay heading is **known input**, not a separately measured native incoming direction.

**Native event integrity:** Code inspection confirms completed/fresh hash-matched native execution; one emitted ray; native-method-qualified source, interface, detector count and full hit list; matching complete detector counts; exactly one interface encounter and one transmitted branch for positive hit or one-interaction zero; only an allowable Fresnel reflected branch; correct source/observer indices and side; explicit Fresnel policy; finite unit outgoing directions; consistent first-event angles; nonnegative branch powers; no TIR, invalid observation or native truncation. A zero-encounter/zero-detector native completion correctly has an **unavailable first event** without fabricating one. Absent or contradictory counters/methods/events, stale digests and incomplete runs refuse evidence. The native first-interface *crossing coordinate* is not measured or invented.

**R5 conclusion: the historical R4 P1 is corrected at this exact integrated source.** I found no new P0/P1 in the reviewed R5 paths.

## 3. Independent analytical/physical interface check

The three new public entry points remain distinct rather than implicitly merging analytical predictions into native observations:

| Capability | Strict input contract | Permitted result |
| --- | --- | --- |
| A, explicit incidence | opticsim-planar-apparent-depth-query-v1; explicit source, plane, indices, units and requested finite angle or paraxial limit | Conditional finite-angle virtual-axis intercept or expressly requested paraxial limit; native **not-run** |
| B, source + observer | opticsim-planar-observer-point-query-v1; explicit source/observer, oriented plane, indices and units | Conditional one-interface stationary Snell root, proposed source heading and predicted crossing; native **not-run** |
| C, optional physical witness | opticsim-observer-native-witness-v1 wrapping B plus required brightness, Fresnel toggle, run preset, finite tangent-aligned detector and tolerances | Separately authored PhyDemo SingleRay / PlaneGlass / Detector; one measured finite-detector hit, measured zero, miss or withheld/error result, with independent evidence fields |

All three have separate CLIs, format IDs, report/evidence formats and tests. A/B do **not** silently run native, invent a brightness/detector, or advertise a perceived image. The C apparatus is explicitly composed from B's conditional ray direction; the **native forward trace** decides actual interaction and detector observations, rather than the program prescribing the native ray's route. Common world frame is x-right/y-up, with the interface normal from source/negative medium toward observer/positive medium. I checked the unchanged native SingleRay y inversion and planar-interface compilation conventions and the first-event observation projection to confirm this sign interpretation.

**Independent numerical cross-check:** Using the witness's documented geometry **S=(-60,0) mm**, plane x=0 and normal +x, **O=(100,40) mm**, indices **1.5 → 1**, solving the stationary one-interface Snell relation yields crossing **(0,11.2461557712) mm**, incident angle **10.6161089413°**, transmitted angle **16.0419777084°** and signed Snell residual about **5.6×10⁻¹⁷**. The finite-angle virtual-axis depth computed independently from Snell geometry is **39.1118338185 mm**; the observer-line back-extrapolation gives the same **39.1118338185 mm**; the *separately defined paraxial limit* is **40 mm**, not interchangeable with the finite-angle value. This independent arithmetic validates the intended relationship across A/B/C for this representative input; it is **not** a claim that I executed the project's original scripts. The builder's real native positive control independently reports a detector hit approximately **(100,40) mm**, with arrival error **1.42×10⁻¹⁴ mm**.

The source tests cover reversed signed tangents, rotations/translations, unit conversions, equal/different indices, on-axis nonidentifiability, TIR/critical and grazing withholding, world-rounding limits, input refusals, original-byte/hash retention, genuine pinned-native positive controls and source-vs-native distinctions. All three test files execute on the **same integrated tree**. No changed common engine or public schema files introduce a cross-feature collision.

## 4. CI and evidence provenance independently checked

GitHub's Actions runs API for the exact PR HEAD returned **11 workflows, all completed successfully**. I inspected **decoded job logs**, not just PR check labels:

- [Integrated optical composition #44329347455](https://github.com/physicsvigilante/opticsim/actions/runs/44329347455), job **134889188157**: **832 tests / 832 pass / 0 fail**; native witness, signed-reflection and missing-direction markers present; native, build and ordinary Chrome browser acceptance pass (**27 checks / 15 screenshots**, Chrome 157.0.8103.50).
- [Integrated plane-mirror #44329347588](https://github.com/physicsvigilante/opticsim/actions/runs/44329347588), job **134889189837**: **832 tests / 832 pass / 0 fail** and the same required JEE regression markers.
- [Final standalone R5 plane-mirror #44328323494](https://github.com/physicsvigilante/opticsim/actions/runs/44328323494), job **134885546035**: **822 tests / 822 pass / 0 fail**. Its exact HEAD also has **11 successful workflows**.
- Actual markers in decoded integrated logs: **JEE_OBSERVER_NATIVE_WITNESS** (genuine observed hit), **JEE_OBSERVER_NATIVE_FRESNEL_TWO_BRANCH_CONTROL**, **JEE_OBSERVER_SPECULAR_REFLECTION_ADVERSARIAL** (**10 actual pinned-native full-Fresnel positive cases**, **40 injected contradictory summary cases refused**), **JEE_OBSERVER_REFLECTED_DIRECTION_MISSING_MATRIX** (**22 injected malformed direction records**, all refusal reports saved), **JEE_OBSERVER_NATIVE_REAL_ZERO_CONTROLS** (**two separately authored genuinely executed native zero cases**) and **JEE_OBSERVER_NATIVE_EVENT_INTEGRITY_MATRIX** (**22 synthetic corruptions refused**).

The tests' intentionally fabricated hash-matched summaries and completed zero counts probe **classifier behavior**, not native truth. The separately authored genuine detector-zero controls are **not claimed to measure a zero for the original observer-directed witness scene**. The earlier two R5 intermediary source heads had **821/822** due to an erroneous expected fault stage in a test-only injected getter; the final exact R5 source corrects that assertion and has green exact-head runs. No failure is concealed or retrospectively rewritten.

**Reviewer provenance:** I independently inspected exact Git objects/blobs, source and tests, native-adapter/observable boundaries, CI run metadata and decoded logs, and recomputed signed optical and apparent-depth geometry using separate arithmetic. **I did not execute Node tests, install or run the pinned PhyDemo package, launch Chrome, or create native optical measurements myself.** All native and browser results above remain attributed to **builder CI**. A matching digest establishes freshness relative to an authored canonical scene, **not cryptographic authentication of real rays**; mutation tests intentionally bypass that distinction.

## 5. Findings / residual risks

**P0: none. P1: none.** The R4 malformed-reflection P1 is specifically resolved and verified against both result paths. No acceptance of a forged hit, fabricated image or synthetic zero was identified in the reviewed source.

**N1 — nonblocking test coverage improvement: direct classifier exception branch.** The R5 hostile getter regression demonstrates a durable **native-infrastructure-error** because structured cloning/projection raises before the evidence classifier. It does **not** exercise the later **NATIVE_RESULT_QUALIFICATION_EXCEPTION** catch. Static control flow is fail-closed, and the critical missing/null reflected-direction matrix exercises normal refusal/report persistence, so this is **not a P1**. A future test could inject an otherwise projection-qualified malformed record that triggers only the classifier's catch and assert a saved report, null hit and exit 2, without claiming it was genuine native output.

**N2 — nonblocking cross-capability regression improvement.** In a future test, feed B's computed signed incident angle into A's explicitly finite-angle contract for the same source/interface and assert agreement between the two conditional virtual-axis intercepts across both signs, rotations, unit conversions and near-boundary refusals. The present APIs are independent and their geometry is consistent in the reviewed representative case; I found no new integrated defect. This would make the present cross-interface mathematical consistency harder to regress.

**Scope limits (not release claims):** Full Fresnel energy conservation, polarization, continuous illumination, diffraction, image formation, a model eye, complete optical history, universal observer arrival, inferred source authenticity, and multi-interface inverse solutions are **not certified**. Native detector events are finite sampled data. A completed native zero means zero crossings of **that detector**, not invisibility. The two analytical entry points always remain **native not-run**.

## 6. Disposition and owner hold

**CLEARED FOR OWNER DECISION** at exactly **09ad081a34ced0fa969affc1bf54766cabffb04a** / tree **1b2caf6186c8eaf678963238d2292001b2fa9667**, for this **13-file planar-only combined candidate**. The source-C final R5 code **passes this independent scoped safety review**, including the correction that previously blocked R4. This verdict does **not** retroactively change the accurate historical CHANGES REQUESTED verdicts at PR #151/#153/#155/#157, clear excluded v14–v19/native parallel-beam, earlier alternative apparent-depth or directional-footprint research, or merge PRs #144/#150/#159.

Production main remains unchanged. PR #161 must remain **draft/unmerged** pending a **separate explicit owner integration decision** and the ordinary release/branch-safety controls. [Issue #123](https://github.com/physicsvigilante/opticsim/issues/123) was independently checked **open**, and the main branch was **unprotected** at review; this review does **not** resolve or waive that release-safety item. No Opticsim source files, historical reviews, releases or deployments were modified during this review.

**Final verdict: CLEARED FOR OWNER DECISION.**
