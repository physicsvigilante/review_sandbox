# SIM_HEAT PR #82 · R2 offline conduction reference

Review the general H1 offline conduction calculation and its post-freeze TwinBridge evidence. Decide whether the source, numerical bounds and independently expressed analytical checks support the claims for the admitted domain and the held-out exercise. Record any broader qualification or evidence requirements still open.

| Identity | Pin |
| --- | --- |
| [Draft PR #82](https://github.com/physicsvigilante/sim_heat/pull/82) base (PR #80 head) | `6904ec8219be0ddb8ec1635a9d000ddda80307c9` |
| [Source head](https://github.com/physicsvigilante/sim_heat/commit/7ee5bffb5a251ee75c4dab6ac54aaffccdc59d10) / tree | `7ee5bffb5a251ee75c4dab6ac54aaffccdc59d10` / `cef23b38146c48ebb99674ce5615139ecd644a3f` |
| Frozen solver | `f05f6a8fbdfd5ac177a5441d22b40dda6bf8e0d4` |
| Post-freeze case, givens and analytical oracle | `892e9e47e138b5ffd040e952d1ffa6598d2a052d` |
| Retained first output, oracle results and controls | `954cf65e1dffd04c706654418f30d891d1ccba57` |
| Hosted evidence | [Run 44851088533](https://github.com/physicsvigilante/sim_heat/actions/runs/44851088533) · [Job 136682348849](https://github.com/physicsvigilante/sim_heat/actions/runs/44851088533/job/136682348849) · [Artifact 14684359708](https://github.com/physicsvigilante/sim_heat/actions/runs/44851088533/artifacts/14684359708) |

GitHub reports archive size 316,924 bytes and SHA-256 `37818c0e3a3b7a2e9d3168e68df031224e6802a5c8db7c3cda54fbabe5f21a71`. Chat A verified run and artifact metadata. Inspect the actual archive, check the digest and source-head file, and distinguish your own replay from the hosted job and the original Windows attempt.

## Review questions

1. Verify the Git ancestry, freeze order, source and case identities. Inspect the [givens and equations](https://github.com/physicsvigilante/sim_heat/blob/7ee5bffb5a251ee75c4dab6ac54aaffccdc59d10/qualification/h1_n13/heldout/GIVENS.md), authored model, study and separate facts. Check the port orientations, units, heat-flow reversal and energy accounting.
2. Inspect the new assembly, steady/transient calculation, exact input binding, matrix exponential bound, static rounding and per-output error checks. Probe representative edge cases and refusals independently; distinguish demonstrated coverage from the larger admitted grammar.
3. Reproduce the [held-out replay](https://github.com/physicsvigilante/sim_heat/blob/7ee5bffb5a251ee75c4dab6ac54aaffccdc59d10/qualification/h1_n13/heldout/REPLAY.md) at the exact head. Verify whether the workflow actually generated fresh output and checked the 34 exports, four requests and three integrals at all 1,201 samples. Examine signed power, integrated energy, the oracle's independence, and the seven negative controls. Report any missing or unexercised checks.
4. Use offline source mathematics only. Native OpenModelica execution, radiation, teaching effectiveness and adoption as a production reference are outside the claim. The historical seven reference failures and eight native-readiness holds remain open. State limits on any R2 verdict explicitly.

Publish your own report at `projects/sim_heat/pr-82/reviews/review-01-chat-b.md` in the central hub. Preserve original source and evidence. Leave PR #82 draft and unmerged.
