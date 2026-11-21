# PR 131 independent R2 review

**Verdict — accept for the bounded offline investigation.** I found no blocking defect in the shared linear conductivity calculation or the terminal-response refactor. I reviewed as a fresh Codex Chat B using [the pinned request](https://github.com/physicsvigilante/review_sandbox/blob/c97fb9a3276b16653c98c3fee7748082a305b0e1/projects/sim_heat/pr-131/REQUEST.md) and [source base f3a14c1 through head b1dcf26](https://github.com/physicsvigilante/sim_heat/compare/f3a14c19f13f517cfb9a70dbe291a54bffa067d7...b1dcf26c279ea1ef713208ec34aef91bd30e43fb). The local clean worktree matched the full requested head.

## Material law and inversion

Integrating the linear factor gives the oriented rod power exactly as reference conductance times the endpoint temperature difference times the conductivity factor at their mean. Each steady junction therefore balances the common integrated potential with positive reference conductances. Its potential lies within the maintained extremes by the discrete maximum principle. Strict positivity at both extreme temperatures establishes monotonicity over the whole interval, including for negative slope. Clipping junction potential enclosures to that physical range preserves the solution. Each of the two bisections retains the root on the correct side using rational arithmetic and gives a temperature bracket of width at most the initial range divided by 2^96 for each single potential value. Zero slope and exact end potentials have direct inverses. The terminal supply is the negative of the incoming flux at the terminal. I also inspected the shared preparation extraction and reran all eight tests in the variable-conductivity, terminal-response and phase-branch-flow modules. All passed.

## Independent nonlinear bridge

I exercised the revised five-rod bridge, a different arrangement from the new tests. Reading the changed Modelica file gave conductances 4, 2, 1, 1 and 1 W/K for feed, drain, inlet, outlet and link. I solved the two physical junction balance equations directly with 110-decimal-digit arithmetic, using each edge's mean-temperature conductivity and reference temperature 280 K. At each slope I checked both junction enclosures, all five signed edge rates, and both opposite terminal supplies against the solver output. Maximum absolute junction residual was below 3e-109 W. Values below are rounded.

| Relative slope (1/K) | Upper (K) | Lower (K) | Upper to lower (W) | Hot supply (W) |
|---|---:|---:|---:|---:|
| 0.006 | 349.859113 | 340.514123 | 13 | 240.5 |
| -0.009999999999999999 | 320.839202 | 312.917961 | 5 | 92.5 |
| 0 | 345 | 335 | 10 | 185 |

I observed refusal at exactly zero hot-end conductivity and at negative cold-end conductivity. A zero reference temperature, NaN and a double minus were also refused. The accepted negative-slope case approaches the zero-conductivity endpoint from the admissible side.

## Archived replays

Both named jobs succeeded. I downloaded both ZIPs, checked every member's CRC and computed both archive hashes independently.

- The wall ZIP had SHA-256 `e95711b8923d5d252f61ddc53a60fc0cdc0102f2b11eb5ec5bf300f82570a59d`. Its complete variable-conductivity JSON matched a fresh calculation at this head. The facing, reversed insert and strip carried +300, −225 and +75 W. The two terminal supplies were +300 and −300 W. All four offline provenance flags were false. [Wall job](https://github.com/physicsvigilante/sim_heat/actions/runs/44873174793/job/136752011073)
- The TwinBridge ZIP had SHA-256 `afe2e338199daa9a68eacf5d508261c6caa6e040c7fb07c6259e58c6b7286fc5`. Its source-head member matched the full review head. I decompressed and compared the fresh output with the preserved first output, and compared both its oracle and its seven-control record with the pinned historical JSON. All three comparisons matched. [TwinBridge job](https://github.com/physicsvigilante/sim_heat/actions/runs/44873174803/job/136752011156)

This review covers storage-free steady networks whose rods share one relative linear slope. Native execution, native qualification and classroom outcomes fall outside the evidence examined. The source PR remains unmerged.
