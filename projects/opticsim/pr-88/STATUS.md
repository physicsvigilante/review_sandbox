# Opticsim PR #88 — independent R2 finite-hit numerical safeguard design review

**State: CHAT B REVIEW-01 `CHANGES-REQUESTED (DESIGN ONLY)`; revised design v2 published, exact-head 11/11 CI PASSED; TARGETED CHAT B REVIEW-02 PENDING.** No production implementation, new optical physics, mandatory v9 measurement gate, PhyDemo patch, public result change or merge authorized.

## Exact identities

- Source [draft PR #88](https://github.com/physicsvigilante/opticsim/pull/88): **open, draft, unmerged**. Original production/main base `fa158fc78da7a35b6a02eaed58c0cdbd4b699220`; pinned PhyDemo `811f508d2b070898c241a568b0c167dcb8645251`, Node 24.19.0.
- **Original design head independently reviewed:** `28c4aa94bbbf6b5a63a8bef433c80186e08a3d35`. The [Chat B review-01](reviews/review-01-chat-b.md) verdict for this immutable SHA is **CHANGES-REQUESTED**, with **three high-severity design blockers B1–B3 and two major B4–B5**. It is preserved unchanged.
- **NEW revised v2 proposal head:** `391047a5467f8e27f7b2162074900e8387945b9f`, [pinned proposal](https://github.com/physicsvigilante/opticsim/blob/391047a5467f8e27f7b2162074900e8387945b9f/docs/NATIVE-FINITE-FORWARD-QUALIFICATION-PROPOSAL.md). [v1→v2 exact diff](https://github.com/physicsvigilante/opticsim/compare/28c4aa94bbbf6b5a63a8bef433c80186e08a3d35...391047a5467f8e27f7b2162074900e8387945b9f): **one documentation file +60/−22 lines only**. The full PR remains exactly four research/docs/workflow files, with **no `src/`**, no numerical policy, no scene schema, no additional native or browser feature.
- **Revised-head existing CI:** all **11/11 GitHub Actions workflows passed**, including the original research-only shadow and **750/750 Node tests**. Since this was a **documentation-only revision**, passing CI does **not** demonstrate any new reported-point tolerance, production observer neutrality, qualified publication or browser implementation.

## Retained physical evidence and negatives

- Earlier [research PR #87](https://github.com/physicsvigilante/opticsim/pull/87) found actual finite-glass native represented-ray/finite-edge forward disagreements, including a completed v9 critical rotated case. This is a **native numeric representation consistency** issue, not proof of continuum physical truth or a universal critical-angle trajectory.
- The original PR #88 final head [unified CI 43753292106](https://github.com/physicsvigilante/opticsim/actions/runs/43753292106) passed **11/11 workflows, 750/750 Node tests**, 24 synthetic v9 scenes (48 initial native executions plus 16 alternating critical repeats), 55 finite-edge check events and one unknown. [Original raw artifact 14177321360](https://github.com/physicsvigilante/opticsim/actions/runs/43753292106/artifacts/14177321360), GitHub ZIP SHA256 `5a1ceda61fe4d33158049ccc8705f46d79dea8f51ee45739182a8715d2e896e1`, downloaded/rehash-checked by Chat A.
- The first three research CI attempts [43752308258](https://github.com/physicsvigilante/opticsim/actions/runs/43752308258), [43752585277](https://github.com/physicsvigilante/opticsim/actions/runs/43752585277) and [43752839859](https://github.com/physicsvigilante/opticsim/actions/runs/43752839859) **failed** under ungrounded separate-execution exact-critical parity. They were preserved. Multiple plain unwrapped native executions of **unchanged** critical scenes also varied, so no observer-induced causation **or** neutrality has been demonstrated.

## Developer v2 response (not independent acceptance)

[Developer response-01 — Chat A](responses/response-01-chat-a.md) proposes:

- **B1:** Replace unapproved mandatory first release with **Stage 0 research**, separately owner-approved **Stage 1 opt-in/noncertifying diagnostic**, and a wholly separate future **Stage 2 mandatory v9 measurement qualification** decision, only after observer-neutrality evidence and R2 review. No current canonical readouts change.
- **B2:** An independently computed binary64 ray/finite-edge intersection **must agree with the native-reported incident point** within a justified, independently tested **error/uncertainty envelope**. Computed as well as reported point vertex ambiguity matters. Missing bound, ill-conditioning or boundary → **unknown**, not checked.
- **B3:** A complete **counterfactual Stage 2-only** publication matrix for true native terminal status, separate audit/measurement qualification, native checker/CLI/raw reports, `summary.observations`, all trusted detector/interface readouts even without requests, result coverage, comparison, browser, qualified export/raw import and A→B→A run epoch. **No such production gate exists.**
- **B4/B5:** 128 is an **unvalidated diagnostic cap** pending 128/129 fault controls, complete 1–4 SingleRay / 0–2 detector / Fresnel-on/off native workloads, CPU/memory/Chrome measures, and exact preflight installation/invocation identity and missing-start/observer-bypass negatives.

These are **Chat A design corrections**, not proof that future code is safe, deterministic, physical or teacher-facing. No result should be upgraded to physics-qualified on this basis.

## Independent review handoff and hold

- [Targeted review-02 request](FOLLOW-UP-02.md) · [ready-to-paste second Chat B prompt](REVIEWER-PROMPT-02.md) · [original Chat B review-01](reviews/review-01-chat-b.md).
- **NO independent Chat B review-02 is yet recorded**. Its reserved append-only path is `projects/opticsim/pr-88/reviews/review-02-chat-b.md`. Chat A must not create or author this reviewer report.
- A second *design-only* pass would **not** approve Stage 1 production diagnostic, a Stage 2 mandatory rule, any source merge or deployment. Owner separately authorizes any implementation and a fresh full R2 implementation/code/evidence review at its exact head; a mandatory policy change requires a still later separate owner decision.

**Keep PR #88 and its disposable research workflow draft/unmerged. Production `main` remains unchanged.**
