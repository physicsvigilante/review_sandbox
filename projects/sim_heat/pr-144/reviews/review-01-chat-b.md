# PR 144 independent R2 review

**Pass for the offline radiating layer stack.** No demonstrated code defect. Chat B independently inspected the four-file diff and reviewed source commit `f9005ea2d7840c77bbe07569f05f1a8733884a65` against base `20718b37c3948e7751fa608638c77a95436ddcee`. Review packet commit `1dfc4f449da9813065ebc1d8d0dfe16ffb61d065`. Source files were not changed during review. [Source diff](https://github.com/physicsvigilante/sim_heat/compare/20718b37c3948e7751fa608638c77a95436ddcee...f9005ea2d7840c77bbe07569f05f1a8733884a65)

## CI and reproduction

Both jobs reported success for the exact reviewed head. I downloaded both ZIPs and computed SHA-256 on their original bytes. I exported the source directly from the pinned Git object and replayed the archives using Windows Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0 and mpmath 1.3.0.

- Series ZIP SHA-256 `43663299e37189abeac6271f76127a5064638acbb438ce865c0d0b94e38633aa`. All five CLI outputs matched the corresponding archived JSON structures, including the new radiating-layer-stack output. [Job 136766478816](https://github.com/physicsvigilante/sim_heat/actions/runs/44877872138/job/136766478816) and [archive 14696493302](https://github.com/physicsvigilante/sim_heat/actions/runs/44877872138/artifacts/14696493302)
- TwinBridge ZIP SHA-256 `e3ceab8653dde7c5f4e841059a92e3f92186d7693d14462ad4f57c6188acd044`. Fresh conduction output matched the archived and frozen JSON. The independent oracle and seven historical controls reproduced the archived summaries. I verified the archived source-head text. [Job 136766478643](https://github.com/physicsvigilante/sim_heat/actions/runs/44877872139/job/136766478643) and [archive 14697091528](https://github.com/physicsvigilante/sim_heat/actions/runs/44877872139/artifacts/14697091528)
- Four focused radiating-stack and baseline stack tests passed locally. Initial runtime discovery found missing packages in other environments before selecting the pinned runtime.

## Independent physics checks

The source model gives conductances of 4, 1 and 3 W/K. The first is in series with the other two in parallel, giving 2 W/K overall. With the hot terminal on the left, facing, strip and insert carry respectively 1, 1/4 and −3/4 times the signed layer power because the insert ports are reversed. Facts SHA-256 is `f4687ad77987ba5b5452d19b4c3aaa7a17ee3ab2320b8b8a3ddca73b177b4d5b`.

- For the archived emission case, integrating each linear conductivity law across a 60 K drop gives a factor of one on average because the reference is the face midpoint. Both layers and the 0.5 K/W contact therefore carry 120 W. The surface at 200 K radiates 120 W to 0 K. I checked all four faces (380, 320, 260, 200 K), both reported powers and all six signed rod intervals against exact rational values.
- For a new absorption case, I prescribed a 320 K surface, 400 K enclosure, area 2 m², emissivity 0.5 and sigma 1e−9 W/(m² K⁴). The exact radiation balance yields −15.11424 W. The wall faces must then be 297.32864, 304.88576, 312.44288 and 320 K for the same thermal contact. I used layer midpoint references 301.1072 and 316.22144 K, slopes +0.002 and −0.001 per K, and put the first layer's cold terminal on the left. Every face, both powers and all six oriented rod values lay in their reported intervals with widths below 1e−12 in their reported units.
- With zero emissivity and separately with equal bath and enclosure temperatures, both layers enclosed the uniform bath temperature and zero flow. The focused tests also refused emissivity above one. The four offline status fields were false in all independent examples.
- Independent rational inputs 200/3, 144 and 777/11 K lay within their inverse fourth-power brackets for a nonzero 100/3 K origin. Integer fourth-root flooring followed by a one-tick upper enlargement encloses the exact root, and clamping to the physical endpoint preserves that enclosure.

## Scope judgments

| Dimension | Judgment |
|---|---|
| Source interpretation | Pass for the authored two-terminal geometry, rod orientations and explicit radiative properties. |
| Physical and numerical results | Pass for the reviewed steady offline series model and its signed balances. |
| Native simulation | Unverified. The reviewed calculation runs offline and reports native execution and qualification as false. |
| Provenance | Pass for the exact source and archive replays above. |
| Teaching outcomes and textbook coverage | Unassessed. |

Independent Codex Chat B reviewer, 2026-11-21. The evidence supports retaining the scoped pass on this source head. Production merge remains an owner decision.
