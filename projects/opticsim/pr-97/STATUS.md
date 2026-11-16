## Independent Chat B R2 verdict — 2026-11-16

**PASS — BOUNDED NUMERICAL RESEARCH/EVIDENCE ONLY** at original unchanged PR #97 head `760473cafceb70c055bb7c13b138a16c5e4d7620`. [Original separate Chat B review](reviews/review-01-chat-b.md), committed in the review hub. Reviewer independently downloaded/rehashed original PR #96 source ZIP and both PR #97 ZIPs plus each member; checked exact protocol freeze, 48/48 scheduled slots for *each* run, **96/96 actual native fingerprints**, original failed CI audit and source-head **12/12 workflows**. Independently implemented a distinct integer/dyadic exact geometry check on **44/44 TAP callback samples** (8 distinct patterns: **12 represented nonforward from two patterns**, **24 point-agreement UNKNOWN**, **8 near-vertex UNKNOWN**); a separate JS replay reproduced **44/44 pinned-native binary64 incident points and rounded gates**. The **32 callbacks from 8 failed native TAP trials remain unqualified**.

**The 21/48 switched native statuses** across two executions with identical original physical inputs and schedule were independently verified at original ordinals `1,3,5,8,9,10,11,12,16,21,26,30,31,35,36,38,40,41,45,46,48`. Distinct total outcomes: first **26 completed/22 failed**, second **25/23**, neither changed or repaired. Evidence does **not** establish a causal effect of observer overhead.

**New finding R-01 (IMPORTANT): native RNG remained uncontrolled**. Original seed `0x9700A55` randomized trial *order* only; Opticsim production adapter does not set native `randomSeed`. Pinned PhyDemo Scene.js defaults null and seeds from system time on scene load; pinned Glass.getIncidentData consumes `scene.rng()` for a perturbed inside/outside helper ray. Thus equivalent saved scenes/schedules are **not equivalent controlled native RNG streams**. This is a blocker for any stronger stability/observer-mechanism conclusion, **not a blocker to the bounded research PASS** or exact represented-line arithmetic for observed coordinates. Possible RNG contribution has not been established experimentally. Keep the finding and source refs in all later reports.

**Scoped next test (new preregistration only, NOT native repair):** choose one original nominal-critical case, run **6 balanced four-mode blocks = 24 fresh processes** with one fixed, separately recorded **test-only native randomSeed**, leaving all physical source bytes unchanged. Distinguish native compiled/config hash from original physical scene hash. Preserve both PR97 original ZIPs and all failed runs. Independent Chat B review of any new numerical study needed before stronger inferences.

**RELEASE HOLD:** PR #97 remains **DRAFT/UNMERGED**, including disposable CI. No PhyDemo patch, numerical cutoff/tolerance, Stage-1 accepted output change, Stage-2 mandatory withholding, source/schema migration, image claim or deployment approved. [Developer disposition](responses/response-01-chat-a.md) is not independent review.

---

# Opticsim PR #97 — preregistered repeat critical native profile controls

**CURRENT: RESEARCH EXECUTED, ALL 12/12 SOURCE-HEAD WORKFLOWS PASSED, test-only exact-reference replay PASSED at exact draft HEAD `760473cafceb70c055bb7c13b138a16c5e4d7620`. Independent Chat B R2 numerical RESEARCH review PASSED for bounded evidence only. PR97 DRAFT/UNMERGED. No production physics or policy change.**

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

## Original-byte preservation and cross-run verification — Chat A, 2026-11-16

**NOT an independent Chat B verdict.** I downloaded the original three GitHub Actions ZIPs through the connected GitHub account, independently checked ZIP/member SHA256s in a separate local container, then uploaded their **byte-identical ZIPs** to owner-accessible persistent ChatGPT Pages. These private archives are accessible to this owner but not necessarily to external reviewers:

