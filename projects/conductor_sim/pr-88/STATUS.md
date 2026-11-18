# M36e PR #88 — Original p26 answer presentation and evidence review status

**2026-11-18: draft source candidate is OPEN/UNMERGED, no independent Chat B verdict or owner merge authorization. Full source PR CI still in progress at packet publication.** Any old completed green workflow should not substitute for current-source complete CI.

- **Production source PR:** https://github.com/physicsvigilante/conductor_sim/pull/88.
- **Exact current candidate HEAD:** `75ef212d79dc26ff97621fb1f2ed4e287bbed56d`; **actual native Git TREE:** `f5be8433b39cf8827c19da1cd0586869347a33f4`.
- Released owner-approved M36d merge/main base `8bca8e5d1c157e05b3f04e6185e927bd7ee79941`; reviewed tree `523d02e95dbb4791acd630f9c535eb552262c606`; **20/20 actual main-push workflows passed** (filtered event `push` and head branch `main`).
- Frozen preregistration M36e charter-only commit `77957e7509280e891197789be143784bae692a7b`.
- [Full independent scientific/browser request](REQUEST.md) · [Fresh reviewer prompt #01](REVIEWER-PROMPT-01.md).
- Expected new reviewer-authored report `reviews/review-01-chat-b.md` is **not published** when this packet is written.

## Real source change and honest limits

M36e is a **small source-specific JEE p26 source-answer viewer refinement**, NOT a new production field law, FEMM physics, general viewer, motion system or original-JEE apparatus. In the released M36d, actual p26 original `SolidSphere` V(R/2) and V(3R/2) were mathematically correct in saved native results, but not both visible together; old generic profile heading implied induced-charge density for isolated fixed-Q solid, and 37×37 circle-boundary sampled colours looked blocky.

Updated `tools/m36d_true_solid_sphere.py` renders actual **V(R/2), V(3R/2), |E(R/2)|, signed outer sigma with SI units** visibly together, with source-versus-teacher R/Q and original illustration distinction, as one accessible state-aware answer card per existing stored-state slider. The state cards come from REAL saved `MixedRadialBackend` outputs. Default original visible without JS; two later states are expressly teacher hypotheses (negative Q/radius/shifted centre and grounded). Only this p26 viewer labels isolated charge density correctly; inherited general M5 “Induced surface-charge profile” remains untouched. Sampling increases to **65×65 real physical grid points**; no claim of antialiased/pixel-perfect metal edges or a new solver.

**No production solver/ODE/FEMM, original PDF, old M6 baseline, M36a 30-case inventory or public M5 template changes.** One previously audited original JEE p26 apparatus, two teacher worlds, zero original-coverage increment; no `N/30` success rate.

## Developer-controlled source-first actual execution

- Initial [branch CI #44281302235](https://github.com/physicsvigilante/conductor_sim/actions/runs/44281302235) **FAILED** 1/41 new/old tests because the new HTML assertion required the `hidden` attribute adjacent to `data-m36e-state` instead of accepting a valid middle `data-m36e-role`. Physics/rendering was NOT changed by the correction; original red attempt is retained.
- Corrected source branch [CI #44281477440](https://github.com/physicsvigilante/conductor_sim/actions/runs/44281477440) **COMPLETED SUCCESS** at exact HEAD/TREE after **41 focused tests**, **3 actual native physics states**, **3 separate no-production-import SI Gauss checks**, **3 actual offline Chromium state frame checks** with native values visible and numeric units accurate, **7/7 intentional real Chromium forgeries refused** for intended source/provenance reason. Entire Git source HEAD/TREE and original PDF SHA verified and retained.
- GitHub Actions evidence artifact **14416662754**, name `m36e-true-p26-original-visible-source-answers`, provider-reported ZIP SHA256 `55596b28a0b2491b1d1d2fd9f67c78578c7eddf4a5e77ccdcb227fff39296c66`; Chat A did not independently download and rehash it, and these checks were **developer-authored/orchestrated**, not an independent Chat B scientific/visual verdict.

## Remaining release gates

1. FULL candidate `75ef212d79dc26ff97621fb1f2ed4e287bbed56d` source-head PR and push CI **all actually complete success**, including Python 3.10 and 3.12, genuine FEMM5, complete historical Chromium, M36b/c/d unchanged regression and new M36e source/native/real-browser gate. Initial snapshot was queued/in progress; check live.
2. Separate-context reviewer must independently open original p26 notes PDF where possible, check mathematical source formula/teacher labels, inspect three actual HTML/screenshots, verify true solid/one outer face, independently invent and execute native/display manifest forged data attacks on real source data and strict refusal boundary, not merely rely on 41 author tests.
3. Reviewer publishes a NEW original report `reviews/review-01-chat-b.md` with exact HEAD/TREE and PASS / CHANGES-REQUESTED / INSUFFICIENT-EVIDENCE. Preserve first failed CI and any reviewer failures. This is **review scientific evidence, not owner release authority**.
4. Require explicit separate owner merge approval after no-blocker review, guarded expected-head merge, reviewed exact native TREE equality and every actually triggered postmerge `main` push workflow successful.

**Original physics scope:** genuine single solid conducting sphere in charge-free vacuum, no external-point-charge-induced distribution, current versus time, irregular 3D cavity/local field, or automatic general PDF/LLM authored problem completion. Browser presentation is not simulated dynamics.
