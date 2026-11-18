# PR49 — focused independent presentation review (Chat B)

**Date:** 2026-11-18  
**Verdict: PASS (scoped R1 presentation/evidence metadata).** No blocking affected-path defect found. This is not new-physics approval, a local-flux accuracy certificate, teacher/human Windows validation, permission to merge, or an actual-main release audit. PR49 must remain draft until separate owner-controlled integration and post-merge gates.

## 1. Source pins and authentication

- Candidate HEAD: **9963c09d169a04cea488886db5f04c0de4074886**; Git tree **4da6b80f53d78b2394c8516b9463e442fffb50fe**.
- Released base: **f6a078354ec2a657ca010c5c92ea578a0f55a2ad**; tree **65935bb395552d3dfb466a6e48d03230f18b6b66**.
- Preview: **7635a3e96079f54167dbbb14f96299e8397555a1**.
- Exact original source ZIP SHA256 **7ae28db3a740cd3aeb1feefd31f5a53600773aa130cde6be6858c943376aa4a7**; inner tested-source TAR SHA256 **375c61cbdea9c9fb2f9595fdc475f46f898143f55f22b75f421ed19646c7222e**.

I verified every one of **394** original tracked source-file Git blob hashes against git-tree.txt, then independently reconstructed candidate tree **4da6b80f...**. Reverse-applying the supplied bounded candidate_diff.patch in an isolated copy produced the exact **391-file released base tree 65935bb3...**. The live connected GitHub base→candidate comparison names six changed paths: the viewer, its Gauss workflow, the lesson document, and three added qualification files. All **388 other baseline files** (including numerical modules and old tests) are identical. A separate live HEAD→preview compare returned **zero changed paths**; the preview was one commit ahead. The connected commit interface did not expose an ordered parent list, so the author's ordered [base,head] assertion was not independently validated.

The supplied whole handoff bundle SHA256 was **051b9b5d6860ce8de90190e30a7e656fbeab1a0000f174f1a99abf1775b6226c**. Its **191** checksum-manifest entries matched. Original nested ZIPs passed own SHA256, safe/unique path and CRC checks: source 4 members, Gauss 114, Ubuntu 2,186, Windows 2,186, offline overlay 14. Gauss ZIP SHA256 **3dd97ba302defcfe9131b51fbb101afe83b3b25b2c7cb864cd490bdea732e195**; Ubuntu **ad69ab8c8071ba600ba218f1b0b80e481c4123536ae0396a88efef6c939e19ae**; Windows **b436acf0ca867a67c8012a596441263a9916e8bdd0decab25a854350588a37da**; PR44 wheels **2f51d4a7aa4ef2a5d722627a6b3707c6e8efaef3bc486ab47675574df3d01295**. The original wheel SHA256SUMS also passed. These checks establish consistency with recorded source/artifact hashes, not independent cryptographic authorship or live GitHub Actions artifact-ID authentication.

## 2. Execution — do not confuse author reruns with new tests

In a separate reviewer container, actual **PyVista 0.48.4 / VTK 9.6.2** rendered using **vtkEGLRenderWindow** and software OpenGL (Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0). The five original PR44 offline wheels were installed with **pip --no-index --no-deps --find-links ... --target <isolated reviewer overlay>** after verifying their digests; no owner's-machine installation. Environment: PYTEST_DISABLE_PLUGIN_AUTOLOAD=1, PYVISTA_OFF_SCREEN=true, VTK_DEFAULT_OPENGL_WINDOW=vtkEGLRenderWindow, LIBGL_ALWAYS_SOFTWARE=1, MPLBACKEND=Agg, PYTHONPATH pointing to the original extracted candidate src plus isolated overlay.

Exact commands from the extracted original source tree (script paths point to reviewer-owned files outside the candidate):

