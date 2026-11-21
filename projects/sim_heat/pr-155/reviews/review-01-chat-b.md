# Chat B independent R2 review of PR 155

**Verdict. Accept the offline heated-rod profile calculation at this source head.** I found no blocking or major defect. This verdict covers junction temperature bounds, continuous maximum temperature and the interval enclosing its location, measured from each rod's authored end A. The evidence supports steady, one-dimensional, uniform generation in constant-property rods.

I reviewed base `e42285bf65ca261b331bc7a1e35e9f41511f5ac4` through head `545d1b6c78ca9b2ff83892b9f5dc177b54467557`, verified the source worktree was clean, and read the three-file request at hub commit `181f796998e3122f5d521a23ebc023904a94af8f`. [Draft source PR](https://github.com/physicsvigilante/sim_heat/pull/155)

## Independent calculations

I assembled the grounded nodal conductance matrix directly from the SI givens in the study facts, added half of each rod's power to each free endpoint and solved the simultaneous equations with rational Gaussian elimination. For each rod I integrated its axial heat rate, which starts at G(Ta−Tb)−P/2 and increases linearly by P over the normalized rod length. I compared temperatures at both ends and at every interior heat-rate zero. This calculation used neither the candidate's reciprocity solver nor its peak functions to obtain expected answers.

- For the original bridge I also read the Modelica connections and dimensions. The upper path has two 2 W/K rods, the lower path has two 1 W/K rods, and the 1 W/K link runs upper to lower. With 28 W on the link, the loaded nodes are 334 K and 336 K. The outgoing axial rate from A starts at −16 W and reaches zero at 4/7. The peak is 2370/7 K. The complete locally computed JSON matched the CI bridge profile.
- I ran three load patterns per network on the bridge, composite wall with reversed insert, three-bath star, three-bath triangle and series extension. The patterns were zero generation on the first rod, simultaneous generation of 17 + 90i W on each rod in facts order starting at i = 0, and 500 W on the final rod. Every node temperature, peak and maximizing position was enclosed. The balanced unheated bridge link contains both extremal positions 0 and 1. The triangle exercises a network comprised entirely of fixed nodes. In the 500 W bridge run, the lower and upper junctions reached 3060/7 and 2810/7 K respectively.
- In a disposable source-pinned bridge variant I changed the link to a circular rod (d = 0.1 m, L = 0.1 m, k = 10 W/(m K)), updated the model, descriptor, facts and parameter provenance, and applied 412 W to feed, 101 W to link and 88 W to outlet. I evaluated kπd²/(4L) on each side of π using adjacent decimal bounds at 80 decimal places. The independently computed nodes and all rod maxima and positions fell within the reported intervals for both evaluations.
- Source inspection confirms that the probe conductance is computed from the outward heat rate at a unit probe. Reciprocity follows from symmetry of the grounded nodal matrix. The hottest temperature increases monotonically with either endpoint and with the nonnegative curvature coefficient. Clipping the stationary point bounds and returning the entire rod for overlapping zero-power endpoint bounds conservatively enclose possible maximizers.
- Eight focused repository tests passed locally. Six additional profile-mode refusals covered missing generation, negative power, exponent notation, unknown rod, repeated rod and stale facts hash. The four execution, certification and runner flags were false throughout the independent successful cases.

## CI and evidence boundaries

Both pull-request workflow runs associated with the exact reviewed SHA succeeded. I downloaded both original ZIPs, hashed their bytes, and checked every entry's ZIP CRC.

| Workflow and archive | SHA-256 | Content checked |
| --- | --- | --- |
| [Series run 44883978426, artifact 14699550008](https://github.com/physicsvigilante/sim_heat/actions/runs/44883978426/artifacts/14699550008) | `ff44e2de8e486309da39bc5c417dcf4324a7ce9c87cae292298889fb3aa732ef` | Five files including the heated bridge result replayed above. |
| [General conduction run 44883978428, artifact 14698439402](https://github.com/physicsvigilante/sim_heat/actions/runs/44883978428/artifacts/14698439402) | `08dd42de5ae2dc5b8f1bc0b19f68582822d14da95d2ae53f4bc5363e2700729c` | Source-head file matched. Decompressed TwinBridge output, control results and oracle results matched the frozen JSON by value. |

This is a separate-context computational review. The CI and independent calculations provide offline evidence. Native execution, runtime qualification and classroom outcomes remain outside the reviewed claim. The source PR remains unmerged.
