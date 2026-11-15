# Opticsim PR #88 — targeted Chat B R2 design re-review request (round 2)

This is a **targeted review of the five responses to the first design review**, not a new project-wide architecture review, a native solver patch, or an implementation-code review.

## Freeze and authorization

- Source [draft PR #88](https://github.com/physicsvigilante/opticsim/pull/88), base production main `fa158fc78da7a35b6a02eaed58c0cdbd4b699220`, pinned PhyDemo `811f508d2b070898c241a568b0c167dcb8645251`.
- **NEW exact design v2 head:** `391047a5467f8e27f7b2162074900e8387945b9f`, [pinned revised document](https://github.com/physicsvigilante/opticsim/blob/391047a5467f8e27f7b2162074900e8387945b9f/docs/NATIVE-FINITE-FORWARD-QUALIFICATION-PROPOSAL.md). Initial independently reviewed v1 head `28c4aa94bbbf6b5a63a8bef433c80186e08a3d35`.
- [One-file proposal-only v1→v2 diff](https://github.com/physicsvigilante/opticsim/compare/28c4aa94bbbf6b5a63a8bef433c80186e08a3d35...391047a5467f8e27f7b2162074900e8387945b9f) (+60/−22 markdown lines). No `src/` or vendor edits, no new executable tests in this revision. Previous PR #88 research runner, first failures and raw data remain untouched.
- [Independent Chat B review-01](reviews/review-01-chat-b.md) concluded **CHANGES-REQUESTED (DESIGN ONLY)**. Preserve that exact report and its old SHA. [Developer response](responses/response-01-chat-a.md) is an attributable implementation-side proposal, **not** external proof.
- Existing [review request](REQUEST.md) and [first Chat B prompt](REVIEWER-PROMPT-01.md) are historical; do not overwrite them or the first report.
- No source or CI permission to merge or change native numerical policies. A second design pass does not authorize Stage 1/Stage 2 implementation or release.

## Questions — prioritize conceptually unsafe false confidence

1. **B1:** Does the revised **Stage 0 research → separately approved Stage 1 diagnostic-only → separately approved Stage 2 mandatory policy** actually eliminate a premature mandatory gate? Is the diagnostic correctly **noncertifying** when exact-critical observer neutrality remains unproved? Is the one-callback-owner/postrun-BigInt model credible without proving behavior neutrality by comparing two different critical executions?
2. **B2:** Can the proposed **native callback incident point vs independently calculated finite crossing point P*** requirement address the reported-point counterexample, with `unknown` on unjustified tolerance? Must the contract state an exact testable error envelope **before even design** can be called pass, or can that legitimately be a later verified implementation prerequisite? Does the computed endpoint/vertex rule avoid false positives?
3. **B3:** Evaluate the **counterfactual Stage 2-only public publication matrix** for a completed-but-inconsistent, unknown, checked, checked-no-hit, stopped/incomplete and A→B→A run. Check no-request UI, raw checker, CLI, `summary.observations`, native result coverage, comparisons, qualified packages and browser. Does the Stage 1 advisory-only sidecar still risk presenting canonical readouts as vetted despite a demonstrated inconsistency? Distinguish `native.status`, `executionPassed` and measurement fitness.
4. **B4:** Is the 128-callback diagnostic cap now correctly labeled unproven policy rather than physics proof? Are 128/129 injected faults, 1–4 sources, 0–2 detectors, Fresnel true/false, long weak branches and bounded BigInt/browser cost required before production, without silently deciding a new cap?
5. **B5:** Does the new complete source, one-Glass and all-detector native callback-ownership rule reject a no-hit but missing-start/hook false clean? Is all-source direct emission evidence truly non-circular, and does a one-wrapper design preserve the original ray/return identity?

**Reviewer disposition:** `pass`, `changes-requested`, or `insufficient-evidence` at this **new exact design SHA**, explicitly **DESIGN ONLY**. If the SHA moved mark stale. Distinguish (a) design-level contracts now coherent, (b) numerical error bound and actual behavior neutrality unproved, and (c) future mandatory policy approval not yet sought. Do not treat lack of implemented tests as a demonstrated production code bug; do not claim any new run unless truly executed.

**Report:** A new append-only Chat B report at `projects/opticsim/pr-88/reviews/review-02-chat-b.md` using the central [REVIEW-TEMPLATE.md](../../../REVIEW-TEMPLATE.md). Do not rewrite `review-01-chat-b.md`, edit PR #88 source or merge anything. Return the new report's GitHub link.
