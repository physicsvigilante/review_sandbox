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

## New live source-pinned external execution — 2026-11-18 (review #02 gap addressed, formal verdict pending)

The latest independent review [#02](reviews/review-02-chat-b.md) was **INSUFFICIENT-EVIDENCE**: the reviewer's own original hostile Python and real PDF-tamper probe had NOT been executed, although it confirmed all **16/16 current-source PR/push CI jobs SUCCESS** and found no new demonstrable production defect. Review #01 remains CHANGES REQUESTED on superseded source; review #02 remains INSUFFICIENT-EVIDENCE (do not relabel either report).

Chat A published the **verbatim reviewer-authored 77-line probe** at [probes/review-02-original-hostile-controls.py](probes/review-02-original-hostile-controls.py) and actually executed it in a separate review_sandbox-only [GitHub Actions run #44238910525](https://github.com/physicsvigilante/review_sandbox/actions/runs/44238910525) (**COMPLETED/SUCCESS, attempt #1**), without changing `conductor_sim` source HEAD `527e6cee5f96a011729d2d0a668da9b688ab03d0` / native TREE `fff1c03417c857b6cce04156427e3eeaf9919a65`, source PR state, or any prior review.

The runner asserted the literal Git commit/tree, hashed both real source PDFs to the original frozen SHA-256, accepted the genuine inventory, and printed **9/9 expected hostile rejections**: three modified official 2021 source/grouping controls, three balanced 3D-refusal swaps, one matching forged JSON digest pair and two binary midpoint-bit-flip copies of the actual 20.7/9.1MB PDFs. It then printed `ALL NOVEL PYTHON CONTROLS PASSED`. Workflow jobs all successful. Evidence artifact ID `14398662234` with GitHub-reported ZIP SHA-256 `1b332b90dbf7e1ea39502ebea401c0183366d894b3fbdf87c194debd17745a0f` (ZIP **not** third-party rehashed). Detailed [Chat A response](responses/response-02-chat-a.md). This is execution by a GitHub-hosted runner of the original separate-context reviewer's script, **not** reviewer-interactive local execution or human scientific certification.

A new [narrow completion Prompt #04](REVIEWER-PROMPT-04.md) requests Chat B to independently verify the execution and publish **distinct `reviews/review-03-chat-b.md`** with scoped PASS / CHANGES-REQUESTED / INSUFFICIENT-EVIDENCE. This latest report does not yet exist at status writing. **Source PR #84 remains draft/unmerged and owner approval remains absent.** Separate verified actual JEE-30 original physics replays and browser evaluation: **0/30** for this planning artifact. The 24/3/3 triage remains provisional, not achieved simulation success.

## 2026-11-18 — M36a protected release verified, PR #84 merged

Owner explicitly approved proceeding after independently published Chat B [review #03](reviews/review-03-chat-b.md), which returned scoped **PASS** for exact source `527e6cee5f96a011729d2d0a668da9b688ab03d0` / Git tree `fff1c03417c857b6cce04156427e3eeaf9919a65`. All **16/16 premerge source-head workflows completed SUCCESS**, including Python 3.10/3.12, 97 actual FEMM 5 tests, complete 73-step Chromium historical workflow, and the separate reviewer-original hostile execution [#44238910525](https://github.com/physicsvigilante/review_sandbox/actions/runs/44238910525) that confirmed nine expected rejection controls and actual original PDF raw-byte hashes.

[Source PR #84](https://github.com/physicsvigilante/conductor_sim/pull/84) was marked ready and **successfully merged with `expected_head_sha` safeguard**. Actual merge commit [`4e5fd2044a171bc889edf626f2c7795e15d5188c`](https://github.com/physicsvigilante/conductor_sim/commit/4e5fd2044a171bc889edf626f2c7795e15d5188c) has parents released M35b `73e076cf7eaf7fefbae2b24afc1f54ff8f0b6fc6` and exact reviewed candidate `527e6cee5f96a011729d2d0a668da9b688ab03d0`; its **actual Git TREE is exactly `fff1c03417c857b6cce04156427e3eeaf9919a65`**. Remote `main` pointed to the actual merge commit when checked.

The actual postmerge **`main` push triggered 15 workflows and all 15 completed SUCCESS** at that exact merge commit, including Python, real FEMM, historical Chromium and all inherited source scientific checks. An extra workflow listed for the same source commit on an unrelated new development branch was explicitly excluded from the *main-push* denominator; this preserves correct release accounting. **M36a fully released** within its limited provisional source-anchored 30-apparatus inventory/evidence scope.

**No actual 30-apparatus original-question replay was newly certified by M36a.** Its historically frozen provisional 24 scoped capable / 3 partial / 3 unsupported documented routes remain *not a 24/30 solved score*. Actual source-JEE native/independent/browser replays are being developed separately in [M36b draft PR #85](https://github.com/physicsvigilante/conductor_sim/pull/85), without rewriting the M36a inventory or source PDFs. Prior review #01 changes-requested and #02 insufficient-evidence remain visible as original historical findings.
