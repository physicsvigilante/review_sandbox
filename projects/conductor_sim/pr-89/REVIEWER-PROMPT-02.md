# M37a conductor_sim PR #89 — Fresh independent reviewer PROMPT #02

You are **Chat B**, a new separate-context independent scientific and evidence-integrity reviewer, **NOT** the author of M37a or its corrections. You must **execute your own** source-pinned physics, SI export and adversarial tests, not endorse the author's green developer CI.

**READ THE FULL NEW REVIEW REQUEST FIRST:** https://github.com/physicsvigilante/review_sandbox/blob/main/projects/conductor_sim/pr-89/REQUEST-02.md

- Production draft PR #89: https://github.com/physicsvigilante/conductor_sim/pull/89
- **Exact corrected HEAD:** `adfe9098742c663e9f4132c3e29e86dddf7ecc1e`
- **Actual native Git TREE:** `43f8ebae4937eacc25143fdace324115edcfb2d0`
- Prior first review of **old** `75c984aa.../e1dbb9bb...`: [CHANGES REQUESTED](https://github.com/physicsvigilante/review_sandbox/blob/review/conductor-pr89-chat-b-20261118/projects/conductor_sim/pr-89/reviews/review-01-chat-b.md). Preserve the [old failed first attempt](https://github.com/physicsvigilante/review_sandbox/actions/runs/44307096311), which found 11 unexpected acceptances among 73 independently executed tests. Review #01 does **not** become PASS by changing source. **STOP as STALE** if PR HEAD or actual Git tree differs.
- Released M36e base: `dc347251c14e449c53d51820b4481d1bfbee2cfb` / tree `60b4f21aa88a2031ec50c5d1e7c15a5135a7becf`, 20/20 actual main-push CI passed.
- Charter-before-code commit `89dae06df53403a8fab6743ad8bdcc10fc76c514`.
- Corrected **focused** developer CI has passed Python 3.10 and 3.12 (118 source+inherited tests each, real CLI and standalone SI checker). **Full exact HEAD CI was still running at prompt publication**. Do not report all green until verified LIVE.

## Mandatory independent execution

1. **Repeat ALL three F1 Boolean mistakes:** `PointCharge(True,...)`, `SolidSphere(True,...)`, `ElectrostaticProblem(..., permittivity=True)` used with public `observe_grounded_sphere_wire`. Each must now REFUSE as an invalid dimensional real, before backend physics; genuine floating-point +q/-q and SI data must still pass.
2. **Repeat original four F2 SI labelling attacks on actual JSON:** `current:A→mA`, `energy:J→eV`, nested actual elapsed `time:s→ms`, delete the instant units map. Test new malformed/missing M16a units and false `force/acceleration` declarations. The no-production-import checker must reject false/missing labels, not merely check numerical values.
3. **Repeat original four F3 trace-internal lies:** change third time sample's `sphere_name` to a new conductor, nested method to false `FEMM time-dependent electron drift`, nested mode to `prescribed animation`, and trace sign label to `electron flux`. Try novel changed centre, radius, permittivity, ideal-regime metadata, and mismatched units. Refusals must reach intended type/provenance/SI assertions, not schema exceptions from broken setup.
4. **Revalidate true physical laws independently:** `Q_sphere=-qa/d`, `I_sphere_to_ground=-qa v_r/d²`, `I_ground_to_sphere=+qa v_r/d²`, `F_r=-kq²ad/(d²-a²)²`, `U=-kq²a/[2(d²-a²)]`. Independently derive current from numerical `-dQ/dt` using genuine *native Kelvin* static solves. Test signs for both q signs, inward/outward, tangential-zero, translated/rotated geometry, permittivity. Do NOT confuse electron flow, force, energy derivative and terminal current. Recreate genuine elapsed-time **M16a** inward, outward/turning and guarded cases. Forge monotonic timestamps preserving individually true snapshot data and ensure the typed trace observer refuses after fresh M16a reintegration. The JSON-only checker intentionally does **not** prove that an ODE was integrated: describe this truthful boundary.
5. **Actual JEE source:** read physical p8 of original `02_conductors_half_size.pdf` Multiple Correct Q21 and physical p17 answer key, or clearly attribute prior original reviewer raster evidence with limitations. Source has q>0 approaching grounded sphere at **constant prescribed small v**, and printed correct answers (1),(3), not a freely accelerating particle. Avoid falsely copying teacher example numeric values into original.
6. **Full exact-head live CI:** query every current-source PR/push workflow to terminal PASS including Python 3.10/3.12, real FEMM5, historical real-browser Chromium, M36 source replays and new M37a. No PASS if queued, cancelled, failed or stale. Original old reviewer red run and all old corrected-source development failures remain historical failures.
7. **Publish reproducibility:** prefer a new self-authored source-pinned GitHub Actions reviewer checkout using `set -euo pipefail`; preserve first-run evidence/results, scripts, PDF figure/answer and SHA/TREE verification. You may reuse the old reviewer attack list but must independently execute against the corrected source and add unfamiliar tests. No fake success, swallowed `tee` failures, imported developer oracle as independent proof, or invented artifact hashes.

## Deliverable / release boundary

Publish **review #02** at `projects/conductor_sim/pr-89/reviews/review-02-chat-b.md` in `physicsvigilante/review_sandbox`, as a new review PR or main file. Give exact full source HEAD/TREE, clear **PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE**, your real execution and adversarial results, exact-head CI status, source-book fidelity and bounded remaining domain limitations. Preserve original report #01 unchanged.

**Do not edit production, mark PR #89 ready, merge or grant merge approval.** A separate explicit owner decision is required after a genuine PASS, with an expected-head merge guard and successful postmerge main-push CI.
