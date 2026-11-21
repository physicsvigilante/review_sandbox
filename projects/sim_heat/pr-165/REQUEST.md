# R2 independent review of source-preview identity

Review draft [SIM_HEAT #165](https://github.com/physicsvigilante/sim_heat/pull/165) at `6ebfc50574a61a49b7e4f645ab82f727af127b30` against #164 `fe6ed43691391a7413c473fca44707155dc61695`. Assess the normal admission-to-preview path, post-admission mutation, identity of the actual source buffers displayed, authentic unchanged studies and revisions, and stale-file behavior. Preserve the native hold and all historical provenance pins.

[Offline CI run 44905571443](https://github.com/physicsvigilante/sim_heat/actions/runs/44905571443) ran the full matrix and retained logs from both trees. Both jobs are **red**. Investigate whether the two N1 qualification errors (the frozen AGENTS.md digest) are the same on both revisions and whether any new failure or unrelated drift is present. Keep the gate status explicit in the verdict.

- [offline-base-6ebfc50574a61a49b7e4f645ab82f727af127b30](https://github.com/physicsvigilante/sim_heat/actions/runs/44905571443/artifacts/14707563519) with sha256:8267d1d89d29fa420160519a85f0afac7c5bc83f6cd128217cdca74a71639d10.
- [offline-head-6ebfc50574a61a49b7e4f645ab82f727af127b30](https://github.com/physicsvigilante/sim_heat/actions/runs/44905571443/artifacts/14706864587) with sha256:b2d9f952c831417503ccb23d65b0ecd00053ae3045a2db6ce104d81162bd8209.

The Windows baseline ran 477 Python tests, then 478 with the new regression. Both have the same Python failure/error identities, several setup refusals and three Node failures out of 42 tests. The local pinned interpreter has no Playwright. Linux CI ran the browser scripts. Local logs are in C:/Users/samee/AppData/Local/Temp/simheat-164-provenance-evidence. The regression on #164 displayed 987 kg for the 1 kg D1 body. Confirm the evidence independently.
