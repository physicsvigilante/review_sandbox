# M37b / conductor_sim PR #90 — Targeted Independent Reviewer PROMPT #02

You are **independent Chat B**. This is ONE **NARROW no-JavaScript original-first-frame browser-integrity re-review**. You may be the same original reviewer or a fresh reviewer. **Do not restart an unchanged Kelvin/M16a/full-JEE physics review.**

**READ THE FULL SOURCE-PINNED REQUEST FIRST:** https://github.com/physicsvigilante/review_sandbox/blob/main/projects/conductor_sim/pr-90/REQUEST-02.md

- Production **DRAFT** PR #90: https://github.com/physicsvigilante/conductor_sim/pull/90
- **Corrected exact HEAD:** `c8333b61dd5a147086842ab9162a3ed0ef495373`
- **Native Git TREE:** `44b754e005c3d720cb3e59c1debd363ca2d8d639`
- Previously reviewed old head `155b0544684d3d880a83a661cc8e14a0ce22f26b` / tree `f48f54b8c49217b7c66179fe014b6fab1ea4dc4d`: [independent review #01 CHANGES REQUESTED](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/conductor_sim/pr-90/reviews/review-01-chat-b.md) and [review PR #10](https://github.com/physicsvigilante/review_sandbox/pull/10). Original red finding: **production browser checker accepted seven forged static initial HTML values when JavaScript was disabled**, masked by script-enabled `show(0)`.
- One narrow 4-file correction: `tools/check_m37b_prescribed_browser.py`; new `tools/check_m37b_nojs_hostility.py`; `.github/workflows/m37b-source-current.yml`; `docs/m37b.md`. **No new physical solver/authoring/viewer renderer changes, no PDF changes. Verify live diff and exact SHA/TREE; STOP as stale if moved.**
- Previous independent Kelvin 31-state math and 28 adversarial JSON refusals passed; separate [native reviewer workflow](https://github.com/physicsvigilante/review_sandbox/actions/runs/44353866101) completed SUCCESS. Preserve all original reviewer evidence and earlier failed development CI.
- At prompt publication **full exact-HEAD production CI was not yet terminal green**. Independently verify all **26** exact-head PR+push workflows SUCCESS including real FEMM5, full Python 3.10/3.12, historical Chromium and new M37b real Chromium **ten** HTML-attacks. **NO PASS if pending/fail/cancelled.**

### Mandatory first-attempt execution, not static code endorsement

1. In a **fresh source-pinned checkout**, verify `git rev-parse HEAD`, `HEAD^{tree}`, original pdf SHA-256 `9dff3c02a9f1848d2c3d99cb1a6e7a44dc7f5a51f7a3a2b8cc92d10ce1fbca5d`, exactly four new changed files, and PR draft/unmerged state.
2. Independently run real Playwright Chromium against **actual generated HTML and independently SI-checked JSON**. Run both scripts-enabled and `java_script_enabled=False` original fallback. Verify one workbook apparatus with symbolic q>0, R, prescribed constant inward small v and answer (1),(3); numbers q=1nC,R=.10m,d0=.30m,v=.04m/s,T=3s are **teacher-chosen**, not printed original givens.
3. Take actual physical first-frame DOM before JS can repair it (JS disabled) and compare visible **t,d,induced Q,both signed currents**, source-charge x/y/sign/sign-x, fixed sphere cx/cy/r, plotted current-marker cx/cy, slider original index and disabled controls, all 31 static plotted points, visible source and teacher attribution.
4. Reproduce **all seven** original accepted HTML-only forgeries, preserving genuine JSON: marker x=500, marker y=230, charge cx=690, sign label x=690, initial t=999s, initial distance=333m, initial opposite current +9A. Every case MUST raise an intended physically specific browser refusal. Add 2+ unfamiliar HTML-only attacker mutations (e.g. source sign, sphere radius, slider initial time); a correct earlier script-enabled refusal is acceptable for sign/geometry.
5. Verify new `python -m tools.check_m37b_nojs_hostility --output-dir ...` actually runs ten real Chromium hostile cases (all refused), leaves original HTML / SI JSON unchanged, retains actual hostile evidence and no external HTTP/JS exceptions. Do NOT trust its code alone; independently attack the same release checker.
6. Record actual reviewer test execution, **first attempt** logs and source-head/tree, original and forged screenshots, reason per hostile case, full terminal exact-head developer CI. Use `set -euo pipefail`; if local file:// navigation is blocked use Playwright `set_content` with the **byte-identical** HTML and clearly state navigation adaptation. No swallowed errors or forged "PASSED" claims.
7. Previous checked M37b source physics authoring and Kelvin code are **unchanged**; reuse the already independently executed 31-state Kelvin physical oracle, raw SI factory tests and JSON hostile checks after exact diff verification. No new blanket physics review.

### Deliverable and release safety

Publish `projects/conductor_sim/pr-90/reviews/review-02-chat-b.md` in `physicsvigilante/review_sandbox` (new review PR or main) with exact HEAD/TREE and **PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE**, actual browser variants, current 26/26 exact-head CI and explicit educational/provenance limits. Preserve old review #01 **CHANGES REQUESTED** and its first-run evidence untouched. A targeted PASS on this unchanged source is sufficient for the separate **owner** merge decision; no third broad review requested.

**NO production edits, mark-ready, merge or implicit owner approval.** Chat A must separately request explicit owner authorization after true PASS, use `expected_head_sha` guarded merge, verify main Git tree equal to independently reviewed tree and actual postmerge main CI.