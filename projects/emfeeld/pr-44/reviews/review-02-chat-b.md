# EM Fields PR #44 — independent review-02, NEW Chat B context

**Verdict: PASS — scoped independent continuation on the exact candidate below. R2-B01 is closed by new reviewer-owned real PyVista execution. No merge performed or authorized by this review.**

**Attribution:** GPT-6 Astra Pro, OpenAI reviewing assistant, **18 November 2026**, in a **NEW independent reviewer conversation/context**. I am not the assistant context that wrote [review-01](review-01-chat-b.md), did not execute its old tests, and do not claim its executions as mine. This report continues the independent evaluation from that published report under [the new-chat handoff](../REVIEWER-HANDOFF-NEW-CHAT.md). Publication uses the connected `physicsvigilante` account; this is not a separate human reviewer's endorsement.

The original review-01 remains an immutable **INSUFFICIENT EVIDENCE** report about its own execution context. Its historical 42 physics/state cases, 15 reconstructed VTK cases, 67 source-authored focused tests and original archive/PDF inspection are not included in my counts. My supported conclusion is the focused missing real-controller/graphics/evidence gate, contextualized by fresh analytical spot checks, not a newly repeated whole-project or cross-platform qualification.

## 1. Exact candidate and preservation

| Identity | Verified value |
|---|---|
| Source repository | `physicsvigilante/emfeeld` |
| Only reviewed/executed commit | `e253d0acf15e7505f1da8ab95cb519b59b0d720b` |
| Git tree | `8a4a14d70ba824e8a338add08356003e79a248bc` |
| Base | `60b6e751363d0b922a02c3a259110547b79cf25c` |
| Source-equivalent CI preview | `04f8926ff15697ecccd9d89f71e837f2eb45bf56` |
| Preview tree/parents | Same candidate tree; ordered `[base, candidate]` parents, independently fetched from GitHub |
| Original review-01 blob | `d56a2fca14407ff6d6b2d7d09f452e73a705a6be` |

GitHub's candidate commit record and the original source artifact agree on the tree. I safely extracted the source TAR, independently computed all **382 Git blob identities**, indexed the files with their recorded modes, and reproduced that exact tree with `git write-tree`. There are **32 package Python modules**. GitHub's exact base-to-candidate comparison reports **nine additions, zero modified/deleted baseline files**. The auxiliary runtime-provisioning branch was not substituted for the candidate.

After every test group, the final audit rehashed all 382 tracked source files: **unchanged**. The reconstructed source working-tree diff is empty, with no untracked source files. Original outer/source/runtime ZIP bytes and all five wheel bytes remain unchanged. The source repository, old review, original archives and historical evidence were not edited. All new outputs were placed outside the reconstructed source.

The handoff, review-01, original prompts/request, runtime record, author response, qualification report, exact source contract, production controller/physics/output-guard code and relevant existing test interfaces were read. The previous review's textbook-page interpretation and original OS/viewer/lesson archive audits are historical evidence; I did not repeat those audits or independently reopen the PDF in this focused continuation.

## 2. Original archive and runtime verification

| Supplied original archive | Independently recomputed SHA-256 |
|---|---|
| User handoff ZIP, observed digest | `31af122456656678b4347ef3fae820e0b001a9e4b085ab8a723e7063e929233c` |
| Source artifact `14401692570` | `33059d044eb2b8ce824ecd6c7b65e3e05033b2fd30ca1f77676cd2f8e0437367` |
| Runtime artifact `14406007331` | `2f51d4a7aa4ef2a5d722627a6b3707c6e8efaef3bc486ab47675574df3d01295` |
| Source TAR inside original source ZIP | `ffafd8907459cfc32e3408e66bccdd2aea89608b8639eb3d47ef92c5ef8396f5` |

Source/runtime digests match the published handoff/runtime record. The outer, source and runtime ZIPs passed CRC, duplicate-name, safe-path and symlink checks; they contain 4, 4 and 14 entries respectively. The TAR contained only admitted regular files/directories. All five original wheel SHA-256 values, sizes, wheel CRCs, package names and versions were checked against `manifest.json` and the supplied runtime record before installation. Full per-file identities and wheel hashes are in `01_zip_audit.json` and `02_source_runtime_verified.json` in the evidence bundle.

I installed only the supplied wheels with `--no-index --no-deps --target /mnt/data/pr44_review02/overlay`. No network package installation or change to the owner's Windows/Conda environment occurred. The observed environment was:

