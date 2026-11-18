# M36d PR #87 — independent Chat B scientific R2 review #01

**Reviewer:** fresh separate-context GPT-6 scientific reviewer, not the production author  
**Review date:** 2026-11-18  
**VERDICT: PASS — BOUNDED SCIENTIFIC R2 for the EXACT pinned candidate only.**

This PASS is for the genuine standalone solid-conducting-sphere electrostatics, the specific original JEE p26 Illustration 1 source demonstration, and two separately declared teacher hypothetical worlds. It is **not** a production release authorization, not proof of automatic PDF-to-model generation, and not evidence for any full JEE-30 solved percentage. The sole original exam apparatus count remains **one**. The source PR MUST remain DRAFT/UNMERGED pending separate explicit owner permission.

## 1. Exact source identity, correction and CI

| Gate | Independent observation |
|---|---|
| Production PR | [conductor_sim #87](https://github.com/physicsvigilante/conductor_sim/pull/87), OPEN / DRAFT / UNMERGED |
| **Production candidate HEAD** | **e5fa85abe990abe8fdedc555e9313ac0420a56a7** |
| **Native git TREE** | **523d02e95dbb4791acd630f9c535eb552262c606** |
| Released main/base M36c | 6e6f53aa6762c327f58ef709379c41b1477c0931 |
| Old failed candidate HEAD | d607d1b9564c5b45e99a19cac3b33adcb33852f9 (NOT APPROVED) |
| Notes PDF SHA-256 | 8d0d9b5cf821219058cfc4b7685a39b777e460944df44c3f9cffcb68157a60e5 |
| Workbook PDF SHA-256 | 9dff3c02a9f1848d2c3d99cb1a6e7a44dc7f5a51f7a3a2b8cc92d10ce1fbca5d |

I fetched live GitHub PR metadata and the actual git commit-tree object, and a distinct reviewer-owned GitHub Actions checkout **asserted the literal SHA and Git TREE** with git rev-parse. That checkout independently SHA-256 verified both original PDF files. Rechecked production HEAD immediately before publishing: unchanged, PR open/draft/unmerged.

**Full exact-HEAD CI: 19 of 19 workflows COMPLETED SUCCESS**, individually verified, not inferred from stale branch runs. Particularly: [Python #44273099186](https://github.com/physicsvigilante/conductor_sim/actions/runs/44273099186) has independently completed Python **3.10 and 3.12** jobs; [genuine FEMM5 #44273099267](https://github.com/physicsvigilante/conductor_sim/actions/runs/44273099267) passed; [historical browser #44273098959](https://github.com/physicsvigilante/conductor_sim/actions/runs/44273098959) completed its **73 workflow steps**; [M21d #44273099004](https://github.com/physicsvigilante/conductor_sim/actions/runs/44273099004), [M36b #44273099224](https://github.com/physicsvigilante/conductor_sim/actions/runs/44273099224), [M36c #44273099078](https://github.com/physicsvigilante/conductor_sim/actions/runs/44273099078), and [M36d source/native/Chromium #44273099112](https://github.com/physicsvigilante/conductor_sim/actions/runs/44273099112) all passed the literal current HEAD. These developer-controlled workflows are necessary supporting evidence, **not** my substitute for original tests.

The actual corrective commit diff between old d607d1b... and reviewed e5fa85a... changes **one file only: tests/test_m14b_mixed_radial.py**. It removes the formerly required rejection of an isolated single SolidSphere, replacing it with new positive admission and no-fictitious-inner-face checks. The original point-source, two-solid, overlapping-shell and eccentric-shell refusal cases remain in the same test. No production physics source, PDF, renderer or M6 benchmark was changed by this correction.

**Preserved real negative history:** old [M21d #44272283613](https://github.com/physicsvigilante/conductor_sim/actions/runs/44272283613) was FAILURE (99 passed / 1 failed). Old [Python #44271994213](https://github.com/physicsvigilante/conductor_sim/actions/runs/44271994213) had 2172 passed / 1 failed (paired 3.10 job cancelled), caused by the old single-solid refusal expectation. They are not misrepresented as green.

## 2. Reviewer-owned ORIGINAL execution, evidence identity and first failure

My separate review_sandbox branch contains an independently written [probe](https://github.com/physicsvigilante/review_sandbox/blob/review/conductor-m36d-chatb-r2-01/projects/conductor_sim/pr-87/reviews/independent_probe_chat_b_01.py) and [pin-locked workflow](https://github.com/physicsvigilante/review_sandbox/blob/review/conductor-m36d-chatb-r2-01/.github/workflows/reviewer-conductor-m36d-chat-b-01.yml). The reviewer workflow checked out the exact production commit detached; **it did not run against a floating production branch, modify source files, merge a PR or mark anything ready**.

[Successful original scientific run #44275567819](https://github.com/physicsvigilante/review_sandbox/actions/runs/44275567819): **four unfamiliar real public-backend native models**, **six actual denied-domain refusals**, **21 hostile changes to a freshly generated detached source manifest all rejected**, **three actual offline Chromium source/teacher frames**, plus original p26 PDF rendering and SHA checks. The script preserved real native numerical values and independently computed Gauss predictions rather than making fixtures with expected numbers.

[Independent artifact #14415210035](https://github.com/physicsvigilante/review_sandbox/actions/runs/44275567819/artifacts/14415210035) contains novel numerical observations, logs, all 21 rejection reasons, source identity, real PDF p26 image, three viewer screenshots and hashes. GitHub-provider ZIP SHA-256: **6e2e8c554caf7427590d9310112d77bb234ca1cd6aeacc16fccef71564b52cea**. I **actually downloaded the ZIP**, independently recomputed exactly the same SHA-256, extracted its contents, read numerical JSON/rejection messages and personally viewed all four PNGs (original p26 page and three browser frames). This evidence is a separate reviewer-designed test, **not an independent human laboratory measurement**.

**First reviewer attempt preserved as failure:** [#44275293725](https://github.com/physicsvigilante/review_sandbox/actions/runs/44275293725) stopped at the corrective-diff inspection after the exact SHA, TREE and PDF checks passed, because my checkout used the default one-commit shallow history; predecessor d607d1b... was absent locally. This was a **reviewer workflow setup defect**, not production physics failure. I changed only the review workflow checkout depth to 2 and reran cleanly; the second attempt above passed. The first failed attempt and its artifact remain visible.

## 3. Original printed p26 image — scientifically accurate source interpretation

I independently viewed the freshly rasterized **physical page 26** from the byte-verified original POTENTIAL_CONDUCTORS1.pdf. **Illustration 1 reads “A conducting sphere of radius R has charge Q”** and requests **V(R/2)** and **V(3R/2)**. Its printed solution explicitly gives the conducting interior potential **kQ/R** and exterior potential at 3R/2 **2kQ/(3R)**. It does **not** supply numeric Q, R or a specific nonzero world center; those values in the software are teacher choices. Illustration 2 immediately below is a *different* nonconducting uniformly charged sphere, which must not be conflated with Illustration 1.

**Source-wording qualification (important):** p26 Illustration 1 is text and equations; it does **not itself depict a filled cross-sectional disk or explicitly spell the word “solid”**. It specifies an ordinary conducting sphere with no cavity or shell arrangement; taking it to be a genuine solid spherical conductor is a physically consistent, useful realization. However, a statement that the printed Illustration 1 literally *draws a solid disk* would overstate the source. The viewer demonstrably draws a solid disk; that viewer image is not a reproduced source illustration.

The actual M36d source example is **one** standalone real SolidSphere, R=0.10 m, Q=+1.0 nC, with stable physical name **Sphere A**. In freshly generated native output, I verified **V(R/2)=89.8755179226 V**, **V(3R/2)=59.9170119484 V**, **E(center)=E(R/2)=0**, and **uniform outer sigma=+7.95774715459×10^-9 C/m²**. The signed revised teacher model genuinely recomputes R=.12 m, Q=−2 nC, shifted center=(.025,0,0): **V(R/2)=−149.792529871 V**, **V(3R/2)=−99.8616865807 V**, **E at +3R/2 in world x = −554.787147670 V/m**. The separately authored grounded world yields zero Q, V, E and sigma. Only the first is linked to the original question; the other two are teachers' hypothetical states.

## 4. Four fresh unfamiliar real native physical models — PASS

I used public ElectrostaticProblem, SolidSphere, FixedNetCharge, Grounded and MixedRadialBackend APIs, never copied developer sample numeric triples, and **derived expected V/E/sigma outside the backend** using k=1/(4π×8.8541878128×10^-12) SI. The probes include a tilted unit direction (2,−1,2)/3, its reverse, and a second oblique 3D direction. They compare signed **all three E components**, not just magnitude; V at center and multiple interior/exterior radii, zero internal E, three outer-surface directions, charge bookkeeping, exactly one physical boundary, refusal of the inner-face sigma request, and real surface-E refusal.

| Novel reviewer world (not developer's cases) | Real native metal potential | Independent outer sigma | Real signed 3D E at 2.35R along (2,−1,2)/3 |
|---|---:|---:|---|
| +3.7 nC, R=.073 m, c=(.170,−.090,.230) m | +455.533447005 V | +5.525176294×10^-8 C/m² | (+753.3043, −376.6521, +753.3043) V/m |
| −4.6 nC, R=.155 m, c=(−.065,.120,−.310) m | −266.727343512 V | −1.523647738×10^-8 C/m² | (−207.7346, +103.8673, −207.7346) V/m |
| Grounded, no sources, R=.065 m, c=(.410,−.200,.110) m | 0 V | 0 | (0,0,0) V/m |
| Isolated fixed zero charge, R=.215 m, c=(−.070,−.150,.090) m | 0 V | 0 | (0,0,0) V/m |

Every V, all signed E components, face charge and sigma matched independently calculated Gauss-law predictions to numerical tolerances. For the nonzero spheres the field at R has different one-sided limits: **SingularField** was actually raised instead of inventing a value at the boundary. A SolidSphere's inner_surface_charge_c=0 is **bookkeeping**, not an inner physical charge face; accessing inner sigma raised ValueError. This passes the requested substantive physical novelty test.

## 5. Six unsupported near-domain exclusions and historical regression — PASS

The actual backend **supports=False and solve raised UnsupportedProblem** for all six newly authored inadmissible arrangements:

1. Standalone SphericalShell (a hollow shell, not a solid).
2. Standalone real solid with one internal PointCharge.
3. Standalone real solid with one exterior PointCharge.
4. Two independent SolidSphere bodies.
5. True solid plus eccentric nonconcentric shell.
6. True solid plus intersecting/overlapping shell.

A **separate new valid M14b two-conductor test** also solved an R=.067m +1.3nC solid plus a concentric shell (.21/.25m, net −0.4nC), checking outer core +1.3nC, inner shell −1.3nC, outer shell +0.9nC and independent exact signed voltages. The historical M6 hollow benchmark is **not rewritten** (absent from PR changed-file list, retained production test passed). Existing M36b/c current-source workflow replays are green. This supports the narrow single-solid extension without a broad, untested new 3D solver claim.

## 6. Fresh detached scientific record forgery tests — PASS within tested contract

My independent script called the **actual production native p26 exporter** to freshly create native-solid-sphere.json and HTML, then passed its untouched manifest to the *stdlib-only, no-production-physics-import* m36d_solid_reference.check: **positive control PASS**.

I then independently deep-copied that real manifest, making **21** distinct hostile alterations, each rejected with a directly relevant assertion message. Attacks covered: forged p26 page; forged Illustration anchor; teacher sample falsely labelled original PDF numeric givens; inflated one-original-apparatus count; fictitious source time/current; fake Sphere A name; a supposedly hollow physical shape; nonzero geometric inner radius; hollow drawn ring; altered rendered name and radius; fake inner-surface charge; reversed outer charge; false negative-world net charge; flipped external signed field; wrong outer sigma; teacher/source roles and titles misattributed; grounded nonzero net charge; grounded called isolated; and invented per-state time axis.

**21/21 intentionally forged variants refused**, with the original unmodified detached dataset accepted. This is a valid **bounded detached-data semantic consistency check**, not cryptographic authenticity against a coordinated adversary who edits source/checker/HTML together.

## 7. Actually viewed original PDF raster and independent Chromium screenshots — PASS with UI caveats

My exact-HEAD reviewer workflow **actually opened offline Chromium** and saved first/source, revised negative/translated teacher, and grounded hypothetical full-page screenshots. I then downloaded and personally inspected those images.

- **Source frame:** clearly filled gray metal disk, one uniform **Sphere A / outer** density, outward signed field lines, positive equipotential palette; radius and +1nC identified as teacher examples. No hollow inner face or second charge profile.
- **Teacher negative frame:** visibly larger and laterally shifted filled disk, blue negative-potential palette, inward arrows, negative net and outer charge, conspicuous teacher-hypothetical label.
- **Teacher grounded frame:** smaller filled disk, zero conductor/net/outside field, no field-line traces, a zero-valued outer profile, and a clearly labelled grounded source-free hypothetical.
- Every frame was genuinely switched with the HTML slider, and the browser-observed embedded frame reports **inner_radius_m=0, one actual outer profile**, no extra point sources, and **mode=static**. All three images differ by SHA-256. Recorded **zero HTTP requests and zero JavaScript errors**. This is authentic browser evidence, not evidence of classroom comprehension.

**Nonblocking UI improvements:** visible white/blocky squares directly outside the circular boundary are sampled-grid rendering artifacts, not a physical cavity. The inherited label **“Induced surface-charge profile”** is less precise for a singly charged isolated sphere than **“Surface-charge density”**. More importantly, the original p26's two requested **V(R/2) and V(3R/2) values are in the validated native data, but are not prominently displayed together as source-specific answer readouts** in the screenshot; a future source-answer card should expose both. These are presentation refinements; they do not invalidate the current exact-solver/true-geometry objective. The central source explanation correctly says these are *precomputed static* states, not a charge-transport timeline.

## 8. Bounded decision and authority

| Gate | R2 outcome |
|---|---|
| Exact production SHA, Git TREE, unchanged PDFs and correction footprint | **PASS** |
| All 19/19 exact-HEAD CI, Python 3.10/3.12, real FEMM5, 73-step historical browser | **PASS** |
| Original printed p26 conducting-sphere formula and source/teacher provenance | **PASS**, note absence of literal printed filled-disk figure |
| Four independent unfamiliar real public-backend solid spheres, signed 3D Gauss tests | **PASS** |
| Boundary singularity, no phantom inner sigma, isolated vs grounded physics | **PASS** |
| Six invalid-domain refusals and independent familiar mixed-model regression | **PASS** |
| Fresh native manifest positive check and 21 targeted hostile refusals | **PASS** |
| Actual independently generated offline Chromium, viewed screenshots, visible true solid | **PASS**, minor display recommendations |
| Arbitrary 3D charge induction, multiple eccentric conductors, point-charge perturbation | **NOT QUALIFIED** |
| Moving charge, current, heating, dQ/dt, new original JEE exam count, automatic PDF parsing | **NOT CLAIMED / NOT TESTED** |

**FINAL VERDICT: BOUNDED PASS** for **e5fa85abe990abe8fdedc555e9313ac0420a56a7** / TREE **523d02e95dbb4791acd630f9c535eb552262c606** only. This is a genuine modest composable capability: an author can now arrange one independently charged/grounded **solid** sphere in previously supported uniform source-free electrostatics and obtain correct physical/visual output using the established solver and viewer, without inventing a new solver. Scope remains one original JEE illustration plus two teacher physical revisions.

**RELEASE AUTHORITY REMAINS CLOSED.** This review is NOT an owner instruction or authorization to merge. Chat A must request **separate explicit owner approval**, guard any eventual merge with expected_head_sha, independently verify that the reviewed exact Git TREE lands on main, and confirm actual **postmerge main-push workflow** success. A changed production HEAD invalidates this review pin.
