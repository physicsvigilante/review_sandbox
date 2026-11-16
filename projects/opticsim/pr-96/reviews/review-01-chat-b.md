# Independent Chat B R2 numerical research/evidence review — Opticsim PR #96

**VERDICT: PASS — FOR BOUNDED NUMERICAL RESEARCH/EVIDENCE ONLY.** This does **not** approve native optics, any change to critical-angle or intersection algorithms, a numerical tolerance, point-error bound, source interpretation, Stage-2 measurement withholding, the disposable CI workflow, or a production merge. **KEEP PR #96 DRAFT AND UNMERGED.**

**Date:** 2026-11-16. **Source PR:** https://github.com/physicsvigilante/opticsim/pull/96; reviewed exact head **2f705f5167666b2fc2c7cd4de9572e8baded119f**, base/main **50dd0f4d9530d0a61bb4c7064c4326a8ac0ce518**, pinned PhyDemo **811f508d2b070898c241a568b0c167dcb8645251**. Independent review framework: https://github.com/physicsvigilante/review_sandbox/blob/main/PROTOCOL.md and https://github.com/physicsvigilante/review_sandbox/blob/main/REVIEW-RISK-POLICY.md. Full request: https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-96/REQUEST.md.

## 1. What was independently inspected versus executed

I read the central R2 request/status/prompt/protocol/risk policy; exact-head Opticsim AGENTS.md; the original independent PR #92 and PR #93 numerical research reviews; the scope/hold on PR #94; **all five** new PR #96 files; production base finite-hit exact and single-owner diagnostic code; and pinned upstream PhyDemo geometry.linesIntersection and its finite-segment, forward-ray, squared-step predicates. I verified GitHub base-to-head and protocol-to-head identities, exact-head CI, both historical setup-failed workflow logs and original artifact bytes.

I **independently downloaded original GitHub Actions ZIP artifact 14229080814** using the connected GitHub account. In a disposable local directory, I wrote **new** Python 3.13.5 binary64 sign/exponent/mantissa → common 2^-1074 **integer lattice** → cross-product determinants and reduced integer t/u. This program did not import or execute the developer's Python Fraction checker, the production JS audit, or its generated reference. I independently reproduced the randomized xorshift/Fisher–Yates schedule and rehashed the exact archived files. Separately, Node 22.16.0 recomputed all six serialized scene hashes and all 36 report-native fingerprints; a new JavaScript reconstruction of the pinned *global-coordinate* linesIntersection operation order tested all archived TAP samples against the serialized native points and pinned geometric acceptance predicates.

**Evidence boundary:** I did **not** execute any new PhyDemo/native simulator trial, Chrome/browser run, original textbook/source interpretation, native memory-bit capture, or an uninstrumented same-event counterfactual. The genuine native trials were run by GitHub Actions and **inspected** here. Local Python and JS were offline independently authored audits of preserved JSON data; source-head CI was inspected rather than rerun locally.

## 2. Preregistration, source scope and provenance

The six cases and protocol were separately committed at **3bd989e17ed47932f218a4b339158d59647c9fb2** at **2026-11-16 13:04:22 UTC**. Its sole added file is the frozen PROTOCOL.md; its Git blob **bae6dd6bd377283f48a80fa72874423fbb426a02** is *identical* at the reviewed head. The initial PR #96 CI run began at **13:06:44 UTC**, after that commit. The runner's blob **e536a97e1b0efc005da01cba3c818ec30e72e5b7** is identical at the first attempted head **89bd636b0e828e49d447e56f23d5314415202509** and final head. Later corrections changed only the disposable workflow build prerequisite and Python input-path default; the six-case runner and deterministic schedule were **not changed after observing outcomes**. The earlier audit-failed run and successful run have byte-identical inputs.json and identical 36-slot schedules.

The six synthetic cases are subcritical tilt −23° with shift (−350,+220) at critical−7°; supercritical tilt +61° with shift (+130,+80) at critical+7°; critical shift (−380,+260); critical tilt −23°; critical tilt +61° with shift (+120,−220); and critical tilt +14° with shift (−170,+330). All use the same 6000×1000 mm, inside-index 1.6/outside-index 1.3 polygon family and a single source. I independently reconstructed their authored rigid transforms, coordinates, directions and six serialized document hashes; the maximum independent Python-vs-JS transform-coordinate roundoff was about **4.55e−13 mm**, with source/direction values matching. The protocol constrains the numeric construction, but does **not** preregister a precomputed scene hash; scene hashes are generated before trials in inputs.json and checked for identity per trial.

