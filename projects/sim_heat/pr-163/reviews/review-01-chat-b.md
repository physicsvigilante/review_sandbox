# Chat B independent R2 findings for PR 163

**Accepted for the specified offline inverse-calorimetry scope.** I found no blocking defect in the reviewed changes. Source base `279bba48010368e1a876525b2d0fe7aee303eb99`, head `1e99769bae1ba9de2748605d29592cc31d104efe`, packet `1a75c45b8c7c4f7599e108c79625f0d866a11e6d`. [Source diff](https://github.com/physicsvigilante/sim_heat/compare/279bba48010368e1a876525b2d0fe7aee303eb99...1e99769bae1ba9de2748605d29592cc31d104efe)

## Independent physics and refusal checks

The wall givens yield conductances 4 W/K on either side of the interface, giving 200 W unheated hot supply at 100 K bath difference. Uniform source power contributes half at each rod endpoint. The 40 W strip shifts the interface by 2.5 K and directly delivers 20 W to cold. The resulting background is +190 W hot and −230 W cold. For facing and insert powers P and Q, each bath's supply decreases by (3P+Q)/4 and (P+3Q)/4 respectively. The determinant is 1/2. I evaluated the four measurement corners independently and checked each through the source entry point. The individual ranges are 238–242 W and 78–82 W. These are marginal ranges, with correlated powers within them.

I also applied a forward balance to the three-terminal star with conductances 2, 3 and 5 W/K and baths at 380, 330 and 280 K. The junction temperature is 315 K plus the total generated watts divided by 20 W/K. Each bath supplies its conductance times its temperature excess above the junction, less half its rod's source power. I supplied the first two powers as unknowns and the third as known for three triples in watts, (50,90,20), (60,30,10) and (100,10,30). Each of the three bath pairs enclosed both true powers with interval widths below 1e−18 W in all nine reconstructions. The first case had signed supplies +89, −24 and −225 W.

All nine tests across the new module, rod generation and single-rod inference passed locally on the pinned archive. The new tests exercised singular partitions, a duplicate bath, negative inferred power, an overlapping known source, reversed intervals, and permutations of the two measurements and rods. Source inspection confirmed interval division follows a determinant-zero exclusion, and a lower inferred bound below zero refuses the observation.

## CI and archive replay

Both exact-head workflows succeeded. I downloaded the ZIPs, recomputed SHA-256, and verified the following.

- Series artifact `14699513133` matched `e324658a90e0a953f6663ddfb7af7ba94efbf63d777bc4812d7bbb11f1b26cd3`. A fresh CLI invocation produced JSON equal to the archived calorimetry result, including the input hashes and four false qualification/execution flags. [Series run](https://github.com/physicsvigilante/sim_heat/actions/runs/44886048823)
- General-conduction artifact `14700052535` matched `944fed03c6d3a127272b151678973537a04fb60cabce42cae9717cfc3b928a04`. The archive's source-head entry matched the pin. Independently rerunning the conduction command, oracle and controls reproduced the decoded candidate and both reports. They also matched the frozen held-out evidence. [General-conduction run](https://github.com/physicsvigilante/sim_heat/actions/runs/44886048864)

The first local test invocation missed a temporary checkout across sandbox calls and failed at module import. I reran it against a persistent exact-commit export for the results above. The evidence supports steady uniform heating and bounded signed bath supplies in the offline model. Native OpenModelica execution, native qualification and experimental accuracy remain outside this review. Source remains draft and unmerged.
