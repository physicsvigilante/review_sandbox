# SIM_HEAT H3-04 PR #19 — central R2 review status

**Status: `merged` — independently reviewed, owner-authorized, post-merge verified.** Chat B's [Review 01](reviews/review-01-chat-b.md) independently gave **scoped R2 PASS** at the exact source head `e81b98c3a2ddd483e7ab9222c5d2b566cb599665` (review Git blob `09213f3af573c996c591e608fc61b4c26cc03c70`). Under the owner's standing authorization, GitHub merged the identical reviewed head as `8ca22cdeb84a6b4621865651f53b916f94c88c85` on 2026-11-16 12:11:10 UTC. **All three post-merge `main` workflows have completed successfully at exactly this merge SHA.**

| Field | Value / result |
| --- | --- |
| Project | `sim_heat` |
| Source PR | [#19](https://github.com/physicsvigilante/sim_heat/pull/19) — **closed, merged** |
| Base SHA | `ab45af5a33888850e8577f9c70b6f8d78c168cf1` (merged Ring4 main) |
| **Exact source HEAD** | **`e81b98c3a2ddd483e7ab9222c5d2b566cb599665`** |
| Source Git tree | `72af80e17fb8619b0663f1333a6075111e4073b6` |
| Risk class | **R2**, archived native multi-batch receipt and comparative evidence semantics |
| Original physical revision | Existing `H1_D2` → `H1_D2_K2`, hypothetical `rod.k` 100 → 200 W/(m K), unchanged parent model/study |
| Original successful native run | [43693191224](https://github.com/physicsvigilante/sim_heat/actions/runs/43693191224), `completed/success`, executed SHA `52b1635932a3e4519b91f3bf093c0c21b0248d91` |
| Native ZIP artifact | [14153251022](https://github.com/physicsvigilante/sim_heat/actions/runs/43693191224/artifacts/14153251022), 3,820,474 bytes, ZIP SHA-256 `dc32a0a36a27f031ce7a13da83ebdd26a3dd6ac1d14612fa597b36cb439f4843` |
| Original native batch | Batch 1, case 1; 88/88 archived file hashes verified from actual downloaded ZIP |
| D2-K2 MAT SHA-256 | `a4ebf82400d1e65c8b84992f57862650d7c3d132fba93cd1bfeeda2b040bebf9` |
| D2-K2 CSV SHA-256 | `f3fd607a4f8701f1736942db6547be7f477e6fcc0973ca4730835b64efc8c7e0` |
| Source-native case JSON | `viewer/network/data/D2_K2.json`, SHA-256 `a057e076aa31971c82509b70566892f9be60850046231104feac5d9e6365748b` |
| Original canonical analysis | 1,001 saved physical time instants, 0–9,375 s, 1,000 intervals; 21 unchanged saved preview points |
| Native checking status | 34 passing diagnostic checks, `diagnostic_checks_passed_not_native_qualified`, `nativeQualified=false`, public requests `diagnostic_only` |
| Exact-head source CI | [43858903289](https://github.com/physicsvigilante/sim_heat/actions/runs/43858903289), `completed/success`, exact source HEAD |
| CI tests | H1 151/151, analytic 4/4, Python adapter 20/20, JS 23/23, real Chromium desktop/mobile PASS |
| CI evidence artifact | [14222866556](https://github.com/physicsvigilante/sim_heat/actions/runs/43858903289/artifacts/14222866556), 5,238,535 bytes, whole ZIP SHA-256 `b7ad8ca2594677bc4080cf659c68669494e1db79f2ed9af796e159810b195a4d` |
| Chat B review | **SCOPED R2 PASS** — [Review 01](reviews/review-01-chat-b.md) at exact head `e81b98c3a2ddd483e7ab9222c5d2b566cb599665`, original report blob `09213f3af573c996c591e608fc61b4c26cc03c70` |
| Owner merge authorization | Standing owner instruction to merge after completed independent R2 PASS and exact CI |
| Merge SHA | [`8ca22cdeb84a6b4621865651f53b916f94c88c85`](https://github.com/physicsvigilante/sim_heat/commit/8ca22cdeb84a6b4621865651f53b916f94c88c85); GitHub `merged=true`, PR `closed`, merge timestamp 2026-11-16 12:11:10 UTC |
| Main identity | Verified identical to merge commit; 0 ahead / 0 behind |
| Post-merge CI | **PASS, 3/3 on exact merge SHA:** [H1 offline 43864268282](https://github.com/physicsvigilante/sim_heat/actions/runs/43864268282), [generic viewer 43864268328](https://github.com/physicsvigilante/sim_heat/actions/runs/43864268328), [thermal viewer 43864268319](https://github.com/physicsvigilante/sim_heat/actions/runs/43864268319) |
| Postmerge verification | **Complete — 3/3 `main` workflows SUCCESS** at merge SHA; no new OpenModelica launch |

## Preservation and trust limits

The first five original native viewer case JSONs, H1 Modelica laws, parser/study/revision checks, native runner, numerical thresholds, old native campaign batches and frozen H1-C1 source remain unchanged. The reviewed change adds one generic *offline* historical-campaign adapter, one source-linked D2-K2 JSON case and catalog entry, one read-only dedicated comparison page/logic, and offline/Chromium regression tests. It does **not** implement in-browser arbitrary Modelica, parameter sweeps or unrestricted reruns; chart strokes connect native saved points visually without extra computed observations. The original and successor native data stay `diagnostic_only`, `nativeQualified=false`; SHA-pinning and metadata matching do not independently attest arbitrary new archives.

Early H3-04 development failed/cancelled CI at different source SHAs remains part of the source history. No previous run status is relabeled. The final exact-head CI passed, and the original historical native campaign is an independent earlier run; **zero new OMC commands** for the new comparison page.

## Independent reviewer findings and release record

- [Original review request](REQUEST.md) and [Chat B Review 01](reviews/review-01-chat-b.md) remain their original files. Chat B independently downloaded and hashed original baseline D2, four-batch D2-K2 campaign and exact-head CI ZIPs; verified **592/592 native campaign file hashes**, original source parent/revision identity, native MAT/CSV channels, 1001 physical-time points, 34 diagnostics and source-exact 21-point previews.
- Reviewer independently calculated both two-body transient solutions and native energy balances. At like times the doubled-conductivity case exchanges heat faster and retains the same **asymptotic** 308.15 K equilibrium. No exact finite-time equilibrium or independent native qualification is claimed.
- Original Review 01 verdict **scoped PASS**, with three **nonblocking** limitations: (F-01) stronger fully rehashed *authentic-shaped synthetic* campaign mutation tests are desirable before generalizing archived native ingestion; (F-02) caller-supplied run/commit/ZIP hashes do **not** themselves authenticate arbitrary other GitHub executions; (F-03) dynamic multi-pair source/identity coupling would require fresh guard/test policies before expansion. No demonstrated production bug or new native run was claimed.
- The owner granted standing authorization for routine development and merge **after required independent R2 review**. Verified unchanged PR head, original exact-head [CI 43858903289](https://github.com/physicsvigilante/sim_heat/actions/runs/43858903289) SUCCESS and base main identity before using GitHub's expected-head merge guard. PR #19 was marked ready and merged as `8ca22cdeb84a6b4621865651f53b916f94c88c85`. Github PR closed/merged and main matches the merge commit.
- **Post-merge CI verified 3/3 PASS** on that exact commit: [H1 offline](https://github.com/physicsvigilante/sim_heat/actions/runs/43864268282), [generic viewer](https://github.com/physicsvigilante/sim_heat/actions/runs/43864268328), [thermal viewer](https://github.com/physicsvigilante/sim_heat/actions/runs/43864268319). Existing source-catalog bundles, H1 model/physics/numerical policy, historical native attempts and failed development CIs remain unchanged. None of these post-merge checks is a new OMC native experiment.

**PR #19 merged and its R2 cycle complete.** New case observations remain `diagnostic_only` / `nativeQualified=false`; demonstration is bounded to an already authored D2-K2 hypothetical rod conductivity revision. No arbitrary parameter sweep, general LLM-authoring proof, independent sensor/physical measurement or classroom evaluation is implied.

**Next independent development:** improve original-campaign adapter negative tests (F-01), and consider stronger source-pair coupling only with a separately scoped, tested R2 change. No repeat review of the unchanged PR #19 source is needed.
