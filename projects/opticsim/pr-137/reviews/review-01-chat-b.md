# Chat B — independent design review of Opticsim PR #137 (D-02 / B1)

**Date:** 2026-11-18  
**Verdict: CHANGES REQUESTED.**

This is a **design-contract review, not a code or physics-runtime acceptance**. D-02 has a good bounded direction: native finite-window detector selections from two separately authored source angles, with any post-native line intersection explicitly non-observer and non-image. I recommend a **native-hit-only B1a** first, with all **public derived intersection coordinates withheld** until a distinct, preregistered native/numerical stress gate. The current document is candid about unvalidated thresholds, but it still specifies an immediately displayable numeric **advisory** example and leaves several implementation-critical invariants and output states underspecified. Correct those before using it as an implementation contract. **No current production defect is established; no merge, implementation or image feature is authorized.**

## 1. Exact Git source and scope checked

| Item | Independent observation |
| --- | --- |
| Reviewed PR | [Opticsim draft #137](https://github.com/physicsvigilante/opticsim/pull/137): open, draft, unmerged; head branch design/jee-detector-selected-pair-v1 |
| **Authored HEAD** | **3db3711c7a21f5dd477b09d5668a9a8becd6a6a7** |
| **Authored Git tree** | **725d9d450f711a9e379f4137e5c284aa3e0de641** |
| **Actual base / HEAD parent** | **d3509e82fb65d81aabe336666851f8f2962623f4**, tree **45ff3bcd9093a527652f13f76c3cc0b02826642f** |
| **Synthetic PR merge** | **29dc4a4c7205597af93fe3256845bfcc93d57459**; its Git object has **the same tree 725d9d450f711a9e379f4137e5c284aa3e0de641**, and parents base + authored HEAD |
| Diff | One commit ahead, none behind; **one added file, 182 additions, zero deletions**: docs/jee-detector-selected-native-pair-design-v1.md |
| Production / pins | No tracked source, old CLI, saved scene/schema, test, native pin, browser, workflow or historical evidence changed |

I read the entire design document at the exact HEAD, [the detailed reviewer request](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-137/REQUEST.md), [issue #136](https://github.com/physicsvigilante/opticsim/issues/136), and [#135 independent R2 research review](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-135/reviews/review-02-chat-b.md). I directly fetched the Git commit objects (rather than trusting PR prose), compared base to HEAD, inspected current production implementation at the stated base and consulted source-level native observation/persistence contracts.

**Source-level compatibility findings:** At the base, **prepareScene** in src/authoring.js accepts explicitly authored v5 single-ray planar apparatuses and canonicalizes mm/cm/m. src/adapter.js and src/planar-media.js capture genuine finite detector events and native interface branch/direction measurements without rewriting the solver. src/observables.js checks each canonical scene hash, clones the arguments before asynchronous hashing and exposes **per-request** available/qualified/suppressed/unavailable status. The existing **evaluateDocument** in scripts/author-scene.mjs and the guarded **reserveAuthoringOutput** in scripts/authoring-evidence.mjs can be reused. Existing scripts/run-problem.mjs intentionally plans at most **one native run** and must remain frozen. The new B1 dispatcher/CLI is **not** already implemented.

## 2. CI and independent physical calculations

[Planar CI run #44242161435](https://github.com/physicsvigilante/opticsim/actions/runs/44242161435) checked out **29dc4a4**, whose tree is identical to the authored HEAD; recorded **Node 24.19.0**, pinned PhyDemo **811f508d2b070898c241a568b0c167dcb8645251**, **790/790 Node tests passing** and successful native/browser regression steps. [Optical composition/Chrome CI #44242161458](https://github.com/physicsvigilante/opticsim/actions/runs/44242161458) similarly checked out the same merge tree and passed browser/native steps. I independently fetched the head-associated CI metadata: **11/11 workflows completed successfully**, and inspected the native and browser job-step results and representative raw logs. This is **builder CI that I inspected, not freshly independent execution**. Because PR #137 changes only documentation, these 790 tests **do not exercise the proposed B1 request, line-intersection algorithm or proposed 0.01/0.5 mm/2× cutoffs**. The 12 extra research tests from held #135 are not in this 790-test production baseline.

I separately recomputed the basic optical and 2D-line geometry from the **native hit numbers reported in the independently reviewed #135 R2 evidence**; I did **not** rerun or newly retrieve all raw #135 native log entries here:

- For one source at (−120, 0) mm, plane x=0, detector centred at (40,0) mm and emitted ±0.5°, **1.5→1**, Snell gives outgoing angle approximately **±0.750011899990226°**. Independent predicted detector y is **±1.570861127468572 mm**, agreeing with the R2-reported native y **±1.5708611274685678 mm**.
- Back-projecting the reported outgoing lines from p = (40, ±1.5708611274685678) and u = (0.9999143248553549, ±0.013089803247560816), with signs paired consistently, gives **cross = 0.02617736355354841**, both signed ray parameters **−120.00647357027965 mm**, and pairwise intersection **(−79.99619199829817, approximately 0) mm**.
- With **1→1 or 1.5→1.5**, a separate independent reference gives detector y = ±160 tan(0.5°) = **±1.396298846521406 mm** and backward-projected source depth **120 mm**; R2's native-coordinate reconstruction reports **120.0000000000008 mm**.
- A **hypothetical post-native** +10⁻⁶ rad perturbation applied to **only one** of the baseline measured outgoing unit directions while holding the hit points fixed moves my computed intersection about **0.004585 mm**. This illustrates conditioning, **not a measured native error, native accuracy budget, confidence interval, tolerance or certified uncertainty**. A fitted line-intersection residual close to zero proves algebraic consistency of two lines, not optical accuracy.

This supports the limited premise that the B1 pairwise construction is mathematically meaningful for a static 2D example. It does **not** establish a unique point image: a different selected ray pair can give another intersection outside the paraxial regime, and independent runs with a single finite detector do not instantiate a common eye, pupil, retina, image plane or simultaneous perceptual measurement.

## 3. Ranked findings

### P0 — No immediate production or documentary integrity defect demonstrated

No existing engine or native implementation was changed in #137. The exact proposed merge tree agrees with the authored tree, and the source diff is documentary. **P0: none.** This says nothing about whether a future B1 code implementation would be correct.

### P1-F1 — Public numeric intersection is not yet admissible; split the release

**Location:** D-02 sections 4–5 and acceptance P0/P7.  
**Finding:** The proposed advisory display gates — absolute direction cross-product ≥0.01, detector-endpoint clearance ≥0.5 mm and backward extension/scene-scale ≤2 — are **unvalidated heuristics**. They do not bound native angular/position errors, large-coordinate loss, physical image error or the sensitivity of all accepted scenes. Plane-centred coordinates reduce *post-native* cancellation but cannot repair precision already lost by upstream native tracing or native hit capture. Extension ratio additionally lacks a normative definition of **scene scale**, so its acceptance region cannot be reproduced. The given 5 mm, 120/40 mm sample is not a validated 1–10 mm family.

**Required correction:** Define a staged contract: **B1a returns two fully qualified native hit/readout records and null/withheld public derived geometry** (optionally persist test-only mathematical diagnostics). **B1b numerical coordinates require a separate preregistered native stress/accuracy and sensitivity gate**, explicit admitted geometric/coordinate ranges, a deterministic reference algorithm, measured tolerances and independent review. Do not treat the word **advisory**, a numerical cutoff or #135's research-only approval as authorization to release a point. If retaining geometry fields in B1a, mark them **withheld/null** with a stable reason code, rather than a usable point labeled advisory.

### P1-F2 — Scene-family and run/evidence identity must be normative, not optional

**Location:** D-02 section 3 steps 1–4 and section 6.  
**Finding:** The design says a scene-family signature may **optionally** be derived, although the core safety condition requires *exact apparatus equality apart from one explicit source direction*. Distinct scene hashes by themselves prove neither equality of media/policy/detector nor correct association of a readout with a run. Merely calling a cloned B scene is not an adequate persisted/output verification contract if data may later be loaded, reordered or processed asynchronously.

**Required correction:** **Mandate** a canonical, collision-resistant identity for each validated saved scene, and a **mandatory, checked family-equality predicate** comparing **every canonical field** except the specifically identified source emission.directionDeg, with any component-order normalization explicitly defined. Pin/check schemaVersion, adapterVersion, upstreamCommit, physics.model, all media/index/Fresnel parameters, source/plane/detector IDs and shapes, runPolicy-derived simulation settings and remaining presentation fields. Both executions must bind to their own immutable scene/text hash, original input hash, requested first/second directions, native pin and run-local snapshots; both evidence hashes must be different. Reject stale, reused, mismatched or swapped snapshots **before** computing geometry. Do not pair native callback index positions or run-local parentage tokens as cross-run ray identities. A hash is an integrity key, **not independent proof of optical truth**.

### P1-F3 — Output state machine and warning/readout qualification are incomplete

**Location:** D-02 section 4 sample and sections 3/7.  
**Finding:** The sample's singular **inputReadoutStatus**, global **nativeEvidenceStatus** and top-level **status: advisory** do not define a complete status lattice for **four separately requested observables per run**; actual evaluateObservables returns statuses and warnings **per request**. It is unclear how to aggregate a qualified input with an available one, what a completed-with-native-warning (other than deliberate Fresnel-off readout caveat) permits, and how a failed second invocation affects **executions: 2** or both run records. The booleans **nativeImageDetected: false** and **physicalImage: false** can read as negative physical findings even though no image was assessed.

**Required correction:** Specify a deterministic request/result schema for each outcome, including per-run **attempted/completed**, actual native status, executionPassed, canonical SHA, source angle, raw native warnings, **per-observable** status/warnings/reasons/value, native crossing count and full hit or explicit null. Native evidence aggregation is **available only if all required reads are available**, **qualified if any required valid read is qualified**, otherwise unavailable/suppressed as appropriate; arithmetic **never upgrades native qualification**. Reject or withhold derived geometry on unknown/non-whitelisted native warnings, truncation, undefined behavior, failed capture, or stale state; preserve *all* original warnings wherever an execution actually occurred. Make **0 attempts + no fabricated run evidence** the preflight-invalid case, report 1 attempt when the second fails to start, and never advertise two completed executions without two. State separate top-level refusal categories and reason codes for **invalid-input**, **needs-information**, **out-of-scope/unavailable**, native **completed miss** (measured zero and derived unavailable/null), native **incomplete/stale** (suppressed/null) and **numerical conditioning withheld** (native hits retained). Encode image/observer evaluation as **not-assessed** rather than an apparent measurement of absence.

### P2-F4 — Strict angle/geometry/branch admission still needs machine-checkable definitions

**Location:** D-02 section 2 and section 3 step 5.  
**Finding:** The v5 authoring primitive is real and suitable, but the additional B1 preflight has not specified all edge cases. **First ≠ secondDirectionDeg** is a numeric inequality, not necessarily two physically different directions (**−180° and +180°** represent the same heading modulo 360°); infinitesimal separation cannot justify two reliably distinguishable outgoing lines. **Detector tangent parallel to plane** needs an explicit modular-angle convention/tolerance, and **source/receiver side** tests need an oriented normal and signed-distance rule for reversed plane normals and media. A valid source heading that never reaches a plane should be a genuine native miss or typed nonqualifying result, not silently repaired. The contract should clarify whether exact endpoint equality, tangency, source-directed-away cases and TIR are invalid input versus executed no-transmission/miss.

**Required correction:** Define preflight ordering and explicit equivalence modulo 360°, exact ID/type allowlists including nested unknown fields, unique IDs, finite bounds **after mm/cm/m conversion**, normal-side index interpretation, detector endpoint/whole-segment signed-side checks and orientation modulo 180°. Use native first-event fields (**outcome, incidentIndex, destinationIndex, branches, transmitted direction**), emission count and actual complete hit events to verify exactly **one** fully qualified transmitted crossing in each run; any reflected branch must be excluded from the receiving-side selection, with no arbitrary source lineage inference. Treat a native TIR/no-transmission or finite detector miss as measured zero/unavailable geometry, not a fictitious hit. Optional **detector-ray-provenance** is run-local object ancestry and is not mandatory global lineage or a full optical path.

### P2-F5 — Specify and test numerical policy more precisely

**Location:** D-02 section 5.  
**Finding:** A 1 mm detector with **≥0.5 mm clearance at each endpoint** admits at most its exact midpoint; this is a brittle boundary, not a robust 1 mm-width operating region. The chosen cutoffs can reject valid large virtual-depth constructions or admit inaccurate ones without any proven bound. A local orthonormal normal/tangent frame is sensible, but the exact signed formula, parallel test, residual diagnostics and scene-scale definition remain open.

**Required correction:** Define signed backward parameters (both **strictly negative**), signed source-side test, determinant and near-antiparallel conditions, finite-number/near-unit-vector verification and endpoint margins from **both actual endpoints**, not an assumed symmetric detector. Define a translation/rotation/units-invariant **scene scale from physical geometry** and explicitly state its numerator/denominator. Keep local and reconstructed global coordinates separate, and publish only if output error and native sensitivity have measured bounds within an independently reviewed domain. Reconsider whether 1 mm width belongs in the advertised range; include exact boundary and width≈1 mm tests. The independent Snell calculation must remain a **post-native oracle only**, never a substitute ray trace or input to propagation.

### P2-F6 — New CLI and evidence/recovery semantics need a concrete contract

**Location:** D-02 sections 3/6 and acceptance P8–P9.  
**Finding:** The proposed standalone CLI is the right integration boundary. Existing **evaluateDocument**, **evaluateObservables**, **sceneHash**, **prepareScene** and the fresh-only evidence-directory guard exist at the stated production base. However the design does not fully specify the file manifest/checksums, setup-vs-native failure distinction, interruption/partial-run output and reporting of refusal before either run. **reserveAuthoringOutput** prevents ordinary symlink/path clobbering but explicitly is not a hostile concurrent filesystem sandbox. The existing problem dispatcher is single-run and cannot silently absorb B1.

**Required correction:** Specify versioned manifest with original raw input bytes and SHA, canonical A/B scene JSON + SHA, family identity, one independent evaluation and observable bundle per attempt, native pin, raw warnings/readout warnings, and derived/test-only diagnostics in separate files. All files must be exclusive/fresh; on partial failure retain only genuinely completed facts, and mark report incomplete/infrastructure-error rather than recycling a prior run. No old **run-problem.mjs**, **author-scene.mjs**, saved v5–v19 schema, pinned PhyDemo, browser or historical evidence edits; no public **opticsim-problem-v1** routing until separately reviewed.

### P2-F7 — The proposed stress programme must produce measured acceptance criteria

**Location:** D-02 section 5, acceptance P0–P10.  
**Required before B1b geometry:** Preregister a bounded **test-only** native matrix, with independent review of fixture/oracles *before* execution and a recorded finite error/conditioning policy: equal and unequal indices in both directions, normals 0/±90/±180/±37°, physically equivalent rotations/translations and mm/cm/m, detector widths 1/5/10 mm, endpoint margins both sides, multiple axial depths, source-angle separations, full Fresnel versus transmitted-only caveat, native near-grazing/near-critical/TIR and no-hit cases, near-parallel/antiparallel and very long extensions, high coordinate translations within actual bounds, invalid/missing/stale capture, truncation/warnings, and mixed component orders. Require actual two-run SHA/family identities and native count/branch/hit consistency **in each case**. Measure reproducibility, invariance residuals and the largest sensitivity to disclosed **hypothetical** perturbations; explicitly distinguish those from a native numerical uncertainty estimate. Predefine tolerances and withhold unstable cases. No cherry-picked accepted points.

### P3 — Interpretation and hygiene

- Use a more explicit public label such as **two independent native detector samples / conditional 2D supporting-line extrapolation**, never eye, pupil, image or observer. A shared finite segment does not establish that both rays meet at a single point on the segment, much less at an eye; the backintersection is generally ray-pair dependent.
- A single source plus explicit second absolute direction is a practical **bounded LLM-authorable** input; avoid duplicating two full scenes or introducing generic v20 ray composition. Preserve explicit user physical choices, especially refractive indices, normal orientation and Fresnel policy.
- The top-level strict grammar should define whether duplicate JSON object keys are rejected, since ordinary JSON.parse discards earlier duplicates before allowlist validation. Report missing required physical facts as needs-information rather than inventing them.
- Keep the #135 **RESEARCH ONLY** finding, held #133/#129 and all other draft branches separate. [Issue #123](https://github.com/physicsvigilante/opticsim/issues/123) on main protection is an independent governance gate.

## 4. Minimal corrective path and owner gate

**Recommended order:**

1. **Revise D-02** to mandate the family/execution identity invariant and a complete per-run/per-observable refusal/qualification matrix. Replace ambiguous image booleans with explicit nonassessment semantics.
2. Define **B1a: native-hit-only** standalone CLI output (actual selected counts/positions/directions/first-event branch and raw warnings from both independent native calls; derived point withheld/null). Any internal numerical scratch output must be clearly test-only and never counted as an answered image question.
3. Run the distinct preregistered **test-only numeric feasibility** campaign; independently review results, range, cutoff policy and conditioning. Only then design **B1b** opt-in advisory geometric coordinates with validated scope and no claim of observer/physical image.
4. A later **separate production source PR** based on actual main needs fresh exact-tree CI, authentic native tests, existing Node24/Chrome regressions, independent physics/code review and explicit owner release/merge decision. The design-only PR is not such an implementation.

## 5. What I independently did and did not execute

**Independently checked:** the exact HEAD/base/synthetic-merge Git objects and tree identities; base-to-head change count; full D-02 document and review request; issue #136 and independent #135 R2 report; current-base native authoring, adapter, planar event, hit capture, observable/hash/status, CLI and evidence-guard code; head-associated 11 CI workflow results, selected native and browser jobs and their archived builder logs; independent scalar Snell and 2D line-intersection calculations on R2-published native data; hypothetical perturbation calculation. No repository contents other than this requested review are changed.

**Not independently executed:** no fresh Node 24 suite, test-core build, PhyDemo native trace, local clone/install, actual two-run B1 CLI, independent browser or Chrome run, or new numeric stress campaign. The successful **790/790** and **11/11** are **GitHub builder evidence inspected**, and the R2 native numbers come from the earlier independently reviewed research report; they are **not** fresh B1 implementation evidence.

**Final verdict: CHANGES REQUESTED — design contract only.** The native pair concept is reasonable and reusable; make the identity and result semantics normative, and stage **native hits before public geometry**. Do not treat #135 clearance, regression CI, hypothetical sensitivity or a label saying advisory as a numerical accuracy certificate. No merge, source implementation, eye/pupil/image claim or owner release authorized.
