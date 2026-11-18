# M37a / conductor_sim PR #89 — Targeted F4 independent re-review #03

**Purpose:** Close one independently reproduced scientific-export integrity blocker using the smallest possible review. This is NOT a fresh full physics review. **The same independent Chat B reviewer who found F4 may perform this targeted re-review**; a brand-new reviewer is not required. The physics implementation has not changed since the already executed R1/R2 source reviews.

## Exact identity

- Production draft PR: https://github.com/physicsvigilante/conductor_sim/pull/89
- **Exact corrected HEAD:** `630f6d320a1b4cb00bf7bb0780cd3deca4ec0f7e`
- **Actual Git tree:** `796f319edf5829455e842d9bad63b770d17ff9fa`
- Released base: `dc347251c14e449c53d51820b4481d1bfbee2cfb` / tree `60b4f21aa88a2031ec50c5d1e7c15a5135a7becf`, actual 20/20 postmerge main CI pass.
- Immediately prior independently reviewed source #02: `adfe9098742c663e9f4132c3e29e86dddf7ecc1e` / tree `43f8ebae4937eacc25143fdace324115edcfb2d0`; [R2 report: CHANGES REQUESTED](https://github.com/physicsvigilante/review_sandbox/blob/review/conductor-pr89-r2-20261118/projects/conductor_sim/pr-89/reviews/review-02-chat-b.md).
- Prior first independent report: [R1 CHANGES REQUESTED](https://github.com/physicsvigilante/review_sandbox/blob/review/conductor-pr89-chat-b-20261118/projects/conductor_sim/pr-89/reviews/review-01-chat-b.md).
- Original source-specific F1–F3 were fixed and **independently passed** on prior R2, with 99 actual executed cases (27 positive; 68 expected refusals; one documented JSON-only ODE proof limit; **three F4 unexpected acceptances**). Its original red [independent run #44315235077](https://github.com/physicsvigilante/review_sandbox/actions/runs/44315235077) is retained and must not be relabelled PASS.

## Narrow source-change trust boundary

The exact `adfe9098..630f6d3` source diff changes ONLY:
- `tools/m37a_ground_wire_reference.py` (stdlib, NO production physics imports);
- `tests/test_m37a_grounded_wire_current.py`;
- `docs/m37a.md`.

The actual Kelvin solver, public M37a observer, M16a integrator and native motion semantics, FEMM5, renderer and original PDFs are **unchanged**. Reviewer must verify that diff and native Git TREE rather than trusting this statement. There is **no need to redo a new blind physics derivation or rescan the original PDFs** if the source bytes and predecessor tests are confirmed unchanged; cite the independently executed R1/R2 physics and original-p8 constant-speed JEE source work. If other source changed, STOP STALE and require proper broader review.

## F4 repaired contract; mandatory new reviewer execution

R2 F4 found that the **offline JSON-only** SI checker accepted:
1. genuine `max_abs_energy_drift_j≈2.45e-20 J` falsified to `1e9 J`;
2. genuine positive `guard_m=1e-7 m` falsified to **`-0.3`**;
3. `termination=duration` with a forged structurally valid `surface-guard` event.

On this HEAD the checker now:
- requires numeric finite non-Boolean **positive** guard, and ensures all saved physical charge locations remain outside the declared conductor radius plus guard;
- checks reported **maximum absolute energy drift** against actual saved independently checked `energy_drift_j` samples without inventing a new near-cancellation SI reference;
- validates each event kind, numeric time/displacement, physical 3D position, authored-axis relationship, chronology, nonempty description and approach guard;
- refuses any guard event in a duration-complete history;
- requires exactly one *final* guard event matching the final actual saved sample for genuine `surface-guard` termination.

The first developer F4 source run `1668d0ce...` correctly showed **119 PASS / 1 FAILED TEST MATCHER**: the novel hostile event was rejected earlier for being physically geometrically inconsistent, not at the intended final-sample assertion. The final test-only commit `630f6d3...` makes the event geometrically consistent, while it still falsely claims the final event position, and requires **specifically the final guard event comparison** to reject it. Both red development runs must be preserved, not relabelled.

**Current exact-head focused M37a GitHub workflow:** both Python 3.10 and 3.12 passed **120 tests each**, including genuine turning/guarded M16a histories, corrupt summary/guard/event variants and genuine JSON/stdlib SI checker. These are author-controlled results, NOT independent re-review PASS.

The reviewer must do one **targeted** source-pinned execution (may adapt the existing self-authored `challenge_r2.py` and its independent oracle rather than rewriting 99 prior cases) with `set -euo pipefail`:
1. Assert exact HEAD and native TREE, production PR DRAFT/UNMERGED, the three changed files above, and no changes to physical solver / integration / original PDF.
2. Regenerate genuine CLI exported JSON and verify **true duration, real M16a turning, real M16a surface-guard** histories pass. Verify 0-JS? Not applicable: M37a is JSON-only, no new UI.
3. Rerun **all three original F4 hostile JSON mutations** with intended rejection reason (summary, negative guard, false terminal event) and novel cases for NaN/Boolean summary/guard, empty/non-list events, illegal event kind, out-of-range/negative event times, wrong/Boolean event displacement/position, missing final guard event, non-final/duplicate guard events and forged but internally geometry-consistent final guard position. Require refusals from actual scientific-consistency assertion, not missing files/errors.
4. Replay the **original reviewer-owned R2 suite** where practicable to show no F1–F3 regression and ongoing SI current/force/energy/typed-timeline consistency; unchanged independently reviewed native code need not undergo new broad original test authoring. A partial re-run is acceptable only if the reviewer explains exactly what was not reexecuted, checks the exact source diff, and uses the complete passed CI.
5. Review the static checker proof ceiling: a consistent hand-edited monotonic JSON timeline cannot be independently re-integrated by an import-free JSON checker; the public typed observer separately re-runs the qualified existing M16a integrator. **This is an honest documented limitation**; do not claim cryptographic authentication.
6. Verify all exact current-source **25 PR+push workflows** to complete SUCCESS: Python 3.10/3.12 full, dedicated M37a, real FEMM5 and historical Chromium/source. At request publication full CI was still running. **No PASS on pending/failed/cancelled jobs or older SHA.**

## Review process efficiency

For this bounded fix, **one fresh, targeted independent verification is sufficient** if it passes. Do not require a new full review for unchanged physical code, an additional separate reviewer, or new architecture review. Preserve old independent failures; a new PASS applies **only** to the current HEAD/TREE. A later edit of physics, evidence integrity, or export validation invalidates this review and must be risk-assessed; a pure comment change can be checked by exact diff with automated tests without reflexively restarting broad review.

## Review artifact and permission

Publish new `projects/conductor_sim/pr-89/reviews/review-03-chat-b.md` in `physicsvigilante/review_sandbox` on a dedicated review PR or main with **PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE**, exact HEAD/TREE, machine-readable first-attempt reviewer evidence and all F4 hostile reasons, confirmed full CI and scope limitations. Link predecessor evidence; do not rewrite history. Do NOT modify production PR #89 or mark ready/merge. A scientific review PASS requires a **separate explicit owner merge authorization** and expected-head merge to reviewed Git tree, followed by complete postmerge main-push CI.
