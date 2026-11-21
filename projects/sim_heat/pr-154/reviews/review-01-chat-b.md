# Independent Chat B R2 review of SIM_HEAT PR 154

**Verdict.** Accepted for the bounded offline calculation of steady terminal heat rates at the reviewed head. I found no blocking or major defect. Source merge remains an owner decision.

Reviewed base `2083be6a02c51f95d178ed8dfeb0176a767f2fb1`, head `e42285bf65ca261b331bc7a1e35e9f41511f5ac4`, and hub packet `a7f18b77ed59f5bb76d5548fbb52f8dac40f92bb`. I acted as the independent Codex reviewer and inspected the five-file diff and the existing preparation and interval paths. [Pinned source](https://github.com/physicsvigilante/sim_heat/tree/e42285bf65ca261b331bc7a1e35e9f41511f5ac4)

## Physics and independent checks

For a constant-area, constant-conductivity rod with uniform total heating P, integration of the steady heat equation gives the end supply from A as G(Ta − Tb) − P/2. Exchanging A and B gives the other end supply. Thus the equivalent nodal loads are P/2 at each end, independent of the declared orientation. Symmetry of the conductance matrix implies that a unit terminal temperature solution gives the absorption fraction for an injection at each node. The code averages the two endpoint influences, intersects their bounds with the physical range [0, 1], and subtracts absorbed power from each bath's original supply.

- In the source composite wall, the insert runs from the cold bath toward the junction. Under 320 W in the facing and 80 W in the insert, the direct junction balance is 8 Tj = 4(380) + 4(280) + 200. This gives 355 K. The hot bath supplies 4(380 − 355) − 160 = −60 W, and the cold bath supplies 4(280 − 355) − 40 = −340 W. Their sum removes the entire 400 W.
- I exercised a separate all-maintained triangle with 3.5, 6, and 9.25 W on its three different rods. Direct endpoint balances predict 4.75, 6.375, and 7.625 W received at warm, middle, and cool. All six reported intervals enclosed the expected received powers and the corresponding supplies 125.25, 38.625, and −182.625 W.
- Five focused tests passed locally, covering a three-bath internal junction, hot-bath reversal, zero generation, bad sources, and inherited terminal-response behavior. Additional probes refused a wrong facts digest and a nonfinite power. Altering insert conductivity and independently altering its endpoint in fresh facts, even with each altered file's actual digest, produced the respective physical-parameter and connectivity binding errors.

## Evidence and limits

Both PR workflows reported success for the exact head. I downloaded and CRC-checked both ZIPs. The series archive SHA-256 was `64847209c137854175a13abfb109eb4e8f5c473f8a51539ba79899c17c4b6e0d`; its generated rod result equaled a fresh local calculation in every JSON field. The TwinBridge archive SHA-256 was `addaab5681b52e559eb6dfb776cb12d1f3f055e7ea53d054c64f705d652a204e`; its recorded source head matched, and its decoded output, oracle results and controls equaled the frozen records. TwinBridge supplies regression evidence for the underlying conduction engine. [Series run](https://github.com/physicsvigilante/sim_heat/actions/runs/44883754909) · [TwinBridge run](https://github.com/physicsvigilante/sim_heat/actions/runs/44883754845)

This review covers uniform generation specified as total watts per rod, fixed baths, linear steady conduction and terminal rates. The heated-rod result carries offline flags. Native heated-rod simulation, spatial temperature profiles and classroom outcomes remain outside the demonstrated scope.
