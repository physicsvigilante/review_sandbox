# SIM_HEAT H3-07 PR #25 — independent R2 status

**Status: `merged` — independent scoped R2 PASS and post-merge verification complete.** [Chat B Review 01](reviews/review-01-chat-b.md) is independently authored (Git blob `94e41c785c4e63a4c46d4cecb0ee33c7f90c5d9d`), **scoped PASS**, exact reviewed head `d5be85cb4c0b3bc079a12bb5ccea0a7c143ebf9c`. GitHub merged the unchanged reviewed source as `3287fafc8f1f3cb84b84a4db1c28f032f460e6ca` under standing owner authorization. **Post-merge CI 3/3 successful on this exact main SHA.**

| Field | Pinned result |
| --- | --- |
| Source PR | [SIM_HEAT PR #25](https://github.com/physicsvigilante/sim_heat/pull/25) — **closed/merged** |
| Base SHA | `8aa18488f949c6d1b506d80e44afc2a25e71b2c7` |
| **Exact reviewed source HEAD** | **`d5be85cb4c0b3bc079a12bb5ccea0a7c143ebf9c`** |
| Source tree | `05fa0292e0ad049dd7c3bcee242087ea71459425` |
| Risk class | **R2**, native source-pair provenance and same-page refusal semantics |
| Review origin | [PR #23 independent Review 01](../pr-23/reviews/review-01-chat-b.md) — **scoped PASS**, two **nonblocking** future safeguards F-01 and F-02 |
| Work tracking | [SIM_HEAT Issue #24](https://github.com/physicsvigilante/sim_heat/issues/24) |
| F-01 | Same original run ID means same `compiledSourceCommit` for both original native selectors; distinct case slots/artifacts from that run remain allowed |
| F-02 | Same-page valid → refused → valid now purges hidden native value/source-label DOM and resets controls while preserving selector recovery |
| Original source | Existing original D2 [run 43691263273](https://github.com/physicsvigilante/sim_heat/actions/runs/43691263273) and D2-K2 [run 43693191224](https://github.com/physicsvigilante/sim_heat/actions/runs/43693191224), independently checked previously |
| Preserved | Exactly **8 changed paths**; no H1 law/Modelica/checker/runner, original native archives, six published source-case JSONs, original v2 pair index or source manifest, H1-C1 frozen files |
| Exact-HEAD source CI | [43876894794](https://github.com/physicsvigilante/sim_heat/actions/runs/43876894794) — **completed/SUCCESS** on exact source |
| CI regression counts | **151/151 H1**, **4/4 analytical**, **33 Python discovered = 32 passed + 1 original-archive optional test skipped**, **24/24 Node**, real Chromium desktop/mobile PASS |
| CI artifact | [14230601766](https://github.com/physicsvigilante/sim_heat/actions/runs/43876894794/artifacts/14230601766), **5,880,269 bytes**, ZIP SHA-256 **`2f9e5e110c90304e2577a6e10f057c261d216a29be42600fbe00f0a15658c40a`** |
| Author artifact audit | Original ZIP separately downloaded, full SHA-256 and CRC verified (33 members), head marker equals exact source; real refusal/recovery screenshots inspected |
| New OpenModelica execution | **None** — no new builds/launches/version queries |
| Native output trust | Existing historical `diagnostic_only` / `nativeQualified=false`; internal self-pinned source metadata is not external GitHub attestation |
| Independent reviewer verdict | **SCOPED R2 PASS** — [Chat B Review 01](reviews/review-01-chat-b.md), exact original report Git blob `94e41c785c4e63a4c46d4cecb0ee33c7f90c5d9d` |
| Owner authorization | Standing authorization to merge a genuinely R2-passed exact-head candidate after CI; no separate routine approval required |
| Actual merge | [`3287fafc8f1f3cb84b84a4db1c28f032f460e6ca`](https://github.com/physicsvigilante/sim_heat/commit/3287fafc8f1f3cb84b84a4db1c28f032f460e6ca), GitHub merged=true, PR closed, 2026-11-16 14:08:08 UTC |
| Main identity | Verified identical to merge SHA; compare 0 ahead / 0 behind |
| Postmerge CI | **3/3 completed/success at exact merge SHA:** [H1 offline 43882591811](https://github.com/physicsvigilante/sim_heat/actions/runs/43882591811), [thermal viewer 43882591680](https://github.com/physicsvigilante/sim_heat/actions/runs/43882591680), [generic viewer 43882591877](https://github.com/physicsvigilante/sim_heat/actions/runs/43882591877) |

## Trust and historical boundaries

The current public original D2 → D2-K2 physical pair still uses externally identified genuine prior GitHub source runs and the same original saved K/J/W values. The new test-only second comparison selector is a **synthetic label on the same approved pair with an intentionally wrong commit**, not a new Modelica output or added teacher sample. H1 physics, native evidence, numerical policies, and earlier Review #23 PASS remain unchanged.

A newly self-repinned fake source manifest and matching case data can still pass internal metadata consistency by design; **external independent GitHub run/commit/artifact/full-original-ZIP checks** are mandatory for any new adopted native source. The new F-01 check prevents one internally inconsistent same-run SHA assertion; F-02 removes stale hidden DOM observations and preserves same-page recovery. Neither is a new native scientific qualification or classroom efficacy claim.

## Independent review, owner authorization and completed merge

- [Original independent review request](REQUEST.md) and [ready-to-paste prompt](REVIEWER-PROMPT-01.md) remain source-pinned historical documents.
- [Chat B Review 01](reviews/review-01-chat-b.md) independently returned **scoped R2 PASS** at exactly `d5be85cb4c0b3bc079a12bb5ccea0a7c143ebf9c`, tree `05fa0292e0ad049dd7c3bcee242087ea71459425`. The reviewer independently SHA/CRC-checked original D2, D2-K2 and exact-head CI artifacts; performed 11/11 targeted production JS admissions/refusals, checked historical raw sample/power/energy preservation, and ran a reviewer-owned isolated same-page DOM test. Original Chromium was **author-CI only**, not independently run by Chat B, because its review environment blocked browser navigation. The distinction remains explicit.
- Prior PR #23 nonblocking **F-01 and F-02 are resolved** in this scoped correction: same-run cross-artifact execution SHA consistency and real same-page refusal/recovery with hidden numeric/source-label DOM removal. No other blocker/major/minor production defect demonstrated; F-03 is an intentional ongoing **external GitHub native provenance boundary**, not a bypass or a qualification upgrade.
- Owner's standing authorization covers merges **after** required scoped R2 PASS. Verified exact PR reviewed-head and source [CI 43876894794](https://github.com/physicsvigilante/sim_heat/actions/runs/43876894794) `completed/success`, matching main base, then marked the draft PR ready and requested an expected-head guarded GitHub merge. GitHub confirmed **merged=true**, PR closed, merge SHA `3287fafc8f1f3cb84b84a4db1c28f032f460e6ca` at 2026-11-16 14:08:08 UTC. The `main` branch and this merge SHA are identical (0 ahead/behind).
- **Post-merge verification complete: 3/3 `main` workflows SUCCESS** at exactly `3287fafc8f1f3cb84b84a4db1c28f032f460e6ca`: [H1 offline 43882591811](https://github.com/physicsvigilante/sim_heat/actions/runs/43882591811), [thermal explorer 43882591680](https://github.com/physicsvigilante/sim_heat/actions/runs/43882591680), [generic thermal network viewer 43882591877](https://github.com/physicsvigilante/sim_heat/actions/runs/43882591877). No new OpenModelica build/launch is claimed.
- Original H1 law, numerical policy, historical failure/qualification evidence, six native case JSON bundles, H1-C1 frozen assets and the original v2 source-pair manifest/index remain unchanged. All source-linked numeric observations remain historical `diagnostic_only` and `nativeQualified=false`; internally self-consistent case metadata **does not attest** a new native GitHub run, scientific accuracy, physical measurement or classroom outcomes.

**PR #25 merged, independently reviewed and post-merge verified.** Next work, if undertaken, must preserve this history, derive any new native evidence from a separately checked original GitHub source/run/archive, and obtain new R2 review whenever source admission/evidence semantics materially change. No further review round for this exact source correction is required.
