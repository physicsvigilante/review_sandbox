# PR #47 — independent R2 technical review (Chat B)

**Verdict: SCOPED PASS** — 2026-11-18. This is a separate-context technical review of the bounded, opt-in JEE Gauss-law lesson. **It is not** a merge authorization, an independent human teacher trial, a manual Windows UI acceptance, a blind JEE authoring evaluation, an arbitrary-scale numerical proof, or a new native-model physics capability.

**Repository:** [`physicsvigilante/emfeeld`](https://github.com/physicsvigilante/emfeeld) — [draft PR #47](https://github.com/physicsvigilante/emfeeld/pull/47), [Issue #46](https://github.com/physicsvigilante/emfeeld/issues/46). **Candidate:** `fcf9fede87ccd37597d0ba8c9b9013ee99b764f0`; **tree:** `65935bb395552d3dfb466a6e48d03230f18b6b66`; **qualified base:** `aeea3fedb00de4e20304d1f88aa038f3fac1e99e`; **CI preview:** `457e2e3d79b205a7bb61fe7c4af5d9d585415d96` (same tree, recorded ordered parents `[base,candidate]`). The PR is **draft and unmerged** at review. GitHub compare reports four commits ahead, zero behind, exactly nine added paths, and no deletions/modifications to the 382 baseline files. All 391 source files were reconstructed from the original source artifact; `git add -A && git write-tree` independently returned the stated tree SHA.

## 1. Sources and evidence authentication

Reviewed the archived exact-head `AGENTS.md`, `docs/GAUSS_LAW_LESSON_V1.md`, both actual implementation modules (`src/emfeeld/gauss_lesson.py`, `src/emfeeld/gauss_view.py`), both focused physics test files, the actual `viewer_tests/test_gauss_runtime.py`, the Gauss lesson GitHub Actions workflow, preserved author history, Issue #46, GitHub PR metadata/compare, and the original committed `01_theory_elec.pdf` including page images.

The uploaded 49 MB review-ready ZIP passed member CRC and safe relative-path checks. Its original source/lesson/runtime/Ubuntu/Windows ZIPs passed member CRC and SHA-256 checks. Both distinct original source TAR members are byte-identical (`c9be3901bb882e9e69193b51e69ff95d4945dc500720b9ac9549a621286226ea`). All archived 391 files form the exact declared Git tree; no archived evidence was edited.

Live GitHub Actions queries returned **completed/success** jobs for all five exact-head workflows (as opposed to treating the author's dated assertion as live status):

| Workflow | Run ID | Live job conclusion | GitHub artifact and server-provided ZIP digest |
|---|---:|---|---|
| Full current-source Linux/Windows | 44281829329 | Ubuntu success; Windows success | Ubuntu `14418810185`: `aa8951738d38dc58e54a1fc1ec36ab685344ae1c716876cd4d39572c02a436f2`; Windows `14417263763`: `fa28ad0ac8f34601d8bf8f5c77141d1d9d888bec40271b2e393055f3b3647b76` |
| Dedicated Gauss lesson | 44281828953 | Success | `14416219886`: `372266e215c975aa26b6accfd40e3649b3bde6c0029284f73b309adec6ae5dd9` |
| Existing viewer | 44281828951 | Success | `14417541893`: `1734f19ea1e4661464ba8e1f56bcccc9ee5fefb66b0ff48bd8128eb74dba38ff` |
| Existing cavity lesson | 44281829138 | Success | `14417820939`: `82e29a1faced5199c40b13689600ce8d248d0e1e6cbf01fc214d3865d11153c4` |
| Source snapshot | 44281829140 | Success | `14417551219`: `e809ad6857199ede1188761d5f2c27f1d8be22de38f8736277147ce5cec5e97d` |

GitHub's artifact metadata explicitly ties **each** artifact to head SHA `fcf9fede...`; the original ZIPs included in the review bundle match GitHub's server-provided whole-archive digests for all four included PR47 artifacts (source, Gauss, Ubuntu, Windows). The optional PR44 overlay ZIP has SHA-256 `2f51d4a7aa4ef2a5d722627a6b3707c6e8efaef3bc486ab47675574df3d01295`. No separate download of the two auxiliary viewer/cavity ZIP payloads was made in this reviewer environment; their GitHub metadata/digests and author's archived audit were inspected. **Unkeyed local hashes alone are not author authentication.**

The author's full OS logs claim 1,783 headless + 18 historical (one obsolete guard deselected) + 46 real-PyVista passes per OS; these are **author/CI evidence**, not reviewer-owned tests and not additive independent test counts. The original dedicated lesson log claims 83 focused tests and eight scenes; this is also author evidence.

## 2. Fresh environment and commands

Isolated Linux environment: **Python 3.13.5; NumPy 2.3.5; SciPy 1.17.0; pytest 9.0.2; VTK 9.6.2; PyVista 0.48.4**. The five pure-Python wheels from the hashed PR44 overlay were installed offline with `pip --no-index --no-deps --target` into a new, separate reviewer directory; no software was installed on the user's computer. Source was extracted after ZIP/TAR path and CRC safety validation. EGL/software OpenGL was used for offscreen PyVista.

Environment settings included:

```sh
export PYTHONPATH=/mnt/data/pr47_reviewer/overlay:/mnt/data/pr47_reviewer/source/src
export PYTEST_DISABLE_PLUGIN_AUTOLOAD=1
export PYVISTA_OFF_SCREEN=true
export VTK_DEFAULT_OPENGL_WINDOW=vtkEGLRenderWindow
export LIBGL_ALWAYS_SOFTWARE=1
export MPLBACKEND=Agg
cd /mnt/data/pr47_reviewer/source
```

Completed rerun:

```sh
python -W error -m pytest -q tests/test_gauss_lesson.py tests/test_gauss_lesson_extended.py
# 74 passed in 1.28s
```

The first combined focused run produced progress through 76/83 items, but its container invocation exceeded its wall-clock budget: **INCOMPLETE, not a PASS**. A separate full viewer rerun produced **six explicitly passing real-PyVista tests**, then reached the reviewer 240-second time cap while beginning test seven: `RETURNCODE:124`; tests seven through nine were **not established by that local rerun**. An earlier short viewer rerun explicitly passed three tests before the wall cap. They are overlapping runs, not 3+6 distinct successes. The hosted complete CI suites were verified separately above.

Fresh independent scripts, run with warnings as errors against the extracted exact source:

```sh
python -W error /mnt/data/pr47_reviewer/reviewer_physics_challenges.py
# 87 independently authored checks passed
python -W error /mnt/data/pr47_reviewer/reviewer_evidence_challenges.py
# 16 independently authored checks passed
python -W error /mnt/data/pr47_reviewer/reviewer_viewer_challenges.py
# corrected, fresh real-PyVista run: 38 checks passed
python -W error /mnt/data/pr47_reviewer/reviewer_geometry_glyphs.py
# 2 independently authored geometry/glyph checks passed (96 oriented polygons, 24 meshes)
```

**Reviewer-owned checks: 143 passed** (87+16+38+2). These are scripted assertions, not necessarily independent random trials or statistically independent observations. The scripts and their actual stdout logs are retained as separate reviewer evidence, not appended to the candidate source. They used the unchanged production classes; during the 38-check event sweep the reviewer harness temporarily skipped *intermediate camera renders only* to contain software-EGL cost, then restored the real VTK renderer for both full production screenshots. Thus the sweep verifies real widget/key callbacks, actual meshes and receipts, **not high-frame-rate interactive performance**.

## 3. Physics verification

**No blocking physics defect found within the V1 admitted domain.** The independent reference did **not** call production solid-angle methods: it directly integrated Coulomb's outward-normal integrand over a rectangular face. One tangent coordinate was integrated analytically, the other via SciPy QUADPACK. The central face calculation gives `Q/(6 epsilon_0)` for each of six faces, while the separately reported exact total gives `Q/epsilon_0`. For `Q=1 nC`, both yield about `18.82348444 N m²/C` per face and `112.94090666 N m²/C` total.

Independently checked the six signed faces of a displaced charge; exterior sources (nonzero positive and negative face contributions, zero closed sum); negative source signs; three-source superposition; twelve random proper rotations with translations and size scales; near-plane switch at source x=0.9988, 0.9992, 1.0008, 1.0012; and exterior far-field cases x=10³, 10⁶, 10⁸ in surface-half-side units. The face sums were not renormalized to the exact enclosed-charge total. Additional direct source and output tests exercised strict type/magnitude admission, left-handed/nonorthogonal/overflow rotations, invalid quadrature orders, duplicate JSON keys, face/edge/corner boundary points, zero-strength boundary markers, and translated geometry whose side is numerically unresolved.

A **separate axisymmetric 1D Coulomb flux integral** checked the sphere's exact Gauss-law inside/outside classification at radial offsets 0, 0.3, 0.77, 1.2 and 2.5. The production sampled total was checked *as returned*, with its own `sampled-minus-exact` error and 24→96 sample refinement. Exact/near-unresolved sphere boundaries return explicit unavailable results, never an invented zero or half charge.

A useful **nonblocking caution**: near the sphere singularity the quadrature can be extremely inaccurate at the declared finite orders and this is accurately disclosed rather than rescaled. For a +1 nC source at x=0.9999 m in a unit-radius sphere: exact flux `112.94090666`, but `(n_polar,n_azimuth)=(24,48)` gives sampled `55.64463439` and error `-57.29627227 N m²/C`. At x=1.0001 m (outside): exact `0`, sampled `55.41548181`, error `+55.41548181`. At 96×192 the discrepancy is still large. **Do not present the sampled number by itself as a correct closed flux near the boundary.** The current panel labels exact, sampled, and error separately; this is truthful within the contract. Consider a stronger prominent *near-surface quadrature unreliable* warning in a future UX pass.

## 4. Actual controller, geometry, images and evidence

The fresh reviewer scene instantiated the production `GaussLesson` with real PyVista and VTK widgets. It triggered a **real slider `EndInteractionEvent`**, actual bound `KeyPressEvent` callbacks (`N`, `D`, `A`, `M`, `C`, `V`, `S`, `R`, `0`), changed source position/sign/pair/selection, surface translation/size and cube yaw/tilt, made/refined a sphere, and preserved flux through the view-only cutaway and prediction display. A source exactly on the analytic surface cleared stale `fields`, `normal_field` and arrow meshes. The surface retained the **closed mathematical flux** through view-only cutaway/camera updates. The sphere had **no auxiliary cube outline**; its probes lay at the analytic radius. The cube's eight physical corners and twelve actual rotated edges matched the orientation transform, not a world-axis bounding box.

An additional independent viewer challenge examined **96 real rotated polygon faces** and **24 generated arrow meshes**, checking outward polygon winding, normal arrow directions, Coulomb field-arrow directions and 3D tip positions rather than merely relying on a displayed arrow color or a screenshot.

Two **new reviewer-generated real controller screenshots** were visually inspected: `rotated_changed_state/view.png` and `boundary_after_change/view.png`, both 840×560 RGB from a reduced reviewer viewport. The first shows the moved +1 nC point charge, true rotated edges, nonuniform signed face patches and independent face totals; the second shows a plain gray analytic cube, no stale flux arrows/colors, and an explicit **UNDEFINED** result when the source is on its boundary. The reduced viewport causes some instructional text and the colorbar area to crowd/overlap; this is a **presentation improvement**, not a demonstrated false measurement at the default 1440×960 layout. The author-supplied default-size original screenshots were also inspected separately, but **were not counted as fresh reviewer screenshots**.

Fresh screenshot SHA-256 digests:

- `rotated_changed_state/view.png`: `73fbb1162d8fcbf0851805a763b0c784546440e0f4406b66b4c2660709f31c07`
- `boundary_after_change/view.png`: `21b665ebaeb825a25f9f9b92e81cd4530d1ac7db159fac0e9ec93ab6f48e6150`

The first fresh receipt re-read `lesson.json` as the **current** state (charge x=0.43, y=-0.22; cube yaw=23°), preserved the original authored JSON bytes *exactly*, recorded `original_input_equals_current_state: false`, verified screenshot digest against actual PNG bytes, and matched stored `E_dot_n_N_C` and outward-normal SI arrays to the live controller. Both reports recorded implementation hashes of the 34 source modules and the runtime environment. The second receipt ended `execution_complete: true`, **`flux_available: false`**, `exact_total_N_m2_per_C: null`. It is deliberately **not a successful numeric answer**.

Independently tested sixteen headless evidence/admission cases: sealed directory overwrite, descendants, nested descendants, a symlink alias of sealed evidence, unchanged prior file hashes, pre-write refusal of malformed/duplicate/non-byte authored input, all retained input/file SHA-256 digests, the boundary outcome, and an injected late `report.json` write failure producing an **incomplete, unsealed** root rather than a false success. These tests do not claim hostile concurrent-filesystem/ACID security.

## 5. First failures, corrections and remaining caveats

**Reviewer-owned retained first failure:** the first independent viewer script failed at `post_capture_boundary_clears`, because the **reviewer incorrectly assumed world x=1 was on a cube face after applying a 23° rotation**. That coordinate is not generally on the rotated face. Correction was limited to the reviewer harness: reset yaw to 0° before moving x to 1, or equivalently use `center+scale*R@(1,0,0)`. The complete corrected run passed 38 checks. The first log is preserved and **is not a candidate bug**. Candidate source and GitHub PR were not changed.

Historical *author* failures (retained, not retroactively promoted to passes) include early far-field cancellation and near-edge issues, boolean-rotation admission, huge translated geometry, late non-byte source input, a camera-test harness wrapper issue, early cutaway/graphics problems and the misleading world-axis box later fixed at the pinned head. The author's latest local and hosted suites were run after those corrections. No old numerical tolerance was relaxed to hide closure errors in the reviewed code.

**Limitations:** The reviewer-owned local complete nine-test viewer rerun timed out after six observed passes; the fresh independent 38-check graphics suite and its two new screenshots *did* complete. This Linux software-EGL environment is not a manual Windows desktop session or frame-rate study. Human teaching utility remains untested. V1 is only for prescribed static one-to-three point charges, bounded cube/sphere geometry, strictly separated inside/outside boundary classification and sampled sphere flux; no time-dependent Maxwell solver, arbitrary polygonal surface or native model-store observation is added.

## 6. Original textbook problem mapping

The **committed original** `01_theory_elec.pdf` was opened locally (140 pages; SHA-256 `dfed5a5cf241a365a2d94ebfeb73a9473aad66184d73af38be7fbfd81e6876ab`) and its actual **PDF pages 60–61 / printed 1.60–1.61** rendered and inspected, not merely searched by text. **Illustration 47** specifies a **square of edge 2l**, **point charge +Q** at **perpendicular distance l**, then a **cube of side 2l** containing that charge at the centre. The face result is `Q/(6 epsilon_0)`, and the cube result is `Q/epsilon_0`. **Illustration 46** is a *different* nonuniform-field cuboid problem. `l=1 m` and `Q=1 nC` in the example file are authored display values, not numerical givens from Illustration 47. The textbook performs a field/area integral; the lesson's oriented solid-angle triangle algorithm is a separately chosen equivalent numerical method, not misattributed to the text. The textbook's vertex-charge limiting problem is separate from V1's conservative undefined-boundary policy.

## 7. Decision and next gate

**SCOPED PASS**: the declared static Gauss-law lesson has an independently checked analytic physics foundation, strong exact-head evidence, real PyVista scene/controller exercises, truthful refusals and traceable, fresh image/input/physical-state outputs. There is **no identified blocking defect** in the reviewed bounded scope. Two presentation issues are **nonblocking follow-ups**: (1) make near-surface sampled sphere error more prominent when large; (2) avoid text/colorbar overlap at smaller viewport sizes. Neither should be represented as a physics validation failure or as complete teaching acceptance.

**Do not merge automatically.** Keep PR #47 draft until the owner considers this review and directs guarded exact-head integration. After integration, check the **actual-main** Linux/Windows/viewer/lesson workflows and their **new** original artifacts; the premerge preview runs do not substitute for actual-main qualification. Independent human teacher evaluation and manual Windows interaction remain distinct later gates. No candidate source file, PR metadata, or main branch was modified by Chat B.