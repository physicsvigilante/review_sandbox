# Independent Chat B review of calibrated wall cooling

**Verdict** — Accepted for the stated offline analytical scope. No blocking or major finding on source head `7b24f37ea9e21a080590c605cef162f9e68b12b8`, base `cd88e589f1b7139ce29c48ca3ed75dda8b90da70`, packet `9a70d5c6f796e015af0212119cea6cc47f542fe4`. [Draft source PR 160](https://github.com/physicsvigilante/sim_heat/pull/160)

## Independent physics checks

The star source has leg conductances 2, 3 and 5 W/K. Releasing the middle terminal gives an open temperature of (2 × 380 + 5 × 280)/7 K and a driving-point conductance of 3 × 7/(3 + 7) W/K. The measured increments halve every 20 s. With 100 J/K capacity, 2 W/K wall and 0.5 m² air area, the fitted coefficient is 10 ln(2) − 4 W/(m² K). The fitted equilibrium is 390 K and its balance requires the air temperature to be 390 + 40/h K.

I checked three transfers at 180 decimal digits. For each row I independently evaluated the new steady balance, time constant, half-life and exponential temperature. All four reference values lay within their reported fractional intervals.

| New area (m²) | Capacity (J/K) | Initial (K) | Elapsed (s) | Reference final temperature (K) |
|---:|---:|---:|---:|---:|
| 1 | 150 | 430 | 60 | 372.789097206452215567787 |
| 0.125 | 33 | 175 | 0.000001 | 175.000011038887610973982 |
| 7 | 20 | 120 | 10000 | 394.81868000347290630025 |

For positive conductances the steady weighted mean is monotone in each temperature and has a fixed derivative sign in either conductance with the other inputs fixed. The corner enumeration thus covers all possible results, including correlated calibration quantities. The exponential time update is affine in each of the equilibrium and decay factor separately. I checked the exponential enclosure at 0, 10⁻¹⁸, 255.999, 256 and 256.001. At and above the cutoff, exp(−z) ≤ exp(−256) < 2⁻²⁵⁶. The six focused source tests passed, including the exact initial condition and 395 K withheld fourth reading.

Independent negative controls refused a negative duration, zero heat capacity, missing port and corruption of either input facts pin separately.

## Archive verification

I verified GitHub's successful conclusion, source head and artifact/run association for each run, downloaded the original ZIPs, checked all ZIP members' CRCs, and computed the SHA-256 digests.

- [Series run 44885191212, artifact 14700065844](https://github.com/physicsvigilante/sim_heat/actions/runs/44885191212/artifacts/14700065844) — `242d0b21cf6b7e008adfd155f0ed9defeb2c3864803135fe2f261d7438489344`. Five entries. The complete archived calibrated-wall JSON equalled my local result at the reviewed source head, including both independent sets of provenance fields.
- [H1 run 44885191260, artifact 14700155532](https://github.com/physicsvigilante/sim_heat/actions/runs/44885191260/artifacts/14700155532) — `cdbd12f8070d567b0a8eb05d423d75e9198abbd26fa9ef4ec392e5ab4fa17d84`. Four entries. The embedded source head matched. The archive contains offline control, oracle and replay evidence.

The transfer assumes exact readings, constant lumped capacity, negligible radiation, fixed baths, and the same uniform air temperature and film coefficient across both experiments. The checks establish offline interval predictions under those assumptions. OpenModelica execution, measured hardware transferability and classroom effectiveness remain outside this review. Native and independent-certification flags remain false. The source PR remains subject to owner merge approval.
