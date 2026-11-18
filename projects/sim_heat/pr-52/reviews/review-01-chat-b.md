# SIM_HEAT PR #52 — Independent Chat B targeted R2 review 01

**Outcome: SCOPED PASS** — PR51 F-01 strict integer metadata correction in the steady and campaign archived-evidence adapters, **and preservation of the six original diagnostic bundles only**. This is not an unrestricted source approval, production merge authorization, or native/scientific qualification. **Original PR51 review-01 remains CHANGES REQUESTED at its original head.**

## Reviewed identity, authority and limits

| Item | Exactly reviewed |
|---|---|
| Project / PR | [physicsvigilante/sim_heat PR #52](https://github.com/physicsvigilante/sim_heat/pull/52), open **draft**, unmerged |
| Source head | `e78ec2ccb2f8f97bbc1b282ec6bbe2847c1e1603` |
| Source Git tree | `2ad10a1679d528f88030494f0349171502ef8e0f` (checked via GitHub Git commit API, not just PR body) |
| Immediate base | Original reviewed PR51 `52d693a748ad3709c99215bac0a5840a236937a6` (tree `7dcbb52c40f5b431ccdfe5dd4d2329fa21463829`) |
| Comparison | [PR51 exact head → PR52 exact head](https://github.com/physicsvigilante/sim_heat/compare/52d693a748ad3709c99215bac0a5840a236937a6...e78ec2ccb2f8f97bbc1b282ec6bbe2847c1e1603), seven commits, **five files total** |
| Reviewer | Chat B, separate review conversation, GPT-6; independent-in-context, not a human assessor or proven different model family |
| Evidence date | 2026-11-18, approximately 04:10 UTC / 09:40 IST |
| Risk / scope | **R2**, narrowly re-review of historical PR51 major F-01: type semantics of archived provenance, case sample counts, original-archive preservation and CI |
| Source changes by reviewer | **None** to `sim_heat`. This independent report is the only requested GitHub write, to `review_sandbox`. No merge, model/reference/native invocation or release operation. |

I read the pinned reviewer prompt, [central REQUEST](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-52/REQUEST.md), central protocol/risk policy/template, original [PR51 Chat B review](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-51/reviews/review-01-chat-b.md), `AGENTS.md`, relevant H1 contract/offline amendment/C1 freeze and exact-head source/diff/CI. Chat A's intended verdict was **not** treated as independent evidence.

**Diff verified:** exactly two modified production files, `viewer/network/tools/build_steady_case.py` (+3 lines) and `viewer/network/tools/build_campaign_case.py` (+5/−1 lines), plus three new files: `viewer/network/tests/test_provenance_integer_types.py`, `viewer/network/PR51_F01_TYPED_PROVENANCE_SCOPE.md`, and `.github/workflows/pr51-f01-typed-provenance.yml`. The two production diffs only insert three exact-type guards apiece; they do not alter expected counts, preserved MAT/CSV bytes, decoder/checker calls, physical equations, studies, references, runner, native plan, or previously published viewer/case/catalog/comparison files.

## Findings

### F-01 — MAJOR in PR51; **resolved in PR52's bounded source**

**Category:** provenance/schema strict-type admission. **Confidence:** high for exact-head source semantics and observed hosted adapter regressions; independently re-expressed against original archive metadata; limitations below.

- [Steady, lines 121–125 and 141–149](https://github.com/physicsvigilante/sim_heat/blob/e78ec2ccb2f8f97bbc1b282ec6bbe2847c1e1603/viewer/network/tools/build_steady_case.py#L121-L149): selected case `canonicalSamples` must have **`type(value) is int`** before `== 2`; `mat_provenance.json` `samples` must be exact `int` before `== 2`; `duplicateRowsCollapsed` must be exact `int` before `== 1`.
- [Campaign, lines 118–123 and 144–152](https://github.com/physicsvigilante/sim_heat/blob/e78ec2ccb2f8f97bbc1b282ec6bbe2847c1e1603/viewer/network/tools/build_campaign_case.py#L118-L152): the corresponding case and provenance fields must be exact `int` before comparison with `len(study.grid)` (1001 on original D2_K2) or one duplicate.
- The source uses `type(record.get(field)) is int`, **not** `isinstance(value,int)`. For missing keys `.get` returns `None` and the conjunction short-circuits to the existing structured `steady_evidence` / `campaign_evidence` `require` refusal. JSON Boolean, float (even numerically equal), string and null cannot pass. The previous PR51 bare comparisons would admit `2.0 == 2`, `1001.0 == 1001`, `1.0 == 1` and `True == 1`.
- No alternate branch bypasses these checks in the inspected two compilation functions before producing a viewer output. Existing full-manifest digests, original candidate receipt/reference checks, MAT/CSV shape and GitHub identity-input agreement remain in place. Returned `source.evidenceKind='historical_native_diagnostic'`, `source.nativeQualified=False`, and `source.publicRequestStatus='diagnostic_only'` are unchanged.

**No demonstrated residual code defect** was found within this narrowly changed F-01 surface. Existing external authentication is *not* solved: matching a caller-supplied ZIP SHA and run/commit/artifact strings proves internal consistency only; separately trusted GitHub run/artifact records are required to call an archive the authentic historical one.

## Personally performed checks — not a hosted test claim

**Independent original-archive custody and reexpression.** I used the GitHub connector to download **all five actual original workflow artifact ZIPs** into an isolated read-only-input environment, verified their whole-file SHA-256 against independently retrieved GitHub Actions artifact metadata, checked ZIP CRCs and original attempt `nativeQualified=false` statuses. Both targeted actual original records have literal integer metadata: **S1 (2, 2, 1)** and **D2_K2 (1001, 1001, 1)** for case canonical/provenance samples/duplicate rows.

I then **personally executed a standalone Python reexpression of the exact six PR52 guard expressions on the genuine S1 and D2_K2 member data**, rebuilding all ZIP members into disposable **test-only** copies and recomputing the affected `artifactSha256` manifest entry and outer ZIP digest. Every other member (including MAT, CSV, source, presealed reference and saved checking result) was byte-preserved. Originals remained unchanged. Outcome:

| Local test-only probe | Personally observed |
|---|---|
| Positive literal-integer controls, one rehashed ZIP per original | **2/2** pass the exact three-field integer/count expressions |
| Wrong-type single-field mutations: 3 fields × 2 actual archives × 7 variants (`matching float`, `true`, `false`, numeric string, `null`, missing key, `0.0`) | **42/42** refused by the independently executed new guards; zero guarded admissions |
| Historical PR51 loose-equality comparison against those 42 mutations | **8** would pass due to numeric type coercion (six matching floats and two `true` duplicate counts), reproducing the mechanism of original PR51 F-01 |
| Repacked ZIP versus original GitHub SHA | Every test-only repack differs from the authentic original digest; passing a new repack's own SHA is **not** GitHub attestation |
| Original ZIP preservation | Five original ZIPs remained read-only and their SHA/CRC checks passed |

**Precise execution limitation:** this local 44-probe set is **independent reexpression of pinned production guard logic against actual original archived metadata**, not execution of the entire production Python adapters or verification that all 42 raise the actual `Refusal` class. Direct Git cloning was unavailable in this runtime, and I did not reconstruct the complete production/dependency tree. The **real adapter executions and structured refusal codes** are separately supported by exact-head hosted test logs, not misrepresented as my own runs.

**Five authenticated original ZIP identities, independently downloaded/rehashed/CRC-tested:** (D1 and D2 share their original artifact.)

| Original case(s) | GitHub run / artifact | SHA-256 of personally downloaded ZIP |
|---|---|---|
| D1 / D2 | [43691263273](https://github.com/physicsvigilante/sim_heat/actions/runs/43691263273) / 14152886226 | `8fc38b9e2f040b48ab5cbeab34e8698b7c99c4d462a1e31e8bc33b0395185379` |
| DEV_BRIDGE | [43699424883](https://github.com/physicsvigilante/sim_heat/actions/runs/43699424883) / 14155084346 | `f16975a25eea79f61f7819fb9e704ab04a33630044a51a0d062b8399c1c9ce38` |
| S1 | [43820600508](https://github.com/physicsvigilante/sim_heat/actions/runs/43820600508) / 14204656273 | `82b4a87b66e0022d582da931253649b3829f6633119a57081c02dc253dc5dbd9` |
| TEACH_RING4 | [43845664024](https://github.com/physicsvigilante/sim_heat/actions/runs/43845664024) / 14215520616 | `0bc1433be66df2827f8907d100ca264f6a721fe8ad40644b962500b97fa9b8b2` |
| D2_K2 | [43693191224](https://github.com/physicsvigilante/sim_heat/actions/runs/43693191224) / 14153251022 | `dc32a0a36a27f031ce7a13da83ebdd26a3dd6ac1d14612fa597b36cb439f4843` |

I also independently checked that the five GitHub Actions run heads and corresponding artifact metadata bind their original recorded source commit identities. No original native binary was executed. The six published *preview bundle* replay comparisons below were **inspected from hosted CI**, not locally rebuilt.

## Exact-head GitHub CI — downloaded/inspected, not locally rerun

[**Successful run #44232637466**](https://github.com/physicsvigilante/sim_heat/actions/runs/44232637466), push, attempt 1, `head_sha=e78ec2ccb2f8f97bbc1b282ec6bbe2847c1e1603`; job `134561125994`, all required offline/archive/browser steps SUCCESS. Independent GitHub Git-commit metadata shows tree `2ad10a1679d528f88030494f0349171502ef8e0f`.

[**Workflow artifact #14396095895**](https://github.com/physicsvigilante/sim_heat/actions/runs/44232637466/artifacts/14396095895) was **personally downloaded and inspected**, not merely taken from the PR prose: **5,874,322 bytes**, whole-file SHA-256 **`2c22dd3db778942227acec29364819e73bd0a0822b006a7b5cc9bfc4a1555d36`**, **34 distinct members and 34/34 CRC-valid**. This equals GitHub Actions' independently returned artifact digest/size. Internal `head-sha.txt`, `head-tree.txt`, and five-path `source-diff.txt` match the exact reviewed head/tree/comparison.

| Exact-head hosted evidence | Independently inspected result | Classification |
|---|---|---|
| `targeted-F01-tests.log` | **9/9 PASS** using actual steady/campaign adapter functions | Hosted execution, not my local 42 probes |
| `h1.log` | **152 PASS** | Hosted |
| `arithmetic.log` | **4 PASS** | Hosted |
| `adapters.log` | **63 collected: 62 PASS, 1 optional SKIP** | Hosted; the nine new focused tests are *included* in the 63, not additional passes |
| `node.log` | **31 PASS** | Hosted |
| Unique full hosted total | **249 PASS, 1 optional SKIP, 0 FAIL** | 152 + 4 + 62 + 31; **no double counting** |
| `archive-replay.json` | **Six original cases BYTE_IDENTICAL**, `nativeExecutedByReplay=false` for D1, D2, DEV_BRIDGE, S1, TEACH_RING4, D2_K2 | Hosted real-adapter archive replay, not locally rerun |
| `compare-replayed.json` | Git blob `f70e4f077bb1dff6b6163bb1770fe4515bd44903`, matching unchanged published `viewer/network/data/compare_index.json` | Personally rehashed downloaded CI bytes and compared to pinned source blob |
| Explorer Chromium smoke | **PASS**, 21 PNGs and `browser.log`; hosted original test step SUCCESS | Browser was hosted, **not launched by me** |

The new focused tests call the **real production adapters** and check structured `steady_evidence` / `campaign_evidence` refusals. Their S1 data and D1 campaign source are **test-only fixtures**; the campaign test is not a claim that the original D2_K2 native campaign was rerun. The separate original-archive replay is the evidence for the genuine six unchanged cases. Its six preview SHA-256s also match the published source `viewer/network/data/index.json` catalog, which is not modified by this PR.

I **visually inspected** three images from the downloaded hosted artifact: `browser/steady.png` (steady algebraic evaluations correctly distinguished from physical time; diagnostic-only source), `browser/refusal.png` (refusal message and cleared graph/values) and `browser/whatif-desktop.png` (two source-linked saved histories, diagnostic limitations). This supports the existing hosted smoke, **not** a locally performed Chromium run, accessibility audit, independent teaching study or new native physics verification. The workflow has no OpenModelica/native launch step.

### Earlier CI must remain visible

- [**#44232238318**](https://github.com/physicsvigilante/sim_heat/actions/runs/44232238318): **SUCCESS** at earlier `ce9503a2318451f85676bba253244ad03033cbd1`, but imported inherited campaign class caused **three tests to be collected twice** (12 targeted, 66 adapter methods), so its counts are not treated as unique coverage.
- [**#44232475551**](https://github.com/physicsvigilante/sim_heat/actions/runs/44232475551): genuine **FAILURE** at earlier `d003aced0a0944b66dbb635e42f6b82328cd7b1a`. I inspected job logs: **18 errors**, including `AttributeError: 'CampaignTypeAuditTests' object has no attribute 'fixture'`; removing the accidental import-based collection had also removed implicit fixture initialization. Archive replay/browser steps were skipped on this failed run.
- [**#44232637466**](https://github.com/physicsvigilante/sim_heat/actions/runs/44232637466): current **SUCCESS** after explicit synthetic fixture `setUpClass()` initialization, with nine focused methods and no duplicate class collection. This **does not erase** the prior failure or promote its results.

## Separate scope judgments

| Dimension | Scoped disposition | Basis / limitation |
|---|---|---|
| Source interpretation fidelity | **Preserved / not re-adjudicated** | No textbook facts, source provenance, model/study inputs or physical assumptions changed in five-path diff |
| Physical/numerical correctness | **Unchanged / not newly certified** | Old checker/reference and native data intact; no new independent physical calculation or C1 accuracy PASS |
| Composition and authorability | **Not newly demonstrated** | Adapter change is strictly metadata admission; generic topology/explorer tests are historical offline evidence |
| Native simulation/observable coverage | **No new native qualification** | Six original diagnostic archives retained; `nativeQualified=false`, `diagnostic_only`; native launch not performed |
| Evidence integrity / provenance | **SCOPED PASS for F-01** | Six exact-int guards, 42 local reexpression negatives, two positives, hosted real-adapter refusals, external original artifact hashes and six-byte-identical hosted replay |
| Teacher-facing usefulness | **Existing hosted smoke supported; new usability unknown** | Reviewed screenshots and browser logs, no teacher or independent browser evaluation |
| Textbook-answer completeness | **Not assessed** | Outside this metadata correction |

## Unchanged historical hard stops and release advice

The independent [PR51 original review](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-51/reviews/review-01-chat-b.md) remains **CHANGES REQUESTED** at `52d693a748ad3709c99215bac0a5840a236937a6`; this **new** scoped successor does not rewrite it. Original C1 F0 `hotLead.G` reference precision **80× versus required ≥100× — FAIL**; PR32 exact cross-host bitwise regeneration of the reviewed original PR31 V2 reference **FAIL**; its alternate seal remains unadopted. All **nine** C1 native public values remain `not_computed` and the **11** owner-authenticated real native release/backup/host/runtime/plan/CAS/pre-native R2/budget gates are still missing. None of these are converted into PASSES by offline diagnostic evidence.

**Recommendation: SCOPED PASS for PR52 F-01 and original-data preservation only.** No further fix is required for the six inspected guards at this exact head. A production merge remains a separate, explicit owner decision with its own gates; this report does not approve merging PR51, PR52 or any other branch, altering C1 frozen reference/numeric outcomes, issuing a signed release, trusting arbitrary caller-rehashed archives, running `omc --version`, invoking OpenModelica/native prepare/build/launch, or creating new scientific qualification. A changed PR52 source head requires a new bounded check.
