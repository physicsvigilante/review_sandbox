# Opticsim PR #135 — JEE finite detector-window native research status

**2026-11-18: BUILDER FEASIBILITY COMPLETE; INDEPENDENT PHYSICS REVIEW PENDING.** [Draft test-only PR #135](https://github.com/physicsvigilante/opticsim/pull/135) starts from production `main`, does NOT merge unreleased candidate A or v14–v19, and changes **one test file only**. No new authorable observer, eye, image, native optics method, scene schema or browser rendering is present.

| Checkpoint identity | Exact evidence |
| --- | --- |
| Production base | `d3509e82fb65d81aabe336666851f8f2962623f4` |
| First source, preserved | `ad4ab62c8c2fa70abcbe48c05742bac4303870bd` — **11/11 CI PASS**, then test-only warning-provenance improvement |
| Final source HEAD | `58001725e8fd97cbfeb00ee9eaff705a864ecae5` |
| Authored source Git tree | `ff0c6e46ea97b650c5e7e58680f180c458a437c1` |
| Tested synthetic PR merge | `a2a798de26b70e0fcf2cd04366bed660184abbba` |
| Tested merge Git tree | `ff0c6e46ea97b650c5e7e58680f180c458a437c1` — identical |
| Final diff | Only `test/jee-finite-detector-window-feasibility.test.mjs`, 462 added lines |
| Pinned native | PhyDemo `811f508d2b070898c241a568b0c167dcb8645251` |
| Supported CI | Node `v24.19.0`; **799/799 tests PASS**, 9 new native research tests |
| Workflow results | **11/11 standard workflows SUCCESS** on final HEAD, no retry needed |
| Main branch | Unchanged / not protected; #123 separate |

## Actual builder-CI native findings

[Full structured Node24/native log](https://github.com/physicsvigilante/opticsim/actions/runs/44235111520) records both true PhyDemo ±0.5° source runs through one 1.5→1 plane at x=0 from S1=(-120,0). Exactly one sampled native detector crossing per run on the same finite D1, center (40,0), length **5 mm**, with measured y≈±1.57086112747 mm, endpoint clearance ≈**0.92913887253 mm**. Distinct scene hashes `4007c919f63cdbd4a1d0ff6f57ec5ac438fa6295eee4ac1f4bdca70d19e6ccf0` and `37fb3a4da5b1f87ecf794e3f148b07cbe7bc6351efb802f73da2b6bf351569f3`. Real full-Fresnel interface encounters include transmitted and reflected branches, with zero warnings/truncation.

Derived **post-native pairwise 2D backward intersection** at (-79.99619199829817,0) mm; `lineSine=0.02617736355354841`, backward distances 120.00647 mm, endpoint clearances 0.92914 mm. This is **not** one or two actual eyes, a pupil, a native propagated ray, a unique stigmatic image or continuous irradiance. These are actual detector-hit measurements followed by separate geometry, not a manufactured native ray.

Shifted window sampled counts [0,1], shortened or translated-away window [0,0]; derived point withheld. Reverse/rotated/translated/unit conversions and component order passed, as did TIR/near-critical detector misses, simulation maxRayDepth=0 suppression, stale/no-capture, incompatible families, duplicate/single run and near-parallel rejection. Post-native ±0.0001 mm/±0.000001 rad synthetic perturbation shifted derived point at most **0.00152917262686 mm in this fixture**; this is NOT a bound on native or eye/image error.

Full Fresnel gives native/derived `available` **geometric** readings (never an observer-image claim). Deliberately transmitted-only `partialReflection:false` gives `qualified` readings and derived `qualified`, with exact Fresnel-omission warning. The final test-local postprocessor also retains **BOTH** invocations' distinct native warning/status/hash records when one ray misses the finite detector and the derived point is `unavailable/null`. Initial source's premature return was corrected without changing native code; both source attempts and CI remain archived.

[Existing optical composition/Chrome regressions](https://github.com/physicsvigilante/opticsim/actions/runs/44235111578) also pass; no B browser feature exists.

## Pending independent checkpoint

[**Copy-ready Chat B prompt**](REVIEWER-PROMPT-01.md) · [**Detailed independent review/evidence request**](REQUEST.md) · [Preregistered physical scope #134](https://github.com/physicsvigilante/opticsim/issues/134).

**Independent Chat B review PENDING**; reviewer must inspect exact Git source/CI evidence, independently recompute scalar/line geometry, assess native/derived distinction and challenge finite-window, warning association and heuristic conditioning. Review clearance, if granted, would be **RESEARCH ONLY** and not a production B API/eye, merge, or owner release decision. Keep #133 candidate A source/review, #129 aperture correction and main safety #123 separate.
