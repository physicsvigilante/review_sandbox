# M37a PR #89 — Targeted turning-event re-review #04 (not a new full physics audit)

This is a **minimal independent R4 task** to verify one repaired saved-JSON turning-event evidence contract. Prior R1/R2/R3 failed results remain historically valid for their older exact source commits. **The same independent reviewer may execute this**, retaining their own prior source-pinned harness and Kelvin reference. Do not repeat full physics/PDF investigation for unchanged code.

## Exact source gate

- Production PR: https://github.com/physicsvigilante/conductor_sim/pull/89 (expected DRAFT/UNMERGED; verify live).
- **Current corrected HEAD:** `d843a981a2b5ba4591f1c1afd169fd49bca7083f`.
- **Current native Git TREE:** `77afef9445a3ac65d228dfe029bb7c0d5b67ba10`.
- Prior R3 source: `630f6d320a1b4cb00bf7bb0780cd3deca4ec0f7e`, tree `796f319edf5829455e842d9bad63b770d17ff9fa`.
- Prior R3 **CHANGES REQUESTED:** https://github.com/physicsvigilante/review_sandbox/pull/8 ; [full report](https://github.com/physicsvigilante/review_sandbox/blob/review/conductor-pr89-r3-report-20261118/projects/conductor_sim/pr-89/reviews/review-03-chat-b.md).
- R3 first actual reviewer workflow **FAILURE retained:** https://github.com/physicsvigilante/review_sandbox/actions/runs/44320918820.
- Earlier R1/R2 independently reviewed Kelvin charge/current/force/energy, real M16a elapsed-time histories, F1/F2/F3, original workbook p8 Q21 prescribed constant speed with answer key (1),(3). These reviewed source implementations and original PDF are unchanged in the R3→R4 delta.
- **Changed files only:** `tools/m37a_ground_wire_reference.py`, `tests/test_m37a_grounded_wire_current.py`, `docs/m37a.md`; no public force model, M16a integrator, FEMM, viewer, existing physical code or original PDF modifications. Check live Git diff and exact native tree; STOP STALE if changed.

## Specific R3 blocker and correction

Reviewer R3 accepted a fabricated `turning-point` event **exactly at the first saved sample t=0**, even though its saved `velocity_m_s = -0.05`, a contradiction provable from the same exported document. The other **38** R3 hostile variants were refused and genuine duration, off-grid turning and surface-guard trajectories were accepted; the inherited independent R2 harness replayed **99/99 expected** results. Do not re-review these unchanged domains from scratch.

The current checker validates each saved turning event:
- A turning point must be **inside** the genuine sampled elapsed-time interval; initial/terminal non-bracketed invented turns are refused.
- If it coincides with an **interior** saved time, the recorded signed velocity must be numerically zero to a scale-aware local tolerance; a clearly nonzero velocity is refused.
- If it lies **between** samples, their signed velocities must demonstrate the physically permitted **outward→inward** reversal for a point charge under an attractive grounded-sphere image force, not merely matching an arbitrary event label.
- Event position must lie on the authored actual radial axis and be a local radial-distance maximum relative to its bracketing saved physical samples; multiple turning events are impossible in this single-sphere radial domain and are refused.
- It continues to preserve authentic off-grid M16a turning events, real surface-guard termination, strict SI labels and the F1/F2/F3/F4 prior refusals. It does NOT infer an exact off-grid root from adjacent points or claim that a JSON-only checker independently re-integrates the ODE.

Historical first developer commit `05f05103...` was **122 cases with one test matcher failure**: a fake event at an actual nonzero-velocity sample was rightly rejected by the earlier physical assertion rather than a later sign-bracketing assertion. Final test-only SHA `d843a981...` makes this probe genuinely off-grid while keeping both velocities outward. The first red developer evidence must remain red. Current exact-head dedicated M37a branch-push source workflow achieved **122/122 focused tests PASS on both Python 3.10 and Python 3.12**, plus example and independent standalone SI JSON checker. These are developer-controlled tests, NOT reviewer PASS.

## One new independent execution (bounded)

Execute a source-pinned checkout, assert exact HEAD and native TREE, original PDF blob unchanged and diff only in the three stated files; do not edit production. Use your *prior reviewer-owned R3 script*, update only source-head assertion, and run the new checks within the same source-pinned session. Do not hide failures with pipelines (`set -euo pipefail`).

Required:
1. Re-run the **actual R3 false turning point at time zero with `v=-0.05m/s`** from freshly produced valid native example JSON. It must now refuse with an intended physical turning-event reason.
2. Add unfamiliar cases: false interior sample turning with nonzero speed, false off-grid turn where sampled velocity does not reverse, sign reversal in physically forbidden inward→outward direction, duplicate turns, event position not a genuine radial maximum, fake exact-time event with mismatched position/velocity, malformed/bool event time. Require intended scientific refusals, not mere setup errors.
3. Preserve positive evidence: **genuine unchanged duration**, native M16a **off-grid turning** (with actual bracketing opposite velocities and authentic max radius), and **surface-guard** endpoint must all pass. Replay original F4 trio (false max energy drift, negative guard, impossible guard event) and sample F1–F3 refusals; the unchanged physical code does not require a new SI model derivation.
4. Independently check that `tools/m37a_ground_wire_reference.py` imports NO production physics and that JSON-consistent but arbitrarily *re-timed* trajectories remain a **documented proof ceiling**, not falsely asserted to be genuine ODE computation. Public typed M37a observer, unchanged here, already re-integrates M16a separately.
5. Verify all current **exact SHA** PR and branch-push workflows finish SUCCESS (expected 25 including actual FEMM 5, Python 3.10/3.12 and historical Chromium). **At prompt publication full CI was not yet complete**; prior-source 25/25 green is NOT current SHA release evidence. Do not issue PASS on pending, cancelled or failed runs.

## Published outcome

Publish `projects/conductor_sim/pr-89/reviews/review-04-chat-b.md` in `physicsvigilante/review_sandbox`, on main or separate review PR, attributed, with exact HEAD/TREE, actual first-run results and test refusal reasons, bounded verdict **PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE** and terminal exact-source CI. Do not overwrite R1/R2/R3 red records.

**DO NOT edit production PR, mark ready, or merge.** A genuine targeted independent PASS is sufficient for one **separate explicit owner merge decision**. Only owner approval permits an `expected_head_sha` guarded merge, exact reviewed Git-tree equality on main and all postmerge main-push CI SUCCESS. No additional redundant independent review is required after a PASS on an unchanged HEAD/TREE.
