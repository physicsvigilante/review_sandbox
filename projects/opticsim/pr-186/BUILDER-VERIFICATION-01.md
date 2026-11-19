# Opticsim PR #186 — exact-source builder verification and ONE independent-review handoff

**Date: 2026-11-20 (IST). Status: builder-verified, DRAFT, UNMERGED, NOT independently cleared.** This report describes builder CI and archived real native/browser evidence; it does not stand in for an independent reviewer, a textbook J09 solution, a public deployment or the owner's release decision. Full review target: [Opticsim PR #186](https://github.com/physicsvigilante/opticsim/pull/186).

## Exact Git identity — separately fetched source and synthetic merge objects

| Item | Verified Git SHA |
|---|---|
| Current production main / parent | `dcdaf6361a1aea151b15cde925d27ea9fe39ad9e` |
| **Exact final PR #186 source head** | **`a05e4ac88afcd23e17fe07c4be8c8076b5c628c3`** |
| **Source Git tree** | **`ad100b92d2f6a9c061a59f13311f0bb3c06b65a8`** |
| Tested GitHub PR synthetic merge | `163b1519aeb7f31c203e0e58de440ba7bb59860e` |
| Tested synthetic-merge Git tree | **`ad100b92d2f6a9c061a59f13311f0bb3c06b65a8`**, identical to exact source |
| Synthetic-merge parents (ordered) | [current production main, exact PR head] |
| Pinned upstream PhyDemo | `811f508d2b070898c241a568b0c167dcb8645251`, release v5.4.0 |
| Upstream pin file Git blob in **both** main and PR | `c371abf2169bba28b1c400d022b55caf78cb647c` |

The builder independently fetched actual source and synthetic-merge Git commit objects through GitHub and compared the tree SHA. This **does not claim a separate in-job tree comparison**. The exact-head branch has 21 changed paths: **9 added, 12 modified, 0 deleted**. No existing upstream native physics source or pinned checkout was patched. Production main remains unchanged by PR186.

## Physical scope: new isolated, JEE-adjacent v25 native GRIN

