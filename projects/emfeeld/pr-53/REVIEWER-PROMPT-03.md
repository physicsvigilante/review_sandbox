# EMFEELD PR53 — focused Float32 corrective follow-up #03

**Builder request, not an independent verdict. Keep PR53 draft/unmerged.** Continue Chat B's review-02 only for the remaining R2-02 primitive-geometry defect and this four-path correction. Do not repeat accepted physics/JEE or unchanged metadata/help reviews.

## Exact source

- Repository: https://github.com/physicsvigilante/emfeeld ; PR https://github.com/physicsvigilante/emfeeld/pull/53
- Previously reviewed head: `b8fda4de6d7dd14dad2eb134894ad194463ccade`.
- New head: **`f90d536b29d1d253966d1e53bcfe3ae22b36f4fe`**; head tree **`060d451a16905eb219f0d327489e4464b13a8aaa`**.
- Unchanged actual main/base: `d3de5d7165945630e1a3979afa7252132d5efe5e`.
- Synthetic PR CI merge: **`5c0f5a2480510177f1f6be329936945bb9b16efc`**; combined tree **`77c03d1092fe1c55a1c4641b82402894eb5d4155`**. This is NOT production main.
- Exactly four modified paths from review-02: `web/three_preview/model.js`, `model.test.js`, `README.md`, and `tools/qualify_browser_preview.py` (+202/-29). No `app.js`, Python engine/exporter, physical inputs/tolerances, dependency or workflow change. Complete PR still adds the same ten paths to main.

Original current source artifact **14513636751**, [source run 44492653153](https://github.com/physicsvigilante/emfeeld/actions/runs/44492653153) SUCCESS: ZIP SHA256 `2ea4a69b70eebaca7b27521dbdffe5ef2797d80542941a176517f8d7e9e435f6`, nested TAR SHA256 `3661318a4f8e1b65b6bc1057b2b0e773bfa139c507e6e5178b6120b0c9b9373f`. Downloaded/rehashed, CRC checked, all **420 file/mode/blob identities** matched to local tested combined tree via native Git. This is author evidence, not independent source verification.

## Preserve review history and independence

[review-02-chat-b.md](reviews/review-02-chat-b.md) and review-01 remain **CHANGES REQUESTED**, unchanged. Review-02 cleared R2-01/R2-03/R2-04 and obtained real reviewer-owned Chromium execution: [run 44487694013](https://github.com/physicsvigilante/review_sandbox/actions/runs/44487694013), artifact **14510329377**, SHA256 `bfb271f8f8bb6d583dd4469eb408f9eb708fb7feff7e082e58208430106fb659`. That run exposed geometry loss on the old source; it is not acceptance of this new source. The former independent-execution gap is not incorrectly reopened as though no reviewer browser run ever occurred.

The reviewer may adapt the existing isolated [review_sandbox PR17](https://github.com/physicsvigilante/review_sandbox/pull/17) harness for a NEW pinned run. No reviewer code has been modified by the builder. Preserve previous dependency/setup/race harness failures. Do not replace independent tests with author CI.

## Focused challenges

Before actor construction, `model.js` now checks actual `Math.fround` vertices for every **physically nonzero consecutive trajectory segment** and the actual `center +/- direction*span` truncated-line endpoints. Compare with unchanged `app.js` and the pinned Three.js 0.180.0 Float32 storage. Exact repeated physical samples remain valid, including stationary/returning paths. Distinct physical points lost even during binary64 translation must be rejected. No original JSON is rounded in place, dropped, resampled or reintegrated.

Every potential triangle actually emitted by `potentialTriangles()` must retain **nonzero Float32 area**. Three distinct but collinear Float32 vertices must be refused; already-degenerate emitted triangles are also refused. Null-potential holes emit no triangles and must not be rejected as degenerate surfaces. The boundary is primitive nondegeneracy, not exact Float32 length/area fidelity, pixel visibility or universal hostile-input safety.

Independently retest your exact in-bounds 61-sample trajectory `x_i=20*(0.25+i*1e-11)`, i=0..60, bounds [-10,10] in all axes, and your nonzero triangle with normalized vertices `(0.25,0.25,0)`, `(0.250000001,0.25,0)`, `(0.250000001,0.250000001,0)`. Test path and triangle **separately and together**, so one rejection cannot mask another defect. Also challenge far-translated path collapse, source-line collapse, three-distinct-but-collinear triangle, and at least one new reviewer-chosen boundary case.

Execute genuine Chromium/WebGL on this exact source to check visible refusal, **no new actor construction**, no retained old actors/physical readouts, disabled controls, **valid -> real playing -> invalid -> valid advancing replay**, and **invalid startup -> valid replay**. The new expectation is refusal: old reviewer groups that passed because they reproduced admission/collapse must not be blindly reused as new acceptance criteria. Keep ordinary electric/gravity/line-plane controls, representable fine geometry, repeated samples and null holes. Reuse unchanged previous evidence proportionately rather than repeating broad physics review.

## Author evidence, not independent execution

- Local Node **37/37 PASS**. New tests first produced **8 failures / 29 passes** on the unchanged reviewed validator; red log retained before 37/37 green.
- All **31** browser-negative fixtures separately reached their intended validation errors in Node.
- Installed-package Python suite: **1,929 PASS**, warnings treated as errors.
- Actual archived Three.js `BufferGeometry`/`Float32BufferAttribute` constructors additionally executed in **Node, not Chromium**: six new collapses reproduced then rejected by the new preflight; all **2,400** ordinary nonzero path segments and **2,384** emitted potential triangles remain nondegenerate.
- Fresh Python snapshot bytes unchanged: electric `13a4efb45557322da056cf61829fdadacaedc489851c242fb564702605cde41b`; Sun `04f9e12624710d694120562dc49f6fc5c605434d617395bfaed92bfa4478fee4`; line/plane `d74602d0b77aca990ea202f26bb092652667cd261f0d4660f228a1f9d9856611`.
- No local WebGL success claimed. Earlier local Chromium navigation was administrator-blocked; no policy bypass attempted.

## Current CI status at initial handoff — verify again before acceptance

Five workflows completed SUCCESS: source **44492653153**, real PyVista **44492653213**, Gauss **44492653116**, cavity **44492653042**, dipole **44492653127**.

Browser **44492653092** is still preparing runtime dependencies; no current-source hosted browser PASS claimed yet. Expected checks: 37 Node groups, three ordinary WebGL scenes, **31 matched-checksum refusal cases / 14 recovery paths**. Expected counts are NOT observed results until the actual report is audited.

Release candidate **44492653058** remains in progress. Both Linux/Windows passed setup, current headless regression and the earlier input/example checks; later viewer/revision/ensemble qualification remains pending. Old run **44481502744** remains Windows PASS / Linux CANCELLED during apt/OpenGL setup before tests. Do not relabel that attempt.

Use the final PR description or subsequent request addendum for actual completed CI results and original browser artifact identity. Current CI and artifact audit remain mandatory gates.

## Verdict/report

Publish a NEW `projects/emfeeld/pr-53/reviews/review-03-chat-b.md` in review_sandbox: exact head/tree, commands, new reviewer-authored cases, original real-browser artifact/run identity, failed attempts/limitations, and scoped **PASS**, **CHANGES REQUESTED**, or **INSUFFICIENT EVIDENCE**. Do not edit old reviews or production source, and never merge PR53 from this review. Independent acceptance, owner-approved exact-head integration, matching reviewed main tree and fresh actual-main qualification are separate gates.
