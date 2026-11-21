# Independent Chat B review of SIM_HEAT PR 137

**Verdict: accepted for the bounded offline signed energy calculation.** No blocking findings. Reviewed base `d4e1425699296095c4a870e14cc06587912a8682`, head `7ec2c293de6a692b9d6e5697b69736d94361c66a`, and [request at 5b6a1a1](https://github.com/physicsvigilante/review_sandbox/blob/5b6a1a111582313b06e4fb0006d7fe854f4a95e1/projects/sim_heat/pr-137/REQUEST.md). A fresh Codex reviewer context performed these checks. [Source diff](https://github.com/physicsvigilante/sim_heat/compare/d4e1425699296095c4a870e14cc06587912a8682...7ec2c293de6a692b9d6e5697b69736d94361c66a)

## Physics and numerical enclosure

For each positive-duration panel the directed net power stays positive on a reached trip and decreases along the trip. Positive conductivity makes each physical conduction contribution decrease with temperature. Radiation also decreases with temperature. The start upper and finish lower directed-power bounds therefore enclose the denominator, including passive coupling uncertainty. All four products of signed endpoint radiation with positive endpoint residence-time bounds enclose the entire panel integral. Outward integer rounding preserves containment. The exact stored energy minus the radiation interval gives the oppositely ordered conduction bounds. Both channels use positive energy into the body.

I derived the composite-wall conductance from the study rods as 4 W/K in series with (1 + 3) W/K. I separately integrated each channel with SciPy adaptive quadrature using capacity 137 J/K and relative conductivity slope -0.001/K about 300 K. For bath B and body T the conduction power was 2(B-T)[1-0.001((B+T)/2-300)]. Radiation was sigma times the difference of enclosure and body fourth powers at unit area and emissivity. Each reference and its estimated numerical error fit inside the returned interval.

| Body trip K | Bath / enclosure K | sigma W/(m2 K4) | Conduction reference J | Radiation reference J |
|---|---|---|---:|---:|
| 330 to 340 | 380 / 310 | 2e-9 | 1490.12954 | -120.12954 |
| 373 to 362 | 380 / 250 | 5e-8 | 51.15357 | -1558.15357 |
| 360 to 340 | 280 / 350 | 2e-9 | -2742.76621 | 2.76621 |

The last cooling trip crossed the enclosure temperature and reversed instantaneous radiation. At exact equilibrium (380 K for bath, enclosure and body) a same-temperature target returned two exact zero intervals. A requested departure to 370 K returned unreachable and null energy bounds. All five checked-in energy and target-time tests passed offline. The initial bundled-interpreter attempt failed to import SciPy. The successful run used the already installed CI Python with SciPy 1.17.0.

## Archived CI evidence

I retrieved both ZIPs from GitHub, calculated SHA-256, checked every ZIP entry CRC, and verified job success and artifact run head against the reviewed source. Both computed digests matched the packet.

- [TwinBridge archive 14695852123](https://github.com/physicsvigilante/sim_heat/actions/runs/44875458157/artifacts/14695852123), SHA-256 `4955001e66d8fd350fee87bab75c798d2441fcc4995f489fd7c5d0b4e740209d`. The source-head file matched. The decompressed fresh result, oracle result and control result matched the three frozen records as parsed JSON.
- [Series archive 14695637643](https://github.com/physicsvigilante/sim_heat/actions/runs/44875458052/artifacts/14695637643), SHA-256 `a6fcd4bde7f2e7e12b8d512234cf78936ce4222dfb6f4c19ba2a68cecf569b00`. Parsed all five JSON files (wall, revised wall, series, full network and radiating-body energy). A fresh offline run on the pinned star inputs reproduced the entire archived energy JSON. Native execution, native qualification, independently certified reference and runner-consumable flags were all false.

Scope is the opt-in offline diagnostic and its provenance. These runs provide no new OpenModelica or classroom evidence. No source changes or merge were made.
