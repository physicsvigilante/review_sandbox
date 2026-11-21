# Chat B review of insulated two-body exchange

**Verdict — accept for the bounded offline observer.** I found no blocking or major issue. I reviewed the five-file change on base `a6e667663153145782cf132f8e71a204b6326b65` at head `a192da4d8d79b1fa39c8a5b81d86a7d34368f17d`. GitHub reported the same refs and an open draft PR. [Source PR](https://github.com/physicsvigilante/sim_heat/pull/97) · [Pinned request](https://github.com/physicsvigilante/review_sandbox/blob/089858d08d5648fa9cf5b829de213ff551392663/projects/sim_heat/pr-97/REQUEST.md)

## Physical law and source interpretation

For algebraic, storage-free rods between two uniform bodies, the signed power from body 1 to body 2 is G(T1−T2). Kirchhoff balance at internal nodes makes the endpoint powers equal and opposite. Applying C1 dT1/dt = −G(T1−T2) and C2 dT2/dt = G(T1−T2) gives exponential decay of the signed difference with time constant C*/G, where C* = C1 C2/(C1+C2). Integrating the power gives C*(T1−T2) joules at infinite time. Total initial internal energy determines the capacity-weighted equilibrium temperature. The implementation orders the two owners by name and negates incoming power at the first node under a unit difference. The units are W/K for G, J/K for C*, W for initial transfer, seconds for the time constant, K for temperature and J for integrated transfer. Zero initial difference gives zero transfer with a positive perturbation time constant.

The observer requires one connected transient component, exactly two bodies, no maintained temperatures and resolved positive conductance. It calls the inherited general preparation path, which binds the authored model, study, analysis and pinned facts. The four offline status fields are copied from that preparation. The source fixtures describe illustrative inputs.

## Reviewer executions

- Replayed the three changed tests in the pinned local Python environment. All passed, including the equal-temperature parallel network and maintained-bath refusal.
- Independently selected a parallel-series network. I retained a 1/5 W/K direct rod and added two rods of 2/5 and 3/5 W/K in series with their A ends meeting at an ownerless node. The alphabetical first body started at 330.15 K with capacity 1500 J/K and the second at 300.15 K with 500 J/K. Series reduction gives 6/25 W/K, hence total 11/25 W/K. The observer returned exactly 11/25 W/K and 66/5 W initially, 375 J/K, +11250 J at infinite time and 322.65 K at equilibrium. The time interval contained 9375/11 s with width below 1e−10 s. Its facts SHA-256 was `407c270f1baf2c705ff891f562d89063c31c5b37c2432df1ea35321a79334f1c`. The first execution passed.
- Exercised a stale facts digest, a freshly hashed conductivity mismatch, and an unused source node. They were refused respectively at the source hash, model-to-facts binding and graph checks.
- D2 returned −60 K for cold minus hot, 1/5 W/K, −12 W initially, −22500 J at infinite time, 308.15 K and 1875 s. The authored history request uses the opposite temperature order. I compared all 1001 archived temperature differences and rod powers at their supplied times to 60 exp(−t/1875) K and 12 exp(−t/1875) W using 85-digit decimal arithmetic. Maximum absolute errors were 3.49e−15 K and 8.84e−16 W (rounded upward). Fresh local law and history outputs matched the archived JSON values.

## CI and provenance

Both jobs reported success for the reviewed head. I downloaded both ZIPs, recomputed SHA-256 and checked archive integrity. The 30-entry study archive included both D2 outputs. The four-entry TwinBridge archive recorded the reviewed source head. Its decompressed output, oracle results and seven controls matched the frozen historical JSON. Both workflows checked out the explicit PR head and ran offline. [Study job](https://github.com/physicsvigilante/sim_heat/actions/runs/44863019163/job/136720413429) · [General conduction job](https://github.com/physicsvigilante/sim_heat/actions/runs/44863019178/job/136720413548)

| Archive | Verified SHA-256 |
|---|---|
| [Study 14690347474](https://github.com/physicsvigilante/sim_heat/actions/runs/44863019163/artifacts/14690347474) | `70c899e8899b32c3b46f5f4213fd8492502ef4e86742530e1cf1b48303ea1545` |
| [General 14690508236](https://github.com/physicsvigilante/sim_heat/actions/runs/44863019178/artifacts/14690508236) | `6a3f40c24f36fa6f6d7322ca4409b13135ee2be73c9cdee72b042954282c942f` |

The law and the challenge both report false for native execution, native qualification, independently certified reference and runner consumption. This independent-in-context Chat B review establishes analytical agreement over the tested offline scope. No native job was run. Independent human source certification, experimental validation and classroom outcomes remain outside this review. Source merge requires the owner's separate approval.
