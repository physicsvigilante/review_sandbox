# EM Fields PR #17 — R2 independent-context review request

**Status:** exact-head author qualification passed; source PR is draft/unmerged; independent Chat B review not yet performed. Owner approved implementation, **not merge**. Prepared 2026-11-16 (Asia/Kolkata).

## Source identity and scope

- Project: emfeeld
- Source PR: https://github.com/physicsvigilante/emfeeld/pull/17
- Design PR #16 (separate, draft): https://github.com/physicsvigilante/emfeeld/pull/16
- Tracking issue: https://github.com/physicsvigilante/emfeeld/issues/15
- **Base SHA:** 8fe6331aefa252585b3b90f54b8ee7cbbac5e605 (qualified PR #14)
- **Approved candidate head:** 62121252c6526c53c29440dcd8f41b6109f70e04
- **Canonical source tree:** 339224f69e5c671dea83678cdb00845887ce27b4
- **CI merge-preview checkout:** 6d1c219e67cf300df7044f24690edf779270ac8f — verified identical Git tree
- **Risk:** R2, physical revision/identity and recorded numerical-evidence semantics
- **Reviewer destination:** projects/emfeeld/pr-17/reviews/review-01-chat-b.md — new, Chat B authored only

Read exact-head [AGENTS](https://github.com/physicsvigilante/emfeeld/blob/62121252c6526c53c29440dcd8f41b6109f70e04/AGENTS.md), [frozen Atomic V1 contract](https://github.com/physicsvigilante/emfeeld/blob/62121252c6526c53c29440dcd8f41b6109f70e04/docs/ATOMIC_SCENARIO_REVISIONS_V1.md), [physics contract](https://github.com/physicsvigilante/emfeeld/blob/62121252c6526c53c29440dcd8f41b6109f70e04/docs/PHYSICS.md), and [pinned base-to-head diff](https://github.com/physicsvigilante/emfeeld/compare/8fe6331aefa252585b3b90f54b8ee7cbbac5e605...62121252c6526c53c29440dcd8f41b6109f70e04).

Only production changes are new src/emfeeld/atomic_revisions.py and a narrow V3 dispatch in src/emfeeld/model_revisions.py. New tests/test_atomic_revisions.py, tools/qualify_atomic_revisions.py, verification/check_atomic_revision_runs.py, a CI step and the frozen design document are additive. No force laws, solver, integrator, energy policy, viewer, dependencies, numerical thresholds or historical test modules changed.

## Physical and evidence contract

One proposal-version-3 atomic_change may combine 2–4 **disjoint** V1 property or V2 source/particle insertion/removal operations against **one exact parent**. Members use stable physical target IDs, canonical old-value preconditions and explicit literal provenance; no two may target the same entity. All source/particle changes are assembled and final-snapshot validated in memory before **one** immutable accepted revision is published. Failed transactions retain rejection records, never accepted intermediate descendants. Existing local structural-write lock and complete accepted-history scan prevent ID reuse across siblings/ancestors. New composite no-op members reject with code no_op_member; historical V1 single-property no_op remains unchanged. Dangling surviving computed-input receipts, deleted-body investigations and stale presentation IDs must refuse rather than auto-repair. Every requested analysis recomputes fresh; construction admission is not numerical qualification.

**Exclusions:** no many-body forces, backreaction, simultaneous electric/gravity coupling, conductor behavior, shell/plane motion, time-dependent transitions, symbolic constraints, distributed transactions or general branch merging.

## Exact-head hosted CI and artifacts

- [Linux/Windows full clean-install qualification #43751887519](https://github.com/physicsvigilante/emfeeld/actions/runs/43751887519): **SUCCESS on Ubuntu 24.04 and Windows 2022**, each with **1,342 headless + 18 historical behavioral + 33 real-PyVista = 1,393 suite-member tests**. Historical obsolete whole-file freeze assertion remains explicitly deselected. 34 additional focused atomic test executions are the same definitions already counted in headless, not new tests.
- [Separate real-PyVista qualification #43751887558](https://github.com/physicsvigilante/emfeeld/actions/runs/43751887558): **SUCCESS**; 1,342 cumulative tests and real rendering/slider events.
- [Source snapshot #43751887494](https://github.com/physicsvigilante/emfeeld/actions/runs/43751887494): provenance artifact, not independent physics testing.
- Each OS completed frozen E1/G1/T1 native qualifications: **3 accepted atomic revisions, 6 complete baseline/final runs, 1 deliberate rejected old-presentation run, 36 static independently expressed field/potential checks, and 7 trajectories** checked against same-author separate ideal-source formulas and fixed-step RK4 (not Chat B independence).
- **Linux ZIP** artifact ID 14176882398; GitHub-published SHA256 932b1689c0d34bb121a1ccaa0539ea1c9db0988ef1ebb60ce88ff5cd11865880.
- **Windows ZIP** artifact ID 14177380152; GitHub-published SHA256 e93c60adb6ec39c7f7dd95bb0bcab57edcf65bee2181e616c8aaf2714a6d6ea6.

GitHub's job logs and artifact metadata were checked. **No separate downloaded ZIP byte-by-byte/CRC audit is claimed here.** Same tests on two OSs are not 2,786 distinct tests.

## Frozen same-author physical transfers

- E1: replace an electric line source in a negative line + axial uniform-field model; verify the new line/uniform field/potential, axial acceleration, separately RK4-checked transverse trajectory, stable remaining particle identity and explicit refusal of an old display naming the removed line.
- G1: change the mass of one prescribed fixed gravitational sphere and add a third independent body atomically; verify all three new trajectories against independent sphere/point expressions and RK4, not falsely treat old bodies' trajectories as unchanged under changed gravity.
- T1: in a static electric shell-plus-point arrangement, change two distinct source charges atomically; verify separate ideal-source fields/potentials with **no** shell motion claim.
- Negative cases include malformed/duplicate members, stale parent and identity reuse, bad physical inputs, last-source replacement, interrupted/colliding local store state, dependent receipts and transitive invalidation, removed particle observations, explicit reindexing, and a singular launch accepted as model construction but refused as numerical success.

## Historical attempts, limitations and review request

Preserve first failed CI logs: early [release #43750725799](https://github.com/physicsvigilante/emfeeld/actions/runs/43750725799) / [viewer #43750725784](https://github.com/physicsvigilante/emfeeld/actions/runs/43750725784) reported a test-status expectation mismatch (one failure, 1,336 other headless passes), not a proven physics bug. The V3-specific composite no-op evidence semantics were then clarified and retested; original V1 behavior was preserved. See [PR timeline](https://github.com/physicsvigilante/emfeeld/pull/17); do not erase original attempts.

Structural writer locking is **local**, not distributed/crash-safe ACID. Incomplete crashed state may require forensic inspection. SHA hashes are integrity checks, not proof of external authenticity. Results are not independent human physical adjudication or classroom teaching validation. Real offscreen rendering is not native Windows mouse interaction. No user Conda/store/run files changed; teaching evaluation remains paused.

**Chat B task:** independently challenge the pinned implementation and the evidence, including atomicity across late failures, parent/ID lifetime, dependency receipts, provenance, crash and concurrency boundaries, native mapping and E1/G1/T1 reference calculations. Run novel adversarial cases where possible; distinguish independent execution from reading Chat A outputs. Write a **new report** under projects/emfeeld/pr-17/reviews/review-01-chat-b.md following [protocol](../../../PROTOCOL.md) and [review template](../../../REVIEW-TEMPLATE.md), with exact SHA/tree, findings, and scoped **pass / changes-requested / insufficient-evidence**. Do not alter the source PR or imply merge permission. Owner can say “Review complete” after publication; source merge still requires **separate explicit approval**.
