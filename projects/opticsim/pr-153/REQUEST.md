# Opticsim PR #153 — independent R2 review request: complete native zero-crossing truthfulness

**NEW SOURCE SHA / DO NOT MERGE.** Prior independent [PR #151 R1 review](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-151/reviews/review-01-chat-b.md) returned **CHANGES REQUESTED, P1**: a fresh complete native detector result of zero actual crossings was misreported as unavailable evidence. This targeted correction is a child of that *frozen* source. Do not retroactively amend the R1 review or infer production release authority.

## Exact source and dependency

- [Draft PR #153](https://github.com/physicsvigilante/opticsim/pull/153), HEAD **`1107014449ac9fb89fce9bdaa93a44052d664b09`**, source Git tree **`3c9eae288f89b9882aa599c36b7d925f6b6d5331`**.
- True base: independently reviewed but **CHANGES REQUESTED** PR #151 HEAD `e078f1208b40514ed7d5f853b1c7520e36341431`, which is a child of reviewed but held PR #150 HEAD `0fb738f69b3257113c73dbf9d1f2917037daa5cc`.
- Temporary [CI-only PR #154](https://github.com/physicsvigilante/opticsim/pull/154) targets production main `d3509e82fb65d81aabe336666851f8f2962623f4`, with synthetic merge **`1f68493d432b7c97f89f2371554404fcc08fd0cb`**. Verify its *actual* Git tree **`3c9eae288f89b9882aa599c36b7d925f6b6d5331`** is identical to the corrected source Git tree and parents are [main, exact HEAD]. The temporary PR is for CI only and must close **unmerged** once evidence is captured.
- Only three changed files versus #151: `scripts/jee-observer-native-witness.mjs`, `test/jee-observer-native-witness-v1.test.mjs`, `docs/JEE-OBSERVER-NATIVE-WITNESS-V1.md`. No edit of the PhyDemo solver, canonical scene schema, adapter, prior independently reviewed parent source, or production main.

## Original P1, corrected semantics

The already existing `evaluateObservables` contract treats a completed native `detector-crossings = 0` as an **available measured zero** and `detector-hit-events = []` as a **complete, count-matched available empty hit list**. If the emitted ray never reached the planar interface, `interface-interactions = 0` is available and `interface-first-event` is legitimately **unavailable**; its absence is not evidence of incomplete tracing. The original #151 witness required one crossing/hit and an available first interface event before classifying the result and mislabeled those genuine complete negatives `native-evidence-unavailable`.

The correction adds **`native-observed-no-crossing`** for precisely a **completed / execution-passed / fresh scene SHA, exactly ONE emitted native ray, available actual detector crossing count = 0, complete count-matched empty native hit-event list**, valid native method identifiers, and valid interface-observation consistency. Two admission cases must qualify:

1. Exactly one native planar interface interaction, a genuine first event with stated media indices, and zero detector crossings.
2. Exactly ZERO native interface interactions, available interaction count zero, **no first event** (proper status `unavailable`, value null), and zero detector crossings.

The result has native `completed`, a specific **`MEASURED_ZERO_DETECTOR_CROSSINGS`** reason, explicit actual detector crossing count zero, a *null* accepted detector hit and incoming direction, null positional error, false arrival, and a warning that **one finite detector missing a sampled ray is not proof of invisibility, a physical shadow, or no light elsewhere**. This is a successful **measured negative** (CLI exit code 0), not a verified positive arrival. The source must not promote zero emitted rays, inconsistent hit count/list, contradictory first-event provenance, stale hash, incomplete run, missing methods, unqualified native evidence or nonfinite values to this status.

Positive `verified-sampled-arrival` requirements and exact measured detector hit/direction/first-event-angle comparison must remain unchanged. New nonblocking result-clarity correction also reports `NATIVE_FIRST_EVENT_ANGLE_MISMATCH` for an angle-only failure instead of incorrectly blaming user-chosen positional/directional tolerances, with success withheld.

## Tests and provenance (two different kinds of evidence)

1. **Explicitly SYNTHETIC complete, hash-matched negative summaries**, created via the existing test-only executor injection, exercise the witness's new *classification* logic with one native interface event vs zero native interactions/first event unavailable. This injection is NOT a genuine native miss, and must not be claimed as one. Tests also inject zero-emitted, inconsistent hit list, contradictory first event, and angle-only disagreement.
2. **Separate genuine pinned PhyDemo native controls** intentionally alter source heading in fully authored canonical v5 scenes away from the analytical predicted ray: (a) 30° traverses the plane and misses finite detector, (b) 180° misses both plane and detector. Those runs should independently prove that complete native zero crossings and empty detector hits are available in the ordinary observer contract, both with native first event and without. Because the physical scene differs from the original proposed direction, the test must NOT attribute this separate native miss to the original observer-position query.
3. Preexisting true native positive S=(-60,0) → O=(100,40), index 1.5→1, Fresnel-off example must still produce a real native detector hit at (100,40), complete event evidence and Fresnel warning; stale/incomplete, analysis-unqualified, detector-refused, and CLI evidence tests must still pass.

The old [PR #151 builder CI](https://github.com/physicsvigilante/opticsim/actions/runs/44305042852) was 809/809 Node tests, 11/11 workflows, but did not cover this critical zero measurement. Fresh exact-head CI on #154 is separately required; inspect real run/job logs, not only badges, and keep the distinction between builder native executions and reviewer-independent calculations. No claim about a new PhyDemo or mathematical optics improvement is made by this child.

## R2 reviewer tasks

Independently inspect the three changed files and unchanged `src/observables.js`, `src/native-observations.js`, native detector adapter and canonical scene freshness gates. Confirm the new measured-zero classification accepts both one-transmission/no-detector and zero-interface-interaction/no-detector cases; rejects all inconsistent/missing readings; preserves positive arrival checks, warnings and truthful error codes. Review exact source and CI synthetic merge Git identities; verify completed workflows and native-miss evidence logs. Think through whether a full-Fresnel reflected branch, detector endpoint ambiguity or a genuinely zero emitted ray can be misclassified. Assess whether status `native-observed-no-crossing` and exit code 0 are appropriate for an otherwise successful measured negative (without claiming visibility/invisibility).

Publish an independent R2 report to **`projects/opticsim/pr-153/reviews/review-01-chat-b.md`** with exact SHA/tree, physically meaningful provenance, P0/P1/nonblocking findings and verdict **CLEARED FOR OWNER DECISION / CHANGES REQUESTED / INSUFFICIENT EVIDENCE**. **No source changes, PR merges, release approval, modification of the frozen #151 review, or silent inheritance from independently reviewed #150.** Production main and branch-protection issue #123 remain separate.


## Final exact-head CI verification — 18 November 2026

**All 11/11 standard GitHub Actions workflows now completed SUCCESS** for exact candidate head `1107014449ac9fb89fce9bdaa93a44052d664b09`, source/CI tree `3c9eae288f89b9882aa599c36b7d925f6b6d5331`. The optical composition workflow [run #44311430794](https://github.com/physicsvigilante/opticsim/actions/runs/44311430794), **attempt 2**, job `134829111931`, passed **814/814 Node tests**, genuine pinned native separate no-hit controls, opaque blocker Chrome tests, browser acceptance **27 checks / 15 screenshots** and hosted smoke **5 checks / 1 screenshot**, Chrome 157.0.8103.50. The first attempt passed 814/814 Node tests but failed later at an unrelated opaque blocker browser step with **`Chrome/Chromium unavailable; no browser validation performed`**. The builder reran **only that failed job**, without changing source code or Git tree; its second attempt succeeded. Distinguish this infrastructure retry from a physics correction and do not silently erase the original failed attempt.

The [new exact-source optical log](https://github.com/physicsvigilante/opticsim/actions/runs/44311430794) includes `JEE_OBSERVER_NATIVE_ZERO_CLASSIFICATION` (explicitly **synthetic completed summary** used for code classification) and `JEE_OBSERVER_NATIVE_REAL_ZERO_CONTROLS` (two **separately authored actual native** scenes, one transmitted ray missing finite detector and one ray missing both plane and detector). These independent physical scenes are **not** native evidence for the original analytically proposed shooting ray.

**Reviewer must still independently inspect the final source/CI evidence. Green builder CI is not an independent physical verdict.**