- Python **3.13.5**, executable `/opt/pyvenv/bin/python`; isolated Linux x86-64, glibc 2.41.
- PyVista **0.48.4**, imported from `/mnt/data/pr44_review02/overlay/pyvista/__init__.py`.
- VTK **9.6.2**, imported from `/opt/pyvenv/lib/python3.13/site-packages/vtk.py`; actual render window **`vtkEGLRenderWindow`**.
- NumPy **2.3.5**, SciPy **1.17.0**, matplotlib **3.10.8**, Pillow **12.3.0**, pytest **9.0.2**.
- Production imports resolve to `/mnt/data/pr44_review02/source/src/emfeeld/`, not an installed alternative or support-branch copy.

`04_environment.json` records actual import paths, package versions and environment variables. This is not claimed byte-identical to the author's hosted environment. Single-thread numerical-library variables, offscreen EGL/software rendering, `MPLBACKEND=Agg`, disabled pytest plugin autoload and disabled source bytecode writes were set.

A direct remote artifact-metadata fetch was refused by the connector's URL policy. Therefore I claim independent verification of the **attached original bytes against the published digests**, plus independent Git source-tree reconstruction, not a new remote artifact-metadata audit. The earlier five-archive remote audit remains attributed to review-01. One preview-commit API read initially disconnected; a later read of the same URL succeeded. Both administrative limitations are recorded separately from product tests.

## 3. Newly executed reviewer-owned tests

**34 completed reviewer-authored pytest cases passed: 16 actual graphics/evidence cases and 18 analytical spot checks.** This is the count from completed corrected/split runs, not a claim of first-pass success. No author test, old reviewer test, partial timeout, diagnostic, duplicate rerun or pilot is added to this total.

| New test group | Completed result | Retained execution receipts |
|---|---:|---|
| Actual production initialization, four sliders, registered keys, camera/cutaway/lines, invalid updates | **5 passed**, exit 0 | `06_real_controls_corrected.*` |
| Actual production arrow meshes and curves, six near-wall configurations | **6 passed**, three fresh processes, exit 0 each | `07_glyph_R1.*`, `07_glyph_R037.*`, `07_glyph_R10.*` |
| Changed live controller to actual PNG/current state/arrays/hash receipts | **2 passed**, exit 0 | `09_captures_first.*` |
| Injected capture failures and protected-output aliases | **3 passed**, exit 0 | `09_failure_and_guards_first.*` |
| Independently derived analytical/context checks | **18 passed**, exit 0 | `08_physics_spots_corrected.*` |

The executable sources are `review_helpers.py`, `test_06_real_controls.py`, `test_07_real_glyphs.py`, `test_08_physics_spots.py` and `test_09_snapshots.py`. Every completed command, actual elapsed duration, log path and exit code is retained in its `.execution.json`. The recorder refuses to reuse an existing label. The normalized command structure was:

```sh
E=/mnt/data/pr44_review02/evidence
. "$E/env.sh"
python "$E/run_recorded.py" NEW_LABEL python -m pytest -vv -rA \
  -p no:cacheprovider --basetemp=NEW_EMPTY_PATH TEST_FILE [SELECTION]
```

The actual recorded selections were: all `test_06_real_controls.py`; `test_07_real_glyphs.py -k 1.0-53.0`, `-k 0.37-121.0`, and `-k 10.0-88.0` in separate processes; all `test_08_physics_spots.py`; `test_09_snapshots.py -k real_changed`; and `test_09_snapshots.py -k 'not real_changed'`. The union of the three glyph selections is all six cases; their per-process deselections are not omitted cases. Raw receipts contain the exact original labels and output directories, rather than the illustrative `NEW_LABEL` placeholders above.

### Real controls, not callback surrogates

Tests instantiated unmodified production `CavityLesson` and actual PyVista/VTK objects. Opening the lesson retained the same validated authored model object and identical serialized state/float64 position bytes. All four slider representations were enabled, visible, attached to the right renderer and absent from the left renderer, with visible title/value information and correctly interpreted panel bounds.

For offset, polar angle, azimuth and isolated-Q, tests set real representation values and invoked VTK start/interaction/end events. The production callback registration consumed the end event. Registered lowercase `g/n/c/l` behavior was exercised through `SetKeyEventInformation` and actual `KeyPressEvent`/`KeyReleaseEvent`, not by substituting direct calls to the four toggle methods. Direct method calls were used separately for invalid-input refusal tests.

Model positions, all slider values, internal angular settings, stored Q and rendered lesson text agreed after changes. Grounding set exterior charge/field and conductor potential to zero without changing the cavity field; changing stored Q while grounded left the physical model unchanged; isolating restored that prescribed Q. Reversing q reversed the cavity field and updated labels. Invalid offset/angles/Q values left model, controls, camera and display state unchanged.

