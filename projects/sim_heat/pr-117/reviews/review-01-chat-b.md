# Chat B independent offline R2 review of PR 117

**Verdict: accept for the requested offline scope.** I found no blocking defect in the signed rod observations on the pinned source. The optional result uses the authored rod direction from port a to port b. A negative entry reports heat transported in the opposite direction.

- [Review request at 0693f99](https://github.com/physicsvigilante/review_sandbox/blob/0693f99db5b656128d27b3f0cc2ae9b701f2eb46/projects/sim_heat/pr-117/REQUEST.md)
- [Draft PR 117](https://github.com/physicsvigilante/sim_heat/pull/117), base `deb8ed877329a6efe21af7926269bcc300f074df`, head `3afe62a6bc8e3e693a79b54887c08d816f950ba8`. The local clean checkout and GitHub head agreed.

## Worked 1000 s wall

The facing conductance is 4 W/K, in series with parallel conductances 1 and 3 W/K. The equivalent conductance is 2 W/K. At 120 W the donor exhausts 90,000 J of latent heat in 750 s. Its solid heat capacity is then 1100 J/K, and the receiver remains on its plateau. At 1000 s the temperature difference is `60 exp(-250/550)` K. The integral is `90000 + 1100 (60 - ΔT)` J. In a 90-digit decimal calculation, the rational output intervals enclosed every reference below. The archived JSON matched a fresh local run.

| Rod | Instantaneous W | Cumulative J |
| --- | ---: | ---: |
| facing | 76.168370273 | 114107.396350 |
| strip | 19.042092568 | 28526.849087 |
| insert | −57.126277705 | −85580.547262 |

The reversed insert accounts for three quarters of the physical outward heat. At the interface, facing equals strip minus insert for both rate and heat.

## Independent bridge and changing-temperature checks

I exercised two bridge conductance sets with either terminal as donor. Both reservoirs had 1 kg solid and 1 kg liquid, latent heat 10 J/kg, and transition temperatures 320 and 300 K. With solid and liquid specific heats of 10 and 20 J/(kg K), both phase inventories exhaust together at 10 J. At six seconds both temperatures have moved. I calculated the remaining drive directly as `20 exp[-G(1/20 + 1/40)(6 - 10/(20G))]` and total transfer as `10 + (20 - ΔT)/(1/20 + 1/40)`.

The unit-drive junction balances give ordered rod coefficients (feed, drain, inlet, outlet, link) of (1, 1, 0.5, 0.5, 0) W/K for the balanced bridge and (1.4, 1.3, 0.45, 0.55, 0.1) W/K after the feed change. These satisfy both junction balances and give G of 1.5 and 1.85 W/K. For each polarity I checked all five signed rates against coefficient times drive and all five energies against coefficient/G times transfer, reversing signs when the cold-named port was hotter. All intervals enclosed the expected value with widths below 1e-12 in their respective units. Both bath temperatures also agreed. The default terminal responses equaled the base implementation for both bridges. Removing only the optional rods field recovered the base duration result for all four cases and the worked wall.

## Regression and CI archives

Fifteen local tests passed across phase branch flow, terminal response, time-state, coupled baths, transfer time and equilibrium. These include equal temperatures, missing-input and invalid-contact refusals. Both jobs checked out the PR head and succeeded. I downloaded both ZIP archives, checked their SHA-256 digests and ZIP integrity, and inspected their contents.

- [Series job 136736086300](https://github.com/physicsvigilante/sim_heat/actions/runs/44868053612/job/136736086300) produced [archive 14692339267](https://github.com/physicsvigilante/sim_heat/actions/runs/44868053612/artifacts/14692339267), SHA-256 `eac4ce07f92a50ba99115d09a2d2998b8d86653ff536f8178f536f9b750cabc0`. All 13 JSON files parsed. The 1000 s result preserved the separately archived previous observation exactly after removal of the rod field.
- [General replay job 136736085972](https://github.com/physicsvigilante/sim_heat/actions/runs/44868053609/job/136736085972) produced [archive 14692643573](https://github.com/physicsvigilante/sim_heat/actions/runs/44868053609/artifacts/14692643573), SHA-256 `d481dad4d2110929ffb1c00d9cb618d02f2d01e272a270fafa20fbb92b49feb7`. The source-head member identified the pinned commit. The decompressed fresh result matched the frozen first output as JSON. I reran the TwinBridge verifier over the archived candidate (49,241 analytical comparisons) and reran the seven controls. The resulting reports matched both the archive and frozen records.

This review covers linear, fixed, storage-free rod networks coupled to the admitted two-bath enthalpy model. The results retain false values for native execution, native qualification, independently certified reference and runner consumption. I performed no native or classroom evaluation. The source PR stays draft and unmerged.
