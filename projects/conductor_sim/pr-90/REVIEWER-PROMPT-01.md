# M37b / conductor_sim PR #90 — One independent source+physics+browser reviewer PROMPT #01

You are an **independent reviewer**, not the author of M37b. This is **ONE consolidated review**, not a repeat of M37a's already independently qualified Kelvin solver or M16a integrator. Execute actual new tests and browser challenges against the exact source.

**READ THE FULL REVIEW CHARTER FIRST:**
https://github.com/physicsvigilante/review_sandbox/blob/main/projects/conductor_sim/pr-90/REQUEST-01.md

**Production DRAFT PR:** https://github.com/physicsvigilante/conductor_sim/pull/90  
**EXACT HEAD:** `155b0544684d3d880a83a661cc8e14a0ce22f26b`  
**Native Git TREE:** `f48f54b8c49217b7c66179fe014b6fab1ea4dc4d`  
**Released base:** M37a merge `133acf97a123e6167aeaac3ca2a2b2094af1d36f`, tree `c728041ca5118013c6979d120c8805f31ee09fa0`, actual 22/22 main-push CI passed.  
**Charter BEFORE code:** `24300b2050430634532bb1978cba38eb7d3f39e4`, `docs/m37b_charter.md`.

At the time this prompt was composed, **24/26 exact-HEAD production workflow runs** were successful, with Python/visualization still running. **DO NOT RETURN PASS unless you independently verify all 26 terminal SUCCESS and the live PR/HEAD/TREE remain identical.** Stop STALE if the source moved. Do not substitute earlier-head green CI.

## Physical/educational target

Original unchanged `02_conductors_half_size.pdf` physical **p8 Multiple Correct Q21**, original p17 answer key **(1),(3)** (verified previously by the independent M37a reviewer on exact original PDF SHA-256 `9dff3c02a9f1848d2c3d99cb1a6e7a44dc7f5a51f7a3a2b8cc92d10ce1fbca5d`). A **positive external charge q** approaches a **grounded metallic sphere radius R** at **externally maintained constant small speed v**; correct conventional sphere→ground current is **positive and increases**. The original is a **workbook exercise** with symbolic givens, not an asserted official JEE past-paper item. The numbers q=+1nC, R=.10m, d0=.30m, v=.04m/s, duration=3s are visibly **TEACHER-CHOSEN ONLY**. The new 31 frames are ONE original apparatus/teacher illustration, **not** 31 textbook problems.

```text
d(t)=d0-v*t > R+guard
Q_sphere=-q*R/d(t)
I_sphere_to_ground=q*R*v/d(t)^2 > 0
dI/dt=2*q*R*v^2/d(t)^3 > 0
F_radial=-k*q^2*R*d/(d^2-R^2)^2
U_mechanical=-k*q^2*R/[2(d^2-R^2)]
```

The source describes **prescribed constant speed**, NOT a freely accelerating M16a particle. M37b is a genuinely new authoring *protocol* reusing static M37a Kelvin solves, not a FEMM electromagnetic transient, circuit simulation, Joule heating, or electron-drift visualization.

## Required new reviewer-owned execution

1. **Pin source:** fresh checkout and `git rev-parse HEAD^{tree}`, ten-file actual PR diff, charter ancestry and unchanged original PDFs, M37a production force/current observer, M16a solver, FEMM and historical viewers.
2. **New scientific tests:** independently recompute all 31 native physical q/Q/I/force/induced-energy/timestamp/source-position values with your own Kelvin SI math; check the one-half induced-energy factor, current sign and increasing trend, and native finite differences `-dQ/dt` against genuine shifted Kelvin states. Independently author at least one signed negative-q inward and one positive-q outward, translated nonaxis and changed-permittivity scenario; keep them labelled TEACHER HYPOTHETICAL, not original.
3. **Strict authoring and integrity:** challenge raw SI `author_prescribed_grounded_sphere` with Booleans in charge/radius/epsilon/**raw coordinates**. Note historical `PointCharge` normalizes Boolean coordinates before the new spec sees them; DO NOT falsely claim raw data can be recovered from an existing model. Reject nonfinite SI, wrong constraints, extra metals/sources, q=0, near/inside metal, surface guard crossings and invalid duration/speed/count. Forge native typed samples and require the viewer to refuse.
4. **Source-specific standalone JSON oracle:** `tools/m37b_source_reference.py` must import *no production physics*. Execute it on real saved source-specific output and independently mutate 12+ unfamiliar combinations of signed current, force, energy, units, declared q/R/d/v, SI time/position, source answer options, Boolean counts, extra false claims and wrong teacher-original attribution; accept only scientifically consistent declared-domain data.
5. **REAL offline Chromium:** check the true generated `p8-ground-current.html` against independently validated `p8-ground-current.json`. Verify visible workbook symbolic and teacher numeric claims, all actual drawn current-curve points, fixed sphere/charge geometry, t/d/Q/I/opposite-current visible numbers and synchronized marker for multiple selected time snapshots, source/restart/play, mobile width, and a useful **JavaScript-disabled original-first-sample fallback** with disabled fake controls. Include novel HTML-only attacks: forged visible original source text, stale numerical caption, altered `<polyline>` data, sphere radius, charge-sign label, slider numeric text, embedded JSON, hidden attribution or an unauthorized request. No browser-side physics, no external HTTP, no JavaScript exceptions.
6. **Evidence and CI:** independent source-pinned workflow or equivalent executed Python + Playwright, `set -euo pipefail`, preserve actual first attempt and hostile inputs/screenshots. Require **26/26 exact-head complete SUCCESS** (Python 3.10/3.12, actual FEMM5, historical browser/source, dedicated M37b real-browser and independent SI jobs). Prior development red runs stay red. Do not treat mere uploaded artifacts or valid-looking HTML as independent scientific proof.

## Deliverable

Publish a new attributed `physicsvigilante/review_sandbox/projects/conductor_sim/pr-90/reviews/review-01-chat-b.md` (main or dedicated review PR) with **PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE**, exact HEAD/TREE, real source and viewer hostile outcomes, full CI, source numeric attribution and defined limitations.

**DO NOT merge or mark production PR #90 ready.** A true independent PASS is only enough for a separate explicit owner approval decision. Chat A then uses `expected_head_sha`, verifies identical reviewed Git TREE on main, and requires actual postmerge main CI. No extra redundant full physics review if this one passes.