After a reviewer camera rotation/elevation/zoom, cutaway and line toggles preserved the camera exactly. Cutaway removed/restored the rim and changed rendered surface geometry, while model bytes, probed fields/potentials and induced totals stayed identical. Hiding lines removed the actual line/arrow actors and restoring them restored the expected counts.

### Actual production glyph meshes and physical regions

Six fresh configurations used both charge signs, `a/R=.9`, `B/R=1.07`, and three oblique orientations/scales: `(R, theta, phi) = (1,53,-137), (.37,121,67), (10,88,-166)`. The near-wall model was reached through actual slider events, not a reconstructed substitute glyph algorithm.

I examined **42 actual production cavity `pv.Arrow` meshes** and **96 exterior arrow mapper datasets**, and verified the cavity mesh points matched their renderer mapper points. Every cavity glyph vertex remained inside `r/R<1`; the largest observed radius was **0.9753902554512024**. Every exterior glyph vertex remained outside `B/R=1.07`; the smallest observed exterior radius was **1.410099983215332**. These are sampled-case observations, not a universal bound.

The 42 associated cavity curves remained inside the cavity, terminated at the documented near-wall region, retained the documented source gap and followed physical E for both signs; the smallest sampled segment/field directional cosine was **0.9999902280589296**. Negative-charge ordering was checked explicitly. Exterior paths remained outside the conductor and followed their physical field direction. Actual vertex arrays and per-case receipts are retained. No particle-motion or calibrated-flux claim follows.

### New real screenshots and live-state evidence

Two new **1400x900** state-bound PNGs were captured after actual widget/key changes and personally opened in this new conversation:

| Fresh scene | Visible/current state | PNG SHA-256 |
|---|---|---|
| Grounded negative-charge cutaway | q=-1.4 nC, a/R=.820, theta=73 degrees, phi=-64 degrees; inner +1.4 nC, outer 0, conductor +1.4 nC; stored isolated Q=+1.15 nC, ignored physically while grounded | `0d7345459c3c708c090cb48ee10912275ceee1f044eafc6e6297e8461d0f47c0` |
| Isolated positive-charge full shell | q=+1.4 nC, same position/angles, Q=-.75 nC; inner -1.4 nC, outer +.65 nC, conductor -.75 nC, metal V=4.6735 V | `ea42dc4f3ec8968394624fa0d3a7d8f7f030743aed909c80c93e896b66c6e5f9` |

All four controls and explanatory labels were visible. Grounded view had no exterior curves; full-shell view had outward exterior curves and no cut rim. The source marker, sign-dependent density and field changes agreed with the recorded states. Sampled-integral error was displayed, not normalized away. The full-shell view naturally obscures interior detail; some long exterior rays cross overlay regions/image edges in the reviewer-rotated/zoomed view. This is a visual-layout observation, not a demonstrated field-region defect or blanket approval of arbitrary framing.

The test deliberately passed the obsolete initial model and a different requested count to `save_snapshot`; the live-controller path correctly captured the **current** model and controller count. Original authored bytes were retained separately. `lesson.json`, `report.json`, six saved curve arrays, exact widget values, camera/settings, all **32** source-module receipts, actual PNG digest and complete successful integrity inventory were independently compared. Each saved PNG also matched a second screenshot of the unchanged live controller **pixel for pixel**. The visual inspection record is `VISUAL_INSPECTION.md`.

### Failed capture and protected outputs

Fault injection replaced only the screenshot operation for negative tests, after constructing a real production controller. An injected `OSError` and an intentionally blank returned PNG each left current input/original input/arrays and an explicit incomplete `outcome.json`, with **no success report or integrity seal**. Both deliberate failures and their traces remain preserved. Retrying their existing or nested output directories was refused without changing retained bytes.

Nine destination challenges covered an existing new reviewer seal, a child of that seal, ordinary/dangling symlink aliases, a normalized path alias, model-store/question-lock children and an existing input file. All were refused before expensive tracing/rendering/screenshot operations. Protected bytes remained unchanged. These fixtures were newly created by this reviewer; historical sealed evidence was neither edited nor used as a disposable negative fixture. The negative tests do not substitute fake objects for the positive real-graphics acceptance tests.

### Fresh analytical context

Twelve parameterized cases compared production E/V with a separately written direct real-plus-image Coulomb expression at 23 seeded cavity probes each, across two oblique directions/offsets, both signs and grounded/two prescribed-Q settings. They also checked zero metal field, conductor potential, correct exterior field, continuous boundary potential, physical regularity at the mathematical image coordinates, finite-difference `E=-grad(V)`, local surface density and the near-wall normal-field relation.