GitHub comparison from production base to reviewed head shows **five added research-only files, 542 additions, zero deletions**: frozen PROTOCOL.md, runner run.mjs, exact-check.py, README.md, and the disposable workflow. No production src/, vendor, numerical cutoff, physical scene schema, native ray propagation, Stage-1 canonical output, Stage-2 policy or public UI files changed. PR #96 remains draft, open, unmerged, and still had the pinned head when checked.

## 3. Original GitHub CI artifact: independently verified bytes

**Original newly executed native research CI:** https://github.com/physicsvigilante/opticsim/actions/runs/43872962563 — success, exact PR head. GitHub test-merge checkout **202c474e0a8656ac11e1d385e4f1e418a1d2ec97** has exactly the production base and reviewed head as parents; it is *not* a new production merge. The CI log shows Node **v24.19.0**, pinned setup, fresh-process research runner, passing Python reference, and artifact upload. All **12/12 exact-head workflows** (11 existing and one disposable research workflow) have completed **success** conclusions.

| Original archive object | Independently computed bytes | Independently computed SHA-256 |
| --- | ---: | --- |
| ZIP artifact **14229080814** | **12,217** | **467b548edbcdfc8cf4aecdab416d134d3ac703572a4e0330a4379fcb28df9929** |
| inputs.json | 19,205 | caa07af040d0a71b50ea6b69470aa55a545b04d52195994913123a902b434df3 |
| report.json | 120,930 | 9324aabab62a2ab0e3636c30dec2154e590daf7c90304e8aeafa564e41250698 |
| exact-reference.json | 23,826 | 497d2e568ca851dd98941be38ccd54b7473953b56405b653771f784633808f12 |

The exact-reference.json sourceReportSha256 equals the independently measured original report.json SHA. The independently regenerated inputs/scene and native fingerprint hashes also match: **six of six scene hashes, 36 of 36 native fingerprints**, without assuming a matching fingerprint is a proof of physical correctness or an identical hidden internal path.

**Historical failures preserved, not native research successes:** CI run https://github.com/physicsvigilante/opticsim/actions/runs/43872666690 failed before any trial because the workflow built a browser bundle instead of dist/test-core.cjs (MODULE_NOT_FOUND). CI run https://github.com/physicsvigilante/opticsim/actions/runs/43872775256 completed all 36 native trial processes, then failed the Python audit due to the obsolete native-single-owner-hit-capture-v1 report path (FileNotFoundError). I also downloaded that **original earlier two-member artifact 14228657123**: ZIP **9,689 bytes**, SHA-256 **7ce492a2ed1211d462d53c76018337b548845dd461de0ed3ceb9f4147de97ff4**; earlier report SHA-256 **9d06d60f31a3434cd63b89f7105cb8055c594efe6e4cd22aa35eed20bdf625a1**; its **inputs.json SHA-256 is identical** to the successful archive. The historical audit did **not** complete in that run, and the historical original outputs were not rewritten.

## 4. Original 36 scheduled fresh-process native trials

The independent seed **0x9500A55**, per-case two-block, per-block three-profile shuffle reconstructed all **36/36** scheduled positions, case IDs, blocks, slots and modes. All positions have corresponding records with correct scene SHA, no missing trial, no runner capture fault and no schedule error. Runner code launches a **fresh Node OS subprocess per position**. The record provenance and CI log are consistent with these launches; I did not rerun them.

| Case | ordinary OFF completed / failed | ordinary ON completed / failed | separate TAP ON completed / failed |
| --- | --- | --- | --- |
| subcritical-tilt-m23 | 2 / 0 | 2 / 0 | 2 / 0 |
| supercritical-tilt-p61 | 2 / 0 | 2 / 0 | 2 / 0 |
| critical-shift-neg | **0 / 2** | **1 / 1** | **1 / 1** |
| critical-tilt-m23 | 2 / 0 | 2 / 0 | 2 / 0 |
| critical-tilt-p61-shift | 2 / 0 | 2 / 0 | 2 / 0 |
| critical-tilt-p14-shift | **0 / 2** | **2 / 0** | **1 / 1** |
| **Total** | **8 / 4** | **11 / 1** | **10 / 2** |

