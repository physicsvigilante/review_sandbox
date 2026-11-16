# Chat B independent R2 review — conductor_sim M27b PR #63

- **Project / source repository:** conductor_sim — https://github.com/physicsvigilante/conductor_sim
- **Source PR:** https://github.com/physicsvigilante/conductor_sim/pull/63 — open, draft, unmerged at last verification on 2026-11-16.
- **Base SHA:** 4a967f469df999bc4a97c434dfdd6b69f49893ba
- **Exactly reviewed HEAD:** 08ad6ea0a30d440f70f83f89e865a87fe9a0f96f
- **Reviewed source tree:** 2affa61b9efd44f5949f5c6e8136f8ad179e893b (matched the source tree recorded in the independently downloaded focused artifact; the entire Git tree was not independently reconstructed).
- **Source diff:** https://github.com/physicsvigilante/conductor_sim/pull/63/files
- **Reviewer:** Chat B, separate-context ChatGPT conversation, GPT-6
- **Date:** 2026-11-16 (Asia/Kolkata)
- **Scope / risk:** R2; invariant physical planes, real off-axis motion, ideal charged-wire safety, independent dynamics, exact-state visuals, historical refusals, source provenance.
- **Were source files changed by reviewer?** No. No source commits, merges or PR mutations. New native tests ran on an isolated extracted copy of the pinned CI source.
- **Outcome: PASS (scoped).** No demonstrated blocker or major defect. One minor CI-reporting provenance wording error needs correction when convenient; it does not invalidate the actual source-given charge, integrated dynamics, or student viewer. No production merge is authorized by this report.

## Independent evidence chain

I verified the live source PR HEAD matched the required pinned SHA immediately before writing this report. The CI focused artifact records the GitHub test-merge commit 5edd16bd2390e7f1909d6a2485cd032adad0507a and expected tree 2affa61b9efd44f5949f5c6e8136f8ad179e893b; do not mistake this test-merge commit for the PR source HEAD. I separately checked the pinned source file src/conductor_sim/ring_motion_symmetry.py against its Git blob hash bda505363f35b1444235d2aea7bb1cf2a762b020 inside the CI source archive.

The following ZIPs were **personally downloaded and SHA-256 rehashed**, rather than merely trusting labels:

| CI artifact | Recomputed SHA-256 | Findings |
| --- | --- | --- |
| Focused run 43757091565, artifact 14178333560 | 861a19c4d0351f60c9ad2d58186b994a042aa67138ea9599828712374a76e4de | Matches GitHub-reported digest; inspected workbook, driven and reserved numerical JSON, tree/commit records |
| Visualization run 43757091497, artifact 14178987218 | b66596099530c70348292a858426b35f295454734c7534aca71f81680a2fa033 | Matches GitHub-reported digest; inspected HTML, 390px/wide PNGs, browser assertion JSON and embedded source.zip |

The source PDF was included in the extracted CI archive. I rendered and visually read PDF page 12 directly (source PDF SHA-256 9dff3c02a9f1848d2c3d99cb1a6e7a44dc7f5a51f7a3a2b8cc92d10ce1fbca5d). The scan confirms ring A +10 μC, ring B −20 μC, radii 30 cm, center separation 40 cm, axes horizontal, external field +up at 10^5 N/C, and probe charge q=+10 μC. It also says the probe is originally released from rest at center A, has a symbolic mass m, and in Q41 its motion along the center line is assumed. The new free-plane experiment explicitly changes the launch to x=0.20 m with v_x=0.1 m/s and sets mass 0.01 kg and duration 0.015 s; these **are teacher hypotheticals**, not an exact execution of the original Q41. This distinction is clear in examples/m27b_offaxis_motion.py:34–58 and the rendered student-facing title/provenance.

## Findings

### F-01 — MINOR, provenance wording in browser CI summary (demonstrated; not a physics blocker)

- **Location:** tools/check_m27b_browser.py:149 and its emitted m27b-browser.json, source field.
- **Input/reproduction:** Read the original scanned page 12 paragraph preceding Q40–41, and compare against the browser summary statement: "teacher-hypothetical charge/mass/launch/time."
- **Expected:** Probe charge q=+10 μC is **source-given**. Numerical mass, shifted position, nonzero initial velocity, elapsed duration, free-motion interpretation and numerical parameters are **teacher-chosen**.
- **Observed:** The summary includes "charge" among hypothetical values, although the actual authored code uses the correct source q=+10 μC (examples/m27b_offaxis_motion.py:44) and its displayed provenance correctly identifies mass/start/velocity/duration as hypothetical. No wrong charge is integrated or plotted.
- **Type/confidence:** Direct original-page visual inspection plus exact source and emitted JSON; high confidence.
- **Correction/regression:** Change this CI-only summary to distinguish source-given charge from chosen mass/launch/duration, and add an assertion against the source-anchored card. This is **minor wording cleanup**, not a reason to change the physics or invalidate current numerical evidence.

