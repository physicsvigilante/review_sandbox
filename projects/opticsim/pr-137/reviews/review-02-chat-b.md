# Chat B — Opticsim PR #137 D-02 R2 independent second-pass design review

**Date:** 2026-11-18  
**Verdict: CLEARED FOR OWNER DECISION — DESIGN ONLY.**

The corrected B1a proposal resolves the three R1 P1 blockers at the **design-contract** level: it admits only two independently executed, pinned-native single-ray detector samples through one identical finite detector; requires exact whole-scene family/run identities; and defines truthful per-observable qualification, warning provenance and partial-run/refusal semantics. In particular, **B1a publishes no derived two-line backintersection, even for the demonstrated 5 mm positive fixture**. Public mathematical coordinates require the separate B1b preregistered numerical feasibility, accuracy/conditioning and review gates. This is not permission to implement without a source review, merge, release an eye/observer/image feature, or assert a validated numerical location.

## 1. Exact Git identity, diff and limits

| Check | Independent observation |
| --- | --- |
| Target | [Opticsim draft PR #137](https://github.com/physicsvigilante/opticsim/pull/137); open, draft, unmerged at review |
| **Authored HEAD** | **`7f19f6d5c97608fc0eb1399cea3a3582938f2f6a`** |
| **Authored Git tree** | **`914e1296f1cfb2da61ebbdddc98a907ee32e39a8`** |
| Actual production base | `d3509e82fb65d81aabe336666851f8f2962623f4`; tree `45ff3bcd9093a527652f13f76c3cc0b02826642f` |
| Synthetic tested PR merge | `45f4eaa87128321bc7e479275d5819237f2da4a8`; **same tree `914e1296f1cfb2da61ebbdddc98a907ee32e39a8`**, with base + authored HEAD as parents |
| Base-to-HEAD comparison | Ahead 5, behind 0; **exactly one added file, 197 additions, 0 deletions**, `docs/jee-detector-selected-native-pair-design-v1.md` |
| R1 ancestry | Original R1 HEAD `3db3711c7a21f5dd477b09d5668a9a8becd6a6a7` is a verified ancestor (HEAD 4 ahead, 0 behind from R1); its report remains separate |
| No changed production artifacts | No `src/`, test, CLI, native pin, scene schema, Chrome/browser, workflow, old frozen script or historical evidence changed |

I obtained HEAD, base and proposed-merge **raw Git commit objects**, verified their parents and tree hashes, and compared base/HEAD with the GitHub compare endpoint; the identities above were not assumed from the PR body. The reviewed document is the **197-line** final R2 document, **not** intermediate R2 HEAD `4effded...`. I read [REQUEST-02](../REQUEST-02.md), [R1 review](review-01-chat-b.md), the entire actual R2 design document, [issue #136](https://github.com/physicsvigilante/opticsim/issues/136), and [independent #135 R2 research review](../../pr-135/reviews/review-02-chat-b.md).

## 2. Disposition of the three original R1 P1 findings

| R1 finding | R2 disposition | Exact reason |
| --- | --- | --- |
| **P1-F1: unvalidated public numeric intersection** | **Resolved for B1a design** | Sections 1, 4 and 6 force `geometry.status:'withheld'`, `value:null` and `B1B_NUMERICAL_GATE_NOT_RELEASED` even after two positive native hits. No public calculated intersection, depth, virtual ray or image point. Former `0.01 / 0.5 mm / 2×` display cutoffs are withdrawn from B1a. B1b is another preregistered and independently reviewed gate. |
| **P1-F2: optional/inadequate scene-family/run identity** | **Resolved for B1a design** | Section 3 requires a canonical **complete v5** scene A; B deep-cloned from A with only the named source's `emission.directionDeg` changed; distinct saved `sceneHash` values; full-scene component-ID lexical sort and removal of **only that angle** for the canonical family predicate; both canonical representations and SHA-256 hashes must agree. Immutable source bytes/sha, role, heading, scene, native pin and invocation-local summary hashes must be checked independently. |
| **P1-F3: incomplete result and partial-execution semantics** | **Resolved for B1a design** | Sections 3–5 specify the four independent observables per run, raw native warnings/errors, observable status/value/method/warnings/reasons, `available` / `qualified` / `unavailable` / `suppressed` / `infrastructure-error` reductions, true `nativeAttempted/nativeCompleted` counters, distinct preflight/refusal reason codes, completed zero/[] misses and no fabricated unattempted records. `observerAssessment`/`imageAssessment` are explicitly `not-assessed`. |

These are **normative proposed requirements, not implemented functions or executed acceptance tests**. The earlier R1 report remains a correct CHANGES REQUESTED evaluation of the *original* HEAD.

## 3. Independent design/physics/contract assessment

**Authoring and physical geometry.** The input is bounded and reasonably LLM-authorable: one existing v5 point source with exactly one explicitly authored single-ray heading; one real planar interface with explicit normal, refractive indices and Fresnel boolean; one actual finite detector and one **second absolute heading**. The seven top-level request fields are mandatory, extras rejected; source/interface/detector roles and IDs are explicit. Source and both finite detector endpoints must lie at least 1 mm from the plane on **opposite** signed-normal sides after mm/cm/m conversion, with full detector length **2–10 mm** and detector tangent parallel to the plane tangent modulo 180°, using the stated representation-only 1e-9° guard. The normal and side definitions match the existing `interfaceNormal` / `signedSide` semantics, including reversed normals; neither source side nor receiving medium is inferred from global x. Headings use wrapped modulo 360° equivalence: +180° and -180° are identical, and less than/equal to 1e-9° separation does not qualify as a second authored heading. This guard is not claimed to make nearly parallel rays numerically useful.

**Strict validation.** The new 1 MiB duplicate-member check must occur **before** ordinary `JSON.parse`, at **all** object nesting levels, so duplicate physical values cannot disappear. The final contract gives invalid/duplicate/unknown supplied fields priority over missing fields, before diagnosing valid-but-unsupported physical scope. This requires a new bounded validator; the existing `inspectAuthoringRequest` alone is not an implementation of that stronger global precedence. Native work is forbidden after invalid preflight, and missing physical facts cannot be silently repaired by `prepareScene`.

**Actual native selection.** At baseline `d3509e8` I inspected `src/authoring.js`, `src/contract.js`, `src/qualified-utils.js`, `src/planar-media.js`, `src/adapter.js`, `src/observables.js`, `scripts/author-scene.mjs`, `scripts/run-problem.mjs` and `scripts/authoring-evidence.mjs`. `prepareScene` builds valid pinned v5 planar documents; `sceneHash` hashes `serializeSave`, while `canonicalJSON` sorts JSON object keys (the proposal explicitly adds component-ID sorting); `evaluateDocument` exposes a canonical scene SHA, native status, warnings, first-interface and detector observations; `evaluateObservables` clones invocation inputs before asynchronous hashing and returns separate per-request statuses. The existing adapter records detector hit positions and incoming directions from native incident data **before** native callback mutation, with an existing endpoint ambiguity guard; the planar observer captures first-event direction/branch/index evidence, delegating to native once. Thus the proposed four `source-emissions`, `interface-first-event`, `detector-crossings` and `detector-hit-events` are source-compatible. Native callback order and run-local parentage are **not** cross-run ray IDs. The old `run-problem.mjs` is single-run, so the proposed new pair CLI is genuinely necessary and not already present.

A positive B1a selection must show **per run** one emitted source ray, one valid first plane encounter with transmitted outcome and correct oriented indices, exactly one transmitted native branch, one actual detector crossing, exactly one complete finite hit event and consistent incoming/transmitted unit directions. A reflected Fresnel branch is retained as evidence but not misassigned to the opposing detector. The complete sample is a genuine 2D finite-window measurement. It is **not** a simultaneous two-ray observation at an eye, a numerical image construction or continuous irradiation measurement.

**Warning/status semantics.** The baseline `evaluateObservables` can label reads `qualified` when **any** warning exists, including raw runtime warnings. R2 correctly adds an essential **fail-closed pair-specific reduction**: an explicitly recognized Fresnel-off caveat can remain `qualified` but any unreviewed native warning suppresses selection; neither a qualified input nor a measured count of zero can become `available` by arithmetic. The raw warning/error list and each observable's independent status/warnings remain attached to every genuinely attempted run, including a null aggregate. Actual completed detector misses retain zero counts and empty complete event lists, while incomplete capture is **not** converted to a fabricated empty list.

**Execution and persistence.** The run roles, input SHA, individual scene SHA, family SHA and native pin are mandatory; an invalid preflight gives 0/0 and no execution records. A pre-run family integrity mismatch is a zero-attempt infrastructure refusal, whereas a returned stale execution identity is a post-attempt suppression. An ordinary completed miss/incomplete result does **not** justify skipping the prepared second run; unrecoverable setup/storage/integrity failure **does**. An invocation-start failure counts only an actual attempted invocation, never a completion. The proposed `scripts/detector-selected-pair.mjs` reuses a fresh-only no-clobber directory, persists real A/B evidence independently and writes a checksum-linked final manifest last. A hard-crash partial directory without a valid finalized manifest cannot be reported as success, resumed with stale results or promoted to two completed native executions. Historical scripts remain byte-frozen. The existing directory guard is correctly **not** described as a hostile concurrent filesystem sandbox.

## 4. Independent numerical cross-check: research data, not B1a output

I independently recomputed the following scalar Snell/reference geometry and two supporting-line intersections **from numeric native hit and outgoing-vector values published in the independently reviewed #135 R2 report**. I did **not** rerun PhyDemo or independently re-download/parse the full #135 native artifact in this R2 design review.

- **One 5 mm detector at x = 40 mm; source (-120,0) mm; ±0.5° single-ray headings; 1.5→1:** Snell predicts |transmitted angle| = **0.7500118999902258°**, detector |y| = **1.5708611274685715 mm**; the published native |y| is **1.5708611274685678 mm**. Using the published outgoing unit vectors, the independent 2D cross determinant is **0.02617736355354841**, both signed extension parameters are **−120.00647357027965 mm**, and the mathematical supporting-line intersection is **(−79.99619199829817, 0) mm**. Each hit has **0.9291388725314322 mm** nearest finite-endpoint margin.
- **Equal-index 1→1 or 1.5→1.5 control:** published native |y| = **1.396298846521404 mm**, consistent with independent **160 tan(0.5°) = 1.3962988465214063 mm**. The determinant is **0.017452406437283397**, signed parameters **−160.00609254171871 mm**, supporting-line intersection **(−120.0000000000008, approximately 0) mm**, and nearest margin **1.103701153478596 mm**.

Those derived coordinates are included **only as an independent review calculation**. They **must not** be returned publicly by B1a. Fitting two lines exactly does not bound native angular error, scene-scale sensitivity or image quality; the prior independently reviewed #135 tests are **research only**, at `d6aff4e388aef982c3fc1b88039d4ac6951b4fca`, still held/unmerged. No optical observer or original JEE-answer fidelity has been verified.

## 5. Ranked findings and remaining gates

### P0 — No critical source-integrity or physical-claim blocker identified

The exact design Git objects and one-file scope are consistent. No source code has been modified by #137, no public derived point is admitted, and no incorrect physical image claim is required by the R2 contract.

### P1 — No unresolved **design-only** blocker from R1

The prior three P1 findings have normative resolutions. This does **not** pre-approve future implementation; first-source tests must demonstrate the specified hash, native, warning and failure-state invariants.

### P2-F1 — Make branch-direction agreement an executable B1a acceptance rule

**Design `3 / positive hit gate.** “Explicitly checked finite direction consistency tolerance” requires a concrete reviewed angular/vector error policy in the **source PR**, not merely a check that vectors are finite. Also verify the complete native per-interface interaction count when asserting exactly one encounter; `interface-first-event` alone carries only the first event. Require negative controls for mismatched outgoing branch/hit directions and misleading callback order. **Nonblocking for design owner decision; mandatory for source acceptance.**

### P2-F2 — Implement strict parser/identity/precedence as hostile-to-ambiguity tests

**Design ``2–5.** Unit-test nested duplicate keys (including identical-valued duplicates), extra/wrong nested fields combined with missing facts, ±180° modulo equivalence, component reorder equality, mutation after input snapshot, altered simulation/presentation/native pin, A/B role swaps, stale summary SHA and pre-run family mismatch. The baseline authoring inspector is not enough to satisfy this new total-order refusal policy. Also define the exact reported counter boundary on an executor call that throws during startup. **Nonblocking for design owner decision; required for B1a source PR.**

### P2-F3 — Prove finite-window and interruption behavior at source gate

**Design ``2, 5, 7.** The newly narrowed **2 mm and 10 mm** length endpoints are proposed, not validated native-positive domains; exercise both with suitable genuine hit/miss scenes and the existing endpoint ambiguity threshold, as well as full Fresnel versus transmitted-only warnings. Test 0/1/2 attempted/completed counts for first-run failure, legitimate first-run miss, second-run startup failure and hard interruption. File-level SHA checks, no clobber, no premature successful manifest and no stale partial-directory resume need adversarial fixture tests. **Nonblocking for design owner decision; required for source acceptance.**

### P2-F4 — Correct the now-stale opening PR description before owner disposition

The **opening** of [PR #137](https://github.com/physicsvigilante/opticsim/pull/137) still describes immediately “optional ADVISORY 2D backward line geometry” and first-release speculative `0.01 / 0.5 mm / 2×` numeric display thresholds, though later appended R2 notes and the **actual final document** withdraw that B1a feature. This is a misleading review/owner entry point, not a defect in the final R2 design. Update PR summary to lead with **B1a native hits only; all derived coordinates withheld**; label B1b deferred. No PR metadata was changed by this review.

### P2-F5 — B1b accuracy remains a distinct, unfulfilled gate

The proposed `6` stress matrix is well scoped, but no actual admitted domain, numerical uncertainty/sensitivity bound, tested local tangent/normal algorithm, near-parallel/antiparallel refusal policy or preregistered tolerances yet exist. A 5 mm positive fixture, algebraic residual or hypothetical post-native perturbation cannot calibrate the native solver. Reject any attempt to back-port old heuristics, reveal debug backextensions in public output, or reinterpret `advisory` as accuracy approval. B1b needs separate preregistration **before** real stress runs, independent feasibility review, versioned opt-in contract and exact-source implementation review.

### P3 — Teacher-facing terminology

Prefer **“two independent native ray samples crossing the same finite detector”** and show scene directions, sampled hit coordinates/unit directions, per-run statuses and qualification next to each event. Avoid “observer,” “eye,” “image position,” “visibility,” “darkness” and “unique image” in B1a affordances. Both `observerAssessment` and `imageAssessment` should stay `not-assessed`, not boolean negatives.

## 6. Verified final-source GitHub CI and what it proves

I independently queried workflow runs by exact authored HEAD and obtained **11/11 completed, successful pull-request workflows, each attempt 1**, with no reported failed workflow. The two representative exact-HEAD raw job logs were inspected:

- [Planar refraction workflow #44247326360, job #134609411214](https://github.com/physicsvigilante/opticsim/actions/runs/44247326360): actual checkout of synthetic **`45f4eaa...`**, **Node v24.19.0**, pinned **PhyDemo `811f508d2b070898c241a568b0c167dcb8645251`**; Node TAP reports **790 tests, 790 pass, 0 fail**; native/browser regression steps completed successfully.
- [Optical composition workflow #44247326431, job #134609318996](https://github.com/physicsvigilante/opticsim/actions/runs/44247326431): same merge checkout, same Node/native pin, baseline test/build success and real preinstalled **Chrome 157.0.8103.50** browser acceptance **27 checks / 15 screenshots**, hosted smoke **5 checks / 1 screenshot**.

This **is builder CI inspected by an independent reviewer**, not 11 independently executed validations. Because this PR adds **documentation only**, its 790 legacy production tests cannot execute the nonexistent pair request, new standalone CLI, strict B1a parser/status reducer, manifest protocol, future 2/10 mm B1a acceptance fixtures, B1b numerical geometry or eye/image capability. The 12 additional #135 research tests are **not merged into this production baseline**.

**Independently performed in this pass:** full exact R2/R1/request/previous research reading; raw Git HEAD/base/merge tree and parent inspection; compare/ancestry and one-file scope verification; current-base source-level compatibility checks; exact-HEAD CI workflow/job-step/raw-log inspection; independent numerical arithmetic from separately published native readings; design and status/exception-path analysis. **Not independently run:** fresh Node 24 suite, local build, PhyDemo native traces, new B1a CLI, Chrome/browser, new 2/10 mm fixture executions, B1b stress campaign, or any image/observer verification.

## 7. Owner decision and follow-on gates

The **B1a native-hit-only design** is sufficiently bounded for the owner to decide whether to commission a **separate main-based, draft B1a implementation PR**, with its own parser, full-scene integrity check, two authentic pinned-native runs, complete four-observable readouts, warning/status matrix, no-public-geometry guard, evidence manifest, source tests and independent physics/code review. A later **B1b** remains opt-in and separately gated by preregistered numerical testing and independent acceptance. The research-only #135 and held #129/#133 branches remain independent. [Main protection issue #123](https://github.com/physicsvigilante/opticsim/issues/123) is not resolved by this review. **Do not merge #137, change production files, authorize a public calculated point, or describe sampled detector hits as an eye/image.**
