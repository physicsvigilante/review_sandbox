# M37a PR #89 — Fresh independent Chat B reviewer prompt #01

You are a **fresh separate-context independent scientific reviewer (Chat B)**, not the author of the M37a changes. You must execute original physics and provenance challenges. Do not accept the developer's old or current CI summary as your independent test.

**READ THE COMPLETE REVIEW REQUEST FIRST:**
https://github.com/physicsvigilante/review_sandbox/blob/main/projects/conductor_sim/pr-89/REQUEST-01.md

- **Target production PR (DRAFT / UNMERGED at packet publication):** https://github.com/physicsvigilante/conductor_sim/pull/89
- **EXACT HEAD:** `75c984aaae18e44997332e330ed3a519a7b6a8da`
- **Native Git TREE:** `e1dbb9bb673f4efc2950939d0c1e021697393d59`
- **M36e released base:** `dc347251c14e449c53d51820b4481d1bfbee2cfb`, native tree `60b4f21aa88a2031ec50c5d1e7c15a5135a7becf`, all **20/20 actual postmerge main-push checks SUCCESS**.
- **Pre-implementation charter:** `89dae06df53403a8fab6743ad8bdcc10fc76c514`.
- **CI at prompt publication:** final exact-head CI was **queued**, not yet complete; no green PASS is asserted.

## Scientific target

One external point charge `q != 0` at `d > a` outside one grounded **solid** conducting sphere. Original static Kelvin model and force-energy API are already qualified. M37a adds an ideal *net terminal current observable* from `Q_sphere=-qa/d`; the **signed current in the sphere→ground direction** is `I=-qa (dr/dt)/d²`. Independently verify the **factor 1/2** for induced *mechanical* energy and force law. Positive q moving inward implies **positive conventional sphere→ground current**, while charge changing sign reverses. Pure tangential motion has zero **net** wire current despite redistributed local sigma. Do not mistake this for a general circuit, FEMM time solver, or electron drift.

There are TWO genuinely different origins of velocity:
1. Teacher **prescribed instantaneous** 3D velocity: no simulated time path, no invented acceleration.
2. **Actual elapsed time** from already existing M16a RK4 radial solution. M37a now **re-integrates** M16a to refuse forged yet locally consistent monotonic histories. Deliberately test this attack; spoofed velocities, energies and fabricated events also must fail.

## Required independent execution

1. Confirm GitHub live exact HEAD and native `git rev-parse HEAD^{tree}`; **STOP and declare STALE if changed**. Confirm 8 changed files and no M16/FEMM/solver/viewer/PDF changes, draft/unmerged. Preserve original red CI history (109 passed/4 failed, then 112 passed/1 failed) as red evidence; they were corrected on subsequent commits, not transformed into PASS.
2. Execute a fresh source checkout and an **original reviewer-written Python/stdlib Kelvin oracle**, compare all signed source charge, induced conductor Q, force `-kq²ad/(d²-a²)²`, energy `-kq²a/[2(d²-a²)]` and `I=-qa v_r/d²`, include independent finite-difference `-dQ/dt` computed from actual **native** resampled physical equilibria. Test +q/-q, inward/outward, arbitrary 3D radial and tangential motion, translations and permittivity. Real SI numbers/units, not just regex strings.
3. Actually run a genuine M16a moving particle and a physical surface-guard termination. Verify every saved time, Q(t), I(t), velocity, force, induced U, energy drift and source ID. Try a **forgery of the intermediate time that remains strictly increasing while ALL instantaneous snapshot physics remain correct**; the final observer should refuse on re-integrated timeline. Try unfamiliar method/event/charge/centre/units forgery. Use **at least 12 targeted novel attack variants**; distinguish domain-specific refusal vs setup errors.
4. Independently validate actual JSON and standard-library checker `tools/m37a_ground_wire_reference.py`; ensure checker imports **no production physics**, rejects changed current/force/energy/source attribution, and remains honest that saved JSON alone cannot attest an ODE or reviewer provenance.
5. **Actually visually read the original `02_conductors_half_size.pdf` page 8, Multiple Correct Q21** and relevant figure/options/answer. This PDF is a workbook (NOT asserted official JEE past paper); original p8 source was marked PARTIAL in M36a. Check whether source gives a velocity or prescribed approach, asks actual time-dependent current or only qualitative direction and which of its options are supported. Teacher numeric q/a/r/v/m must never be assigned to original printed givens. No new whole-question JEE success without full evidence.
6. Query **all exact-head completed current-source** workflow runs (Python 3.10 and 3.12, real FEMM5, historic real Chromium, source replays, new M37a both PR and branch push). At prompt publication latest runs still queued: PASS forbidden while checks pending, cancelled, or failing. Red source workflows from older corrected development heads remain recorded.
7. Prefer self-authored dedicated GitHub Actions pinned checkout in `review_sandbox` when local network/execution unavailable, with `set -euo pipefail`, genuine first-attempt results, reproducible log/json and any original source PDF crop/screenshot. Do not edit production. Not a staged fake success.

## Required report

Publish `physicsvigilante/review_sandbox/projects/conductor_sim/pr-89/reviews/review-01-chat-b.md` on a review branch (PR) or main. Attribute yourself, exact HEAD/TREE, real test commands and results, actual p8 source inspection, independent physical SI references, hostile rejection reasons, full exact-head CI status and explicit remaining domain/educational limits. Verdict **PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE**.

**Never merge, mark ready or modify PR #89 production.** Even an independent PASS is NOT merge approval; Chat A must separately ask the owner, expected-head guard, compare actual Git tree on `main`, and require all actual postmerge workflows success. If production HEAD changes, your verdict does not transfer.
