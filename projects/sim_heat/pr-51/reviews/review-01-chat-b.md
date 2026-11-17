# SIM_HEAT PR #51 — Independent Chat B review 01

**Outcome: CHANGES REQUESTED — scoped R2 review.**

The principal corrections work, the exact-head hosted evidence is genuine and consistent, and all six original published bundles replay unchanged. One independently reproduced omission remains: the steady and campaign adapters still accept Boolean/floating-point substitutions in integer-valued MAT/CSV provenance and case sample counts. This is a residual gap in the requested cross-adapter strict-type audit, not evidence of corrupted authentic archives or a new physical/numerical regression.

## Identity, scope and independence

| Item | Reviewed identity |
|---|---|
| Source repository / PR | `physicsvigilante/sim_heat`, [PR #51](https://github.com/physicsvigilante/sim_heat/pull/51) |
| Exact reviewed head | `52d693a748ad3709c99215bac0a5840a236937a6` |
| Exact reviewed tree | `7dcbb52c40f5b431ccdfe5dd4d2329fa21463829` |
| Base | `c06fb5395781482bd6bbe055d10bc10cdf3bba8d` |
| Diff | [Exact base-to-head comparison](https://github.com/physicsvigilante/sim_heat/compare/c06fb5395781482bd6bbe055d10bc10cdf3bba8d...52d693a748ad3709c99215bac0a5840a236937a6) — one commit, 11 paths, seven modified and four added |
| Reviewer | Chat B, separate review conversation; GPT-6 Astra Pro |
| Evidence close | 2026-11-17 19:43:27 UTC / 2026-11-18 01:13:27 Asia/Kolkata |
| Risk / scope | R2: shared JSON admission, generic junction identity, archive/report consistency, strict Boolean/integer semantics, external archive identity and preservation |
| Source changes by reviewer | None in SIM_HEAT. Only this new independent report is published to `review_sandbox` |
| PR state at final identity check | Open, draft, unmerged; still at the exact reviewed head |

Read the [central request](../REQUEST.md), central protocol/risk policy/template, pinned project instructions, H1 implementation contract and offline amendment, C1 freeze boundary, changed-source material and relevant parser/checker/decoder dependencies. The developer audit and PR narrative were treated as claims to check, not an independent verdict. This is independent review context, not independent human authorship, independent model weights, or a new scientific reference certification.

PR50's separate schematic fix is excluded. This report applies only to the head above; a successor needs its own scoped disposition.

## F-01 — Remaining integer-type coercion in steady/campaign provenance

**Severity: major within this evidence-integrity acceptance scope; bounded operational impact. Category: strict schema/provenance consistency. Confidence: high, executed against exact production module bytes. Required correction, not an optional refactor.**

Locations at the reviewed head:

- [Steady adapter, lines 121–125 and 140–146](https://github.com/physicsvigilante/sim_heat/blob/52d693a748ad3709c99215bac0a5840a236937a6/viewer/network/tools/build_steady_case.py#L121-L146).
- [Campaign adapter, lines 118–121 and 142–148](https://github.com/physicsvigilante/sim_heat/blob/52d693a748ad3709c99215bac0a5840a236937a6/viewer/network/tools/build_campaign_case.py#L118-L148).

Both paths use loose numerical equality for `item['canonicalSamples']`, `provenance['samples']` and `provenance['duplicateRowsCollapsed']`. Consequently `True == 1`, `1.0 == 1`, `2.0 == 2` and `1001.0 == 1001` still admit the wrong JSON types. Complete serialized receipt/report comparisons do not cover these separate metadata objects. The transient adapter already explicitly checks the corresponding types.

### Independently executed results

Each row is a separate mutation of an authentic archive copy. Member hashes and the test-only outer ZIP hash were recomputed; original archives, MAT/CSV bytes and saved checking references were not changed.

| Changed field | S1 steady result | D2_K2 campaign result | Expected |
|---|---|---|---|
| `mat_provenance.json: duplicateRowsCollapsed = true` | Accepted | Accepted | Typed refusal |
| `mat_provenance.json: duplicateRowsCollapsed = 1.0` | Accepted | Accepted | Typed refusal |
| `mat_provenance.json: samples = 2.0` / `1001.0` | Accepted | Accepted | Typed refusal |
| Selected `attempt.json` case: `canonicalSamples = 2.0` / `1001.0` | Accepted | Accepted | Typed refusal |

Equivalent D1 transient variants were refused. The accepted steady/campaign outputs remained `diagnostic_only`, `nativeQualified=false`; output fields derived from the decoder or literal integers concealed the malformed input type rather than exposing it as an error.

### Reproduction

Use this exact source head and original artifacts `14204656273` (S1) or `14153251022` (D2_K2). First establish a successful unchanged replay using the separately verified identities below. Work only on a new, explicitly test-only repack.

For S1, the selected attempt prefix is `h2_s1_native_successor_attempt/`; for D2_K2 it is `batch_1/`. In either case select `case_01`. Change only one field from the table. For a provenance-file mutation, serialize that changed JSON and update its relative `case_01/mat_provenance.json` SHA-256 in the selected attempt's `artifactSha256`. For a case-record mutation, change only the selected record inside `attempt.json`. Preserve all other member bytes, write the changed attempt, and ZIP the same member names into a new test file. Supply that test file's recomputed outer SHA to the appropriate adapter, retaining the original run/commit inputs and, for campaign, branch `experiment/h1-cloud-resolution-once` and batch/slot `1/1`.

At this head, these calls return a case instead of raising `Refusal`. Supplying the authentic original ZIP SHA instead correctly refuses every repack. Thus this finding concerns **internal evidence admission after a supplied hash has matched**, not a cryptographic bypass, forged GitHub attestation, altered original artifact or false native qualification.

### Required correction and regression

Require `type(value) is int` for all three fields in both adapters before their existing numerical equality checks. Do not use `isinstance(value, int)`, which admits Boolean values. Retain the existing expected counts/grid checks, exact serialized reports, reference pins and external identity requirements.

Add cross-adapter regressions covering genuine integer acceptance, Boolean/float rejection for duplicate counts, float rejection for sample/canonical counts, and unchanged replay of all six originals. Use test-only fixtures/repacked copies; never rewrite a historical record to make it conform. No new physical reference, native launch or architectural change is necessary.

This is a residual omission in the touched audit surface, not a newly introduced numerical regression. The PR's narrower statement about changed execution/check counts is supported; it does not resolve these additional strict-type cases requested for review. I require this small correction before endorsing completion of the cross-adapter type-hardening audit.

## What was personally executed

Direct Git cloning was unavailable in this environment. I therefore fetched commit-pinned files through the GitHub connector, materialized the relevant complete Python modules in an isolated review directory, and verified their Git blob SHA-1 values before execution. This was **not** a full repository checkout or a local rerun of the hosted suite. All twelve original case model/study files used locally, and `SimHeat.mo`, were also checked against the exact-head Git tree.

The executed source included these exact blobs:

| Module | Verified Git blob |
|---|---|
| `h1/study.py` | `545fad71c467adf300c01ba357d5fc77d7eb85e0` |
| `h1/model.py` | `791192ecaf2da54db7023070e411641b05c863d7` |
| `h1/verification.py` | `567a326565659da4b844efc26b0314e6994c3f6f` |
| `viewer/network/tools/build_case.py` | `174ce09fef8c25292d7e768a90458d04349deb7e` |
| `viewer/network/tools/build_steady_case.py` | `c2646ae55a44b37207cfeb49c1e1b3387af784ed` |
| `viewer/network/tools/build_campaign_case.py` | `09a8fef730cdb6a1d5285ec777ca706bac2861ea` |

The complete `policy`, `decoder`, `reference` and `temporal` dependency copies also matched their pinned blobs. Local Python 3.13.5, NumPy 2.3.5 and SciPy 1.17.0 matched the relevant hosted versions; nothing was installed for this review.

### Shared JSON admission

Personally exercised nested positive/negative exponent overflow, nonstandard nonfinite constants, escaped/nested duplicate keys, non-object roots, malformed numerical syntax, excessive integer tokens and deep nesting. Malformed probes returned `Refusal` with descriptor semantics. Finite controls retained integer versus floating-point types, maximum finite float, subnormal values, Boolean/null values and signed zero. A 4,300-digit integer remained an integer; a 4,301-digit token refused. All six original studies still admitted.

**First-attempt correction retained:** my first extra depth probe incorrectly expected a 2,000-level JSON array to refuse; the parser accepted it and my assertion failed. The implementation does not promise a fixed 2,000-level limit. Subsequent 10,000- and 20,000-level probes produced typed refusals. The first result is a reviewer expectation error, not a demonstrated parser defect, and is not hidden or counted as a passing test. I make no exhaustive fuzzing claim.

### New collision composition

Authored a new parser/topology test, rather than merely replaying the added fixture. An ownerless first node connects `aaa.port_a` with `bbb.port_b`; two later/isolated Body components reserve `junction_0` and `junction_0_1`, and a rod reserves `junction_0_2`. The graph correctly generated `junction_0_3`, retained distinct owners and had no false self-loop. Reversing declaration and connection ordering produced the same graph. All six original published graphs were also preserved by complete bundle replay.

### Original replay and adversarial archive checks

Personally downloaded, hashed and CRC-checked all five original ZIPs, then invoked the exact adapters for all six published cases. Both SHA-256 and Git blob identities of the resulting bundles match the pinned catalog/tree.

During replay and mutation checks, `reference.prepare`, `reference.calculate` and subprocess creation were patched to raise immediately if invoked. No such call occurred. Replaying the saved checker is not regenerating its analytical reference and not running a native binary.

Across **54 separately repacked test probes** spanning D1, S1 and D2_K2: **43 refused**, **three unchanged-content repacked positive controls accepted**, and **eight malformed-type variants accepted**, establishing F-01. Refused variants included numeric substitutions for saved Boolean flags, a false check under a success label, changed public values, missing manifest entries, failed preflight records, float check counts, Boolean/float execution counts and mismatched external run/commit inputs. There were no uncontrolled exceptions in this 54-probe set. Every one of the 54 repacks was also refused when presented against its original trusted ZIP hash.

The repacked positives are controls, not newly authenticated native artifacts. No original artifact was overwritten.

## Exact-head hosted evidence — inspected, not personally rerun

[Push CI run 44148890246](https://github.com/physicsvigilante/sim_heat/actions/runs/44148890246), attempt 1, and job `134271418151` are successful at the exact reviewed head. I independently inspected GitHub run/job/artifact metadata and the downloaded artifact, rather than relying on PR text.

[Artifact 14358266358](https://github.com/physicsvigilante/sim_heat/actions/runs/44148890246/artifacts/14358266358): **5,873,728 bytes**, **33 unique CRC-valid members**, SHA-256:

`c0acc90ef3153625e4f480201d12a6ab43d79bfff433d2cd546fe1d22d746282`

My computed digest matches GitHub's artifact digest. The artifact's `head-sha.txt` and `head-tree.txt` match the requested head/tree; its source-change receipt matches the eleven-path diff. The workflow uses failure propagation and separately records test, archive-replay and browser steps; it contains no OpenModelica execution step.

| Hosted evidence | Verified result | Reviewer classification |
|---|---|---|
| `h1.log` | 152 passed | Inspected hosted log, not locally rerun |
| `arithmetic.log` | 4 passed | Inspected hosted log, not locally rerun |
| `adapters.log` | 54 collected: 53 passed, 1 skipped | Inspected hosted log, not locally rerun |
| `node.log` | 31 passed | Inspected hosted log, not locally rerun |
| Total | **240 passed, one skipped, zero failures** | Not 241 passes |
| Original archive replay | Six published bundles byte-identical | Inspected hosted results and personally reproduced separately |
| Saved comparison index | Unchanged | Hosted output personally rehashed against pinned Git blob `f70e4f077bb1dff6b6163bb1770fe4515bd44903`; builder not locally rerun |
| Full explorer Chromium smoke | PASS | Inspected successful job step, browser log, test source sections and selected screenshots; Chromium not launched by reviewer |

The optional skip is `test_optional_original_native_archive_and_fully_rehashed_test_only_mutants`, whose optional original archive environment input was not supplied at that unit-test step. The developer's separately reported local pass is **not** counted as either a hosted pass or my execution of that named test. My actual-original replay and independently authored mutation probes are separate evidence.

The retained browser artifact contains 21 PNGs. I visually inspected `refusal.png` and `whatif-desktop.png`: refused source data clears the displayed graph/values/history/provenance, and the comparison shows saved native histories with explicit diagnostic limits and no interpolated-physics claim. The hosted smoke source/log covers case switching, transient/steady behavior, saved-time controls, CSV/import races, comparisons and desktop/mobile views. The final PASS occurs after the script's assertions and page-error check. This supports that hosted smoke, not cross-browser/accessibility/classroom qualification. The developer's earlier locally blocked navigation attempt remains a failure, not a retrospective pass.

## Independently checked original archive custody

GitHub's workflow-run artifact metadata independently bound each original artifact ID, size/digest and source head to the run below. These match the locally downloaded bytes and internal identities. Caller-provided identity strings alone would not establish this.

| Cases | Run | Artifact | Original source commit |
|---|---:|---:|---|
| D1, D2 | 43691263273 | 14152886226 | `1b68b14dd05c5eb8f148b02055890563cdc32095` |
| DEV_BRIDGE | 43699424883 | 14155084346 | `b3779603563db4b26aeef8c2dd552965698deb4f` |
| S1 | 43820600508 | 14204656273 | `337ef554fb40da9408485bda8f2a4024c84720f6` |
| TEACH_RING4 | 43845664024 | 14215520616 | `39b2067c9b6ea5f903dc4c360a78241b24df7c09` |
| D2_K2 | 43693191224 | 14153251022 | `52b1635932a3e4519b91f3bf093c0c21b0248d91` |

Original ZIP SHA-256 values, personally recomputed:

```text
14152886226  8fc38b9e2f040b48ab5cbeab34e8698b7c99c4d462a1e31e8bc33b0395185379
14155084346  f16975a25eea79f61f7819fb9e704ab04a33630044a51a0d062b8399c1c9ce38
14204656273  82b4a87b66e0022d582da931253649b3829f6633119a57081c02dc253dc5dbd9
14215520616  0bc1433be66df2827f8907d100ca264f6a721fe8ad40644b962500b97fa9b8b2
14153251022  dc32a0a36a27f031ce7a13da83ebdd26a3dd6ac1d14612fa597b36cb439f4843
```

Personal original-replay bundle SHA-256 values, matching [the exact-head catalog](https://github.com/physicsvigilante/sim_heat/blob/52d693a748ad3709c99215bac0a5840a236937a6/viewer/network/data/index.json):

```text
D1          49c605d5a23da7d521da6c8db186dbd2d435facb60c31289822322e20a6dfebf
D2          c0fc143db30278898d13340faa7f60baf62185b40296767a6114e359d3c705ea
DEV_BRIDGE  07dbe0987b99c89d9a20f0a1317b3699cddbf85186dcee3ae71d6d0005c364d8
S1          eacab37b499a47c094cbd642acfee269a1bea7c82d16b15b9217a8c13ef1e4e7
TEACH_RING4 b4f46b2953409980ea5d5ed1b41cafaf5a7504003da44038d9d51286bb6e8a34
D2_K2       a057e076aa31971c82509b70566892f9be60850046231104feac5d9e6365748b
```

The adapters check agreement with external identity inputs; they do not contact GitHub or authenticate an arbitrary repack. That boundary is correctly documented. The transient adapter's required keyword/CLI identity inputs and wrong-run/wrong-commit refusals close the identified self-description gap without creating a signature scheme.

## Preservation, dimensions and release advice

The exact diff changes no physical component equations, original model/study files, reference specifications or payloads, published case/catalog/comparison data, numerical thresholds, native runner or historical execution plans. Current `h1/study.py` does change; old source-pinned plans must therefore refuse it. The resolution-test patch adds the new parser only to temporary scratch fixture repinning and adds a historical-plan rejection regression. I inspected that patch and its hosted test evidence; I did not locally execute that historical-plan test.

| Assessment dimension | Scoped conclusion |
|---|---|
| Source interpretation | Preserved, not newly re-certified. No new PDF interpretation or textbook constants were adopted by this review. |
| Physical/numerical correctness | No physical-law or allowance change. Full saved checker reports replayed consistently on originals; no new independent reference-accuracy certification. |
| Composition/authorability | Generic name allocation passed an unfamiliar valid collision composition and order permutation. This is offline graph evidence, not a new native composition qualification. |
| Simulation coverage | Six historical diagnostic cases retained. No additional native trajectory or export mechanism established. |
| Evidence integrity | Manifest/report and external-identity corrections supported; F-01 prevents complete cross-adapter strict-type acceptance. |
| Teacher usefulness | Existing explorer/comparison functionality supported by hosted smoke and selected visuals. No teacher usability study or classroom validation performed. |
| Textbook-answer completeness | Unchanged and not established by this corrective PR. |

C1 remains a separate qualification boundary. The recorded original 80× versus required ≥100× precision failure and later exact saved-reference reproduction failure are not converted into passes. No C1 reference was regenerated; no uncomputed C1 native value became computed; main's archived diagnostics are not C1 transfer qualification. Historical failures and PR50's separate review are preserved, not reopened or merged into this verdict.

**Release advice:** make the narrow F-01 source/test correction, retain original evidence and published bytes, and obtain a scoped successor review with its exact-head offline evidence. Do not merge this head as completion of the strict-type audit. No new native run is needed to resolve this finding. No merge, deployment, new native authorization, reference adoption, reference regeneration or scientific qualification is granted by this report.
