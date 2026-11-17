# Opticsim PR #118 — independent review request: native directional detector footprint

**Status: final exact-head CI verified; independent Chat B review NOT received. DO NOT MERGE.**

## Candidate, scope and isolation

Source [draft PR #118](https://github.com/physicsvigilante/opticsim/pull/118), `feature/directional-detector-footprint-v1` created **directly from current production main `d3509e82fb65d81aabe336666851f8f2962623f4`**, independently of unreleased v14–v17 optical-object extensions. **Exact final source HEAD `7d44e52d2c4c5db30d91e4e87970b706c18a90f6`**; reviewer must independently verify source Git tree and synthetic CI merge.

The pinned PhyDemo source `811f508d2b070898c241a568b0c167dcb8645251`, simulator, detector/mirror/lens optical propagation, detector `onRayIncident` handler, native hit-event 32-cap collector, original scene versions and old readout defaults **must be unchanged**. New functionality is a **pure derived result on existing opt-in native crossing samples**, not an image solver or new physical component.

## Measurement contract

New request `{ "id":"foot","kind":"detector-directional-footprint","componentId":"Dhit" }` triggers the **already implemented** opt-in native `detector-hit-events` observer, even if no separate hit-events request is present. The unchanged physical detector's ordered finite segment endpoints p1→p2 define unit tangent t and unit **positive left normal n=(-t_y,t_x)** in y-up coordinates. Each actual native hit is independently observed as `pointMm`, `distanceFromP1Mm` and pre-interaction `incomingUnit`.

**Group separation** by sign of incoming dot normal is a *detector-relative crossing orientation*, NOT source attribution or a physical inbound/outbound interpretation. For each sign, compute unweighted sampled count, min/max along detector, mean distance/point, span and **population RMS** sampled spread sqrt(sum((s_i-mean)²)/n). The two direction groups are never paired into ray trajectories, mixed into a false image, or weighted by brightness. With zero hits, count=0 and **mean, centroid, min/max, span and RMS are null**. One sample has RMS=0 as a sampled statistic, **not** zero physical image width.

The new result is available only on the same exact scene hash and fully completed/native qualified run. It uses the existing **32 actual detector-hit bound**, 0.01 mm endpoint exclusion and 1e−5 mm on-segment residual. It independently checks event count against native `detector-crossings`, finite coordinates, actual detector tangent projection, normalized directions (norm error <=1e−7) and fails closed for nearly parallel rays with |u·n|<=1e−8. Such additional classification guards are **readout availability** conditions, not new ray intersection tolerances or native physics changes. Native overflow withholds entire derived footprint, not clipped leading samples. Incomplete/failed/stale run suppresses all requested readings under unchanged host rules. A completed native run with contradictory per-hit input makes **only this new derived result** unavailable; old crossing counts remain intact.

## Source and CI to inspect

Review `src/detector-directional-footprint.js`, `src/observables.js`, `src/native-observations.js`, `scripts/author-scene.mjs`, `src/app.js`, `src/evidence-panel.js`, `src/result-preview.js`, `test/detector-directional-footprint.test.mjs`, `scripts/detector-directional-footprint-acceptance.mjs`, `scripts/detector-directional-footprint-browser.mjs` and the new CI workflow step. Inspect full diff against main for any unexpected optical/native edits.

There are fixed synthetic reference fixtures: `test/fixtures/detector-hit-plate.json` (single native ray through planar n=1.8 and finite mirror; two native detector hits, one in each signed group; independent Snell-derived positions), and `test/fixtures/detector-hit-lens.json` (existing v4 ideal lens + mirror, six forward and five returning native crossings). A separately arithmetic-constructed 45° detector sample checks means and RMS without computing rays. Public CLI tests include complete reflection/refraction, real miss, 33+ crossing overflow and incomplete full-Fresnel withholding. Real Chrome must verify fresh sampling, material-index changes affecting positions, saved qualified export/reopen without embedded native results, empty groups with null statistics, and incomplete suppression. **Do not call any of these an independently executed reviewer-native test unless you actually rerun them.**

Historical R1 detector-hit transfer fixtures and original freeze SHA must stay unchanged. A new *post-exposure* provenance record `test/fixtures/directional-footprint-app-postfreeze-v1.json` records the exact before/after Git blob identity of the viewer opt-in switch, without reclassifying prior tests as blind.

## Final exact-head source evidence (not an independent reviewer-native run)

The final PR #118 source HEAD is `7d44e52d2c4c5db30d91e4e87970b706c18a90f6` with Git tree `f9890d94d91be2e09e00faf9d8c7e6d87531ec47`. Synthetic main-target CI merge `690a4d1fb0f7256a97c59f8b3c1fb2b9e1c4f82c` has the **same exact Git tree**, checked via GitHub commit-object API.

**799/799 supported Node 24 tests PASSED, 11/11 standard workflows successful**, including [unified workflow 44067489898](https://github.com/physicsvigilante/opticsim/actions/runs/44067489898) and [planar/Chrome workflow 44067489904](https://github.com/physicsvigilante/opticsim/actions/runs/44067489904). The new public CLI acceptance script logged **5/5 distinct native outcomes passing**, and the new actual Chrome directional footprint test logged **7/7 checks, 4 screenshots**: forward/return sample groups, physical index edit, qualified export/reopen, genuine detector miss with null centroids and full Fresnel incomplete-run withholding. The prior native hit list's own CLI/Chrome acceptance also passed.

**Historical failed source CI retained:** one initial artifact provenance test copied the wrong old viewer Git blob literal, detected correctly by the test itself. The fixture already held the actual main Git blob; the copied assertion was corrected. No old frozen data, native optics or physical processing was edited to make it pass. The reviewer should inspect first-run failure as well as final CI.

## Adversarial independent checks requested

- Recompute signs for horizontal, vertical, oblique and reversed detector tangent; independently reproduce group means, population RMS and world-coordinate centroids. Check geometric consistency of event records, endpoint margin and raw crossing count reconciliation. Try fake positive/negative ordering, zero hits, exactly 32 vs >32, event arrays with invalid floats, altered point/distance, and unit direction near grazing.
- Confirm that an optional request **by itself** enables one native collector in CLI **and** Chrome, and that default/no-request execution remains byte-for-byte compatible with prior canonical observations. Review whether a malformed optional derived report can alter native detector power or counted interactions (it must not).
- Verify real planar index=1.8 example's two native positions against independent Snell and detector line intersections, and confirm warning qualification discloses Fresnel-off rather than claiming full physical reflectance. Check lens/mirror multiple sampled event groups without asserting source attribution, flux weighting or image formation.
- Scrutinize staleness/completion and overflow safeguards, full-Fresnel tree incompleteness, result preview/evidence panel truthfulness, qualified export and preservation of prior review/frozen experiment data.
- Do not equate these unweighted crossing statistics with an optical point spread function, image position, resolution, irradiance, power in watts or a tracked complete light path. This is a teaching-oriented sampled detector statistic.

## Independent disposition

A separate Chat B should publish a new report to `physicsvigilante/review_sandbox/projects/opticsim/pr-118/reviews/review-01-chat-b.md` **after final exact-head Node 24 and Chrome CI evidence is available**. Cite exact head/tree, independent calculation vs source-native outcomes, findings and residual limitations. Verdict **CLEARED FOR OWNER DECISION**, **INSUFFICIENT EVIDENCE** or **CHANGES REQUESTED**. No human optics expert or complete-image certification is claimed. Chat B cannot authorize source merging; PR #118 and the unreleased prior v14–v17 PRs have independent owner release gates.
