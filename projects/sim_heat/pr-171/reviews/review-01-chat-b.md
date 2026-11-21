# Independent R2 review of the fourth rod thermometer

**Verdict: accept for the documented offline local-quadratic check.** No blocking findings.

I reviewed [source #171](https://github.com/physicsvigilante/sim_heat/pull/171) at `2ae5fe77b3b9befe609d88f956507501dfa99af4` against `d93914eb6b00b87d6956bd25d2daddcd1c91395b`, using the [review packet](https://github.com/physicsvigilante/review_sandbox/tree/02ac66020718a4917762658a0c96a07a824a0df9/projects/sim_heat/pr-171). I checked the four changed working files against their commit blobs, allowing for checkout line endings. The four focused unittests passed locally.

## Independent calculation

With scaled coordinate s = 8x, I placed three probes at s = 1, 3 and 6 with independent Kelvin intervals [405,407], [392,395] and [315,318]. For each of the eight endpoint triples (a,b,c), I formed d = (b−a)/2 and e = ((c−b)/3−d)/5, then evaluated a + (s−1)[d + (s−3)e] using rational arithmetic. This uses successive secant slopes. The extrema occur at corners because the predicted temperature is affine in the three readings. Every intermediate temperature between those extrema is attainable because the input box is convex.

| x measured from port a | Independent predicted interval (K) |
|---|---|
| 0 | [397, 2021/5] |
| 1/4 | [6032/15, 6077/15] |
| 7/8 | [271, 1398/5] |
| 1 | [655/3, 703/3] |

All four intervals matched the engine exactly for all six permutations of the input probes. The first, third and fourth cases extrapolate within the rod. For a linear 320, 330, 350 K profile at 0.2, 0.4, 0.8, the reported heating was zero. At x = 1 the independent prediction is exactly 360 K. Measured bands touching from either side passed. Moving the nearest edge away by 10⁻¹⁸ K on either side failed.

The fourth check rejected a repeated position spelled 0.3750, negative and above-one positions, and inverted Kelvin bounds. The spelling .375 was rejected by the existing unsigned-decimal grammar before a position comparison. Broadening the middle reading of the linear case to [329,331] K refused unresolved heating sign even with a fourth measurement. This preserves the three-probe sign criterion. A compatible fourth band establishes existence for the local profile only. It does not establish four-probe identification of source power, compatibility with all network boundaries, or the cause of a discrepancy.

## Archived evidence

The pinned [CI job](https://github.com/physicsvigilante/sim_heat/actions/runs/44907706565/job/136856717572) passed. I downloaded [artifact 14708856580](https://github.com/physicsvigilante/sim_heat/actions/runs/44907706565/artifacts/14708856580), verified SHA-256 `4739144fa1acabc66cb8e4beb7b7dee7fda71e23d85864d685168067a45f9639`, checked head.txt against the source head, and read the 245-test success in regression.log. The archived fourth-thermometer.json predicts [1515/4,1525/4] K and rejects 382 K. It records all four execution, qualification, certification and runner flags as false. This review supplies independently executed arithmetic and refusal checks. Native execution and empirical thermometer validation remain outside this milestone.
