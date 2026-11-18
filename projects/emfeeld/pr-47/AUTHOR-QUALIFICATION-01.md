# PR #47 — author qualification, current-source evidence and remaining gates

2026-11-18. This is author execution and archive inspection, **not independent R2 review**.

## Source and preservation

Candidate head `fcf9fede87ccd37597d0ba8c9b9013ee99b764f0`; Git tree `65935bb395552d3dfb466a6e48d03230f18b6b66`; base/main `aeea3fedb00de4e20304d1f88aa038f3fac1e99e`. GitHub CI preview `457e2e3d79b205a7bb61fe7c4af5d9d585415d96` has the same tree and ordered parents [base, candidate]. Both branch updates were guarded with the exact preceding head. No main branch update or merge occurred.

The original final source archive was downloaded, CRC/unique-path/safe-path/whole-hash checked, and its391 tracked files compared byte-for-byte to the local tested files and original Git blob inventory. Local Git tree construction and the remote created tree both give `65935bb...`. All382 qualified baseline paths are byte-identical; precisely nine paths are added: two lesson modules, two headless test files, one actual-PyVista test file, one example, one contract, one qualification script and one dedicated CI workflow. Existing workflows, PDFs, solver/measurement code, tests and historical evidence are unchanged.

Original source artifact14417551219, workflow44281829140: whole ZIP SHA256 `e809ad6857199ede1188761d5f2c27f1d8be22de38f8736277147ce5cec5e97d`; original tested-source TAR SHA256 `c9be3901bb882e9e69193b51e69ff95d4945dc500720b9ac9549a621286226ea`.

## Implemented scope

An opt-in static JEE lesson with a real rotatable PyVista cube/sphere, one to three held prescribed point charges, charge selection/position/sign, a pair preset, surface translation/size and cube orientation, predict/reveal, quadrature refinement and a display-only cutaway. The surface is imaginary, not matter. No trajectories, conductor response, general PDE solver or native observation schema extension is implied.

Cube face flux uses signed outward solid angles with a stable determinant and an equivalent near-plane rectangular antiderivative. The exact enclosed-charge total is computed separately; face values are not adjusted to force closure. Sphere sampling reuses existing quadrature without normalization and displays sample-minus-exact error. Local E dot n colors, fixed-length normal/field-direction glyphs and integrated flux are distinct. Boundary/unresolved positions yield explicit unavailable flux and clear stale colors/arrows. Bounds and the conservative zero-strength-marker boundary rule are documented.

Source interpretation: actual original PDF SHA256 `dfed5a5cf241a365a2d94ebfeb73a9473aad66184d73af38be7fbfd81e6876ab`; Illustration47, printed1.60–1.61/PDF60–61 is the square/centred-cube point-charge example. Illustration46 is a different nonuniform-field cuboid exercise. Default l=1m and Q=1nC are display choices. The original Issue46 conflation was corrected in a new comment, not hidden by rewriting historical evidence.

## Completed exact-final-source local execution

Python3.13.5, NumPy2.3.5, SciPy1.17.0, PyVista0.48.4, VTK9.6.2, software EGL offscreen. The declared optional viewer dependency was installed only in an isolated container overlay; nothing was installed on the user's computer. The original offline overlay ZIP was separately hashed; it contains dependency wheels, not independent reviewer results.

All commands used warnings as errors and disabled unrelated preinstalled pytest auto-plugins:

- `python -W error -m pytest -q tests`: **1,783 passed**.
- `python -W error -m pytest -q viewer_tests`: **46 passed**, actual PyVista.
- Historical behavioural suite with the existing obsolete all-file-freeze exclusion: **18 passed, one deselected**.
- New Gauss-specific real runtime subset: **nine passed**, included within46, not additional unique tests.
- `tools/qualify_gauss_lesson.py`: **eight actual scenes passed**: central cube, off-centre, exterior, undefined boundary, sphere, refined sphere, opposite-sign pair and rotated cutaway.

