# SIM_HEAT PR55 — corrected source-preview R2 scoped pass; CI applicability gate outstanding

**Current state:** `INDEPENDENT-REVIEW-04-CORRECTED-HEAD-SCOPED-PASS; CHAT-A-ACCEPTED; CI-GATE-01-UNRESOLVED; DRAFT-UNMERGED; NO-NATIVE-AUTHORIZATION`.

## Correct source/review mapping

[PR55](https://github.com/physicsvigilante/sim_heat/pull/55) remains **draft and unmerged**. Its **current corrected HEAD** is `1383a06d20422182cdae643337d6ddbdd6fcc5ec`, **tree `9d1216afcd3f6ba5978a6e4cf0fa79ca69ad5c9d`**, based on main `0278b79b4da1c3196edca7903189713e0482f3f6`. The original first head is `0b15c02e5c3c60af32224e0ec5f29a2920927d5a`, original tree `1be95f7dc60bd729d691e437c06f7914f0e045e4`.

- [Chat B review-01](reviews/review-01-chat-b.md), [review-02](reviews/review-02-chat-b.md), and [review-03](reviews/review-03-chat-b.md) independently each say **CHANGES REQUESTED** on the **OLD original HEAD**. They are preserved unchanged, not incorrectly treated as reviews of the correction.
- [Chat B review-04](reviews/review-04-chat-b.md), blob `5eaada4bbc2040a698ca50178267dbee065cdd99`, is the **actual independent correction-cycle-02 review of current HEAD/tree**. It returns **SCOPED PASS** for fixed F-01/F-02/F-03, **NOT MERGE READY** due CI-GATE-01. Its new filename is because `review-02-chat-b.md` and `review-03-chat-b.md` were already occupied; no previous reviewer file was overwritten.
- [Chat A disposition](responses/response-02-chat-a.md) accepts review-04's bounded pass, preserves all earlier negatives and records the unresolved CI issue. Previous [response-01](responses/response-01-chat-a.md) contains the original F-01/F-02/F-03 corrective work and exact-head hosted evidence.

**F-01:** typed component/node selection avoids valid `node_0` name collision. **F-02:** original whole-component and `@model` provenance retained distinctly and visible, without inventing scalar facts; refusal clears them. **F-03:** unsupported imported mode/component and provenance kind now refuse. R2 pass is source-only, not a new solver, native measurement, browser JSON origin authentication, textbook accuracy or teacher qualification.

## Successful source-specific evidence

[Exact-head source-preview push CI 44272584312](https://github.com/physicsvigilante/sim_heat/actions/runs/44272584312) and [PR CI 44272593014](https://github.com/physicsvigilante/sim_heat/actions/runs/44272593014) succeeded. [Audit-core 44272592956](https://github.com/physicsvigilante/sim_heat/actions/runs/44272592956) succeeded. Source-only suite: **281 passed and one optional unittest skipped**; six original D1/D2/DEV_BRIDGE/TEACH_RING4/S1/D2_K2 archived native diagnostic bundles replay **BYTE_IDENTICAL**, `nativeExecutedByReplay=false`; saved D2/D2_K2 comparison unchanged. Actual hosted HTTP Chromium original explorer plus new source-preview desktop/mobile identity/provenance/mode/refusal/race checks passed. [Artifact 14413740683](https://github.com/physicsvigilante/sim_heat/actions/runs/44272584312/artifacts/14413740683), 8,339,309 bytes, SHA-256 `b6289d0b729706f52065b230b1f62b7a6f76252adb49279f34fd2ecb24e3e078`, 46 CRC-valid unique files. Reviewer independently executed narrower V8 probes and inspected hosted CI; they did **not** personally rerun actual H1 Python admission or Chromium real HTTP. Preserve evidence attribution and original blocked-localhost attempts.

## CI-GATE-01 — genuine red unrelated workflow

[Product-entry PR workflow 44272592968](https://github.com/physicsvigilante/sim_heat/actions/runs/44272592968) **failed** in candidate job `134692657687` at PR synthetic merge ref. Its unchanged product-only guard compares original historical baseline `4162c3d...` to PR55 merge source over `h1 experiments qualification viewer`, correctly finds legitimate PR55 source-preview files and exits 1; `tests/**` broadly triggered the product-only workflow. Later candidate steps **skipped**, baseline candidate `134692657797` passed. This does **not** disprove the dedicated PR55 source-preview tests, but **the full check suite is not green**, and any required-status applicability needs explicit resolution. Branch protection endpoint was forbidden to the integration and public ruleset list was empty; cannot claim exhaustive branch-protection knowledge.

Next owner integration gate: bounded **separate prospective CI trigger/applicability correction** preserving product-only protected-source assertions for product changes, exact-head testing and risk-based review, plus explicit disposition of the old failed run. No review/source-merge owner approval has occurred.

## Preservation and next direction

All original six published cases remain `diagnostic_only` / `nativeQualified=false`, and TEACH_SPLIT3's four source-only requests remain `not_computed`. Historical C1 original 80× versus required 100× reference-precision failure, cross-host seal mismatch and nine uncomputed native public observations remain separate. PR54 stays [draft/unmerged](https://github.com/physicsvigilante/sim_heat/pull/54). No OpenModelica query/install/build/launch, frozen-reference regeneration, C1 historical stack merge, release, deployment or source merge authorized by this review or disposition.


## Prospective CI applicability follow-up — separate PR56

[Draft PR56](https://github.com/physicsvigilante/sim_heat/pull/56) is a **separate, unmerged R1 CI applicability candidate** for CI-GATE-01, not an amendment to corrected PR55's R2-reviewed source. PR56 HEAD `21eac064f98d76f12a31f03daf3bad3470cfbf96`, tree `0b789438b4aa1d0ecf6cbc6d38030eb540b97d48`, changed only `.github/workflows/product-entry-ci.yml` and a new `tests/test_product_ci_scope.py` with positive/negative trigger/guard controls. [Product CI 44278285853](https://github.com/physicsvigilante/sim_heat/actions/runs/44278285853) and [audit-core CI 44278285564](https://github.com/physicsvigilante/sim_heat/actions/runs/44278285564) **PASS**; candidate 260 tests passed/one optional skip, six original byte-identical archive replays, original comparison unchanged and hosted Chromium smoke PASS. The independent [PR56 review packet](../pr-56/REQUEST.md) is published; **review not yet complete, merge not approved**.

**Old PR55 product-entry run 44272592968 remains a genuine historical FAIL** and required-status applicability remains an explicit owner merge gate. Merging PR56 first can cause PR55's **other** dedicated source-preview CI's *fixed-old-base 14-path allowlist* to see PR56 files in the merge-ref source and refuse; that policy must be made current-base-relative in a separately checked, proportionate change if/when base main advances. Do not claim PR56 alone clears every PR55 gate or silently waive the old failure.
