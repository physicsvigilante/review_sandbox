# PR 159 independent Chat B review

**Accept for the offline, constant-property, exact-reading inverse calculation.** I found no blocking or major defect. This review covers identification from three equally spaced readings with negligible radiation, fixed baths and known wall response, capacity and film area. Native simulation, experimental accuracy and source merge approval are outside this verdict.

Reviewed as an independent Codex reviewer of physicsvigilante/sim_heat draft PR 159, base e92df6371294eea259a97d0437f10a90d85effc5, head cd88e589f1b7139ce29c48ca3ed75dda8b90da70, packet d205afa5c3abeb84fe46fbb84a5e078c770d600a. Compared the diff, inspected the pinned model, checked local inverse and shared port sources against Git blobs, and ran the six focused tests successfully.

## Independent reference and refusals

For exact Kelvin readings x,y,z the recurrence gives equilibrium (xz−y²)/(x−2y+z). The total conductance is −C ln[(z−y)/(y−x)]/Δt. From the model, 4 W/K in series with parallel 1 and 3 W/K gives wall conductance 2 W/K. With the opposite bath at B the inferred air temperature is (G Teq−2B)/(G−2). These relations reproduce the worked example and its archived result.

Using 160-digit mpmath, I checked the exact equilibrium plus containment of G, h and air temperature for capacity 30 J/K and area 0.125 m². Additional cases were cold port (370,382,391) at 1 s, hot port (650,600,570) at 4 s, cold port (480,440,420) at 8 s, and cold port (400+4e−18,400+2e−18,400+1e−18) at 5 s, using decimal literals. My first hot-port probe used 10 s. It correctly refused because total conductance fell below 2 W/K. Repeating that negative case, a constant first pair, an unknown port and a wrong facts digest each produced the expected refusal. The focused tests also exercise alternating increments, linear readings, negative inferred equilibrium and negative inferred air temperature.

Exact rational differences preserve the geometry of the readings. Correct rounding of the integer logarithms and taking their immediate decimal neighbors enclose each logarithm; subtracting opposite endpoints, followed by positive rational scaling, bounds the rate. The film lower bound guarantees a positive denominator throughout the air-temperature calculation. Holding other coordinates fixed, its expression is monotone in each coordinate, so the eight corners bound the entire box even when the actual port and conductance estimates are correlated.

## CI and source provenance

Both pull-request workflow runs concluded successfully on the reviewed head. Independently downloaded the two ZIPs, verified SHA-256 and ZIP member integrity, and inspected their contents.

- Run 44884923630, artifact 14699308605, SHA-256 991b49a37afb98704433b353417dae1327442ab985d3a786e54e048cc221f008. The archived three-reading JSON exactly matched a local replay as parsed JSON. Its three SHA-256 fields matched the raw pinned model, study and facts blobs. Native execution, qualification, independent reference certification and runner-consumability flags were all false. [Series archive](https://github.com/physicsvigilante/sim_heat/actions/runs/44884923630/artifacts/14699308605)
- Run 44884923644, artifact 14700175008, SHA-256 280ceaa4c189d6e86ab3e0e4694dc418d8c1f7575ddec446bb5816cd31e962b5. The general conduction archive carried the exact source head, compressed replay, control refusals and oracle comparisons. Its role is historical regression coverage. [General replay archive](https://github.com/physicsvigilante/sim_heat/actions/runs/44884923644/artifacts/14700175008)
