# M36c PR #86 — independent Chat B GPT-6 R2 review

**Reviewer:** Chat B, GPT-6, independent of the production implementation  
**Date:** 2026-11-18  
**VERDICT: CHANGES-REQUESTED. Production release is blocked by original-source fidelity and saved-observation attribution defects.**

The qualified analytical conductor calculations are substantially correct: three fresh out-of-sample native worlds and separate SI Gauss/Kelvin calculations passed. The verdict is not a numerical-solver FAIL. It addresses whether the project is actually replaying the original textbook questions, and whether saved scientific observations retain physically correct conductor, angle and source associations.

## Identity and current-head CI

| Item | Directly verified |
|---|---|
| Production | [conductor_sim PR #86](https://github.com/physicsvigilante/conductor_sim/pull/86), **open, DRAFT, unmerged** |
| HEAD | **1f5bd9fcee30f534e15f874c87f8ff0441a62fe8** |
| True native Git tree | **b31fd1843b57de5403d2a36b2cb86fa1385f659a** |
| Released M36b base | 5693aaa4fca42fa996fd0983b95c8a104a45af93 |
| Workbook original PDF SHA-256 | 9dff3c02a9f1848d2c3d99cb1a6e7a44dc7f5a51f7a3a2b8cc92d10ce1fbca5d |
| Notes original PDF SHA-256 | 8d0d9b5cf821219058cfc4b7685a39b777e460944df44c3f9cffcb68157a60e5 |

The GitHub commit-object tree was directly checked. My separate clean workflow asserted HEAD and TREE using Git, and recomputed the original PDF hashes. No production source code or PR state was modified.

**All 17/17 actual pull-request-triggered workflows on this exact HEAD were completed SUCCESS** at review time, including Python 3.10/3.12, dedicated actual FEMM5, historical Chromium/source checks, M36b and M36c source physics and browser. Representative current-head workflows: [Python](https://github.com/physicsvigilante/conductor_sim/actions/runs/44258179036), [real FEMM5](https://github.com/physicsvigilante/conductor_sim/actions/runs/44258178578), [historical visualization](https://github.com/physicsvigilante/conductor_sim/actions/runs/44258178924), [M36b](https://github.com/physicsvigilante/conductor_sim/actions/runs/44258178632), [M36c](https://github.com/physicsvigilante/conductor_sim/actions/runs/44258178778).

Retain the failed historical runs: [#44257593862](https://github.com/physicsvigilante/conductor_sim/actions/runs/44257593862) failed at the **older 320ffde... HEAD** due to an over-strict binary-float coordinate comparison; [#44257760238](https://github.com/physicsvigilante/conductor_sim/actions/runs/44257760238) failed at **older 51896c... HEAD** because of an incorrectly guessed viewer label. The fixed [#44257940761](https://github.com/physicsvigilante/conductor_sim/actions/runs/44257940761) succeeded on the reviewed HEAD. Old red runs are not erased or relabelled, and they are not current-head PR failures.

## What the independent reviewer ACTUALLY executed

[Chat B reviewer workflow #44260257949](https://github.com/physicsvigilante/review_sandbox/actions/runs/44260257949) completed **SUCCESS** using a clean, pinned checkout and [my separately authored Python probe](independent_probe_chat_b.py). Its evidence artifact is **14407947026** (chat-b-m36c-independent-conductor-science), and I downloaded and verified its ZIP SHA-256 **44e1f978c5d1c92e141ad2849d9a08418072a639aeb20ef871bec0750486edee**. The artifact contains independent-results.json, logged output, all original native replays, seven original PDF page images, and first/last independent Chromium screenshots.

**60 reviewer SI scalar/refusal check records** include these genuinely unfamiliar, LIVE public-backend experiments:

| New physical model, deliberately different from source fixtures | Separate Gauss/Kelvin SI result | Result |
|---|---|---|
| Floating connected solid sphere radius 0.12 m with **-3.7 nC**, shell radii 0.27/0.28 m initially **+0.8 nC** | Final exterior **-2.9 nC**, negative initial gap E, true signed before/after metal faces, zero final gap E, energy released **2.848138519 × 10⁻⁷ J** | **PASS** |
| Two nested shells 0.072–0.085 m / 0.17–0.19 m, net +2.1 nC/-0.4 nC, displaced cavity point **-1.25 nC** at z=0.029 m | First inner/outer faces **+1.25/+0.85 nC**, second inner/outer **-0.85/+0.45 nC**, Kelvin near/far **+7.5466136 × 10⁻⁸ / +5.8236244 × 10⁻⁹ C/m²** | **PASS** |
| Isolated neutral solid sphere radius 1.6 m, **-2.3 µC** external point at z=4.3 m | Kelvin image +0.85581395 µC, central image -0.85581395 µC, zero physical sphere net; surface potential **-4807.295145 V** | **PASS** |

**Actual public-engine refusals passed:** nonconcentric shells, intersecting conductor shells, point source placed within shell metal, point source placed inside solid metal. These do NOT establish arbitrary 3D cavity physics.

I independently derived the original seven manifest case values from SI laws, not developer-saved expected fields. Workbook p3 energy release is **8.98750685 J** with the stated finite shell (ideal zero thickness: **8.98755179 J**); linked workbook p10 shells carry ±**2.00277010 µC** and release **0.090124204 J**; workbook p14 outer potential remains **134.813277 V** under explicitly illustrative R=0.10 m, q=1 nC; notes p69 central/near/far sigma and signed face totals match Kelvin; workbook p9 neutral sphere potential is **1797.510358 V** and induced-only tangent potential **-449.377590 V**. All qualified numeric assertions passed.

## Original PDFs: I visually inspected the actual printed pages

The independent workflow rendered the exact GitHub source PDFs. I downloaded and actually viewed **workbook PDF pages 3, 9, 10, 14** and **notes PDF pages 26, 27, 69**, not just the M36a inventory text.

- **Workbook p3 Q27:** a genuine **solid conducting sphere**, 10 cm, +20 µC, inside a neutral thin 20 cm shell. The source replay retains the solid-versus-shell distinction, full radial gap/exterior energy, and correct near-9 J equilibrium release. Wire connection is two static states, not a heat-rate simulation.
- **Workbook p10 Q13/Q14:** correct original 10/20 cm, equal/opposite shells from Emax=1.8 million V/m. These are two question anchors describing **one physical apparatus**. The energy release is valid, but no current versus time is solved.
- **Workbook p14 Q7:** printed R, 2R, q, 2q are symbolic; the run's R=10 cm and q=1 nC are teacher choices. Unchanged exterior field/outer potential is correct.
- **Workbook p9 Q27:** neutral **solid** sphere, AB=4 m tangent, BC=3 m, +1 µC at A are real source givens. Kelvin potential and negative induced contribution are correct. The separate five-position sweep is teacher-authored static exploration.
- **Notes p69 Illustration 7:** centre versus displaced cavity charge, -q inner / +4q outer, uniform versus nonuniform density are faithful. The 4 cm shift is a disclosed teacher numeric choice.

### F-01 — BLOCKER: notes p27 Illustration 4 does not replay its printed question

[Original notes page 27, Illustration 4](https://github.com/physicsvigilante/conductor_sim/blob/1f5bd9fcee30f534e15f874c87f8ff0441a62fe8/POTENTIAL_CONDUCTORS1.pdf) draws a **central** point charge q inside two concentrically charged spherical shells q1 and q2, marks **A** in the innermost cavity and **B** in the intershell gap, and explicitly asks for **V(A) and V(B)**. The printed solution is V(A)=kq/r+kq1/a+kq2/b and V(B)=k(q+q1)/r1+kq2/b.

The native case **p27-cavity-two-shells** instead authors a point charge **off-centre at z=0.02 m**, and its four published native observations are the two shell net charges, induced inner face total, and first-shell potential. It **never specifies or measures V(A) or V(B)**. This is a valid extension to demonstrate cavity induction, but it is not the printed problem's numerical or symbolic solution; the central-charge formula does not generally apply to its displaced source.

**Required:** provide a central-source authored original A/B configuration and actual evaluated V(A), V(B) with independent printed-formula checks, keeping the off-centre variant separately and explicitly marked teacher extension. Alternatively downgrade this question to partial rather than counting it as a successful original-source apparatus. Do not replace the printed asked-for observable with convenient shell totals.

### F-02 — SOURCE-FIDELITY CORRECTION: notes p26 sphere portrayed as a hollow shell

[Original notes page 26, Illustration 1](https://github.com/physicsvigilante/conductor_sim/blob/1f5bd9fcee30f534e15f874c87f8ff0441a62fe8/POTENTIAL_CONDUCTORS1.pdf) asks for V(R/2) and V(3R/2) of a **conducting sphere**. The candidate authors a **SphericalShell with inner radius 0.09 m, outer radius 0.10 m** and labels its interior observation **'electric field in hollow interior'**. The printed apparatus does not specify a hollow inner cavity. The sampled potentials happen to match the conducting sphere because both have constant potential inside a charge-free interior, but the visible metal geometry is different.

**Required:** model the source sphere as solid if feasible, or clearly disclose the hollow shell as a mathematically equivalent **proxy for these specific sampled V/E observables**, not a literal original shape. Avoid teaching the source as a sphere with a real cavity.

## Independent saved-evidence falsifications

I altered the **real exported native-conductors.json** and independently called the detached source reference verifier. **12 hostile physical/coverage forgeries were correctly REJECTED**, including a shell inner/outer face swap that preserves net charge, reversed signed gap E, fabricated pre/post field energies, wrong outer V, flattened shifted Kelvin density, a falsely charged neutral sphere, p3 shape replacement, splitting one p10 system into two successes, false wire-current time, and fake p8 induced-current or p70 local 3D success.

### F-03 — BLOCKER: saved observation angle/conductor/source metadata can be forged

**Three further adversarial mutations were ACCEPTED as valid by the source-free reference checker:**

1. Swap p69 density observations' **near theta=0** and **far theta=π** while keeping all saved density magnitudes unchanged. The checker passes, even though the strong near-side density is falsely attributed to the far side.
2. Reassign the p27 **inner-shell voltage** observation's conductor field to **'outer'** while retaining the inner-shell numeric value. The checker passes, even though first and second shell potentials are different.
3. Replace p27 **source_anchor='Illustration 4'** by **'Completely different source'**. The checker passes.

This follows directly from [source-free reference notes-row checks, lines 195–205](https://github.com/physicsvigilante/conductor_sim/blob/1f5bd9fcee30f534e15f874c87f8ff0441a62fe8/tools/m36c_jee_conductor_reference.py#L195-L205): kind, state index, optional physical point, and observed numerical value are checked, but **theta_rad, conductor attribution, and source_anchor are not checked**. The [native producer, lines 114–138](https://github.com/physicsvigilante/conductor_sim/blob/1f5bd9fcee30f534e15f874c87f8ff0441a62fe8/tools/m36c_jee_conductor_replay.py#L114-L138) emits those meaningful fields.

**Required:** verify the expected angle, named conductor and source-anchor association using separate fixed source contracts, and add hostile regression tests that must reject these exact forgeries even when the numerical magnitudes remain unchanged. A correct number attributed to the wrong conductor or angle is not physically correct evidence.

## Chromium screenshots and pedagogical interpretation

I downloaded and SHA-verified developer artifact **14407485227** (SHA-256 **ea59a43cda5f4f690c39a5d94044a8a915ca074df36e954c565d12eb2462e442**) and visually inspected all seven original first-frame screenshots. My own clean workflow opened actual generated offline HTML in **Chromium**, used the stored-frame slider on **p3, p69 and p9**, and preserved first/last screenshots. I visually inspected the **p3 after-wire** and **p69 shifted-source** images: the former shows zero core charge and outer-shell +20,000 nC, the latter shifts the source with a strong near-side induced density curve. No external network requests or JS page errors were seen in these independent three viewer interactions.

The viewer is genuinely useful for potential contours, field lines, signed face totals and sigma curves, but some rasterized potential fills near circular surfaces appear blocky/polygonal, and source case IDs and teacher choices are less conspicuous than the textbook questions. These are **nonblocking usability cautions**, not established numeric defects. I did not perform student comprehension testing.

**Static means static:** connected-shell frame changes are two equilibria, not a current waveform; p69 is two alternative charge placements; p9's position sweep is teacher-chosen quasi-static exploration, not physical elapsed motion. No finite conductivity, heat rate, p8 approach-time dQ/dt, or p70 nonconcentric three-cavity 3D local surface field is supported.

## Separate axis scores

| Dimension | Reviewer determination |
|---|---|
| Original source interpretation | **CHANGES REQUIRED** — p27 original V(A), V(B) missing and central charge relocated; p26 hollow proxy not disclosed as source substitution |
| Qualified numerical conductor electrostatics | **PASS** for tested public analytical families and sampled SI observables |
| Genuine static observation coverage | **PARTIAL as original textbook completion** — seven selected source-inspired physical arrangements, eight historical question anchors, p27 is not yet original-question-complete |
| Saved evidence integrity | **CHANGES REQUIRED** — 12 physical controls rejected, three real angular/conductor/source-attribution forgeries accepted |
| Viewer technical functioning | **PASS with readability cautions** — actual real Chromium and visible alternate static frames |
| Optional textbook answer completion | **NOT ESTABLISHED**; no 7/30, 8/30, 14/30, 24/30 or other extrapolated JEE success percentage |

**Final release decision: CHANGES-REQUESTED; DO NOT MERGE OR MARK PRODUCTION PR #86 READY.** Resolve F-01 and F-03, correct or conspicuously disclose F-02, preserve old failed attempts and original PDF hashes, and requalify the resulting changed source with new exact-HEAD/TREE CI plus fresh independent R2 review. Any changed source SHA makes this review's pin stale. Separate explicit **owner authorization**, expected-head guarded merge and successful **all main-push workflows** remain required after a no-blocker review. This review is scientific evidence, not owner release permission.