The new74 headless tests are included within1,783. The83 dedicated CI cases below overlap74 headless plusnine graphics; do not add these counts to inflate coverage. Final local source/module hashes, exact current state, original input bytes, samples, image hashes and outcome/manifest files were independently checked read-only. Human Windows operation, teaching usefulness and independent review remain not_evaluated.

## Completed current-source hosted qualification and original archives

**Dedicated Gauss lesson44281828953: SUCCESS.** Original artifact14416219886, whole ZIP SHA256 `372266e215c975aa26b6accfd40e3649b3bde6c0029284f73b309adec6ae5dd9`:71 members,83 passing focused tests andeight scenes. Original TAR is exactly the source TAR above. All56 scene manifest references, all34 implementation-module hashes in each receipt, current-state/image binding and numeric scene semantics were checked. The boundary scene executes successfully while flux remains unavailable, not a fabricated zero or successful numeric answer.

**Existing real-viewer workflow44281828951: SUCCESS.** Original artifact14417541893, SHA256 `1734f19ea1e4661464ba8e1f56bcccc9ee5fefb66b0ff48bd8128eb74dba38ff`:22 members, nine legacy scenes,17 PNG hashes matched to the original report and exact same source TAR. Its original headless log reports1,783 passes. Automated rendering is not human acceptance.

**Conductor lesson44281829138: SUCCESS.** Original artifact14417820939, SHA256 `82e29a1faced5199c40b13689600ce8d248d0e1e6cbf01fc214d3865d11153c4`:49 members,71 focused tests,six scenes,36 scene manifest references and all34 source-module hashes checked; original source TAR matches exactly. This is regression evidence for unchanged conductor source, not a new independent scientific review.

All original ZIPs passed whole-hash, CRC, uniqueness and safe relative-path checks. No original archive was edited or resealed. The bundle preserves the primary original source and Gauss lesson archives intact; auxiliary artifact IDs/digests allow direct independent retrieval.

## Preserved first failures and corrections

Original29 tests passed on the initial core, but author adversarial probes found far-field cancellation, near-edge closure loss, huge translated geometry losing representability, and boolean rotation admission. These prompted explicit bounds/roundoff-aware classification, a stable analytic determinant, near-plane evaluation and new references/refusals. No old physics tolerances were relaxed.

The first local pytest command stopped on an unrelated auto-loaded pytest_asyncio deprecation before execution. The subsequent commands disabled third-party plugin auto-loading; this is not a product-test PASS for the failed command. Two early graphics attempts hit the local command wall clock and remain incomplete. An author camera test initially passed a PyVista CameraPosition wrapper directly to NumPy; its harness was corrected to use a list, with the original error retained.

Two incomplete full local runs were intentionally stopped before further changes; they are not counted. Later admission probes found an overflowing large rotation, wrong exception type for invalid order and a non-byte source-input failure after output creation; new preflight guards/refusals and tests resolved these. Screenshot inspection found overlapping slider labels; values were moved into distinct titles. A subsequently completed candidate `eb577dc...` passed1,783/45 local suites, but actual image inspection then found the world-axis bounding box misleading for spheres/rotated cubes. Final `fcf9fede...` draws only actual cube edges and no auxiliary sphere cube, adds a geometric test, and reruns all final-source suites as reported above. Earlier outputs remain separately attributable.

## Gates still separate

The full current-source Linux/Windows clean-install workflow is44281829329. Its latest exact status and original OS archive audit are recorded in the handoff's CI-status record or a later qualification addendum; pending jobs are not PASS. Prior commit or main results cannot qualify this new source. Independent R2 review is not yet performed. PR47 remains draft/unmerged. After accepted independent review and guarded integration, new actual-main OS/viewer/lesson workflows and original archives must be checked again. No independent teacher trial, unseen-question success, manual Windows acceptance or arbitrary-scale mathematical proof is claimed.

PR45's distinct timeout-only actual-main release gate is complete, recorded at `projects/emfeeld/pr-45/POSTMERGE-AUDIT-20261118.md`. That does not release this new lesson.
