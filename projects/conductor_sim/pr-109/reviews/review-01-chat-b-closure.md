# Independent review #01 — closure addendum for conductor_sim PR #109

**Final scoped verdict: PASS.** 20 November 2026. This is a separate follow-up to the earlier [CHANGES REQUESTED report](review-01-chat-b.md), retained intact as historical evidence. **PASS is not approval to merge.**

## Immutable production identity and review scope

- Production PR: https://github.com/physicsvigilante/conductor_sim/pull/109 — draft/open/unmerged at inspection.
- Literal source HEAD: `975e2e23a86fe29bbaafebc20e684312d2aa5b6d`.
- Native source tree: `ddcc0b9923584495f78e2ea05a7f1ff56622e8d2`.
- Released main base: `337001f2e0d1ce62c87fa4352993c4a074cfbde6`.
- The 14 changed production files are newly added evaluation documents/probes/tests only; production physical solvers, original PDFs, original coverage matrix and historical evidence are unchanged. Separate M40c PR #105 remains draft/unmerged.
- Exact reviewed-head CI: **21/21 workflows and 24/24 check runs completed success**, including Python 3.10 and 3.12, true FEMM and browsers. Older `5dfecc80...` three failed workflow runs remain visibly failed.

## Former blocker B1 closed — independent original PDF byte hashes and printed-page inspections

