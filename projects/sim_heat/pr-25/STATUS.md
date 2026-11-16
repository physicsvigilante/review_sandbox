# SIM_HEAT H3-07 PR #25 — independent R2 status

**Status: `awaiting-independent-review`.** The targeted source correction, exact-head CI and reviewer handoff are complete. **No Chat B independent result or merge is claimed.** Standing owner authorization applies only after R2 PASS.

| Field | Pinned result |
| --- | --- |
| Source PR | [SIM_HEAT draft PR #25](https://github.com/physicsvigilante/sim_heat/pull/25) — **open/unmerged** |
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
| Independent reviewer verdict | **Not yet submitted** — Chat B alone writes `reviews/review-01-chat-b.md` |
| Merge | **Not authorized until independent scoped R2 PASS and CI at unchanged reviewed head** |

## Trust and historical boundaries

The current public original D2 → D2-K2 physical pair still uses externally identified genuine prior GitHub source runs and the same original saved K/J/W values. The new test-only second comparison selector is a **synthetic label on the same approved pair with an intentionally wrong commit**, not a new Modelica output or added teacher sample. H1 physics, native evidence, numerical policies, and earlier Review #23 PASS remain unchanged.

A newly self-repinned fake source manifest and matching case data can still pass internal metadata consistency by design; **external independent GitHub run/commit/artifact/full-original-ZIP checks** are mandatory for any new adopted native source. The new F-01 check prevents one internally inconsistent same-run SHA assertion; F-02 removes stale hidden DOM observations and preserves same-page recovery. Neither is a new native scientific qualification or classroom efficacy claim.

## Handoff

Read [REQUEST.md](REQUEST.md), [REVIEWER-PROMPT-01.md](REVIEWER-PROMPT-01.md), the central [REVIEW-TEMPLATE.md](../../../REVIEW-TEMPLATE.md), [PROTOCOL.md](../../../PROTOCOL.md), and [REVIEW-RISK-POLICY.md](../../../REVIEW-RISK-POLICY.md).

**Next:** Chat B reviews exact HEAD `d5be85cb4c0b3bc079a12bb5ccea0a7c143ebf9c` and writes a **new independent** report at `reviews/review-01-chat-b.md` directly to this central repository. The owner may return and say **“review done”**. Chat A will fetch that exact independent report, fix any demonstrated defects and ask for targeted re-review only if needed; standing owner authorization permits merging only a scoped review-passed unchanged HEAD, followed by main/postmerge CI verification. **PR #25 remains draft and unmerged.**
