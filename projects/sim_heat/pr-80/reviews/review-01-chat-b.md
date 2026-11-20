# SIM_HEAT PR #80 — independent Chat B R2 review-01

**Verdict: CHANGES REQUESTED** (one reproduced, bounded **source-evidence provenance** blocker in the directly callable N12 staging helper). The **normal `prepare()` pipeline and actual hosted packets** passed the checks described below. The defect is **not** an OpenModelica/native-runner bypass, a demonstrated mathematical error in the legitimate source-only candidates, or permission to adopt a reference. Keep PR80 draft/unmerged.

**Review date:** 2026-11-20. **Reviewer:** Chat B, separate conversation, original source/CI inspection and separately executed offline checks. **Scope:** N12 three-case source-only staging and evidence semantics, **not** native execution, a protected owner certificate, N3 implementation, OpenModelica qualification, first-author private hidden scoring, release, or deployment.

## 1. Exact pinned object and CI provenance

| Identity | Independently verified |
| --- | --- |
| Source repository / PR | [physicsvigilante/sim_heat PR #80](https://github.com/physicsvigilante/sim_heat/pull/80), **open, DRAFT, unmerged** |
| Exact source HEAD | **`aef1efe599cae31f6ee4b114b1a3051325732bfb`** |
| HEAD Git tree | **`eba28a02b5cc1855e96403c1284c104cddd6addc`** |
| PR79 reviewed successor base | **`ca5654a789f2291d6f0ceb7fd798b15d4310a122`** (base tree `b46db61581fa44da44a6efe8deda960d4c558094`) |
| GitHub synthetic PR checkout | **`6810feaa6149290309d53956a6b687055a624c0e`**, parents exactly `ca5654a...` and `aef1efe...`, **same tree** `eba28a...` |
| [Hosted workflow run #44723343960](https://github.com/physicsvigilante/sim_heat/actions/runs/44723343960) | pull_request, head `aef1efe...`, attempt 1, completed **SUCCESS**; job `136244422829` |
| Hosted artifact | `14623071581`; **independently downloaded and SHA-256 rehashed** `5eba7e9fa5f298b845c37c70480bbc997117bf4eb8d2dc367c7976787279e035`, identical to GitHub-reported `sha256:` digest |

The exact base-to-HEAD comparison is **four additions only**: `.github/workflows/h1-n12-triple-stage-ci.yml`, `qualification/h1_n12/README.md`, `qualification/h1_n12/stage_reference.py`, and `qualification/h1_n12/tests/test_stage_reference.py`. **Zero prior paths changed.** In particular, first-author `model.mo` / `study.json`, H1 parser, Modelica, N1–N11, N3 planning, legacy `reference.prepare`, native infrastructure, C1 and archived diagnostics were not changed in this PR. The source branch is four commits ahead of the base, zero behind.

From the **downloaded hosted artifact**, I safely extracted `source.tar` to separate scratch and used local Git object construction (`git add -A -f; git write-tree`) to reconstruct tree **`eba28a02b5cc1855e96403c1284c104cddd6addc`**, independently matching the GitHub HEAD and synthetic checkout trees. This is stronger than trusting a source archive's name.

The hosted logs report separately executed suites of **8+13+6+6+18+13+13+11+15+12+16+17+34+152 = 334 passing Python test methods**, including **8 new N12** tests; documentation parity also passed. The workflow invoked N12 preparation **twice** as separate Python processes in `prep-A` and `prep-B`, then executed an explicit recursive **10-file equality check**. I *personally* opened all ten files under each artifact directory and compared their bytes **10/10 identical**, including all six model/study snapshots, three candidate payloads, and stage receipt. Neither this review nor the hosted workflow ran OpenModelica, native build, or native simulation.

## 2. Source interpretation and real H1 admission — PASS within offline scope

I independently compared the [original public selector T1-T task](https://github.com/physicsvigilante/sim_heat/issues/58#issuecomment-6981681502) with the exact frozen original `model.mo`, `study.json` and independent `reference-facts.json`. The model encodes **two thermostat nodes (367 K and 289 K), three finite-storage bodies, ten rods (including T06 with diameter 0.016 m, not radius), two ownerless junctions and exactly seven physical port partitions**. The 18 authored `connect()` statements reproduce the original port-a/port-b orientation and junction membership. All **41** given numerical physical slots match (two boundary temperatures, three body triples, ten rod triples); the original study has all **41** slot-provenance records plus an `@model` regime assumption, and the **eight** original requested identities, including the signed T06 and T10 flows and ordered temperature difference. All input/provenance attributions correctly identify illustrative values, **not** textbook givens. No new heat transfer, capacity, geometry, or law was introduced.

The original-source pins are:
- model SHA-256 `2c60e40f1ad8d85f46968f03712d23e8cd6b9c656cf609a38a97d198d0873ae`;
- original study SHA-256 `12ad51f59d2bd6c6561d4059f68b4263e7d4e39cdf5493f353a7affee6929d2a`;
- independently expressed source facts SHA-256 `39f18db09fa618bc73bbe75ca40f33d41ded70a1c73865b2a0e376973d9adfbf`;
- unchanged N3 plan **Git blob** `357a7cd92576b04bbb256ad2728633ebf92149af`;
- unchanged, previously R2-scoped-reviewed N11 module **Git blob** `c136e77d4cea69a1c1d0fa1157f80e3a5013bf9e`. Blob SHA-1 is a *Git object identity*, not a second source SHA-256 or owner signature.

I separately ran the eight N12 unit tests from the actual artifact source tree: **8/8 PASS**. The `three_studies()` transformation preserves the **exact primary study bytes** and changes **only** id / analysis for the two companions, as required by frozen N3 `runDefinitions`. With the **unchanged** `h1.study.load_study`, primary, tight and dense are independently source-admitted and each original request remains **`not_computed`**. Study descriptors and hashes inspected in the hosted packets:

| Role | Study ID / distinguishing analysis | Saved times | Exact descriptor SHA-256 |
| --- | --- | ---: | --- |
| primary | original `H1T1TFirstAttemptV1`; DASSL 1e-8, 2400 intervals | 2401 | `12ad51f59d2bd6c6561d4059f68b4263e7d4e39cdf5493f353a7affee6929d2a` |
| tight | `H1T1TFirstAttemptV1_N1_TIGHT`; DASSL 1e-10, 2400 intervals | 2401 | `e7effca1fcd6e858fdeb19ba8e623780ffb5ef52aed669751f74e9d78c8e9758` |
| dense | `H1T1TFirstAttemptV1_N1_DENSE`; DASSL 1e-8, 4800 intervals | 4801 | `5f4b4bdc335a5a876de3d9d642f06c85ffe5b8499af9f892437c5be6ca3ce350` |

These are *three distinct H1-admitted study inputs*, not three native solutions. The **physical source model bytes are identical** in every case. Primary and tight candidate **grid, units, all 77 exported series, all eight requested reference series and all five signed integrals** are byte-equivalent as parsed data, as appropriate for a shared ideal physical target independent of future DASSL tolerance. No claim of improved native solver accuracy follows.

## 3. Mathematical proof and staged-data identities — PASS for the authentic `prepare()` path

I independently ran the **actual `qualification.h1_n11.rational_dynamic_proof.audit()` offline** from the downloaded, exact-tree source. It reconstructed the original N1 traces and obtained:

- **2400-interval original trace SHA-256:** `b13877c8d069a60928cf3b23ae007b1a10feb53151f00ffb65a57082a7fc10af` — 2401 × (77+8+5) = **216,090** source-physical budget comparisons.
- **4800-interval original trace SHA-256:** `9ba71a1d2fccb39be071df0647793f6fb844737e2ac9c91bb143546ab8d26b40` — 4801 × 90 = **432,090** comparisons.
- **Total: 648,180**; canonical **N11 mathematical receipt SHA-256:** `ea7d3dcf841811778a19673fdc34c44041ec8bcdbb7434feabc7d60f074544a8`, independently matching both hosted stage receipts. All native/bundle certification fields remained false.

The unchanged N11 audit enforces the original source interpretation, outward rational enclosure and original N9 static checks, exact grid times and signed flows, all original 77/8/5 labels and physical budgets. This is **source-only mathematical checking**, not an external mathematical certificate or OpenModelica result. The earlier [N11 PR78 independent SCOPED PASS](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-78/reviews/review-01-chat-b.md) has its own bounded scope; N12 does not promote it to owner authority.

I compared the hosted stage receipt to all three canonical candidate payloads, their precise descriptor/model/source-facts hashes and their **actual JSON bytes**:
- primary packet `5a2712f49bd1032b7dea7ac7d210d69f17b132035416247c779c8f98edac12d4`;
- tight packet `53101969a460b232ce47822d6782e93dfd43a5d46ac0c40999a1a186d4fcc8e7`;
- dense packet `d2743134eb5b452dda8dfa21a1de14ca7493e252e1b6e8d70f949ad5b552ca59`.

All 3 × (77/8/5) inventories and all 2401/2401/4801 lengths were present, plus separate SHA pins. The hosted `original-native-hold.json` attests **zero native calls**, `nativeExecutionReady=false`, `referenceAccuracyCertified=false`, **eight open native blockers**, and the preserved **seven original legacy static 100× errors**: `T02.G`, `T06.A`, `T06.G`, `T07.G`, `T08.G`, `T10.G`, `T_Plug.C`. These were verified directly from artifact data, not repaired or reinterpreted as passes.

## 4. F-01 — BLOCKING: direct `stage_packet()` can launder caller-controlled evidence into a source-verified origin label

**Location:** [`qualification/h1_n12/stage_reference.py` lines 149–220](https://github.com/physicsvigilante/sim_heat/blob/aef1efe599cae31f6ee4b114b1a3051325732bfb/qualification/h1_n12/stage_reference.py#L149-L220), notably the direct `stage_packet(role, study, trace, trace_blob, proof, proof_sha)` boundary and its emitted `origin`. **Reproduced in separate local scratch, with offline Python only.**

The direct helper checks `sha256(trace_blob)` against the **real pinned** N1 trace digest, but then **copies `trace["columns"]`, `trace["units"]`, `trace["requests"]`, `trace["integrals"]` and `trace["grid"]` from a separately supplied dictionary**. It never establishes `trace == json.loads(trace_blob)`. It checks only report flags / inventory counts, not the original data/units. The `proof` object is also supplied by its caller, and `digest(canonical(proof)) == proof_sha` checks a **caller-created self-digest**, not actual execution of `n11.audit()` or a protected expected receipt. The helper further does not pin or H1-admit the supplied `study` against the selected role.

**Actual adversarial reproduction:** I generated the **real original N1 2400-interval trace** with the correct `b13877...` byte SHA; retained that authentic `trace_blob`; altered a distinct in-memory `trace` dictionary so `T06.Q_flow[0] = 987654321.0`, its unit became **`J`** instead of `W`, public `t_collar_to_plug[0] = -987654321.0`, and signed `T_Collar.Q_in` integral entry changed. I supplied an invented **minimal** N11-shaped proof with `individualPhysicallyEnclosedSamples = 648180`, boolean claims and source pins, **no `grids` evidence**, plus its self-computed digest `4f1da37b5a54aca4a8a54edd59674d58b2c6d43186acb21f19796d18014abfda`. I requested role `tight` with the **original primary** study bytes. `stage_packet()` **accepted all of it** and emitted:

- the *authentic N1 trace SHA* beside data and a unit **not present in those trace bytes**;
- the *invented N11 proof self-digest* as `originalN11ProofReceiptSha256`, despite no underlying audit;
- `role="tight"` with original `studyId="H1T1TFirstAttemptV1"`;
- `origin="SHA_VERIFIED_ORIGINAL_SOURCE_ONLY_N1_WITH_SEPARATELY_REVIEWED_N11_MATH"`.

This is a **real inaccurate source/evidence-origin assertion** when the helper is called directly, even though its output still correctly has `nativeQualified=false`, `runnerConsumable=false`, `referenceBundleWritten=false`, etc. The same defect allows missing/extra field labels of the same total count, reversed flow signs and unit substitutions at this direct-helper boundary. The new N12 tests cover a *wrong blob digest*, but not an **authentic blob with a divergent data dict**, nor a **self-hashed fabricated proof** or role/study mismatch.

**Scope and impact:** I found **no bypass of the genuine `prepare()` CLI in its examined path**. It calls `n11.audit()` itself, regenerates and N9-verifies both original N1 traces, passes `json.loads(blob)` from the same trusted bytes, H1-admits the derived studies and rechecks pinned sources before staging. The actual hosted artifact packets passed independent verification. **No legacy/native runner can consume this new schema or exercise this helper as a native permission gate.** The defect is nevertheless material for an R2 milestone whose output is presented as **source-verified evidence**, because the public top-level helper can manufacture the same candidate schema and provenance label without satisfying those preconditions. It must be fixed or explicitly de-authorized before a **SCOPED PASS on N12 evidence semantics**.

**Required narrow correction:** Either (preferred) make `prepare(out)` the **only authority-bearing staging entry point** and move packet construction into an unexported/private verified-context path, **or** make direct packet construction enforce the identical content bindings: parse and validate the **supplied pinned trace bytes internally**, verify actual original labels/units/series instead of trusting a disjoint `trace` object, bind actual N11 proof to a freshly executed source-pinned audit (or do not assert it), and require the exact admitted role/study identity. A self-selected SHA-256 digest alone is **not** owner or mathematical proof authority. If retaining a raw composing helper, label its product explicitly **unverified**, remove the `SHA_VERIFIED...N11_MATH` origin claim at that boundary, and prevent it from producing a packet indistinguishable in schema/authority claims from genuine `prepare` output. Add narrowly targeted regression tests: good blob + bad data/units/flow signs, fake self-digested proof, missing proof grids, mismatched study role/model/provenance, original-source change before final writing, and native flag/schema refusal. Do not repair the old runner or adopt an N3 certificate as a shortcut.

## 5. Authority/refusal boundaries and residual limits

The **actual hosted** N12 candidate schema is exactly `sim_heat.h1_n12.source_only_three_case_reference_stage/1`, **not** current `sim_heat.reference_bundle/2` or future `sim_heat.h1_n3.reference_bundle/1`. Candidate files contain **no `seal`, `semanticSeal`, native allowances, trusted toolchain/host manifest, protected pre-output expected digest, owner signature or single-use lease**. `referenceBundleWritten`, `runnerConsumable`, `referenceVersionAdopted`, `externalOwnerApprovalVerified`, `nativeAttemptAuthorized`, `nativeExecuted`, `nativeQualified`, `runtimeReady` are all false; its stage receipt also keeps `runPermissionGranted=false` and eight native blockers open.

The **full `prepare()` path** refuses an existing/in-repo target before proof, verifies pinned original/model/facts and frozen N3/N11 code identities, validates three H1 study sources, reruns N11, N1 and N9 and re-reads protected inputs prior to first stage write. Original inputs and C1 remain untouched. The eight existing focused N12 tests passed personally and in hosted CI. Those protections do **not** cure the independent direct-helper defect above, and do not establish a hostile concurrent-filesystem race-free guarantee after the final re-read. No external owner attestation, native output, runtime version/OMC/MSL identity or new source composition qualification exists here. Do **not** interpret source digest or two-run determinism as an authenticated prospective checking reference.

**Review execution limitations:** I independently ran **8 N12 tests**, the real N1 primary generator and the **full N11 offline audit** with original SHA identities; I independently inspected and byte-compared both **hosted** stage directories and rehashed the ZIP; I did **not** rerun all 334 hosted test methods, run OpenModelica, independently recalculate every 77-channel time history from another physics derivation, certify future N3 solver tolerances, or certify an actual native run. No source, historical evidence or runner files were edited on GitHub.

## 6. Disposition

**CHANGES REQUESTED on exact HEAD `aef1efe...` / tree `eba28a...`.** Preserve this original CI run, its artifact and its honest green results, and preserve the existing seven historical failures and eight native holds. Do not merge, deploy, execute OMC or adopt a reference. Fix **F-01 only** with targeted negative tests and a new pinned head/CI, then request a **targeted Chat B R2 re-review** of the changed provenance boundary. No broad reopening of the unchanged N11 mathematics is necessary unless the fix changes it. Source publication/merge remains a separate owner decision even after review.

**Primary reviewed materials:** [PR80 REQUEST](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-80/REQUEST.md), [pinned N12 source](https://github.com/physicsvigilante/sim_heat/tree/aef1efe599cae31f6ee4b114b1a3051325732bfb/qualification/h1_n12), [CI run](https://github.com/physicsvigilante/sim_heat/actions/runs/44723343960), [N11 source](https://github.com/physicsvigilante/sim_heat/blob/aef1efe599cae31f6ee4b114b1a3051325732bfb/qualification/h1_n11/rational_dynamic_proof.py), [N3 migration contract](https://github.com/physicsvigilante/sim_heat/blob/aef1efe599cae31f6ee4b114b1a3051325732bfb/qualification/h1_n3/migration-plan.json), and [original selector T1-T](https://github.com/physicsvigilante/sim_heat/issues/58#issuecomment-6981681502).
