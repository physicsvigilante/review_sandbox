# Independent Chat B targeted R2 design re-review — Opticsim PR #88, round 2

**Verdict: PASS — DESIGN ONLY**, restricted to the corrected *pre-implementation* contract at exact source head `391047a5467f8e27f7b2162074900e8387945b9f`. This does **not** certify native geometry, observer neutrality, a production implementation, browser performance, Stage 1 authorization, Stage 2 mandatory withholding, or a source PR merge.

- **Reviewer:** Chat B, separate ChatGPT conversation (GPT-6), not an independent human or different model-family review.
- **Date:** 2026-11-16 (Asia/Kolkata).
- **Project:** `physicsvigilante/opticsim`; [draft PR #88](https://github.com/physicsvigilante/opticsim/pull/88).
- **Base:** `fa158fc78da7a35b6a02eaed58c0cdbd4b699220`; **reviewed v2 head:** `391047a5467f8e27f7b2162074900e8387945b9f`; reviewed prior v1: `28c4aa94bbbf6b5a63a8bef433c80186e08a3d35`.
- **Pinned design:** [NATIVE-FINITE-FORWARD-QUALIFICATION-PROPOSAL.md](https://github.com/physicsvigilante/opticsim/blob/391047a5467f8e27f7b2162074900e8387945b9f/docs/NATIVE-FINITE-FORWARD-QUALIFICATION-PROPOSAL.md); [exact one-commit v1→v2 diff](https://github.com/physicsvigilante/opticsim/compare/28c4aa94bbbf6b5a63a8bef433c80186e08a3d35...391047a5467f8e27f7b2162074900e8387945b9f).
- **Review material:** central `PROTOCOL.md`, `REVIEW-RISK-POLICY.md`, `FOLLOW-UP-02.md`, previous `reviews/review-01-chat-b.md`, Chat A `responses/response-01-chat-a.md`, pinned Opticsim `AGENTS.md`, pinned proposal and exact revision diff, plus PR metadata and exact-head workflow summaries. Historical first-review findings and failed CI history are not superseded.
- **Source changes during this review:** none. No source PR edits, production code, native engine, browser, or policy changes.
- **Risk:** R2 numerical/evidence-critical; **review scope:** targeted B1–B5 revised **design**, not executable implementation.

## Independent findings / re-disposition

### B1 — previously blocker: premature mandatory v9 gate / observer neutrality

**Resolved at design level; important empirical limitation retained.** The exact diff removes the initial mandatory v9 measurement gate. Stage 0 stays research only; proposed Stage 1 is separately authorized, opt-in and **explicitly noncertifying**; any mandatory Stage 2 is a *new policy decision* with separate owner approval, verification and R2 review. The same-run owner/wrapper contract requires one original native delegation with unchanged `this`, arguments, return identity, mutations and exceptions; hot callbacks take bounded scalar snapshots and defer exact BigInt processing. This is a coherent *proposed invariant*, **not** evidence of behavioral neutrality at numerically unstable critical geometry. Uninstrumented cross-run variability means apparent agreement/disagreement between different runs cannot prove or disprove observer neutrality. Tests must inspect actual within-run callback and return invariants, and separately examine distributions and benign-angle parity.

**Residual implementation risk (not a new design blocker):** ensuring even a snapshot failure never prevents original native delegation, that wrapper ownership is unique, and that output/callback timing is not perturbed remains unproved. Test fault injection for capture exceptions, hook substitution, output identity and native-error propagation before releasing an opt-in implementation.

### B2 — previously blocker: false incident-point accepted by finite-forward t/u

**Resolved at design level, pending independently justified uncertainty envelope.** For edge (10,0)→(10,10), incoming ray (0,5)→(1,5), represented-ray intersection is `t=10`, `u=1/2`, `P*=(10,5)`. A callback claiming `P_native=(10,7)` lies on the same finite edge and cannot be rejected by the original forward-`t`/finite-`u` test alone. The revised design explicitly requires **independent P* vs reported-point agreement** within a derived, adversarially tested numerical envelope; the (10,7) counterexample must not be `checked`. If a bound is unavailable or the event is near tolerance/conditioning/vertex ambiguity, the result is **unknown**, not clean or a gratuitous bug accusation. Both native and computed points receive edge/corner scrutiny, with exact `t>0`, strict cutoff and interior finite-`u` conditions.

**Residual prerequisite:** the design deliberately does *not* invent a global absolute tolerance. A future implementation must derive and independently challenge the scale/conditioning-aware point-error envelope against actual finite precision and native representations, including endpoint, near-parallel, translation, rotation, very short forward and two-close-face cases. Without it, affected events cannot be promoted to checked.

### B3 — previously blocker: inconsistent public surfaces and qualification meaning

**Resolved at counterfactual Stage-2 design level only.** Revised document distinguishes truthful native `completed`, ordinary `executionPassed`, per-run `numericalAudit`, and **separate measurement fitness**. Its proposed atomic run-epoch/revision envelope supplies coherent rows for completed checked, completed inconsistent, completed unknown/cap, complete zero-hit, incomplete/stopped/stale, A→B→A delayed callbacks, and non-v9. It explicitly covers checker/CLI, `runProblemEvidence`, `evaluateObservables`, `summary.observations`, result coverage/comparisons, no-request native UI, browser result panels, qualified authoring exports and raw import. Completed-but-inconsistent would *remain native-completed* while trusted native-dependent readouts are unavailable; raw counters/rendered rays may remain only conspicuously **unqualified**.

**Stage-1 caution:** advisory optics measurements remain *canonical under pre-existing rules*, not independently certified. When a Stage-1 diagnostic finds inconsistency, the relevant displayed result must clearly say the existing native-dependent values **are not certified by this diagnostic**. A clean advisory result must not silently upgrade canonical measurements. The proposal makes this distinction; UI testing must verify it in context, especially with no explicit result request and export/reopen.

### B4 — previously major: arbitrary 128 callback budget and insufficient coverage

**Resolved as a declared uncertainty and verification gate, not as an established bound.** The v2 proposal labels 128 as an **unvalidated diagnostic-availability budget**, never a physics cap. The 129th callback means unavailable, not an accepted first-128 partial pass or proof of native error. It requires 128/129 injected faults, 1–4 source cardinalities, 0–2 detectors, Fresnel full partial reflection on/off, weak/long branches, stop/truncation, memory/time/BigInt bit-cost and real-Chrome responsiveness before any production diagnostic. It does not secretly select a new proven limit.

**Residual prerequisite:** show actual admitted-scene upper-tail costs; bound snapshot storage and integer counter behavior without interfering with native propagation. Do not turn diagnostic unavailability into blanket refusal without separate Stage-2 authorization.

### B5 — previously major: incomplete ownership and false-clean zero hit

**Resolved at design-contract level; independent source completeness remains challenging.** The revised preflight requires exact registries and original handler identities for **all** authored SingleRay sources, the sole Glass, and **all** detectors. Each source must demonstrably start once and return a valid emission; all Glass incidents must be captured by the owning hook with same-run meter checks. A zero-hit trace with a missing source/start, replaced detector/interface handler or bypassed hook must **not** be clean. The design explicitly cautions that meters generated from the same wrapper are *not independent confirmation*. It preserves original ray and `newRays` return identities and discourages inferred parentage.

**Residual prerequisite:** hostile tests must independently inject missing, duplicated, bypassed and replaced starts/handlers, including zero-hit/missing-start and silent detector bypass. The final implementation must explain its non-circular registration and direct-emission evidence; design language alone does not establish reliable coverage.

## Exact SHA / CI / negative history

GitHub commit comparison confirms **one commit ahead**, one changed file: `docs/NATIVE-FINITE-FORWARD-QUALIFICATION-PROPOSAL.md`, **+60/−22**. The revised source head remains a **draft**, unmerged PR. All **11 first-page PR-triggered workflow summaries returned for this exact commit** reported `completed/success`, including unified workflow [43757031446](https://github.com/physicsvigilante/opticsim/actions/runs/43757031446). This review inspected their **reported summaries**, **not** downloaded logs, performed tests or rehashed ZIP artifacts. No fresh native, Node, independent exact-binary64 script or Chrome run was executed here.

Earlier v1 research workflow [43753292106](https://github.com/physicsvigilante/opticsim/actions/runs/43753292106) is reported by the prior review as 11/11 green, 750 Node passes and 64 native executions. This is *prior report evidence*, not independently rerun for this v2 review. Preserve the **first three FAILED** shadow CI attempts [43752308258](https://github.com/physicsvigilante/opticsim/actions/runs/43752308258), [43752585277](https://github.com/physicsvigilante/opticsim/actions/runs/43752585277), [43752839859](https://github.com/physicsvigilante/opticsim/actions/runs/43752839859) and the prior review's original counterexamples unchanged. Their cross-run parity failures and observed variability have not been erased by later green CI. This v2 diff contains **no executable implementation** of the new claimed protections.

## Separate scope judgments

| Dimension | Judgment | Basis |
|---|---|---|
| Source interpretation fidelity | Not assessed for new source problems | Only numerical reliability design; no new textbook-source interpretation |
| Physical/numerical correctness | **Design contract pass; actual qualification unknown** | Exact represented dyadic intersection and native-point agreement are appropriate necessary tests; validated bounds still missing |
| Native simulation and observable coverage | **Design contract pass; implementation unknown** | Complete-source/Glass/detector ownership and future publication matrix specified, not implemented |
| Evidence integrity and provenance | Pass for revision traceability; independent experimental verification not done | Pinned SHA, exact markdown-only change, prior failures preserved, current workflow summaries checked |
| Teacher-facing usefulness | Conditional / untested | Diagnostic-first warnings can avoid overstating trust; no UI/teacher evaluation |
| Textbook-answer completeness | Not applicable | Not a textbook-answer engine review |

## Release advice

**PASS means the B1–B5 *revised pre-implementation design* is coherent enough to be considered by the owner; it is not a permission to ship.** Before a separately approved Stage-1 implementation: prove owner/hook coverage, numerical uncertainty handling, honest advisory and no-request UI, same-run delegation identity, A→B→A run epochs, hostile 128/129/zero-hit cases, accepted source/detector/Fresnel coverage and bounded browser resource costs. Require exact-head implementation-level R2 review and explicit separate owner authorization. Future **Stage 2 mandatory measurement withholding** needs its own policy decision and independently reviewed evidence/publication gate; do not infer consent from this design pass.

**Do not merge Opticsim PR #88, modify `conductor_sim`, rewrite review-01, or relabel old failed CI as passing.**