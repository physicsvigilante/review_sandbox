# Independent Chat B review #01 — conductor_sim M40b PR #102

**VERDICT: PASS (FOCUSED, EXACT SOURCE ONLY).**

This is a fresh reviewer-owned scientific and actual-browser experiment, not a developer CI badge and **not owner approval to merge**. The tested native source is production `conductor_sim` commit **`0191ced5c49a1a5d02c9a897867ceca951fb9aca`**, native Git TREE **`5ea6098d463eec12fbc184ab3a6fca2f27699e9a`**. Production PR [#102](https://github.com/physicsvigilante/conductor_sim/pull/102) was rechecked on 2026-11-19: **draft, open, unmerged, exact unchanged head**.

## Scope and provenance gate

Reviewed only M40b real 3D-to-XY projection, signed *pointwise* surface charge density and SI attribution, static isolated/grounded pairing, near-wall original-ray preservation, bounded hostile inputs, HTML escaping/CSP and actual desktop/mobile Chromium. M40a six-cavity physics, older FEMM, and historical JEE PDF problem answers were **not** re-reviewed. M40b makes **zero new original JEE workbook item solution claims**.

The independently executed GitHub Actions [review run #44574672629](https://github.com/physicsvigilante/review_sandbox/actions/runs/44574672629), job #135738814576, completed **SUCCESS on the first actual reviewer execution**. This runner separately checked `git rev-parse HEAD` and `HEAD^{tree}`, saved both, compared the live charter with the charter-only original commit `e429bd422b321d5dd7c87c14fa18248eabcd57e5` (byte-identical), and verified the original frozen PDF SHA-256:

- `02_conductors_half_size.pdf` = `9dff3c02a9f1848d2c3d99cb1a6e7a44dc7f5a51f7a3a2b8cc92d10ce1fbca5d`
- `POTENTIAL_CONDUCTORS1.pdf` = `8d0d9b5cf821219058cfc4b7685a39b777e460944df44c3f9cffcb68157a60e5`
- Frozen `docs/m40b_charter.md` SHA-256 = `0a7042a41e2c432a9a2ff5d283cedf1171299d2f88e750f5bccfd7c24c59acb4`.

Native comparison against the released M40a production baseline `14ba75e9e8f8b5904eb774e0789b5f56a9a58223` confirms **exactly eight newly added files**, all in the announced allowlist. No M40a solver, M39a Gauss kernel, original viewer, or original JEE PDF was edited by PR #102. This was enforced independently with `git diff --name-status` and the source and tree checks.

The rechecked exact-head production CI has **24/24 completed-success workflow runs**: 22 pull-request events and two push events, including focused M40b physics/real Chromium; no pending or failing current-head workflow remained. Historical initial red M40b push/PR runs, including [#44565691642](https://github.com/physicsvigilante/conductor_sim/actions/runs/44565691642) and [#44565676598](https://github.com/physicsvigilante/conductor_sim/actions/runs/44565676598), remain untouched.

## Reviewer-owned unfamiliar physical case

Unlike the developer teacher sample, the independent model places **two genuine disjoint spherical cavities at the identical projected world XY center** `(1.6,-0.2)`, with true centers **`(1.6,-0.2,-1.9)`** (radius `0.90 m`) and **`(1.6,-0.2,1.7)`** (radius `0.85 m`). Their true 3D center distance is **3.60 m**, exceeding the sum of radii **1.75 m**. A third empty void lies at `(-1.4,-1.5,0.7)` with radius `0.5 m`; the outer sphere is translated to `(1.2,-0.9,0.4)`, radius `6.5 m`. Four original, distinct off-axis charge-source IDs are linked to their authentic 3D positions. The lower cavity carries `+3.1e-9 C` and `-3.1e-9 C` (whole inner face `0 C`), the upper cavity `+1.7e-9 C` and `-4.0e-9 C`, and the third cavity is empty. Authored isolated metal charge is `+8.1e-10 C`.

Independent containment, noncontact/disjointness, source identity, XY projection center, radius, source marks, and common outer metre scale were tested; genuine Chromium confirms the projected rings overlap at the exact same XY center while the page and source table expose their distinct Z coordinates. Nothing depicts overlapping physical 3D holes, a cut plane, a 2D electric-field solution, or chronology.

## Independently calculated signed physics (100+ decimal digits)

The reviewer implemented an independent **110-digit Decimal real-charge plus Kelvin-image normal-electric-field oracle**. For each source at local cavity position `p` and radius `R`, the independent oracle places its image at `R²p/|p|²` with image charge `-qR/|p|`, forms the real and image fields at the spherical wall, and evaluates conductor inner-face `sigma = -epsilon E·n` from the **unrounded admitted raw binary64 ray**. No expected value was obtained from M40b, M40a Poisson-kernel implementation, or the supplied M40b reference checker.

**150 signed per-state density observations** (three cavities × 25 original rays × two independent isolated/grounded states) were compared with relative tolerance **5e-11**, with **worst observed relative error `8.203646984987296e-15`**. The lower signed-neutral cavity has **24 positive / 1 negative** sampled point; the other charged cavity **15 positive / 10 negative**; the empty cavity **25 exact zeros**. Native whole-face Gauss values are separately correct, never approximated by summing sample tiles. Grounded outer sigma and charge are exactly zero. The isolated outer whole-face charge is **`-1.4900000000000004e-9 C`**; the outer sphere density follows `Q/(4*pi*R²)`. All 150 inner measurements match between the two *static* electrical constraints.

A **new oblique, nonzero-Z almost-unit near-wall raw ray** `(0.36996300554937117,-0.5199480077991163,0.7699230115486914)` was admitted. High-precision image-field evaluation yielded authentic `-2014476.5305739806 C/m²`; substituting the binary64 rounded display normal would yield `-2014476.5254708396 C/m²` (relative error **`2.5332343127165665e-9`**, demonstrably above the comparison tolerance). The actual exported sample and rendered HTML follow the original raw ray. A further requalified teacher hypothetical relocates the near-wall charge as a **new static model**: native values change appropriately, and separate isolated/grounded pair and M40b witness checker pass; no source motion is claimed.

## Visible-to-witness and hostile integrity

The independently generated HTML and saved M40b JSON were compared against the *actual* physical scene and native v2 witness. Source IDs, signs, charges, true XYZ, Gauss whole-face totals, pointwise signed `C/m²`, theta from +Z, phi from +X toward +Y, display-only unit normal, raw input ray, and electrical-constraint identity are consistent. **35 hostile cases refused**: separately changed visible source identity/charge (including Boolean), source Z, cavity XY/Z/radius, whole-face charge, local signed sigma, raw ray, display normal, theta/phi, outer face/grounded density, unit metadata and role flags; witness-layer original ray, normal, source position and sigma; state-witness swap; nonfinite numbers, cancelled/source tamper, bad/overlong normals, Boolean/nonfinite charges, forbidden HTML-like IDs, physically impossible source placement and truly intersecting cavities.

### Real browser

Reviewer-owned GitHub Actions installed actual Playwright Chromium `143.0.7499.4` via Playwright `1.57.0`, loaded the fresh standalone HTML with **JS enabled and disabled**, at **1280×820 desktop** and **390×844 narrow mobile**. All four runs checked **75 genuine signed point tiles**, full signed SI against the manifest, source and cavity XYZ text/IDs, physical SVG geometry and source markers, sign-aware CSS classes, θ/φ text, zero remote requests, and mobile horizontal-scroll affordance. Screenshots from all four viewports were recorded and inspected (both desktop and mobile); the user-readable warning and source Z are visible; mobile overflow is horizontally scrollable. A script added to a copied HTML file was **blocked by CSP**; invalid script-shaped source IDs were rejected before rendering. No JavaScript is needed to show the original scientific data.

## Caution: externally edited HTML is NOT authenticated

A malicious **post-export alteration of static HTML text** can display `9999 C/m²` while an unchanged, authentic JSON manifest still passes the **JSON-only** independent checker. The reviewer demonstrated this explicitly with `forged-visible-html.html`. This does **not** compromise native renderer-from-typed-solution correctness or its HTML escaping/CSP, and it does **not** contradict the declared boundary: neither edited external HTML nor wholly self-consistent rewritten JSON has an authenticated teacher-history origin. But it is important not to claim that the JSON-only checker independently authenticates an arbitrary distributed HTML file. If future releases promise verified *downloaded HTML bytes*, they must add a trusted source anchor and an HTML-to-manifest/digest check. This is a documented boundary and optional future hardening, **not an M40b scientific display blocker**.

## Evidence links and exact replay

- Reviewer-owned experiment source: [review-01-chat-b-probes.py](review-01-chat-b-probes.py); native experiment script SHA-256 `c851df0308cb33d70fcf13f4e793135af921b65b69ee6a9694917802c4f71096`.
- Replay workflow: [m40b-pr102-chatb-review01.yml](../../../../.github/workflows/m40b-pr102-chatb-review01.yml) (path from repository root: `.github/workflows/m40b-pr102-chatb-review01.yml`).
- Exact new full green [review Actions run #44574672629](https://github.com/physicsvigilante/review_sandbox/actions/runs/44574672629) and [18-file evidence ZIP, artifact #14555382909](https://github.com/physicsvigilante/review_sandbox/actions/runs/44574672629/artifacts/14555382909) (retained for 30 days). Archive contains SHA/TREE, changed file list, source hashes, frozen charter, original logs, complete independent density JSON, manifest, HTML, hostile refusals, relocation model, four genuine browser screenshots and summary JSON. This is first-attempt actual reviewer evidence, not a synthetic report.
- Developer green focused [M40b push #44569718416](https://github.com/physicsvigilante/conductor_sim/actions/runs/44569718416) is corroboration only; it was **not substituted** for this review.

**Final gate:** PASS for the specified production HEAD/TREE and scoped M40b release contract. If production HEAD/TREE changes, this PASS is no longer applicable without review of the delta. This PASS is **not permission to merge**; PR #102 must remain draft/unmerged until a separate explicit owner approval, expected-head guarded merge, reviewed tree equality after merge and completed actual successful post-merge main-push CI. No auto-merge, no production modification, no original PDF mutation, and no edits to prior M40a evidence were performed.
