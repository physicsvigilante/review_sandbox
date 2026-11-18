# conductor_sim M37b / PR #90 — independent Chat B source + physics + browser review #01

**Reviewer:** Chat B, independent ChatGPT reviewer  
**Review date:** 2026-11-18 (UTC)  
**Verdict: CHANGES REQUESTED**  
**Release consequence:** Keep production PR #90 DRAFT and UNMERGED. No owner merge approval is implied.

## 1. Exact source and gate identity

- Production draft PR: https://github.com/physicsvigilante/conductor_sim/pull/90
- Reviewed candidate HEAD: **155b0544684d3d880a83a661cc8e14a0ce22f26b**
- Native Git TREE (read directly from Git commit object): **f48f54b8c49217b7c66179fe014b6fab1ea4dc4d**
- Base merged M37a: **133acf97a123e6167aeaac3ca2a2b2094af1d36f**
- Charter-before-code: **24300b2050430634532bb1978cba38eb7d3f39e4**, whose actual Git parent is exactly the base above.
- Fresh PR metadata: draft=true, open, merged=false, head unchanged. Fresh base..HEAD comparison: exactly **10 files**, all in the preregistered changed-file list, no old physics/PDF change.
- Live GitHub Actions inventory at this HEAD: **26/26 completed SUCCESS** (24 pull_request, 2 push; Python checks, actual FEMM5, existing historical/source browsers and dedicated M37b). No earlier-head run substituted. Example exact-head push run: https://github.com/physicsvigilante/conductor_sim/actions/runs/44343488972 .
- Downloaded the actual push-triggered artifact **14444697263**, which contains exact-head p8-ground-current.json and HTML and true Chromium screenshots. It states HEAD 155b054... and TREE f48f54... . The matching PR-triggered artifact had the GitHub synthetic merge ref 240c38... but the **same native TREE and byte-identical JSON and HTML**. All independent tests below use the raw push exact-head artifact.
- Exact native Python 3.10 CI artifact **14445600669** reports original PDF SHA-256 **9dff3c02a9f1848d2c3d99cb1a6e7a44dc7f5a51f7a3a2b8cc92d10ce1fbca5d**, matching the independently registered source SHA. Its JUnit source-focused tests report **93 tests, 0 failures, 0 errors, 0 skipped**.

## 2. Blocking finding B1 — browser gate fails to attest the JavaScript-disabled first-frame geometry/labels

**Severity: release-blocking test/evidence defect.** The authentic generated HTML is correct; this is not evidence that the Kelvin solver or rendered unmodified scene has wrong physics. The *release browser checker* nevertheless accepts modified HTML that falsifies the scientifically meaningful first snapshot for a user with JavaScript disabled, in direct conflict with the charter's HTML-only hostile-integrity and fallback acceptance requirements.

**Reproduction against actual production assertions, not an approximation:**

1. The original production browser checker file is Git blob **fe226f4950f6916094a61916fff6074f1f636307**. The production standalone JSON reference checker is Git blob **eb0da147932789a652580250799399665fa0f098**; the independently reconstructed byte-exact copies were checked with git hash-object.
2. Change only the initial SVG chart marker x coordinate in p8-ground-current.html from 61 to **500**. Keep the independently validated JSON, embedded JSON, other chart points, physical samples and JS unchanged. See reviewer-owned source-checkout reproduction script: [reproduce-nojs-checker-gap.py](./reproduce-nojs-checker-gap.py).
3. Normal JS executes show(0) immediately, silently restoring the marker to x=61 before the existing checker samples the DOM. Without JS, the HTML's original marker persists at **x=500**, visibly disconnected from the start of the time/current curve (t=0); a wrong first-frame plot is presented.
4. Existing browser checker accepts **both** untouched and forged HTML. In this restricted reviewer Chromium environment, the original checker logic was executed without changes to any assertions, adapting only its three file:// navigations to Playwright set_content of the *same HTML bytes*, plus using the installed system Chromium executable. The original file:// navigation is blocked by the review-container administrator. The same sequence ran in actual offline Chromium; this is a browser execution result, not an inferred static-code warning.
5. Seven distinct HTML-only false first-frame mutations **all passed** these otherwise unchanged production checker assertions:
   - initial marker cx=500;
   - initial marker cy=230;
   - static source charge cx=690;
   - static sign-label x=690;
   - first displayed time **999 s**;
   - first distance **333 m**;
   - first opposite-current label changed to the wrong positive sign.
   JS startup repairs all seven for normal display, but each remains a wrong static fallback with JS off. The existing fallback code checks Q/current, source visibility, disabled controls and no-JS banner, but omits these other first-frame quantities and SVG coordinates. Relevant source: https://github.com/physicsvigilante/conductor_sim/blob/155b0544684d3d880a83a661cc8e14a0ce22f26b/tools/check_m37b_prescribed_browser.py#L145-L162 .

