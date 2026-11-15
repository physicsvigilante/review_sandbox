# Opticsim PR #81 — R2 pre-implementation **design** review request

This packet requests an **independent, separate-ChatGPT-conversation critique** of a frozen **proposed evidence contract**, not code implementation review. No Chat B verdict exists yet. Do not conflate R2 design scrutiny with the mandatory future R2 review of actual implementation.

## Identity / freeze

- Project: `opticsim`; source: https://github.com/physicsvigilante/opticsim
- **Source proposal PR:** https://github.com/physicsvigilante/opticsim/pull/81 (**draft, unmerged**)
- **Exact proposal head:** `df783a3c2f5e51ad5edbacd35f6d82f1a02cfea7`
- **Exact production base:** `00e6211d6d40c0db8c62910f9e57b910b6aeb6f5`
- **Pinned proposal document:** https://github.com/physicsvigilante/opticsim/blob/df783a3c2f5e51ad5edbacd35f6d82f1a02cfea7/docs/NATIVE-RAY-PROVENANCE-PROPOSAL.md
- Source diff: https://github.com/physicsvigilante/opticsim/compare/00e6211d6d40c0db8c62910f9e57b910b6aeb6f5...df783a3c2f5e51ad5edbacd35f6d82f1a02cfea7 — exactly **one added 137-line documentation file**, zero `src/` or test/source-workflow edits
- Risk: **R2 physical/evidence critical** for the planned feature, **but current candidate contains docs only**. Outcome pertains only to design acceptability, not production behavior.
- Supported Node environment: **24.19.0**; pinned PhyDemo `811f508d2b070898c241a568b0c167dcb8645251`.
- Source proposal CI: https://github.com/physicsvigilante/opticsim/actions/runs/43730335002 (unified) and PR #81 Checks for the full workflow suite. CI status must be read live; it is not proof that unimplemented functionality works.

## Source-grounded feasibility evidence, not an implemented feature

1. [PR #79](https://github.com/physicsvigilante/opticsim/pull/79), head `ab0285940878eb30625605754e7a90847d574286`: test-only ray identity and directly returned native `newRays` child observation (plus frozen six-case transfer trial), not a public API; deliberately unmerged.
2. [PR #80](https://github.com/physicsvigilante/opticsim/pull/80), head `a40994a41f54ca45ac8fd8c3d7e6dcae17b736fb`: [supported Node CI 43729455968](https://github.com/physicsvigilante/opticsim/actions/runs/43729455968), 11/11 workflows passed. **12 native scenarios**: 8 narrow observed-identity runs; 4 withheld due to native Fresnel truncation, stop or intentionally missing source callback; a separate coincident-interface preflight refused. [Raw artifact #14166949457](https://github.com/physicsvigilante/opticsim/actions/runs/43729455968/artifacts/14166949457), GitHub ZIP SHA-256 `539e6bf53e898a79d76337cbe6ed3d3a74e27c67d5b8d010958a9353d48a7837`.
3. Current native measurement boundaries are in pinned production base `src/adapter.js`, `src/native-observations.js`, `src/observables.js`, `scripts/author-scene.mjs` and `docs/DETECTOR-HIT-EVENTS.md`. The proposed feature is **not** in any of these files. Research wrappers were test-only.

All prior research is **same-assistant developmental evidence**. Original textbook-image interpretation was not independently checked; user teaching effectiveness and physically correct general ray lineage remain unproven. A critical-angle native success at one scene is **not** evidence of reliable exact-critical angle physics across all media.

## Review target

The proposed new **opt-in** observable `detector-ray-provenance` would operate only on existing schema-v5 planar tracing with **one interface, one/two explicit single-ray sources, one/two passive detectors**. For a selected detector, it would return only actual crossing ray tokens and the complete observed **transitive direct parent graph** of those rays. Actual native emission callbacks establish roots; actual `onRayIncident.newRays` establish direct children. Same-object primary mutation keeps the token; `rayIndex` never provides source identity. No route/continuous illumination/image claim.

**Failure/unknown separation is central:** stopped/truncated/undefined/stale runs suppress output; absent source callback, unknown ray/parent, duplicate identities or inconsistent counts make provenance unavailable; caps of **64 observed ray objects per run** or **32 selected-detector hits** refuse full arrays rather than clipping; invalid geometry/scope is unavailable. A completed, qualified native miss can legitimately yield empty nodes/crossings. Other existing native observations retain their meaning.

## Priority R2 design-review questions

1. Does actual pinned PhyDemo source/incident callback identity justify roots and **immediate** parents? Identify realistic native cases in which children are reused, allocated without `newRays`, swallowed, duplicated, or otherwise evade identity accounting.
2. Could an unobserved emission with **no downstream incident callback** create a falsely complete empty attribution despite matching source counters? Challenge source-count and detector-count cross-checks.
3. Is the first-release **one-plane / 1–2 single rays / max 64 tokens / 32 selected hits** restriction coherent? Would mirror, additional detector, TIR, sampled fan or exact-critical numerical pathology invalidate the intended evidence meaning even inside this scope?
4. Could nested wrappers around the current `observeSourceSet` / `observeDetectorSet` / `observeInterfaceSet` change callbacks, outputs or sampling? What independent regressions and compare-native baseline must be mandatory?
5. Is `nodes` + `crossings` self-contained and safely limited to **observed parentage**, not accidentally presented as full path? Should statuses `unavailable` vs `suppressed` and native-warning policy differ?
6. Do event caps and graph-closure requirements prevent partial or orphan-node output without unbounded retention? Challenge overflow behavior and multi-detector consistency.
7. Identify the smallest **novel**, independently expressed physical/numerical and negative tests essential before *implementation* R2 sign-off. Avoid repeating existing tests merely to inflate coverage.

## Output and authority

Chat B should review **exact pinned PR #81 head**, source `AGENTS.md` at production base, central `PROTOCOL.md` and `REVIEW-RISK-POLICY.md`; inspect the existing source APIs as needed and not assume a new implementation exists. Distinguish conceptual defects/risks from bugs reproduced in production. If it can conduct new test-only trials, record exact changed test source/CI and keep the current candidate untouched; otherwise mark unknowns rather than inventing execution.

**Write a new review as Chat B**, not Chat A, at:

`projects/opticsim/pr-81/reviews/review-01-chat-b.md`

Use [REVIEW-TEMPLATE.md](../../../REVIEW-TEMPLATE.md); outcome `pass` / `changes-requested` / `insufficient-evidence` is explicitly **design-only**. A review PR is acceptable. Do not merge Opticsim PRs or modify source code. Any future implementation requires separate owner approval, CI, new exact implementation head and **new full R2 code review**.