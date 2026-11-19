# Independent scientific correction review #03 — conductor_sim PR #100 (M40a B1-R)

**Verdict: scoped PASS for the reviewed exact source HEAD/TREE.** A fresh, reviewer-owned first-attempt GitHub Actions execution reproduced the four formerly failing near-wall oblique cases using separately authored 110-digit real-source-plus-Kelvin-image normal electric fields. The corrected production native evaluator and genuine v2 exports passed all numerical, authenticity-consistency and hostility checks. **NOT permission to merge**: owner approval and post-merge verification are separate gates.

## Source identity and change control

- Production: https://github.com/physicsvigilante/conductor_sim/pull/100 ; rechecked open, **DRAFT and UNMERGED** at the time of verdict.
- Exact native commit HEAD: **b2303a5bd424b2dff6f088c15691aa2ce2c5f3e2**.
- Exact native Git TREE: **ab41e066ca6d53809b27b142ae35105eaebbf032**.
- The first reviewer Actions run checked out this **literal commit SHA** and asserted both actual git rev-parse HEAD and git rev-parse HEAD^{tree}; both matched. Independently read GitHub native commit tree also matched.
- The source changes since previous review #02 (e4a64a580cf1a3eca93d4b7315ed1f4aa4ab585e) are **exactly these four modified files**: docs/m40a.md; src/conductor_sim/spherical_multicavity.py; tests/test_m40a_spherical_multicavity.py; tools/m40a_spherical_reference.py. The actual checkout checked this exact allowlist; no older Gauss, FEMM, Chromium, visual system, workbook PDF or charter changed.
- The reviewer runner recomputed and confirmed original frozen SHA256 identities: 02_conductors_half_size.pdf = **9dff3c02a9f1848d2c3d99cb1a6e7a44dc7f5a51f7a3a2b8cc92d10ce1fbca5d**; POTENTIAL_CONDUCTORS1.pdf = **8d0d9b5cf821219058cfc4b7685a39b777e460944df44c3f9cffcb68157a60e5**; docs/m40a_charter.md = **b9da8056206f0c3026edee543712ff7fca070f535e11f95d89eb1beea4e7fdf3**.
- Final-head developer CI independently enumerated from GitHub: **24/24 workflow runs SUCCESS**, **29/29 check runs SUCCESS**, all bound to this identical HEAD. This includes both Python 3.10/3.12 native suites and inherited actual FEMM/browser checks. Developer results are prerequisites, not substituted scientific evidence.

## Fresh scientific method (not the native Poisson kernel or bundled oracle)

The source of truth for each independent physical expected density was the reviewer-authored script: [review-03-chat-b-probes.py](./review-03-chat-b-probes.py). Every raw binary64-encoded ray component and every absolute source/cavity coordinate is converted separately to Decimal and the physical unit direction is recovered with **110 decimal digits**. The cavity wall is x=a*n.

For a real point charge q at displacement u from the cavity center, d=|u|, the exact Kelvin image has charge q_image=-q*a/d and location u_image=a²*u/d². The separate normal electric-field projection gives:

**sigma = -(1/(4 pi)) [ q n·(x-u)/|x-u|³ + q_image n·(x-u_image)/|x-u_image|³ ].**

The reviewer computes this *electric field* expectation without importing the production local sigma function, the production Poisson/Kelvin density branch, or the bundled record checker. Only after independently computing expected numbers does the reviewer call native physics and use the bundled verifier to test *export consistency and refusals*. A display-normal field is not substituted for the real raw ray. The comparison limit for the new probes is **5e-11 relative**, deliberately stricter than the prior 2e-10 tolerance, except for the radial analytic pole (1e-12). All tested nonzero values had correctly signed densities.

## Original radial B1: PASS

Actual cavity radius 0.85m, source q=+3.1e-9 C, radial position a*(1-1.2e-8) on +x; query both (1,0,0) and raw (1+9e-13,0,0). Both produce **-4742217.655739458 C/m²**, equal to the separately evaluated real+image normal field; double-precision analytic pole formula -q*(a+d)/(4*pi*a*(a-d)²) gives **-4742217.655739457**. Same-direction exact and near-unit are exactly equal in native output. Export retains the raw x coordinate and produces display unit normal (1,0,0). Grounded exterior sigma = exactly zero.

## All four original reviewer #02 oblique failures: FIXED, PASS

Exact b directions and source positions follow review #02, radius 0.85m and fractional wall gap 1.2e-8. Query w=normalize_binary64(b+(5e-9,-2.5e-9,1e-9)), raw n=w*(1+9e-13). Grounded charge is +3.1e-9 C; isolated charge is -2.4e-9 C with fixed net metal charge +1.1e-9 C.

| Case | Independent real+image C/m² | Actual native C/m² | Relative error | Original #02 erroneous native C/m² |
|---|---:|---:|---:|---:|
| b=(0.6,0.8,0), grounded | -3532142.26790142 | -3532142.26790142 | 0 | -3532142.2752839886 |
| b=(0.6,0.8,0), isolated | +2734561.7557946476 | +2734561.7557946476 | 0 | +2734561.761510185 |
| b=(0.48,-0.64,0.6), grounded | -4242770.360599676 | -4242770.360599676 | 0 | -4242770.356589729 |
| b=(0.48,-0.64,0.6), isolated | +3284725.440464265 | +3284725.440464265 | 0 | +3284725.43735979 |