**Required correction, bounded:** In the actual real-browser no-JS branch, independently compare the **initial displayed t, d, induced Q, both current labels, slider initial index, charge cx/cy, charge sign text/x, and current marker cx/cy**, plus fixed sphere geometry, directly against the source-specific verified JSON's first readout/layout. Retain the already good curve-all-31, attribution visibility, mobile and disabled-control checks. Add hostile tests that mutate each *static HTML attribute/label without touching JSON* and require refusal, including one marker-only attack that ordinary JS masks. Re-run targeted real Chromium and newly affected CI at the new head; never relabel the prior green developer CI red.

The newly authored independent reviewer browser verifier includes those no-JS checks: it **detected 20/20** HTML-only mutations. This contrast proves the gap is in existing release assertions, not an impossibility of testing static fallback.

## 3. Independent physical and SI evidence (passed in inspected exact-head export)

A separate reviewer-owned pure-image-charge oracle, not importing production physics, independently checked **all 31** genuine saved states. It used the Kelvin image charge q'=-qR/d at a radial image location R²/d, then computed actual source-image force, U=(q times image potential)/2, signed sphere charge and terminal current, with world position and velocity at each prescribed timestamp.

- Source q=+1.0 nC, grounded R=0.10 m, d0=0.30 m, signed radial speed -0.04 m/s, duration 3 s; 31 actual prescribed samples.
- At t=0 s: d=0.30 m, sphere Q=-3.333333333333334e-10 C, conventional sphere-to-ground I=+4.444444444444445e-11 A; induced force radial=-4.2129149026224257e-08 N; induced mechanical U=-5.617219870163234e-09 J.
- At t=3 s: d=0.18 m, Q=-5.555555555555556e-10 C, I=+1.234567901234568e-10 A; force=-3.2241695683334883e-07 N; U=-2.006149953629726e-08 J.
- All 31 signed values, timestamps, world positions/velocities, forces and energy-halving factor match independent image-charge calculations; current strictly increases, d strictly decreases, source never meets guard.
- Independently computed central finite differences of newly evaluated Kelvin **image equilibrium** charges at 29 interior points agree with -dQ/dt; maximum relative error **4.76e-10**. These were fresh independent mathematical image calculations, **not** native M37a function calls; do not falsely label them native re-execution.
- Six separate TEACHER HYPOTHETICAL analytical cases (signed ±q with inward/outward speed, translated oblique axis, modified permittivity, and guarded near-surface case) passed this reviewer-owned SI calculation. They were **not** passed to the uninstalled native production module in this environment. The developer's exact-head 93 tests cover some actual native authored cases, but they do not replace independent novel native tests if a later PASS is considered.
- Source fidelity: exact original PDF digest from actual CI matches the independently registered M37a source; source is workbook physical p8 Multiple Correct Q21/p17 key (1),(3), symbolic q>0, grounded solid R and prescribed inward constant v. The original PDF pages were previously independently visually inspected in M37a; this reviewer relied on that byte-identical source evidence plus an actual CI SHA check and did not claim a new PDF page visual inspection. All numerical inputs remain explicitly **TEACHER-CHOSEN**, never asserted official JEE past-paper data or 31 distinct problems.

## 4. Exact production standalone JSON checker and hostile export tests (passed)

The standalone tools/m37b_source_reference.py was independently checked to have **no production physics imports**; its source was reproduced byte-for-byte (Git blob **eb0da147932789a652580250799399665fa0f098**), executed successfully on the genuine saved source-specific JSON, then given **28 new hostile mutations**. All **28 were refused for meaningful domain, physics, provenance, index, readout or layout reasons**, not setup exceptions.