**29 completed, seven genuinely failed.** Failed source ordinals **14, 16, 17, 18, 31, 33, 35** retain the error **“G1: native interface emitted nonfinite or indeterminate encounter evidence”**. No warnings or recorded truncations were present. ON/TAP failures correctly show **suppressed** numerical advisory; ordinary OFF does not enable Stage-1 finite-hit advisory. A captured hit from a subsequently failed run is real observation, **not a completed qualified optical reading**.

For the **far ±7° controls**, all **6/6 subcritical** trials have observed first-contact **transmission**, and all **6/6 supercritical** trials have observed first-contact **total-internal-reflection**, on the first observed polygon face; all 12 completed. This is a coarse observed first-event result only. The four calculated-critical geometries deliberately have **no exact ideal Snell/TIR branch oracle**.

The successful archive has **eight distinct native fingerprint values** across six cases, with two alternatives at each of critical-shift-neg and critical-tilt-p14-shift. The earlier failed-audit CI generated the **same inputs and same schedule**, but profile completion denominators were **10/2 OFF, 9/3 ON, 10/2 TAP** (still 29/7). Eight scheduled positions switched status between these two experimental executions. The noncritical cases remain stable in these archives. This demonstrates sensitivity of these near-critical observations across separate fresh executions, **not** a causal effect of an optional observer. Ordinary OFF retains the normal application's native source/interface instruments; ordinary ON adds shipped Stage-1 diagnostics; the separately TAPped ON profile additionally performs synchronous method capture. Equal fingerprints likewise do not prove observer neutrality.

## 5. Independently recomputed all 32 actual TAP events

**Method:** For each of 32 original TAP callback points, I decoded the archived coordinates' IEEE-754 mantissas/exponents into exact integer multiples of 2^-1074, converted **authored y-up faces to native y-down** while leaving the native p1/p2/incident coordinates untouched, selected the unique incident-proximal *finite* face, and calculated exact signed cross-products and reduced rational ray parameter t and edge parameter u using integer numerator/denominator arithmetic. This is independent from developer exact-check.py's Fraction.from_float. I independently evaluated the source's face, reported-vertex, conditioning, computed-vertex, exact-forward, segment and cutoff decision order, and exact P* versus archived point. All **32/32 reason/status classifications agree** with both original JavaScript classifications and the archived same-author Python comparison. All 30 recorded non-vertex exact t/u numerator/denominator values agree; I also computed the two withheld near-vertex ratios but **left those classifications UNKNOWN**.

All 32 reports uniquely ground to one finite authored face: greatest independent face residual approximately **4.42e−8 mm**, below the existing **1e−5 mm** source classification guard; face ID is proximity-inferred, **not** a directly observed native Glass loop index. Across all 32 samples there are only **17 distinct complete serialized binary64 hit signatures** (p1, p2, incident, selected-face coordinates and cutoff), not 32 independent numerical configurations. Of those 17 signatures, 13 have point-agreement UNKNOWN, two are exact represented-line nonforward, and two are near-vertex UNKNOWN. These signatures are based on the **serialized original JSON**, not original native-memory negative-zero bit certification.

| Archived TAP event category | Event count | Distinct full numerical signatures | Interpretation |
| --- | ---: | ---: | --- |
| EXACT_INTERSECTION_NOT_FORWARD | **4** | **2** | Definite contradiction for the exact lines represented by the saved binary64 scalars, subject to the evidence and conditioning boundaries |
| NATIVE_INCIDENT_POINT_AGREEMENT_UNBOUNDED | **26** | **13** | **UNKNOWN**, not clean and not a proven incorrect native ray point |
| REPORTED_HIT_AT_OR_NEAR_VERTEX | **2** | **2** | **UNKNOWN**; no unguarded vertex inference |
| **Total** | **32** | **17** | Repeated observations are not independent physical systems |

**The two repeated nonforward signatures:**

- **Ordinals 15 and 18, hit index 2**, critical-shift-neg, face-12: exact represented **t = 0**, twice; one eventually completed, one **failed**. Exact represented P* vs archived incident displacement is approximately **0.000400126394 mm**.
- **Ordinals 33 and 34, hit index 2**, critical-tilt-p14-shift, face-12: exact represented **t = −2382431877766392 / 4244811457804902702551 ≈ −5.61257408e−7**, twice; one **failed**, one completed. Exact represented P* vs archived incident displacement is approximately **0.0000377043441 mm**.

