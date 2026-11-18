# M36e / conductor_sim PR #88 — Chat B independent R2 review #01

**VERDICT: CHANGES-REQUESTED on the exact pinned HEAD/TREE. DO NOT MERGE.**

This is an evidence-integrity verdict, not a finding that unmodified native physics is wrong.

**Identity and scope.** Production [draft PR #88](https://github.com/physicsvigilante/conductor_sim/pull/88) was OPEN, DRAFT and UNMERGED at final inspection. Actual source HEAD **75ef212d79dc26ff97621fb1f2ed4e287bbed56d**, true native Git TREE **f5be8433b39cf8827c19da1cd0586869347a33f4**, both checked independently with GitHub objects and source-pinned reviewer checkout. Released base HEAD **8bca8e5d1c157e05b3f04e6185e927bd7ee79941**, base tree **523d02e95dbb4791acd630f9c535eb552262c606**. Reviewer: Chat B in a separate GPT-6 conversation (independent context, not human experimental verification). Date: 2026-11-18. Risk R2: original p26 JEE source-answer presentation, offline Chromium, physical/source-evidence integrity. **No production source changed by this review.**

[Exact production diff](https://github.com/physicsvigilante/conductor_sim/compare/8bca8e5d1c157e05b3f04e6185e927bd7ee79941...75ef212d79dc26ff97621fb1f2ed4e287bbed56d) spans exactly seven source-scoped runner/browser, new tests, docs and workflow files. No production physical law, original PDF, FEMM, or inherited generic M5 renderer changed. One pre-existing source apparatus, **ZERO additional original JEE questions**.

## Live source CI (separate from independent reviewer evidence)

The latest production source-HEAD query returned **23/23 completed SUCCESS** checks, including Python 3.10 and 3.12, genuine FEMM5, historical visualization and Chromium, M36b/c/d and dedicated M36e source-native/browser integrity. The earlier source [run #44281302235](https://github.com/physicsvigilante/conductor_sim/actions/runs/44281302235) originally FAILED 1/41 from an overly restrictive test expecting adjacent HTML state/hidden attributes; retained as FAILED. The corrected [branch source run #44281477440](https://github.com/physicsvigilante/conductor_sim/actions/runs/44281477440) and exact-HEAD [PR source run #44281854111](https://github.com/physicsvigilante/conductor_sim/actions/runs/44281854111) succeeded. Source CI alone is not an independent review.

## Original physical source and science — independently verified

Original **POTENTIAL_CONDUCTORS1.pdf, physical p26**, was actually rendered to a page image and visually inspected. [Original PDF p26 image](../evidence/original-pdf-page26.jpg). **Illustration 1** asks potential at R/2 and 3R/2 of a conducting sphere with *symbolic* radius R and charge Q. Illustration 2 alongside it is a **nonconducting** charged sphere and must not be substituted. The source gives no numeric R/Q. First numeric case R=0.10m, Q=+1nC is a TEACHER example; the negative and grounded states are TEACHER hypotheticals.

For a source-free isolated solid sphere, analytic SI equations from Gauss law are:

- V(R/2) = kQ/R; V(3R/2) = (2/3)kQ/R; E(R/2) = 0.
- Signed outer sigma = Q/(4πR²); no real inner charge-density face.
- Vacuum k = 1/(4πε0), ε0 = 8.8541878128e-12 F/m.

| Teacher world | V(R/2), V | V(3R/2), V | E_x(3R/2), V/m | sigma_outer, C/m² |
|---|---:|---:|---:|---:|
| R=0.10 m, Q=+1 nC | +89.8755179226 | +59.9170119484 | +399.446746323 | +7.95774715459e-9 |
| R=0.12 m, Q=-2 nC, centre x=0.025m | -149.792529871 | -99.8616865807 | -554.787147670 | -1.10524266036e-8 |
| R=0.08 m, grounded and source-free | 0 | 0 | 0 | 0 |

Reviewer-authored independent math (not imported from conductor_sim) matched all three newly generated native observations, signed exterior fields, true solid geometry, charge ledgers, and 6 representative physical points per embedded 65×65 potential grid per state. Actual physical shape is a SOLID disk with inner_radius_m=0, stable Sphere A, one outer sigma profile and no source masks. Static state selector is **not time evolution**.

## Independent browser execution and evidence history

Reviewer-authored [Python first-probe source](../reproductions/chat-b-review01.py) and [source-pinned GitHub Actions workflow](https://github.com/physicsvigilante/review_sandbox/blob/review/chat-b-m36e-pr88/.github/workflows/m36e-chat-b-review01.yml) are exclusively in review_sandbox.

- Original [reviewer first run #44284481575](https://github.com/physicsvigilante/review_sandbox/actions/runs/44284481575) confirmed source HEAD/TREE and generated 3 native solutions but then **FAILED** on the reviewer PDF thumbnail path (missing directory). The workflow erroneously displayed SUCCESS because a Python-to-tee pipeline omitted pipefail. **That first run does not count as browser evidence.** Its first logs/artifact are preserved; the reviewer harness was corrected, without editing production.
- Corrected [independent reviewer run #44284846678](https://github.com/physicsvigilante/review_sandbox/actions/runs/44284846678) completed SUCCESS with strict pipefail. It regenerated true native source, rendered original p26, independently computed SI/native/grid, ran real offline Chromium through 3 states, checked no-JS original first frame, tested role HTML/JS injection, and executed ten **new** real-browser/data hostile mutations **once each**. [Exact first completed adversarial JSON](../evidence/chat-b-first-attempt-results.json) and [console record](../evidence/chat-b-console.log).
- Positive Chrome had exactly one active answer card at each selected state, and each visible V(R/2), V(3R/2), |E(R/2)|, outer sigma and unit matched the separate analytic SI and native manifest. The correct source-only heading is **Surface-charge density (one real outer face)**. Original no-JS frame alone was visible. **No HTTP requests, no JavaScript errors**. Malicious authored role text containing an img-onerror payload plus script text was safely escaped; no injected element/script executed.
- Reviewer actually opened screenshots derived from the real Chromium captures: [original state](../evidence/state-0.jpg), [negative teacher state](../evidence/state-1.jpg), [grounded teacher state](../evidence/state-2.jpg), [solid scene detail](../evidence/scene-0.jpg). The juxtaposed original potentials are prominently readable above the slider. Charged-state images still have clear white stair-step wedges at the circular boundary despite 65×65 actual samples. No direct 37×37 comparison was conducted; no pixel-perfect improvement is claimed. Original full-resolution PNGs are retained in the Actions artifact.

### Ten FIRST-COMPLETED unfamiliar forgeries

The **target** is the actual production real-Chromium validator tools/check_m36d_solid_browser.py on generated HTML/JSON copies. It is not the reviewer's independent SI checker. The unmodified export passes all positive cases.

| Probe | Forgery | Actual production browser validator |
|---|---|---|
| A1 | Negative teacher visible V(3R/2) replaced with 9999 V | **REJECTED**, stale/forged visible V |
| A2 | Negative teacher visible outer sigma sign reversed | **REJECTED**, stale/forged sigma |
| A3 | True teacher Q=-2 nC visibly captioned Q=+2 nC while physical values remain negative | **ACCEPTED**, scientifically false visible charge |
| A4 | Grounded teacher falsely captions solved Q=7 nC while retaining the word Grounded | **ACCEPTED**, false grounded charge |
| A5 | Visible teacher radius R=0.12 m changed to R=1.2 m, geometry unchanged | **ACCEPTED**, false input geometry |
| A6 | Printed source falsely claims exact numeric R/Q while retaining SYMBOLIC and other teacher disclaimers | **ACCEPTED**, contradictory fabricated source givens |
| A7 | Remove source teacher-1 hidden attribute; JS auto-hides it on load | **ACCEPTED**; reviewer separate no-JS browser sees both state 0 AND state 1 at once |
| A8 | Forge negative teacher numeric data-native-value | **REJECTED**, native mismatch |
| A9 | Change native-manifest original V(R/2) and matching visible/HTML numeric values together | **ACCEPTED by browser**, but reviewer independent SI **REJECTED** 106.8755179226 versus 89.8755179226 V |
| A10 | Falsify actual embedded source-sampled grid potential at [2][2] to 1,000,000 V | **ACCEPTED by browser**, reviewer source-free embedded-grid SI **REJECTED** 1e6 versus 21.8672131392 V |

**Interpretation:** Seven cases survived the browser-only validator; five involve wrong presentation/provenance/fallback and two require an independent physical layer to reject. Browser-verifier success cannot be used as proof of physical truth. These are integrity-guard gaps, **not findings of incorrect unmodified generated answers**.

## Findings and required corrections

**F-01 — MAJOR, blocking.** Signed net-charge, grounded-Q and radius captions are checked only via substrings, not values. Source [tools/check_m36d_solid_browser.py lines 91–102](https://github.com/physicsvigilante/conductor_sim/blob/75ef212d79dc26ff97621fb1f2ed4e287bbed56d/tools/check_m36d_solid_browser.py#L91-L102) checks whether Grounded or Isolated net Q= appears, but does not ensure the visible charge sign, magnitude, radius or centre matches saved native geometry/observed conductor results. **Reproduced A3/A4/A5 accepted.** Required: numeric/unit-aware comparison of *visible* signed charge, R and centre for all three states, including Q=0 in grounded empty space; hostile browser regressions.

**F-02 — MAJOR, blocking.** The original-symbolic vs teacher-numeric provenance checker is keyword-based. Source [browser verifier lines 61–64](https://github.com/physicsvigilante/conductor_sim/blob/75ef212d79dc26ff97621fb1f2ed4e287bbed56d/tools/check_m36d_solid_browser.py#L61-L64) only requires SYMBOLIC and teacher-chosen somewhere. **A6 accepted** even when the page falsely specifies numeric textbook R and Q; original source p26 visually establishes that claim is false. Required: validate the full original-source assertion and refuse contradictory purported source givens.

**F-03 — MAJOR, blocking.** The visible source sample-grid values are not physically checked by the browser/source verifier. Source [lines 130–155](https://github.com/physicsvigilante/conductor_sim/blob/75ef212d79dc26ff97621fb1f2ed4e287bbed56d/tools/check_m36d_solid_browser.py#L130-L155) checks 65×65 dimensions, geometry, metal region and profile but not actual grid potential/field physics. The existing separate stdlib reference validates manifest native probe samples, **not embedded HTML grid**. **A10 accepted** despite a grossly unphysical in-grid 1,000,000 V value; the reviewer Gauss grid check rejected it. Required: a deterministic independent coordinate-based physical spot-check or verified native provenance binding on the embedded viewer grid. This is not a request for another general physics solver.

**F-04 — MAJOR for required static fallback, blocking.** The real Chromium source verifier launches JS-enabled pages only and JS conceals a missing original no-JS hidden-state contract. **A7 accepted** by target but actual reviewer JS-disabled Chromium showed both original and teacher state simultaneously. Required: enforce original-only visible fallback in an actual no-JS browser run and add an adversarial removal-of-hidden regression.

**F-05 — Informational: physics defense in depth must remain.** A9's fake matching native manifest/HTML values passed browser equality, correctly failed the independent Gauss SI checker. This is not an additional blocker if the separate physics gate remains mandatory, but the browser alone must never be described as science certification.

**F-06 — MINOR visual wording/legibility.** Actual charged screenshots still have white staircase wedges near the real circular boundary. No measured old/new reduction; remain explicit about limits. The inherited generic M5 subtitle says induced surface charge even for the isolated sphere, while the corrected source-only density heading is scientifically accurate. Consider source-scoped subtitle wording without modifying valid general induction viewer semantics.

## Separate scope judgments

| Dimension | Verdict | Basis |
|---|---|---|
| Original source interpretation | PASS for unmodified export; integrity FAIL under A6 | Actual physical p26 visually read, source symbolic |
| Physical/native correctness | PASS within scoped isolated sphere | Independent analytic R/Q/E/sigma, native and embedded unmodified points |
| Source/teacher native coverage | PASS | 1 original apparatus + 2 teacher changes; true solid and one outer face |
| Offline browser positive functionality | PASS | Real Chrome all three source/teacher frames, original no-JS, no HTTP/JS errors |
| Browser observable/provenance integrity | **FAIL** | A3–A7 and A10 forged inputs accepted |
| Source role markup injection | PASS for tested payload | Escaped role text, no executed script or injected element |
| Teacher usability | PASS with limitation | Visible juxtaposed potential answers, legible panels; white grid wedges persist |
| General conductor/3D/motion/JEE30 extrapolation | NOT CLAIMED | Correctly bounded source-specific milestone |

## Release advice / no merge authority

**CHANGES-REQUESTED. Keep source PR #88 DRAFT and UNMERGED.** The minimal fix is to make the source-only verifier/hostile checks actually reject fabricated (i) signed Q and R/centre, (ii) numeric-original source claims, (iii) in-grid potential values, and (iv) broken no-JS source fallback. Recompute and preserve a **new HEAD/TREE** if fixed, rerun required exact-head CI and request focused independent re-review of corrected paths. Preserve old negative attempts. There is no reason to reopen the general Gauss solver or alter unrelated historical viewers.

Even a future independent PASS never gives merge authority: owner must explicitly approve, merge with expected-head guard, verify resulting main has the exact reviewed native Git TREE, and confirm every actual postmerge main-push check SUCCESS.