### F-02 — INFORMATIONAL, numerical rather than exact real-arithmetic plane certificate

- **Location:** src/conductor_sim/ring_motion_symmetry.py:17–41; src/conductor_sim/prescribed_motion.py:316–333.
- **Basis:** The certificate deliberately uses radius/world-ULP-dependent center tolerance and approximately 1e-11 axis orientation tolerance, rather than literal zero. For a circle centered on the proposed plane, exact mathematical invariance occurs only when its axis is tangential (meridian) or normal (equatorial). Near-threshold finite precision models are numerical admissions, not exact reflection theorems.
- **Observed:** New off-plane center +7e-8 m was refused even with an enormous authored length scale; an axis with world-y component 4e-7 was refused; the novel physically invariant configuration maintained zero sampled normal position and force. The unchanged runtime checks the full world force, without projecting away a normal component.
- **Residual limitation:** Keep the strict physical admission and runtime force guard. Retain a near-tolerance-boundary regression and avoid claiming an absolute exact-symmetry guarantee for perturbations below floating-point certification tolerance. **No demonstrated new defect.**

### F-03 — INFORMATIONAL, singular-wire safety claim is correctly bounded

- **Location:** src/conductor_sim/prescribed_motion.py:280–305; src/conductor_sim/motion_2d.py:503–545.
- **Proof:** For distance d(x,W) to the fixed circular wire W, the triangle inequality implies |d(x,W)−d(y,W)| ≤ |x−y|. Every point on a straight chord of length L is at most L/2 from its midpoint M. Therefore d(x,W) ≥ max(0,d(M,W)−L/2). Requiring this lower bound to exceed the configured guard makes the accepted **numerical chord** safe relative to W. The controller checks both accepted half-chords, as well as sampled stages, and halves/refuses unsafe steps.
- **New test:** With ring radius 0.15 m and guard 0.005 m, the chord from (0.08,0.01,0) to (0.22,0.01,0) has true endpoint wire distances 0.0693774 m and 0.0702272 m, but a dense numerical chord search finds a minimum about 2.29e-6 m; the production midpoint lower bound is zero and rejects this chord. A separately authored native approach run stops at 0.0322904783 s with termination source-guard, **before** duration 0.11 s; last clearance to the wire is 0.00507361127 m and one guard event is recorded. It does not claim collision, rebound, or duration completion.
- **Residual limitation:** A guarded RK chord is not a mathematically certified enclosure of the entire unknown continuously curved exact ODE trajectory. The code and charter accurately distinguish these. **No demonstrated new defect.**

## Physics and source audit

The circle-reflection criterion is physically sound. With ring center c in the proposed plane P, reflection across P maps the full uniformly charged circle onto itself exactly if the ring axis is parallel to P (meridian) or perpendicular to P (equatorial). Applying this requirement to **each ring separately** is sufficient for their superposed potential to be reflection-even and the electric field's normal component to vanish on P. Source-plane-preserving point/rod inventories, held and every scheduled uniform field, and gravity are separately qualified. With initial position and velocity in P, Newton's equation with unprojected F=qE+mg remains in P until the modeled domain terminates. The code never establishes admissibility from a single locally canceled transverse force.

The new branch is narrow: M27b imports the existing M27a full-3D UniformRingField source law, applies its actual wire clearance, and reuses the prior shared adaptive RK4/energy/event/driven-motion controllers. The pull-request diff does not change the M27a elliptic field formula or rewrite the core integrator. Mixed new full-ring plus historical axis-only ring/disc motion is expressly rejected; existing axis-only-only motion remains covered by tests. New held fields and later scheduled phases are qualified; stationary-medium isotropic linear drag preserves the plane.

The conservative energy convention is K+qV+Ug with no induced-charge half factor or conducting back-reaction. For the driven case, the recorded work relation is ΔK = W_fixed + W_applied + W_gravity − dissipated energy. The fixed-source viewer and the new geometry projection do not create a fictitious particle guide.

## New independently authored and executed tests

**A. Unfamiliar production-native transfer — PASS.** The reviewer authored a configuration not present in the M27b frozen P1–P7, U1, workbook or reserved R1 cards:

- Full ring 1: +4.1e-9 C, R=0.13 m, center (0.075,0,−0.045) m, axis (1/√2,0,1/√2).
- Full ring 2: −2.6e-9 C, R=0.085 m, center (−0.11,0,0.07) m, axis (0,0,1).
- Held uniform E=(1.4,0,−0.8) V/m and g=(0.035,0,−0.08) m/s².
- Probe q=−5.2e-10 C, m=4.2e-7 kg, p(0)=(0.025,0,0.11) m, v(0)=(0.062,0,−0.042) m/s.
- Authored physical plane normal (0,1,0), duration 0.085 s, sample spacing 0.0085 s, source guard 0.006 m, relative tolerance 1e-10.