Additional cases checked the centred negative-charge limit, zero grounded field, isolated exterior cancellation, charged/singular interface refusal and invalid model refusal. Two independent scalar-integral checks at `a/R=.89` compared surface quadrature orders 8/32/128 with direct angular integration, preserving numerical error and `renormalized=False`. No production density was rescaled. These are **18 new spot cases**, not a recreation or relabeling of the previous reviewer's 42 cases or a proof of all admitted floating-point inputs.

## 4. First failures and limitations retained honestly

1. **First controls run: 5 failed.** All stopped at one reviewer helper assertion that compared panel-relative slider coordinates with window-absolute bounds. The actual PNG already showed correctly positioned sliders. A separate real-coordinate diagnostic recorded the right viewport origin `(1008,0)`, size `(392,900)` and representation coordinates. I corrected only the reviewer helper's coordinate-frame conversion, retained original helper/tests/log, and reran all five cases: **5 passed**. No product source change.
2. **Two glyph batches timed out.** Outer tool limits were 20,000 ms and 60,000 ms. The logs show three and four completed-case progress records respectively, but no completed suite exit. Their receipts use **null exit codes**, not invented success or exit 124. The second attempt's prospective label `07_real_glyphs_completed` did not make it complete. Both logs/output directories remain. All six unchanged cases subsequently completed in three fresh processes with exit 0. The batch-timeout root cause was not diagnosed; long-session or repeated-renderer lifetime stability is not certified.
3. **First physics run: 16 passed / 2 failed.** The oblique nominal surface point normalized to `0.9999999999999999` in float64; grounded V was about `+/-8.85e-14 V`, exceeding my original unscaled `1e-15 V` absolute tolerance. An independent **80-digit** calculation showed the actual float-coordinate point is slightly inside R and has a small nonzero potential (~`3.45e-14 V` for positive q). I retained that diagnostic and initial test, used a documented roundoff allowance proportional to `32*epsilon*(k|q|/R)/(1-t)^2`, and kept a separate exact-axis boundary assertion at the original tolerance. All **18 passed** afterward. This is a reviewer tolerance correction, not a production formula/tolerance change or a claim of exact zero at every rounded nominal surface point.
4. The screenshot failures were **intentional negative tests**, not passed screenshots. Their incomplete artifacts are never counted as successful sealed evidence. Administrative inspection/API failures are recorded separately in `ADMINISTRATIVE_OBSERVATIONS.json`.

No previous reviewer timeout has been reclassified. No full headless suite, Windows run, original five-archive re-audit, original six author-scene reinspection, manual mouse interaction or teacher acceptance was newly performed. Author cross-platform CI remains author evidence; the earlier independent archive/PDF work remains the previous unavailable reviewer's evidence.

## 5. Evidence package and decision boundary

All new test sources, original failed harness versions/logs, timeout artifacts, exact commands/exit receipts, raw PNGs, successful/failed snapshots, actual mesh arrays, analytical diagnostics, dependency/import records and final preservation checks are retained in:

**`emfeeld-pr44-review02-new-context-evidence.zip`** — **17,020,028 bytes**, **168 entries**, SHA-256:

`87d39e0372b1e2c4a4da6a7fe4948c705fddc0a04f47d13f10952c99e752905f`

Its per-entry manifest SHA-256 is `0472096209eeb4c8b5144e60779d2ba8b21bcc1f986bee96ec59e258f630c5e4`. Packaging rechecked ZIP CRC and every manifest entry hash. The user's original handoff ZIP is included unchanged. Test symlinks are recorded as link metadata rather than followed during packaging. Installed dependencies/font files are not redistributed. The binary bundle and receipt are supplied as downloads in this review conversation; they are **not** falsely described as a new GitHub Actions artifact or as files uploaded by this report-only GitHub publication. Preserve the bundle for future reviewers whose conversation context may be unavailable.

`10_final_integrity.json` is the evidence index: **34 completed new reviewer cases; 382 source files unchanged; exact tree intact; original ZIPs/wheels unchanged; zero old-review/author tests counted as mine; no merge**.

**R2-B01: RESOLVED for the pinned candidate.** This new independent context actually instantiated the production PyVista controller, exercised real widget and registered key events, checked actual geometry and camera/physics separation, captured and visually inspected changed-state PNGs, verified state/array/hash binding, and challenged failed/protected output paths. No blocking product defect was demonstrated by these completed focused checks. No product correction was required to close the original execution-evidence gap.

**Final verdict: scoped PASS.** This does not certify arbitrary conductor geometries, a general PDE/Maxwell solver, whole-book solving, genuinely unseen teacher-question comprehension, universal numerical error bounds, long-session stability, manual Windows usability or pedagogical acceptance. The lesson remains the bounded spherical-conductor static-equilibrium adaptation described in its contract. Owner-controlled integration and any later actual-main CI/original-archive qualification are separate tasks. **Do not merge as part of this review.**
