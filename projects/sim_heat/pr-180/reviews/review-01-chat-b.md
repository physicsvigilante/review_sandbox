# Independent R2 review of the radial phase bath

**Verdict. Accepted for the bounded offline calculation at source head `4ca58b194f5911297e7883cba50439ebc6ea4b77`.** No blocking findings. I reviewed the change against `20bc1fddb2a88aee21d9dbaaadfc3f65a7267b23` under packet `5b1a17657db43addd9d3ed6740c88e69c4804aff`. [Source PR](https://github.com/physicsvigilante/sim_heat/pull/180)

## Independent balance and exhaustion

I used the three-terminal triangle, a 310 K phase bath at warm, the 330 K reservoir at middle, and the cool terminal at the inner face of a 1.25 m cylinder. The two coatings span 0.10–0.15–0.30 m with conductivities 2 and 1 W/(m K). The outer film has h = 4 W/(m² K) and 260 K air. Emissivity is zero. The rod dimensions give conductances 0.6, 1 and 1.5 W/K for warm–middle, warm–cool and middle–cool.

I calculated the cylinder-plus-film resistance independently as R = ln(1.5)/(5π) + ln(2)/(2.5π) + 1/(3π) K/W. Inner-face balance gives (310 − T) + 1.5(330 − T) = (T − 260)/R. With 90-digit arithmetic, each 75-significant-digit reference fell inside its reported interval, whose width was below 1e−10 in its corresponding SI unit.

| Quantity | Independent value, rounded |
|---|---:|
| Inner-face temperature | 282.010980593761 K |
| Outward shell rate | +99.972548515596 W |
| Inflow to phase bath | −15.989019406239 W |
| Inflow to maintained reservoir | −83.983529109358 W |
| Time to exhaust 0.1 kg liquid at 1000 J/kg | 6.254292240147 s |

The signed rates close. The requested 80 s horizon produced an exhausted plateau and exactly zero remaining liquid. The implementation uses the inner surface in the terminal response and intersects the phase-port bounds with the balance of shell flow and the other reservoirs. The extracted legacy plateau functions retain the existing sign, inventory and time rules. Five focused legacy and radial tests passed.

## Replay, controls and scope

GitHub reported success for [job 136866906477](https://github.com/physicsvigilante/sim_heat/actions/runs/44911105484/job/136866906477). I hashed the downloaded [archive](https://github.com/physicsvigilante/sim_heat/actions/runs/44911105484/artifacts/14709553114) to `1d5f242f3a343e8f625d033fa50e058b8583208fe427d81eb4772fda5a4fc9a0`. Running the workflow's phase command on the pinned clean worktree reproduced the archived JSON bytes after Windows newline normalization, SHA-256 `c80f4eabf27baed458bb4c0bf0e281fb8ad069e8a99e9fecf0aabbc3f2a19db3`. The worked case melted at approximately 26.598137640666 W and retained both phases over 120 s. I hashed the three actual study, model and facts files and matched all three result identities. The four native, certification and runner flags were false.

I observed refusals for negative duration, zero solid inventory, coincident ports, decreasing layer radius and a mismatched facts hash. Two initial mis-indexed control arguments separately exercised negative liquid mass and a malformed inner radius. An initial shell invocation lost its per-command temporary source directory and imported no candidate code. The clean exact-head rerun above supplied all executed review evidence.

This review covers constant conditions, steady storage-free conduction and the coexisting-phase interval up to exhaustion. Native execution, experimental validation and post-exhaustion dynamics are outside the claim. Source merge remains an owner decision.