The original-bug densities remain measurably outside the declared 2e-10 limit and all four are rejected as false v2 evidence. The four genuine native v2 records preserve original **input_direction** exactly, independently reproduce **unit_normal** for display, and contain physically correct signed density for that original raw direction. The isolated outer Gauss face has the appropriate uniform signed charge; the grounded outer sigma stays zero.

## New unfamiliar near-wall case and ordinary controls: PASS

- Novel 3D source center (0.231,-0.417,0.119)m, independent basis normalize_binary64((0.227,-0.517,0.826)), fractional gap 1.6e-8, signed source -1.9e-9 C, grounded metal, outer radius 5m. With translated absolute source (0.4238445397841787,-0.8562098108740985,0.8207162548974957)m and oblique raw direction (0.22687592917029417,-0.5167174290407139,0.8255485517460923), reviewer physical real+image sigma and actual native value both equal **+1323522.2686654583 C/m²**, relative error zero at displayed double precision. Native v2 evidence passes.
- Exactly centered source: independent -2.202836582586787e-10 versus actual -2.2028365825867878e-10 C/m², relative 3.53e-16.
- Very-near center displacement 1e-250m: exact at displayed double precision, **-2.202836582586787e-10 C/m²**; no image-position overflow.
- Ordinary off-center/non-near-wall source (0.17,0.08,-0.03)m: exact at displayed double precision, **-2.028458743894825e-10 C/m²**.
- Two noncoincident opposite charges with exactly neutral net cavity source charge: *nonzero* local induced sigma **+2.783016365624333e-10 C/m²** versus independent **+2.7830163656243344e-10**, relative 5.58e-16. No false uniform-neutral conclusion.

## v2 provenance/integrity and refusal tests: PASS

**10/10** genuine independently examined exported v2 record checks passed. **87/87** reviewer-executed hostile refusals passed, with **zero** scientific failures. For *each* of four old oblique fixtures the verifier rejected the old prematurely-normalized density, reversed sign, false zero, inconsistent display normal, altered raw ray **even with correctly updated display**, swapped coordinates **even with correctly updated display**, Boolean raw coordinate, wrong source identity, wrong surface ID, false C/m² units, bogus provenance, false newly solved original JEE claim, invented local field/potential/force/current or temporal claims, and schema v1 mislabeling. The altered/raw and swapped failures were caused by a physically different independently recalculated density, not merely a display-vector consistency guard.

Additional native-hostile checks refused normals whose length deviated by >1e-12, the zero ray, Boolean/NaN/infinite components, invalid source-wall separations at and inside 1e-8 relative clearance, subqualified/tremendous signed source charges, near-cancellation posing as exact zero, and unsupported local E, V, force and current calls.

**Important evidence limitation:** the standalone v2 witness mathematically checks *internal consistency*, source identities, and authored role claims. It does **not cryptographically authenticate** a completely rewritten and otherwise self-consistent third-party JSON record to its historical teacher input; that still requires a trusted external anchor. The code and report do not claim such historical authentication.

## Actual first-run evidence, preservation and verdict

- Reviewer-owned first-attempt workflow: https://github.com/physicsvigilante/review_sandbox/actions/runs/44559876035 — **SUCCESS**, native source pin/checkout, Git TREE, changed-file allowlist and frozen hashes, candidate install, fresh numerical/hostility execution and artifact upload all passed on **Python 3.12**. No silent retry or artificial tolerance change.
- First-attempt original artifact **14549175519**: https://github.com/physicsvigilante/review_sandbox/actions/runs/44559876035/artifacts/14549175519 (full reviewer-run numerical JSON, raw first-attempt log, native HEAD/TREE, limited diff, frozen SHA hashes, reviewer script and evidence hashes).
- Reviewer-owned workflow: [m40a-pr100-review03-independent.yml](../../../../.github/workflows/m40a-pr100-review03-independent.yml) (canonical path is repository .github/workflows/m40a-pr100-review03-independent.yml). Reviewer-owned script: [review-03-chat-b-probes.py](./review-03-chat-b-probes.py).
- Actual first-run summary: **11 numerical scenarios, 10 genuine accepted record checks, 87 hostile refusals, 0 failures**. Numerical errors in the 11 independently compared cases were either exactly zero at binary64 output precision or at most 5.58e-16; all well within the preregistered reviewer threshold.
- Original [review #01 PR #23](https://github.com/physicsvigilante/review_sandbox/pull/23) and [review #02 PR #24](https://github.com/physicsvigilante/review_sandbox/pull/24) remain CHANGES REQUESTED, including the historical deliberately red science [run #44549264045](https://github.com/physicsvigilante/review_sandbox/actions/runs/44549264045); these original documents, first-attempt failure artifacts and their conclusions are **not altered**. Their previously verified six-cavity and Gauss surface integrals and legacy FEMM/browser evidence were reused, not needlessly re-executed.

**Final verdict: SCOPED PASS.** The earlier B1-R raw-direction Kelvin precision and versioned v2 evidence-integrity blockers are corrected at the **exact literal HEAD/TREE** pinned above. The corrected numerical evaluation preserves the original admitted near-unit direction rather than sampling a distinct rounded direction. There is no evidence here for unqualified arbitrary irregular-cavity 3D field/potential solutions or newly solved original JEE workbook items.

**Release control:** Production PR #100 must remain **DRAFT and UNMERGED** until a **separate explicit owner merge approval**. If approval is given, use an expected-HEAD guard, confirm the native Git TREE that lands on main matches this reviewed TREE, and demand actual complete successful post-merge push CI. Do not auto-merge. Any future change to the production reviewed source SHA or TREE invalidates this exact-source PASS.
