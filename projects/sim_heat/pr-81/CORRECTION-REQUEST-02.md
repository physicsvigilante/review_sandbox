# PR #81 · Targeted R2 re-review of F-01

Determine whether [the F-01 correction](https://github.com/physicsvigilante/sim_heat/compare/538fbb097f81d3c66b458fa7cf99bd35a9ed7aac...dcd6ab3b3e383e4262d9798d62b846deb9346274) resolves the mixed Windows root spelling finding and preserves the study loader's original containment and refusal behavior. [Original independent report](reviews/review-01-chat-b.md) · [Chat A response](responses/response-01-chat-a.md)

| Source | Pin |
| --- | --- |
| [Draft PR #81](https://github.com/physicsvigilante/sim_heat/pull/81) base | `6904ec8219be0ddb8ec1635a9d000ddda80307c9` |
| Previously reviewed head and correction parent | `538fbb097f81d3c66b458fa7cf99bd35a9ed7aac` |
| [Corrected head](https://github.com/physicsvigilante/sim_heat/commit/dcd6ab3b3e383e4262d9798d62b846deb9346274) | `dcd6ab3b3e383e4262d9798d62b846deb9346274` |
| Corrected tree | `a5dfa438f59e65804783b8e41626ca7541a9c487` |
| Exact-head Windows CI | [Workflow run 44848972080](https://github.com/physicsvigilante/sim_heat/actions/runs/44848972080) |

Independently exercise the four combinations of long and short paths for both the nested study and the case root. Verify that the aliases are distinct and refer to the same file or directory. On this machine the worktree's Documents ancestor had a real 8.3 alias, while newly created temporary directories did not necessarily have one. Exercise recursive parent revision admission and compare file and descriptor identity. Inspect the fallback's original-component checks, resolved containment and authored model/parent path refusals. Probe relevant failure paths. Distinguish actual Windows behavior from synthetic equivalents and distinguish CI from personal checks.

Inspect the changed loader pin and unchanged historical N1 manifest. The check run is scoped to offline behavior. The separate earlier full-suite records and native-readiness holds retain their scope. Keep review-01 intact. Publish your verdict, evidence and limitations in a new `projects/sim_heat/pr-81/reviews/review-02-chat-b.md`. Use offline tests only and leave the source PRs unmerged.
