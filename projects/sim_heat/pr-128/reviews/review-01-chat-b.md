# PR 128 independent Chat B review

**Verdict: accept for the scoped offline reservoir-energy ledger.** No blocking findings. Reviewed as the owner-selected fresh Codex reviewer against source head `3ece211710e6c10552b678ce2c7d04d61d123c3c`, base `68e272d841db22841642202fc1ae804f4ce50910`, and [pinned request](https://github.com/physicsvigilante/review_sandbox/blob/41254fca27e684a6db7176283f60822039be7bf3/projects/sim_heat/pr-128/REQUEST.md).

## Independent physics and regression checks

I used the six-rod joined_terminals network, with coolL as the 300 K bath, warmL as the radiating surface, middleR at 330 K and coolR at 280 K. I independently solved the two interior nodal balances and the fourth-power face equation at 125 decimal digits. For face temperature F, centre C and contact J, the balances were 10C − 3J = 2F + 1500 and 4.6J − 3C = 478. The face residual was 2(F − C) + 0.00000004536(F⁴ − E⁴) for enclosure temperature E. I evaluated each support's incident rod flows directly. Every stage's reported enclosure and support interval contained its signed reference integral, including recovery. The stage reference energies summed to zero within 1e-100 J.

| Schedule | Bath (J) | Enclosures (J) | middleR (J) | coolR (J) |
|---|---:|---:|---:|---:|
| 520 K for 13 s, then 250 K for 8 s | 2997.287587 | −3650.199779 | −1723.907928 | 2376.820120 |
| Same schedule, then recovery at 210 K for about 44.679423159 s | 0 | −85.668813 | −6125.320116 | 6210.988929 |

All cumulative bounds enclosed the unrounded references. The fully recovered bath interval was exactly [0, 0] J. Base and head returned identical complete untracked objects for both schedules. All four offline provenance/capability flags were false.

With each phase initially 1 kg and latent heat 200000 J/kg, 520 K for 10000 s exhausted the solid after approximately 778.3989513368164 s. Only that duration contributed energy, and the subsequent 250 K stage was absent. A requested 520 K duration of 778.398951336816365782 s fell inside the computed event-time interval and produced exhaustion_time_uncertain. The returned energy bounds enclosed the independently integrated result at the earlier of the true depletion time and the requested end. The subsequent stage was omitted and a recovery request raised the coexistence refusal. Source inspection confirmed four-corner interval multiplication for signed rates and uncertain durations. Summing coordinate bounds may widen the ledger because rates and stopping times are correlated.

## CI and archived evidence

I verified successful job conclusions, run/archived head identities, archive CRCs, and SHA-256 over the downloaded ZIP bytes.

- [Series job](https://github.com/physicsvigilante/sim_heat/actions/runs/44872236684/job/136749111382) and [five-file archive](https://github.com/physicsvigilante/sim_heat/actions/runs/44872236684/artifacts/14694441589). SHA-256 `fe5b129ae8042efeb1fbd3c2a91371070269b4eb5c16202edb00644e69d38551`. A local replay of the star recovery case matched the complete archived ledger JSON.
- [TwinBridge job](https://github.com/physicsvigilante/sim_heat/actions/runs/44872236693/job/136749111142) and [four-file archive](https://github.com/physicsvigilante/sim_heat/actions/runs/44872236693/artifacts/14694203090). SHA-256 `00d82250074c94039f0e6891c7a77bc98926b070f0297880824552ea96ef7f23`. The archived source-head file contained the reviewed head. Decompressed fresh output, oracle results and control results matched the pinned held-out records as JSON.

Seven focused repository tests passed locally in addition to my independent checks. This review covers offline analytical output through the modeled plateau and recovery. Native execution, source merge, and promotion of qualification were outside scope.
