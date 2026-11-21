# Independent Chat B review of phase-bath target time

**Verdict — accept the bounded offline observer.** I found no blocking defect at head `590056d97e5efc8a767f7d653055841beb685f9e` against base `2cbf9781978a388265a654849366466e1b3a418a`. I reviewed the six-file diff in a fresh reviewer context and used the pinned Python executable for independent checks. The source PR remains subject to separate owner merge approval. [Source PR](https://github.com/physicsvigilante/sim_heat/pull/112) · [Pinned request](https://github.com/physicsvigilante/review_sandbox/blob/0b4c3ff7ea5e69da83cb01cfa7d80f0ac93dbed5/projects/sim_heat/pr-112/REQUEST.md)

## Physics and signed energy

During coexistence, a constant port inflow exhausts the available solid or liquid. The signed latent energy divided by the inflow gives a positive plateau duration. After exhaustion, integrating the heat balance gives the sensible time as the total final heat capacity times the port resistance times the natural logarithm of the initial-to-final equilibrium temperature-gap ratio. Both gaps retain the same sign and their ratio exceeds one in each admitted direction. The sensible energy is total mass times final specific heat times signed temperature change.

| Independent case | Plateau (s) | Sensible (s) | Total (s) | Latent, sensible energy into bath (J) |
|---|---:|---:|---:|---:|
| Worked wall, 273.15 to 293.15 K | 781.469350 | 261.126796 | 1042.596146 | +167000, +50400 |
| Three-bath star, 340 to 320 K | 3500.000000 | 915.257968 | 4415.257968 | −231000, −38000 |

I calculated the star's open temperature as (2 × 380 + 5 × 280)/7 = 2160/7 K and its resistance as 1/3 + 1/7 = 10/21 K/W. Independent high-precision logarithms also agreed for star heating to 308.571428571428571428 K and for wall heating and cooling to within 10⁻¹⁸ K of their respective equilibria. The latter two elapsed times were 58890.095996 s and 46123.376238 s for the tested inventories. All three signed energy fields matched the separate energy balances.

## Uncertainty and refusals

I exercised the target entry point with a deliberately widened three-terminal response row. Cold coupling was 1.5 W/K, hot coupling ranged from 0.50 to 0.70 W/K, and self-conductance ranged from 2.0 to 2.2 W/K. For each of 21 physically consistent couplings, the returned intervals enclosed both stage times and their sum for heating from 270 to 295 K and cooling from 340 to 320 K. Heating to 309 K and cooling to 310 K were refused because the interval included equilibria on both sides of the target. Starting at 309 K with that uncertain row was refused for unresolved heat direction. This interval stress test used an injected response law. The worked wall and star cases above ran through the actual pinned study loader.

My first widened-row probe compared a rounded 120-digit decimal against an exact rational plateau endpoint. It failed at the endpoint for 270 K with hot coupling 0.50 W/K. Repeating with exact rational plateau times and 160-digit logarithms passed all 42 cases.

Through the normal entry point I also confirmed refusal of exact equilibrium at the initial plateau, a target equal to the plateau or at/beyond equilibrium, reversed target direction, zero transition temperature, zero latent heat or inventory, zero or malformed specific heat, zero target, unknown port and stale facts hash. The seven source tests across target time, latent bath and terminal response passed locally.

## CI and archived evidence

I checked the job results and head SHA through GitHub and independently downloaded, hashed and CRC-checked both archives. Fresh local outputs matched the parsed archived target example and both inherited 600 s and 1000 s latent-bath records in every field. The target example has all four flags false for native execution, native qualification, independent reference certification and runner consumption. [Phase study job](https://github.com/physicsvigilante/sim_heat/actions/runs/44866785920/job/136732125538) · [Archive, SHA-256 3c81390bb28da629b3c30933c03385a478b5b7ea42bcf674166c4ce910a13b37](https://github.com/physicsvigilante/sim_heat/actions/runs/44866785920/artifacts/14692017996)

The general conduction job passed its frozen evidence, regression and independent replay steps. Its archive carried the exact source SHA, compressed fresh output, seven control records and 41 oracle channels. The largest recorded ratio to the original one-percent budget was 1.985 × 10⁻⁷ (rounded up). This CI and the present review cover offline behavior. No new OpenModelica execution, native qualification or classroom validation was performed. [General conduction job](https://github.com/physicsvigilante/sim_heat/actions/runs/44866785783/job/136732124896) · [Archive, SHA-256 ecf6267ef746e6857336320cc8e76d3c632ebbdbaa42112cc2215d7427e65277](https://github.com/physicsvigilante/sim_heat/actions/runs/44866785783/artifacts/14692365995)