**Native result:** 11 saved states; termination duration; last position (0.034490029306480,0,0.103237333714239) m; last velocity (0.158334007610003,0,−0.119950731711289) m/s; maximal sampled normal displacement and normal force both zero; maximum reported absolute conservative-energy drift 2.04443e-17 J. The native source was the extracted frozen CI archive, not a locally rewritten implementation.

**Independent reference:** Separately implemented 2,048 Coulomb midpoint charges per ring, independent 3D basis construction, and SciPy DOP853 with rtol=8e-12, atol=2e-13, max step 0.0002 s. No production elliptic functions or RK4 code were used. Predicted final position (0.034490029327793, approximately 0, 0.103237333712708) m; final velocity (0.158334007892862, approximately 0, −0.119950731936110) m/s. Maximum component discrepancies: **2.13132e-11 m in position; 2.82859e-10 m/s in velocity**. At native final position, direct Coulomb-versus-native electric field maximum component difference was 3.41e-13 V/m; full force difference 2.12e-22 N. Independent energy endpoint difference was approximately 6.29e-23 J. This is a new independent cross-method, source-geometry and integration test, **not** the implementer's previously exposed R1.

**B. Rigid rotation + translation — PASS.** For this same new native case, transform every ring center and axis, uniform E, launch, physical normal and gravity by a 63° Rodrigues rotation about (2,−1,3), followed by translation (0.3,−0.2,0.4) m. Both native integrations completed. Maximum component differences after reversing the coordinate transformation: position 2.22e-16 m, velocity 1.67e-16 m/s, force 1.91e-21 N. No special source-facing coordinate frame was used.

**C. Negative physical admissions and guard — PASS.** Reviewer-authored, natively executed cases refused: ring center 7e-8 m off-plane despite length_scale_m=1e6; ring axis with y=4e-7 (neither meridian nor equatorial); mixed new full ring with legacy axis-only ring; and a later field phase with a nonzero plane-normal component. The new chord/approach guard case in F-03 terminated as source-guard, not duration. Two real ring rims and stable ring:newone/ring:newtwo source IDs with meridian tags were exported as physical source geometry. These are new inputs, not just reruns of the developer's cases.

**D. Native retained suite — PASS.** Using the independently extracted source from the downloaded exact-target CI artifact, I ran tests/test_m27b_ring_motion.py locally: **19 passed in 1.48 s**, under the local Python 3.13.5 environment. These 19 are existing source tests, **not** novel independent evidence; they corroborate that the source archive is runnable. First attempt at my separate rotated test failed during test construction because NumPy float64 scalars are not admitted by the typed public constructors. I corrected my test inputs to ordinary Python floats and reran successfully; this was a reviewer setup failure, **not a production regression**, and no source files changed.

## Cross-checks against actual retained CI numerical artifacts

The following values were computed independently, using the same separate Coulomb/DOP853 reference against numerical output I downloaded; these are **not** new production executions of those existing cards:

| Existing case | Maximum component position error | Maximum component velocity error | Other evidence |
| --- | --- | --- | --- |
| Workbook Ring A/B + vertical held E | 1.72679e-10 m | 4.05610e-8 m/s | True world-y displacement +0.0115036655 m at t=0.015 s; direct field max error 1.64e-8 V/m, full force max error 1.64e-13 N; independent x=0.275 m detector time differs by 2.83e-9 s |
| Workbook variant + drag and t=0.008 s 20 kV/m extra field | 1.51030e-10 m | 3.88682e-8 m/s | Correct 20 m/s² jump in upward acceleration with continuous state; final work-balance error −2.95204e-9 J, nonnegative dissipation 1.440995e-6 J |
| Developer-exposed R1 nonparallel-ring reserved card | 1.43580e-13 m | 1.52064e-12 m/s | Independently recomputed using Coulomb/DOP853, but **not blind**, not a first reserved execution |

The first reserved R1 **developer** execution was GitHub run 43755933184 at earlier source c76eb6f5…, with its own 512-site/700-step velocity-Verlet reference and already disclosed acceptance errors; I have **not** relabeled that first run as independent Chat B evidence.

## Viewer, temporal truth and legacy paths

I inspected source_geometry.py:174–225 and the saved wide/mobile event/driven HTML, PNGs and browser test JSON in the rehashed visualization artifact. The diagrams show two actual orthographic 3D ring projections with charge, radius, true world axes, original center separation, stable physical IDs and meridian mode. The moving probe follows a visibly two-dimensional curved world-x/y trajectory, with correct positive upward displacement and live saved physical-time force/velocity/energy readouts. The UI text calls out teacher numerical assumptions, full 3D off-axis source E/V, absence of conductor response, and the difference between graphical interpolation and native saved states.

