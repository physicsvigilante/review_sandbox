# M37a PR #89 — R4 CONTINUATION on corrected HEAD (not a new full review)

This is an **update to the existing targeted independent R4 review**, NOT a fifth broad scientific review. The same Chat B reviewer may continue their own R4 source-pinned harness and issue **one final `review-04-chat-b.md`**. Preserve both original R4 failed workflow attempts and earlier R1/R2/R3 negative reports; never relabel a failure PASS. The final verdict is for the new exact SHA/TREE ONLY.

## Source integrity — STOP if stale

- Production draft PR: https://github.com/physicsvigilante/conductor_sim/pull/89
- **NEW corrected candidate HEAD:** `73d7daee9f31f6feee3e6305205aa28abc3e48af`
- **NEW native Git TREE:** `c728041ca5118013c6979d120c8805f31ee09fa0`
- Previous R4 tested HEAD `d843a981a2b5ba4591f1c1afd169fd49bca7083f`, TREE `77afef9445a3ac65d228dfe029bb7c0d5b67ba10`.
- Source diff from that R4 head changes **only** `tools/m37a_ground_wire_reference.py`, `tests/test_m37a_grounded_wire_current.py`, `docs/m37a.md` (one commit). NO Kelvin solver, native M37a current observer, M16a ODE, FEMM, existing viewers, frozen charter, or original PDF bytes changed.
- Released M36e base main: `dc347251c14e449c53d51820b4481d1bfbee2cfb`, reviewed tree `60b4f21aa88a2031ec50c5d1e7c15a5135a7becf`, 20/20 postmerge main CI success.

Verify live PR draft/unmerged, `git rev-parse HEAD`, `git rev-parse HEAD^{tree}`, diff and original source PDF identity. If any differs, STOP as STALE rather than applying old review verdict.

## Preserved R4 first-attempt scientific findings

R4 reviewer branch: https://github.com/physicsvigilante/review_sandbox/tree/review/conductor-pr89-r4-20261118

- [Failed R4 execution #44325743876](https://github.com/physicsvigilante/review_sandbox/actions/runs/44325743876)
- [Failed R4 execution #44326169759](https://github.com/physicsvigilante/review_sandbox/actions/runs/44326169759)
- The latest self-authored R4 challenge correctly accepted genuine duration, off-grid-turning and guarded M16a histories, refused all prior R3 F4 and F1–F3 attacks, and correctly refused the R3 initial-nonzero-velocity false turn. A new attack **`novel/exact-sample-zero-velocity-but-different-event-position`** was **UNEXPECTEDLY ACCEPTED**: turn event time was set equal to a genuine saved sample, its saved velocity/current/kinetic energy were made locally consistent with zero speed, BUT the event still falsely occupied a **different physical position** (original off-grid turning position). A continuous motion cannot have two locations at one time.
- Old R4 executions were truly FAILED; their source checkout, mutation inputs, raw logs and evidence are preserved on the reviewer branch. No independent PASS yet.

## Exact correction under review

At a turning-point event **coincident with an exact saved physical timestamp**, the independent stdlib JSON checker now additionally requires **event signed displacement and 3D physical position to match the stored particle state at that same time**, using explicit numeric checks. It still requires near-zero saved velocity, appropriate outward→inward bracketing, one turning point at most and a physically possible radial-distance maximum. It does not invent an ODE solution or exact off-grid turning time.

The author added a regression that independently generates a genuine M16a off-grid turn, serializes it to JSON, changes one saved sample's velocity/current/energy ledgers **consistently**, and falsely labels the old event position with that sample's time; the checker must reject the inconsistent displacement. A second variant binds displacement but leaves the false position, which must also reject. Genuine duration/turn/guard and earlier F1–F4 remain tested.

**Developer-only focused exact-HEAD workflow** completed **123 passed** each on Python 3.10 and 3.12 with the real teacher CLI/stdlib SI checker. This is NOT independent reviewer acceptance. **All 25 exact-HEAD PR+branch-push full workflows**, including real FEMM5, full Python, historical real Chromium and M36 source replays, must complete SUCCESS before a PASS. At this packet's creation some remained in progress, so current full CI is **not yet certified green**.

## Minimum independent verification — one execution, no architecture reset

Use your prior R4 `challenge_r4_turning.py` and the previous R2 replay script as *reviewer-owned* baselines. Update exact source-pin assertions only in your new reviewer-only execution code; do not modify production or overwrite the original first attempts. Use `set -euo pipefail` and retain first-run artifacts.

1. Execute the exact previously **unexpectedly accepted** `novel/exact-sample-zero-velocity-but-different-event-position` attack against freshly generated corrected source JSON. Demand a physical `ValueError` for inconsistent **same-timestamp** position/displacement; refuse merely returning a success object.
2. Repeat original R3 `t=0,v=-0.05m/s` false turning event and prior R4 attacks (wrong offgrid velocity bracket, fabricated same-sample nonzero velocity, duplicate turn, wrong radial maximum, malformed guard/event/energy metadata). Require proper scientific refusals, not incidental setup errors.
3. Add at least two unfamiliar exact-time cases: (a) forged event displacement inconsistent with saved displacement despite plausible 3D geometry, (b) event position inconsistent with saved vector at matching time despite a zero-velocity entry. Confirm genuine **off-grid turning**, genuine **duration** and genuine **surface guard** are still accepted.
4. Confirm stdlib-only export checker has no production physics imports; it validates internal numerical/metadata consistency, **not cryptographic authenticity or genuine ODE provenance**. Previously reviewed native typed observer re-integrates actual M16a (unchanged). An otherwise internally consistent falsified JSON time history remains a separately documented limited-proof case.
5. Query all current **25 exact HEAD** workflows until terminal conclusion. Prior old-head green 25/25 is not evidence for this HEAD. If any pending, failed or cancelled, don't issue PASS.

Original workbook p8 Multiple Correct Q21 and p17 answer key were already independently inspected on unchanged PDF bytes: positive charge approaches grounded sphere at **externally maintained constant small speed**; physical current direction/magnitude correspond to (1),(3). No new original printed numerical givens or full auto-graded original problem are claimed. No need to rescan unchanged PDF.

## Output

Publish a single attributed `physicsvigilante/review_sandbox/projects/conductor_sim/pr-89/reviews/review-04-chat-b.md` (new review PR or main) that **preserves both historical failed R4 runs** and includes the new exact SHA/TREE, new actual independent execution and PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE. Do not cite an older test as if executed on this head.

**NO production changes, no mark-ready, no merge.** A real independent R4 PASS on exact current HEAD plus completed exact-head CI is enough to request **one separate explicit owner merge approval**. After approval Chat A uses `expected_head_sha` and verifies reviewed Git TREE on main and all real postmerge main-push CI. No unnecessary new full reviewer.
