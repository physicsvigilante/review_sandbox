# Independent Codex review of Opticsim PR #227

**Outcome: pass. No unresolved blockers or demonstrated defects within the bounded v36 scope.**

- Source [PR #227](https://github.com/physicsvigilante/opticsim/pull/227), integrated production base `01492dfb901f2cbc45f127d21bef057ddc9bb820`.
- Exact reviewed head `3a27bd37878bdbfeb8dc257b59832c2b2f5689ef`, Git tree `6f137ce4e00f822c0e07574538bedfda8420a5dc`.
- Reviewer: independent-in-context Codex agent, 2026-11-21. Scope: public v36 geometry and composition, native callback qualification, detection and stale/failed evidence, version compatibility, CLI/Chrome provenance. No production source changed in this review. [Exact source](https://github.com/physicsvigilante/opticsim/tree/3a27bd37878bdbfeb8dc257b59832c2b2f5689ef)

## Findings and verification

The explicit v36 contract compiles the admitted assembly into one native AngleSource, one real finite Glass and one passive Detector. Its per-ray audit checks the authored source launch and both brightness channels, finite face and direction continuity, signed refraction or reflection at the actual callback, and a finite downstream Detector passage or safe miss. Counts are based on actual exits. The scope remains the bounded 2D meridional section with an external detector and transmitted-only refraction at noncritical interfaces. No full Fresnel branch, power transmission, skew or image claim is warranted. The original A19 conditional angular evidence and frozen test-only study remain byte-preserved.

I rebuilt the core from PhyDemo pin `811f508d2b070898c241a568b0c167dcb8645251`. Sixteen focused v36, frozen-study and v18 provenance tests passed, as did 61 separate existing composition, v29, v35, polygon and finite-hit-diagnostic checks. The v36 app provenance fixture binds the verified current `src/app.js` Git blob `309a947b58e1aea4b9335c29bf49c8f645621c62` and retains the historical v35 app blob.

An independent ray-geometry calculation checked 350 deterministic authoring trials with varied sampling, orientation, material, aperture and translations up to about 9.8 m. Fifty-four layouts were inadmissible at validation and 17 required withholding. All 279 qualified cases agreed on all 1,261 native exit classifications (344 direct, 811 guided and 106 side leaks), Glass interaction/TIR counts, and 487 finite detector hits plus 774 misses. The actual Detector signed relative-power totals agreed in both orientations. The public baseline had three guided exits, two side leaks, ten native TIR interactions and five detector crossings.

A separate 30-case critical sweep used both signs of incidence and three translations. All 18 near/equal cases were withheld. Eleven of the twelve cases at signed critical margin ±0.000002 qualified on the expected side of the boundary. In the last case, a genuinely delegated native transmitted sidewall ray made a second Glass callback only about 0.00000543 mm farther along the same wall after a translation of +9770 mm in x and −9745 mm in y. The public audit correctly suppressed the entire fan after observing that repeat callback despite a native completion event.

Four delegated source, Glass and Detector perturbations all withheld public observations: a displaced emitted ray, redistribution of its polarization channels without a change of total, one omitted detector hit on a side-leaking ray, and a collinear downstream Detector continuation displaced from the actual contact. A previously verified report did not qualify a physically edited scene. Existing tests also exercise stopped runs and ambiguous detector endpoints.

## Browser and retained evidence

Independent Chrome 158.0.8127.37 passed all seven acceptance checks. The browser showed the two sidewall exits separately from the five crossings, cleared observations at critical incidence, retraced after an edit, and saved and reopened the revised qualified package with four guided exits and one side leak. The report records zero runtime errors and external network calls. Hosted Chrome for Testing 158.0.8127.36 passed the same seven checks. The downloaded revised packages matched byte for byte, with scene SHA-256 `a1fde91fc48e51f91d61bd128283734afba1e454e7971c040be188aed6906c97` and integrity SHA-256 `e0ff02892e6007b3b9bfff2537e823785513e0f362e68f5ab3cc6386c0a7782e`.

Verified the exact-head authoring archive `14697522905` (SHA-256 `ab9b7df0acd3f9ee3e90d152c014ed2051cd330dc924af5d2284ef2b568fdfca`) and browser archive `14697537653` (SHA-256 `2ce4ca7b00bdefb588020676b6a2be082005887fb5b67aa654d03acec98ec008`). All six normal CLI files matched the independent replay byte for byte, including native evidence SHA-256 `eb2881d2c344c8ecef1fde54efef39b5aafc6afed517a88acd57dc4e7fa6f7ab`. The hosted report, screenshot and revised package were present and inspected. [Authoring archive](https://github.com/physicsvigilante/opticsim/actions/runs/44880801361/artifacts/14697522905) · [Browser archive](https://github.com/physicsvigilante/opticsim/actions/runs/44880801361/artifacts/14697537653)

## Hosted CI and release

All 11 hosted exact-head PR workflows completed successfully. The optical workflow logs identify synthetic merge checkout `97c0b2282f77ae4961c16e4749a27eff62250f30` with the stated head and production base, 1,330 Node tests passed with zero failures or skips, and all seven v36 Chrome checks passed. Independent Git merge-tree computation from the stated base and head reproduced the reviewed tree. [Optical composition CI](https://github.com/physicsvigilante/opticsim/actions/runs/44880801361) · [Unified workflow CI](https://github.com/physicsvigilante/opticsim/actions/runs/44880801375)

Remaining passing workflow run IDs are `44880801324`, `44880801326`, `44880801328`, `44880801351`, `44880801355`, `44880801367`, `44880801382`, `44880801388` and `44880801456`. This clears the exact reviewed v36 source for owner-authorized integration. The report makes no classroom assessment or claim of a native solution for the original A19 limit question.
