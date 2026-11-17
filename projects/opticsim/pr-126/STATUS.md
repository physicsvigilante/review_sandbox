# Opticsim PR #126 — JEE-first native parallel-beam feasibility

**SOURCE-CI COMPLETE. Research-only, no public Beam authoring yet. Independent physics review pending. DRAFT / UNMERGED / NOT RELEASED.**

## Exact identities

- [Research PR #126](https://github.com/physicsvigilante/opticsim/pull/126), source HEAD `2632efa3d1e2187e4cd793eb80a505b7302919c7`, Git tree `604e69cfd195ade6968ca6df3ddb557ad9e9337e`.
- Base is production main `d3509e82fb65d81aabe336666851f8f2962623f4`, not a held thick-lens research branch.
- Synthetic GitHub CI merge `87fdee7377c1d417bc20e4bcabbf966c4823452f` has the **same exact Git tree**, verified through both Git commit objects. This is not a production merge.
- Only two added paths: `test/jee-native-parallel-beam.test.mjs` and `docs/JEE-FIRST-DRAFT-NEXT-STEPS.md`. No production source, source adapter, schema, geometry validator, measurement cutoff, upstream pin, workflow, original test or historical freeze changed.

## Native results actually observed in source CI

All eight new tests passed using pinned native PhyDemo Beam, not a manually generated ray list. Width40mm and medium native density0.2 emitted8 parallel samples; density0.4 emitted16. Fixed low brightness avoided native saturation in these controls.

| Control | Observed outcome |
|---|---|
| Free-space parallel source | Eight samples at y=+17.5,+12.5,+7.5,+2.5,-2.5,-7.5,-12.5,-17.5mm, all direction +x |
| Converging ideal lens f=100mm | Eight native detector samples at focal plane x=100,y=0; reversed illumination also passed at x=-100,y=0 |
| Diverging ideal lens f=-100mm | Eight downstream measured positions agree with twice the incident height; max absolute y=35mm; no virtual-image detection claimed |
| Finite 12mm gap before lens | Six native opaque-arm absorptions, two surviving lens/detector samples |
| 60mm slab, incidence30 degrees | Eight samples satisfy independently calculated Snell/exit geometry for n=1.5 and1.8; respective perpendicular displacements11.628826929126161mm and14.974937325880997mm |
| TIR, n1.5->1 at60 degrees | Eight actual native TIR events and detector hits with expected reflected direction |
| Sampling/repetition | Eight versus16 samples; same ideal focal plane and repeated native event evidence |
| Full-Fresnel / processed stop | Incomplete Fresnel truncation0.006030001375125609; stopped low-budget control. Both withhold the complete position list |

Complete controls reported zero truncation and undefined behavior. Transmitted-only refraction controls deliberately omit partial Fresnel reflection, retaining native TIR. These are synthetic teaching controls, not scored original JEE answers or continuous optical/image/power certification.

## Full verification, including the failed first browser attempt

**798/798 Node24 tests passed; all11/11 standard workflows ultimately succeeded.** This count is production main's790 existing tests plus8 new, not the separate held integration stack's866 tests. [Native curved run44125543968](https://github.com/physicsvigilante/opticsim/actions/runs/44125543968), [optical run44125544838](https://github.com/physicsvigilante/opticsim/actions/runs/44125544838), [planar run44125545198](https://github.com/physicsvigilante/opticsim/actions/runs/44125545198) and [unified run44125545232](https://github.com/physicsvigilante/opticsim/actions/runs/44125545232) succeeded.

[Qualified-authoring run44125544327](https://github.com/physicsvigilante/opticsim/actions/runs/44125544327) **first failed** at job134188198748: all798 Node tests, build and existing CLI cases passed, but browser discovery returned `Chrome/Chromium unavailable; no browser validation performed`. Later demo steps were skipped, and their missing artifact caused a secondary upload failure. A single **unchanged-source job retry** (job134191230302) then passed the existing browser import/edit/export and supported-demo checks, with all steps successful. Do not call this a clean first-pass11/11 result or silently erase the failed attempt. The reason browser discovery failed on the first runner has not been established beyond that log.

The source-CI evidence is builder execution, not an independently executed reviewer experiment. Existing Chrome regressions passed on retry; **no new public beam CLI/browser authoring path exists yet**.

## Scope and next step

The harness replaces only the test-native source of an otherwise supported optical scene. It asserts other native objects unchanged and canonical `parallel-beam` rejection. It never qualifies the substituted beam scene using the old point-source document hash. A real authoring contract still needs whole-emitter-segment bounds/clearance, unambiguous starting-medium validation, old-version preservation, explicit physical versus sampling fields, ordinary CLI and real Chrome edits/export/reopen.

[Independent review request](REQUEST.md) and [copy-ready review prompt](REVIEWER-PROMPT-01.md) prepared; no reviewer verdict received. The reviewer must independently check native source orientation, physical references, exactly-once delegation and all evidentiary limits before supporting the next source-design step.

The JEE-first plan defers detector-capacity expansion and further complicated thick-lens trains. Issue#124's v18-specific >32-hit feasibility remains **deferred and open**, not solved. Consolidation remains gated by exact-source review and explicit owner release decisions; no held PR, main branch, historical source pin, protection setting or deployment was changed.
