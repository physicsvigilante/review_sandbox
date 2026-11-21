# SIM_HEAT PR 127 independent Chat B review

**Verdict — accept for the requested offline recovery calculation.** I found no blocking or actionable defects. I reviewed the four-file diff from `b16004ff5f84a6d67b24e8681071d969cf83921e` to `68e272d841db22841642202fc1ae804f4ce50910` as the owner-selected Codex reviewer in a fresh context. The source worktree HEAD matched the packet. The review covers a steady radiating face and an isothermal two-phase bath during coexistence. [Source PR](https://github.com/physicsvigilante/sim_heat/pull/127) · [Pinned request](https://github.com/physicsvigilante/review_sandbox/blob/a4ab6d8e762e764224b415d053c78b28ebed8a79/projects/sim_heat/pr-127/REQUEST.md)

## Independent energy, mass and time checks

I solved the star junction balance from its 2, 3 and 5 W/K rods and bisected the radiating face balance independently using 90-digit decimal arithmetic. For a 302 K bath, 280 K maintained reservoir, 1 m² face, emissivity 0.8 and sigma 0.0000000567, I used 170000 J/kg latent heat and 0.43 kg solid plus 0.19 kg liquid. Each stage's accumulated energy E, remaining solid mass (0.43 − E/L) and liquid mass (0.19 + E/L) fell within the returned bounds in both the star and equivalent triangle. I checked recovery inflow, signed recovery energy, duration, absolute end time and exact final masses in all four runs.

| Schedule (K × s) | Recovery enclosure | Net energy before recovery | Additional time |
|---|---:|---:|---:|
| 435 × 173, 296 × 41, 375 × 23 | 305 K | +5072.2502622 J | 150.873482167 s |
| 295 × 211, 417 × 37, 299 × 19 | 430 K | −7753.8324691 J | 222.147865064 s |

The magnitude of recovery time equals |E|/|Q|. The code uses the smallest numerator and largest denominator for the lower bound, and reverses those choices for the upper bound. Energy added during recovery lies in [−E_high, −E_low]. Monotonic return from a coexisting inventory to its initially positive masses preserves both phases throughout recovery.

## Edge and refusal checks

- The exact equilibrium schedule of 13 seconds at 280 K, with the bath, maintained reservoir and recovery enclosure also at 280 K, gave zero recovery energy, zero additional time and absolute end time 13 s.
- The wrong-direction enclosure, 30000-second solid or liquid depletion, and a 435 K exposure of 1929.995731182624543228 s with uncertain depletion all refused recovery. The ordinary schedule reported `exhaustion_time_uncertain` in the last case.
- A 435 K exposure for 100 s followed by 296 K for 100.230085390163310158 s gave an energy interval spanning zero (approximately −1.92e−16 to +3.10e−16 J). Recovery refused. My first cancellation probe supplied more than 18 decimal places and hit the input grammar. The reported case uses the admitted precision. A separate nearly balanced recovery enclosure of 369.637602348236142782 K after one second at 435 K also refused.
- Both checked-in recovery unit tests passed locally.

## Pinned CI evidence

I checked successful job conclusions and artifact metadata for the pinned head, independently downloaded both ZIPs, computed SHA-256 over their bytes, and checked every ZIP entry's CRC.

- Series job 136748377784, artifact 14694376289, SHA-256 `c36d5cf4b09df55b70417a0c41dbfa82c30906b48c33e452cd3d9db5f65bbf80`. All five JSON members parsed. The archive contains wall, series, revised-wall and full-network records plus `phase-recovery-time.json`. The complete archived recovery document matched the local result for the workflow inputs. Its native execution, native qualification, independent certification and runner-consumable flags were all false. [Job](https://github.com/physicsvigilante/sim_heat/actions/runs/44872001048/job/136748377784) · [Archive](https://github.com/physicsvigilante/sim_heat/actions/runs/44872001048/artifacts/14694376289)
- General conduction job 136748377818, artifact 14694411234, SHA-256 `ba98c2a2d0176434f1139a7216c2152f2bdd8a80dcce9dffa95290d35e070ae1`. The embedded source head matched the review SHA. The decompressed fresh TwinBridge result matched the frozen first output as parsed JSON. Both the oracle and control records matched their frozen counterparts. [Job](https://github.com/physicsvigilante/sim_heat/actions/runs/44872001077/job/136748377818) · [Archive](https://github.com/physicsvigilante/sim_heat/actions/runs/44872001077/artifacts/14694411234)

All physics checks were offline. Native qualification and source merge require separate authority and evidence.
