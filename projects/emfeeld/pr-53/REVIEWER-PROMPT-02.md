# PR53 focused corrective re-review #02 — browser boundary only

**DRAFT / UNMERGED / NO INDEPENDENT PASS YET.** This is an author handoff, not a review verdict. Continue from [review-01-chat-b.md](reviews/review-01-chat-b.md), whose CHANGES REQUESTED verdict and original evidence remain unchanged. Do not re-review accepted Python physics or repeat broad JEE qualification unless a new material defect is found.

## Immutable source identities

Source repository: https://github.com/physicsvigilante/emfeeld ; draft PR: https://github.com/physicsvigilante/emfeeld/pull/53 .

- Previously reviewed head: `0c9afc19cc355f6e4e5cc7b67f9b5425f3abe8c2`, tree `7a012b2a441dd1fc07f50bc3dc63dcce9eed98a6`.
- Corrected head: **`b8fda4de6d7dd14dad2eb134894ad194463ccade`**, head tree **`7c9bc833d641cabcca4c9025357314d02661eb30`**.
- Unchanged actual-main base: `d3de5d7165945630e1a3979afa7252132d5efe5e`.
- Fresh GitHub synthetic PR merge: **`640c1d0d83981a7a39fe9bef989bab54199689a7`**, ordered parents `[main base, corrected head]`, tree **`84135a2482ab8d277a206120f1de90bb7ce297e7`**. This is the exact tested combined source, **not production main**. Author audit matched all 420 file/mode/blob identities to this tree and to the original CI source TAR.

The correction is one child commit with exactly FIVE modified paths: `web/three_preview/model.js`, `app.js`, `model.test.js`, `README.md`, and `tools/qualify_browser_preview.py`. No Python engine, renderer-neutral exporter, scene, physical tolerance, PyVista/JEE adapter, dependency or workflow file changed. The total PR continues to add the same ten browser-related paths relative to main.

## Builder disposition of review-01 findings — independently challenge these claims

**R2-01:** The validator now requires shape-specific source roles, potential/marker/annotation roles, nonempty unique IDs within each relevant list, animation time unit `s`, literal Boolean flags, normalized source directions, and matched raw-field sample structures. It rejects rather than infers missing/contradictory meanings. Keep this bounded exported-V1 contract; no universal hostile-JSON security claim is intended.

**R2-02:** Bounds use `lo + (hi-lo)/2`, with finite positive spans required. Before any THREE actor construction, rendered source centers, saved trajectory samples, potential vertices and arrow origins must be finite, within +/-1e6 normalized units, and not lose a nonzero offset to binary32 zero. Radii and source spans must be in [1e-6,1e3] normalized units; arrow lengths in [1e-3,1e3], avoiding THREE ArrowHelper's built-in 0.0001 shaft floor. Source extent and normalized bounds spans are also checked. README states these enforced rendering limits, not new physical limits or camera/pixel-visibility guarantees. No physical JSON clamping/resampling occurs. Signed extreme potential color ranges use an overflow-safe display-only ratio. Node positives include ordinary astronomical and coherently scaled/translated huge coordinates; do not misdescribe these Node positives as separate real-browser stress runs.

**R2-03:** Only browser-visible `playback_help` text is replaced by supported Play/Pause/slider/orbit instructions. The upstream annotation and entire snapshot stay unchanged. No Space/Home/arrow-key promise remains.

**R2-04:** The PR body now identifies corrected head, actual-main target and historical versus current evidence. It no longer calls the source stacked on still-draft PR52.

Invalid scenes must clear stale actors, readouts and active controls. The inspection hook exists before initial loading so a refused startup can recover when a valid scene is selected. Recovered replay must actually advance, not merely change a status flag.

## Fresh author-hosted evidence — available, NOT reviewer-owned

