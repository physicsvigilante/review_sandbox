# M36a PR #84 — independent source-interpretation review status

**2026-11-17 UTC:** Source PR is **DRAFT, OPEN, UNMERGED**. The independently scoped *coverage inventory* reviewer request is ready, but **source CI is still running**. No independent Chat B verdict or owner merge approval exists. Do not mark PASS/released based on green developer subsets.

- **PR:** https://github.com/physicsvigilante/conductor_sim/pull/84
- **Candidate HEAD:** `b6d7fccad26666100b172097b01738aedc8c9cf6`
- **Candidate native Git TREE:** `2d0e4197d8e4405ec28029bb3f124fc86fa7ec80`
- **Base released M35b:** `73e076cf7eaf7fefbae2b24afc1f54ff8f0b6fc6`, matching source tree `89363a917e3862d663d934501a1b5cd8a22a84c0`
- **Preimplementation charter-only commit:** `13eb3afde0efac049387d90a64eff44227f2acb4`
- **Reviewer packet:** [REQUEST.md](REQUEST.md) and [REVIEWER-PROMPT-02.md](REVIEWER-PROMPT-02.md)
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

## 2026-11-18 — Independent R2 review #01: CHANGES REQUESTED; corrections staged

The fresh [review #01](reviews/review-01-chat-b.md) independently reviewed source `b6d7fccad26666100b172097b01738aedc8c9cf6` / TREE `2d0e4197d8e4405ec28029bb3f124fc86fa7ec80` and returned **CHANGES REQUESTED**. Specific findings: (F-01) original full Chromium visualization run [#44156812874](https://github.com/physicsvigilante/conductor_sim/actions/runs/44156812874) was actually CANCELLED at the ten-minute limit with later steps skipped; (F-02) exact official 2021 source+paired-question identity was not pinned; (F-03) a balanced route-count swap could relabel three irregular local-3D refusals as supported; (F-04) stored PDF SHA strings were compared without hashing the actual PDF bytes; (F-05 minor) STATUS prompt hyperlink pointed to stale #01. Representative independent analytical checks did **not** demonstrate a source physics defect, but inventory-truth and CI gates were legitimately open. The reviewer did not independently execute its hostile mutation scenarios, which are now added as developer tests.

**Corrected source PR #84 remains DRAFT and UNMERGED. Current development HEAD `527e6cee5f96a011729d2d0a668da9b688ab03d0` / actual Git TREE `fff1c03417c857b6cce04156427e3eeaf9919a65`**. The new source commits:

- `a1e2415`: literal official-paper/source/question identity and explicit local-3D must-refuse IDs; streaming SHA256 verification of real checked-in PDFs against frozen M21a digests (also rejects two mutually altered JSON strings).
- `fe865149`: explicit `official_apparatus` with exact `Q9` and `Q10` membership for one 2021 Paper 1 apparatus.
- `a424a16b`: historical full Chromium job timeout raised from 10 to 25 minutes; **all existing viewer/source steps are retained**. This does not count the previously skipped steps as passed.
- `527e6cee`: first-class adversarial tests for source replacement, extra Q11 substitution, other paper/year provenance, false multicavity support despite preserved 24/3/3 totals, metadata-collusion, actual altered PDF bytes and retained browser steps.

**Source HEAD changed after review #01, so that verdict is stale for the correction.** Exact-head new Python/FEMM/Chromium CI is queued/in progress at the time of this status amendment. Do not call green before completion; do not claim independent R2 acceptance or release. A source-pinned **targeted review #02**, distinct from the historical first #01, must examine each correction and its current-head CI. A new immutable prompt #03 can be published when source CI is checked; earlier prompts #01 and #02 are stale to the corrected source. Owner approval, exact-head merge, reviewed Git tree equality and all real main-push workflows remain required. Physical original-question replays remain zero in M36a.

## Targeted Chat B handoff #03 published — 2026-11-18

**Authoritative correction source head:** `527e6cee5f96a011729d2d0a668da9b688ab03d0` / Git TREE `fff1c03417c857b6cce04156427e3eeaf9919a65`. The published separate-context review #01 on `b6d7fcc...` remains **CHANGES REQUESTED** and is NOT retroactively converted to PASS.

Updated independent targeted [REQUEST-03.md](REQUEST-03.md) and [REVIEWER-PROMPT-03.md](REVIEWER-PROMPT-03.md) are the ONLY current review packet. Intended independent finding file: `reviews/review-02-chat-b.md` (not published at packet issue). Reviewer must run original new hostile tests for F-02/F-03/F-04, and verify the genuinely completed full historical visualization workflow for F-01—not simply the longer timeout text. F-05 stale #02 pointer has been fixed. Owner merge approval remains absent.

Current-head workflows in GitHub were **12/16 successful and four still running** (full visualization, two Python workflows, dedicated real FEMM) when last sampled. These counts are dated observations, **not** a claim of current full green status; always requery. Source scope remains a provisional 24/3/3 documented-route matrix and ZERO new JEE source-specific simulation replays. Historical first-failed Python and source-b6d7 cancelled visualization must stay preserved in any new report.
