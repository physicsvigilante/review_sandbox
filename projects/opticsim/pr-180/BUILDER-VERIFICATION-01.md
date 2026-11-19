# Opticsim PR #180 — exact-source builder verification and one-review handoff

**2026-11-19. Builder verification only. Independent physics/integration review PENDING. PR #180 is DRAFT, UNMERGED; production `main` is unchanged by this candidate.** This is not an independent model assessment, a blind JEE evaluation, a fully solved original JEE question or owner merge approval.

**Target:** [Opticsim PR #180](https://github.com/physicsvigilante/opticsim/pull/180). This is the **only review target** for the consolidated v24 public curved-entry authoring and real native evidence. Do not split it into separate reviews for research, native, UI or integration.

## 1. Exact identity — primary Git objects independently re-read

| Object | Verified SHA |
|---|---|
| Final candidate HEAD | `635fc28d48d4ebf5408ce5a45988b7831da6a81b` |
| Final candidate Git tree | **`cca59685effa922182111b875187dcd6c999edb2`** |
| Production `main`, no PR180 merge | `bbcc94a51865da8ccbf4fdfe79ecf6449b3b9d93` |
| GitHub synthetic PR merge | `b638b9c77e58c0fba05c3d165c8b4f4d7a0a3972` |
| Synthetic merge tree | **`cca59685effa922182111b875187dcd6c999edb2`** — identical |
| Synthetic merge parents | `[bbcc94a51865da8ccbf4fdfe79ecf6449b3b9d93, 635fc28d48d4ebf5408ce5a45988b7831da6a81b]` |
| Pinned native PhyDemo | `811f508d2b070898c241a568b0c167dcb8645251` (unchanged) |

[Source commit Git object](https://api.github.com/repos/physicsvigilante/opticsim/git/commits/635fc28d48d4ebf5408ce5a45988b7831da6a81b) and [synthetic merge Git object](https://api.github.com/repos/physicsvigilante/opticsim/git/commits/b638b9c77e58c0fba05c3d165c8b4f4d7a0a3972) were **read separately**. Equality is established by Git-object reads; do **not** attribute a separate tree-identity assertion to CI. The optical job checked out the synthetic PR merge.

The [actual diff from current `main` to the synthetic tested tree](https://github.com/physicsvigilante/opticsim/compare/bbcc94a51865da8ccbf4fdfe79ecf6449b3b9d93...b638b9c77e58c0fba05c3d165c8b4f4d7a0a3972) is **14 paths: seven added, seven modified, none deleted**. All six separate CI files copied from merged infrastructure PR #181 are byte-identical to main, and the pinned real-Chrome unified workflow is preserved. Only the optical CI workflow receives **two new required v24 acceptance steps and two evidence paths**. Existing PhyDemo/vendor code, historical stored problem attempts and frozen JEE source policy remain untouched.

## 2. What actually changes in the engine

Existing native `SingleRay`, `Glass`, `Detector` and `Blocker` do all physical propagation. The new **schema v24** `native-curved-entry-observation-tracing` is a conservative authoring composition of those already supported primitives. It permits exactly one externally originating, right-to-left, slightly off-axis native single ray, one right-hand **semicircular closed Glass** region with lower exterior than interior index, **two independent passive detectors inside the glass** and **one fully opaque native blocker inside** the glass, after the detectors but before the genuine flat back boundary.

The curved entrance is the true circular `face-arc`; `face-flat` is still a real part of the native closed region. No open refracting surface is substituted. The source, material index, finite radius, detector positions, screen, approximation policy and measurement requests are explicit. The validator checks finite geometry and clearances but never computes/steers a refracted ray or assigns the encounter sequence. Every actual hit is decided by unmodified pinned PhyDemo.

Bounded admission: radius 50–1000 mm, two absolute indices [1,4] with `insideIndex > outsideIndex`, `partialReflection=false` explicitly omits non-TIR Fresnel branches; horizontal single ray `±180°`, source in a narrow `±0.08R` central strip, fully internal vertical detectors at 0.55R–0.9R and absorber at 0.2R–0.5R, minimum endpoint/boundary and axial spacing. The real retained flat side can be hit if the blocker is removed from a **research-only** raw fixture; such a run is not mislabelled a single-entrance witness. The public authoring contract requires the blocker.

**No new physical image detector, standalone sphere surface, 3D observer, continuous irradiance, diffraction or symbolic J15 solution exists here.** Native two-detector coordinates can be mathematically extended to the axis, but this extension is not a native ray or detected image. The new v24 `src/app.js` exposes only the correct `single-ray` source mode and labels the actual apparatus, rather than offering incompatible point-source modes or falsely labelling the scene as an ideal-lens model.

Native v21 Beam/semicircle, v23 Beam/full CircleGlass and all older saved schemas stay separately versioned; the historical 24 composition profiles are preserved and one additional v24 profile is admitted. No original JEE image is inferred from the new teaching controls.

## 3. Native and browser CI at the exact final tree

All **11/11 exact-head GitHub PR workflows succeeded**, with zero failed runs. [Optical composition run 44559774415](https://github.com/physicsvigilante/opticsim/actions/runs/44559774415), [job 135685548055](https://github.com/physicsvigilante/opticsim/actions/runs/44559774415/job/135685548055): **953/953 Node tests passed, zero failed/skipped.**

The new [public acceptance](https://github.com/physicsvigilante/opticsim/blob/635fc28d48d4ebf5408ce5a45988b7831da6a81b/scripts/jee-curved-entry-acceptance.mjs) completed **11 source-byte-bound cases**: **four** distinct actual full native runs, and **seven** strict refusals before native execution with **zero native calls**. Baseline requests obtain 1 actual emission, 1 native `face-arc` event, 0 `face-flat` events, 1 crossing at each internal detector, 1 real native blocker absorption, and no image claim. Signed height, translation and independent scale variations retrace actual native systems. Missing exterior index, source wrong-way direction, absent/overlapping absorber, out-of-region detector, Fresnel-on and extra glass refuse rather than silently repairing apparatus.

Existing public native v19–v23 and dedicated Chrome checks passed. New [v24 real-Chrome test](https://github.com/physicsvigilante/opticsim/blob/635fc28d48d4ebf5408ce5a45988b7831da6a81b/scripts/jee-curved-entry-browser.mjs) passed **8/8 checks with four PNG screenshots**, using **Google Chrome for Testing 158.0.8127.36**. It visibly imports real qualified v24 geometry, exposes only valid physical controls, changes the material index and native refracted angle, rejects a colliding absorber and clears stale readings, exports a result-free qualified package, reopens it and recomputes native observations. Its archived report has zero JavaScript exceptions and zero off-origin HTTP requests. No public website deployment is performed or claimed.

**Builder-verified artifact:** [GitHub ZIP artifact 14548376683](https://github.com/physicsvigilante/opticsim/actions/runs/44559774415/artifacts/14548376683), from the **exact final run**, ZIP SHA-256:

`01edfdec4dd8849a0e17fab0ee4900ab1a01fe55dc6748200fec6c272feed6fd`

The builder downloaded this ZIP and recomputed its SHA-256, matching GitHub metadata. All **387 ZIP member CRC checks passed**. Its v24 section contains **59 members**: all **11 original input.json byte SHA-256 values match their individual report claims**; four positive real-native summary files, seven zero-native refusal reports, and the Chrome report with **8 successful checks, four real screenshots**. These artifacts are *builder GitHub CI* and downstream builder file checks, **not independently operated PhyDemo, Node 24 or Chrome replay**.

[Machine-readable verified handoff, immutable record](https://github.com/physicsvigilante/review_sandbox/blob/c1b2735aa47af8825c9120df64fb2e9edb71d33d/projects/opticsim/pr-180/BUILDER-VERIFICATION-01.json).

## 4. Red-test history retained, not hidden

- The initial genuine-native probe was numerically correct across an off-axis convergence series but its exactly axial control incorrectly demanded binary64-identical y values (~1e-14 mm); it was corrected to a **bounded near-zero check** and still explicitly refuses identifying a focus from one axial ray. No native physics was adjusted.
- Adding v24 initially broke two legacy catalog-count assertions (25 new total versus prior 24). Instead of concealing this, the tests now explicitly assert **24 unchanged historical profiles plus exactly one new v24 profile**. Historical model equations and canonical fingerprints remain intact.
- Initial post-PR178 push CI had Chrome missing; this was independently corrected by infrastructure-only PRs #179 and #181, both merged with **11/11 actual postmerge workflows passing**. v24's tested source tree includes their pinned Chrome prerequisites. No Chrome test was turned off or mocked.
- The first new v24 native/browser flow passed **953 Node tests and all 11 public authoring cases**, but failed Chrome UI controls: the old source-mode picker had no schema-v24 single-ray option. The final code adds v24 to its **single-ray-only** menu and accurate physical labels, then the real Chrome check passed. The browser error is preserved in GitHub Actions history; it was not a solver result.

## 5. Required ONE independent review — no split reviews

Review **exact source `635fc28d48d4ebf5408ce5a45988b7831da6a81b`**, tree **`cca59685effa922182111b875187dcd6c999edb2`**, and the identical synthetic integration tree. Inspect actual code and attached final artifacts, not only this builder report.

Focus on the **physical meaning of the real curved-arc entrance and retained flat closure**; material direction, native Snell and absorption; geometry admission and boundary clearances, including possible rare missed screen or second-face events; source-mode isolation; actual measured rather than prescribed detector hits; corner/seam, Fresnel and native completeness safeguards; stale, invalid and depth-limited suppression; preservation of historical contracts and CI/browser provenance. The existing pure paraxial J15 analytical query and fully reviewed v21/22/23 native physics need not be reviewed from scratch where their code is unchanged.

**Required GitHub deliverable:** commit a complete independent Markdown report to the default branch of `physicsvigilante/review_sandbox` at:

`projects/opticsim/pr-180/reviews/review-01-chat-b.md`

Read the committed report back from GitHub, then return its **immutable permalink, actual review commit SHA, exact reviewed source SHA**, and verdict **CLEARED FOR OWNER DECISION** or **CHANGES REQUESTED**. A chat-only verdict does not fulfill this gate. If publication fails, state it explicitly. Do not modify Opticsim source, merge or publish the demo as part of the independent review.

**Builder disposition:** candidate complete at exact reviewed source and CI; one independent review is due; **PR #180 remains DRAFT, UNMERGED and production main unchanged.** No further unrelated capability, full JEE solved-rate claim or background merge is authorized by this evidence.
