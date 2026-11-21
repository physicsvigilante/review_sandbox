# PR 143 independent R2 review

**Verdict: accept the bounded offline investigation at `20718b37c3948e7751fa608638c77a95436ddcee`.** I found no blocking numerical or provenance defect in the reviewed change. I reviewed this as the separately dispatched Chat B reviewer against base `c99940b6505fd0332d73c5cabc5718451ae0d22b`. [Pinned request](https://github.com/physicsvigilante/review_sandbox/blob/f771b1d950d8e3b6828157267f35260e988a785e/projects/sim_heat/pr-143/REQUEST.md) · [Source diff](https://github.com/physicsvigilante/sim_heat/compare/c99940b6505fd0332d73c5cabc5718451ae0d22b...20718b37c3948e7751fa608638c77a95436ddcee)

## Independent offline checks

- Ran the two focused source tests on Python 3.13.5. Both passed, including the equal-bath, negative-contact, terminal-selection and layer-count controls.
- Constructed a four-layer reference from exact face pairs (240,252), (255,267), (267,279), (315,327) K, contacts 0.125, 0 and 1.5 K/W, the pinned 2 W/K composite wall and slopes 0.001, −0.012, 0 and 0.012 per K. Each layer's reference temperature was its face midpoint, so the integral over each layer equaled its 12 K rise. Each oriented interval contained the expected −24 W or +24 W on reversal. All eight faces and each insert's signed 18 W magnitude were enclosed in both directions with alternating terminal orientation. Instrumentation counted 194 off-root inverse calls above the hot-bath potential across the two runs.
- Checked the inverse at both endpoints, within 10⁻³⁶ K of each endpoint, and at 700/3 K. Across 200–400 K with reference 300 K, slopes ±0.009999999999999999 per K approach vanishing conductivity at opposite ends. The constant and both nonlinear inverses enclosed each rational input temperature when supplied its exact potential.
- Isolated conductance uncertainty by injecting three two-terminal response intervals [1,3], [2,5], [3,9] W/K, with negative rod coefficients, and contacts 0.75 and 0.125 K/W. For all eight conductance corners at each bath orientation (300 and 400 K), direct series-resistance arithmetic gave signed currents, individual branch currents and all face temperatures inside the reported intervals. This injection tests propagation of uncertainty. The four-layer test above used real pinned source inputs.
- Checked why clipping preserves the sign of the final residual. At positive trial current any remaining layer requires a strictly positive potential increase, including after an upstream trial reaches the hot bath. The material positivity guard makes the inverse monotone over the admitted range. Rounding the square root and then the temperature outwards preserves the direction of the envelope.

## Archived evidence

Queried runs by exact source SHA and verified both successful job IDs. Downloaded the ZIPs via the GitHub artifact endpoint and computed SHA-256 over their bytes.

| Job | Artifact ID and SHA-256 | Content check |
|---|---|---|
| [Series wall](https://github.com/physicsvigilante/sim_heat/actions/runs/44877646175/job/136765775835) | 14696726079 · `af3b8da1dbbe696bfed032678c1727ccf044c94d0e4d036784f3755991a94da8` | The stack JSON equaled a fresh pinned local evaluation field for field. Four inherited wall/network JSON files were also present. |
| [TwinBridge](https://github.com/physicsvigilante/sim_heat/actions/runs/44877646264/job/136765776092) | 14696462968 · `1a9284659a2021bf522a5554b685bf1062969dc4657fb365a24511c835c30c9d` | The archived source head matched. Decompressed output, oracle results and all seven controls equaled their frozen local JSON records. |

The evidence supports steady two-terminal layers with a common linear relative conductivity law inside each layer, passive contacts, and prescribed bath temperatures. The CLI records offline provenance, with native execution, native qualification, independently certified reference and runner consumption all false. Native and classroom performance remain unassessed. Source merge requires the owner's separate decision.
