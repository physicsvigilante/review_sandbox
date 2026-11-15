# Opticsim PR #81 — independent Chat B targeted R2 design re-review (round 2)

- **Source / PR:** [physicsvigilante/opticsim PR #81](https://github.com/physicsvigilante/opticsim/pull/81), still **draft, open and unmerged** when checked.
- **Production base:** `00e6211d6d40c0db8c62910f9e57b910b6aeb6f5`.
- **Exactly reviewed revised design head:** `d814455cf823907551cbc7914d1f8b3b508efcab` (confirmed as live PR head during review).
- **Prior, unchanged reviewed head:** `df783a3c2f5e51ad5edbacd35f6d82f1a02cfea7`.
- **Pinned revised document:** [NATIVE-RAY-PROVENANCE-PROPOSAL.md at revised head](https://github.com/physicsvigilante/opticsim/blob/d814455cf823907551cbc7914d1f8b3b508efcab/docs/NATIVE-RAY-PROVENANCE-PROPOSAL.md).
- **Actual scoped diff:** [old review head → revised head](https://github.com/physicsvigilante/opticsim/compare/df783a3c2f5e51ad5edbacd35f6d82f1a02cfea7...d814455cf823907551cbc7914d1f8b3b508efcab). Confirmed **one documentation file, +46/−18**, one commit; no feature implementation in this revision.
- **Reviewer:** Chat B, independent *conversation/context*, GPT-6; not an independent human optics specialist or proof of different model weights.
- **Review date:** 2026-11-15 (IST).
- **Scope / classification:** targeted re-review of corrections F-01–F-07 to **R2 pre-implementation design only**. Original [review-01](review-01-chat-b.md) remains **CHANGES-REQUESTED at its old head**. This report does not replace it or certify code.
- **Repository changes by reviewer:** none to Opticsim or its draft PR; the only write is this new report in the separate review hub. No merge or deployment.
- **New native/browser tests run by reviewer:** **none**. Reviewed pinned source/contracts and GitHub CI metadata; independently recomputed elementary Snell reference values. No CI logs or ZIP artifacts were downloaded anew for this round.
- **Updated-head CI observed:** GitHub returned **11 completed/success** workflow runs associated with revised head (run IDs `43733303685`, `43733303689`, `43733303691`, `43733303696`, `43733303713`, `43733303720`, `43733303726`, `43733303744`, `43733303756`, `43733303778`, `43733303796`). They test a **documentation-only** revision, not the unimplemented provenance feature.

**Outcome: `pass` — DESIGN ONLY.** The revised normative contract resolves the previous three major design objections and the four smaller clarification requests sufficiently for the owner to *consider separately authorizing bounded implementation*. There is **no demonstrated production code defect and no implementation sign-off**. Critical tests remain unperformed because this is a design, not an implemented feature.

## Findings against the exact revised diff

### F-01 — RESOLVED at design level (formerly MAJOR): no-hit lost source must not become a valid empty graph

**Evidence:** [proposal lines 69–92](https://github.com/physicsvigilante/opticsim/blob/d814455cf823907551cbc7914d1f8b3b508efcab/docs/NATIVE-RAY-PROVENANCE-PROPOSAL.md#L69-L92), [fail-closed table lines 95–103](https://github.com/physicsvigilante/opticsim/blob/d814455cf823907551cbc7914d1f8b3b508efcab/docs/NATIVE-RAY-PROVENANCE-PROPOSAL.md#L95-L103), [acceptance line 126](https://github.com/physicsvigilante/opticsim/blob/d814455cf823907551cbc7914d1f8b3b508efcab/docs/NATIVE-RAY-PROVENANCE-PROPOSAL.md#L126). At the [pinned upstream SingleRay](https://github.com/ricktu288/ray-optics/blob/811f508d2b070898c241a568b0c167dcb8645251/src/core/sceneObjs/lightSource/SingleRay.js#L94-L106), one native start returns `newRays:[ray1]`; [Simulator initialization](https://github.com/ricktu288/ray-optics/blob/811f508d2b070898c241a568b0c167dcb8645251/src/core/Simulator.js#L531-L543) invokes optical object starts and enqueues returned rays.

The v2 contract demands exact validated-source-to-native-instance registry equality *before execution*, exactly one observed start per required source, exactly one unique valid returned object and successful registration by actual `WeakMap` identity. It explicitly rejects reliance on the old per-source meter sum as independent evidence. These invariants are evaluated **before** an empty crossing result can be accepted. Therefore, a missing/nonrecording source observer with zero downstream callbacks is not permitted to look like a real miss.

**Required implementation falsification:** Run an actual valid no-hit scene (positive control), then delegate the actual start but silently omit its identity registration (negative control), with **zero interface/detector callbacks** in both. Expected `available` empty only for the complete positive ledger; `unavailable / PROVENANCE_UNKNOWN_OR_INCONSISTENT` for the negative. Also test 0/2 starts and malformed/duplicated returned rays. Not executed here.

### F-02 — RESOLVED at design level (formerly MAJOR): original callback delegation and legacy measurements

**Evidence:** [proposal lines 113–116](https://github.com/physicsvigilante/opticsim/blob/d814455cf823907551cbc7914d1f8b3b508efcab/docs/NATIVE-RAY-PROVENANCE-PROPOSAL.md#L113-L116); production [`observeSourceSet` / `observeDetectorSet`](https://github.com/physicsvigilante/opticsim/blob/00e6211d6d40c0db8c62910f9e57b910b6aeb6f5/src/adapter.js#L75-L175), [`observeInterfaceSet`](https://github.com/physicsvigilante/opticsim/blob/00e6211d6d40c0db8c62910f9e57b910b6aeb6f5/src/planar-media.js#L53-L102), and pinned [`Detector.onRayIncident`](https://github.com/ricktu288/ray-optics/blob/811f508d2b070898c241a568b0c167dcb8645251/src/core/sceneObjs/other/Detector.js#L244-L261).

The revised design now **forbids independent nested/competing native-calling wrappers**, mandates one owning per-instance callback pipeline installed before start, captures pre-mutation object reference/arguments, delegates to the original exactly once with identical `this`/arguments, observes returned child references, and returns the *same* return object. It explicitly covers **selected and nonselected detectors** and preserves signed power, ordinary crossings, interface first events and optional positional events. This is conceptually coherent with current existing before/after observer semantics. No new ray propagation or array modification is allowed.

**Required future evidence:** wrapped/unwrapped pinned-native comparisons for counts, power, interface first event, child/parent object identity, segments, truncation and undefined behavior; reversed component ordering as separate scenes; parent-equals-child, duplicated child and orphan faults must refuse without changing native physics.

### F-03 — RESOLVED at design level (formerly MAJOR): private graph, public-surface suppression and A → B → A

**Evidence:** [proposal lines 87–92, 99–109, 117–118 and 132](https://github.com/physicsvigilante/opticsim/blob/d814455cf823907551cbc7914d1f8b3b508efcab/docs/NATIVE-RAY-PROVENANCE-PROPOSAL.md#L87-L132); existing [CLI summary/diagnostics split](https://github.com/physicsvigilante/opticsim/blob/00e6211d6d40c0db8c62910f9e57b910b6aeb6f5/scripts/author-scene.mjs#L30-L55), [native snapshot](https://github.com/physicsvigilante/opticsim/blob/00e6211d6d40c0db8c62910f9e57b910b6aeb6f5/src/native-observations.js#L1-L13), [hash-only evaluator](https://github.com/physicsvigilante/opticsim/blob/00e6211d6d40c0db8c62910f9e57b910b6aeb6f5/src/observables.js#L65-L82), [Session revision guard](https://github.com/physicsvigilante/opticsim/blob/00e6211d6d40c0db8c62910f9e57b910b6aeb6f5/src/session.js#L19-L44) and [QualifiedUI sequence/revision guard](https://github.com/physicsvigilante/opticsim/blob/00e6211d6d40c0db8c62910f9e57b910b6aeb6f5/src/qualified-ui.js#L152-L161).

The changed contract keeps *all* token/parent/crossing metadata private until **terminal native completion plus every source, identity, detector, scope and cap gate**; it prohibits graph fields not only in requested results but also in raw checker diagnostics, CLI JSON, browser/debug/session state and qualified exports on invalid attempts. Explicit **run epoch in addition to scene SHA** handles a delayed first-A callback after A → B → A; a fresh same-hash run gets a new registry. The graph reaches the public evaluator only as a fully gated, bounded opt-in projection, never as temporary diagnostics. This is an adequate design-level publication boundary; the current CLI and UI dataflow must be adapted to enforce it, not assumed safe already.

**Required future evidence:** inspect full public report and browser/export surfaces during pending, failed, stopped, truncated, warned, unknown and stale runs; test delayed old-A completion after fresh A; test clearing prior accepted public result at invalidation, raw import and rerun. No such execution performed in this review.

### F-04 — RESOLVED (warning/approximation priority)

[Proposal lines 95–109](https://github.com/physicsvigilante/opticsim/blob/d814455cf823907551cbc7914d1f8b3b508efcab/docs/NATIVE-RAY-PROVENANCE-PROPOSAL.md#L95-L109) now normatively prioritizes stale/incomplete `suppressed`, then unsupported/native-warning/identity/cap `unavailable`, then `qualified` **only** for an otherwise clean explicitly transmitted-only `partialReflection:false` model caveat, or `available` for a clean full Fresnel model. Machine reason codes are distinct from explanation text. This corrects the original conflation between model approximation notes and **actual native execution warnings**. Existing generic observable warning behavior cannot be reused blindly for this new kind.

### F-05 — RESOLVED (allowlist, caps and shared identity)

[Proposal lines 23–31, 109 and 129](https://github.com/physicsvigilante/opticsim/blob/d814455cf823907551cbc7914d1f8b3b508efcab/docs/NATIVE-RAY-PROVENANCE-PROPOSAL.md#L23-L31) now explicitly allow only **one v5 planar interface, 1–2 `point-source/single-ray`, 1–2 passive detectors, zero other types**; both requested detectors share one epoch/identity registry but independent **32-hit** caps. Global **64-object** overflow refuses all provenance, whereas an overflowing nonrequested detector count alone cannot fail the other selected detector. Cap boundary trials `64/65` and `32/33` are correctly labeled **injected observer fault-stream guard tests**, not physically reachable ordinary cases in this narrow source domain. A native detector's ordinary total count is not capped.

### F-06 — RESOLVED (identity versus critical-angle physics)

[Proposal lines 28, 118, 125 and 133](https://github.com/physicsvigilante/opticsim/blob/d814455cf823907551cbc7914d1f8b3b508efcab/docs/NATIVE-RAY-PROVENANCE-PROPOSAL.md#L118-L133) separate near/exact-critical **observed object identity** from reliable numerical angles or detector-destination predictions. Independently recomputed (analytical, **not native tests**): `asin(1/1.5)=41.8103148957786°`, high→low index 1.5→1 at 30° gives `48.5903778907291°` refraction, 50° is TIR, and low→high 1→1.5 at 30° gives `19.4712206344907°`. The pinned [`BaseGlass` discriminant `sq1<0`](https://github.com/ricktu288/ray-optics/blob/811f508d2b070898c241a568b0c167dcb8645251/src/core/sceneObjs/BaseGlass.js#L204-L283) explains exact-critical sensitivity. This design certifies neither an optical path nor physical critical-limit behavior.

### F-07 — RESOLVED (teacher-facing limits and run-local tokens)

[Proposal lines 69–79 and 117–119](https://github.com/physicsvigilante/opticsim/blob/d814455cf823907551cbc7914d1f8b3b508efcab/docs/NATIVE-RAY-PROVENANCE-PROPOSAL.md#L69-L79) declare `method:"native-observed-object-parentage"`, run-local ephemeral token semantics and a machine-readable limitation. Same-object interactions yield **no** new edge; `detector-hit-events` cannot be paired by assumed index; no full route, image, irradiance, source-image interpretation, propagation time or inferred material result is claimed. That is the right narrow teaching contract for direct native ancestry.

### A-01 — MINOR, nonblocking **implementation watchpoint** (new adversarial control, not an observed defect)

The **installation** of one owning observer for every admitted interface and selected/nonselected detector is mandatory [lines 113–115](https://github.com/physicsvigilante/opticsim/blob/d814455cf823907551cbc7914d1f8b3b508efcab/docs/NATIVE-RAY-PROVENANCE-PROPOSAL.md#L113-L115), but the source ledger is the only component class with a separately spelled-out installed-registry equality assertion. Ordinary detector crossings and new provenance could be counted in the **same** owning wrapper; agreeing counters are then not independent evidence if that wrapper was never installed. A fault that delegates the genuine detector callback while silently losing both records could falsely look like an empty detector result unless handler-installation coverage is asserted. This is **not** a compliant implementation of the revised one-wrapper requirement, so it does not reopen the design.

**Concrete implementation safeguard:** preflight-assert exact validated-ID/native-instance/handler ownership for **all** admitted interface and detector observers, not only sources, and inject a *test-only missing/nonrecording selected-detector wrapper* while the actual detector receives a crossing. Expected **unavailable**, never `available` empty or synthetic attribution. Retain existing source and native detector power/count checks; do not mislabel two counters from one wrapper as independent simulator corroboration. Also test a nonselected detector fault and the per-detector cap isolation rule. This closes a plausible accidental implementation false-positive without adding a generic ray-history system or changing native physics.

## Independent evidence and limits

1. **Actually inspected in this conversation:** central [PROTOCOL.md](https://github.com/physicsvigilante/review_sandbox/blob/main/PROTOCOL.md), [REVIEW-RISK-POLICY.md](https://github.com/physicsvigilante/review_sandbox/blob/main/REVIEW-RISK-POLICY.md), [FOLLOW-UP-02.md](../FOLLOW-UP-02.md), [Chat A response](../responses/response-01-chat-a.md), original [review-01](review-01-chat-b.md), this exact revised proposal, original production `AGENTS.md`, `docs/PLANAR-REFRACTION.md` and `docs/DETECTOR-HIT-EVENTS.md`, production adapter/observers/CLI/native snapshot/session/UI source, and pinned upstream `SingleRay`/`Simulator`/`BaseGlass`/`Detector` methods. **Checked actual source diff rather than adopting Chat A's self-triage.**
2. **Diff identity and live state:** one updated document (+46/−18) and the current PR head/base checked directly through GitHub. Earlier review remains correct for its old SHA; no re-review of unchanged unrelated architecture.
3. **CI observed, not rerun:** 11 successful docs-only workflow records associated with updated commit; no new code-level evidence is implied. The original review's PR #79/#80 native research and artifact claims are retained as *historical Chat A evidence*, not independently rerun or rehashed here.
4. **Independently calculated:** basic Snell/TIR angles listed in F-06 (a small analytical check). **No native simulations, callback injections, browser runs, screenshots, installs, full project tests, or CI reruns by Chat B.**
5. **Limit of this verdict:** even a carefully written ledger contract is not evidence that the eventual installer, run-epoch propagation, asynchronous exporter or numerical statuses work in code. No production bug was observed or claimed.

## Separate scope judgments

| Dimension | Judgment | Basis |
|---|---|---|
| Source interpretation fidelity | **Unknown** | The source IDs remain authored labels, not independently verified textbook/image interpretation. |
| Physical/numerical correctness | **Unknown for implementation** | Pinned native algorithms inspected; elementary independent Snell references recomputed; near-critical correctness not certified. |
| Native simulation and observable coverage | **Design pass; implementation untested** | Callback object/return semantics support minimal direct ancestry; no new feature or new Chat B native run exists. |
| Evidence integrity and provenance | **Design pass; release evidence pending** | Exact prior/revised SHAs and one-file diff established; strict private data/run-epoch gates prescribed; current CI is docs-only. |
| Teacher-facing usefulness | **Plausible but untested** | Narrow child/source explanation could be educational; no path/image/illumination claim or classroom assessment. |
| Textbook-answer completeness | **Not assessed** | No problem answer solver or independent source-backed task success added. |

## Release advice

**`pass` applies only to the revised pre-implementation proposal.** The owner may separately approve a **bounded implementation**, with emphasis on the genuine clean-zero-hit versus silently missing-root pair; exact once/return-reference and two-detector compatibility; missing selected-detector observer safeguard A-01; injected parent/cycle/cap faults; native-warning-versus-model-caveat precedence; whole-surface non-leakage; and A → B → A delayed-callback suppression. Use exact-head pinned-native evidence, no-opt-in historical fingerprints, accepted full CI and real browser regression where the feature is exposed.

**Keep source PR #81 draft and unmerged.** The implementation must receive its own **new R2 independent code/evidence review** and explicit owner merge approval. This report does not authorize source commits, a production merge, a native solver change, or a broader ray-history engine.
