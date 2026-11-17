# M36a PR #84 — independent source-interpretation review status

**2026-11-17 UTC:** Source PR is **DRAFT, OPEN, UNMERGED**. The independently scoped *coverage inventory* reviewer request is ready, but **source CI is still running**. No independent Chat B verdict or owner merge approval exists. Do not mark PASS/released based on green developer subsets.

- **PR:** https://github.com/physicsvigilante/conductor_sim/pull/84
- **Candidate HEAD:** `b6d7fccad26666100b172097b01738aedc8c9cf6`
- **Candidate native Git TREE:** `2d0e4197d8e4405ec28029bb3f124fc86fa7ec80`
- **Base released M35b:** `73e076cf7eaf7fefbae2b24afc1f54ff8f0b6fc6`, matching source tree `89363a917e3862d663d934501a1b5cd8a22a84c0`
- **Preimplementation charter-only commit:** `13eb3afde0efac049387d90a64eff44227f2acb4`
- **Reviewer packet:** [REQUEST.md](REQUEST.md) and [REVIEWER-PROMPT-02.md](REVIEWER-PROMPT-01.md)
- **Expected reviewer report:** `reviews/review-01-chat-b.md`, **not yet published**.

## Candidate source and scope

The original 29 M21a source-question anchors are included unchanged plus one earlier independently documented official 2021 Paper 1 Q9–10 two-charge apparatus, counted as one system. Docs-only support hypotheses: **24 scoped route / 3 partial / 3 unsupported**. These labels are not a completion rate. The 30 entries all have `case_replay_status=pending`, all first four educational/physics dimensions `not_evaluated`, and zero freshly executed source-specific native, numerical verification, viewer and original-PDF rereads. **No source-specific 30-problem simulation PASS has occurred here.**

- Frozen [M36a charter](https://github.com/physicsvigilante/conductor_sim/blob/b6d7fccad26666100b172097b01738aedc8c9cf6/docs/m36a_charter.md)
- [Current source matrix](https://github.com/physicsvigilante/conductor_sim/blob/b6d7fccad26666100b172097b01738aedc8c9cf6/docs/m36a_jee30_coverage.json)
- [Auditor](https://github.com/physicsvigilante/conductor_sim/blob/b6d7fccad26666100b172097b01738aedc8c9cf6/tools/m36a_jee30_audit.py)
- [Ten regression tests](https://github.com/physicsvigilante/conductor_sim/blob/b6d7fccad26666100b172097b01738aedc8c9cf6/tests/test_m36a_jee30_audit.py)

## Current developer status (not independent source certification)

A separate literal GitHub read of candidate JSON vs M21a verified all 29 IDs, source files, PDF pages, printed anchors, families, original M20c tiers and provenance fields matched exactly, and 30th ID was unique. The inherited PDF digests matched; no new PDF pages were visually examined. Matrix had exactly 24/3/3 labels, no invented PASS, and all new evidence counts zero.

At first packet publication, current source head triggered Python 3.10/3.12 and historical FEMM/Chromium workflows; some were still queued/in_progress. **CI was not fully green at publication.** Reviewer must fetch live statuses tied to exact source SHA before any no-blocker conclusion; the initial run-state chronology must not be retroactively overwritten. No new physics source, solver, FEMM mesh or viewer module was changed by this branch.

## Pending release gates

1. All actual HEAD-associated required CI workflows complete SUCCESS and targeted new ten tests genuinely execute on this source.
2. Fresh separate-context R2 review of scientific *coverage-meaning* and doc scope, including independent source anchor checks and adversarial negative probes, not a pretended 30-case simulation.
3. Explicit owner approval before expected-head merge. Check merged tree and every real main-push workflow afterward.
4. Full 30-case JEE native/independent/browser execution belongs to a subsequent scoped task and must not be implied by releasing a planning inventory.


## Superseding current-source #02 — NOT released, latest exact-head CI pending

Initial M36a HEAD `796d3f31d67dbeb5d82f57bf02512cf05242df64` / TREE `c79540e3c4807673bb6037ebbc9fad014144c706` had **8 failed tests** in the Python source-head run [#44155780188](https://github.com/physicsvigilante/conductor_sim/actions/runs/44155780188) because the author's new validator wrongly searched for “2021” inside the *printed anchor*; that year is recorded in the explicit `source_provenance` of the same frozen official 2021 case. Even adversarial negative tests failed early with that message, so their claimed rejection checks were **not** validated by the original run. No physics, PDF metadata, original 29 source anchors or route categories were altered. The initial failure is retained, not reclassified as PASS.

Correction `b6d7fccad26666100b172097b01738aedc8c9cf6` / TREE `2d0e4197d8e4405ec28029bb3f124fc86fa7ec80` validates the printer label and source provenance as distinct fields. New source-head Python matrix #44156813429 and full browser/FEMM CI have been triggered, **not yet verified green** at this status amendment. Updated full [review request](REQUEST.md) and reviewer [PROMPT #02](REVIEWER-PROMPT-02.md) supersede old #01. No separate reviewer report exists or owner merge approval.
