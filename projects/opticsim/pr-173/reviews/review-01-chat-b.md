# Opticsim PR #173 — Chat B focused independent follow-up review (archived review 01)

**Review date:** 2026-11-19  
**Reviewed repository / PR:** [physicsvigilante/opticsim #173](https://github.com/physicsvigilante/opticsim/pull/173)  
**Previously reviewed source:** `d6e5d404a2e159d1d6d14b38d353108fe09c3c03` (tree `6b953f3f8c3ce93238f062bb076cd6f68f349e04`)  
**Exact corrected source reviewed:** **`efa7ac9ddbed0bf82ce529d16f754036a6d7f79f`**  
**Corrected Git tree:** `526cf3c1e5e47c1e5e0c0d38a4c733bfb0a08201`  
**PR base:** `59b485d14ac28ca4ee97acc754a4cd207a7d33f1`  
**PR synthetic merge:** `b7d1d648c3e0de3d30936303e04faf1734a07bef`, same verified tree, ordered parents [base, corrected head]  
**Disposition:** **CLEARED FOR OWNER DECISION**  
**Confirmed P0/P1 blockers:** **None within this seven-file correction and its inspected integration paths.**  
**Merge authorization:** **Not granted by this review.** PR remains draft and unmerged; owner must decide separately.

## 1. Scope, provenance and review method

This is the **first archived Chat B report for PR #173**. The prior *PASS WITH CONDITIONS* was an **unarchived, user-provided read-only review** of the earlier source SHA; it was **not** a previously published GitHub review or a review of the correction. Its requested follow-up focused on a real later near-vertex native callback, non-normal Snell, critical-angle boundaries and two detectors. This report does **not** repeat the original full architecture/physics review.

I independently fetched the pinned corrected and prior source files, compared the two Git commits and the current source/merge Git objects, inspected the qualification/measurement integration, independently computed numerical refraction and boundary values, and directly inspected GitHub workflow statuses, an optical-job log, a red-stage job log, and artifact metadata. **I did not execute pinned PhyDemo, Node tests, a browser/Chrome, or GitHub Actions myself.** All quoted native callbacks, detector positions, authored public workflows and screenshots are **builder-operated GitHub CI evidence**, independently inspected as evidence rather than re-executed reviewer tests. Independent calculations below are standalone mathematics, not a second ray-tracer or native runtime reproduction.

GitHub [commit comparison](https://github.com/physicsvigilante/opticsim/compare/d6e5d404a2e159d1d6d14b38d353108fe09c3c03...efa7ac9ddbed0bf82ce529d16f754036a6d7f79f) reports **3 commits ahead, 0 behind, exactly seven changed paths**:

| Changed path | Focus of independent inspection |
| --- | --- |
| [src/prism-beam-qualification.js](https://github.com/physicsvigilante/opticsim/blob/efa7ac9ddbed0bf82ce529d16f754036a6d7f79f/src/prism-beam-qualification.js) | New v22-only 0.1-mm and 1e-5 critical thresholds, necessary incident Snell test |
| [src/native-prism-beam.js](https://github.com/physicsvigilante/opticsim/blob/efa7ac9ddbed0bf82ce529d16f754036a6d7f79f/src/native-prism-beam.js) | Shared named thresholds; unchanged 0.1-mm initial sample-screening semantics |
| [src/triangular-prism.js](https://github.com/physicsvigilante/opticsim/blob/efa7ac9ddbed0bf82ce529d16f754036a6d7f79f/src/triangular-prism.js) | v22 callback clearance argument; legacy v8 default remains 0.01 mm |
| [src/finite-glass-geometry.js](https://github.com/physicsvigilante/opticsim/blob/efa7ac9ddbed0bf82ce529d16f754036a6d7f79f/src/finite-glass-geometry.js) | Optional inclusive vertex check; old strict-less-than default retained |
| [src/planar-media.js](https://github.com/physicsvigilante/opticsim/blob/efa7ac9ddbed0bf82ce529d16f754036a6d7f79f/src/planar-media.js) | v22 schema gate and observation-only native hit checks; exact original delegation |
| [test/jee-prism-beam-v22-review-conditions.test.mjs](https://github.com/physicsvigilante/opticsim/blob/efa7ac9ddbed0bf82ce529d16f754036a6d7f79f/test/jee-prism-beam-v22-review-conditions.test.mjs) | Five focused tests with raw-native versus injected provenance |
| [docs/NATIVE-PRISM-BEAM-V22.md](https://github.com/physicsvigilante/opticsim/blob/efa7ac9ddbed0bf82ce529d16f754036a6d7f79f/docs/NATIVE-PRISM-BEAM-V22.md) | Explicit risk envelope, old-version retention, and limitations |

No pinned PhyDemo implementation or ray-propagation source was modified by this correction; the documented pinned engine stays `811f508d2b070898c241a568b0c167dcb8645251`. The new checks determine *qualification of evidence*, never replace native Snell/Fresnel, choose a ray branch or edit outgoing rays.

## 2. Vertex clearance: v22-only and historical preservation — PASS

**Source tracing:** [planar-media.js, lines 55–85](https://github.com/physicsvigilante/opticsim/blob/efa7ac9ddbed0bf82ce529d16f754036a6d7f79f/src/planar-media.js#L55-L85) applies the enlarged clearance **only** when the component is a prism **and** `doc.schemaVersion===22`. [triangular-prism.js, lines 47–54](https://github.com/physicsvigilante/opticsim/blob/efa7ac9ddbed0bf82ce529d16f754036a6d7f79f/src/triangular-prism.js#L47-L54) passes the supplied 0.1-mm threshold into the shared helper with inclusive mode enabled; omitted arguments use historical `PRISM_CLEARANCE_MM=.01`. [finite-glass-geometry.js, lines 29–43](https://github.com/physicsvigilante/opticsim/blob/efa7ac9ddbed0bf82ce529d16f754036a6d7f79f/src/finite-glass-geometry.js#L29-L43) implements the exact predicate `distance <= clearanceMm` in inclusive mode and `distance < clearanceMm` in its unchanged default. The previous tree's helper used the same strict `< clearanceMm` default. The v9 polygon caller also continues passing 0.01 mm with no inclusive opt-in.

**Boundary logic independently inspected:** v22 rejects hit distances **below or equal to** 0.1 mm (including the mathematical equality), whereas v8 rejects distances **strictly below** 0.01 mm; at the mathematical 0.01-mm equality v8 does not exclude by vertex distance alone. Both are Euclidean distances to the triangle vertices at **actual native callback points**, not a guessed outgoing trajectory. The existing v22 emitting-segment and initial deterministic sample checks still reject the 0.1-mm inclusive initial-vertex band [native-prism-beam.js, lines 39–61](https://github.com/physicsvigilante/opticsim/blob/efa7ac9ddbed0bf82ce529d16f754036a6d7f79f/src/native-prism-beam.js#L39-L61). The native observer records `invalidObservations` rather than changing the native return [planar-media.js, lines 72–85](https://github.com/physicsvigilante/opticsim/blob/efa7ac9ddbed0bf82ce529d16f754036a6d7f79f/src/planar-media.js#L72-L85).

**Evidence distinction:** builder's raw native experiment observed later callbacks at 0.0517580189739361 mm; a **separate artificial 0.05-mm callback** tested v22 invalidation against v8 acceptance and verified a single delegate call. These are distinct experiments. The corrected test does not demonstrate a separate pinned-native callback lying at **exactly** 0.1000000000000000 mm, so inclusive equality is supported by direct code/predicate inspection rather than a reviewer-run binary64 boundary experiment. This is a non-blocking coverage opportunity, not evidence of a regression.

## 3. Independent signed, non-normal Snell check — PASS

Using the explicit authored short prism with y-up vertices `(0,-70), (0,70), (20,0)` mm and `n_inside=1.5`, `n_outside=1`, a horizontal ray enters the flat face normally and exits a genuinely sloping face. Independently from the native callback ledger:

- `theta_i = atan(20/70) = 15.945395900922854°`.
- `theta_t = asin(1.5 sin(theta_i)) = 24.335670676828293°`.
- For both faces the unit outward normal is `(70,+/-20)/sqrt(5300)`; the direction normal cross-product has opposite signs on the two faces. With the convention `cross(incoming,normal)`, the independently required signed tangential Snell value is **+0.412081691846067** on face-23 and **−0.412081691846067** on face-31, equal to `n_outside*cross(outgoing,normal)` in each case. The outgoing unit directions consistent with this are approximately `(0.989297114433502, -0.145915110161857)` and `(0.989297114433502, +0.145915110161857)`, respectively. Both have positive outward normal projection.

The test checks the signed equation with actual observed `incoming`, `outgoing` and `outwardNormal`, **on both faces** [follow-up test, lines 29–64](https://github.com/physicsvigilante/opticsim/blob/efa7ac9ddbed0bf82ce529d16f754036a6d7f79f/test/jee-prism-beam-v22-review-conditions.test.mjs#L29-L64). The exact-head [builder optical CI log](https://github.com/physicsvigilante/opticsim/actions/runs/44501950972) prints `JEE_V22_OBLIQUE_SNELL` with `15.945395900922856°`, `24.335670676828293°`, zero native TIR and four crossings. These numbers match the independent mathematics to rounding. This verifies the test's physical expectation; it is **not** an independently executed native ray run.

## 4. Critical-angle boundary and fail-closed qualification — PASS

For the same 70-mm half-height and 1.5:1 exit indices, independent analytical quantities are:

`theta_c = asin(1/1.5) = 41.810314895778596°`, and `x_c = 70 / sqrt(1.5² - 1²) = 62.60990336999411 mm`.

Defining the **signed** necessary Snell residual `R=1.5*x/sqrt(x²+70²) - 1` for an interior ray approaching a sloping face:

| Apex offset from x_c | Independent signed R | Physical side of boundary | Builder's **raw pinned-native** observation | Qualified v22 |
| --- | ---: | --- | --- | --- |
| −0.000001 mm | −8.87328566e−9 | below critical | 2 recorded transmissions, 0 TIR | failed; all requested values suppressed |
| 0 mm | 0 (within binary64 rounding) | exact numerical boundary | 0 recorded transmissions and 0 TIR; no branch outcome inferred | failed; all requested values suppressed |
| +0.000001 mm | +8.87328544e−9 | above critical | 0 recorded transmissions, 2 TIR | failed; all requested values suppressed |

These independent residuals are all well within the new **1e-5 dimensionless** exclusion band. The builder log reports absolute minimum residuals 8.873285661792352e−9, 0, and 8.873285661792352e−9 (small rounding difference above critical is immaterial). All three separately replayed raw-native scenes emitted `simulationComplete`, but this **does not** imply qualification. On the canonical qualification path they report `native.status='failed'` and suppress the requested results.

The v22 test does **not** invent a critical transmitted ray: it obtains actual native incident directions and normals at the selected Glass hit and uses only the necessary equation `abs(n1*abs(cross(incoming,normal))-n2) <= 1e-5` **when `n1>n2`**, after the native hit has been selected [qualification module, lines 1–16](https://github.com/physicsvigilante/opticsim/blob/efa7ac9ddbed0bf82ce529d16f754036a6d7f79f/src/prism-beam-qualification.js#L1-L16); [planar-media.js, lines 73–85](https://github.com/physicsvigilante/opticsim/blob/efa7ac9ddbed0bf82ce529d16f754036a6d7f79f/src/planar-media.js#L73-L85). Native still decides transmission/TIR.

**Integration independently traced:** [check-scene.mjs, lines 19–83](https://github.com/physicsvigilante/opticsim/blob/efa7ac9ddbed0bf82ce529d16f754036a6d7f79f/skills/sim-ro-image-to-scene/scripts/check-scene.mjs#L19-L83) combines observer errors with native diagnostics via `core.Session`; `executionPassed` requires completion and validated roundtrips. [author-scene.mjs, lines 30–57](https://github.com/physicsvigilante/opticsim/blob/efa7ac9ddbed0bf82ce529d16f754036a6d7f79f/scripts/author-scene.mjs#L30-L57) publishes a qualified observation snapshot **only if completed**. [observables.js, lines 75–95](https://github.com/physicsvigilante/opticsim/blob/efa7ac9ddbed0bf82ce529d16f754036a6d7f79f/src/observables.js#L75-L95) requires same-scene SHA, `executionPassed===true` and a qualifying completed status; otherwise all requested readings are `suppressed` and null. The corrected test explicitly asserts all readings suppressed and status non-completed [lines 65–110](https://github.com/physicsvigilante/opticsim/blob/efa7ac9ddbed0bf82ce529d16f754036a6d7f79f/test/jee-prism-beam-v22-review-conditions.test.mjs#L65-L110). The native terminal event and a qualified public reading are correctly distinguished.

## 5. Real later near-apex callback versus synthetic test injection — PASS, documented limitation

The dedicated test [lines 111–150](https://github.com/physicsvigilante/opticsim/blob/efa7ac9ddbed0bf82ce529d16f754036a6d7f79f/test/jee-prism-beam-v22-review-conditions.test.mjs#L111-L150) first confirms **public authoring rejects** a deliberately unsafe Beam configuration. It then changes **only the Beam** in a separately labelled **unqualified raw native research scene**, runs the actual pinned `core.Simulator`, and captures real `Glass.onRayIncident` callback points. Builder CI prints **six actual native callbacks, two within the new 0.1-mm apex band, closest 0.0517580189739361 mm**, and a resulting v22 observer error. This is genuinely *native-produced later ray geometry*, **not** a fabricated callback; however, the substituted raw-native input **would not be admitted as a public v22 authored scene**. No public qualified ledger or canonical export is claimed for it.

The **different** test [lines 151–180](https://github.com/physicsvigilante/opticsim/blob/efa7ac9ddbed0bf82ce529d16f754036a6d7f79f/test/jee-prism-beam-v22-review-conditions.test.mjs#L151-L180) manually injects a 0.05-mm hit using a stubbed original method to check observer policy, the v8 contrast and **exactly once native-method delegation**. That injected hit is **synthetic, not evidence that native PhyDemo chose the point**. The first test's real callbacks plus the second test's controlled policy contrast adequately validate the correction's observation path without authorizing the raw source.

**Remaining limitation (non-blocking):** there is no demonstrated *publicly admitted*, fully qualified Beam whose later native trajectory approaches a vertex inside 0.1 mm; the observed later near-vertex example uses a purposely refused initial Beam. Any stronger future end-to-end admission test should use an admissible source if one is constructible. Do not re-label the existing raw-native fixture as a canonical student case.

## 6. Two detectors and unchanged earlier contracts — PASS

[Follow-up test, lines 181–204](https://github.com/physicsvigilante/opticsim/blob/efa7ac9ddbed0bf82ce529d16f754036a6d7f79f/test/jee-prism-beam-v22-review-conditions.test.mjs#L181-L204) compiles `Beam, Glass, Detector, Detector`, with detector planes at x=200 and x=300 mm, and asserts **four sampled native crossings and four finite actual hit positions for each detector**, with positions on each detector's respective x-plane. The exact-head builder log emits `JEE_V22_TWO_DETECTORS` with these counts. This is **not** a source-to-hit ray identity or continuous flux claim.

[Existing v22 acceptance tests](https://github.com/physicsvigilante/opticsim/blob/efa7ac9ddbed0bf82ce529d16f754036a6d7f79f/test/jee-prism-beam-v22.test.mjs) and the optical CI log retain: the full triangle's **4 native emitted rays, 12 Glass events (four on each face), 4 genuine TIR, 0 detector crossings** as a **qualified sampled zero**; the short triangle's **4 positive detector crossings**; the dense **64 crossing count with its >32 positional list entirely withheld**; stale/hash, stopped and depth-limit suppression; and historical v8 SingleRay versus v19 Beam save/compilation isolation. The seven-file correction does not alter v8/v9 prism and polygon clearance defaults or widen v19/v20/v21 contracts. Across all CI, pre-existing workflows also pass. This is strong regression evidence, not a claim of exhaustive regression proof.

## 7. Git identity, red/green CI, Chrome and artifact evidence — VERIFIED FROM GITHUB

I independently retrieved the corrected [Git commit](https://github.com/physicsvigilante/opticsim/commit/efa7ac9ddbed0bf82ce529d16f754036a6d7f79f) and GitHub's synthetic merge Git objects: **both contain exact tree `526cf3c1e5e47c1e5e0c0d38a4c733bfb0a08201`**; synthetic merge parents are the unchanged `main` and the corrected exact head. Each of the following **11 GitHub Actions runs** has `head_sha=efa7ac9ddbed0bf82ce529d16f754036a6d7f79f`, completed status, successful conclusion and attempt 1, as checked independently via GitHub's run endpoints:

| Workflow | Run | Result |
| --- | --- | --- |
| Parameter experiment checks | [44501951016](https://github.com/physicsvigilante/opticsim/actions/runs/44501951016) | SUCCESS |
| Qualified authoring checks | [44501950920](https://github.com/physicsvigilante/opticsim/actions/runs/44501950920) | SUCCESS |
| Quasi-static source motion checks | [44501951191](https://github.com/physicsvigilante/opticsim/actions/runs/44501951191) | SUCCESS |
| Planar refraction checks | [44501950847](https://github.com/physicsvigilante/opticsim/actions/runs/44501950847) | SUCCESS |
| Optical composition checks | [44501950972](https://github.com/physicsvigilante/opticsim/actions/runs/44501950972) | SUCCESS |
| Plane-mirror angular inverse checks | [44501951015](https://github.com/physicsvigilante/opticsim/actions/runs/44501951015) | SUCCESS |
| Deterministic planar angular query checks | [44501951114](https://github.com/physicsvigilante/opticsim/actions/runs/44501951114) | SUCCESS |
| Numerical ray reliability diagnostics | [44501951182](https://github.com/physicsvigilante/opticsim/actions/runs/44501951182) | SUCCESS |
| Original refraction problem pair | [44501950918](https://github.com/physicsvigilante/opticsim/actions/runs/44501950918) | SUCCESS |
| Curved mirror checks | [44501951126](https://github.com/physicsvigilante/opticsim/actions/runs/44501951126) | SUCCESS |
| Unified problem workflow checks | [44501951071](https://github.com/physicsvigilante/opticsim/actions/runs/44501951071) | SUCCESS |

I directly inspected optical composition [job 135483712644](https://github.com/physicsvigilante/opticsim/actions/runs/44501950972): **903 tests / 903 passed / 0 failed**, `npm run build` passed; the v22 public workflow reports **7 inputs = 4 native-complete + 3 refused before native**; Chrome v22 workflow log explicitly reports **8 checks passed, 5 screenshots**. These **were executed by CI, not this reviewer**.

The earlier intentional [red CI run 44501110629](https://github.com/physicsvigilante/opticsim/actions/runs/44501110629), pinned to `6250d496f5d35d818377e1a67f122463e4e39575`, reported **903 tests, 900 passed, 3 failed**; I inspected its log and found failed near-critical and vertex qualification assertions. The green exact-head source also corrects an intermediate mistaken test expectation: **when qualification fails, its public interface ledger is withheld**, so the final test captures a **separate test-only raw native ledger** of the same scene and never presents it as qualified output.

GitHub artifact API lists, at this exact source head:
- [`llm-authoring-evidence`, artifact 14518485542](https://github.com/physicsvigilante/opticsim/actions/runs/44501950972/artifacts/14518485542), GitHub-reported SHA-256 `9824c11061a4e029061e0271a01b8d1d795b3e2312ab19b3548500a4c0abd1a5`.
- [`opaque-blocker-evidence`, artifact 14516859996](https://github.com/physicsvigilante/opticsim/actions/runs/44501950972/artifacts/14516859996), GitHub-reported SHA-256 `1374b4e2f316817f70e44bbd69c2523c27a2b485197eefbe3ff4e4158d7c940f`.

The builder reported ZIP CRC, original public case input hashes, qualified portable exports without cached results, browser screenshot existence and runtime-error checks. **I checked artifact identities/digests as published in GitHub metadata and relevant CI log lines, but did not independently download/decompress the ZIPs or rerun Chrome.** No independent browser screenshot review is claimed here.

## 8. Findings, limitations and disposition

**P0:** None confirmed.  
**P1:** None confirmed within the bounded seven-file correction and the inspected fail-closed integration.

**Non-blocking limitations / sensible follow-ups:** (1) later near-apex native witness is real, but uses an intentionally inadmissible source in an unqualified raw scene; add an admitted-scene witness if practical; (2) exact 0.1-mm binary64 callback equality is demonstrated by code-level inclusive comparison, not a separate native boundary case; an explicit precision-focused unit test would improve robustness; (3) an exactly critical physical branch is **not** classified by the observer, correctly withheld within the 1e-5 band; (4) Fresnel partial reflection remains explicitly disabled for v22, a documented approximation; (5) I performed **no independent pinned-native or Chrome execution**, so the operational run claims are supported by the builder's CI provenance rather than a second execution environment.

**Final verdict: CLEARED FOR OWNER DECISION.** The corrected v22-only callback policy, conservative near-critical numerical refusal, true later raw-native near-apex evidence, separate synthetic injected test, signed non-normal Snell expectation, two-detector sampled counts, historical isolation, full fail-closed suppression and exact-head CI collectively address the earlier *PASS WITH CONDITIONS* concerns at the reviewed scope. This is **not** a merge, deployment or release approval. Keep PR #173 draft/unmerged until a separately authorized owner decision; PR #172 and unrelated branch-protection work remain outside this review.
