# Chat B R2 independent review 01 — M36a JEE-30 candidate inventory

**Verdict: CHANGES-REQUESTED (inventory planning/source-interpretation review only).** No certification of any of the 30 original JEE apparatus simulations is made. The representative physics routes are generally honest and bounded, but one required source-head visualization CI workflow is CANCELLED, and the source/evidence auditor has reproducible *logical* blind spots requiring new negative tests. Keep the source PR draft and unmerged.

| Identity | Reviewed value |
| --- | --- |
| Project / source | [conductor_sim](https://github.com/physicsvigilante/conductor_sim) |
| Source PR | [#84](https://github.com/physicsvigilante/conductor_sim/pull/84) (open, draft, not merged when rechecked) |
| Base released M35b commit | 73e076cf7eaf7fefbae2b24afc1f54ff8f0b6fc6 |
| Exactly reviewed source HEAD | b6d7fccad26666100b172097b01738aedc8c9cf6 |
| Native source Git TREE | 2d0e4197d8e4405ec28029bb3f124fc86fa7ec80 |
| Frozen preregistration | 13eb3afde0efac049387d90a64eff44227f2acb4 |
| Reviewer | Chat B, separate GPT-6 conversation; independently read GitHub source and evidence, not a human subject-matter review |
| Review date | 2026-11-18 |
| Risk / scope | R2 scientific source-interpretation and evidence-meaning review of a provisional planning inventory, not 30-case native coverage certification |
| Production/source changes by Chat B | **None**. No source PR approval, merge, or CI rerun |
| Review specification | [Request](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/conductor_sim/pr-84/REQUEST.md), [reviewer prompt 02](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/conductor_sim/pr-84/REVIEWER-PROMPT-02.md) |

## Verdict rationale and findings, ordered by severity

### F-01 — BLOCKER: required full source-head visualization workflow did not complete

**Evidence observed:** The current-head [Visualization and source checks run #44156812874](https://github.com/physicsvigilante/conductor_sim/actions/runs/44156812874) completed as **cancelled**, not success. Its sole visualization job, ID 134299626630, started 2026-11-17 19:17:03 UTC and ended 19:27:12 UTC. The checked-in [.github/workflows/visualization.yml](https://github.com/physicsvigilante/conductor_sim/blob/b6d7fccad26666100b172097b01738aedc8c9cf6/.github/workflows/visualization.yml) configures a 10-minute timeout. The job log reports "The operation was canceled." The elapsed interval is consistent with reaching that limit; there is no evidence of a numerical assertion failure at the interruption point.

**What passed and what did not:** Its initial actual Chromium sweeps, Python pytest step (2,063 passed, 97 deselected), source-backed M6–M15 exports, and several browser checks succeeded. The job was cancelled while entering the later M15 nested-cavity phase. Subsequent M15, M16, M17, M26 and M27 steps were **skipped**. The successful separate Chromium jobs do not retroactively execute these skipped full-workflow steps.

**Required correction:** Split or bound the long visualization workflow, or otherwise make its required source-head checks complete successfully within configured limits. Rerun on the exact candidate source HEAD; any source change requires a new pinned HEAD/TREE and CI reconciliation. Do not call all required CI green while this run is cancelled.

### F-02 — MAJOR: the 30th official-apparatus source identity is not fail-closed

**Evidence type: source-code inspection and independent logical mutation, not executed Python audit.** In [tools/m36a_jee30_audit.py](https://github.com/physicsvigilante/conductor_sim/blob/b6d7fccad26666100b172097b01738aedc8c9cf6/tools/m36a_jee30_audit.py), the original 29 cases receive exact source/paper/page/question/tier/provenance comparisons. In contrast, the new 30th case checks ID, null old tier, page 16, the substring "Questions 9" in printed anchor, and 2021/official provenance substrings. It does **not** compare its source field to a pinned authoritative value or require the exact paired Questions 9–10 apparatus.

An adversarial mutation that replaces the 30th source with "fabricated-source.pdf" and the printed anchor with "Paper 1 Questions 9–11" still satisfies those explicitly coded 30th-case predicates (checked against the actual downloaded JSON and validator conditions). Other fields and declared counts need not change. Thus a plausible incorrect source/grouping is not caught by the current specific guard. This is a logical counterexample to the validator's intended identity guarantee; local Python execution of the mutated checkout was unavailable.

**Required correction:** Validate canonical 30th source identity and the two-question grouping explicitly, ideally with structured source ID and apparatus members, and add negative tests for source replacement, incorrect question-group membership, and year/provenance confusion. Preserve the genuinely correct first-source failure and separate fixed-field metadata gate.

### F-03 — MAJOR: frozen 3D refusal identities are not enforced by the count-only guard

**Evidence type: source-code inspection and independent in-memory JSON mutation.** Swapping the status of p70-three-cavities from "unsupported" to "supported_scoped" while swapping p01-single-08 the other way leaves totals exactly **24 / 3 / 3**. Both are allowable enum strings, document references still exist and all evidence flags remain pending. The current auditor validates the route enum and totals but not the identity of must-refuse cases. A silent false claim of general local multicavity 3D physics could therefore pass its categorical checks.

**Required correction:** Add a narrowly scoped fail-closed refusal/qualification check for the three deliberately rejected local-field cases (p11-linked-28, p70-cavity-offset, p70-three-cavities) and a tampering test. The auditor still cannot prove scientific truth; changing a frozen physical scope should require a deliberately documented new review rather than a counterbalancing count swap.

### F-04 — MAJOR: inherited PDF digests are compared as metadata, not recomputed from original bytes

**Evidence type: code inspection and immutable Git-tree comparison.** The auditor compares candidate.frozen_baseline.original_pdf_sha256 with historic.source_sha256. It does not compute SHA-256 from the two checked-in PDF files. A binary source PDF edit with metadata strings left unchanged would evade that check.

**Current repository integrity is nevertheless supported:** The pinned Git trees for M35b main and this HEAD have identical blob identities for the original PDFs: 02_conductors_half_size.pdf = 90d8869b0f01cc2ea13f83721985a5d8419f1d0e and POTENTIAL_CONDUCTORS1.pdf = 03e573af4038073a3b1a7b0ae67ef90c93fe1c24. The unchanged historical M21a JSON blob is 5c0ecb1633e691b1175c4095b5307bdc1bfa3740. Thus this is an *auditor safeguard gap*, not a demonstrated alteration of the current source PDFs.

**Required correction:** Rehash both actual source PDF byte streams against the historical SHA-256 values during the standalone audit. Include a temporary-file source-byte tamper regression. Keep the M21a inventory itself historically immutable.

### F-05 — MINOR: review-hub status has a stale prompt hyperlink

The central [STATUS.md](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/conductor_sim/pr-84/STATUS.md) labels its active link "REVIEWER-PROMPT-02.md" but its Markdown destination is REVIEWER-PROMPT-01.md. Prompt 01 is pinned to an outdated failed HEAD. Correct this review-hub link separately; it does not change the scientific source verdict.

### F-06 — EVIDENCE LIMITATION (not a demonstrated source-code defect)

The two original workbook/source PDFs could not be opened as binary page images via the connected GitHub file reader and were not available as named user uploads in this review. I verified their unchanged Git blob identities and reviewed original M21a's exact paper/anchor metadata. I also separately inspected official 2021 and 2020 exam PDFs; these do **not** substitute for new visual rereading of all 29 workbook anchors. No claim of a fresh 30-workbook-source visual audit is made.

## Source integrity and denominator reconciliation

Independent direct comparison of pinned candidate JSON to pinned M21a JSON found **all 29** historical cases unchanged and in order across ID, file, PDF page, printed anchor, question family, provenance and historical tier; their original M20c A/B/C classifications are not re-presented as current engine achievements. The extra unique ID is jee2021-p1-q09-q10-equipotential; the actual recorded apparatus is the official 2021 Paper 1 Q9–10 two-charge setup, **one system**, with no invented M21a old tier. The current matrix's declared classes exactly match the entry counts.

| Provisional document-based route hypotheses | Candidate count |
| --- | ---: |
| supported_scoped (bounded existing observation/physics route; not a fresh JEE PASS) | **24 / 30** |
| partial (some authentic physical observables, original situation not fully represented) | **3 / 30** |
| unsupported (requested local 3D conductor physics refused) | **3 / 30** |
| **New M36a case-specific native replays** | **0 / 30** |
| **New M36a independently verified original JEE simulations** | **0 / 30** |
| **New M36a original-case browser inspections** | **0 / 30** |
| **New M36a original-workbook PDF visual rereads** | **0 / 30** |

All 30 case replay states are "pending"; four mandatory evaluation dimensions remain "not_evaluated" and optional answer completeness remains "not_attempted". Three supported labels are not partial only because the exact requested *scoped* observable is represented; they do not certify full physical time history or arbitrary geometry. The unsupported cases are not completed simulations, even when a Gauss-law charge total is easily available. The selected cohort is not a statistically representative measure of all JEE examination problems.

The three "partial" cases are p08-multiple-21 (grounded sphere approach / unspecified induced-current time protocol), p13-matrix-05 (mixed wiring and geometric regimes), and p16-archive-numerical-01 (oil-drop final equilibrium versus underdetermined transient). The three "unsupported" cases are p11-linked-28, p70-cavity-offset, and p70-three-cavities for **local** irregular/multicavity induced field or surface density; Gauss-law totals alone do not qualify the local 3D picture.

## Independent physics/source-interpretation challenges

These are **independently computed small analytical checks and code/source reviews**, not newly integrated original problem executions. Relevant pinned production files inspected include distant_spheres.py, dipoles.py, prescribed_motion.py, motion_events.py, jee_potential_explorer.py, ring_field_observer.py and mixed_radial.py, plus source examples and focused historical tests.

1. **p2 Q19 ideal metal surface / electron stopping.** The one-sided sheet field for surface density -2.0×10⁻⁶ C/m² has magnitude |E| = |sigma|/epsilon0 = **225,881.8135 V/m**, not the insulating two-sided-sheet half-field. A 100 eV electron launched normally toward it has ideal initial speed **5.93097×10⁶ m/s**, reversal travel **0.442709 mm** and reversal time **0.149287 ns** using electron rest mass. The M24a code uses exactly the one-sided field, a numerically located velocity reversal, and separately labelled *teacher-chosen* starting distances of 1 mm or 0.2 mm. No induced conductor motion, contact or microscopic collision is inferred. **The scoped support label is reasonable.**
2. **p5 Q47 rigid dipole.** Uniform-field static interaction energy U = -pE cos(theta); from parallel, delta U = pE[1-cos(theta)]. With explicitly *illustrative* q=1 nC, separation 0.04 m and E=120 V/m, the four illustrative 40°, 90°, 115° and 180° poses give energy increases approximately **1.12299, 4.8, 6.82857 and 9.6 nJ**. The actual M23a dipole observer computes static finite-pair energy and torque, not fictitious elapsed angular dynamics. **Scoped support for the source's energy/orientation question is reasonable; rotation-time dynamics are not established.**
3. **p15 IIT-JEE 2012 proton between vertical plates.** Release from rest gives horizontal electric acceleration qE/m and downward gravity g. A 45° initial resultant requires qE = mg. Using *disclosed rounded source-example constants* m = 1.67×10⁻²⁷ kg, q = 1.6×10⁻¹⁹ C, g = 10 m/s², gap 0.01 m gives **E = 1.04375×10⁻⁷ V/m, V = 1.04375×10⁻⁹ V**. M21e actually composes independent E and g with a joint native trajectory and domain guard. **Scoped support is justified; pure qE-only motion would not be.**
4. **p12 Q40 two rings with transverse E.** At x = 0 and 0.4 m, each ring radius 0.3 m, charges +10 and -20 microcoulomb, test charge +10 microcoulomb, the independent ring-potential endpoint calculation gives **q(V_A - V_B) = +3.5950207169 J**. The external upward field 10⁵ V/m exerts **1 N transverse force**, but zero work between those equal-y endpoints. Code computes source ledger and no invented free axial trajectory. **Scoped static endpoint support is justified**, but not an unconstrained path.
5. **Official 2021 Paper 1 Q9–10.** For charges -Q at (0,0) and +Q/sqrt(3) at (2,0), V = 0 implies |r| = sqrt(3)|r-(2,0)|, hence **(x-3)²+y²=3**: centre (3,0) m and radius sqrt(3) m. Independent numeric substitution at five points on this circle gives residuals at floating-point zero. The actual viewer example samples the real potential grid, masks source singularities and states that Q=1 nC is illustrative, not original. Independently checked the [official 2021 Paper 1 PDF](https://jeeadv.ac.in/past_qps/2021_1_English.pdf), which places Q9 and Q10 on this one physical arrangement. **The grouping as one apparatus is correct.**
6. **p2 Q15 and p68 connected distant spheres.** In the leading isolated-self-capacitance limit, common potential gives Q_i proportional to R_i and E_1/E_2 = R_2/R_1. Production distant_spheres.py explicitly requires "self-capacitance-leading-order", bounds geometric coupling sum R_i/d_ij to at most 0.05 as an **admission policy, not a proven 5% error**, conserves charge and refuses nearby, nested and touching configurations. **Supported only in the stated asymptotic regime**, not exact close-sphere polarization nor time-varying wire current.
7. **p8 grounded sphere, p13 mixed shells, p70 multicavities.** A Kelvin-position sweep is not induced current dQ/dt without a specified approach protocol; disjoint and nested connections cannot be blended automatically; nonconcentric/irregular three-cavity local 3D charge maps are not supplied by the axisymmetric/spherical infrastructure. Their **partial/unsupported** labels are scientifically defensible.
8. **p3 Q30 and oil-drop source caveat.** The uniform-gap electron transit reference from rest is t = sqrt(2 m d²/(eV)); the actual event service reports first upper-plane encounter without post-impact claims, with teacher-chosen numerical d and V. For the JEE Advanced 2020 oil drop, the requested final force balance using rho=900 kg/m³, r=8×10⁻⁷m, g=10m/s², V=200V, gap 0.01m, e=1.6×10⁻¹⁹C gives continuous n≈**6.03186**, integer response approximately six. The [official 2020 Paper 2 PDF](https://jeeadv.ac.in/past_qps/2020_2_English.pdf) asks for the electron count, not a fully specified transient. Drag constant, switching time and full launch state are not supplied; M24b adds these as expressly teacher-defined illustrative values. The workbook's inherited printed "Numerical Q1" anchor is distinct from the original exam's question numbering. **"Partial" is conservative for full dynamic coverage**, and static equilibrium can be presented separately.

**Classification judgment:** No concrete incorrect scoped label was demonstrated within the representative source/code examples above. This does **not** independently certify all 24 classifications; source-original visual inspection and the separate original-question replay phase remain outstanding. The current science is not being rejected wholesale; the audit fail-closed and CI gates are.

## CI and independent execution evidence

| Evidence | Observed exact-source result | Distinction |
| --- | --- | --- |
| [Current-head PR Python run #44156813429](https://github.com/physicsvigilante/conductor_sim/actions/runs/44156813429) | Python 3.10 PASS; 3.12 PASS; the 3.12 log reports **2,063 passed, 97 skipped, 17 warnings**; all 10 M36a audit tests represented by ten dots | Existing Python regression checks; 97 skipped tests not passed |
| [Current-head push Python run #44156800941](https://github.com/physicsvigilante/conductor_sim/actions/runs/44156800941) | Both Python 3.10/3.12 success | Independent GitHub workflow execution, not Chat B local rerun |
| [Current-head real FEMM run #44156813667](https://github.com/physicsvigilante/conductor_sim/actions/runs/44156813667) | PASS, 97 actual live FEMM tests, native solver built, its separate Chromium review successful | Not 30 original-question replays |
| Current-head targeted Chromium runs [M18b #44156813173](https://github.com/physicsvigilante/conductor_sim/actions/runs/44156813173), [M18c #44156812793](https://github.com/physicsvigilante/conductor_sim/actions/runs/44156812793), [M15c #44156812959](https://github.com/physicsvigilante/conductor_sim/actions/runs/44156812959), [M19e #44156812973](https://github.com/physicsvigilante/conductor_sim/actions/runs/44156812973) | PASS | Distinct tests; they do not erase the cancelled full visualization job |
| [Full source-head visualization #44156812874](https://github.com/physicsvigilante/conductor_sim/actions/runs/44156812874) | **CANCELLED** at the configured ten-minute limit; later steps skipped | Required CI gate remains open |
| [Original first-source Python failure #44155780188](https://github.com/physicsvigilante/conductor_sim/actions/runs/44155780188) | **8 failed**, 2,055 passed, 97 skipped in Python 3.12; original 3.10 job cancelled | Real first-attempt failure retained. The 2021 printed-anchor-vs-provenance validator error caused cascading wrong-failure messages. Current-head correction no longer fails those ten tests. |
| Chat B's own checks | Read GitHub JSON/validator code, separately compared 29 historical identities, compared tree blobs, computed small physics references, and evaluated adversarial JSON and source-guard logical counterexamples | **Did not execute** pinned local Python audit CLI, pytest, FEMM solver, or original-case Chromium browser. Direct authenticated GitHub document reader cannot supply PDF binary for local clean checkout. |

No production code, original PDFs, numerical machinery or viewer module was changed by PR #84. The current source has no demonstrated new physical solver regression in the inspected examples. The original developer audit error is fully attributable to its incorrect metadata gate, but the preserved eight failures are important historical evidence and must not be rewritten as a clean first attempt.

## Separate scientific/educational scope judgments

| Axis | Judgment for this **planning inventory review** | Basis |
| --- | --- | --- |
| Source interpretation fidelity | **Conditional / not comprehensively established** | 29 inherited identities exact, 2021 official grouping reasonable, representative original physics checked; 30th provenance guard weak; full workbook visual reread unavailable |
| Physical/numerical correctness | **Sampled references consistent; 30-case status unknown** | Independent equations and representative production code; no 30 source-specific native replays |
| Simulation and observable coverage | **Provisional 24/3/3 only; achieved 0/30** | Scopes and refusals substantially bounded but not freshly independently simulated |
| Evidence integrity/provenance | **CHANGES REQUESTED** | New-source identity, frozen refusals and PDF-byte hash not fail-closed; earlier first failure honestly retained |
| Teacher-facing usefulness | **Not evaluated in M36a** | Existing example/browser regressions, not independent original-case student viewer inspections |
| Textbook answer completeness | **Not attempted / optional** | Not a gate to educational simulation acceptance |

## Minimum corrections and re-review / release advice

**Before any PASS:** (1) obtain a fully successful current-source visualization workflow, not cancelled; (2) make the 2021 source/apparatus identity fail closed and add hostile mutations; (3) bind deliberately unsupported irregular-3D case identities, rather than just counts; (4) check actual original-PDF bytes against historical digests with a tamper regression. Keep the prior failure record and all source-specific evidence denominators unchanged. Correct the central stale prompt link as low-risk housekeeping. If correction changes the source HEAD, re-pin exact HEAD/tree, rerun required CI and seek **targeted** independent re-review of these guards. The original workbook figures should receive independent source-page inspection when tools allow; do not assert this occurred here.

The next genuine validation milestone is a small **source-authored native and browser replay suite** for the sheet stop, dipole energy, proton E+mg, ring endpoint work, far-separated sphere model, 2021 zero-V circle and a negative 3D multicavity refusal. Report actual passes, unsupported refusals and teacher-assumed quantities separately. That later milestone, not this inventory, can establish numerical/visual original-problem coverage.

**Release authority remains with the owner.** This report is an independent scoped review, not PR approval. Do not mark PR #84 ready, merge it, push it to main, or convert provisional 24/3/3 labels to a 24-of-30 solved score.
