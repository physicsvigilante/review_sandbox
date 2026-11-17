# Opticsim PR #131 — research checkpoint status

**2026-11-17: BUILDER FEASIBILITY COMPLETE; INDEPENDENT REVIEW PENDING.**

[Draft PR #131](https://github.com/physicsvigilante/opticsim/pull/131) adds only `test/jee-apparent-depth-feasibility.test.mjs` (298 lines) to production base `d3509e82fb65d81aabe336666851f8f2962623f4`. No production code, solver, schema, native instrumentation, UI or existing tests changed. No merge or deployment was performed. This branch is independent of the held v14–v19 feature chain; its suite count is not that chain's suite count.

## Frozen source and actual execution

| Identity | Value |
| --- | --- |
| Source HEAD | `aa36f2ce10f148e404d5534e4000f53adc62f9b5` |
| Source / tested Git tree | `4203121ce123ad803ec8f41737e2a01ae6d7dd2f` |
| CI synthetic checkout | `1d8a51c35f0213f34c4d6f7b02290eaa47aec5ab` |
| Pinned native PhyDemo | `811f508d2b070898c241a568b0c167dcb8645251` |
| Runtime in inspected CI log | Node v24.19.0 |
| Node result | **801/801 passed; 0 failed, 0 skipped, 0 cancelled** |
| New research tests | **11/11 passed on first source attempt** |
| Standard workflows | **11/11 completed successfully** |

The builder inspected [the full Node/native job log](https://github.com/physicsvigilante/opticsim/actions/runs/44143858695/job/134253547783) and compared source/CI Git tree objects. The [optical composition run](https://github.com/physicsvigilante/opticsim/actions/runs/44143858494) also passed its existing native, CLI and real-Chrome/browser regression steps. This is builder CI evidence, not independently rerun physics and not a new apparent-depth browser demonstration.

## Selected native-backed findings

For a source 120 mm from a single plane, object index 1.5 and observer-side index 1, full-Fresnel native detector measurements yield these **derived backward-line intersections**:

| Explicit incident directions | Normal intersection depth, mm |
| --- | ---: |
| ±5° | 79.61636684775047 |
| ±1° | 79.98476458468129 |
| ±0.1° | 79.99984769083608 |
| ±30° | 61.10100926607784 |

The separately calculated near-normal paraxial limit is 80 mm. Native rays were not changed to enforce it. Three nearby incident directions 20°, 21°, 22° produced nonconcurrent pairwise backward intersections; two of those intersections differ by 2.4715758168506468 mm. The test does not average them into a unique image.

Reverse viewing, rotations/translations, units, component ordering, equal indices and reversed index contrast passed. Native TIR and finite-detector misses retain empty measured hit lists/zero counts while the derived point is unavailable. Near-parallel pairs are withheld; depth-zero incomplete runs suppress native readouts; stale or missing captures cannot authorize derived values. Existing native evidence and documents remain unchanged with capture ON/OFF.

## Limits and next gate

No new authorable observer or public apparent-image observable exists in this PR. Symmetric diagnostic ray pairs are not asserted to enter one eye. The test-local conditioning thresholds are heuristics, not proven uncertainty bounds. A future result contract must preserve native qualification warnings and explicitly label derived geometry rather than copy the local helper's status uncritically.

[Copy-ready Chat B review prompt](REVIEWER-PROMPT-01.md) · [Full request, raw-log pointers, findings and review questions](REQUEST.md).

Next checkpoint: independent review of this exact research source and its interpretation before a bounded production design. PR #129's separate safety-correction gate remains separate. Every held Opticsim PR remains unmerged; neither CI nor this builder-authored status grants release authorization.
