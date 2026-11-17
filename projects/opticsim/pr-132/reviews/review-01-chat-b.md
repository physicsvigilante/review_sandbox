# Chat B — independent design review: Opticsim PR #132

**Date:** 2026-11-18 (Asia/Kolkata)
**Verdict: CHANGES REQUESTED.**
**Scope:** Exact draft, design-only source. This is not a review of implemented optics code or a fresh review/approval of PR #131. No code, tests, dependencies, workflow or production branch were modified by this review.

## 1. Exact source and governance identity — independently verified

| Check | Independent finding |
| --- | --- |
| [Opticsim PR #132](https://github.com/physicsvigilante/opticsim/pull/132) | Open, draft, unmerged |
| Production base | `d3509e82fb65d81aabe336666851f8f2962623f4` |
| PR source HEAD | `07dcf1d6ed0c094071d2d5347ab14baa2bd35c04` |
| Source Git tree | `0917d9d70a01ae107b08bb0a031524cc32df3a07` |
| Synthetic merge commit | `ab6f82ef377a31f9e1649c12a4678936a78b186c` |
| Synthetic merge Git tree | `0917d9d70a01ae107b08bb0a031524cc32df3a07` — **identical** |
| Diff | Only new `docs/jee-apparent-depth-observer-contract-v1.md`; **140 additions, zero deletions, one commit** |
| Source content blob | `e9760bac0e6489482d4a09e43ba8c0ea65dec16f` |
| Actual current `main` | `d3509e82fb65d81aabe336666851f8f2962623f4`; **unprotected** |

I fetched Git commit objects independently: the design HEAD has the stated production base as its sole parent; the synthetic merge has base and design HEAD as parents; the trees coincide. The base-to-head compare and complete PR patch confirm a 140-line documentation-only addition. No application source, native engine, schema v20, tests, existing saved scenes, vendor pin, or viewer is changed.

The production [problem dispatcher](https://github.com/physicsvigilante/opticsim/blob/d3509e82fb65d81aabe336666851f8f2962623f4/src/problem-workflow.js), [planar angular facts solver](https://github.com/physicsvigilante/opticsim/blob/d3509e82fb65d81aabe336666851f8f2962623f4/src/planar-angle-queries.js), [native observables](https://github.com/physicsvigilante/opticsim/blob/d3509e82fb65d81aabe336666851f8f2962623f4/src/observables.js), [run-problem CLI](https://github.com/physicsvigilante/opticsim/blob/d3509e82fb65d81aabe336666851f8f2962623f4/scripts/run-problem.mjs), [scalar Snell guard](https://github.com/physicsvigilante/opticsim/blob/d3509e82fb65d81aabe336666851f8f2962623f4/src/angular-math.js), and [v5 planar geometry](https://github.com/physicsvigilante/opticsim/blob/d3509e82fb65d81aabe336666851f8f2962623f4/src/planar-media.js) were inspected at the exact base. The separate [PR #131 independent research review](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-131/reviews/review-01-chat-b.md) was read, not treated as new runtime evidence. [PR #129](https://github.com/physicsvigilante/opticsim/pull/129) and [PR #131](https://github.com/physicsvigilante/opticsim/pull/131) remain draft/unmerged. [Issue #123](https://github.com/physicsvigilante/opticsim/issues/123) documents held v14–v19 dependencies and the main-branch protection gap; #132 introduces none of those held dependencies.

## 2. Independent physical derivation and numerical verification

Choose a local frame with the single infinite plane at x=0, source/object at (-d,0), object medium on x<0, receiving/observer medium on x>0; this is a local convention, **not an authored global scene or eye position**. Let r=n_object/n_observer, and i be the **object-medium angle to the plane normal**. A ray with incident sign +i meets the interface at (0,d tan i). Snell gives sin t = r sin i. Its transmitted supporting line is y=d tan i + x tan t. The -i ray has the opposite sign. Their *backward extensions* intersect at x=-d tan i/tan t, y=0, provided a transmitting, nondegenerate solution exists.

Thus the symmetric-ray normal depth is

- `d_s(i) = d tan(i)/tan(t) = (d/r) sqrt(1-r² sin²(i))/cos(i)`;
- the continuous near-normal limit is `d_a = d/r = d n_observer/n_object`; **no near-zero tangent division is needed**;
- with `z=sin²(i)`, `(d_s/d_a)²=(1-r²z)/(1-z)` and `d/dz [(d_s/d_a)²]=(1-r²)/(1-z)²`.

Accordingly, for a safe wholly transmitting interval, symmetric depth decreases with angle for r>1, increases for r<1, and is exactly d for r=1. The endpoint interval is a **conditional symmetric two-ray construction** only. It is not arbitrary-observer positional uncertainty, native numerical error, a common finite-pupil observation, or a unique stigmatic image. Non-symmetric oblique rays need not back-intersect at one point. The distinction between object-medium i and receiving-medium t is essential.

Independent high-precision Snell calculations (not PhyDemo runs):

| d; object → receiving indices | object incidence | symmetric depth | paraxial depth |
| --- | ---: | ---: | ---: |
| 120 mm; 1.5 → 1 | 0° limit | 80.0000000 mm | 80 mm |
| same | 0.1° | 79.999847690836 mm | 80 mm |
| same | 1° | 79.984764584681 mm | 80 mm |
| same | 5° | **79.6163668477505 mm** | 80 mm |
| same | 30° | **61.1010092660779 mm** | 80 mm |
| 120 mm; 1 → 1.5 | 10° | **181.547904626475 mm** | 180 mm |
| 120 mm; 1 → 1 | 30° | **120 mm** | 120 mm |

For 1.5 → 1, `i_critical=asin(2/3)=41.81031489578°`. Above critical, no propagating refracted ray exists; at/near critical, floating-point classification and depth sensitivity require a conservative refusal. A 30° symmetric pair differs from the 80 mm paraxial value by **18.8989907 mm**, approximately **23.62%** of that value. For 1 → 1.5, an 89.999° incidence (no TIR) gives symmetric depth about **7.687 million mm** for the same 120 mm object depth: restricting only TIR cannot bound this construction. r=1 deserves an exact equality branch near grazing to avoid cancellation.

The numerical 5° output and labels in [D-01 lines 39–93](https://github.com/physicsvigilante/opticsim/blob/07dcf1d6ed0c094071d2d5347ab14baa2bd35c04/docs/jee-apparent-depth-observer-contract-v1.md#L39-L93) are mathematically correct **when read with their stated conditional limitations**.

## 3. Ranked findings, required corrections, and positive assessments

### P0 — No demonstrated fundamental physics blocker

The paraxial formula, symmetric-ray derivation, Snell/TIR distinctions, local source/receiving-side orientation and separation between non-native A and future native B are sound. Neither an eye location nor a native image can be inferred from A. The design correctly refuses slabs, curved media, unspecified observers, diffraction and arbitrary optical composition.

### P1-A — A's result status overclaims inside the existing dispatcher contract (revision required before coding)

[D-01 lines 60–93](https://github.com/physicsvigilante/opticsim/blob/07dcf1d6ed0c094071d2d5347ab14baa2bd35c04/docs/jee-apparent-depth-observer-contract-v1.md#L60-L93) uses `status:'available'` for a result whose stated validity depends entirely on a declared paraxial assumption. The accompanying method, warnings, `qualification.basis:'assumption-dependent'`, `native.status:'not-run'`, and `interpretation/questionSupport:'not-assessed-by-engine'` are strong mitigations, **but cannot guarantee all downstream consumers will preserve those fields**.

Existing `src/planar-angle-queries.js` returns `conditional` for explicit analytical branches; `src/observables.js` returns `conditional` for ideal-image analysis, whereas actual native observations use `available` or `qualified` when eligible. `resultCoverage` currently counts all three statuses as coverage, and `method-suitability.js` explicitly categorizes them as conditional results in that routing context. Therefore the safe normative status for A, both standalone and mapped into problem results, is **`conditional`**; do not conflate computability with observation. Preserve `method`, declared assumption(s), limitations, provenance/warnings and `native.status:'not-run'` on both calculations and report/UI paths. Where no angle cone was given, `symmetricAngleEnvelope:null` and an explicit no-quantitative-cone-bound notice remain correct.

Also reconcile refusal categories with the current dispatcher: absent required facts/assumption should be **`needs-information`** in problem-workflow results; malformed values/unknown fields are **`invalid-input`**; physically unsupported scopes or TIR cone are **`unavailable`**, and near-critical numerical uncertainty can be **`numerically-indeterminate`** if a dedicated status is approved. One blanket `unavailable` for missing input and invalid input, as currently proposed, loses a meaningful existing distinction. All refusals must retain null value, typed reason and zero native calls.

### P1-B — The finite-cone acceptance policy contradicts an unqualified paraxial-ready result (revision required before coding)

[D-01 lines 33–58](https://github.com/physicsvigilante/opticsim/blob/07dcf1d6ed0c094071d2d5347ab14baa2bd35c04/docs/jee-apparent-depth-observer-contract-v1.md#L33-L58) currently accepts any stated `0<maxIncidentAngleDeg<90` subject to TIR/critical guard, while `viewing.model:'paraxial'` asserts near-normal viewing. A 30° cone is well below critical for 1.5 → 1 yet yields a 23.62% shift from the paraxial depth; a nearly grazing cone at r<1 can cause huge, highly sensitive results without TIR. This is not merely a missing implementation tolerance.

**Required decision:** define an explicit near-normal admission criterion/controlled approximation domain for A, or treat wide cones as *finite-angle diagnostic only*, clearly flagging that the single paraxial value is not validated for that cone. Decide whether the 30° A6 case is a refusal or an explicitly non-paraxial diagnostic; it must not silently show `available` approximate depth. Include a conservative validated near-critical **and near-grazing** guard, bounded and finite derived output, lower numerical depth clearance (a positive subnormal input may underflow to apparent zero), and handling for equal/nearly equal indices. No arbitrary tolerance from PR #131's research harness should be reused as a physics certification.

### P1-C — The exact registered request and native-free CLI contract are not yet specified (revision required before coding)

D-01 names a fact `format`, a result `kind`, and a possible helper, but **does not define the problem query-format/evaluator mapping and evidence behavior** required to fit the current deterministic dispatcher. At the exact base, `src/problem-workflow.js` maintains separate known-kind registries, query formats, accepted `physical.format` families, strict request-field validation, a calculator result list and `verifyNative` handling. An unknown new fact family is currently sent toward `resolveProblemRequest`, not to a standalone apparent-depth evaluator. `scripts/run-problem.mjs` and `scripts/preflight-problem.mjs` depend on that same registration; `scripts/author-scene.mjs` follows a native scene/build path and is not a native-free facts CLI.

**Before coding, document a normative invocation** for `opticsim-problem-v1` with an exact requested kind, declared accepted facts family and query contract, plus the intended standalone facts CLI route (if separate). Specify how `verifyNative:true` on reduced facts is refused/not-run without inventing a scene, how `native.required/canRun/calls` remain false on A-only cases, how output qualifiers survive the dispatcher/calculation serializer, and which input/output hashes and errors are persisted. This is a bounded registration change, not authorization for natural-language routing, new v20 schema or reworking the whole architecture.

### P2-A — B resolves the conceptual P1-B observer-selection omission only at detector-window level

[D-01 lines 95–103](https://github.com/physicsvigilante/opticsim/blob/07dcf1d6ed0c094071d2d5347ab14baa2bd35c04/docs/jee-apparent-depth-observer-contract-v1.md#L95-L103) appropriately requires two separately authored v5 single-ray runs, the same **actual finite detector segment** and independently completed transmitted hits. This is better than interpreting PR #131's 2,000 mm research detector as a pupil. But it still establishes only two selected crossings in separate runs, **not simultaneous rays entering a person's eye**. The request's physical meaning must remain a derived, detector-selected pairwise *2D line point*.

Native `detector-hit-events` exposes bounded hit coordinates/incoming directions with **callback order, not source ID or complete path**; `interface-first-event` is an encounter measurement, not a path ledger. Require strict one-source/one-emission/one-plane/one interaction/one unambiguous transmitted branch/one detector hit per run, including matching native branch direction, endpoint clearance, scene-equivalent geometry and run-specific evidence. Require receiver-side detector and source-side backextension in the **oriented plane-normal frame**, not a fixed global x sign. No implicit association by array index or label; reject unqualified lineage rather than fabricating it. Future departures from that exclusivity need a separate provenance design.

### P2-B — B's P1-A qualification principle is correct; formalize the derived evidence shape before any B code

[D-01 lines 103–109](https://github.com/physicsvigilante/opticsim/blob/07dcf1d6ed0c094071d2d5347ab14baa2bd35c04/docs/jee-apparent-depth-observer-contract-v1.md#L103-L109) explicitly repairs the research helper's `qualified → available` mistake in principle. The declared lattice is appropriate: stale/incomplete/suppressed evidence never yields a point, unavailable/ambiguous evidence never yields a point, and **any qualified accepted input makes the derived geometric result qualified**, with original caveats preserved. This is **not yet implemented**.

For future B, define a versioned immutable result/evidence structure containing **both** source-scene hashes, native pin, invocation identities, detector/source/interface IDs, authored directions, original per-run native status, each source observable's status, warnings, count/hit/branch evidence, and any derived numerical-withholding reasons. Verify equality of complete apparatus/numerical controls after excluding **only** the explicit direction change. Capture/snapshot values before asynchronous hash/evaluation and fail closed on stale or cross-run mixture. Preserve warnings and run association even for a null derived result; distinguish `suppressed` from `unavailable` in consumers and serialization. Never silently treat `qualified` first-encounter or detector evidence as `available`.

### P2-C — B's geometry and numerical tests are a credible *plan*, not a certified estimator

For `p₁+s₁u₁=p₂+s₂u₂`, both `s₁<0` and `s₂<0`, a source-side intersection, actual finite-window crossings and oriented physical compatibility are necessary. Two-line algebraic residuals alone are tautologically small and do not test correctness. Both small `|u₁×u₂|` near parallel **and** near antiparallel, grazing/TIR adjacency, near-equal media, long backward extrapolations and translated large coordinates must be checked. Review actual finite detector lengths and *both* hits; moving or shortening the segment must yield real misses. Test sensitivity to perturbations of actual hit/direction inputs and transforms, and preregister scaled thresholds, maximum-extrapolation budgets, endpoint clearance and withheld status. The research `1e-6` checks provide no native error certificate. Three nonconcurrent rays must not be averaged into one image. These unresolved numerical budgets are **B-only future gate requirements**, not evidence that B has already passed.

### P3 — Naming and consumer communication

Prefer a visibly qualified label such as “receiving medium (conventionally observer side)” for `observerIndex`; no actual observer position is supplied. `maxDifferenceFromParaxialMm` must be described as **difference between two stipulated geometrical constructions**, never a general error bar or eye/pupil uncertainty. Explicitly label equal-index return depth as the undeviated ray continuation, not proof of a physically generated virtual image. Keep “real object normal depth” distinct from an object's global x position.

## 4. Decision, revisions and further gates

The **two-capability decomposition is directionally sound**. A can use one-plane reduced facts without inventing a scene or eye; B must remain a separate native feasibility/release line. The current document nevertheless leaves three A **P1 contract decisions** unresolved: status/refusal semantics, physically honest angle-cone/numeric admission, and deterministic dispatcher/CLI mapping. **Revise D-01 before starting A implementation, then obtain a fresh exact-HEAD/tree independent review of the revised document.** Do not treat a revised design as an implemented or tested result.

After design resolution, any A implementation must be on a separate draft source branch with strict validation, original-facts fidelity/refusal tests, numerical checks including reverse/equal-index and near-critical/grazing cases, bounded no-native evidence and full Node24 integration/source review. B additionally needs a separate preregistered small finite-window native/conditioning research experiment, complete branch/warning provenance, and later code review. Held v14–v19 features, #129, the PR #131 research artifact and release/safety #123 remain distinct gates. No feature merge, auto-merge, production release or main protection change is authorized here.

**Evidence boundary / independence:** I read exact Git commit/tree/patch metadata, the full 140-line new design, the exact production dispatcher/observables/authoring and scalar contracts, prior independent #131 review, the linked request and governance items; I independently recomputed Snell and symmetric-ray depths with high-precision arithmetic. I **did not independently run PhyDemo, Node24 CI, Chrome or the browser viewer**, and did not verify numerical native precision for this unimplemented API. Previously reported successful CI runs are builder evidence for unchanged regression tests, not a certification of A or B. All optics production source and held PRs remain unchanged by this review.