The page source and Python renderers use precomputed validated trajectory samples; there is no newly written browser ODE, electric field solver, fabricated guide or unqualified collision. The old M19b standalone prescribed viewer and its import validator explicitly refuse full-ring motion (prescribed_viewer.py:295–306; prescribed_viewer_validation.py:89–101); the new M24a/M24b event/driven viewers use shared qualified source geometry. Source IDs in the user-facing viewer match the model's ledger.

**Limit on my browser evidence:** I visually inspected downloaded real-Chromium CI screenshots, independently rehashed the source artifact, checked its browser JSON, and inspected the source HTML. I **did not run my own new Chromium session** because the local Playwright Chromium binary was unavailable. The original real-browser gate passed on CI, including saved-time controls, path toggling, separate pages, 390px responsiveness, zero console/page/network errors. This is CI execution evidence, not independently rerun browser execution.

## CI history, without reclassifying failures

- GitHub run 43757091625: actual Python 3.10 and 3.12 job logs each report **1,807 passed; 97 skipped; 9 warnings**.
- Run 43757091565: focused physics log reports **160 passed**, reserved regression passed, workbook and driven generated JSON/HTML both completed.
- Run 43757091501: actual **97 FEMM 5 tests passed**, a conductor-domain nonregression check, **not** independent charged-ring ODE validation.
- Run 43757091497: actual visualization and real Chromium steps successful, including the M27b browser gate.
- I retrieved **17** completed/successful PR-triggered workflow runs for this commit via the linked GitHub interface; the author describes 18/18 applicable checks. Because the interface presents only its filtered first page, I do not claim independent enumeration of all 18.
- Historical **failed** first attempts remain failures: run 43755539988 (obsolete prior M27a static-only test expectation), run 43755933109 (real Chromium test failure), and diagnostic run 43756841708 ("Identifier 'data' has already been declared" from reusing one JS lexical page context). The new browser harness uses separate pages, rather than modifying the physics or rendering formula. The earlier failures are **not** restated as first-run passes.

Root source AGENTS.md was checked and was absent (GitHub 404; no AGENTS.md in extracted source archive). The central review protocol, risk policy, report template, frozen M27b charter and reserved card, source composability and teaching evaluation contracts were read.

## Separate scope judgments

| Dimension | Judgment | Basis |
| --- | --- | --- |
| **Source interpretation fidelity** | **PASS, bounded** | Source ring geometry/E/charge confirmed against scanned p12. Explicitly teacher-chosen mass, launch, time and free 2D dynamics; old Q41 axial/rest condition is not falsely reproduced. Minor CI-only charge provenance wording in F-01. |
| **Physical and numerical correctness** | **PASS for qualified regime** | Reflection criteria, unprojected world force, independent direct Coulomb/DOP853 on three saved cases plus truly new native transfer, rotation covariance, energy/force and negative admissions. |
| **Native simulation and observable coverage** | **PASS for tested M27b functionality** | Fresh native trajectory, guard censor, typed event/driven saved observations and source IDs; reexecuted 19 existing M27b tests. No claim of unrestricted 3D or contact dynamics. |
| **Evidence integrity/provenance** | **PASS for inspected artifacts, some untested scope** | Both ZIPs independently rehashed and source/CI identities checked; original failures retained. The reported 18-check total, full Git tree hash reconstruction, and fresh independent Chromium are not independently established. |
| **Teacher-facing usefulness** | **PASS for inspected examples** | True curved 2D path, visible ring identities, source geometry, source/teacher differentiation and readable state/energy/event labels. New browser interactivity independently inspected via real-CI visual evidence, not replayed locally. |
| **Textbook-answer completeness** | **NOT ATTEMPTED / not required** | Q41's original symbolic mass/rest/along-center-line setup is different from the expressly teacher-hypothetical off-axis free-motion exploration. |

## Release advice

**PASS for the exact reviewed source HEAD only.** No verified physical admission, Coulomb field, conservative/driven dynamics, singular-wire chord safety, or display blocker was found. Correct the small F-01 CI-provenance wording when convenient; retain near-tolerance and guard regressions. Preserve the source charter, reserved R1 first-run evidence and historical failed CI. The new independently authored native case shows meaningful **composability**: two unfamiliar nonparallel rings, gravity and an additional field required only new model authoring, not a source-code modification.

Residual bounds remain essential: only individually certified meridian/equatorial planes, prescribed nonresponsive fixed sources, no mixed legacy axis-only/full-ring motion, no actual contact, no generic free-3D solver, no exact-trajectory wire enclosure, and no full symbolic Q41 answer. A new changed HEAD would require appropriate targeted re-review.

**No production merge, deployment or source PR modification was performed or authorized here. Separate explicit owner approval is required before merging PR #63.**
