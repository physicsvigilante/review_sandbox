# SIM_HEAT PR #37 — independent Chat B R2 review (F-02 exact-byte OFFLINE staging)

- **Source:** [physicsvigilante/sim_heat, draft PR #37](https://github.com/physicsvigilante/sim_heat/pull/37); historical F0 experiment, **do not merge to main**.
- **Reviewed base:** `7cfa35a1cd5cc858e48bcdc4da453bf2dc22b7f2` (PR #36).
- **Exactly reviewed head:** [`d1d6a32252b41dabad832668de642ecaf475a2a3`](https://github.com/physicsvigilante/sim_heat/commit/d1d6a32252b41dabad832668de642ecaf475a2a3).
- **Git tree:** `af85a6f1848a0f1231612144a1230689be8cf0f2` (checked using GitHub Git-data API and CI receipt).
- **Reviewer/date:** Chat B, separate ChatGPT context (GPT-6), 2026-11-17. Independence is contextual, not an independently credentialed human expert.
- **Risk/scope:** R2 evidence semantics; source/manifest provenance, exact saved bytes, negative paths, PR #36 F-06 strict types, CI. **No native physics run or scientific-law change is being approved.**
- **Source modification by reviewer:** None. No OpenModelica invocation, no native runner/version query, no frozen file edit, no historical PR merge.
- **Verdict: CHANGES REQUESTED — bounded to offline staging readback/evidence integrity.** The exact four scientific input bytes and the F-06 type fix pass inspection. Two reproducible readback-provenance weaknesses prevent an unqualified R2 PASS; neither currently confers native execution authority.

## Provenance, frozen scope and direct evidence

GitHub compare of reviewed PR #36 base against exact head is **ahead 8 commits / behind 0** and changes **exactly six paths**: ADDED `qualification/h1_c1/f02/stage_immutable_inputs.py`, `test_stage_immutable_inputs.py`, `IMMUTABLE_INPUT_STAGE_SCOPE.md`, `.github/workflows/h1-c1-f02-immutable-input-stage.yml`; MODIFIED `offline_control_preflight.py` and `test_offline_control_preflight.py`. No frozen H1 laws, original Modelica, studies, native runner, reference archive, manifest, owner record, or unlaunched native plan changed.

I compared GitHub Git-tree blob identities at this head, PR #36, reviewed PR #33 archive tree and the original F0 tree. **All 14 original frozen F0 source/checker/native-runner blob identities** agree with original F0; the first-author case files were introduced later, so are *not* asserted to exist at original F0. Current and reviewed archive trees agree on first-author and modal case inputs, frozen library, original native plan, PR31 compressed reference and archive manifest. Current staged model/study/library bytes also independently reproduce their exact Git blob IDs.

I downloaded and independently hashed:
- [Exact-head CI #44024037373](https://github.com/physicsvigilante/sim_heat/actions/runs/44024037373), [artifact #14302720735](https://github.com/physicsvigilante/sim_heat/actions/runs/44024037373/artifacts/14302720735): **1,190,471 bytes**, ZIP SHA-256 `0c10f8c1e71857354b3566940215ffccde3bfaf2157aed948a66db9ab00914b0`; **35/35 ZIP members CRC-valid**.
- [Original PR31 source artifact #14249313720](https://github.com/physicsvigilante/sim_heat/actions/runs/43915934653/artifacts/14249313720): **2,348,945 bytes**, ZIP SHA-256 `d9259837e0e03c70989b50b2c9dcbf13aca260da4d1cb0ae000b2a23ef65732e`; **13/13 members CRC-valid**.
- [Retained earlier failed PR37 CI #44023899014](https://github.com/physicsvigilante/sim_heat/actions/runs/44023899014), artifact #14302725410: **1,184,972 bytes**, ZIP SHA-256 `d0b0f7e3c2fdad41061da70fa5fca5da9869a61c1c2aace802ddf40028bf2ca0`; **30/30 members CRC-valid**; the original failure remains recorded.

The exact-head artifact contains exactly six members inside `ci-original/` (four data inputs and two JSON metadata files). I independently recomputed their SHA-256 and directly compared the **entire** staged 4,409,800-byte `reference.bundle.json` with the original PR31 `C1_REFERENCE_V2_BUNDLE.json`: **byte-for-byte equal**, raw SHA-256 `0db511dd8dba023d16518667de256029cf3e073463ea21e2478aeac8afd1f368`. I independently recomputed the sorted-key compact JSON canonical seal excluding `seal`, yielding `d2b8e2ca8e1f929cac7b028dcc3f7d0b453921d193f877eb091e23ac70aa4ce9`. The bundle has 37 columns x 4,001 grid samples and four 4,001-sample flow-integral histories; `nativeQualified` is false. **This is exact original archived reference data, not regeneration, cross-host reproducibility proof or a native trace.**

| Staged input | Actual bytes | Independently recomputed SHA-256 |
|---|---:|---|
| `model.mo` (original first-author model) | 872 | `9a165e5ce2cc85da84ecc8bc4e63e2990f2066f3547dc6ba8508fa1afbe5f435` |
| `study.json` (evaluator-modal study; nine public requests) | 6,616 | `b43e85b6b10afd6550a43322cf98097fe9781a606ee01bc031eadbfd4783b31b` |
| `SimHeat.mo` (frozen thermal library) | 3,674 | `e57955b6c32cb34321a6b1908306c4ea9a63ae259b95a5fd48c7e8d3b4da10ea` |
| `reference.bundle.json` (saved PR31 raw JSON) | 4,409,800 | `0db511dd8dba023d16518667de256029cf3e073463ea21e2478aeac8afd1f368` |

The original historical native plan remains `sim_heat.native_batch/1` with **23 pinned source files** and raw SHA-256 `f46b2621b38427ffc098d16d91695a134b7dc4d7f913021be625ee74b8a9319a`; **it has not been launched**. The reviewed compressed XZ (503,552 bytes; SHA-256 `fc5a7df5928c3fb8aef2ba4af516dfbd32b42c0450ebef1051ad4fd7efebd17f`) and whole archive manifest (SHA-256 `50467b138ed64cdb908f2c763bc777e6babf0bb04a0711568acc559112e66f84`) retain reviewed Git-blob identity; current CI checked both fixed SHA-256 values. I did **not** independently download and hash the repository XZ blob a second time; this conclusion combines reviewed Git-object preservation, CI SHA checks, and independent source-artifact/staged-raw byte comparison.

## Findings (priority order)

### F-01 — MAJOR — duplicate permission/state keys bypass readback refusal

**Location:** [`stage_immutable_inputs.py` lines 159–166, 188–212](https://github.com/physicsvigilante/sim_heat/blob/d1d6a32252b41dabad832668de642ecaf475a2a3/qualification/h1_c1/f02/stage_immutable_inputs.py#L159-L212); contrast [`offline_control_preflight.py` lines 46–66](https://github.com/physicsvigilante/sim_heat/blob/d1d6a32252b41dabad832668de642ecaf475a2a3/qualification/h1_c1/f02/offline_control_preflight.py#L46-L66).

**Reproduction:** In an isolated copy of the actual six archived staged inputs, the exact `verify()` predicates were replayed under Python using an independently implemented reference canonical checker. Editing the manifest to contain both `"nativeAllowed": true, "nativeAllowed": false` (in that order) was **ACCEPTED** by the readback predicate, as was the same duplicate pair in `STAGE_STATE.json`. Python's default `json.loads` silently keeps the last duplicate value; the subsequent exact-field-set, equality and `is False` checks therefore see only `false`. A single unambiguous `true`, an extra `"command": "omc build.mos"` field, or flipped historical false field was correctly **REFUSED**. The original disabled-preview loader already uses a duplicate-key-refusing `object_pairs_hook`, but the new staged metadata loaders do not.

**Why it matters:** A readback receipt may report `OFFLINE_STAGED_EXACT_INPUTS_NOT_NATIVE` for a malformed evidence file containing contradictory native-permission assertions. Another JSON consumer may interpret duplicate keys differently. **No native runner consumes this manifest now, and this is not an OMC authorization bypass.** It nevertheless contradicts the intended fail-closed manifest/permission integrity contract.

**Required correction:** Apply strict duplicate-key rejection for **both** stage state and manifest, not just the disabled preview; reject nonstandard JSON constants if the parser is reused. Add actual on-disk adversarial regression cases with duplicate `nativeAllowed`, `nativeExecuted`, `ownerNativeLaunchApproved` and `status` keys. Preserve literal `is False` checks and no-executable policy.

### F-02 — MAJOR — `verify()` can accept a coordinated disabled-preview substitution

**Location:** [`stage_immutable_inputs.py` lines 150–185](https://github.com/physicsvigilante/sim_heat/blob/d1d6a32252b41dabad832668de642ecaf475a2a3/qualification/h1_c1/f02/stage_immutable_inputs.py#L150-L185), specifically `doc.get("disabledPreviewSha256") == sha((root/f02.PLAN).read_bytes())`. Compare [original pinned `f02.load_preview`](https://github.com/physicsvigilante/sim_heat/blob/d1d6a32252b41dabad832668de642ecaf475a2a3/qualification/h1_c1/f02/offline_control_preflight.py#L46-L56).

**Reproduction:** In the isolated staged-snapshot predicate replay, replace the disabled preview's bytes, then edit the stage manifest's `disabledPreviewSha256` to match the substituted file; the **readback predicate ACCEPTED** the altered pair with all four scientific input bytes unchanged. There is no independent literal preview SHA/Git-blob check or call to `f02.load_preview` in `verify()`. The current real `stage()` **does** invoke `f02.audit` before it writes, so the initial staging gate still refuses an altered original plan; the weakness is **post-stage readback** only.

**Why it matters:** The advertised verified readback binds its plan provenance only to an equally editable manifest, allowing a falsely completed receipt after coordinated source/manifest drift. It must not be treated as a fresh certificate that the disabled plan remains the approved exact plan.

**Required correction:** At readback, verify the disabled preview against the independently fixed reviewed Git-blob pin (for example via `f02.load_preview(root/f02.PLAN)`) and require its independently pinned raw SHA-256, rather than only agreement with a mutable manifest. Add a mutation test that changes the preview bytes **and** updates the manifest digest, requiring refusal. Do not call a native runner or recalculate the scientific reference.

### F-03 — MINOR — attempt identity and parent symlink not bound in readback

**Location:** [`stage_immutable_inputs.py` lines 99–107 and 150–157](https://github.com/physicsvigilante/sim_heat/blob/d1d6a32252b41dabad832668de642ecaf475a2a3/qualification/h1_c1/f02/stage_immutable_inputs.py#L99-L157).

**Reproduction:** A direct duplicate `stage(label=...)` is refused by `out.mkdir(exist_ok=False)` (also in hosted tests). However, an **already produced** stage copied/renamed to another valid label passed isolated `verify(label=new_label)`, which echoed the new label in the receipt; the persisted manifest/state do not bind the original attempt label. Also, after replacing the staging-parent directory with a symlink to an external directory containing the six valid staged members, readback accepted the final child directory (it checks `directory.is_symlink()`, not whether its parent is a symlink). This is an isolated local-filesystem reproduction, not remote tampering of GitHub artifacts.

**Correction:** Bind attempt identity (label and optional immutable attempt nonce/commit/tree) to stored metadata and verify it, distinguishing portable snapshots from fresh attempts. Refuse symlinked parent/ancestors and consider no-follow/directory-descriptor techniques if the surface will face concurrent writers. Do **not** mistake an exclusive new directory in transient CI for a durable, atomic one-shot native reservation. No executable write/launch was demonstrated.

### F-04 — MINOR — type hardening is correct for F-06 but not globally exhaustive

**Location:** [`offline_control_preflight.py` lines 112–145](https://github.com/physicsvigilante/sim_heat/blob/d1d6a32252b41dabad832668de642ecaf475a2a3/qualification/h1_c1/f02/offline_control_preflight.py#L112-L145), [`test_offline_control_preflight.py` lines 70–100](https://github.com/physicsvigilante/sim_heat/blob/d1d6a32252b41dabad832668de642ecaf475a2a3/qualification/h1_c1/f02/test_offline_control_preflight.py#L70-L100), new manifest readback line 174.

**PASS for requested PR #36 F-06:** Exact `type(maxLaunchesAfterSeparateApproval) is int` rejects `True` and `1.0` despite Python equality with `1`. Modal `startTime:int`, `stopTime:float`, `intervals:int`, `tolerance:float`, `solver:str` are checked independently of value equality. Exact-head hosted tests cover booleans and floats in these settings. The original disabled plan remains whole-file Git-blob pinned and unchanged.

**Residual:** Other standalone equality comparisons, e.g. `frozenCheckerAndSourcePinsCount == 23` in the preview or `sourcePinCount == 23` in the new manifest, are not type-strict. The isolated readback replay **ACCEPTED `23.0`** in place of manifest `23`; Python dict equality can also equate false historical flags to numeric zero in an independently supplied object. This does not undo F-06, authorize a run, or bypass the pinned original preview on initial staging. Consider explicit types for any future security/evidence-bearing schema fields and add a small regression without broadening the task.

## Independently reproduced refusal cases and hosted CI

**Personally executed, non-native:** Downloaded and hashed the three ZIPs; tested all member CRCs; compared actual PR31 raw reference against staged reference; recomputed canonical seal, staged SHA-256 and Git-blob identities; recomputed the historical physical static error with exact rational arithmetic. In a temporary isolated copy of the real CI staged files, replayed the pinned `verify()` predicates with a separately implemented reference canonical check: authentic baseline ACCEPT; edited `model.mo`, `study.json`, `SimHeat.mo`, reference bytes, extra `build.mos`, missing study, incomplete state, simple native permission forgery, unknown command, alternate seal and historical success forgery all **REFUSED**; the four readback exceptions above **ACCEPTED**. These are *isolated predicate replays*, **not** a claim of importing/running the full source repository in my local Python environment or running native code.

**Hosted source-executed evidence independently inspected:** [CI #44024037373](https://github.com/physicsvigilante/sim_heat/actions/runs/44024037373), `push`, `run_attempt=1`, exact SHA/tree, completed **SUCCESS**, single successful offline-only job `133839981239`. Its actual artifact logs contain **16 staging + 15 strict-type/preview + 11 approved-consumer + 8 binding + 9 archive + 149 frozen-H1 = 208/208 offline test methods PASS**. Original 14/14 frozen-file SHA check lines are `OK`, and the 23-source-pin binding is exercised by the approved offline audit/tests. The seven native/approval CLI spellings `execute`, `build`, `launch`, `native`, `approve`, `reserve`, `run` return invalid-choice refusals. The workflow is full-branch-push-triggered (no paths filter), `contents: read`, `persist-credentials: false`, pinned GitHub action SHAs and a data-only artifact. Its concurrency group is only a CI scheduler, **not** a native reservation.

The earlier [CI #44023899014](https://github.com/physicsvigilante/sim_heat/actions/runs/44023899014) at `8a7507e0a140f25d4a62a001e2589effecaba6be` remains **FAILED**. I checked its job log and saved 16-method test output: three failures arose because expected refusal-message regexes mismatched the **actual** fail-closed exceptions (extra file, missing file, incomplete state). New HEAD amended the test expectations and reran the suites successfully. **Do not reinterpret the prior failed CI as successful.** It is likewise not a new Modelica/physics failure.

Historical F0 `hotLead.G` stayed **FAIL**: originally sealed `0.44999999999999996` W/K vs physically exact `9/20` W/K, independently computed absolute error `4.4408920985006264e-17`, only **80x** below the unchanged native allowance, not mandatory **100x**. The saved V2 `0.45` is **320x** on this scalar, without repairing the original F0 attempt. PR #32 cross-host original-seal regeneration failure remains **FAIL**, alternate `c30e...` is not accepted; no new 85-digit scientific recheck was performed. Original nine requested native readings still have no actual native observations.

## Separate scope judgments

| Dimension | Verdict | Basis |
|---|---|---|
| Original source interpretation and four input byte identities | **PASS (scoped)** | Cross-tree original preservation; exact staged SHA-256 and PR31 original byte equality |
| Physical/numerical correctness | **UNCHANGED / LIMITED** | Frozen physics untouched; original F0 80x failure remains; V2 archived math seal verified, not newly recomputed to 85 digits |
| Native execution and nine observable readings | **NOT RUN / NOT AUTHORIZED** | No OMC, compiler query, build, MAT/CSV or native output; disabled plan incompatible with `native_batch/1` |
| Evidence provenance/readback | **CHANGES REQUESTED** | F-01/F-02 demonstrate metadata/plan ambiguity in readback despite correct staged input hashes |
| Teacher-facing visualization | **NOT TESTED** | No viewer change |
| Textbook answer completeness | **NOT APPLICABLE** | This is input-data staging only |

## Minimal correction/re-review and mandatory native safeguards

For this **offline-only** PR: fix F-01 duplicate-key rejection and F-02 independent pinned-preview validation; add focused on-disk regressions, retain the current verified SHA/data, rerun all relevant exact-head offline tests and publish a **new commit/CI artifact**. Fix or explicitly scope/document F-03 attempt/symlink behavior before using receipts as provenance; address F-04 in the same bounded pass if simple. A targeted independent review of those corrections suffices unless evidence semantics change again. **Keep PR #37 draft/unmerged.**

Even a corrected offline staging PASS cannot authorize native execution. Still missing: owner-authenticated, fresh, protected/signed or equivalently verifiable release/reference root **and durable backup**; separately reviewed source and non-regenerating runnable adapter/plan pinned to exact commit/tree/input hashes; **actual** trusted host identity, executable hash, OpenModelica/MSL/compiler/runtime dependency attestations (planned toolchain strings are not observations); robust fail-closed across-run **atomic one-shot reservation** with crash/partial-evidence preservation and no retries; independent pre-native R2; and **a distinct explicit owner approval for a named compiler query/build/launch budget**. After any separately approved actual run, independently verify native MAT/traces/timestamps, 37 required exports, four integrals, energy checks, all nine public readings and unchanged numerical tolerances. No `reference.prepare` fallback, historical relabeling or PR32 alternate reference substitution is permissible.

**Final verdict: CHANGES REQUESTED for the current R2 offline staging/readback contract; authentic scientific input staging and targeted PR #36 numeric hardening are verified, but a fully defensible completion receipt still needs the bounded corrections above.**
