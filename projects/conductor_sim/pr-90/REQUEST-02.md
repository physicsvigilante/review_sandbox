# M37b conductor_sim PR #90 — Targeted browser-integrity re-review request #02

**One narrowly scoped independent re-review ONLY, not another full Kelvin or M16a audit.** Previous independent source, native, and offline SI checks remain evidence for unchanged source files. Do not equate developer CI green with scientific review PASS.

## Exact corrected source and review scope

- Production [DRAFT PR #90](https://github.com/physicsvigilante/conductor_sim/pull/90), remains OPEN/UNMERGED as of request publication.
- **Corrected source HEAD:** `c8333b61dd5a147086842ab9162a3ed0ef495373`
- **Actual native Git TREE:** `44b754e005c3d720cb3e59c1debd363ca2d8d639`
- **Originally independently reviewed HEAD:** `155b0544684d3d880a83a661cc8e14a0ce22f26b` / native TREE `f48f54b8c49217b7c66179fe014b6fab1ea4dc4d`.
- **Released M37a base:** merged commit `133acf97a123e6167aeaac3ca2a2b2094af1d36f`, native TREE `c728041ca5118013c6979d120c8805f31ee09fa0`.
- Original M37b frozen charter `docs/m37b_charter.md` committed **before** implementation at `24300b2050430634532bb1978cba38eb7d3f39e4`.
- **EXACT four changed files since previously reviewed HEAD**: `tools/check_m37b_prescribed_browser.py`, `tools/check_m37b_nojs_hostility.py` (new), `.github/workflows/m37b-source-current.yml`, `docs/m37b.md`; public physics `src/conductor_sim/prescribed_ground_wire.py`, the SVG generator `src/conductor_sim/prescribed_wire_viewer.py`, the original PDF, M37a Kelvin solver and M16a integrator are UNCHANGED. Verify this with a live Git diff before reusing earlier source claims.

## Historical independent findings, preserved, not reclassified

- [Review #01 main report](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/conductor_sim/pr-90/reviews/review-01-chat-b.md): **CHANGES REQUESTED** on old exact head. It independently checked 31 native-equivalent Kelvin state observations and 28 hostile JSON mutations. Its original live Chromium reviewer harness caught 20/20 altered HTML cases, while the production browser checker wrongly accepted SEVEN falsely authored **JavaScript-disabled fallback** first-state values/attributes (a JS startup `show(0)` silently repairs them).
- [Independent review PR #10, additional native first-attempt](https://github.com/physicsvigilante/review_sandbox/pull/10): also **CHANGES REQUESTED** for the SAME no-JS blind spot. Its exact-head reviewer-owned workflow [#44353866101](https://github.com/physicsvigilante/review_sandbox/actions/runs/44353866101) has now completed SUCCESS. Retain its honest precise source/CI provenance and all first-attempt output; do not label either old negative review PASS.
- The unmodified physical source/book input `02_conductors_half_size.pdf` has verified digest SHA-256 `9dff3c02a9f1848d2c3d99cb1a6e7a44dc7f5a51f7a3a2b8cc92d10ce1fbca5d`. Workbook physical p8 Multiple Correct Q21 and p17 key (1),(3) require a **positive charge approaching a grounded metallic sphere at externally prescribed constant small speed**. Teacher numeric q/R/d0/v/T are not workbook source givens; this is **one original apparatus**, not 31 independent questions. M37b does NOT simulate free M16a dynamics or retarded wire Maxwell physics.

## B1 patch and actual required live re-review

The real production browser checker now verifies the DOM with `java_script_enabled=False` BEFORE calling the fallback pass successful:
1. Original Q21 workbook/source banner and actual visible teacher-numeric attribution.
2. First time **t**, radial distance **d**, induced net sphere charge **Q**, both signed conventional currents **I_sphere→ground** and **I_ground→sphere**.
3. Physically fixed solid sphere **cx/cy/r**, first point-charge **cx/cy**, source charge sign as **SVG text**, sign-label **x**, first plotted current marker **cx/cy**.
4. First time slider **index and min/max** and genuinely disabled no-JS controls, alongside the full original 31-point precomputed static current curve.
5. Every comparison is against the actual separately stdlib SI-verified persisted JSON; the browser must not derive or silently repair an incorrect static original snapshot via JavaScript.

The new real-Chromium runner `tools/check_m37b_nojs_hostility.py` makes **TEN separate HTML-only changes**, preserves actual science JSON and embedded JSON unchanged, and executes the **actual production browser checker** on each. All must REFUSE for scientifically meaningful reason. Seven attacks are the first reviewer examples: false marker x/y, charge x, charge sign x, first visible t, distance, opposite I. Three novel attacker cases: charge-sign label, actual sphere radius, and first slider time index. Source-sign and sphere-radius mutants may correctly refuse **earlier** under the existing script-enabled source/geometry evidence gates; a scientifically correct earlier assertion counts as a refusal. All other JS-startup-masked variants must specifically refuse in the no-JS DOM. Check physical native JSON and original HTML restored unmodified on test completion.

First new development push workflow `44355860921` FAILED only because the new hostile runner demanded the later no-JS sign assertion while the script-enabled checker **already** rejected the forged charge sign; the genuine browser check and both Python versions succeeded. The follow-up test matcher was corrected, along with the analogous earlier legitimate sphere-radius refusal; historical failed run remains RED. **Verified after packet publication: all 26/26 exact-HEAD PR+branch-push workflows completed SUCCESS** (Python 3.10/3.12, real FEMM 5, historical browser/source, M37b dedicated Chromium and 10/10 HTML attacks). This is author-controlled CI and NOT a substitute for independent execution. Reviewer MUST freshly verify live all exact-source terminal conclusions before PASS, including Python 3.10/3.12, actual FEMM5, historical Chromium and source suites, plus M37b B1 attacks.

### Mandatory first-attempt independent execution

Fresh checkout of the **corrected exact HEAD/TREE** in `review_sandbox`, verify PR head/state and 4-file changed scope, preserve first-attempt evidence (use `set -euo pipefail`). A single reviewer may reuse their previous self-authored oracle and exact unchanged native Kelvin source evidence, but must **independently run real browser attacks against the corrected browser gate**—not just read its source or trust developer green CI.

Minimum actual attempts:
- Baseline real generated `p8-ground-current.html` **and** same saved `p8-ground-current.json` must pass real offline Chromium with JavaScript enabled and disabled, including exact original source labels/current graph/mobile/restart.
- Independently mutate at least **all seven** original static first-frame forgeries: marker x/y, charge x, sign-label x, initial time/distance/opposite-current label; keep independently validated JSON intact. Mutants must be REFUSED by actual browser scientific gate while baseline passes. Add two novel no-JS cases (e.g., first source sphere radius/sign label/slider default) with actual reason recorded.
- Confirm the dedicated new runner itself actually executed >=10 attacks with no unexpected acceptance, and restoring native JSON/original HTML. Check screenshots & no external HTTP/JS exceptions.
- Replay at least the original R1 independent source-specific Kelvin number/charge/current proof and a representative source metadata/JSON hostility, or explicitly reuse the source-pinned native R1/R10 result after verifying the exact changed-file scope. **Do not** demand another full native science audit of source code unchanged by B1.
- Require ALL **26 exact-candidate** production workflows complete SUCCESS at time of verdict. Distinguish pull_request synthetic checkout commit from reviewed PR source HEAD; identical Git TREE is valid source equivalence. Never retroactively change old review verdict.

### Publication and permissions

Publish a new attributed `physicsvigilante/review_sandbox/projects/conductor_sim/pr-90/reviews/review-02-chat-b.md` as a new main file or separate reviewer PR, verdict **PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE**, with actual HEAD/TREE, failed/passed hostile evidence, full current-head CI, precise source/teaching limitations. Do not overwrite old review #01 or its negative report/evidence.

**Keep PR #90 DRAFT and UNMERGED.** Review PASS only permits asking for a **separate explicit owner merge decision** with reviewed `expected_head_sha`, verified merged main TREE and actual postmerge CI; independent review is not merge authorization.
