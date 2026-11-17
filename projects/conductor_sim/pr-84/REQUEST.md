# M36a — Full independent interpretation/coverage-meaning review request (R2 source interpretation)

**Project:** conductor_sim · **source draft PR:** https://github.com/physicsvigilante/conductor_sim/pull/84

**Pinned source HEAD:** `b6d7fccad26666100b172097b01738aedc8c9cf6`
**Pinned native source Git TREE:** `2d0e4197d8e4405ec28029bb3f124fc86fa7ec80`
**Released M35b main parent:** `73e076cf7eaf7fefbae2b24afc1f54ff8f0b6fc6`
**Frozen charter-only commit:** `13eb3afde0efac049387d90a64eff44227f2acb4`

## Core question

Does the new **provisional** 30-case JEE capability inventory accurately and conservatively identify where `conductor_sim` already has a qualified *possible route*, where it has only a partial model, and where local physics must still be refused—without representing documentation or old examples as 30 freshly executed simulations? The PR changes no production numerical code; its R2 risk is **source interpretation, scientific scope and evidence semantics**, not new field-law implementation.

The historical [M21a cohort](https://github.com/physicsvigilante/conductor_sim/blob/b6d7fccad26666100b172097b01738aedc8c9cf6/docs/m21a_coverage.json) is 29 preselected original PDF question anchors, with 15 A/5 B/9 C tiered *as of M20c*. It cannot be presented as the current engine's progress. The candidate reuses all 29 identical IDs/pages/question/provenance, adds **one official JEE Advanced 2021 P1 Q9–10 two-charge apparatus** (not two trials), and provisionally triages **24 scoped route / 3 partial / 3 unsupported**.

These are **NOT** 24 physical simulation PASS findings. All 30 cases have `case_replay_status: pending`, all interpretation/physics/simulation/viewer axes are `not_evaluated`, and recorded new source-specific native/reviewer/viewer evidence counts are ZERO. Reviewer must refuse any inflated `24/30 solved` interpretation. Correctness of the triage claims is itself being reviewed.

## Read the pinned implementation and rules

- [Frozen charter](https://github.com/physicsvigilante/conductor_sim/blob/b6d7fccad26666100b172097b01738aedc8c9cf6/docs/m36a_charter.md), [current provisional source interpretation](https://github.com/physicsvigilante/conductor_sim/blob/b6d7fccad26666100b172097b01738aedc8c9cf6/docs/m36a.md), [candidate machine matrix](https://github.com/physicsvigilante/conductor_sim/blob/b6d7fccad26666100b172097b01738aedc8c9cf6/docs/m36a_jee30_coverage.json)
- [M36a offline auditor](https://github.com/physicsvigilante/conductor_sim/blob/b6d7fccad26666100b172097b01738aedc8c9cf6/tools/m36a_jee30_audit.py), [ten adversarial/positive tests](https://github.com/physicsvigilante/conductor_sim/blob/b6d7fccad26666100b172097b01738aedc8c9cf6/tests/test_m36a_jee30_audit.py)
- [M21a source audit](https://github.com/physicsvigilante/conductor_sim/blob/b6d7fccad26666100b172097b01738aedc8c9cf6/docs/m21a.md), [M21a source selection charter](https://github.com/physicsvigilante/conductor_sim/blob/b6d7fccad26666100b172097b01738aedc8c9cf6/docs/m21a_charter.md), [teaching evaluation contract](https://github.com/physicsvigilante/conductor_sim/blob/b6d7fccad26666100b172097b01738aedc8c9cf6/docs/evaluation_contract.md)
- Existing actual qualified physics: `docs/m21b.md`, `m21c.md`, `m21d.md`, `m21e.md`, `m23a.md`, `m24a.md`, `m24b.md`, `m27a.md`, `m27b.md` and the original source modules/tests; do not accept documentation claims without checking representative code.
- [Cross-project review protocol](https://github.com/physicsvigilante/review_sandbox/blob/main/PROTOCOL.md), [risk levels](https://github.com/physicsvigilante/review_sandbox/blob/main/REVIEW-RISK-POLICY.md), [review template](https://github.com/physicsvigilante/review_sandbox/blob/main/REVIEW-TEMPLATE.md).

## Independently verify and challenge

1. **Source integrity:** verify immutable HEAD/TREE vs GitHub, that the first 29 complete source/paper/question/legacy-tier identities are truly unchanged, 30th is a single anchored official 2021 two-charge apparatus rather than a double count, all existing document paths resolve, and old 29/2021 source attribution is accurately disclosed. Where possible inspect **original** PDF figures/pages rather than only relying on M21a prose; if unavailable, explicitly limit claims.
2. **Genuine physics qualification:** independently check at least three adversarial different source families: p2 Q19 one-sided metal sheet vs two-sided insulator, p5 Q47 static dipole energy not unspecified rotation, and p15 IIT-JEE 2012 proton `qE=mg` zero initial speed. Challenge p2 Q15 self-capacitance asymptotic vs close sphere mutual polarization; p12 Q40 two rings in a transverse field with no fictitious axial trajectory; official 2021 true V=0 circle; oil-drop missing transient data. Read enough actual code and checked source example to decide whether any `supported_scoped` route overclaims and should be `partial`. Preserve no conducting response for prescribed-charge rings.
3. **Refusal controls:** verify p11 Q28, p70 irregular cavity and p70 three cavities remain unsupported for *local 3D fields or surface-charge densities*, even though total induced charge by Gauss law is possible. Check p13 mixed wiring/geometry partial, p8 induced-current-time behavior partial.
4. **Audit adversaries:** independently execute the standalone CLI and tests in a literal pinned clean checkout where possible. Try tampering historical anchors, fake numerical PASS, incorrect source links, duplicate IDs, source digest and declared group counts. Confirm fail-closed rather than merely reading test names. Do not turn inventory validation into physics evidence.
5. **CI:** check all actual source-head triggered Python 3.10/3.12, real FEMM and Chromium jobs. Which tests were actually executed and which are skip-based? Preserve any first failure/cancel attempt. CI must complete before a favorable review; don't infer success from a queued job.

## Required report

Publish an ORIGINAL Chat B report at:
`projects/conductor_sim/pr-84/reviews/review-01-chat-b.md` to review_sandbox main, with PASS / CHANGES-REQUESTED / INSUFFICIENT-EVIDENCE, exact source SHA/tree, independent probes, findings/limitations, and **separate scorecards for documented qualified-route proposals versus actually executed JEE simulations**. Avoid claiming the full 30-source sample is JEE-representative or numerically solved. Review Chat B must not edit source production, mark ready or merge.

No reviewer result supersedes owner release approval; any source edit invalidates this exact-head pin and requires a fresh reviewer prompt and CI. The next *physics-validation* phase remains outstanding even if this bounded planning/inventory review passes.

## Corrected source revision #02 (initial first-source CI failure retained)

The first M36a source at `796d3f31d67dbeb5d82f57bf02512cf05242df64`/tree `c79540e3c4807673bb6037ebbc9fad014144c706` was **not** CI green. Its source-head [Python checks #44155780188](https://github.com/physicsvigilante/conductor_sim/actions/runs/44155780188) included eight failures within the ten new M36a audit tests. They traced to **one wrongly specified metadata rule** in `tools/m36a_jee30_audit.py`: it required the year '2021' in the *printed question label*, where the original label contains 'Paper 1 Questions 9–10', rather than checking the existing explicit source provenance containing year 2021. Consequent adversarial tests never reached their intended validation. Source PDF anchors, 29 historical identities, documented support map, physics APIs and 2021 question facts were NOT changed. The original failed test result remains part of the record.

Corrected candidate HEAD `b6d7fccad26666100b172097b01738aedc8c9cf6` / TREE `2d0e4197d8e4405ec28029bb3f124fc86fa7ec80` checks the question label for 'Questions 9' and the provenance for '2021' independently. All full Python/FEMM/Chromium current-head CI **must rerun**, and the reviewer must inspect actual result before PASS. The initial reviewer prompt #01 is now stale; **use PROMPT #02 only**. This is a developer metadata validation correction, not an independently verified 30-case native simulation.
