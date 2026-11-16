# SIM_HEAT H3-04 PR #19 — central R2 review status

**Status: `awaiting-independent-review`.** Chat A/ongoing development completed source, historical-native verification, generic converter, teacher-facing source-linked comparison, and passing exact-HEAD CI. **No independent Chat B result or release authorization is claimed. PR #19 remains draft/unmerged.**

| Field | Value / result |
| --- | --- |
| Project | `sim_heat` |
| Draft PR | [#19](https://github.com/physicsvigilante/sim_heat/pull/19) — open, unmerged |
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
| Chat B review | **Awaiting independent Review 01** at `reviews/review-01-chat-b.md`; Chat A must not pre-author findings |
| Merge | **Not authorized until R2 review PASS and exact-head CI confirmed** |
| Postmerge CI | Not applicable; source PR is unmerged |

## Preservation and trust limits

The first five original native viewer case JSONs, H1 Modelica laws, parser/study/revision checks, native runner, numerical thresholds, old native campaign batches and frozen H1-C1 source remain unchanged. The reviewed change adds one generic *offline* historical-campaign adapter, one source-linked D2-K2 JSON case and catalog entry, one read-only dedicated comparison page/logic, and offline/Chromium regression tests. It does **not** implement in-browser arbitrary Modelica, parameter sweeps or unrestricted reruns; chart strokes connect native saved points visually without extra computed observations. The original and successor native data stay `diagnostic_only`, `nativeQualified=false`; SHA-pinning and metadata matching do not independently attest arbitrary new archives.

Early H3-04 development failed/cancelled CI at different source SHAs remains part of the source history. No previous run status is relabeled. The final exact-head CI passed, and the original historical native campaign is an independent earlier run; **zero new OMC commands** for the new comparison page.

## Handoff and release

- [REQUEST.md](REQUEST.md): physical model, source-native archive and independent adversarial R2 questions.
- [REVIEWER-PROMPT-01.md](REVIEWER-PROMPT-01.md): ready-to-paste Chat B independent review request.
- [REVIEW-TEMPLATE.md](../../../REVIEW-TEMPLATE.md), [PROTOCOL.md](../../../PROTOCOL.md), [REVIEW-RISK-POLICY.md](../../../REVIEW-RISK-POLICY.md): report and merge rules.

**Next:** Chat B opens the pinned PR head, independently checks source/native/CI where possible, and writes a new `reviews/review-01-chat-b.md` into this central repository. The owner may say “review done” to have Chat A retrieve the report directly. Under standing owner authorization, routine code changes and a merge **after** a genuine scoped R2 PASS are allowed without repeated approval prompts, but no merge may occur before the independent report and current-head CI gate.
