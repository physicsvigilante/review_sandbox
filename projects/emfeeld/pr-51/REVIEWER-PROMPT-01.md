# Independent Chat B review request — PR #51 JEE 3D dipole V1 (R2)

**Review class: R2 (new physical relation, numeric admission and current-state evidence). DO NOT merge or edit the candidate.** Create a separate-context, new independent reviewer report at `projects/emfeeld/pr-51/reviews/review-01-chat-b.md`; preserve all first failures, times outs, incomplete attempts and limitations.

## Exact pin and sources

- Repository: [physicsvigilante/emfeeld](https://github.com/physicsvigilante/emfeeld)
- Candidate: [draft PR #51](https://github.com/physicsvigilante/emfeeld/pull/51), head `f7cdf370fa44c40e6b5cb6d0c3ff580a7a364e52`, source Git tree `00592c7cc15d5013b4702951ff0db9baa7376b25`, qualified `main` base `6bfeb2c314841ef861d7d66b67c894a6295b705e`.
- Original preview `d14d78886ba366e6d0115e583cfcc25c7e7f9a80` has the same tree and ordered parents [base, head] (re-verify independently if available).
- Nine additive paths; 403 tracked files, 36 package modules, no baseline modifications. Inspect `src/emfeeld/dipole_lesson.py`, `dipole_view.py`, two new physics/IO tests, real `viewer_tests/test_dipole_runtime.py`, `tools/qualify_dipole_lesson.py`, `docs/DIPOLE_LESSON_V1.md`, exact lesson example and new workflow. Also inspect `AGENTS.md`, `docs/PHYSICS.md`, `docs/RELEASE_CANDIDATE_PROTOCOL.md`, Issue #50 and actual original PDF page.
- Original committed `01_theory_elec.pdf` SHA256 `dfed5a5cf241a365a2d94ebfeb73a9473aad66184d73af38be7fbfd81e6876ab`. **Illustration 35, printed 1.48 / PDF page 48** specifies +e at (1,2,1), -e at (0,1,0), external uniform E=(2,3,0), symbolic p=e(1,1,1), tau=e(-3,2,1). The example adopts SI positions/field and an illustrative q=1 nC; those SI choices/number are NOT the book's own stated numerical givens. Verify the actual question/page image independently; do not conflate its e symbol with the chosen 1 nC example.
- [Author current-source qualification checkpoint](AUTHOR-QUALIFICATION-01.md) and [complete Linux/Windows CI and archive addendum](AUTHOR-QUALIFICATION-02-CI-COMPLETE.md) are claims and pointers, *not an independent verdict*. Original evidence/handoff bundle is supplied in the user conversation. GitHub artifact IDs also permit original independent retrieval.

## Authored physical contract (challenge it, don't accept automatically)

One rigid, static pair of held opposite charges in a prescribed *uniform* external field. Exact finite-pair (not far-field) relations:
`p=q*(r_plus-r_minus)`; `F_plus=q E`; `F_minus=-q E`; `F_net=0`; `tau=sum((r_i-origin) cross F_i)=p cross E`; `U_external=-p dot E` with mutual pair energy explicitly omitted; quasistatic external work is `delta U` ONLY when q, E and separation remain constant, field work = negative. No inertia, temporal rotation dynamics, material polarization or general Maxwell PDE.
- Parallel/antiparallel have torque=0 yet different energy/stability; zero field or zero q has no preferred orientation/angle. Never invent a zero-vector arrow.
- Admission limits: q=0 or 1e-30..1e-3 C; separation 1e-9..1e3 m; coordinates/origin max |component|=1e6 m; E=0 or magnitude 1e-12..1e9 N/C. Strict real finite numbers, duplicate JSON keys rejected, close world coordinates rejected when separation is numerically unresolved. Small nonzero torque is not silently zero; nonzero below representable float64 is refused. Change of work constraints is typed unavailable with null numeric answers.
- Render scales for N, C m, N/C, N m are schematic and distinct; this display transform must not leak into physics values or current-state receipts. Camera orbit is view-only; force arrows originate on the actual plus/minus charges. Purple axial-torque arrow and right-hand rotation cue are not solved angular velocity.

## Required genuinely independent challenges

1. **Analytic physics:** Independently calculate endpoint forces and two lever-arm torques about several origins; compare with reported `p cross E`, not only two calls to the production method. Test central/translated/far (within admitted bounds), q sign swaps, E direction reversal, proper 3D rotations, noncoplanar example and several q magnitudes including elementary charge, zero q/E.
2. **Orientation energy/work:** From actual endpoint external potentials derive U and its zero-at-perpendicular convention. Reproduce Illustration35 vector components. Numerically check dU/dtheta=minus torque component for a separately defined oriented rotation, work signs for reorientation, no work for pure translation in uniform E, and refusal when charge/field/separation changes. Check angle and stability for parallel/antiparallel/perpendicular and near-collinear, including rotation out of page plane.
3. **Numerical adversarial:** Challenge cancellation in torques/energy and signed tiny nonzero moments; invalid bool/list/string/nonfinite/huge JSON numeric, near-unresolved coordinates, upper/lower bounds and the exact-rational cancellation fallback. Avoid relaxing physics tolerances to force an outcome. Distinguish physical zero from numerical underflow refusal.
4. **Real PyVista:** Instantiate actual `DipoleLesson` with PyVista/VTK, not a dummy renderer. Independently trigger native slider end-interactions and registered key callbacks (N, Q, T, O, 1/2/3, V, B, 0). Inspect source marker/force application positions, six sliders retained after redraw, torque-axis direction and right-hand winding, actual screenshot, 1440×960 and 840×560 legibility, camera-only changes, origin outside view, zero glyph behavior and prediction hiding derived arrows/results.
5. **Current-state/evidence:** Recheck saved `lesson.json`, `authored-input.json` exact original bytes, `work-reference.json`, NPZ physical samples, actual display transform/fonts/control state, screenshot PNG digest and module hashes against live production objects. Exercise source/accepted/descendant/symlink evidence-root output refusal, malformed authored input and injected late write failure. Don't call `execution_complete` a completed unavailable physics measurement.
6. **Source/release provenance:** Verify head/base/preview tree, nine changed paths, original source TAR (403 files), all complete CI statuses and ZIP digests; original Linux/Windows tests 1,894 headless +18 historical +62 actual-PyVista *each* are author/CI results, not reviewer-owned cases. Dedicated dipole 83 focused and ten scenes overlap. Original archive Windows whole sha `ac45c2d45ee18745b6b65d5a6cda9e0f52a2f4eb65d4f5dc0b3886da49d57dc1`. Preserve the known deliberately corrupted negative in full OS evidence as an expected refusal.

## Original GitHub artifact retrieval identifiers

| Kind | Run ID | Artifact ID | Original archive SHA256 |
|---|---:|---:|---|
| Source | 44319905552 | 14435605157 | `46e885c79cc4d011a5845156b676b372267a041508e5ecd8f2b608832b3d2b0e` |
| Dipole | 44319905924 | 14434077716 | `68794fc92d7f460f3d8014df3e96f654a823da7c8a85e383e921b8b30abf78d2` |
| Gauss | 44319905664 | 14434253713 | `8d9b6cbcec82b0e5dd6dd9ba1be5e7dce9bf96e55eb53ee8e07fe08b18781224` |
| Viewer | 44319905714 | 14434576422 | `263cd16529749298c0ef328285797a217e8eb803e205f5baa2801f5bf333d417` |
| Conductor | 44319905520 | 14434592015 | `6a81d30b8eff5d867872c7cb27d60747075dd3aca11f207262504a3bdf522ebf` |
| Ubuntu / Windows | 44319905997 | 14436020601 / 14435833145 | `76950977e6083aec8c255a43a22b735b2fa12acb806e6e959ea874a01a3a500b` / `ac45c2d45ee18745b6b65d5a6cda9e0f52a2f4eb65d4f5dc0b3886da49d57dc1` |

Optional offline PyVista overlay from original PR44 artifact 14406007331, sha256 `2f51d4a7aa4ef2a5d722627a6b3707c6e8efaef3bc486ab47675574df3d01295`. It contains selected pure-Python wheels only; separately installed NumPy/SciPy/VTK are still required. Never install on the owner's computer.

## Verdict and ethics of the gate

Write a review with **PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE** (scoped precisely), reviewer-authored test scripts/actual outcomes, independently generated screenshot receipts and any reproducible numbered blockers. Explicitly label author tests vs reviewer-owned checks. Report unexecuted cases and any timed-out runs honestly. Neither an author-generated trial nor a second author script becomes a new independent blind JEE trial; original Issue #36 remains separate. A separate ChatGPT context is not a human expert/teacher evaluation.

**Do not merge, modify source, close Issue #50 or claim release.** Report to the owner; an author chat can then address findings, obtain owner standing-direction integration and fresh **actual main** CI and new ZIP audits. No general field solver or dynamic dipole motion is implemented.