- [Original PR #96 native ZIP — private Page](https://chatgpt.com/space/page_7e4356b6dea48191a5e1d40804ceb9ad): original artifact **14229080814**, 12,217 B, SHA256 `467b548edbcdfc8cf4aecdab416d134d3ac703572a4e0330a4379fcb28df9929`.
- [First PR #97 failed-audit ZIP — private Page](https://chatgpt.com/space/page_cd73b2d1f7188191b835f9585f9832a3): original artifact **14229538642**, 21,080 B, SHA256 `d4929a2d837a6f2d42df17be150145e37bfe312297eea41f36713de7022071c3`.
- [Corrected PR #97 completed-audit ZIP — private Page](https://chatgpt.com/space/page_520115fa6b048191ac4e17f165961cef): original artifact **14230677949**, 23,246 B, SHA256 `a6bae60306f4a0730f4cae021b86a46b534d65736de2cb381f24c507d3eaa22e`.

Independent local per-member SHA256s:
| Original member | SHA256 |
| --- | --- |
| PR96 source `inputs.json` (also byte-identical in both PR97 original and copied inputs) | `caa07af040d0a71b50ea6b69470aa55a545b04d52195994913123a902b434df3` |
| PR96 source `report.json` | `9324aabab62a2ab0e3636c30dec2154e590daf7c90304e8aeafa564e41250698` |
| PR96 source `exact-reference.json` | `497d2e568ca851dd98941be38ccd54b7473953b56405b653771f784633808f12` |
| First PR97 original `report.json` (48 trials; Python audit subsequently failed) | `9fd6e67bc28a6c3a463ee0eb75f2c68e12bc923a54d3c05c350504c19b4a93af` |
| Corrected PR97 original `report.json` (48 new trials) | `7826d3983853e769cf42375fdb58f3623f93265c51ab71be89985651e27253a3` |
| Corrected PR97 new `exact-reference.json` | `4bfcd144c10baa2c6d1bbfeabea372a15869b3bfef79713fdb76295882bc3142` |

The two PR97 reports independently compared on original `ordinal`, `caseId`, `mode`, `sceneSha256` show **the same 48/48 scheduled positions** and identical source case hashes and schedule, but **21/48 individual native status transitions** between `completed` and `failed`. The switched source ordinals are **1, 3, 5, 8, 9, 10, 11, 12, 16, 21, 26, 30, 31, 35, 36, 38, 40, 41, 45, 46, 48**. Aggregate first-run **26/22** versus corrected second-run **25/23** obscures this much larger per-slot difference; report both rather than interpreting nearly unchanged totals as stability. These are distinct process executions, so a repeated slot is not a shared native event or a causal observer counterfactual. All first-run failures and original ZIP bytes remain untouched.

**Research/production HOLD:** independent R2 Chat B review of PR97 original evidence is still pending; no physics, geometry thresholds, measurement or Stage-2 change follows from this evidence.

---

## Scientific boundaries and release hold

At nominal critical incidence on synthetic Glass, actual native results change with repeated same-scene fresh process trials. Two profiles with identical extra scalar-copy/array-push hot paths still differ across executions. That is *repeatability/conditioning sensitivity*, not a controlled causal quantification of observer effects. The original six-case PR96 study had 17 distinct binary64 TAP hit signatures and two distinct represented nonforward signatures; this newly restricted two-case sample has 8 distinct signatures and more repeats. Neither provides a safe native-reported-point error envelope, a real-world exact-critical ray branch or proof of physical optical correctness across broad systems.

**DO NOT MERGE PR #97 OR ITS DISPOSABLE CI**, patch PhyDemo, alter native cutoff, adopt a tolerance, change Stage-1 canonical outputs, source scene schema or introduce mandatory Stage-2 withholding. Original PRs #92–#96 and their frozen artifacts/reviews remain unchanged. Separate Chat B R2 evidence review PASSED bounded research only; see the verdict at the top. No physics/policy change is authorized. Stronger numerical/physics or production policy needs separately approved R2 implementation and physical release controls.