~~~sh
python -W error -m pytest -q tests/test_gauss_lesson_presentation.py
# 39 passed / 0.59 s — existing AUTHOR-authored tests rerun, not 39 new cases
python -W error -m pytest -q viewer_tests/test_gauss_usability.py
# 5 passed / 18.83 s — existing AUTHOR-authored real-PyVista tests rerun
python -W error tools/qualify_gauss_usability.py --output ../reviewer_qualified_scenes
# 6 fresh production scenes, 6 PNG hash/dimension/visibility checks
PYTHONPATH=src:<overlay> python ../reviewer_adversarial.py
PYTHONPATH=src:<overlay> python ../reviewer_live.py
PYTHONPATH=src:<overlay> python ../reviewer_transition.py
PYTHONPATH=../base_reconstruction/src python ../reviewer_base_compare.py > ../reviewer_base_results.json
PYTHONPATH=src python ../reviewer_base_compare.py > ../reviewer_candidate_results.json
~~~

The independent base/candidate measurements were exactly equal in this environment for **11** new configurations (center, 0.99985/1.00015 sphere, zero-net, three-source sphere, all-zero, center/rotated/three-source cubes, sphere/cube undefined boundaries). Both JSON SHA256 = **0b6c4f5dfe265d94eb33fb52b4ddd439faf4aa7d0f3b3aa28853ca878eb06d77**. These are *additional reviewer tests*, separate from the 39+5 author-authored cases.

## 3. Independent caution challenges — PASS

The reviewer separately recomputed the actual display rule **abs(sampled − exact) > 0.01 × sum(abs(all prescribed charges)) / epsilon_0**. All sources, including exterior sources, enter the scale. There is no division by enclosed charge, renormalization, or certificate of local sample accuracy. Nine additional unit-sphere configurations:

| Independent configuration | Exact total (N m²/C) | Sampled total (N m²/C) | Warning |
|---|---:|---:|---|
| +1 nC at x=+0.99985 | +112.940907 | +55.701933 | yes |
| −1 nC exterior at x=+1.00015 | 0 | −55.358205 | yes |
| +1 nC at +0.99985, −1 nC at −0.3 | 0 | −57.238974 | yes |
| +1 nC at +0.99985, −1 nC at −0.99985 | 0 | ~0 | **no** |
| Two +1 nC exterior at ±1.00015 | 0 | +110.716409 | yes |
| Opposite ±1 nC exterior at ±1.00015 | 0 | ~0 | **no** |
| Three mixed inside/exterior sources with zero enclosed net | 0 | +55.358205 | yes |
| Three zero charges, inside/outside | 0 | 0 | no |
| +1 mC near inside, −1 mC interior, +1 aC exterior | 0 | −57,238,973.6619 | yes |

For all nine I checked the displayed rule against raw unrenormalized available physics, original signed error, and display noncertificate metadata. Symmetric cancellation hides opposite individual sampling errors; the proposed contract/doc explicitly warns that a missing banner is **not an accuracy certificate**. This is truthful, not a blocking defect.

## 4. Native resize, control transitions and screenshots — PASS

A real PyVista VTK slider **EndInteractionEvent** moved an initially authored charge from **0.25 m** to **1.00015 m**. New sampled total and signed error were both **+55.358204682531365 N m²/C** while exact total was **0**; caution appeared. Native calls to **ren_win.SetSize(...); Render()**, without physical redraw, exercised **840×560 → 1440×960 → 840×560**. Controller state, report, field arrays, surface probe positions/normals, and camera did not change. Actual annotation fonts changed from title/body/help **28/18/16** at 1440×960 to **18/12/11** at 840×560. New images were visually inspected: results, caution, six slider controls, colorbar/footer and axes were present and separated at the two supported sizes.

A second reviewer-owned **two-charge** actual slider sequence changed **0.9999 → 1.0001** (both distinct in live title/current SI state). Exact flux changed **0 → −112.94090666076802**; sampled values **−57.29627227318852 → −57.52542484981851**; warning remained. Refinement **24 → 48** did not erase it. Prediction hid numeric panel text and caution without changing stored numeric availability. Switching to cube cleared sphere-only caution; setting a surface-boundary source produced **undefined_boundary**, null exact field value, absent E arrays, and no stale caution.

An additional *real* **840×560** translated three-charge cube with +1 mC, −1 mC and +1 aC had a dense but inspectable six-face-flux panel and separated scalarbar/footer/axes. This checks longer admitted readouts; it is not proof of usability for all viewport sizes/DPI or every user.

**Actual new screenshot and receipt hashes** (all actual production PyVista PNGs; images and manifests in companion reviewer evidence ZIP uploaded in the chat):

