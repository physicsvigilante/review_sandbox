# Independent review #02 — conductor_sim PR #109 / JEE-12 source and native replay

**Verdict: PASS — narrowly for mandatory B1/B2 evidence closure at the exact pinned production tree.** This is not certification of twelve fully answered original exercises, not an unrestricted conductor-physics qualification, and **not a merge instruction or owner approval**.

**Reviewer:** ChatGPT GPT-6, independent reviewer #02, 20 November 2026. This review used original raw PDFs and direct execution of the released Python interfaces, not the developer's own JEE-12 probe scripts as its oracle.

## Immutable object verified

- Production PR: https://github.com/physicsvigilante/conductor_sim/pull/109
- PR head: **975e2e23a86fe29bbaafebc20e684312d2aa5b6d**
- Native Git tree: **ddcc0b9923584495f78e2ea05a7f1ff56622e8d2**
- Main/base: **337001f2e0d1ce62c87fa4352993c4a074cfbde6**
- Live PR state rechecked: **open / draft / unmerged**. The distinct PR #105 remains **open / draft / unmerged**.
- Review #01 previously verified 14 PR additions limited to documentation, source-evaluation tests and audit probes, with no modified production solver or source PDF. No released science files were changed to create this report. Source commit/tree were asserted by each independent hosted job.

## B1: Original PDF bytes, rendered pages, and source-to-claim comparisons — PASS

The reviewer authored an isolated GitHub Actions workflow on a new branch of review_sandbox. It checked out production **by commit SHA**, asserted the **native tree**, computed SHA-256 over the **original PDF files**, and used Poppler to render the required pages into reviewer-owned downloadable JPEG/text artifacts. The reviewer then personally examined all **twelve actual page images**, not only developer prose, source excerpts, or success badges.

| Actual file | Verified SHA-256 of raw bytes | Actual inspected PDF pages |
| --- | --- | --- |
| 02_conductors_half_size.pdf | **9dff3c02a9f1848d2c3d99cb1a6e7a44dc7f5a51f7a3a2b8cc92d10ce1fbca5d** | 1, 2, 3, 7, 8, 11, 12, 16 |
| POTENTIAL_CONDUCTORS1.pdf | **8d0d9b5cf821219058cfc4b7685a39b777e460944df44c3f9cffcb68157a60e5** | 26, 27, 69, 70 |

The first column below uses **PDF page indices**. For the workbook, printed textbook page labels are **3.33, 3.34, 3.35, 3.39, 3.40, 3.43, 3.44, 3.48**, respectively. These labels are not interchangeable with the PDF indices.