[Browser workflow **44481502731**](https://github.com/physicsvigilante/emfeeld/actions/runs/44481502731) completed **SUCCESS**, job **135414564329**, on the exact synthetic merge above. Original artifact **14508043360**, name `browser-preview-640c1d0d83981a7a39fe9bef989bab54199689a7`, **14,016,725 bytes**, whole original ZIP SHA-256:

`8d689841c6fd9e47bc789e94cca2430bc3900f3ebeaddae7efecaa18bde02c7a`

The author downloaded that original ZIP, checked SHA/CRC/31 safe unique entries, all 420 source blob/mode identities, 12 preview and 10 runtime integrity entries, exact source inputs, and the nine PNGs. Nested `browser-evidence/tested-source.tar` SHA-256:

`5d13b80568474949d00a8caf0d303ff862e5795185c262e2d75d13bad9b55abb`

Actual run: **25/25 Node groups; 3 genuine Chromium WebGL2 scenes; 25 malformed-input refusals; 2 real scene-selection/replay recovery paths; 9 screenshots; zero JavaScript page errors.** Refusal mutations receive matching test checksums so the semantic/numeric validator is exercised, not just checksum failure. Each initial refusal checks visible error, zero construction count/actors, null snapshot/frame/source, empty stale physical readouts and disabled controls. Both valid→invalid→valid and invalid-startup→valid are exercised. Normal slider/replay/orbit, potential visibility and snapshot/marker/arrow-origin checks remain.

Fresh local exports and hosted snapshots exactly equal original review-01 bytes:

- electric: `13a4efb45557322da056cf61829fdadacaedc489851c242fb564702605cde41b`
- Sun: `04f9e12624710d694120562dc49f6fc5c605434d617395bfaed92bfa4478fee4`
- line/plane: `d74602d0b77aca990ea202f26bb092652667cd261f0d4660f228a1f9d9856611`

Local installed-package regression: **1,929 tests passed with warnings as errors**, on reconstructed combined source matching tree `84135a...`. First pre-install attempt failed subprocess imports; that setup failure was preserved, not relabelled passing. Local Chromium again failed navigation with `net::ERR_BLOCKED_BY_ADMINISTRATOR`; no local WebGL PASS is claimed.

Other fresh runs on the corrected head: source **44481502789**, Gauss **44481502735**, cavity **44481502799** were already SUCCESS at handoff preparation. Real PyVista **44481502812**, dipole **44481502824**, and Linux/Windows release candidate **44481502744** were still in progress at the last preparation check. **Read their actual current status rather than treating this document as all-CI acceptance.** A focused browser review may proceed, but outstanding regression/release gates remain open until completed successfully.

## Focused reviewer work and verdict

Independently inspect only the five-path correction and preserve previous positive physics/source findings. Reproduce the original missing/wrong-role and overflow/subnormal defects against the new source; add at least one newly authored meaning or representability probe, and valid astronomical controls. Check the documented bounded domain really matches admission and actual THREE geometry. Check startup refusal, stale-scene removal and valid recovery; inspect actual rendered marker/arrow positions, saved times, null holes and browser help with unchanged raw snapshots.

**Reviewer-owned actual Chromium/WebGL execution remains required by review-01.** Run independently authored controls/geometry/refusal checks in an environment permitted to host the local preview, for example a reviewer-owned review_sandbox workflow pinned to the tested source above. Do not disable an administrator policy, call a stand-in canvas WebGL, or count the author's hosted run as independent execution. When runtime access is unavailable, explicitly retain INSUFFICIENT EVIDENCE / open browser gate rather than silently granting PASS.

Use `npm test --prefix web/three_preview` and `tools/qualify_browser_preview.py` for reproducibility, but distinguish rerunning these author tests from new reviewer-authored challenges. The original artifact includes the complete source TAR, pinned package lock, environment list, runtime files and genuine screenshots, so no prior ChatGPT sandbox is required.

Write a NEW `projects/emfeeld/pr-53/reviews/review-02-chat-b.md` with exact head AND tested combined tree, reviewer-owned run/artifact identities, findings/disposition for R2-01 through R2-04, limitations, and a scoped PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE verdict. Do not overwrite review-01 or edit/merge the production PR. A scoped PASS is not owner merge approval or actual-main release qualification.

Historical evidence retained: reviewed-source run44464467023/artifact14501073586 SHA `69363d6ec2741be2918e61791bbeccb9be63990d73cd9089ee4ccff301ccbe20`; earlier failed negative-replay run44350533820/artifact14449490116 SHA `8ba56db840d5d8210895166b9f26063fd8a48059820877a4614c2cc1cf7b25ad`. None is relabelled as current-source acceptance.
