# R2 Chat B review of PR 115

**Verdict — accept the pinned offline passage-time change.** I found no blocking issue in the reviewed scope. GitHub reported an open draft with base `e4c64a026917d0fa23ed6997fde7c7db12a63cfc` and head `036a6f53744878d8679c0d4f2967b7ede7d821d3`. I inspected the five-file diff in a clean checkout with that head and parent. [Source comparison](https://github.com/physicsvigilante/sim_heat/compare/e4c64a026917d0fa23ed6997fde7c7db12a63cfc...036a6f53744878d8679c0d4f2967b7ede7d821d3) · [Review request](https://github.com/physicsvigilante/review_sandbox/blob/4ca3a10934551cb52d7b219f85dd89bdc83f1d57/projects/sim_heat/pr-115/REQUEST.md)

## Independent passage and inventory checks

I used the pinned composite wall. Its facing conductance is 4 W/K, and the parallel paths add to 4 W/K, giving 2 W/K in series. My donor began at 330 K with 1 kg each of liquid and solid. My receiver began at 300 K with 2 kg solid and 1 kg liquid. Each latent heat was 6 J/kg. The donor solid and receiver liquid specific heats were 3 and 1 J/(kg K), respectively.

The events occur at 6 J and 12 J. Through 6 J the power is 60 W. From 6 to 12 J the temperature gap decays exponentially with time constant 3 s, reaching 29 K. After 12 J the gap decays with time constant 1 s. At transfer E in that last stage the gap is 29 − (E − 12)/2 K. Equal temperatures require 70 J. I inverted these exponential solutions at 125 decimal digits and compared 115 significant digits of each result with the implementation's rational bounds.

| Target (J) | Elapsed time (s), rounded | Segments |
| --- | --- | --- |
| 0 | 0 | 0 |
| 6 | 0.1 | 1 |
| 12 | 0.20170465502704404 | 2 |
| 50 | 1.2664153920194724 | 3 |
| 69.999999999999999999 | 45.708679339466286 | 3 |

All bounds contained the oracle with widths below 1e-14 s. I repeated the checks with reversed argument order and with the warmer material physically assigned to the port named cold. Both endpoint temperatures matched independently calculated enthalpies. The equilibrium donor held 2 kg solid, 0 kg liquid and released 6 J latent plus 64 J sensible. The receiver held 0 kg solid, 3 kg liquid and absorbed 12 J latent plus 58 J sensible. Endpoint mass and energy balanced in each orientation. The 2 s plateau request also allowed a passage endpoint later than 2 s, as documented.

The implementation refused 70 J, 71 J, a negative target, a positive target between equal-temperature baths, and a positive target with missing specific heats. Both source passage tests passed locally, including simultaneous exhaustion. My first independent run passed 0 and 6 J and failed my assertion at 12 J. I traced this to Python evaluating the capped 6/60 term in the oracle in binary floating point. I used multiprecision operands throughout and reran every case above against the same source.

## Archived evidence and scope

I checked both successful job records, their artifact-to-head bindings, and SHA-256 values computed from downloaded ZIP bytes.

- Passage job 136733916480, artifact 14691923039, SHA-256 `31b6c3d53bc864f96ce4d1ea3dff0af613e3254a2b38353893449bf655274af2`. In `phase-transfer-time.json`, the first 90 kJ took exactly 750 s. The 120 kJ time bound contained my independent result 750 + 550 ln(11/6) s, about 1083.37 s. The archive reports final temperatures 67293/220 K and 5463/20 K and both native flags false. [Job](https://github.com/physicsvigilante/sim_heat/actions/runs/44867362217/job/136733916480) · [Artifact](https://github.com/physicsvigilante/sim_heat/actions/runs/44867362217/artifacts/14691923039)
- General offline replay job 136733916558, artifact 14692666893, SHA-256 `3051de5b55486867fefe5c4e7411f7366cbe2acf6bc4ddae69178b13989c3c06`. Its source-head file matched the candidate. The archive included fresh TwinBridge output, numerical oracle results and refusal controls. [Job](https://github.com/physicsvigilante/sim_heat/actions/runs/44867362228/job/136733916558) · [Artifact](https://github.com/physicsvigilante/sim_heat/actions/runs/44867362228/artifacts/14692666893)

The review covers the offline two-bath calculation through the storage-free conducting network. The evidence supports its energy, timing and refusal semantics. Native phase-change execution and classroom outcomes remain unassessed. Source merge requires separate owner approval.