For the four nonforward callbacks, an independent Node reconstruction of pinned PhyDemo global-coordinate binary64 **linesIntersection** numerically matches the archived incident x/y. It also passes the pinned rounded-point native forward, finite-segment and squared-step predicates. These archived rounded forward distances are approximately **0.0000371431–0.0004001264 mm**, greater than the **0.000001 mm** minimum step. Across **all 32** callback samples, that separate JS replay yields **32/32 numerical point matches and 32/32 passes of those three rounded predicates**. This supports the source-specific *represented-line versus rounded-point inconsistency mechanism*, **not** a unique causal account of upstream full trajectories; replay equality is numerical against JSON, not recovered original negative-zero bits or a new native execution.

**Conditioning caution:** The two nonforward signatures have crossing sines approximately **1.65e−7** and **1.91e−7** (above the existing conservative sqrt(epsilon) classification floor ~**1.49e−8**). These are small denominators/high-condition intersections, not a derivation of a validated incident-point uncertainty envelope. Descriptively, the 26 point-agreement UNKNOWN cases' computed P*–archived incident separations are about **8.75e−15 to 3.26e−10 mm**; this range is **only observed in this preserved sample**, not an error bound, threshold, or proof of physical invalidity.

**Retained failures:** The two failed TAP trials at source ordinals **18** and **33** each captured four callbacks: **eight actual raw samples**, of which **two** are nonforward, **four** have unbounded point agreement and **two** are near-vertex UNKNOWN. The reported near-vertex clearances are approximately **0.000280348 mm** and **0.000239375 mm**, smaller than the documented 0.01-mm exclusion; they were not promoted to checked. Their source advisory remains **suppressed** because the native trial failed. All 12 TAP trials have capture counters equal to actual Glass interaction meters, 0 capture faults, and no extra native-calling wrapper; the TAP still adds synchronous method work.

## 6. Findings, limits and narrow next experiment

**Research evidence PASS:** I find no demonstrated blocker in the **bounded execution, archived provenance, retained failure accounting, independently checked represented-binary64 geometry or honest research-only interpretation**. The earlier immutable protocol, unmodified physical cases, 12/12 actual source-head CI passes and independently authenticated original ZIP/member hashes support this narrow verdict.

**Important nonblocking limits, not production sign-off:**

1. **Only 17 distinct numerical hit signatures** support the 32 TAP-event claims, with only **two distinct nonforward signatures**. Neither 32 events nor 36 trials is an independent random population of optical systems. Do not treat any UNKNOWN as clean.
2. **Four represented nonforward hits**, including two in failed native runs, are exact statements about the saved binary64 line data. Near-critical/small-denominator sensitivity and an unavailable validated native-point error envelope prevent promoting them to ideal mathematical critical-branch, all-history optical correctness or a universal numerical tolerance.
3. **OFF, ON and synchronous TAP are distinct implementations executed in different processes.** Different success frequencies, even across identical archived inputs, cannot establish observer causation. Matching complete native fingerprints cannot establish physical truth or neutrality. The 8 historical failed-audit versus successful-run switched status positions especially reinforce the need for restraint.
4. No newly executed independent native PhyDemo trials, original pre-JSON memory-bit capture, original source-image interpretation, detected optical image, validated power in Watts, causal observer control, or classroom evaluation is present. Source-head CI validates execution/integrity, not these properties. GitHub artifacts have limited retention.

**Smallest defensible follow-up if stronger stability/observer claims are sought:** On a *new, separately preregistered research-only branch*, repeat just **critical-shift-neg and critical-tilt-p14-shift** with fixed byte-identical inputs, a bounded randomized repeated OFF/ON/TAP schedule and an explicit overhead-matched diagnostic control; retain every original process status, full fingerprint and callback/serialization provenance. That would characterize repeatability and possible timing sensitivity, **not** by itself prove a causal no-observer counterfactual. Any native algorithm/tolerance/Stage-2 intervention would require a separately authorized physics design, new native tests and fresh full R2 review.

**FINAL GATE: PASS — BOUNDED R2 NUMERICAL RESEARCH/EVIDENCE ONLY. DO NOT MERGE draft PR #96 OR ITS DISPOSABLE WORKFLOW.** No Opticsim source, history, PR, pinned PhyDemo, cutoff, qualifications, Stage-1 canonical outputs, Stage-2 policy or original archived evidence was changed by this reviewer. This is a newly authored, append-only central Chat B report, not Chat A's developer summary.
