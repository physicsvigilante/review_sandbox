# Opticsim PR #97 — preregistered repeat critical native profile controls

**CURRENT: RESEARCH EXECUTED, ALL 12/12 SOURCE-HEAD WORKFLOWS PASSED, test-only exact-reference replay PASSED at exact draft HEAD `760473cafceb70c055bb7c13b138a16c5e4d7620`. Separate independent Chat B R2 numerical RESEARCH review PENDING. PR97 DRAFT/UNMERGED. No production physics or policy change.**

- Original production `main` `50dd0f4d9530d0a61bb4c7064c4326a8ac0ce518`, pinned native PhyDemo `811f508d2b070898c241a568b0c167dcb8645251`. New test-only source [draft PR #97](https://github.com/physicsvigilante/opticsim/pull/97). Protocol finalized at **`c32c2e1ffbe849a54416df2ce25775cc746ea39d` before any new native execution**, defining exactly 2 reused PR96 nominal-critical cases, 6 balanced randomized blocks each, seed `0x9700A55`, four disjoint profiles and **48 fresh-Node-process native trials**. Only 5 newly added research files (preregistration, JS runner, Python exact-reference, README, disposable workflow). **Zero production `src/`, PhyDemo, schema, native cutoff, measurement, Stage-2 or UI changes.**
- Original PR96 archival [source ZIP artifact 14229080814](https://github.com/physicsvigilante/opticsim/actions/runs/43872962563/artifacts/14229080814), original `inputs.json` **19,205 bytes / SHA-256 `caa07af040d0a71b50ea6b69470aa55a545b04d52195994913123a902b434df3`**. The PR97 workflow downloads original artifact using `actions:read` and source runner verifies those exact input bytes, freezes all 6 original source cases and chooses only `critical-shift-neg` and `critical-tilt-p14-shift` with saved document hashes matching. Original full inputs copied **byte-identically** into new output, not regenerated; no old research artifact or run rewritten.
- Four profiles per frozen block: **ordinary-off** (no optional Stage-1 diagnostic), **ordinary-on** (existing optional Stage-1 advisor), **tap-blackhole** (identical synchronous callback scalar copy/array push as archive, then discard after terminal), **tap-archive** (same callback work, preserve raw coordinates after terminal). TAP variants retain the single native-calling Glass owner and invoke original exactly once. **Hot-path-copy-work matched does NOT imply measured matched time, observer neutrality or causal counterfactual.**

## Preserve original two research runs with honest statuses

**First CI `9df7bea7d5b18ec63a0cc2f82c0c83d5163d6a3b` / [43877888781](https://github.com/physicsvigilante/opticsim/actions/runs/43877888781) FAILED at Python audit launch** (inherited old default input path). Its JS runner successfully executed **all 48 native processes** and kept the authentic [raw original inputs+report archive 14229538642](https://github.com/physicsvigilante/opticsim/actions/runs/43877888781/artifacts/14229538642), GitHub-reported ZIP digest `d4929a2d837a6f2d42df17be150145e37bfe312297eea41f36713de7022071c3`, 21,080 bytes. **Original actual native statuses (not Python-audited in this run)**: OFF **6 completed / 6 failed**, ON **5 / 7**, TAP-blackhole **8 / 4**, TAP-archive **7 / 5**, total **26 completed / 22 failed**; TAP-archive reported **41 actual callback samples**. The first failed CI and raw output are retained, not relabeled success.

**Second corrected audit-path-only commit `760473cafceb70c055bb7c13b138a16c5e4d7620` / [43878097648](https://github.com/physicsvigilante/opticsim/actions/runs/43878097648): research workflow SUCCESS**. Same unchanged original case bytes/schedule and runner source; only Python default input path corrected, no native logic changed. Actual **48 native processes**:

| Source case | Mode | Completed | Failed |
| --- | --- | ---: | ---: |
| critical-shift-neg | ordinary-off | 5 | 1 |
| critical-shift-neg | ordinary-on | 5 | 1 |
| critical-shift-neg | tap-blackhole | 3 | 3 |
| critical-shift-neg | tap-archive | 0 | 6 |
| critical-tilt-p14-shift | ordinary-off | 5 | 1 |
| critical-tilt-p14-shift | ordinary-on | 2 | 4 |
| critical-tilt-p14-shift | tap-blackhole | 1 | 5 |
| critical-tilt-p14-shift | tap-archive | 4 | 2 |
| **Combined OFF** | **12 runs** | **10** | **2** |
| **Combined ON** | **12 runs** | **7** | **5** |
| **Combined TAP-blackhole** | **12 runs** | **4** | **8** |
| **Combined TAP-archive** | **12 runs** | **4** | **8** |
| **Grand total** | **48 real native trials** | **25** | **23** |

The corrected run's **12 TAP-archive native processes captured 44 actual native callbacks**. Same-assistant Python Fraction audit matches all **44/44** original JS classifications, zero mismatches: **12 exact represented-line nonforward**, **24 point-agreement UNKNOWN**, **8 near-vertex UNKNOWN**. There are only **8 distinct full serialized-binary64 hit signatures**, not 44 independent configurations. **32 captured callbacks came from native-failed runs**, including failure-associated nonforward events; no failed trace becomes a qualified optical reading. Native run state changed across source-identical executions (first run 26/22, second 25/23) and distributions differ across per-case/profiles. This alone cannot establish instrumentation causality, observer neutrality, correct ideal real critical branch or error tolerance.
 
**Successful corrected research artifact** [14230677949](https://github.com/physicsvigilante/opticsim/actions/runs/43878097648/artifacts/14230677949), GitHub-reported ZIP SHA256 `a6bae60306f4a0730f4cae021b86a46b534d65736de2cb381f24c507d3eaa22e` (23,246 bytes), contains an exact original PR96 source inputs copy, `report.json`, `exact-reference.json`, and separate fetched original PR96 JSON members. The derived archive's GitHub Action-reported SHA is NOT yet independently rehashed by Chat B. Original output per-member digests and individual failed ordinals must be independently recomputed in review, not invented in this status.

**ALL 12/12 source-head GitHub Actions workflows now VERIFIED SUCCESS**, including 11 unchanged existing project checks and the one disposable research workflow. This only validates source-specific tests and research integrity, not native physical truth or observer neutrality.

## Scientific boundaries and release hold

At nominal critical incidence on synthetic Glass, actual native results change with repeated same-scene fresh process trials. Two profiles with identical extra scalar-copy/array-push hot paths still differ across executions. That is *repeatability/conditioning sensitivity*, not a controlled causal quantification of observer effects. The original six-case PR96 study had 17 distinct binary64 TAP hit signatures and two distinct represented nonforward signatures; this newly restricted two-case sample has 8 distinct signatures and more repeats. Neither provides a safe native-reported-point error envelope, a real-world exact-critical ray branch or proof of physical optical correctness across broad systems.

**DO NOT MERGE PR #97 OR ITS DISPOSABLE CI**, patch PhyDemo, alter native cutoff, adopt a tolerance, change Stage-1 canonical outputs, source scene schema or introduce mandatory Stage-2 withholding. Original PRs #92–#96 and their frozen artifacts/reviews remain unchanged. Require independent Chat B R2 research/evidence review of this exact source and original bytes. Stronger numerical/physics or production policy needs separately approved R2 implementation and physical release controls.