Used a **reviewer-only, read-only source acquisition workflow** in `review_sandbox`: [run #44716381297](https://github.com/physicsvigilante/review_sandbox/actions/runs/44716381297), reviewer commit `fe9ebf7a969398602e7332530a97bb33af4cb6cd`. The workflow checked out the literal HEAD and verified Git HEAD/tree before exporting original bytes and all 12 requested printed PDF page images.

**Reviewer independently re-hashed the downloaded raw original PDFs in a local extracted source snapshot. Both matched:**

- `02_conductors_half_size.pdf`: SHA256 `9dff3c02a9f1848d2c3d99cb1a6e7a44dc7f5a51f7a3a2b8cc92d10ce1fbca5d` (17 pages).
- `POTENTIAL_CONDUCTORS1.pdf`: SHA256 `8d0d9b5cf821219058cfc4b7685a39b777e460944df44c3f9cffcb68157a60e5` (71 pages).

**All twelve actual printed pages independently examined visually**, not by accepting developer notes or OCR as source truth. Independent visual checks and interpretation are:

| Original case | Printed-page facts/figure inspected | Independently established bound |
| --- | --- | --- |
| Workbook p1 Q8 | Electron A→B diagonal 5 m with 3 m transverse; uniform +x E=10 V/m; asks work done **by us** | External +40 eV, **choice (2)**; field work −40 eV; endpoint work only, no free trajectory |
| Workbook p2 Q19 | Electron at 100 eV toward negative `−2.0 µC/m²` **metal** plate; asks just-fail distance | One-sided metal `|sigma|/eps0`, stop 0.442709 mm; printed **0.44 mm choice (1)**; source does not specify initial preview clearance |
| Workbook p3 Q27 | **SOLID** conducting sphere radius 10 cm, charge +20 µC inside uncharged thin shell radius 20 cm, wire connection | Ideal static energy decrease 8.987552 J, printed **9 J choice (2)**; no source current/time waveform; 1µm shell thickness is teacher model |
| Workbook p7 Multiple Q13 | Neutral metal with spherical outside, off-center internal q and non-spherical-looking inner cavity; outside P | Inner total −q, outer +q; outer face uniform absent exterior sources; no inference of a uniquely spherical interior cavity |
| Workbook p8 Multiple Q21 | Positive charge approaches grounded sphere radius R at externally prescribed slow constant v; asks current direction/trend | Conventional sphere→ground current, increasing magnitude, source options **(1) and (3)**; no printed numerical q/R/v or free charged-source dynamics |
| Workbook p11 Linked Q28 | **Irregular outer conductor**, two cavities q1/q2 and additional **exterior q** | Gauss outer total `Q+q1+q2`; topology-only solver properly refuses local irregular exterior sigma with outside source; preserve unsupported full-local-response status |
| Workbook p12 Linked Q40 | Horizontal coaxial charged rings (+10 µC, −20 µC), radius 30 cm, centers 40 cm, upward transverse E=10⁵ N/C, probe +10 µC | Axial electric work 3.595021 J, **3.6 J choice (4)**; transverse field contributes zero work; Q41 is a linked separate ask, not counted as new case |
| Workbook p16 JEE Advanced 2020 numeric Q1 | Terminal-falling oil drop, switching a 200 V supply across 1 cm circular plates, radius 8×10⁻⁷ m, density 900 | Uniform-field final static balance gives ~6 electrons; terminal drag/fringe/switching transient not source-faithfully solved, remains partial; printed JEE Advanced 2020 attribution is present in workbook |
| Notes p26 Illustration 1 | **Conducting solid sphere** with symbolic R,Q; asks V(R/2), V(3R/2), contrasting nonconducting Illustration 2 on same page | `kQ/R` and `2kQ/(3R)`; older M36a 'shell' triage label stale; not an official exam paper |
| Notes p27 Illustration 4 | Central q plus two ideal concentric thin shells carrying q1,q2; A inside first, B between shells | `V_A=k(q/r+q1/a+q2/b)`, `V_B=k((q+q1)/r1+q2/b)`; finite-thickness signed teacher models clearly separate |
| Notes p69 Illustration 7 | Metal carries 3q, cavity +q central versus displaced in separate drawings | Inner −q centered uniform, shifted nonuniform; outer +4q uniform; separate static hypotheses, no invented charge trajectory |
| Notes p70 Illustration 9 | Three circular cavity cross-sections S1,S2,S3 and outer S4, q1 central and q2/q3 displaced. Separate Illustration 8 truly irregular | S1 −q1 uniform, S2/S3 −qi nonuniform, S4 sum uniform; exact local densities only for explicit 3D spherical **teacher instantiation**, not 2D drawing alone |

No original source problem was quietly recast as a different spherical geometry. No invented trajectory, E/V field, numeric source parameter, current waveform or independently certified count was introduced.

## Former blocker B2 closed — reviewer-owned local genuine native execution

Extracted exact pinned production checkout obtained from the same reviewer-only GitHub Actions artifact. Executed **independently authored** reviewer Python code against released public/native `conductor_sim` APIs, with its own Coulomb/Gauss/energy/Kelvin-image calculations as reference. No developer `jee12_*_probe.py` used as an answer oracle.

**18/18 distinct native witness cases PASS**, covering:

- Public prescribed uniform-field endpoint work (original p1).
- Actual M36b event solver stopping distance **and actual native stop time** (original p2).
- Native M36c before/after connected solid-and-shell field energies, plus unfamiliar signed charge/radius alternative (original p3).
- Three signed, translated/oblique, inward/outward M37b prescribed-grounded-sphere-current cases (original p8).
- Native two-ring endpoint field work retaining the orthogonal external field (p12).
- Three signed/translated actual `SolidSphere` `MixedRadialBackend` potential checks (notes p26).
- Three signed/translated `NestedShellBackend` four-face charge ledgers and finite-thickness potentials (notes p27).
- Native M39a Gauss total and **required unsupported local-sigma refusal** (p11).
- Two signed displaced-cavity spherical M40a local sigma cases against a separately evaluated real-charge-plus-Kelvin-image field (notes p69).
- Three-cavity, explicitly teacher-specified spherical M40a test with mixed signs, independent local sigma and uniform/nonuniform checks (notes p70).

**Additional exact-source focused test run:** `PYTHONPATH=src:. pytest -q tests/test_jee12_*.py --disable-warnings` → **11 passed**. The independently written source mathematics/provenance reference with three unfamiliar signed/translated examples also passed **with actual raw PDFs and original cohort loaded**.

Reviewer-owned scripts, exact byte-hash receipts, source images, native JSON results, focused pytest output, original reviewer math reference and browser logs are packaged in the **owner-facing closure evidence ZIP**. The full-resolution original source page captures and pinned complete source snapshot are in reviewer-only [workflow run #44716381297](https://github.com/physicsvigilante/review_sandbox/actions/runs/44716381297), artifact `conductor-pr109-independent-source-acceptance-fe9ebf7a969398602e7332530a97bb33af4cb6cd`. This workflow made **no production changes**.

## Original evidence integrity and browser findings

Re-read pinned `docs/jee12_evaluation_cohort.json`: exactly 12 original IDs in unchanged order; 8 historically *planned* `supported_scoped`, 2 partial, 2 unsupported; all seven `evaluation` fields for every original remain `not_evaluated`, all nested original-independent-review flags false, `reviewer_evidence=none`, and **zero newly certified original full-source answers**. A **scoped evidence-review PASS does not change that machine-readable evaluation status**. Historical M36a 24/30 is a routing plan, not an achieved original score.

Prior real M36b/M36c/M36e source-tree matching GitHub Actions HTML was opened in actual Chromium (mobile, desktop, JS enabled/disabled), with saved logs and screenshots for p2, p26, p27, plus p3 CI screenshot. JS-enabled viewer physics labels, signs, source-versus-teacher metadata and native values matched independently derived quantities. Do not present stored JSON as proof that arbitrarily edited HTML is cryptographically authenticated.

**Non-blocking inherited viewer advisories, not PR109 JEE-12 solver defects:**

- **F3 (moderate)**: no-JavaScript mobile state leaves some diagrams/results empty without a prominent `noscript` or static alternative. Fix in a separate viewer milestone, or explicitly document a JS-required product requirement. Do not advertise full no-JS physics accessibility now.
- **F4 (low)**: p26 existing HTML title says “Original JEE p26” even though the case is a teaching **notes illustration**, not an official paper. Improve copy separately.

## Decision and merge boundary

**PASS for PR109's narrowly defined original-source fidelity, honest evidence, and bounded physics audit**, after independent closure of original B1 (all printed pages/raw PDF digests) and B2 (local native APIs and signed teacher variants). This does **not** claim 12/12 original solved questions or open general irregular-conductor coverage. It does not reopen released M40a, M40b, or FEMM solver audits. It also does not waive separate owner merge approval.

**No merge and no production writes were performed.** Production PR109 and separate M40c PR105 remain draft/unmerged. Any future merge still requires explicit owner authorization, expected-HEAD/tree guard and postmerge successful main-push CI. The earlier CHANGES REQUESTED report is preserved unchanged as historic evidence.
