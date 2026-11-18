# PR #44 — independent R2 request: JEE 3D conductor cavity

**Author request, NOT independent approval. DRAFT / UNMERGED.** Review [PR #44](https://github.com/physicsvigilante/emfeeld/pull/44), Issue #43, under the owner's JEE-first/3D-first direction. Do not merge. Inspect the final author qualification report and actual fresh CI before treating OS/archive gates as passed; this request may precede their final completion.

## Exact candidate

HEAD **`e253d0acf15e7505f1da8ab95cb519b59b0d720b`**, tree **`8a4a14d70ba824e8a338add08356003e79a248bc`**. Base/main **`60b6e751363d0b922a02c3a259110547b79cf25c`** adds only the owner's theory PDF atop qualified PR40 `88324210`. CI preview **`04f8926ff15697ecccd9d89f71e837f2eb45bf56`** must have the same tree and ordered [base, candidate] parents. Nine added files, zero changed/deleted baseline files, **382 tracked files and32 package modules**. Verify these identities from original artifacts, not author prose.

New paths: `src/emfeeld/{conductor_cavity,cavity_lesson}.py`, `tests/{test_conductor_cavity,test_cavity_lesson_io}.py`, `viewer_tests/test_cavity_runtime.py`, `tools/qualify_cavity_lesson.py`, `examples/lessons/conductor_cavity.json`, `docs/CONDUCTOR_CAVITY_LESSON_V1.md`, `.github/workflows/cavity-lesson.yml`. This is a separate opt-in analytic boundary adapter, not a core Source/scene/particle-integrator extension. Existing field laws, event policies, numerical tolerances, original PDFs, old workflows and stored evidence remain unchanged. The expanded implementation inventory can correctly invalidate old source-pinned playback; preserve originals or replay exact inputs into new outputs, never rewrite old receipts.

## Supplied source and bounded adaptation

`01_theory_elec.pdf` original SHA256 **`dfed5a5cf241a365a2d94ebfeb73a9473aad66184d73af38be7fbfd81e6876ab`**, blob **`e8bf45cb2bc8206be0681d5c5367d0943e8b6c95`**,140 pages. Author extracted exact bytes from the GitHub source archive, read relevant text and rendered pages. Printed **1.115**: conductor cavity charge balance; **1.117 Q5**: central charge/thick shell; **Q7**: off-centre charge atR/2 in a neutral **thin shell**, asking field sketches. Printed **1.123–1.124**: method of images and grounded-plane examples.

Default R1m/B1.25m/q1nC is an explicitly **illustrative thick-shell adaptation**, not an exact reproduction of Q7. The spherical image/density formulas are separately derived implementation machinery, not claimed printed on those pages. Reopen the exact PDF and verify this distinction. No whole-chapter solving, unseen independent question, or teacher endorsement is claimed.

## Physical/display contract

One held point charge q at a inside a spherical vacuum cavityR, concentric outer spherical conductorB, no exterior charges. Isolated prescribed net conductorQ OR grounded. Cavity field is the exact real+image expression only in its physical domain; metalE0; exterior separately central-equivalent Q+q or zero. Isolated potential adds k(Q+q)/B. a0 uses the regular centred limit. Image location outside the cavity is not a physical exterior singularity. Point-charge and charged-surface field probes are refused where singular/one-sided; potential is continuous.

V1 bounds: R[1e-6,1e3]m, B/R[1.01,5], |a|/R<=.9, nonzero charge magnitudes[1e-18,1e-3]C, zero permitted, probe coordinates<=1e6R. These are explicit lesson/numerical admission limits. Do not claim arbitrary-scale or arbitrary-conductor support.

Inner surface density is analytic, sampled on a mesh; exact total -q is separate from an **unrenormalized** numerical integral/error. Outer density uniform only under stated geometry/source assumptions. Field curves are numerical direction traces, not time motion or calibrated flux. Negative q reverses arrow direction; paths and actual glyph vertices must stay out of metal. The cutaway is rendering-only, never a physical opening.

Four real sliders set offset/polar/azimuth and stored isolated-Q preset. G switches separately prescribed equilibria, not grounding-history dynamics; N reverses q; C changes cutaway; L shows/hides curves. Opening the viewer must preserve exact authored state; actual visible widgets, model and saved state must agree. Snapshots preserve CURRENT model, original input separately, actual slider/camera settings, PNG/arrays, source identities and failure outcomes. Shared evidence-output guard applies before writes/rendering.

## Preserved first failures and fixes

- Coarse96-node surface quadrature at a/R=.9 failed the asserted2e-13relative accuracy. Refinement to256 meets the unchanged target; density was not rescaled and display32/64-node errors remain visible.
- `3c8c0ff...` first real tests:68pass/2fail. Actual initialization callbacks slightly altered initial position; ignored during widget setup. Camera assertion had an object-to-numeric-array harness bug, corrected without weakening comparison.
- `9a87...`70tests/6renders passed but images showed invisible sliders: global Plotter.clear removed representations. Fixed renderer-only clear and actual enabled/view-prop tests.
- Model setters could leave stale slider values; synchronized them and retained actual values in snapshots/tests.
- `d1a84...`70tests passed but images had clipped labels. Corrected panel layout. New assertion on`669d9d...` produced69pass/1harness failure because stored normalized-display coordinates were compared to panel-relative limits. Conversion now uses actual viewport span; limits unchanged.
- A later direct geometric probe found fixed-length arrow tips outsideR at offsets.5/.65/.9 despite valid underlying curves. Final source positions arrows at half arc length and bounds glyph size by distance to wall/source; actual glyph mesh vertices tested, including both signs at.9R. No analytic field, density or traced path coordinate changed.

All prior source commits, original failed/limited-pass artifacts and local logs remain. Do not call earlier callbacks-only passes complete visual acceptance.

## Actual qualification and remaining review

Author final local source full **1,709 headless** and18 historical/one obsolete guard deselected passed; original V6/discovery/demo replays passed. Final dedicated lesson run **44245981629** records **71 tests** (67headless plus4real graphics), six retained scenes, actual VTK interaction and current-state snapshots. Author downloaded the original lesson ZIP and independently checked its hashes/source/arrays, then inspected all six actual PNGs at full resolution. This is not independent R2 or manual human Windows/teacher acceptance. No local PyVista run: isolated installation failed DNS/package access; hosted real graphics are distinct.

Final exact-head workflows: **44245981602** Linux/Windows release; **44245981615** existing viewer; **44245981717** source; **44245981629** new lesson. Original source artifact **14401692570** reconstructs the exact382-file candidate; original new lesson artifact **14402305972** retains71passes/siximages. Verify remaining actual conclusions and original artifacts from the current author audit before a full source/archive PASS. New lesson images are from Linux; Windows release runs the actual new graphics tests but is not claimed to retain an equivalent six-PNG lesson collection.

## Reviewer-owned tasks

Execute fresh independently derived numerical cases, not just the author's tests: off-axis rotations/signs/centre/zero/Q-cancellation/grounding; independent image or boundary expressions; gradient/equipotential/normal field; density integral convergence without forced normalization; actual image-position regularity outside cavity; nonphysical/ambiguous inputs. Challenge display curves AND glyphs, unsupported domain refusal, physical vs virtual charge and cutaway honesty.

Exercise real controls/camera and visible representation membership/viewport bounds. Inspect actual PNGs, not hashes alone. Check snapshot original/current/camera/slider consistency, failure retention, sealed-root/symlink refusal and no baseline-source writes. Audit fresh original source/Linux/Windows/viewer/lesson ZIPs, exact source tree,32-module receipts, prior physical references and deliberate invalid negative fixture rejection.

Publish **PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE** at `projects/emfeeld/pr-44/reviews/review-01-chat-b.md`, pinning exact source/tree, environment, commands, fresh tests, failures and limitations. **Do not merge.** Guarded integration and fresh actual-main archives remain separate. Issue36's independent unseen JEE task and Issue41's human Windows teaching walkthrough are not supplied by these tests.