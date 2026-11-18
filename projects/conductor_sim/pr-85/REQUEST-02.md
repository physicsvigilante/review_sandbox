# M36b PR #85 — Targeted independent R2 scientific review #02: real source evidence integrity corrections

**Current source PR:** https://github.com/physicsvigilante/conductor_sim/pull/85 (**DRAFT / OPEN / UNMERGED**)

**EXACT corrected source HEAD:** `524a6e07f17cd8bf53eaeec543031f1ec7bbb9eb`

**Actual native Git TREE:** `c7c411d5602ada9db0f3b867c19ec4da6d317f6b`

**Released M36a main base:** `4e5fd2044a171bc889edf626f2c7795e15d5188c` (TREE `fff1c03417c857b6cce04156427e3eeaf9919a65`)

**Reviewed predecessor:** `5cfa02c2b22ad1d488778653d63f54b4f9a06d1d` / TREE `3db298498bdd30b701ced59d3952eb529e835add`, original [Chat B R2 review #01](reviews/review-01-chat-b.md) **CHANGES REQUESTED**. Report must remain preserved and must NOT be retroactively described as PASS.

**Charter-only commit frozen BEFORE implementation:** `6e3be20c83a26318b3b5147268e545a338fa71fb`.

The source is physically unchanged in its field laws, FEMM solver, ODE integrators, original JEE PDFs, and original M36a 30-case plan. The 7 source-selected apparatus and one honest local-3D refusal remain the same.

## Original findings and corrected paths — examine actual code, not summaries

Read original [review #01](reviews/review-01-chat-b.md) in full, especially its **five independently falsified records** from actual downloaded genuine JEE native JSON, along with the additional F04/F05 improvements. Inspect current exact-head [source replay](https://github.com/physicsvigilante/conductor_sim/blob/524a6e07f17cd8bf53eaeec543031f1ec7bbb9eb/tools/m36b_jee_replay.py), [source-free physics reference](https://github.com/physicsvigilante/conductor_sim/blob/524a6e07f17cd8bf53eaeec543031f1ec7bbb9eb/tools/m36b_jee_reference.py), [regression tests](https://github.com/physicsvigilante/conductor_sim/blob/524a6e07f17cd8bf53eaeec543031f1ec7bbb9eb/tests/test_m36b_jee_replays.py), [native teacher transfer](https://github.com/physicsvigilante/conductor_sim/blob/524a6e07f17cd8bf53eaeec543031f1ec7bbb9eb/tools/m36b_transfer.py), [strict separate teacher numerical reference](https://github.com/physicsvigilante/conductor_sim/blob/524a6e07f17cd8bf53eaeec543031f1ec7bbb9eb/tools/m36b_transfer_reference.py), [transfer tests](https://github.com/physicsvigilante/conductor_sim/blob/524a6e07f17cd8bf53eaeec543031f1ec7bbb9eb/tests/test_m36b_transfer.py), and [full M36b source-gated workflow](https://github.com/physicsvigilante/conductor_sim/blob/524a6e07f17cd8bf53eaeec543031f1ec7bbb9eb/.github/workflows/m36b-jee-source-replays.yml).

### F-01 — Stopped electron terminal state

- Previously accepted forged `kinetic_energy_j=1e-18 J` and `v_y=1000 m/s` with full-stop flag true. Corrected `reference_sheet` independently checks full 3D position and velocity, zero transverse components for actual invariant plane, `|v|<=1e-3 m/s`, and `K=.5 m |v|^2` with tight physically dimensioned tolerances. Check legitimate actual terminal event still passes without false refusal.
- **Fresh novel attacks**: change stopped-electron transverse z, full-stop flag, kinetic energy just above credible event tolerance, or physically impossible y/z position, not merely the developer's original parameter cases.

### F-02 — Early passive contact time/root

- Previous checker only required `0<t_hit<t_turn`. Corrected manifest exports the true separate teacher-launch source field, electron mass/charge, initial position/velocity and **full native terminal event** (time, world position, velocity, actual energy).
- Independent reference now computes stable **FIRST** positive quadratic root `2d/(|v0|+sqrt(v0^2-2ad))` and checks event's time, x/y/z root, signed velocity and kinetic energy. Deliberately forged `0.8*t_turn` before reversal must now fail. Do NOT claim an ideal detector is physical contact, collision, bounce, current or induced charge.
- Add own hostile false-before-turn root that is close but wrong, plus correct early terminal positive example.

### F-03 — True ring E and signed work ledger

- Previous checker trusted each saved axial Ex as its own expected value and only validated total work and zero upward-field contribution, not individual ring A/B terms. Corrected reference independently derives `E_x(A) = k Q_B (-d)/(R^2+d^2)^(3/2)`, `E_x(B)=k Q_A d/(R^2+d^2)^(3/2)`, and signed per-source work `q k Q_A(1/R-1/sqrt(R²+d²))`, `q k Q_B(1/sqrt(R²+d²)-1/R)`. It checks each term, their sum, the complete E vectors, and nonzero transverse +1N force while not depicting a fake free axial path. Independent original reference values Ex(A) ≈ +575203.3147 V/m, Ex(B) ≈ +287601.6574 V/m, W_A ≈ +1.198340239 J, W_B ≈ +2.396680478 J, total ≈ +3.595020717 J.
- Reviewer should forge *multiple* ledger entries which cancel in the aggregate, or flip axial E sign while preserving total work, and verify explicit rejection on actual current source.

### F-04 — Nontrivial disconnected? NO: true connected-sphere redistribution

- Retain the preregistered source p2 Q15 teacher realization (+2/+4 nC on radii .1/.2 m) already in equilibrium; its physical E1/E2=2 result remains valid. A **separate labelled teacher hypothetical variant of the SAME two named connected conductors** now starts with +5/+1 nC and must genuinely solve to +2/+4 nC and `-3/+3 nC` signed transfer, with strictly positive `ΔU ≈ .5 k [sum Q_initial²/R - sum Q_final²/R]`. Verify actual backend, actual source IDs/geometry, and no eighth JEE source case artificially added.
- A separate false transfer-energy/value should be rejected; changing initial body to nonqualified close/touching geometry should not be accepted by source backend. The 5% far-separation admission ratio is a policy, not a proven physical uncertainty guarantee.

### F-05 — Official 2021 physical source-mask geometry

- Corrected source record exports actual `source_masks` with `center_m`, `radius_m`, `kind`. The source runner invokes `validate_fixed_potential_map` on the **native sampled grid and contour** before detached export. Independent source-free checker compares masks to actual charge positions, 0.11 m illustrative display-only radius and `display-exclusion` type; count-only is no longer enough.
- Reviewer should move a mask centre, delete a mask, change its radius, or substitute a stale analytic circle unrelated to saved grid. Numeric contour agreement alone does not mathematically authenticate an arbitrary maliciously forged grid; describe actual trust boundary accurately.

## New real physical parameter transfers (separate from 7 JEE questions)

The developer additionally executed actual changed physical models of **three distinct families**, not static changes to labels. The inputs were inspired by the original reviewer but **code and CI execution remain developer authored**, not independently initiated by Chat B:
- Charged sheet electron **175 eV**, sigma **−3.4e−6 C/m²**, launch **1.1 mm**; genuine new M24a terminal reversal and independent first-order reference.
- Finite dipole **q=1.2 nC, d=6 cm, E=200 V/m, θ=65°**, genuine new finite-pair static dipole energy and torque.
- Charged particle with E+g, **m=2e−27 kg, q=1.4e−19 C, E=1.04375e−7 V/m, g=9.81 m/s², 17 ms**, genuine newly integrated full vector time samples.
- Additional actual far-separated conductor charge transfer as above. These **do not** increase the original seven-apparatus denominator or alter the original JEE source givens.

**Reviewer R2 transfer obligation:** independently author/run unfamiliar qualifying physical variants, preferably at least three genuinely different families with positive and adversarial cases, and separate physical analytic references rather than copying author tests. If actual separate-context code execution is unavailable, state precise limitation; do not falsely equate developer CI with independently authored science. A bounded re-review may test F01-F05 and these transfers, not redo the full inherited M36a audit.

## Developer CI and exact-source execution — distinguish roles

The source HEAD `524a6e07...` has a [separate review_sandbox source-pinned smoke #44250006598](https://github.com/physicsvigilante/review_sandbox/actions/runs/44250006598) **completed SUCCESS** in first attempt. Its workflow asserts the literal source Git SHA+TREE then executes **32 targeted Python regressions**, seven actual source apparatus with the corrected source-free numerical checker, and three real new teacher physical variations with their distinct no-production-import reference. Artifact `14403192843`, GitHub-reported ZIP digest `sha256:4e487ac56d79a0900bb84f4828f8c5a37715f98b8df07ec362f8f3cbd607780e` (not independently downloaded/rehashed). This is developer-orchestrated evidence even though executed in a separate GitHub repository.

Full **current HEAD** Python 3.10/3.12, genuine FEMM5, historical 73-step Chromium and the new source-native/replay/browsing PR checks were still queued/in progress when this request was written. **Check their actual latest status before PASS**, and read the first new source-head failed attempt if any. Do not use green CI belonging to old HEAD `5cfa02c2...`.

## Required output and no-merge authority

Publish an ORIGINAL independent re-review verdict at `projects/conductor_sim/pr-85/reviews/review-02-chat-b.md` to `physicsvigilante/review_sandbox`. Include actual source HEAD/tree, check new adversarial cases and original five false accepts, three genuinely new native physics families or explicit limits, source PDF/teacher provenance, actual saved native time/energy records, full CI and browser evidence, plus PASS / CHANGES-REQUESTED / INSUFFICIENT-EVIDENCE. Preserve review #01 CHANGES REQUESTED intact. Do not edit production or mark PR ready/merged. Even if no blockers remain, **separate explicit owner approval**, expected-head merge, exact merge Git tree and all actual postmerge `main` push workflows remain mandatory.

**JEE denominator rule:** M36b is seven selected source-backed apparatus (3 dynamics, 4 static) with one local 3D refusal, plus separate teacher transfer variations. The M36a 30-case candidate capability matrix is not a solved JEE exam score. No new BEM/FEMM arbitrary 3D conductor, textbook solver or scene graph is being claimed.
