# EMFEELD PR #53 — focused independent corrective re-review #02 (Chat B)

**Date:** 2026-11-19  
**Reviewer:** Chat B, separate-context reviewer, not a human/teacher certification  
**Verdict: CHANGES REQUESTED (SCOPED).** Keep production PR #53 draft and unmerged. This is not a production release or a physics/JEE re-review.

This is a **NEW** review. The original [review-01-chat-b.md](review-01-chat-b.md) CHANGES REQUESTED report remains unchanged and is **not** retroactively marked PASS.

## Exact immutable source

- Production: [physicsvigilante/emfeeld PR #53](https://github.com/physicsvigilante/emfeeld/pull/53), draft/unmerged.
- Corrected head: **b8fda4de6d7dd14dad2eb134894ad194463ccade**; head tree **7c9bc833d641cabcca4c9025357314d02661eb30**.
- Previously reviewed head: 0c9afc19cc355f6e4e5cc7b67f9b5425f3abe8c2.
- Actual main base: **d3de5d7165945630e1a3979afa7252132d5efe5e**.
- Tested synthetic PR merge: **640c1d0d83981a7a39fe9bef989bab54199689a7**, combined tree **84135a2482ab8d277a206120f1de90bb7ce297e7**. **Not actual production main.**
- GitHub comparison from prior head to corrected head confirms **exactly five changed paths**: web/three_preview/model.js, app.js, model.test.js, README.md, and tools/qualify_browser_preview.py. The five recovered TAR Git blob identities were independently checked against those at the exact corrected GitHub head. No Python physics, renderer-neutral export, source input, physical tolerance or broader viewer was modified.

## Evidence and boundaries

**Verified original author CI artifact, not reviewer browser execution:** Original attached ZIP from [author WebGL run 44481502731](https://github.com/physicsvigilante/emfeeld/actions/runs/44481502731), artifact 14508043360, size 14,016,725 bytes, whole ZIP SHA-256 **8d689841c6fd9e47bc789e94cca2430bc3900f3ebeaddae7efecaa18bde02c7a**. Independently verified all 31 entries' CRCs and extracted source TAR SHA-256 **5d13b80568474949d00a8caf0d303ff862e5795185c262e2d75d13bad9b55abb**. Staged exactly 420 original source files/modes in Git and reproduced combined tree **84135a2482ab8d277a206120f1de90bb7ce297e7** using git write-tree. Verified preview integrity **12/12**, runtime integrity **10/10**, all three manifest snapshot hashes and examined normal and visible-refusal original screenshots.

The **author** report states three real Chromium WebGL2 scenes, 25 matched-checksum browser refusals, two real recovery paths, nine PNGs and zero JS page errors. These are retained as **author-owned** results, never relabelled independent tests. The three physical JSON snapshots remain byte-identical to original review-01:

- Electric: 13a4efb45557322da056cf61829fdadacaedc489851c242fb564702605cde41b
- Sun: 04f9e12624710d694120562dc49f6fc5c605434d617395bfaed92bfa4478fee4
- Line/plane: d74602d0b77aca990ea202f26bb092652667cd261f0d4660f228a1f9d9856611

**New reviewer-owned Node execution:** **15/15 PASS** new semantic/numeric challenges of the exact corrected model.js, covering positive extreme signed scalars and finite huge-positive midpoints, conflicting source role, missing/duplicate annotation IDs, non-Boolean flags, nonunit line/plane direction, physical field sample mismatch, invalid timeline unit/marker role, nonrepresentable position and subnormal glyph lengths. Additionally reproduced **two new admitted-but-degenerate Float32 geometry cases**, including a stronger case with all samples inside the declared scene bounds. Reran the author's own 25 Node test groups **25/25 PASS**, explicitly distinguished from reviewer-authored challenges.

**Independent browser limitation:** A locally authored Playwright/Chromium attempt launched the browser but navigation to the local HTTP preview failed with **net::ERR_BLOCKED_BY_ADMINISTRATOR**, before page load. No local WebGL, geometry, control, refusal or replay test was marked PASS. No administrator policy bypass was attempted.

**Separate reviewer-hosted WebGL testing:** Independently authored an isolated [review_sandbox draft PR #17](https://github.com/physicsvigilante/review_sandbox/pull/17) that fetches and asserts the exact synthetic merge/tree, constructs independent valid and malformed fixtures, and runs true Chromium/WebGL2 control, geometry, meaning/refusal, startup and replay-recovery scenarios. First reviewer-owned [run 44485643196](https://github.com/physicsvigilante/review_sandbox/actions/runs/44485643196) **FAILED at dependency setup** because npm ci required an absent committed lockfile; it did not execute browser tests. Fixed the independent review harness to install the version-pinned browser dependency without requiring a committed lockfile. [New reviewer run 44485774700](https://github.com/physicsvigilante/review_sandbox/actions/runs/44485774700) was **in progress at first report publication**. Do not infer a browser PASS before its final result and original artifact are independently inspected. Browser acceptance remains a separate open evidence gate.

## Disposition of R2-01 through R2-04

| Original finding | Result | Focused assessment |
|---|---|---|
| **R2-01** required meaning roles, unique IDs, SI time, Boolean flags and source direction checks | **Corrected in examined cases** | model.js lines 5–64 enforce shape-specific source, marker, potential and annotation meanings; unique nonempty per-list IDs; time_unit s, literal flags, normalized source directions and matched raw-field sample arrays. New reviewer negative tests refused. This is a bounded V1 contract, not a universal hostile-JSON security claim. |
| **R2-02** finite midpoint, enforced numerical display bounds and refusal of undrawable geometry | **PARTIAL; NEW BLOCKER** | Safe midpoint and individual coordinates/glyph checks operate on tested controls, but **nonzero path segments and potential triangles can become degenerate Float32 buffer geometry after validation**. Detailed counterexample below. |
| **R2-03** misleading browser keyboard shortcuts | **Corrected** | Browser-facing playback_help now refers to Play/Pause, slider and orbit. The original annotation text and raw JSON bytes remain untouched. Independent source and Node checks passed. |
| **R2-04** stale PR source/main identity | **Corrected** | Live PR body explicitly cites corrected head/tree, actual-main base, tested synthetic merge as not main, and historical evidence as historical. PR remains draft. |

### R2-02 — reproduced in-bounds Float32 geometry loss

Independently authored an otherwise valid V1 scene with bounds in all axes **[-10,10]** (normalizing scale **20**), proper roles/IDs/time/flags and a saved trajectory of **61** physically distinct positions. The world-X position at sample i is **20 × (0.25 + i × 10⁻¹¹)** for i=0 through 60. All positions are *inside the authored bounds*. After the documented display transform, the 61 binary64 X coordinates range from **0.25 to 0.2500000006** and are all different. validateSnapshot() **accepts** the scene. Conversion to Float32Array yields **exactly one distinct coordinate: 0.25**.

In the same accepted scene, a non-null potential triangle has transformed vertices **(0.25, 0.25, 0)**, **(0.250000001, 0.25, 0)** and **(0.250000001, 0.250000001, 0)**. They become three identical **(0.25, 0.25, 0)** vertices when stored in float32, so a nonzero-area surface becomes a **zero-area triangle**. A separate allowed far-translated stress case near normalized display coordinate 999999 also silently collapses 61 distinct samples into one.

**Code-path evidence:** [model.js lines 78–113](https://github.com/physicsvigilante/emfeeld/blob/b8fda4de6d7dd14dad2eb134894ad194463ccade/web/three_preview/model.js#L78-L113) checks each coordinate individually, including whether it rounds to literal float32 zero. It does **not** verify that distinct drawable vertices remain distinct or that triangles retain nonzero area after float32 conversion. [app.js lines 31–33 and 71–90](https://github.com/physicsvigilante/emfeeld/blob/b8fda4de6d7dd14dad2eb134894ad194463ccade/web/three_preview/app.js#L31-L90) use BufferGeometry.setFromPoints() for paths and Float32BufferAttribute for surfaces. The pinned Three.js 0.180.0 implementation of setFromPoints() stores a Float32BufferAttribute. This is loss **in the underlying GPU geometry buffer**, independent of camera positioning or pixel-size guarantees.

**Required correction:** Either (a) reject an otherwise nonzero drawable path segment, line segment or potential triangle when its actual float32 vertex geometry loses the required distinctions/area, **before** constructing THREE actors, with visible refusal/stale-clear/recovery; or (b) build suitably **locally rebased** geometry that preserves the distinctions without editing the original physical JSON, and independently verify the displayed geometry. Add the exact in-bounds 61-sample/nonzero-triangle regression and a real Chromium refusal/geometry/recovery check. Keep source snapshots unchanged. Do not call this merely a pixel-visibility limitation: the vertex information was destroyed before pixel rasterization.

## Outstanding gates and verdict

At the latest independently queried [release-candidate run 44481502744](https://github.com/physicsvigilante/emfeeld/actions/runs/44481502744), **Windows was SUCCESS but Linux remained IN PROGRESS**. Thus not an accepted Linux/Windows release gate. Author source/Gauss/cavity/PyVista/dipole/browser runs were reported SUCCESS independently of this open release gate.

**Final scoped verdict: CHANGES REQUESTED.** R2-01, R2-03 and R2-04 are materially addressed, normal astronomical/signed-potential and safe-midpoint controls work, and source/snapshot provenance is sound. R2-02 still silently admits a representability failure that loses geometry even inside the authored bounds. Reviewer-owned browser acceptance remains explicitly open until an independently completed actual WebGL2 run and its artifact are inspected. Preserve the old CHANGES REQUESTED report, keep PR #53 draft/unmerged, fix only the browser geometry boundary, then request narrow follow-up review. Owner-approved integration and later actual-main qualification remain separate.
