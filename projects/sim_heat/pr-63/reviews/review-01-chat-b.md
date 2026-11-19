# SIM_HEAT PR #63 — independent Chat B R2 review-01

**Verdict: CHANGES REQUESTED** for the checking-only comparator at exact head **232bca1737210a80e1fb8e41b7ec67c6248f6a9f**. This is **not** a rejection of the ordinary primary-only numerical comparison: that path passed my independent controls. The blocking finding is a source-facts hash/parse time-of-check-to-time-of-use gap in a provenance-sensitive admission boundary. **No native qualification, OpenModelica permission, deployment, or merge is granted.**

## Identity, scope, and independence

| Item | Independently examined |
|---|---|
| Source repository / PR | [physicsvigilante/sim_heat PR #63](https://github.com/physicsvigilante/sim_heat/pull/63), still OPEN, DRAFT, UNMERGED at inspection |
| Stacked PR62 base | `29bc126967d180e7f92b0a8bc29f50ee17608eb7` |
| Exact reviewed head | `232bca1737210a80e1fb8e41b7ec67c6248f6a9f` |
| Authenticated full Git tree | `87dae90d2975516553d01af9040f7f62ef82071a` |
| PR synthetic merge / same tree | `3039be8c4b31f955f321dab6534d6e5461ad0421` |
| Reviewer | Chat B, separate ChatGPT conversation, GPT-6; **2026-11-19 (IST)** |
| Risk and boundary | R2, fixed original T1-T offline qualification comparator ONLY. No re-review of unchanged PR62 interval mathematics, PR60 thermal design, production H1, Modelica, runner, or historical C1 |
| Source changes made by reviewer | **None.** All personal tests used an extracted, pinned source archive and separate scratch fixtures. The only repository write authorized by this review is this new report in `review_sandbox` |

I read [REQUEST.md](../REQUEST.md), [REVIEWER-PROMPT-01.md](../REVIEWER-PROMPT-01.md), central `PROTOCOL.md`, `REVIEW-RISK-POLICY.md`, `REVIEW-TEMPLATE.md`, source `AGENTS.md` and relevant H1/N1 contracts, and inspected all four changed files at the pinned SHA: [compare.py](https://github.com/physicsvigilante/sim_heat/blob/232bca1737210a80e1fb8e41b7ec67c6248f6a9f/qualification/h1_n2/compare.py), [test_compare.py](https://github.com/physicsvigilante/sim_heat/blob/232bca1737210a80e1fb8e41b7ec67c6248f6a9f/qualification/h1_n2/tests/test_compare.py), the README and checking-only CI workflow. The changed-file list contains exactly these four added paths; no older H1 or physical source file is in the PR diff.

## Findings

### F-01 — MAJOR, scoped blocker: original facts are hashed and then independently re-read for parsing

**Location:** [`qualification/h1_n2/compare.py` lines 55–65](https://github.com/physicsvigilante/sim_heat/blob/232bca1737210a80e1fb8e41b7ec67c6248f6a9f/qualification/h1_n2/compare.py#L55-L65).

`_original_inputs()` verifies SHA-256 by calling `path.read_bytes()` in a loop. It **then calls `facts_path.read_bytes()` and `study_path.read_bytes()` a second time** to construct the data used by `_companion_contract()`. If an input file changes between those two reads, the digest can be correct for the first bytes while the comparison uses different, unverified bytes. The second read is not cryptographically tied to the original hash result.

**Personally executed, deterministic adversarial reproduction:**

1. On a separate scratch copy of the three pinned original files, prepare both synthetic reference bundles with a changed `spec.provenance` string, recompute their self-contained semantic seals and matching synthetic receipts. Keep the original physical model and both original/companion authored studies unchanged. This uses only the comparator's explicitly **caller-supplied**, unauthenticated seal interface.
2. Without any source-file read change, the same supplied pair **REFUSES** with `n2_comparison: primary reference facts are not the pinned original`.
3. Instrument `Path.read_bytes` only to *schedule a real scratch-file write immediately after the first facts-file hash read*; the second invocation reads the replacement JSON from disk normally. The pinned first-read SHA-256 is `39f18db09fa618bc73bbe75ca40f33d41ded70a1c73865b2a0e376973d9adfbf`; the later parsed file has SHA-256 `497836f139d05ca29b484c5ed1947917a08545ac2db25396a89edf91405ff0d1` and provenance `replacement provenance after SHA check`.
4. On the **unchanged pinned implementation**, `compare_candidates` returns **`checks_passed` with all 85 comparison checks** despite the altered original provenance being parsed after the accepted original digest. The scratch source was discarded; no project source or original reference was edited.

This is a real atomicity defect in the claimed original-byte pin, **conditional on a source-file race and caller-controlled/resealable bundles**. It does *not* prove that a genuinely externally anchored, prospectively sealed reference can be forged, nor that such a race occurred in CI or native execution. Those distinctions matter. Nevertheless, the original facts hash should protect the exact bytes actually consumed, independently of whether a caller is well behaved.

**Required correction:** read each original model/study/facts file **exactly once per invocation**, retain those bytes locally, hash those same snapshots, and parse facts/study from those same verified snapshots. Add a focused negative test that changes the second-read content (or mutates the scratch file at the former boundary) and proves no altered provenance/facts can enter after the hash guard. Leave all frozen originals, prior reviews, and inherited verification unchanged. New correction head and exact-head CI are required; a targeted F-01 re-review is sufficient if nothing broader changes.

### F-02 — MINOR, malformed inputs can escape as Python errors instead of controlled refusals

**Locations:** [`compare.py` lines 41–42, 78–126 and 219–229](https://github.com/physicsvigilante/sim_heat/blob/232bca1737210a80e1fb8e41b7ec67c6248f6a9f/qualification/h1_n2/compare.py#L41-L42) and the inherited receipt/CSV encoding path.

I invoked **`compare_candidates` directly**, supplying valid other arguments and valid receipts, then malformed individual inputs. Observed results:

| Independent malformed input | Actual exception |
|---|---|
| Primary reference `{}` (missing `spec`) | `KeyError('spec')` |
| Primary reference `[]` | `TypeError` (list indexed by a string) |
| Primary allowance `T_Cool.T = 10**400` | `OverflowError` from `math.isfinite` before the H1 verifier |
| Primary CSV containing an unpaired UTF-16 surrogate | `UnicodeEncodeError` before H1 can issue a `Refusal` |

**None returned `checks_passed`; these are availability/structured-error issues, not observed numerical false approvals.** Harden shallow bundle shapes, bound integer-to-float conversion, and translate malformed CSV encoding to explicit `h1.model.Refusal` at the public API boundary. Add focused negative tests. This finding alone would not block a checking-only scoped pass, but should be addressed in the small correction.

## Independent numerical, verification, and failure controls — what passed

**Personal authenticated source:** I downloaded both GitHub Actions ZIPs, independently computed SHA-256, tested ZIP CRCs, extracted their complete `source.tar` entries, and reconstructed Git trees with Git's tree writer. Both reconstructed trees equal the pinned `87dae90d2975516553d01af9040f7f62ef82071a`. Push `source.tar` and PR synthetic merge `source.tar` are not literally byte-identical archives; their **Git trees are identical**. The local source tree remained byte-identical after personal tests.

- [HEAD push CI 44477843399](https://github.com/physicsvigilante/sim_heat/actions/runs/44477843399): downloaded artifact `14507011900`, **1,492,024 bytes**, personally computed ZIP SHA-256 `ad3f8fb5216a3ed7dc5d147c119107be0e6b81a1952cc68d885e768b9ce94f76`, CRC clean.
- [PR synthetic CI 44478153394](https://github.com/physicsvigilante/sim_heat/actions/runs/44478153394): downloaded artifact `14506868426`, **1,492,052 bytes**, personally computed ZIP SHA-256 `19a85e72bcd886ddb80ff8a04f7be2c16d65b967954527fa5cdbba0f623cba77`, CRC clean.
- Each **hosted** artifact contains successful logs for **12 N2 + 17 N1 interval + 34 N1 plan + 152 H1 = 215 distinct tests**, docs parity PASS, the unchanged seven original physical-100x checking-centre refusals and eight execution blockers. The two CI runs are repetitions, **not 430 independent tests**. PR job and push job metadata report SUCCESS. I inspected these hosted records; I did not personally rerun all inherited 203 tests.
- I independently inspected [first RED push 44477497880](https://github.com/physicsvigilante/sim_heat/actions/runs/44477497880) logs: failures were `n2_comparison: exact declared planned grid is required`, consistent with the reported incorrect old grid construction. The reviewed head instead demands equality to actual H1 `Study.grid` (`float(stop) * (i / intervals)`), not an invented `i * (stop/intervals)`. No change to the inherited matching window was found.

**Personal execution:** on the authenticated source, using already-present Python 3.13.5 / NumPy 2.3.5 / SciPy 1.17.0 / mpmath 1.3.0, I reran **12/12 existing N2 tests PASS** (11.74 seconds). Separately I authored and ran **21 adversarial probe cases**, **four direct malformed-API probes** to disambiguate fixture versus production exceptions, and the two supplemental on-disk race/reseal experiments. The reviewer-authored Python probes installed an audit hook forbidding child/native process launch. I did **not** execute OpenModelica.

The reviewer-authored controls found the following on the nominal, unmodified-source path:

| Contract challenged | Personally observed |
|---|---|
| Exactly original T1-T and declared tight/dense variants | Both synthetic positives `checks_passed`; each returned 2 H1 per-run `checks_passed`, 2401 common planned samples, **77 internal exports and 8 public observations** |
| Independently derived all-output oracle | Recomputed names, all maxima, worst sample times, signed `T03.port_a - T_Cool.port`, primary allowances and pass flags for **all 85 outputs** directly from decoded raw CSV vectors; matched module output |
| Four legitimately different primary/dense allowances | Exactly `T02.Q_flow`, `T02.port_a.Q_flow`, `T02.port_b.Q_flow`, `T_Warm.Q_to_network` differ; both otherwise valid runs pass without requiring epsilon equality, and every export comparison uses the **original primary supplied** epsilon |
| Per-run gate as prerequisite | A deliberately failing **primary** candidate and the existing failing **companion** test each refused before numerical cross-run output; no gate bypass found |
| Two individually passing CSVs differing across runs | A `T_Cool.T` +0.75/−0.75-primary-epsilon construction passed the H1 verifier separately on each run but produced `checks_failed`, ratio approximately **1.5** on the primary-only cross-run export |
| Public difference orientation and budget | `request:t_upper_minus_cool` evaluates `T03.T_a - T_Cool.T` on both sides; its epsilon is `local_allowance("K", max(abs(primary_reference_difference)))`, not summed operand allowances or a companion-derived scale. The eight requests were all present |
| Exact grid and timing | Correct dense even-index planned grid matched primary; actual interior jitter within the sealed per-run window was admitted, jitter outside refused; **no interpolation** |
| Duplicate, missing, malformed candidate data | Identical duplicate CSV row was canonically collapsed by the inherited decoder; **conflicting** duplicate timestamp, missing row, duplicated header, NaN and overflow-to-Inf sample each refused |
| Identity, receipts and evidence labels | In-memory companion provenance mutation, tampered bundle without reseal and forged `certified_native` evidence kind refused; output always reports `nativeExecuted=false`, `nativeQualified=false`, `runtimeReady=false`, `independentlyCertifiedReference=false`, `referenceAccuracyCertified=false` |

A deliberate **caller re-seal** is a separate, **already-disclosed trust boundary**, not an additional demonstrated implementation bug: inflating the supplied primary `T_Cool.T` allowance by 2×, recomputing the bundle's temporal policy, seal, and receipt, then passing that newly selected seal as the expected argument changes the above cross-run result from `checks_failed` (ratio ≈1.5000) to `checks_passed` (ratio ≈0.7500). Thus these **caller-supplied semantic fingerprints do not independently authenticate pre-output reference sealing or establish an immutable historical primary tolerance**. The API expressly declares that chronology/trusted seal pinning must come from external evidence. Do not present this synthetic result as native qualification or as proof of a trusted-seal bypass. For any future trusted deployment, externally pin the reference seal **before** candidate generation and independently authenticate that pin.

## Evidence boundary and inherited holds

The currently used `h1.reference.prepare` bundles are **synthetic checking fixtures**, not N1 certified physical reference centres. I personally parsed the downloaded plan-check JSON from both current-head artifacts; each still lists the original physical 100× refusals **`T02.G, T06.A, T06.G, T07.G, T08.G, T10.G, T_Plug.C`**, **eight native-execution blockers**, `nativeCallsThisCheck=0`, `nativeExecutionReady=false` and `referenceAccuracyCertified=false`. I did not recompute all physical interval certificates or inspect native logs, because no native execution was authorized.

| Review dimension | Judgment within this R2 scope |
|---|---|
| Original-source interpretation fidelity | **Conditional/fail on byte-authentication boundary** (F-01); fixed-T1-T/companion data equality otherwise enforced |
| Primary-only cross-run numerical policy | **PASS in personally tested synthetic cases**, including independent 85-output oracle; no certified physical accuracy claim |
| H1 per-run verification integration | **PASS in tested normal and negative cases**; inherited verifier itself outside this changed-file review |
| Evidence integrity and provenance | **CHANGES REQUESTED**: F-01; prospective seal chronology remains external |
| Native simulation and export attestation | **UNQUALIFIED / NOT RUN**; seven checking-centre refusals and eight blockers remain |
| Teacher-facing usefulness | Not evaluated; checking-only API, no student-facing viewer change |
| Textbook-answer completeness | Not applicable to this fixed qualification checker |

## Disposition and smallest next step

**CHANGES REQUESTED at head `232bca17…`**, specifically to close F-01 and add its regression. F-02 is a minor, localized hardening recommendation, ideally included without changing the numerical or source admissibility contract. Preserve the original RED artifact, previous independent reports, frozen facts and seals, and all existing gate statuses. Publish a new correction SHA and re-run exact-head push/PR CI, then request a **targeted independent correction review** of the affected read/validation path; no general H1/PR62 physics re-audit is needed unless the patch changes those semantics.

**STOP remains in force:** no OpenModelica installation, query, build, launch or native result; no original N1/C1 reference regeneration or promotion; no production edits or merges. PR63/PR62/PR60/PR59 remain draft/unmerged unless the owner authorizes changes in a separate decision. This report is an independently authored Chat B finding, not an independent human/physical certification.
