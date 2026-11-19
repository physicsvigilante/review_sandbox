# Independent Chat B review #01 — conductor_sim M38b / PR #92

**Verdict: CHANGES REQUESTED — do not merge PR #92.** This is a scientific visible-page integrity blocker in the *new browser gate*; the independent native Kelvin/3D projection checks themselves passed. It is not an allegation that the unchanged M38a electrostatic law is wrong.

Review completed 2026-11-19. This is reviewer-owned evidence and is **not** a merge authorization. The production PR must stay **open, draft, and unmerged** pending correction, targeted independent re-review, and later explicit owner approval.

## Exact source, prior review boundary, provenance

- Production PR: https://github.com/physicsvigilante/conductor_sim/pull/92
- Exact reviewed production **HEAD**: `1ef915fdae72a032250c75fed2391ca40fab634c`
- Exact native Git **TREE**: `001cf922c6f89140e33e40e9c7379a2558a124dd`
- Released M38a base: `efff38c1608b76ebcd57ab02d51aea359b841f10`
- Frozen charter prior to implementation: `ff3c020b228f027f8a73cf22c48529ba261182d8`, whose only parent is the above base and whose only file change is **A docs/m38b_charter.md**.
- Actual Git diff `base..HEAD`: exactly **nine ADDED files**, no changed or deleted files. Original workbook PDF, M37a `grounded_sphere_wire.py` and M38a `prescribed_ground_line.py` each have identical Git blobs at base and HEAD; because *all* changes are additions, the earlier M37b renderer and all other released files are likewise untouched.
- The new viewer is teacher-hypothetical, **not** the original printed radial p8 Multiple Correct Q21 nor an additional JEE-30 source success. Neither the independent test nor this review extends original-question coverage.
- `PrescribedSphereLineTrace.as_dict()` invokes `validate_prescribed_sphere_line`, including native re-execution; the new viewer's `line_view_manifest` calls this path. The typed-trace entry point is not merely a blind dictionary trust boundary.

### Exact-source developer CI inventory, separately audited

