# Chat B review of SIM_HEAT #123

**Verdict: accepted for the requested offline R2 scope.** I found no blocking or major defect. I reviewed the four-file source diff, ran the eight focused tests, and exercised four additional mass targets. The review covers a coexisting, isothermal phase bath, constant latent heat, steady linear supports and a single radiative exterior through the requested deadline. It does not qualify native execution, post-depletion temperature evolution, or classroom outcomes.

The GitHub PR was open and draft, with base `9b874afda17f968b8ab8af9d0cb65922d854fe16` and head `700ebd552170514953ce6ff863512787c4ebb28c`. My local checkout matched the head and was clean before and after testing. I used a fresh owner-selected local Codex reviewer context. My calculation was independent of the implementation's terminal-response matrix. This is a model review, without independent human or native certification. [Pinned request](https://github.com/physicsvigilante/review_sandbox/blob/f00ffc3b186c723e1bd060ddb8a2160b64bf2a69/projects/sim_heat/pr-123/REQUEST.md) · [Source diff](https://github.com/physicsvigilante/sim_heat/compare/9b874afda17f968b8ab8af9d0cb65922d854fe16...700ebd552170514953ce6ff863512787c4ebb28c)

## Independent network and inventory calculation

I used `studies/joined_terminals`, with warmL held at 300 K as the bath, coolL released as the surface, middleR at 330 K and coolR at 280 K. From the six rods, let q be watts into the bath, C and J the centre and contact temperatures, and S the surface temperature. Node balances give C = 300 + q/2, J = (3C + 0.6×330 + 280)/4.6, S = (10C − 600 − 3J)/5 and incoming radiant power R = 5(S − C). With area 2 m², emissivity 0.75 and sigma 5.67e−8 W/(m² K⁴), the independent enclosure fourth power is S⁴ + R/(8.505e−8). I checked the reported bounds using exact rational arithmetic. Each enclosure interval was narrower than 1e−15 K.

| Process | q (W) | Energy at 800 s (J) | S (K) | R (W) | Enclosure (K, rounded) |
|---|---:|---:|---:|---:|---:|
| Melt | +8 | +6400 | 7054/23 | 310/23 | 308.059858645 |
| Freeze | −8 | −6400 | 6758/23 | −250/23 | 292.558381250 |

Each case converts 0.04 kg at 160000 J/kg. From 0.17 kg solid and 0.23 kg liquid, melting leaves (0.13, 0.27) kg and freezing leaves (0.21, 0.19) kg in solid/liquid order. Starting with exactly 0.04 kg of the consumed phase gives (0, 0.27) kg for melting and (0.21, 0) kg for freezing. The returned powers, energies and final inventories matched all four cases. The full-conversion cases reach zero at exactly 800 s under the reference power.

## Forward, refusal and compatibility controls

I ran the existing forward plateau solver at 308 and 309 K for melting and at 292 and 293 K for freezing. The resulting flow intervals lay strictly on opposite sides of the respective target power. Both partial targets retained coexistence at each neighbouring temperature. Both full targets switched between coexistence and exhaustion on the expected sides, including the reversal for freezing. Excess solid and liquid conversion were refused separately. A tiny radiating area of 1e−7 m² at the freezing target required an impossible negative enclosure fourth power and was refused. A stronger cooling request needing a negative surface temperature was also refused. With the phase target omitted, the complete zero-flow result on the six-rod case equalled the base commit's result.

## CI archive inspection

Both GitHub jobs succeeded at the pinned source head. I downloaded the actual ZIPs, independently hashed their bytes, tested every member's CRC and inspected their contents.

- **Wall**, job 136740902888, archive 14693212410, 4103 bytes, SHA-256 `e2b8c87089836aa0572af0de2ce33af110097f801007c0718810782b7617076a`. The six members included both timed records. Replaying the pinned star inputs locally reproduced both complete JSON observations. They report +20 W and −20 W, +20000 J and −20000 J at 1000 s, and enclosure temperatures of approximately 397.528096 K and 324.472902 K. [Job](https://github.com/physicsvigilante/sim_heat/actions/runs/44869595076/job/136740902888) · [Archive](https://github.com/physicsvigilante/sim_heat/actions/runs/44869595076/artifacts/14693212410)
- **Twin-bridge**, job 136740902776, archive 14693287036, 316924 bytes, SHA-256 `89235ba086647c2d4c18eb90b9610b94c5109cae2a5056dd395f92f1e7f545c4`. Its source-head member matched the candidate. The contents included seven refusal/mutation controls, 41 oracle series (largest reported ratio to the original one-percent budget 1.985e−7 rounded upward), and a readable compressed fresh output. Native execution, native qualification, independent reference certification and runner consumption flags were all false. This is inherited offline regression evidence. [Job](https://github.com/physicsvigilante/sim_heat/actions/runs/44869595091/job/136740902776) · [Archive](https://github.com/physicsvigilante/sim_heat/actions/runs/44869595091/artifacts/14693287036)

I made no source change and left the PR unmerged. Merge approval remains with the owner.