The prior two research-only milestones [PR184](https://github.com/physicsvigilante/opticsim/pull/184) and [PR185](https://github.com/physicsvigilante/opticsim/pull/185) established raw pinned `GrinGlass` ray stepping and preregistered analytical first-integral step-size comparison. They were not public GRIN admission or the originally source-faithful J09 problem solution. PR186 adds an **explicitly bounded** new public *candidate* `schemaVersion=25`, model `native-bounded-grin-tracing`:
- Exactly one ordinary SingleRay `point-source` starting **inside** the physical rectangle, horizontal 0°, near its left face; exactly one `graded-index-rectangle` and one downstream **real passive vertical Detector**. No other optical components.
- All physical geometry and units explicitly authored. Only one fixed trusted native functional family `n(y)^2=1.5+(y-axisY)/(1 mm)`, physical index real, positive and >=sqrt(1.1) throughout; exterior medium fixed and explicitly stated as n=1; partial Fresnel reflections disabled by explicit `partialReflection=false`, native TIR not silently disabled. **No arbitrary user LaTeX expression is evaluated**.
- **v25-only** native numerical policy: Euler integration step 0.0025 mm, maxRayDepth 1024, processedRayLimit 2048 and rayDensity 0.2. **v1–v24 keep their original numerical budgets and contracts**.
- Compiler produces genuine pinned native `GrinGlass` from an allowlisted expression and numeric arguments. The real pinned engine chooses all steps and exit refraction; **no route, source fact, image or detector hit is prescribed**.

`src/native-grin-v25.js` attaches exact per-instance **observation** wrappers to native source, GRIN and detector callbacks. They preserve the native incident/start delegates and rays, record bounded real source, internal step and detector evidence, and compare observations with the **independently derived continuous-field first integral** and Snell/free-space detector prediction for the *same* explicit physical facts. Missing/extra rays, invalid or uninspectable callbacks, >=1024 internal callbacks, reference deviation > **0.002 mm**, incomplete/stopped/truncated/undefined raw native run or hash-stale scene **must withhold all qualified readings even if the raw native engine emitted `simulationComplete`**. The 0.002 mm criterion is a local observed-accuracy qualification, **NOT a universal Euler error bound or proof of exact J09 physics**.

A **test-only** coarse step 0.04 mm (not authorable through v25) causes raw PhyDemo completion but the v25 observation gate reports **failed/withheld-uncertain**, and raw detector-hit event positions are not released as qualified measurements. No extra resolution or ray repair is attempted.

## Presentation-only native render fix — review explicitly

Initial v25 Chrome screenshots showed the 1mm apparatus as a nearly invisible 2px shape. A first close-up at zoom 80 made native SingleRay point glyphs, Detector markings and the ray pen enormous, falsely obscuring the GRIN geometry. This was corrected before freezing the final source. **The actual final archived screenshot** visibly shows the physically bounded purple native glass region, a thin actual pinned native ray, small source marker and finite passive detector.

`src/grin-v25-display.js` is a **v25-only, per-Simulator, instance-local presentation adapter**. The original native PhyDemo `CanvasRenderer.lengthScale` governs pen/glyph sizes in world coordinates; the wrapper sets only those **renderer instances'** lengthScale to `1/(scene.scale*dpr)` at the beginning of each native draw invocation, then invokes the **original pinned native draw exactly once**. It never changes physics-sensitive `scene.lengthScale`, GRIN integrator step, native `onRayIncident`, source `onSimulationStart`, source/medium positions or ray state. Tests assert no effect on v24 or other older schemas, atomic refusal on malformed renderer delegates and real native detector/crossing equality under zoom/Fit.

The v25 camera defaults to 80 CSS pixels/mm; its **only-version** bounded presentation zoom extends to 100, and Fit uses the real browser canvas dimensions. Older versions retain their previous 0.03–10 document zoom bound, historical fitted zoom <=2 and pan behavior. Final v25 browser screenshot must be inspected visually, not just the test's logical PASS flag. No image or path derived from arbitrary assistant prediction was painted.

The final PR's integrated app Git blob is **`553c71a1393be89a30f326d366a7caae388c595e`**; the original independently reviewed v24 integration app blob `ac8ee9e3bf448c4280342d9049052bbbce1691b0` and historical v18 app blob `cfbea455df3f7ea7a30002d0139730c25b235d32` are preserved **as historical provenance**, not recertified as new-v25 binary. The new app blob is bound to `test/fixtures/grin-v25-app-integration-v1.json`.

## Exact-final builder CI, evidence and checks

- **11/11 exact final PR-head workflows SUCCESS** on `a05e4ac88afcd23e17fe07c4be8c8076b5c628c3`. No failures/skips. [Optical composition CI run 44614310435](https://github.com/physicsvigilante/opticsim/actions/runs/44614310435), job [135878787234](https://github.com/physicsvigilante/opticsim/actions/runs/44614310435/job/135878787234) shows **1,047/1,047 Node24 tests**, zero failures, genuine browser setup and complete native/browser suite. Historical v1–v24 regressions remain green.
- Actual v25 public acceptance [`scripts/jee-bounded-grin-v25-acceptance.mjs`](https://github.com/physicsvigilante/opticsim/blob/a05e4ac88afcd23e17fe07c4be8c8076b5c628c3/scripts/jee-bounded-grin-v25-acceptance.mjs) passed **15/15 synthetic cases: 5 genuine native-qualified runs, 10 correctly rejected before native**. Includes changed source x, translated/apparatus size controls, missing essential index, forbidden arbitrary index, out-of-domain n, wrong gradient, Fresnel and run policy, off-axis/grazing launch, missing detector/cross-family mixing.
- Positive native v25 baseline records **366 actual internal GRIN step callbacks**, one emitted ray, one native detector crossing, actual max internal step-position discrepancy ~**0.0003693149 mm**, detector discrepancy ~**0.0004481155 mm** from the independent conditional analytical reference. Both within the **0.002 mm** local gate. **No global error guarantee or detected physical image**.
- Real **Google Chrome for Testing 158.0.8127.36** v25 browser suite passed **9/9 checks, 4 PNG screenshots**, including close-up Fit, unchanged real native detector hit after presentation-only view change, physical source x edit causing a new hit, invalid boundary refusal, qualified export and reopen; zero runtime exceptions/off-origin network requests. Existing v19–v24 Chrome remains passing.
- The builder downloaded exact [final optical/native/Chrome artifact 14573818134](https://github.com/physicsvigilante/opticsim/actions/runs/44614310435/artifacts/14573818134). Actual ZIP SHA-256: **`295fdff190439cbeadb7caa285f00ea1dd90210633491cad495b569856b640c5`**, equal to GitHub digest; all **537 ZIP member CRCs passed**. Parsed archived v25 acceptance (5 native completions, 10 zero-native refusals) and genuine v25 Chrome report/representative fit screenshot. Recomputed **84/84** archived source input/report SHA-256 pairs from the literal raw `input.json` bytes, **zero mismatches**.
- Final authoring [artifact 14573508671](https://github.com/physicsvigilante/opticsim/actions/runs/44614310435/artifacts/14573508671) has GitHub SHA-256 `70067c54936064fca3da2c8231e5453102dcb19f7dc1ffdb4cb81135954c4850`. [Planar CI run 44614310424](https://github.com/physicsvigilante/opticsim/actions/runs/44614310424) passed the retained refraction/browser checks.

The initial development CI red attempts were retained in GitHub: provenance assertions still expecting the old v24 app SHA/catalog count; an HTML range step that represented 80 as 80.03; and an excessively large native-renderer glyph in the screenshot. These were fixed by *version-specific* tests/provenance, display precision and a rendering-only adapter. The source GRIN numerical physical solver and fixed 0.002 mm acceptance threshold were **not relaxed**. The final source CI is green.

## ONE independent review requested: requirements

Review the exact [PR186](https://github.com/physicsvigilante/opticsim/pull/186) final source SHA **`a05e4ac88afcd23e17fe07c4be8c8076b5c628c3`** and tree **`ad100b92d2f6a9c061a59f13311f0bb3c06b65a8`**. Inspect actual final source/CI and artifacts, rather than treating builder claims as clearance. Focus on:
- Differential first-integral correctness, physically positive n² domain and explicit dimension scaling; real native GrinGlass Euler/exit physics vs measured callbacks; **0.002 mm local pass/fail and hidden numerical loopholes**; callback delegate-once and consistent no-qualified-hits on any audit fault or native incompleteness.
- No arbitrary index expression access; isolated v25 numerical policy, strict geometry/units/indices/source mode and cross-family refusal, original v1–v24 schema/CI/browser invariance, stale/revision/hash suppressions and no fabrication of an image/route.
- The **new per-instance rendering adapter**: real CanvasRenderer-only adjustments and no effect on physics-sensitive `scene.lengthScale`, native callbacks, physical extents or old schemas. Examine the final close-up screenshot to confirm the ray and rectangle are visually faithful and source/edit outcomes remain actual native evidence.
- Exact reviewed Git tree equals CI-tested synthetic merge; verify genuine Chrome and archived native evidence integrity. Avoid rerunning old v14–v24 standalone physics reviews when the original source is unchanged. Research PR184/185 support feasibility but are *not* independent v25 physical clearance.

**Mandatory published deliverable:** Commit a full independent Markdown review to the default branch of `physicsvigilante/review_sandbox` at:

`projects/opticsim/pr-186/reviews/review-01-chat-b.md`

Read back the committed report, return the immutable permalink, actual review commit SHA, exact reviewed source SHA and final verdict **CLEARED FOR OWNER DECISION** or **CHANGES REQUESTED**. Do **not** modify source, merge or deploy. A chat-only verdict is insufficient. If GitHub publishing fails, clearly report that it was not published.

**Builder disposition: exact source CI/evidence verified, new v25 public physics held DRAFT AND UNMERGED, independent numerical/integration review PENDING.** Production remains `dcdaf6361a1aea151b15cde925d27ea9fe39ad9e` with only v1–v24 public admission.