Attacks included signed and Boolean q, R, world centre, permittivity, duration, signed v, physical position, SI velocity, timestamps, native net sphere charge, both current directions, force and energy half-factor, SI unit labels, Boolean sample/row indices, wrong source answer options, false official-paper attribution, fabricated workbook numerical givens, teacher hypotheses counted as original, Boolean apparatus count, extra source claims, guard crossing, drawn layout radius/point and stale selected caption. These results support the JSON oracle specifically; they do not certify HTML against unaudited static alterations (finding B1).

## 5. Real offline Chromium evidence (authentic artifact passed; stronger hostile checker found gap)

Actual locally installed Chromium via Playwright loaded the unchanged **33,050-byte exact-head HTML**, executing its inline JS/SVG. Because file:// navigation is restricted here, the byte-identical document was loaded with page.set_content, with no network dependency and no browser-side physics calculation. Verification included:

- All **31/31** selected time snapshots, visible t/d/Q/I/opposite-I, fixed radius/centre, source moving position, q label, marker x/y; **all 31 actual SVG polyline points** versus JSON data.
- Restart, Play advancement, 390px mobile layout, visible original/source-versus-teacher attribution, no-JS fallback controls disabled and original first readouts. No JS exceptions and no external requests for the authentic HTML.
- **20/20** forged HTML variants caught by the *reviewer's stronger* verifier: source text and false numeric attribution, hidden provenance, stale first labels/time/distance, wrong current-curve points, sphere radius, sign and sign position, first marker x/y, charge x, slider range/value, changed embedded JSON and an injected unauthorized HTTP image request. The HTTP request was intercepted and refused, not allowed to communicate outward.
- The **production checker** catches most ordinary tampering but explicitly **misses the seven JS-startup-masked no-JS attacks described in B1**.

Original authentic HTML SHA-256: **79d3dc14083486f6079c9b6813d6726394c58971b1130a41dd39444abbfe4f60**. JSON SHA-256: **14dff444a1f0a247423e62a8724863c7df35aeda8d5112e0a21a9fb877e12215**.

## 6. Authoring boundary and limits

Read-only production source inspection confirmed the new strict raw SI factory checks exact scalar and coordinate types before legacy constructor Boolean-to-float normalization. Already-constructed legacy models cannot attest an earlier raw Boolean; this is a documented preexisting limit, not a new false refusal. The new spec enforces one external signed nonzero source, one grounded solid sphere, guard, nonzero signed radial speed, nonrelativistic ceiling, positive duration and bounded sample count. It reuses the M37a Kelvin observer per prescribed sample; no new FEMM/M16a/retarded EM or circuit heat model is claimed.

The reviewer did not perform a fresh checkout or execute novel cases through the full native conductor_sim package locally: GitHub source read and exact-head CI artifact access were available, but the local container could not reach github.com for a clone. No PASS assertion is appropriate until the above release-checker defect is corrected and the remaining explicitly required independently executed native authoring challenges are either completed or documented as legitimately satisfied by further pinned evidence. Neither this finding nor this review reopens the independently accepted unchanged M37a physics.

**Review-harness first-attempt honesty:** The local first file:// navigation was blocked by administrator policy, motivating set_content; a first independent browser harness check used inner_text on an SVG node (fixed to text_content), and the first reviewer JSON no-import assertion inadvertently matched its own docstring (fixed to AST import inspection). Those were reviewer-harness setup failures, not product failures. Later complete runs used bash set -euo pipefail and retained their logs, hostile inputs, screenshots, and saved results.

## 7. Follow-up gate

Keep PR #90 **draft/unmerged**. Make the narrow browser validation patch and add first-frame HTML-only hostile regressions; preserve past red and green CI history. Publish new exact HEAD/TREE and rerun actual source-specific Python + browser acceptance and all required exact-head checks. A bounded independent recheck should specifically prove the seven bypasses now fail, original HTML still passes, and the native novel-authoring evidence requirement is discharged before a future PASS. Only then may the owner separately decide on a guarded merge, identical reviewed tree on main, and postmerge CI.

**No GitHub production code or PR state was changed by this review.** The only GitHub writes are this attributed review and its reproduction script in the independent review_sandbox.
