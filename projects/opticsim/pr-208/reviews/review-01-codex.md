# Independent Codex review of Opticsim PR #208

**CLEARED FOR OWNER DECISION.** I found no blocker in v31 geometry, its native qualification, the public observation workflow, or browser use.

| Identity | Reviewed value |
| --- | --- |
| Candidate | `9eecd7678a29f97a8e7985a440a916d8fce55996` |
| Tree | `360afe4aeb980e8d83f7969c41bd367a3a62d9ad` |
| Base | `be79aa86931fa13b9c06f6319b125262a2889432` |
| CI merge | `d24894df149a6fe172750efa8fb5ab60addbbc91` |
| PhyDemo pin | `811f508d2b070898c241a568b0c167dcb8645251` |
| Browser app blob | `64f74f2cf8bc81ad87a8b92d03612ee0975962d2` |

## Physical model and qualification

The explicit v31 model composes one rightward directional AngleSource, two PlaneGlass boundaries of one denser slab in a common exterior, one vertical passive Detector, and a separated left-facing concave ArcMirror. The restrictions bound aperture and radius, cone, source placement, finite clearances, ray density and relative brightness. The nearest point of the finite arc clears the detector. The A12 example binds its 200 mm radius, 300 mm axial object distance, 60 mm slab, and glass index 1.5 to the frozen source facts. Exact positioning, the 1 mm transverse probe, exterior index, relative brightness, cone, apertures and reflection policy are study choices. The public outputs are sampled crossings and directions, interface encounters, and mirror counts. An image position or size change calls for separate analytical modelling.

I verified single native delegation per call. Qualification uses each emitted native object identity, the ordered contacts at both faces and the detector, full continuity between calls, one local-normal reflection, tangential Snell checks and the finite-clearance checks. The native result must complete without warnings, extra branches, truncation or inconsistent counts. Detector event directions distinguish the outgoing and returning samples, and the existing signed power semantics apply. Missing stage evidence or a missing v31 verification flag suppresses the new profile's observations. Existing profile qualification remains separately keyed. All 46 prior public example inputs and plans matched the base exactly.

## Independent runs and hosted evidence

The isolated candidate passed 26 focused tests. In a separate geometry check I qualified 324 scenes across axis and axial translations, both valid orientation spellings, radius extremes, source offsets, index ratios, and ray densities of 0.95, 0.97 and 1. I compared 1,800 signed detector contacts with an independent calculation of planar transport and spherical reflection. The maximum ordinate discrepancy was 2.03 × 10⁻⁸ mm and the maximum transverse direction-component discrepancy was 4.09 × 10⁻¹⁰. Seven fault injections covering missing optical and detector callbacks, altered continuity, a premature absorption and missing emission all withheld observations.

An independent Chrome 158.0.8127.37 run passed all seven checks, including refusal of coincident planes, a qualified mirror-radius edit, and export and reopen of the revised scene. Hosted Chrome for Testing 158.0.8127.36 passed the same checks. All eleven workflows passed with 1,225 Node tests. The hosted merge of source and base resolves to the candidate tree. [Optical composition run](https://github.com/physicsvigilante/opticsim/actions/runs/44862193297)

I verified both artifact ZIP digests. All six archived v31 CLI records matched the independent run byte for byte. The independently saved mirror-radius revision matched the archived Chrome download byte for byte with SHA-256 `51ba34d8057f9ed6f369f8f7966b89c0d87fa898ed2ed1bcb2db826fb8b1358b`. [CLI evidence](https://github.com/physicsvigilante/opticsim/actions/runs/44862193297/artifacts/14690372412) · [Profile Chrome evidence](https://github.com/physicsvigilante/opticsim/actions/runs/44862193297/artifacts/14689889046)
