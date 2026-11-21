# Independent Chat B review of SIM_HEAT PR 125

**Verdict: accept for the requested offline observation.** I found no blocking issue in carrying both phase inventories, bounding first depletion, or stopping the schedule. Reviewed source head `b16004ff5f84a6d67b24e8681071d969cf83921e` against `5cc43d06ac32ae780ad4727ac399eb353a32c944` under the [pinned request](https://github.com/physicsvigilante/review_sandbox/blob/3521612d2320806ba2d3ee46053591d3550a1879/projects/sim_heat/pr-125/REQUEST.md). I served as the separately dispatched Codex Chat B reviewer.

## Independent physical check

I used the three-terminal triangle, holding cool at 280 K and the middle bath at 300 K. The pinned rods give conductances 0.6, 1 and 1.5 W/K between warm–middle, warm–cool and middle–cool respectively. For a 1 m² black surface with sigma 0.00000005 W/(m² K⁴), I bracketed the face temperature by 190 rational bisections on [0,1000] K using the three-term surface energy balance. The bath receives 0.6(Tface−300)−30 W. With 2 kg solid, 1 kg liquid and latent heat 1000 J/kg, I integrated each independently calculated power until the next switch or the appropriate energy limit.

| Requested stages (K × s) | Signed bath powers through depletion (W) | Cumulative energies at completed switches (J) | First depletion |
|---|---|---|---|
| 470×2, 230×3, 470×100, 400×1 | +63.843959, −59.417110, +63.843959 | +127.687917, −50.563413 | 37.118362644 s, +2000 J, zero solid |
| 230×2, 470×1, 230×50, 800×1 | −59.417110, +63.843959, −59.417110 | −118.834220, −54.990262 | 18.904673543 s, −1000 J, zero liquid |

For all six evaluated stages I checked enclosure of signed bath, reservoir and radiative rates, cumulative energy, both masses and absolute end time. Each sequence stopped in its third stage. The exact-rational interval update clips accumulated latent energy to the two physical inventory limits. Earliest and latest possible first-hit times use oppositely ordered numerator and power extrema for heating and cooling. A switch inside that interval terminates with an uncertain status and the possible end times are intersected with the exposure duration.

Six focused local regressions passed, including exact depletion at the switch, zero drive, a deliberately broadened power interval with partial event overlap, and prior plateau observations. Additional invalid-schedule probes refused zero duration and a negative enclosure in an otherwise unreachable suffix. The uncertain-event regression injects interval power. It establishes event handling under uncertainty; the triangle calculations exercise actual conductor and radiation laws. All physics checks ran offline.

## Archived evidence and compatibility

I checked successful job 136742210898 in run 44870018803 and job 136742210937 in run 44870018815, downloaded both archives, recalculated their SHA-256 hashes and checked all ZIP entries for integrity. Wall artifact 14693760904 had five members and digest `10cb6f630407a5b5638e02ba09d5e02fa8b6c4052e0e8617b03dcaa1d75f5afe`. The archived sequence JSON matched my local replay in full. Its four capability flags are false. Twin-bridge artifact 14693770892 had four members and digest `29c6a5d9a713740799b496bd18371d8db8c75bb86fbabaec42f911a0d80a362b`. Its recorded source head matches the reviewed SHA. I inspected its archived control, oracle and decompressed output records. [Wall CI](https://github.com/physicsvigilante/sim_heat/actions/runs/44870018803) · [Twin-bridge CI](https://github.com/physicsvigilante/sim_heat/actions/runs/44870018815)

The first compatibility probe mistakenly looked up the new bath-flow field name in the older schema and raised KeyError. With the older field names, seven values matched exactly for the 420 K, 1000 s first star exposure, covering inflow, duration, latent energy, both inventories, radiating face and maintained reservoir. The results support the bounded offline plateau observation through first depletion. Native plateau execution, phase evolution after depletion and source merge remain outside this verdict.
