# Independent R2 review of named observation passages

**Verdict: accept for the offline observation scope.** Reviewed draft [SIM_HEAT PR 91](https://github.com/physicsvigilante/sim_heat/pull/91), base `38063a51ec3a33445aea658d68e4eaadbec0ac3f`, head `53bda493612785d11c1a711f6cce368c656f666b`, against the [pinned request](https://github.com/physicsvigilante/review_sandbox/blob/952a6b81b41f8e5d4238045a0e61fbbf3ce99241/projects/sim_heat/pr-91/REQUEST.md). GitHub returned those exact refs and a clean local checkout supplied the code for the reviewer runs.

## Hosted evidence

Both jobs succeeded at the reviewed head. I downloaded both ZIPs and hashed the archive bytes. The study artifact SHA-256 was `1938067b5904b97ab6ad6faf4460fafcf57c05b1e0ad6c5759dbfea0ec568e80`. Its two named-request JSON results matched my local outputs in every field. The TwinBridge ZIP SHA-256 was `4f7ed3ff599ad40bbda8ec10cfc970cb43a165992affeb544d4a711a75c19730`. Its ZIP CRCs passed, source-head.txt contained the reviewed head, and the archive contained the reference candidate, oracle and refusal results. [Study job](https://github.com/physicsvigilante/sim_heat/actions/runs/44860380511/job/136712144674) · [TwinBridge job](https://github.com/physicsvigilante/sim_heat/actions/runs/44860380383/job/136712144565)

## Physical and adversarial checks

- D1 has capacity 500 J/K and conductance 0.2 W/K to a bath 60 K above the initial body temperature. Thus stored-energy gain is 30000(1 − exp(−t/2500)) J. Half gain occurs at 1732.8679514 s, inside the increasing bracket [1725, 1737.5] s at indices 138–139.
- D2 has capacities 500 and 1500 J/K. Its hot-minus-cold gap decays with rate 0.2(1/500 + 1/1500) per second. The 1 K passage occurs at 7676.8960542 s, inside the decreasing bracket [7668.75, 7678.125] s at indices 818–819.
- I authored a temporary D2 variant named `reverseGap`, swapped both port operands and refreshed the study and facts pins. At −1 K the passage became increasing at the same indices. The former request name and a J threshold for the new request each produced the expected refusal.
- At radius 1 and threshold 0, my five-sample sequence [−2, −1, 0, 1, 2] counted three overlaps and returned the single increasing bracket [0, 2] s on a half-second grid. The code compares exact rational distances to the maximum absolute radius for that request, including equality as overlap. Its scales agree with preparation's K/W and J budgets. A bracket establishes at least one crossing for a continuous observable. It does not establish uniqueness.
- Eleven focused tests passed locally across the named-request, existing temperature and heat-flow reversal suites. Hosted legacy outputs retained the two blue-body passages (indices 369–370 and 943–944) and the positive-to-negative lower-rod reversal (415–416).

The observed results retained false native execution, qualification, independent certification and runner-consumption flags. This separate-context review covers offline threshold interpretation and sampled brackets. It supplies no new OpenModelica execution, external human certification or source merge authorization.