GitHub Actions `actions/runs?head_sha=1ef915...` returned **24 completed/successful runs** at the literal source SHA: 22 `pull_request` and 2 `push`. The focused first successful author run [44461148713](https://github.com/physicsvigilante/conductor_sim/actions/runs/44461148713) shows 176 focused Python tests on each of 3.10/3.12; separate M38a native SI and M38b projection oracle; actual JS-on/mobile/no-JS Chromium; and **20 developer-authored HTML-only attacks rejected for their intended reason**. The focused run's job logs were read rather than taking the PR description on trust. These author checks are *not* an independent PASS. Prior red development attempts are not overwritten by this review.

### Independent execution (not developer-controlled)

- Reviewer-runner GitHub Actions: [run 44464947914](https://github.com/physicsvigilante/review_sandbox/actions/runs/44464947914), `completed/success`, pinned production SHA/tree, genuine Playwright 1.57.0 Chromium.
- Reviewer-authored independent script: [review-01-chat-b-probes.py](review-01-chat-b-probes.py), executed from the full source checkout without editing production.
- Reviewer evidence artifact ID **14500799859** in that run: `conductor-m38b-pr92-reviewer01-first-attempt`; contains test transcript, `review01-results.json`, genuine 41-frame and unfamiliar 29-frame screenshots, *all six forged no-JS screenshots*, and restored-original browser screenshots.
- First *review harness* run [44464823551](https://github.com/physicsvigilante/review_sandbox/actions/runs/44464823551) **failed** before reaching tests because the review workflow initially checked out only one source commit, making the required released-base `git merge-base` call fail (exit 128). Its failure remains visible. Corrected review workflow to use `fetch-depth: 0` only; no production change or replay of a false success. Second run above passed all reviewer probes. This first red result is a **review-infrastructure error**, not a production physics finding.

## Independent mathematical and actual Chromium results

### Original 41-state teacher example: PASS

- Original M38a teacher line: `q=+1e-9 C`, `a=.1 m`, initial `(-.4,.2,0) m`, world `v=(.2,0,0) m/s`, `T=4 s`.
- Independent M38a SI and M38b display reference checks passed for all **41 states**, real fixed local plane and full signed chart.
- Signed sphere-to-ground current: at `t=0`, **+8.94427190999916e-11 A**; at exact closest `t=2.0 s`, zero; at `t=4.0 s`, **-8.94427190999916e-11 A**.
- Real Chromium checks passed JS-on selected frames, physical browser playback/restart, 390px viewport and no-JS original first-frame text, SVG and disabled controls; 0 external HTTP and 0 JS page errors.

### Independently new 3D / negative-charge model: PASS

This model was **not the author example or suggested negative-q seed**:

| Input | Value |
| --- | --- |
| Sphere centre | `(0.83, -0.71, 1.09) m` |
| Source initial world position | `(0.21, -0.23, 1.37) m` |
| Constant Cartesian velocity | `(0.28, -0.10, 0.05) m/s` |
| Charge | `-2.3e-9 C` |
| Grounded solid sphere radius | `0.13 m` |
| Permittivity | `1.6 epsilon_0` |
| T, sample count, surface guard | `4.2 s`, `29`, `0.015 m` |

Independently recalculated the line's 3D positions, radial speeds, induced net metal charge, signed terminal currents, full 3D Kelvin forces, electrostatic energy at **every one of the 29 saved times** using only `math` and directly coded equations, without importing the production physical formulas. Independently calculated fixed basis, scale, exact sphere circle, two path endpoints and all chart vertices:

- True interior closest time `t*=2.2838283828382835 s`; distance `d*=0.46805686377060246 m` (safely outside sphere+guard).
- `u=(0.9287013775293232, -0.3316790634033297, 0.16583953170166485)`.
- `w=(0.041601670014741805, 0.5375781901565932, 0.8421870282306337)`.
- `n=(-0.36848752004256813, -0.7752410517818646, 0.5130480086746526)`.
- True scale `260.65209046863356 px/m`, sphere radius `33.88477176092236 px`; source endpoints approximately `(180.5239,68.0)` to `(510.5836,68.0)` in the local plane.
- Signed conventional current at `t=0`: **-1.0755007224109823e-10 A**; at `t=4.2`: **+1.2669952903220374e-10 A** (sign reversal relative to positive charge).
- Real Chromium replay passed with no-JS first frame, JS-on selected frames, mobile viewport and zero HTTP/JS errors. Escaping of the authored sphere name `Translated <reviewer> & grounded` succeeded.
- A separate qualified radial case independently checked as a **teacher hypothetical** with zero additional workbook items, rather than a false original-source replay.

## Three release-blocking findings: six novel HTML-only forgeries ACCEPTED by production Chromium gate

These tests intentionally changed **only generated local HTML**. Every attack preserved the external genuine native SI JSON and viewer manifest byte-exactly, kept the embedded original JSON script unchanged, and was visibly demonstrated in a **real JavaScript-disabled Chromium page** with actual screenshots before the *unchanged* `python -m tools.check_m38b_line_browser` was invoked in a separate process. A `returncode=0` means the production gate **accepted** false/incomplete visible physics. The script then restored the original HTML byte-exactly and re-passed the unchanged browser check.

The failure point is [`tools/check_m38b_line_browser.py` lines 31–50](https://github.com/physicsvigilante/conductor_sim/blob/1ef915fdae72a032250c75fed2391ca40fab634c/tools/check_m38b_line_browser.py#L31-L50): its `_string` validates genuine DOM `inner_text` and structural `is_visible`, while `_attr` validates numerical SVG attributes and coarse element visibility but **not the actually rendered CSS/generated content or stroke/fill/transform**. Further unguarded checks occur at [lines 52–118](https://github.com/physicsvigilante/conductor_sim/blob/1ef915fdae72a032250c75fed2391ca40fab634c/tools/check_m38b_line_browser.py#L52-L118).

### F-01 — BLOCKER: rendered provenance and signed SI can be falsified by generated CSS text

1. Insert just before `</style>`:
   `#m38b-heading{font-size:0!important}#m38b-heading::after{content:"OFFICIAL PRINTED WORKBOOK Q21 - OFF-AXIS";display:block;font-size:24px;color:#a00}`.
   With JS disabled, actual visible heading now falsely claims an **official original off-axis question**, despite genuine DOM text still saying `TEACHER HYPOTHETICAL`. Real Chromium verified a nonzero displayed `::after` caption and original text at `0px`. **Production browser gate ACCEPTED**, exit 0.
2. Similarly add `#m38b-current{font-size:0!important}#m38b-current::after{content:"-9 A";display:block;font-size:18px;color:#a00}`.
   Real visible first-frame signed current is falsely displayed as **-9 A**, while the DOM's own `innerText` remains genuine. **Production browser gate ACCEPTED**, exit 0.

These are independent from the 20 developer-authored direct text/attribute tampering cases (which the gate correctly rejects). Evidence images: `pseudo-original-source.png`, `pseudo-forged-current.png`.

**Required correction:** The no-JS scientific-visible text proof must reject pseudo-content/zero-font/transparent or overwritten/occluded authoring claims (including their effective ancestor styles), or more robustly require the whole HTML/CSS to match an independently re-generated canonical renderer output *in addition to* genuine Chromium DOM checks. Add regression probes for both forged visibly rendered strings and insist on the intended source/SI refusal, not merely any exception.

### F-02 — BLOCKER: the true path, current-zero axis, and grounded metal can disappear without detection

Three independent HTML-only modifications, each with unchanged numeric circle/path/axis data:

- `stroke="#9e6b30"` → `stroke="none"` on `#m38b-path`. The full physical source path becomes invisible; `_attr` still accepts all four original endpoints. **Gate ACCEPTED**, exit 0.
- `stroke="#567185"` → `stroke="none"` on `#m38b-zero`. The signed-current reference zero line disappears even though the chart still has both signs. **Gate ACCEPTED**, exit 0.
- Add `#m38b-sphere{fill:none!important;stroke:none!important}` to the style. The physical grounded solid sphere circle disappears though its centre and true radius attributes remain. **Gate ACCEPTED**, exit 0.

The reviewer JS-disabled Chromium inspected computed `stroke=none`, and for the sphere both `fill=none` and `stroke=none`, while producing actual screenshots `invisible-physical-path.png`, `invisible-zero-current-axis.png`, `invisible-grounded-sphere.png`. The SVG coordinates were never modified.

**Required correction:** Validate the *effective rendered* SVG appearance of required physical elements (actual stroke/fill, finite positive stroke width where required, opacity, geometry, ancestor visibility and clipping) and add these independent no-JS attacks to the gate. A deterministic whole-HTML integrity check is a simpler complete defense against unreviewed HTML-only CSS edits and avoids an endless whitelist of CSS tricks.

### F-03 — BLOCKER: CSS mirrors the entire claimed physical u–w plane

Inject `#m38b-scene{transform:scaleX(-1)!important}` before `</style>`. Real Chromium reported non-identity scene CSS transform and rendered a reversed physical axis/trajectory, but the same genuine numeric basis vectors, nominal SVG pixel attributes and DOM source claims survived unchanged. **Production Chromium gate ACCEPTED**, exit 0. Screenshot: `mirrored-local-axes.png`.

This is directly incompatible with the charter's **truthful physical local-plane** requirement. The scene's effective SVG/CSS transform needs to be fixed and verified (including ancestors), or the HTML/CSS should be canonical-byte-checked before displayed geometry is accepted.

## Required narrow correction and re-review

1. Fix **only the new M38b HTML integrity/browser checker boundary**; no change to M38a Kelvin physics, M37b printed radial viewer, original PDF, or earlier solved-JEE inventory is indicated.
2. Use a positive-control canonical HTML authenticity check (from the already independently SI-validated native input), and/or a complete browser-enforced effective presentation contract, so an attacker cannot falsify any initial visible source claim, SI quantity, true sphere/path/current axis or orientation by CSS/SVG while leaving native and embedded JSON intact. Keep actual JavaScript-disabled inspection; do not replace browser proof with only a static parser or hash.
3. Add all **six reviewer-authored cases** as regression tests. For each confirm actual false/missing on-screen content **before** invoking the real checker, demand a scientific visible-mismatch refusal (not a swallowed Playwright error), and preserve current original-first-frame and existing 20 attacked-attribute/text controls.
4. Re-run the affected real Chromium baseline/hostility checks on Python 3.12 plus existing source M38b SI tests on the corrected exact source HEAD. Preserve the first red and green evidence; request a **targeted independent follow-up review** with its own head/tree pin.
5. Keep PR #92 **DRAFT, UNMERGED** until a new independent PASS and separate owner approval. Do not infer release authorization from green developer CI or from successful reviewer workflow execution: the reviewer workflow's success means it **successfully detected six scientific validation bypasses**, *not* that M38b passed review.

**Verdict remains CHANGES REQUESTED.** The direct native SI and genuine baseline browser presentation are sound within reviewed cases, but the declared real-browser "false initial physical claims must be refused" guarantee is currently false under six independently reproduced CSS/SVG forgeries.
