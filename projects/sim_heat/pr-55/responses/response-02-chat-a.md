# SIM_HEAT PR55 — Chat A disposition of independent review-02/03/04 and corrected R2

Recorded 2026-11-18. This is the implementer's disposition, **not** an independent reviewer-authored report, a CI waiver, or authorization for source merge, deployment, OpenModelica execution or frozen-reference regeneration.

## Which independent report actually evaluated which source?

The central review directory contains **four separate, immutable Chat B reports**. A later publication found earlier filenames already occupied; the protocol requires appending a new file instead of overwriting another review.

| Independent report | Actual inspected source | Verdict and use |
|---|---|---|
| [review-01](../reviews/review-01-chat-b.md) | First HEAD `0b15c02e5c3c60af32224e0ec5f29a2920927d5a`, tree `1be95f7dc60bd729d691e437c06f7914f0e045e4` | **CHANGES REQUESTED** (F-01/F-02 major, F-03 minor); still valid for OLD source |
| [review-02](../reviews/review-02-chat-b.md) | Same first HEAD/tree | **CHANGES REQUESTED**; did not evaluate corrective successor |
| [review-03](../reviews/review-03-chat-b.md) | Same first HEAD/tree | **CHANGES REQUESTED**; did not evaluate corrective successor |
| [review-04](../reviews/review-04-chat-b.md) | **Corrected HEAD `1383a06d20422182cdae643337d6ddbdd6fcc5ec`**, tree **`9d1216afcd3f6ba5978a6e4cf0fa79ca69ad5c9d`** | **SCOPED PASS** for F-01, F-02, F-03 **ONLY**; **NOT MERGE READY** because CI-GATE-01 remains |

This accepted mapping is based on the **inside of each report**, the exact live Git commit/tree, and the original review-01 defect evidence—not on filenames or chronology alone. The old reports are **not** retroactively upgraded. All four are preserved as reviewer-authored original files.

**Developer disposition:** ACCEPT review-04's narrowly supported pass on the corrected source. Do not request another identical source-preview physics review of this unchanged corrected head. Retain the CI-GATE-01 blocker as its own workflow/merge readiness decision.

## What the correction demonstrably resolves

- **F-01 selection identity:** separate typed `component:<id>` / `node:<id>` options, graph click, pointer and Enter/Space dispatch. A real scratch study admitted by unchanged H1 permits a rod named `node_0` while a logical node is also `node_0`; the two now inspect their own authored physical source facts without narrowing valid names. Chat B personally executed 14 V8 display-validator probes and inspected **hosted** real Python H1/Chromium checks (not personally rerun).
- **F-02 component and model provenance:** original component records in `componentProvenance`, separate from numeric slot attribution; `@model` assumptions visible; original targets/kinds/locators/notes/repeats retained; no fabricated `source_given` scalar facts. Refusal clears assumptions. Chat B checked source and hosted admitted-model tests and screenshots; did not personally run the H1 Python loader.
- **F-03 imported display-schema:** steady-with-bodies and unsupported `native_qualified` provenance kind rejected across scopes; forged computed/public/native statuses remain refused. These are **untrusted JSON display-consistency** checks, not origin authentication or physics solving.
- The independent report explicitly preserves limits: no native TEACH_SPLIT3 readings, no independently checked numerical trajectories, no teacher or textbook qualification.

## Evidence, preservation, and outstanding red CI

Live [PR55](https://github.com/physicsvigilante/sim_heat/pull/55) remains draft/unmerged at corrected head `1383a06d20422182cdae643337d6ddbdd6fcc5ec`, tree `9d1216afcd3f6ba5978a6e4cf0fa79ca69ad5c9d`, base `0278b79b4da1c3196edca7903189713e0482f3f6`. Exactly **10 modified files in the original 14 additions** from old HEAD, no changed original physics, numeric source, native runner, six diagnostic bundles/catalog/comparison, C1 or PR54.

Dedicated corrected source preview [push 44272584312](https://github.com/physicsvigilante/sim_heat/actions/runs/44272584312) SUCCESS; [PR 44272593014](https://github.com/physicsvigilante/sim_heat/actions/runs/44272593014) SUCCESS; [audit-core 44272592956](https://github.com/physicsvigilante/sim_heat/actions/runs/44272592956) SUCCESS. Source-specific suites: **281 PASS, one existing optional unittest SKIP**, six original diagnostic archive bundle replays **BYTE_IDENTICAL** and `nativeExecutedByReplay=false`, D2/D2_K2 comparison unchanged, actual HTTP desktop/mobile source-preview collision/provenance/refusal/race browser smoke PASS. Artifact [14413740683](https://github.com/physicsvigilante/sim_heat/actions/runs/44272584312/artifacts/14413740683): 8,339,309 bytes, SHA256 `b6289d0b729706f52065b230b1f62b7a6f76252adb49279f34fd2ecb24e3e078`, 46 unique CRC-valid members. Locally blocked browser navigation is not claimed as a personal HTTP PASS.

**CI-GATE-01 remains unresolved:** [product-entry PR CI 44272592968](https://github.com/physicsvigilante/sim_heat/actions/runs/44272592968), job `134692657687`, **FAILED** before testing because the product-only `git diff --exit-code 4162c3... HEAD -- h1 experiments qualification viewer` guard refused legitimate H1/viewer source-preview additions. `tests/**` in that workflow's trigger inadvertently included the source-preview tests. Baseline job `134692657797` passed. The reviewer could not certify complete main-branch protection settings (GitHub protection endpoint was unavailable); the connected tool likewise returned HTTP 403 for detailed branch protection while public ruleset list was empty. **No blanket statement that all checks passed or red CI was waived.**

The bounded follow-up is a **separate prospective CI applicability correction**: restrict product-entry workflow triggers to its owned product-document and product-entry tests, while retaining strict protected-source diff checks **for actual product-only PRs** relative to their own base. Run the normal tests and source-archive browser replay on that new workflow commit, and obtain risk-proportionate independent assessment. Preserve existing CI run 44272592968 as failed historical evidence. Do not alter the scoped approved PR55 source-preview head just to make the older workflow green.

## Current stop and next gates

PR55 and separate [PR54](https://github.com/physicsvigilante/sim_heat/pull/54) both remain **draft, unmerged**. No new source-preview R2 review needed on unchanged corrected SHA; CI-GATE-01 still requires separately recorded applicability/required-check disposition and, if appropriate, a narrow CI fix before owner considers integration. Owner approval must be explicit for any future merge. No OpenModelica installation/version query/build/launch, native runner, frozen/adopted reference regeneration, historic C1 branch integration, deployment, diagnostic qualification promotion or invented native observation occurred in this disposition.
