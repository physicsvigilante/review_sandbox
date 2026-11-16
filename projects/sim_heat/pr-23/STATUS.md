# SIM_HEAT H3-06 PR #23 — independent R2 review status

**Status: awaiting independent R2 Chat B Review 01.** The exact source/CI and central review handoff are prepared. **No Chat B verdict, source merge, full native scientific qualification or owner-specific new exception is claimed.** Standing owner authorization covers review-passed routine merges only.

| Field | Exact value |
| --- | --- |
| Project / repo | sim_heat / physicsvigilante/sim_heat |
| Source PR | [#23](https://github.com/physicsvigilante/sim_heat/pull/23) — **draft, open, unmerged** |
| Base on main | 69350dab2a6faf0c10d0c0aa1d2333051f40e0e9 |
| **Review source HEAD** | **439c02ae3157f01c8ccc7ab5eb58297af0c17d92** |
| Source Git tree | 5ee04196a4e9a21f180f63362e1b58acdd793ac2 |
| Risk class | **R2**, source-pair native evidence semantics and v2 browser comparison |
| New manifest | viewer/network/data/compare_sources.json, version sim_heat.viewer.compare_sources/1 |
| Derived pair index | viewer/network/data/compare_index.json, version sim_heat.viewer.compare_index/2 |
| Source-native pair | H1_D2 original and H1_D2_K2 hypothetical one existing rod conductivity changed |
| Original baseline native | [run 43691263273](https://github.com/physicsvigilante/sim_heat/actions/runs/43691263273), artifact 14152886226, full ZIP SHA 8fc38b9e2f040b48ab5cbeab34e8698b7c99c4d462a1e31e8bc33b0395185379 |
| Original successor native | [run 43693191224](https://github.com/physicsvigilante/sim_heat/actions/runs/43693191224), artifact 14153251022, full ZIP SHA dc32a0a36a27f031ce7a13da83ebdd26a3dd6ac1d14612fa597b36cb439f4843 |
| Evidence meaning | Source-linked historical native diagnostics only; nativeQualified=false; public requests diagnostic_only |
| Authenticated source-host boundary | New external GitHub run/commit/artifact/ZIP identities must be checked **outside** manifest/adapter; internally self-pinned fabricated data is not native attestation |
| Source preservation | **10 changed paths**, no H1/Modelica/checker/runner/numerical files, no original six native case JSON changes, no main network renderer modification |
| New tests | Strict H1 direct-parent revision, source index byte replay, synthetic rehashed source/case refusals, native source-pair relation, browser provenance refusal and stale pair fetch |
| Final CI | [43870501998](https://github.com/physicsvigilante/sim_heat/actions/runs/43870501998) — **completed/SUCCESS** at exact source HEAD |
| CI results | **151 H1**, **4 analytic**, **32 Python methods discovered: 31 passed, one optional original-native-archive integration skipped**, **23 JS**, real Chromium desktop/mobile **PASS** |
| CI evidence | [artifact 14227156874](https://github.com/physicsvigilante/sim_heat/actions/runs/43870501998/artifacts/14227156874), 5,561,787 bytes, ZIP SHA-256 **dc9272e8f5b8a14cce3e90c45923994028fbdd2515d91e2846e11525a35e04ff** |
| Artifact QA | Original CI ZIP downloaded by Chat A; complete file SHA-256, ZIP CRC and exact source head-sha.txt checked; screenshot refusal/stale-race reviewed |
| First failed source CI | [43869630924](https://github.com/physicsvigilante/sim_heat/actions/runs/43869630924) — **failed at old SHA on test syntax**; remains a failed historical run |
| Independent Review 01 | **Awaiting Chat B**, path reviews/review-01-chat-b.md |
| Merge | **Not permitted until genuine independent R2 outcome and exact-head CI** |
| Post-merge CI | Not applicable; PR still draft and unmerged |

## Physical and evidence scope

This is a strict generic **comparison-source authoring contract**, not a new physical arrangement, new native model or freeform browser solver. The existing H1 source parser checks only the permitted single conductivity revision. Read-only offline code derives the pair from the already authored and SHA-pinned Modelica parent/child studies and catalog source files. The versioned browser runtime verifies the original per-side native provenance metadata prior to showing genuine saved K/J/W. Exactly one pair is published: D2 → D2-K2; future pairs must first have independently checked genuine native sources and H1 revision admission.

**Caveat (deliberately tested):** A self-repinned fake source-case JSON and matching plan can pass *internal* admission. Original source-host execution must be independently grounded through GitHub Actions run/executed commit/artifact/whole ZIP identity for each future physical candidate. No independent measurement, broad new parameter sweep, H1-C1 held-out transfer, unrestricted Modelica, reference certification or validated classroom learning is claimed. The original six source-linked native viewer bundles and failed H1/C1 history remain unchanged.

## Independent review handoff and stop point

- [REQUEST.md](REQUEST.md): exact source, CI and native provenance, schema changes and adversarial review scope.
- [REVIEWER-PROMPT-01.md](REVIEWER-PROMPT-01.md): user-ready independent Chat B request.
- [REVIEW-TEMPLATE.md](../../../REVIEW-TEMPLATE.md), [PROTOCOL.md](../../../PROTOCOL.md), [REVIEW-RISK-POLICY.md](../../../REVIEW-RISK-POLICY.md): the shared risk-based two-ChatGPT process.

**Next:** The owner sends REVIEWER-PROMPT-01 to the independent Chat B conversation. Chat B reads the **exact review HEAD** and writes a **new report** under reviews/review-01-chat-b.md directly in the central repository. The owner can return and say “review done”; Chat A will retrieve the independent report from GitHub, address defects, run new current-head CI/re-review if necessary and then use standing merge authorization **only on independently reviewed passing source**. **Do not merge until the independent report exists.**