| Screenshot / state | Size | PNG SHA256 |
|---|---|---|
| **Changed-state caution** | 840×560 | **33ac7a68a5f46a6415a76a5db99406ac2938471a6d0ddae5df7826930b938165** |
| Changed-state native resize | 1440×960 | **32afb5eacc3c2017bb2499353003be68af7f13b6f4fce487e091eb5643183e87** |
| Prediction, no visible caution | 1440×960 | **18ed6e817fe734013665d68cd81eaa5fdd69ca2c9208ae021fcec878bb7da982** |
| Undefined boundary, numeric unavailable | 1440×960 | **21e9626dc0334281713123dc9713c69c0f0f735729e214a81f369fc44085d2dd** |
| Long admitted cube | 840×560 | **e16e86341a4232e6e4d5018ad350f0113cd8c7359486ca72014ac2a9ca24b45f** |

Original *authored-input.json* bytes SHA256 **2b847f5acdc2c2d5e3ff8b12438577e704625fc87b81f360a6f760fbeef3df70**, matched byte-for-byte in all three new saved-state receipts; the changed current *lesson.json* SHA256 **07a13a5d0bb2f72c31f743dd67cf319af2639eddcb4cf4fdb7ab27e8b9f9d8db** and recorded original-versus-current inequality. Report physics equalled new measure(current state, current order); the saved SI positions, normals, E field and E·n arrays matched live controller arrays exactly; PNG hashes, reported window sizes and all three snapshot integrity manifests checked with **zero mismatches**. Prediction kept available internal physics while hiding answers. Boundary snapshot correctly recorded **execution_complete=true, flux_available=false** and contained no E arrays. Two protected output writes (existing sealed root and descendant) were refused without modifying the earlier report. Six additional fresh run-script scenes also passed PNG checksum/size/visibility checks.

## 5. Defects, first failures, classification and remaining gates

**Blocking source/evidence findings: none.** All executed reviewer checks completed; no first-failing candidate assertion or reviewer timeout. A *reviewer-owned metadata-print helper* once assumed the unavailable boundary report had a sampled-value key and raised **KeyError**; fixing the helper to use an optional lookup made the audit correct. This was not a candidate change or a relaxed test. Direct git ls-remote failed DNS; live repository/issue/diff comparisons used the connected GitHub service. The connector does not expose the preview ordered parents or remote Actions artifact IDs, so those specifics are recorded as author evidence rather than an independent verification.

The author's earlier scalarbar-key failure, clipped prototype, 240-second incomplete graphics run (48 progress markers), and overstrict cross-host bitwise audit are preserved in source handoff; **none is claimed as a reviewer check**. The author later reported full Linux/Windows **1,822 headless +18 historical (one preexisting guard deselected) +51 real graphics** per OS and 127 overlapping focused/14 scenes; those full suites were **not** independently rerun here. The original legacy-viewer and cavity ZIP payloads were not included in the focused bundle and were not inspected as payloads by this reviewer. No manual Windows operation, human/teacher usefulness, arbitrary-scale/window/DPI validation, or postmerge actual-main CI/archive qualification took place.

The change is adequately classified as **R1 display, layout, and informational receipt metadata** at the tested head. No changed solver, physical admission condition, field law, or measurement status was found; eleven base-vs-candidate cases agreed. Do not escalate to a wholesale re-review of unchanged Gauss physics without a concrete new finding.

**Nonblocking opportunities:** consider a clearer short no-banner-not-accuracy hint in the live panel; perform manual legibility trials for extreme-value/three-source scenes at the 840×560 minimum; keep earlier author failures and platform-roundoff observations intact.

**Final verdict: PASS (scoped).** No merge, mark-ready, PR-source edit, or release assertion is authorized by this review. Follow the separate guarded integration and actual-main qualification gates.

Reviewer evidence ZIP (provided separately in this chat): **PR49_Independent_Review_Evidence.zip**, SHA256 **7ac6451e23a00106e78111a6abb996eb35f20a7e4d0b8c0ad294b12d776e06e6**, containing the new PNGs, current-state reports/integrity manifests, original authored bytes, standalone reviewer scripts, native control event records and exact test logs.
