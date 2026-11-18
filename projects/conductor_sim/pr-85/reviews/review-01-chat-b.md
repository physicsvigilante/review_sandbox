# Independent R2 review #01 — M36b source-JEE replay, PR #85

**Verdict: CHANGES-REQUESTED (scoped to M36b evidence validation, not a demonstrated core-physics failure).**

- **Project / source:** [physicsvigilante/conductor_sim](https://github.com/physicsvigilante/conductor_sim), [draft PR #85](https://github.com/physicsvigilante/conductor_sim/pull/85).
- **Source base:** `4e5fd2044a171bc889edf626f2c7795e15d5188c`; source HEAD: **`5cfa02c2b22ad1d488778653d63f54b4f9a06d1d`**.
- **Independently verified Git TREE:** **`3db298498bdd30b701ced59d3952eb529e835add`**, returned by GitHub Git Commit API for the literal HEAD.
- **Source code scope:** [seven changed PR files](https://github.com/physicsvigilante/conductor_sim/pull/85/files); runner, independently expressed checker, browser checker, regression suite, new workflow, two docs. No pre-existing physics/integrator files changed in this PR.
- **Preimplementation charter:** `6e3be20c83a26318b3b5147268e545a338fa71fb`.
- **Reviewer:** Chat B, GPT-6, separate ChatGPT conversation, *not* a distinct human expert. Date: **2026-11-18 05:52–06:00 UTC** (review window, approximate end).
- **Risk:** R2 — native scientific/evidence and displayed physical interpretation.
- **Source modifications by reviewer:** **none**. Source PR remained **draft/open/unmerged**, pinned HEAD unchanged at final prepublication query. This independent report alone does not authorize release.

## Overall judgment

The seven selected *saved* native apparatus are physically consistent with independent SI calculations on their stated approximations. The released engine APIs are called by the candidate runner, the native output is substantive, the seven original static/dynamic views are genuine generated HTML rather than empty placeholders, and the required historical CI completed. In particular the 2021 official two-charge zero-potential geometry is correct, and the unsupported p70 nonconcentric three-cavity local 3D field is explicitly refused.

**But the central M36b claim is stronger than matching seven preselected outputs.** The new source-free checker fails to reject several deliberately falsified observations in its own saved evidence format. Five independent mutations of *real saved M36b records* were accepted by isolated replays of the pinned checker functions, including impossible stopped-electron energy and falsified ring source-work and axial field. Three other deliberately corrupted controls were rejected. These are reproduced evidence-validation gaps, not assertions that the canonical native run produced incorrect physics. They block the R2 verification gate under the preregistered charter.

Additionally, **no locally installed conductor_sim checkout/runtime** was available to this reviewer, and the container cannot reach GitHub to clone it. I independently executed external physics arithmetic and saved HTML interactions, **not** out-of-sample engine runs using newly authored scenarios. Therefore this review cannot furnish the missing novel-native-execution signoff; no PASS is claimed.

## F-01 — MAJOR / R2: stopped-electron kinetic energy and transverse motion are not verified

- **Location:** [`tools/m36b_jee_reference.py` lines 47–78](https://github.com/physicsvigilante/conductor_sim/blob/5cfa02c2b22ad1d488778653d63f54b4f9a06d1d/tools/m36b_jee_reference.py#L47-L78), specifically the `stop` checks; [`tests/test_m36b_jee_replays.py` lines 50–69](https://github.com/physicsvigilante/conductor_sim/blob/5cfa02c2b22ad1d488778653d63f54b4f9a06d1d/tests/test_m36b_jee_replays.py#L50-L69).
- **Actual baseline:** `p02-single-19` terminal event at 1.4928735837340354e-10 s, x = 0.00055729060936 m, vx ≈ 1.37e-4 m/s, event kinetic energy ≈ 8.49e-39 J. Independent expected stop time ≈ 1.49287358369966e-10 s and displacement ≈ 0.00044270939064 m. Baseline passes.
- **Independent forged tests:** Copy the actual archived `p02-single-19` card; (a) replace `events[0].kinetic_energy_j` by **1e-18 J** while leaving every other field unchanged, or (b) replace `events[0].velocity_m_s[1]` by **+1000 m/s**, still declaring `full_stop=true`. **Both were ACCEPTED** by the verbatim `reference_sheet` function executed in isolation against the actual saved record. These contradictory claims are not physically possible for a full stop. The checker validates only vx, not the vector norm or energy of the event.
- **Required correction:** Verify all three components of event position/velocity (not just x), independent `K = 0.5 m |v|²` and stopping-energy tolerance, and consistent `full_stop` semantics. Add both mutations to the committed regression suite. Preserve appropriate physically dimensioned tolerances.
- **Confidence:** High for checker behavior; this is not evidence that actual production motion is wrong.

## F-02 — MAJOR / R2: early terminal surface encounter time has no independent root check

- **Location:** [`tools/m36b_jee_reference.py` lines 70–77](https://github.com/physicsvigilante/conductor_sim/blob/5cfa02c2b22ad1d488778653d63f54b4f9a06d1d/tools/m36b_jee_reference.py#L70-L77); [`tools/m36b_jee_replay.py` lines 95–104](https://github.com/physicsvigilante/conductor_sim/blob/5cfa02c2b22ad1d488778653d63f54b4f9a06d1d/tools/m36b_jee_replay.py#L95-L104).
- **Actual baseline:** the independently solved first root of `0.0002 + v0*t + a*t²/2 = 0` is **3.87505409689e-11 s**, consistent with saved **3.87505409122e-11 s**.
- **Forged test:** Replace only `early_surface_variant.event_time_s` with `0.8 * t_stop = 1.19429886696e-10 s`. **ACCEPTED** by the isolated exact checker predicate because it merely demands `0 < t_hit < t_stop`. A very late reported surface contact would wrongly be certified despite violating the launch/field equation.
- **Required correction:** Export the early native contact event's true position and velocity as well as time, independently compute the *first* surface root from source sigma, mass, charge, starting distance and speed, and verify chronological preemption of reversal within event tolerance. Add late-but-before-reversal forged event to regression tests.
- **Confidence:** High. The native baseline itself is correct.

## F-03 — MAJOR / R2: ring field and per-source work ledger can be fabricated while total work stays correct

- **Location:** [`tools/m36b_jee_reference.py` lines 124–149](https://github.com/physicsvigilante/conductor_sim/blob/5cfa02c2b22ad1d488778653d63f54b4f9a06d1d/tools/m36b_jee_reference.py#L124-L149).
- **Actual baseline:** source values Q_A = +10 μC, Q_B = −20 μC, R = 0.30 m, separation = 0.40 m, test q = +10 μC, upward E = 1e5 V/m. Independent axial endpoint fields: **Ex(A) = +575203.314704715 V/m**, **Ex(B) = +287601.6573523575 V/m**. Independent work: **W_A = +1.19834023896816 J**, **W_B = +2.39668047793631 J**, **W_up = 0 J**, total **+3.59502071690447 J**. Archived baseline matches all.
- **Forged tests:** (a) Replace `observed_source_work_components[0].field_work_j` with **999 J** but preserve the true total; (b) replace `start_electric_field_v_m[0]` with **−1e9 V/m**. **Both were ACCEPTED** by the isolated `reference_ring`. The checker checks part IDs and the applied-field part's zero work, but not ring A/B part values nor sum of components. The axial field comparison is tautological: the expected Ex is literally read from the actual Ex.
- **Required correction:** Independent source-by-source Coulomb ring endpoint E and potential/work expressions, signed Ex at both endpoints, per-component work and sum against independently computed total. Assert upward qE = 1 N transverse and no free-axial-path claim. Add forged Ex and signed ledger entries to adversarial regressions.
- **Confidence:** High. Prescribed source fields and saved total work are correct in the actual candidate data; the defect is reference coverage.

## F-04 — MINOR: chosen distant-sphere apparatus does not actually exercise nontrivial redistribution

- **Location:** [`examples/distant_connected_spheres.py` `surface-ratio` case](https://github.com/physicsvigilante/conductor_sim/blob/5cfa02c2b22ad1d488778653d63f54b4f9a06d1d/examples/distant_connected_spheres.py); [`tools/m36b_jee_reference.py` lines 181–207](https://github.com/physicsvigilante/conductor_sim/blob/5cfa02c2b22ad1d488778653d63f54b4f9a06d1d/tools/m36b_jee_reference.py#L181-L207).
- The teacher's initial charges +2/+4 nC on 0.10/0.20 m conductors are **already at equal leading-order potential**; final charges are exactly the same and released energy is zero. This correctly checks E1/E2 = 2 for the source question, but it does **not** experimentally demonstrate charge transfer despite the more general “sharing” language.
- **Suggested bounded addition:** Keep the preregistered case and seven-case denominator unchanged; add a distinct teacher-labelled non-equilibrium variation +5/+1 nC at the same radii/separation, expecting final +2/+4 nC, signed transfer −3/+3 nC and positive electrostatic energy release. Exercise the actual backend in CI if source input preservation permits. Do not silently substitute this for the original selected question.
- **Confidence:** High for the test-strength limitation; not a defect in the original answer.

## F-05 — QUESTION / potential evidence integrity gap: no authoritative source-mask geometry exported for independent 2021 verification

- **Location:** [`tools/m36b_jee_replay.py` lines 189–214](https://github.com/physicsvigilante/conductor_sim/blob/5cfa02c2b22ad1d488778653d63f54b4f9a06d1d/tools/m36b_jee_replay.py#L189-L214); [`tools/m36b_jee_reference.py` lines 209–242](https://github.com/physicsvigilante/conductor_sim/blob/5cfa02c2b22ad1d488778653d63f54b4f9a06d1d/tools/m36b_jee_reference.py#L209-L242).
- The manifest exports only `source_mask_count=2`, not mask centres/radii or source-to-mask associations. The reference verifies count and analytic contour residual but **cannot independently detect shifted or incorrectly placed masks**. I inspected the archived HTML image and found the two masks visibly aligned in the actual output, so this is not an observed bad scene.
- **Suggested correction:** Export mask geometry and verify exclusions cover the actual singular source locations; add a changed-mask-location counterexample. Treat independent proof that an arbitrary contour came from the native sampler (rather than an analytically authored list of circle points) as a provenance/evidence issue, not something a geometric residual test alone can certify.
- **Confidence:** Medium, source-inspection limitation rather than an observed production failure.

## CI, provenance and actual artifact inspection

**Fresh current-HEAD GitHub Actions query:** **18/18** associated PR and push runs, all `completed/success`, head SHA identical to above; zero failed/cancelled runs. Relevant independently fetched *job logs and step results*:

| Exact-head workflow | Source and observed job outcome |
| --- | --- |
| [PR Python 3.10/3.12 #44243206739](https://github.com/physicsvigilante/conductor_sim/actions/runs/44243206739) | **2,090 passed / 97 skipped / 17 warnings each**. The 97 skips are explicitly FEMM-only in generic environments, not solver passes. |
| [Actual FEMM5 #44243206749](https://github.com/physicsvigilante/conductor_sim/actions/runs/44243206749) | Separate real solver job successful; **97 FEMM integration tests passed** (per source job and logs), FEMM source checkout/build present. |
| [Full historical Chromium #44243206809](https://github.com/physicsvigilante/conductor_sim/actions/runs/44243206809) | **73/73 actual job steps success**; Pytest 2,090 passed / 97 *deselected*, no cancelled steps. |
| [M36b source branch push #44243111752](https://github.com/physicsvigilante/conductor_sim/actions/runs/44243111752) and [PR #44243206721](https://github.com/physicsvigilante/conductor_sim/actions/runs/44243206721) | New source-native / reference / browser workflows success. Push log explicitly recorded **14 focused regressions passed, seven native apparatus exported, seven reference cases passed, seven real Chromium openings passed**. All are developer-controlled tests, not separate-context novel native tests. |

**Actual source-run artifact downloaded and opened:** workflow #44243111752, artifact **14400163983**, 24 extracted files including `native-replays.json`, `independent-reference.json`, `browser-checks.json`, seven screenshot PNGs, actual offline HTMLs, source-head/tree proof and original-source PDF hash manifest.

- **Independently hashed artifact ZIP, SHA-256:** `bdf2310cc3d534d4d702504b8f6b06cdae713f83443107e82c009ad73e3b807f`. Exactly equals provider-upload digest; this is **a locally computed archive hash**, not merely a repeated GitHub claim.
- **Independently hashed `native-replays.json`:** `b733394dddc13eaf61cda1596f36626616a9ff7ceebc471d13bccfc46c1b3cff` (40,433 bytes). This is the saved unmodified baseline used for the reviewer probes; mutations were made **in local copies**, not in source/archive.
- **Source identity inside downloaded archive:** `source-commit.txt` = the literal HEAD; `source-tree.txt` = the literal Git TREE. Archived PDF SHA manifest reports workbook `9dff3c02a9f1848d2c3d99cb1a6e7a44dc7f5a51f7a3a2b8cc92d10ce1fbca5d` and notes `8d0d9b5cf821219058cfc4b7685a39b777e460944df44c3f9cffcb68157a60e5`. The PDF **bytes were not independently downloaded/rehashed by Chat B**; the source workflow performed the hashing.
- **Native denominator:** seven selected supported apparatus = **three real elapsed-time dynamics** (sheet, plate, proton) + **four true static** (dipole, rings, distant spheres, two-charge contour); one explicitly unsupported p70 local 3D refusal **not** an eighth successful apparatus.
- **Source coverage:** scanned workbook pages p2, p3, p5, p12, p15, p70 were *not* independently reopened as image/PDF pages. GitHub-anchored original-case matrix, source example text and source hashes were read. The **official JEE Advanced 2021 Paper 1 p4 Q9–10 original question and diagram were independently visually reopened** via [official PDF](https://jeeadv.ac.in/past_qps/2021_1_English.pdf): −Q at (0,0), +Q/√3 at (2,0), one circle apparatus; centre b=3 m, radius R=√3 m. Do not elevate the other workbook-page source claims to independently page-reinspected status.
- **Repository AGENTS.md:** absent from the pinned Git tree (recursive tree listing checked); the review follows the central PROTOCOL/REQUEST and source charter.

## Original arithmetic, cross-evidence and novel challenge (executed vs unexecuted)

I separately recomputed **all seven actual saved source cases** with Python standard-library equations, without importing source physics or the developer reference checker. Diagnostic examples:

- Sheet: one-sided conductor E = −225881.8134746 V/m; reversal `t=1.49287358370e-10 s`, displacement `0.00044270939064 m`, early surface root `3.87505409689e-11 s`.
- Plate: `t=3.37212992374e-9 s` and arrival kinetic energy `1.602176634e-17 J`.
- Dipole: all four candidate ΔU values independently match `p E (1−cos θ)`; I additionally selected **65°** in the archived HTML via a separate local system-Chromium run, obtaining ΔU ≈ **2.77143234e−9 J** and τz ≈ **−4.35027738e−9 N·m**, matching the visibly displayed independent static pose/torque.
- Two rings: both signed on-axis field endpoints, ring A/B individual work (numbers in F-03), total +3.5950207169 J and 1 N genuine transverse qE independently checked.
- Proton: **all 25 archived time samples** independently satisfy `x=gt²/2`, `y=−gt²/2`, `vx=gt`, `vy=−gt`, force and kinetic energy at original q,m,g; all preview samples remain between plates. Additionally selected archived browser **t=0.018 s** and visually inspected vector arrows/graphs and saved-state readout.
- Distant spheres: before=after already equilibrated; saved outer surface fields independently agree with `kQ/R²` for both radii, ratio 2 and conserved group charge.
- Official 2021 Q9/10: **197 archived sampled contour points** checked independently against the circle and Coulomb V=0 equation. Maximum radial discrepancy = **0.00171054046 m**; maximum absolute Coulomb potential residual = **0.01771645 V**. The originally attempted exploratory 0.01 V cutoff failed; this was **a reviewer-chosen overstrict grid-interpolation threshold**, not a production defect. The first negative observation is retained here; using 0.02 V as an explicit more realistic independent diagnostic passed. Actual source reference limit is 0.12 V.

**Out-of-sample original physical variations newly invented and independently calculated** (these calculations executed; the novel variants were **NOT run through the production engine**):

| Family | New input | Independently predicted output |
| --- | --- | --- |
| Sheet reversal | 175 eV, σ = −3.4e−6 C/m², clearance 1.1 mm | reversal t = **1.16169771804e−10 s**, stopping displacement **0.455730255 mm** |
| Rigid dipole | q=1.2 nC, separation=6 cm, E=200 V/m, θ=65° | ΔU **8.31429703e−9 J**, τz **−1.30508321e−8 N·m** |
| Electric + gravity | m=2e−27 kg, q=1.4e−19 C, E=1.04375e−7 V/m, g=9.81, t=17 ms | acceleration (7.30625, −9.81) m/s²; position **(0.001055753125, −0.001417545) m** |
| Two rings + transverse E | QA=+8 μC, QB=−15 μC, R=.25 m, d=.45 m, probe +4 μC, Ey=220 kV/m | axial endpoint work **+1.70119437284 J**, transverse force **0.88 N** |
| Far-connected spheres | R1=.1 m, R2=.2 m, before charges +5/+1 nC | leading-order after **+2/+4 nC**, transfer −3/+3 nC |
| Charge-pair zero contour | translate original charges x→x+1 m | circle centre **(4,0) m**, radius **√3 m** |

### Adversarial checker tests actually performed

I copied the **literal predicate bodies** `reference_sheet` and `reference_ring` plus the unchanged `near`/`near3` helpers from pinned `tools/m36b_jee_reference.py` into a standalone local Python test harness, executing them on **deep copies of the actual downloaded native JSON**. This is **isolated function replay**, not a repository checkout or a claim that `python -m tools.m36b_jee_reference` was independently run in its original package environment. The complete `check_native` method simply dispatches these functions for the two affected cards, so source inspection supports the predicted full-checker impact.

| Mutation of genuine archived field | Observed isolated checker | Should happen |
| --- | --- | --- |
| Sheet terminal kinetic energy → 1e−18 J | **ACCEPT** | REJECT |
| Sheet terminal vy → +1000 m/s while `full_stop` true | **ACCEPT** | REJECT |
| Sheet early hit time → 0.8×t_stop | **ACCEPT** | REJECT |
| Ring A field work → 999 J, original total unchanged | **ACCEPT** | REJECT |
| Ring start axial Ex → −1e9 V/m | **ACCEPT** | REJECT |
| Sheet metal E sign reversed | **REJECT** | REJECT |
| Sheet terminal reversal time +5e−11 s | **REJECT** | REJECT |
| Ring total work → 15 J | **REJECT** | REJECT |

The developer already has additional committed tests rejecting a plate kinetic-energy change, proton position change, contour-coordinate change, unsupported local-3D falsely promoted to simulation, and fake static-as-dynamic label. Those are **developer tests**; the eight rows above are the reviewer's independently selected isolated-function probes.

### Actual independent educational-view inspection

I opened **all seven archived CI screenshots** for visual assessment. Charts and labels visibly represent the intended physical distinctions: sheet and plate event preview, 2012 proton under orthogonal forces, non-moving dipole poses/energy graph, proper ring schematic with upward E, static distant sphere states, and a genuinely plotted magenta V=0 contour around +Q/√3 with singular source masks.

I further loaded four saved original offline HTMLs into **locally available Chromium**, using `page.set_content` (file URL navigation is policy-blocked in this container) and exercised dipole pose index 13→65°, proton frame index 9→18 ms, sheet late preterminal frame, and full-page official 2021 static plot; no JavaScript page errors. This is additional **independent browser inspection of saved assets**, not fresh engine-generated HTML.

**Pedagogical judgment:** meaningful and generally legible when opened full-page, especially physical-time/static labels and proton component plots. At the initial 1280×800 CI screenshot viewport, much of each graph lies below the fold; a single opening screenshot does not attest to final event frames or all pedagogy. Dipole viewer exposes a raw compact classification JSON block, which could use clearer teacher-language rendering (minor polish). No classroom learning test or blind teacher authoring evaluation was performed.

## Separate scoped scores

| Dimension | Judgment | Grounds / limits |
| --- | --- | --- |
| **Source interpretation fidelity** | **PARTIALLY VERIFIED** | 2021 official original Q9–10 checked against actual PDF page/diagram. Workbook text, anchors, hashes and teacher distinctions inspected, but workbook page images not independently reopened. One justified p70 local 3D refusal. |
| **Physical and numerical correctness** | **PASS FOR THE SEVEN SAVED OBSERVATIONS ONLY** | Independently derived all seven on saved data. Full production engine under new out-of-sample parameters **NOT RUN**. |
| **Native simulation and observable coverage** | **PARTIALLY VERIFIED** | Pinned developer CI executes three true elapsed-time + four static cases and one refusal. No new independent native variation run. No claim for other 23 provisional M36a cases. |
| **Evidence integrity / falsification resistance** | **FAIL (R2 blocker)** | F-01 through F-03; five scientific false records accepted by checker predicates. Original artifact ZIP independently hashed correctly. |
| **Teacher-facing / educational viewer usefulness** | **BOUNDED POSITIVE, NOT CERTIFIED** | Seven screenshots inspected and four saved HTML views independently interacted with. Quality and source/teacher/time labels generally useful; below-fold first screenshots and no actual teacher testing. |
| **Textbook-answer completeness** | **NOT ATTEMPTED** | Not demanded as this milestone's success criterion. |

**Important denominators:** exactly **seven preselected, not random, original-source apparatus**, with **three dynamics and four static observations**, one separately unsupported 3D refusal. **No automatic seven-of-30 JEE solving rate; no 24/30 claim.** Another original 23 M36a candidate apparatus were not replayed by M36b, and two questions in the official 2021 linked pair are **one physical apparatus**.

## Smallest corrective path and release advice

1. Fix F-01 through F-03 with independent physical predicates for complete stop event state, first sheet contact root, signed ring endpoint Ex and per-source work/sum. Add the **five failing tamper controls** plus preserved positive controls to committed tests. F-04 is a useful nonblocking secondary composability test; F-05 should be included if source-mask integrity is represented as independently verified.
2. Because any checker/source change changes the current HEAD, create **a new pinned SHA/TREE**, rerun genuine focused and all source-head CI (Python 3.10/3.12, real FEMM, historical Chromium, M36b source-native/reference/browser), and publish exact artifact/digest evidence. Retain original failures; do not retroactively edit this report.
3. Run at least three **fresh independently authored supported native parameter variations** across different physics families in a genuine checkout/runtime, with reference outputs specified before viewing results. Prioritize sheet event, finite dipole, and proton qE+mg or ring endpoints, plus one nontrivial far-sphere redistribution. A new targeted Chat B review should verify both checker fixes and fresh native traces.
4. Until then **keep PR #85 DRAFT/UNMERGED**. Even a later no-blocker R2 signoff requires separate explicit owner approval before Chat A may use expected-head merge and verify exact merged tree and all resulting main-push workflows. This report is **not release authorization**.

**Reproducibility provenance:** original GitHub current-head PR and Git-tree API, developer run logs, downloaded unchanged ZIP + archived native JSON hashes above, source checker code at pinned blob, and original reviewer-authored standalone Python arithmetic/predicate test. Original workbook PDF bytes and production package were not independently downloaded into the local reviewer environment. The acknowledged verification limitations are not silently counted as passes.
