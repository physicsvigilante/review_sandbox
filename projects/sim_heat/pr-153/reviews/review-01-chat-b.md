# Independent R2 review of shielded body cooling

**Accepted for the offline shielded-body target calculation at the reviewed head.** I found no blocking defect. The source base is `50f44eb9260c27e302700241282bc23c5e95bda5`, the head is `2083be6a02c51f95d178ed8dfeb0176a767f2fb1`, and the hub request is pinned at `4c368735ff3ba897f13236e635b057f367dc06ec`. [Draft source PR 153](https://github.com/physicsvigilante/sim_heat/pull/153)

## Physics and reachability

I inspected the six-file diff. Equal-area parallel gray faces give a dimensionless resistance of 1/ε₁ + 1/ε₂ − 1 per gap. A storage-free isothermal shield carries equal power across its two sides, so summing gap drops in fourth-power temperature gives the coefficient used by the transient. The worked stack has total resistance 9.25 and coefficient 1/185000000 W/K⁴. A reflecting face interrupts radiative exchange while the independent rod coupling persists. Positive material conductivity makes each bath contribution decrease with body temperature. Radiation does likewise, which justifies the target-end reachability check and the directed-power endpoint bounds. Taking all four corner products of the radiation and residence-time bounds covers a panel containing a sign change.

I separately integrated temperature, radiative energy and conducting energy together in time using SciPy DOP853 with terminal temperature events. I used the 2 W/K composite rod, integrated its linear conductivity analytically between bath and body, and computed the radiation coefficient from the face resistances. All reported intervals enclosed these independent values (reflector energy zero and floating-point round-off in the analytic 1200 J case).

| Body excursion | Conditions | Time (s) | Radiation into body (J) | Conduction into body (J) |
|---|---|---:|---:|---:|
| 450 → 390 K | Worked two-shield case, 400 K enclosure | 101.917966 | −876.496681 | −5123.503319 |
| 305 → 361 K | 350 K enclosure, three face pairs (0.15,0.8), (0.9,0.5), (0.33,1), relative slope 0.003/K | 56.734769 | 307.870044 | 5292.129956 |
| 365 → 377 K | 700 K enclosure, shield (0.7,0), relative slope −0.002/K | 94.958536 | 0 | 1200 |

All cases use 100 J/K heat capacity, 380 K rod bath and 300 K conductivity reference. The first two cross the enclosure temperature in opposite directions. With the bath and enclosure both at 380 K, approaching 380 K from 390 K or attempting to pass it from 370 K returned unreachable in finite time. Starting at the equilibrium target returned already at target.

The exact-head shielded-body, radiating-body time and energy, shield stack, single-shield and radiative-gap modules passed all 18 tests. The unshielded coefficient, schema and energy calculation remain compatible, and the steady stack still uses the same ordered gap arithmetic. An initial test-launch attempt used an unavailable temporary export and reported import errors in an older checkout. The reported passing run used a fresh Git archive of the specified head.

## Archived CI

Both runs reported success at the reviewed SHA. I downloaded the ZIPs, recomputed each SHA-256, and checked all ZIP entry CRCs.

- H1 archive `e7c94232b4e78c70ebd4829274fa61b721b71eb6fc99e91b74f173d7c038c3c2` contains the exact source-head record. Its decompressed fresh output, seven-control report and oracle report matched the frozen held-out JSON records. [H1 archive](https://github.com/physicsvigilante/sim_heat/actions/runs/44883505665/artifacts/14698599209)
- Series archive `fdd7d6074901cc12cdc979f5d1eeaf61ebab077862496371a8bb69fdeb2dc9a0` contains five JSON files. I reproduced the shielded-body JSON field for field using the reviewed code. It retains false values for native execution, native qualification, independently certified reference and runner consumption. [Series archive](https://github.com/physicsvigilante/sim_heat/actions/runs/44883505615/artifacts/14699171140)

The verdict applies to the admitted parallel-plate, storage-free shield model and an isothermal body. All transient evidence here is offline numerical evidence. The source PR remains subject to owner merge approval.
