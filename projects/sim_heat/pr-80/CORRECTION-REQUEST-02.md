# PR #80 · Targeted R2 re-review of F-01

**Decision requested.** Determine whether the corrected N12 staging boundary supports the verified source-origin claim for the primary, tight and dense offline candidates. The original reviewer requested changes on F-01. [Original report](reviews/review-01-chat-b.md) · [Chat A reproduction and correction](responses/response-01-chat-a.md)

| Source identity | Pin |
| --- | --- |
| Draft source PR | [SIM_HEAT #80](https://github.com/physicsvigilante/sim_heat/pull/80) |
| Stacked PR base | `ca5654a789f2291d6f0ceb7fd798b15d4310a122` |
| Previously reviewed head and correction parent | `aef1efe599cae31f6ee4b114b1a3051325732bfb` |
| Corrected head | [6904ec8219be0ddb8ec1635a9d000ddda80307c9](https://github.com/physicsvigilante/sim_heat/commit/6904ec8219be0ddb8ec1635a9d000ddda80307c9) |
| Corrected tree | `c2b08eabdcb301d3ee8e2be36075e916a606ce7e` |
| PR checkout | `390442b7b7802f914eb098051bac2756a0ee3068` |

The correction changes only the N12 staging module and its tests. Review the [two-file correction](https://github.com/physicsvigilante/sim_heat/compare/aef1efe599cae31f6ee4b114b1a3051325732bfb...6904ec8219be0ddb8ec1635a9d000ddda80307c9). The accepted N11 mathematics is outside this re-review unless the correction introduces a concrete dependency on it.

## Checks for the reviewer

1. Independently reproduce the original F-01 control and challenge the corrected entry points. Check whether authentic trace bytes can be paired with a divergent signed series, units, requests or integrals, or a caller-selected proof and digest, to produce the verified origin.
2. Trace the positive path from a freshly executed pinned N11 audit and N9-checked N1 bytes through packet serialization. Check both grid identities, the exact role/study/model/provenance binding and H1 admission with each case directory as its root.
3. Probe missing grids, role substitution, altered sources before the first output write, and any native or runner authority claims. Compare the legitimate candidate identities to the original reviewed evidence and inspect the two hosted scratch preparations.
4. Give a scoped verdict, with exact commands or evidence pointers, distinguishing personally executed probes from hosted results and recording limitations. Keep the seven legacy reference failures and eight native-readiness blockers in scope as preserved holds. Use offline checks only.

## Current-head hosted evidence

[PR workflow](https://github.com/physicsvigilante/sim_heat/actions/runs/44840798964) · [Offline staging job](https://github.com/physicsvigilante/sim_heat/actions/runs/44840798964/job/136648376377) · [Evidence archive 14681270960](https://github.com/physicsvigilante/sim_heat/actions/runs/44840798964/artifacts/14681270960)

GitHub reports success for this exact head, including the regression suites, preserved holds, and the ten-file comparison across two full preparations. GitHub reports an archive size of 12,575,876 bytes and SHA-256 `a7d7e3e5f89bce30269a8d27a76bbaeedb4e0333fa132f9df1c51cd35fbf1b13`. Chat A verified the artifact metadata. Independent archive rehashing is available to the reviewer.

Publish your own new report at `projects/sim_heat/pr-80/reviews/review-02-chat-b.md` in the review hub. Preserve review-01 and leave the source PR draft and unmerged.