| PDF page and source anchor | Independently inspected original wording, diagram, and options | Source fidelity and science boundary |
| --- | --- | --- |
| Workbook **p1**, Single Correct **Q8** | Electron moved by **us** from A to B in uniform +x **10 V/m**; diagram has AB=5 m, BC=3 m and 4 m horizontal displacement. **Option (2): 40 eV**. | External quasistatic work **+40 eV**, field work **−40 eV**; a free electron trajectory is **not** source-defined. |
| Workbook **p2**, Single Correct **Q19** | **100 eV electron**, **large metal plate**, surface sigma **−2.0×10⁻⁶ C/m²**. Original asked limiting starting distance. **Option (1): 0.44 mm**. | Correct one-sided *metal* field is |sigma|/epsilon0, not the isolated insulating sheet's half field. **0.442709 mm**. Developer example's **1 mm launch gap is teacher chosen**. |
| Workbook **p3**, Single Correct **Q27** | **Solid conducting sphere** radius **10 cm**, concentric **thin metal shell** radius **20 cm**, initial inner charge **20 µC**, connected by conducting wire. Asked **heat generated**; **option (2): 9 J**. | Calculate difference in **two static equilibria**, giving ~8.98755 J ideal; do **not** imply time-resolved connection current. Numerical 1 µm shell thickness is a teacher approximation. |
| Workbook **p7**, Multiple Correct **Q13** | **Neutral conductor with spherical outer face**, displaced inner point charge **q** (marked **x**) and outside point P. Printed options: x-dependent V; x-independent V; induced outer **+q uniform**; inner **−q nonuniform**. | **Options (2), (3), (4)** for the drawn off-centre charge; the outside potential is independent of x. The drawn cavity is not a new general irregular-3D sigma solver. |
| Workbook **p8**, Multiple Correct **Q21** | **Positive q** approaches **grounded metal sphere** radius **R** at constant small speed **v**. Options explicitly distinguish wire current **into ground / out of ground** and increasing/decreasing magnitude. | **Options (1), (3)**: conventional positive current sphere→ground and rising as separation shrinks. Static sweeps alone do not establish current; a supplied velocity/time derivative does. |
| Workbook **p11**, linked **Q28** | Original drawing is a **noncircular/irregular connected outer conductor** with two interior cavities carrying **q1/q2** and a **separate exterior point q**. **Option (1): Q+q1+q2, nonuniformly distributed**. | Gauss fixes whole-face total **Q+q1+q2**. Outer distribution is nonuniform, in particular in the external field. Original **external q must not be omitted** to claim a local density solution; local irregular E/V/sigma remains unsupported. |
| Workbook **p12**, linked **Q40** | Two rings radius **0.30 m** separated axially **0.40 m**, carrying **+10 µC, −20 µC**; test charge **+10 µC**; *vertical* uniform electric field **10⁵ N/C** perpendicular to horizontal C_A→C_B. **Option (4): 3.6 J**. | Uniform vertical field contributes **zero axial endpoint work**; the two rings give **+3.59502 J** (independently arithmetic-checked in review #01). No invented trajectory or transverse acceleration. |
| Workbook **p16**, archive numerical **Q1** | Original workbook explicitly prints **JEE Advanced 2020** below question. Two-disc oil drop: **200 V**, **0.01 m**, drop radius **8×10⁻⁷ m**, density **900 kg/m³**, **g=10**, **e=1.6×10⁻¹⁹ C**, initially terminal/falling, switch applied and then stationary. | Ideal electrostatic balance n e(V/d)=mg gives about **6 electrons**; switch chronology, fluid drag constant and fringe field are **not** specified sufficiently for a unique transient. Printed archive attribution is not independent checking of the official exam source. |
| Notes **p26**, **Illustration 1** | Explicit text: **“A conducting sphere of radius R has charge Q.”** Asks V at **R/2** and **3R/2**; printed **kQ/R** and **2kQ/(3R)**. **Illustration 2 below is a different nonconducting volume sphere.** | Source original is a **solid conducting sphere**, not a hollow shell; the old cohort family label is historical metadata, not a valid reinterpretation. |
| Notes **p27**, **Illustration 4** | Drawing central source **q**, thin shells with charges **q1, q2** at radii **a, b**, A radius **r** in inner cavity, B at **r1** between shells. Printed **V_A=kq/r+kq1/a+kq2/b**, **V_B=kq/r1+kq1/r1+kq2/b**. | Original is symbolic ideal thin-shell geometry; finite-thickness shell values or moved charge are explicitly **teacher variations**, not original printed givens. |
| Notes **p69**, **Illustration 7** | One spherical metal shell with **3q** net metal charge, inner point **q** centered (A) or displaced (B). Printed **inner −q, uniform in A/nonuniform in B**, **outer +4q uniform in both**. | Compare two **static** spherical models; not motion. Whole-face Gauss totals and signed local densities are consistent with images. |
| Notes **p70**, **Illustration 9** | Printed **three cavities** **S1/S2/S3** inside one exterior **S4**, central q1 and displaced q2/q3. Printed S1 **−q1 uniform**, S2 **−q2 nonuniform**, S3 **−q3 nonuniform**, S4 **q1+q2+q3 uniform**. Page also has **Illustration 8**, distinct irregular-boundary examples. | The drawing is a **2D cross-section** without a unique complete 3D boundary. Whole-face Gauss totals can be stated; spherical local density is a **separately declared teacher geometry**, not an unrestricted original-figure solve. |

All workbook items other than the distinctly marked archive item are **workbook exercises**, not established official JEE examination problems. Notes Illustrations 1/4/7/9 are **teaching notes**, not official examination papers.

**Direct visual-evidence artifacts:** [workbook eight rendered pages](https://github.com/physicsvigilante/review_sandbox/actions/runs/44718296306/artifacts/14621360033), [notes four rendered pages](https://github.com/physicsvigilante/review_sandbox/actions/runs/44718296306/artifacts/14620222263); actual SHA lines, render provenance and original page bytes are visible in the independent jobs' logs. This reviewer saw all twelve page images reconstructed from these exact job log payloads.

## B2: Independent direct execution of released native APIs — PASS

**Reproducer:** [review-02-chat-b-native.py](https://github.com/physicsvigilante/review_sandbox/blob/review/conductor-pr109-chat-b-r2-20261120/projects/conductor_sim/pr-109/reviews/review-02-chat-b-native.py), [workflow](https://github.com/physicsvigilante/review_sandbox/blob/review/conductor-pr109-chat-b-r2-20261120/.github/workflows/jee12-pr109-review02.yml), [final green evidence run](https://github.com/physicsvigilante/review_sandbox/actions/runs/44718296306), [native trace artifact](https://github.com/physicsvigilante/review_sandbox/actions/runs/44718296306/artifacts/14621350063).

Independent Python was installed from exact production HEAD and called **actual released physical interfaces** (PrescribedField/endpoint_field_work, EventStudy/investigate_motion, ConnectedShellBackend, observe_grounded_sphere_wire, MixedRadialBackend, NestedShellBackend, solve_cavity_gauss, solve_spherical_sigma). It made original SI predictions separately and asserted native values, **without importing developer JEE-12 probe scripts or cached answer JSON**. Evidence contains the reviewer script, stdout, source HEAD/tree and JSON witness records.

| Native witness | Executed result | Separately derived expectation / limit |
| --- | --- | --- |
| p1 work | **external +40.0 eV; field −40.0 eV** | Signed charge × endpoint potential difference; no trajectory. |
| p2 stopping | **0.44270939064000014 mm**, stop **1.4928735837340354×10⁻¹⁰ s**, authentic **terminal-event** | Source 100 eV and one-sided metal E; teacher start **1 mm**. |
| p3 wire connection | **8.98750685427752 J** finite 1 µm shell; analytic ideal **8.987551792261172 J** | Field-energy difference before/after, not thermal time evolution or current. |
| p8 grounding | Sphere→ground **3.7037037×10⁻¹¹ A** at d=0.9 m, **8.3333333×10⁻¹¹ A** at d=0.6 m, with *teacher* radial approach speed 0.05 m/s | Q_ind=−qR/d, current magnitude qRv/d². |
| p26 original | Solid-sphere **V(R/2)=kQ/R** and **V(3R/2)=2kQ/(3R)** through native MixedRadialBackend | Independent symbolic Gauss reference. |
| p27 original/teacher distinction | True native concentric finite-thickness shell A/B potentials and inner-face **−q** | Compare to independently written finite-interface SI Gauss expressions; do not substitute finite values as printed ideal formulas. |
| p69 central/displaced | Native M40a **separate centered and shifted spherical solves**; centered sigma equal on three normals, displaced sigma differs on opposite normals, both have **−q** inner and **+4q** outer, uniform exterior checked | Independent spherical Poisson-kernel formula; source movement is not integrated. |
| p11 refusal | Conditioned Gauss outer whole-face **8×10⁻¹⁰ C** for reviewer-authored q1/q2/Q; local **sigma, E, V all refused** | Actual source has an external q and irregular boundary not embodied in topology-only solver. |
| p70 refusal/teacher | Source-only topology local sigma **refused**; separately qualified three-void spherical teacher variant returned bounded sigma sample, **5.4270043483×10⁻¹⁰ C/m²** | Original 2D drawing does not fix a 3D density map. |

**Three unfamiliar signed/translated physical teacher variations**, genuinely executed, each runs p26 solid-sphere, p27 nested-shell and p69 spherical local-density public APIs with independent SI formulas:

| Variant | Translated center (m) | Source q (C) | Solid V(R/2), V(3R/2) (V) | Displaced inner sigma samples at ±x (C/m²) |
| --- | --- | --- | --- | --- |
| 1 | (0.13, −0.08, 0.06) | **−1.1×10⁻⁹** | −59.91701195, −39.94467463 | +8.62465×10⁻⁹, +1.31984×10⁻⁹ |
| 2 | (−0.17, 0.11, 0.09) | **+2.6×10⁻⁹** | +101.59841156, +67.73227438 | −1.14202×10⁻⁸, −1.49888×10⁻⁹ |
| 3 | (0.09, 0.04, −0.18) | **−0.8×10⁻⁹** | −77.31227348, −51.54151565 | +1.74687×10⁻⁸, +3.34304×10⁻⁹ |

These inputs, dimensions and local density samples are **reviewer-authored tests** and not claimed original source numerical parameters. The three variants use both signs and three genuinely different translated centers.

### Red-run honesty and final-run evidence

1. **Initial run [44717108550](https://github.com/physicsvigilante/review_sandbox/actions/runs/44717108550): FAILED overall.** Both PDF verification jobs checked out the exact source and **verified both actual PDF SHA-256s**, then failed at **pdfinfo: command not found**, exit 127. The independent native job itself **PASSED**. This is a reviewer-harness Poppler setup problem, not evidence of a physics failure.
2. **Corrected run [44717257747](https://github.com/physicsvigilante/review_sandbox/actions/runs/44717257747): all three jobs SUCCESS** after installing Poppler, with twelve original rendered pages and direct native test success.
3. **Strengthened final run [44718296306](https://github.com/physicsvigilante/review_sandbox/actions/runs/44718296306): all three jobs SUCCESS**, after expanding native p69 evidence to **actual centered and displaced** M40a solves. Native job prints **REVIEW02_NATIVE_PASS** and exact production SHA/TREE. The source PDF binaries and production checkout were unchanged across all three attempts.

The original production CI's **21 successful workflow runs / 24 checks** and prior Chromium JS-on/JS-disabled inspection were established by independent review #01, not rerun here. No full production suite or new browser matrix is claimed for review #02, because the target production tree has not moved.

## Findings retained; release scope

**B1 — CLOSED.** Reviewer personally observed original PDF diagrams, wording and choices for all twelve source anchors, verified original PDF SHA-256 hashes and held independent page artifacts. No material source transcription mismatch was found in the scoped source map.

**B2 — CLOSED.** Reviewer-owned, exact-tree hosted execution passed direct released APIs, source-derived SI comparisons, three nontrivial signed/translated systems, true centered/off-center cavity tests, and strict unsupported-boundary refusals. This does not certify an arbitrary 3D conductor solver or all twelve original answers.

**F3 — ADVISORY, INHERITED / NOT FIXED:** Prior Chromium no-JS/mobile inspection found that p2, p26 and p27 offline viewers lose parts of diagram/results without sufficiently obvious JavaScript-disabled notice or static alternative. This is not a new PR109 production-code regression; follow [issue #111](https://github.com/physicsvigilante/conductor_sim/issues/111) to correct or explicitly decide required no-JS coverage.

**F4 — ADVISORY, INHERITED / NOT FIXED:** Existing p26 viewer title uses "JEE original p26" when the actual source is **Notes Illustration 1**, not a proven official JEE exam item. Correct attribution separately in [issue #111](https://github.com/physicsvigilante/conductor_sim/issues/111), preserving the original symbolic solid sphere.

**F5 — SOURCE/FUNCTIONAL BOUNDARY, NOT A DEFECT IN THIS EVIDENCE PR:** Source p11 local irregular 3D response is unsupported with exterior q; source p70 full local 3D geometry is underdetermined. Workbook p16 original switched-oil-drop dynamics remain partial, and p8 static snapshots are not a substitute for signed current until the derivative law is invoked. Neither reviewer evidence nor earlier partial teacher demonstrations may be promoted to full original answers.

**Frozen cohort accounting unchanged:** **12** cases, historical route split **8 supported_scoped / 2 partial / 2 unsupported** and **zero independently certified complete original answers**. All seven official evaluation axes remain marked **not_evaluated** in the unchanged production cohort JSON. This review closes specific B1/B2 *evidence gates*, not that formal performance ledger.

### Verdict and guarded release restriction

**PASS (B1+B2 independently closed, no material counterexample found).** Approval is specifically for this **pinned, evidence-only PR #109 review scope** and is **not merge authorization**. Keep PR #109 **DRAFT and UNMERGED** until a separate explicit owner decision, an exact reviewed-head guarded merge, a verified reviewed native Git tree on main, and genuine post-merge CI. PR #105 remains a **separate draft/unmerged** gate. Source PDFs and production solver files were not changed.

This reviewer wrote only to a **separate reviewer-owned review_sandbox branch/PR**. No conductor_sim branches, tests, issues, pull requests, review threads or Git data were modified by this review.
