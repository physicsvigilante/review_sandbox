# PR #82 · Targeted R2 review of reported error ratios

[Original review](reviews/review-01-chat-b.md) gave a scoped offline pass and demonstrated that setting the maximum ratio for `requests.lowerFlow` to zero left the old analytical verifier's result unchanged. Review the [three-file correction](https://github.com/physicsvigilante/sim_heat/compare/7ee5bffb5a251ee75c4dab6ac54aaffccdc59d10...b96e18a1a988bc323d7bae0eb274a52f4209d4af), its regression and the normal CI replay entry point.

| Identity | Pin |
| --- | --- |
| Draft source PR and stacked base | [#82](https://github.com/physicsvigilante/sim_heat/pull/82) · `6904ec8219be0ddb8ec1635a9d000ddda80307c9` |
| Correction parent | `7ee5bffb5a251ee75c4dab6ac54aaffccdc59d10` |
| Corrected head / tree | `b96e18a1a988bc323d7bae0eb274a52f4209d4af` / `2ae656dc8fee699d944e4ec4e7e791f749654a9c` |
| Exact-head Windows-independent offline replay on Ubuntu | [Run](https://github.com/physicsvigilante/sim_heat/actions/runs/44852412541) · [Job](https://github.com/physicsvigilante/sim_heat/actions/runs/44852412541/job/136686613980) · [Artifact 14686335831](https://github.com/physicsvigilante/sim_heat/actions/runs/44852412541/artifacts/14686335831) |

GitHub reports ZIP SHA-256 `daf1531f4a3bf890fe3f6468a886f0378f05d10e006cc1907782837ebe1b275a`, 316,924 bytes. Check the archive, source head and fresh replay independently.

Assess how each reported maximum is converted to an allowed discrepancy using its own series budget, binary64 sample, analytical reference and uncertainty. Reproduce the old counterexample and probe zero, nonzero understatement, unchanged authentic data and relevant edge cases. Determine which understatements can be detected by this comparison. Check that the regression fails for the intended reason, that CI ran it and applied the successor to fresh output, and that the original solver, oracle, first attempt and controls retain their identities. Identify any new evidence or numerical issue separately from inherited limits. No native execution or source merge is authorized.

Publish a new `projects/sim_heat/pr-82/reviews/review-02-chat-b.md` with your verdict, commands and limits. Keep review-01 intact.
