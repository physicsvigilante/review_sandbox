# Chat B — SIM_HEAT PR55 targeted independent R2 correction review 02

The **original independent [PR55 review-01](reviews/review-01-chat-b.md) remains CHANGES REQUESTED** at old head `0b15c02e5c3c60af32224e0ec5f29a2920927d5a`. Chat A has accepted F-01/F-02 (major) and F-03 (minor) and published a **new, not yet independently reviewed** correction on the SAME draft PR55.

**Review exactly** https://github.com/physicsvigilante/sim_heat/pull/55
- **Corrected HEAD:** `1383a06d20422182cdae643337d6ddbdd6fcc5ec`
- **Corrected tree:** `9d1216afcd3f6ba5978a6e4cf0fa79ca69ad5c9d`
- Immediate parent: original reviewed SHA `0b15c02e5c3c60af32224e0ec5f29a2920927d5a`.
- Base main remains `0278b79b4da1c3196edca7903189713e0482f3f6`.
- Exactly 10 modified files, all within original PR55's 14 added paths; no original existing physics/archives/references changed. PR54 remains separate/draft/unmerged.

**First read the full new central request:**
https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-55/CORRECTION-REQUEST-02.md

Independently challenge the exact original F-01 valid `node_0` component-versus-logical-node selection collision, including picker, real pointer and keyboard activation on a scratch model **actually admitted by H1**. Check F-02 original whole-component provenance retained distinctly from scalar/parameter records, `@model` assumptions visible and clearing on refusal, repeated records and old S1/parameter attributions preserved. Check F-03 steady-with-bodies and unsupported provenance-kind imports now refuse, without pretending that browser display-schema validation authenticates source or computes physics.

Review [exact-head push CI **44272584312**](https://github.com/physicsvigilante/sim_heat/actions/runs/44272584312), [artifact **14413740683**](https://github.com/physicsvigilante/sim_heat/actions/runs/44272584312/artifacts/14413740683), SHA-256 `b6289d0b729706f52065b230b1f62b7a6f76252adb49279f34fd2ecb24e3e078`, 8,339,309 bytes, 46 distinct CRC-valid ZIP entries. **281 unit passes, one optional skip, six original diagnostic bundle replays BYTE_IDENTICAL, existing/new Chromium actual HTTP PASS** are hosted claims to verify, not reviewer-personal executions. Check both import race orderings and source-only `not_computed` statuses.

**Do not ignore unrelated CI failure:** [product-entry workflow 44272592968](https://github.com/physicsvigilante/sim_heat/actions/runs/44272592968) has one genuine failing candidate job because its product-only protected-source diff gate rejects the source-preview H1 addition. Baseline passes; source-preview [PR run 44272593014](https://github.com/physicsvigilante/sim_heat/actions/runs/44272593014) and [audit-core 44272592956](https://github.com/physicsvigilante/sim_heat/actions/runs/44272592956) pass. Independently assess whether a separate CI applicability fix or required-status disposition is needed before any owner-approved merge. Do not describe the entire check suite as green.

Read source `AGENTS.md`, relevant H1 contracts, C1 freeze and central review protocol/policy/template. Attribute personally executed probes separately from hosted evidence, retain first failures, and give one verdict: **SCOPED PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE**. Consider source fidelity, numerical/physical correctness, native coverage, provenance integrity, teacher usefulness and textbook completeness individually.

**Commit your own NEW report**, never editing review-01:
`physicsvigilante/review_sandbox/projects/sim_heat/pr-55/reviews/review-02-chat-b.md`.

Stop before source merge, deployment, OpenModelica installation/query/build/launch, original/frozen reference regeneration, historic C1 merge or promotion of `diagnostic_only/nativeQualified=false` results. Neither a previous green CI nor your scoped verdict is merge permission.
