# Chat B — independent implementation and physics review of Opticsim PR #133

**Date:** 2026-11-18 (Asia/Kolkata)  
**Verdict: CLEARED FOR OWNER DECISION — this exact bounded candidate A source only.**

The new implementation is a **conditional, native-free planar apparent-depth calculation**, not an observed image, an eye or pupil, a ray-backintersection engine, or evidence that an original JEE question was interpreted faithfully. The evaluated source is still a draft, unmerged pull request. Clearance is not authorization to merge or release it. The independently reviewed PR #132 D-01 R2 *design* did not pre-approve this implementation.

## 1. Independently checked Git identity and scope

| Check | Independently observed result |
| --- | --- |
| [Draft PR #133](https://github.com/physicsvigilante/opticsim/pull/133) | Open, draft, not merged at final recheck |
| Exact source HEAD | **5dc594400a3c8d537c180d1162379b5bfda5e3b1** |
| HEAD Git tree, read from the Git commit object | **d02d23e598d8211830928414fb5a1ae232d450f7** |
| Synthetic PR merge commit | **d3dda63d6d079048e8b144d89ce6dcd92f8710b2** |
| Synthetic merge Git tree, read separately from its Git commit object | **d02d23e598d8211830928414fb5a1ae232d450f7 — exactly identical to HEAD tree** |
| Production base, also merge's first parent | **d3509e82fb65d81aabe336666851f8f2962623f4** |
| Base Git tree | 45ff3bcd9093a527652f13f76c3cc0b02826642f |
| Base→HEAD comparison | 11 commits ahead, 0 behind; exactly four changed tracked files; +541/−8 |
| Final changed files | Added src/planar-apparent-depth-queries.js (150 lines); modified src/problem-workflow.js (+64/−8); added test/jee-apparent-depth-analytical.test.mjs (289 lines); added examples/jee-apparent-depth-v1.json (38 lines) |
| Historically frozen scripts/run-problem.mjs | **Blob SHA 2efecbf3eddcd9322782cc1667b02fe495fd4fa8 on BOTH production base and final HEAD** |

I checked the actual [HEAD commit object](https://github.com/physicsvigilante/opticsim/commit/5dc594400a3c8d537c180d1162379b5bfda5e3b1), [synthetic merge commit](https://github.com/physicsvigilante/opticsim/commit/d3dda63d6d079048e8b144d89ce6dcd92f8710b2), base-to-head Git comparison, complete changed-file list, and both copies of the frozen CLI blob. The four-file diff establishes that **no tracked native optics, vendor pin, schemas, browser UI, historical frozen scripts or transfer fixtures/tests were edited** in the final source. The final unchanged run CLI still owns byte-preserving evidence, output, hashing and native dispatch.

## 2. Independent optical derivation and numerical checks

Let the point object's normal depth be **d** in index **n_o**, and the receiving/observer-side medium index be **n_r**. Take **i** as the *object-medium incident angle*. For symmetric incident rays ±i and one ideal infinite plane, Snell gives sin(t) = (n_o/n_r) sin(i). Extending the two transmitted lines backward yields

**d_s(i) = d tan(i)/tan(t) = d (n_r/n_o) sqrt[1 − (n_o/n_r)² sin²(i)] / cos(i).**

The near-normal limit is **d_a = d n_r/n_o**. Writing r = n_o/n_r and z = sin²(i), the squared ratio is (d_s/d_a)² = (1 − r² z)/(1 − z), whose derivative with respect to z is (1 − r²)/(1 − z)². Therefore the endpoint construction is monotone inside a transmitting cone: **n_o>n_r** decreases depth with angle, **n_o<n_r** increases it, and equal indices give exact undeviated continuation. This proves a bound **only for the stipulated symmetric-pair construction**, not an actual viewer's angular uncertainty.

I independently evaluated the formula with 60-digit arithmetic (not copied test expected values, and not PhyDemo):

| Real depth; object→receiving indices; object incidence | d_a, mm | d_s, mm | Abs. relative construction difference | Admission |
| --- | ---: | ---: | ---: | --- |
| 120 mm; 1.5→1; 5° | 80 | 79.616366847750477 | 0.4795414403% | Conditional, admitted |
| 120 mm; 1.5→1; 30° | 80 | 61.101009266077867 | 23.62373842% | Refuse: >5° |
| 120 mm; 4→1; 5° | 30 | 28.225297264777272 | 5.915675784% | Refuse: >1% |
| 120 mm; 4→1; 1° | 30 | 29.931368655020573 | 0.228771150% | Conditional, admitted |
| 120 mm; 1→1.5; 5° | 180 | 180.382307315379305 | 0.212392953% | Conditional, admitted |
| 120 mm; 1→1; 5° | 120 | 120 | 0% | Exact equal-index continuation |
| 120 mm; 4→1; 2.084° | 30 | 29.700574640943871 | 0.99808453% | Conditional, admitted |
| 120 mm; 4→1; 2.087° | 30 | 29.699706822624355 | 1.00097726% | Refuse: >1% |

The source's stable square-root product, direct equal-index branch, and formula have the correct signs and index ordering. At the maximum admitted index contrast, 4 sin(5°) = **0.348622970990633 < 1**; the admitted cone cannot approach total internal reflection or grazing within the stated [1,4] index bounds. A 30° request is **outside policy** even when Snell transmission exists. The ≤5° **AND** ≤1% limits are bounded model-admission decisions, **not physical-image fidelity guarantees** or numerical solver error bars.

## 3. Source, typed validation, dispatcher and evidence review

Read the complete final [pure evaluator](https://github.com/physicsvigilante/opticsim/blob/5dc594400a3c8d537c180d1162379b5bfda5e3b1/src/planar-apparent-depth-queries.js), [dispatcher](https://github.com/physicsvigilante/opticsim/blob/5dc594400a3c8d537c180d1162379b5bfda5e3b1/src/problem-workflow.js), [12 new test definitions](https://github.com/physicsvigilante/opticsim/blob/5dc594400a3c8d537c180d1162379b5bfda5e3b1/test/jee-apparent-depth-analytical.test.mjs), [example](https://github.com/physicsvigilante/opticsim/blob/5dc594400a3c8d537c180d1162379b5bfda5e3b1/examples/jee-apparent-depth-v1.json), plus the unchanged run/preflight CLI, method-suitability implementation, JSON guards and historical freeze test.

**API admission.** The exact new request kind is **paraxial-apparent-depth**, and the fact/query/result formats are the D-01 specified opticsim-planar-apparent-depth-*-v1 values. The new kind is registered deterministically in the existing opticsim-problem-v1 route, fact-contract family map, and shared four-analytical-calculation limit. Its request accepts **id** and **kind** only; a component ID, free-form angle override or eye is rejected rather than inferred. Query passed to the evaluator is exactly the format and kind, without the request ID. Capabilities are defensively copied. Old registered families, native observable ownership and method-suitability dispatch remain in their original branches.

**Strict source facts.** The solver checks the top-level facts, object, media and viewing key allowlists; explicitly requires an object normalDepth and bounded stable ID, explicit mm/cm/m unit, indices in [1,4], and viewing.model = paraxial. Unit conversion precedes the **[0.01,10000] mm** real-depth limit. Invalid zero/negative depth, out-of-bounds index/unit, unexpected fields, or wrong scalar type cannot produce a value. A non-paraxial model and other fact formats are unavailable; omitted required physical facts are needs-information through the planner. The positive finite output limit is **50000 mm**, though it cannot be hit from currently admitted depth and index endpoints; the defensive nonfinite/overflow branches should not be presented as independently exercised by these finite fixtures.

**Cone behavior.** Supplying maxIncidentAngleDeg requires a finite number strictly >0 and ≤5; the code computes the endpoint pair and then also enforces **≤1%** construction discrepancy, with **null** value on any refusal. Without a supplied cone, symmetricAngleEnvelope is **null**, and an explicit no-quantitative-bound warning is carried. Equal indices are an exact continuation case. All scalar results are assumption-dependent, not native-qualified.

**Status matrix (source-path verification corroborated by final CI tests):**

| Authored case | Planner/result and public behavior |
| --- | --- |
| Valid A-only, native not requested | conditional scalar; explicit method, assumptions, limitations, warnings and question-fidelity refusal; scene/preparation null; nativeRequests/targetBindings empty; preflight no-native-required; run exit 0 |
| Valid A-only, no cone | conditional scalar, null angle envelope, explicit lack-of-bound warning |
| Explicit cone >5°, or ≤5° with >1% model discrepancy | unavailable with OUTSIDE_PARAXIAL_DOMAIN or PARAXIAL_CONSTRUCTION_DISCREPANCY; scalar null |
| Missing essential fact; malformed/extra fact | needs-information / MISSING_FACTS or invalid-input / INVALID_FACTS; scalar null, native not eligible |
| Unsupported known viewing model or substituted facts family | unavailable with UNSUPPORTED_VIEWING_MODEL or UNSUPPORTED_SCOPE; scalar null |
| Nonfinite or nonpositive derived intermediate (defensive branch) | numerically-indeterminate / UNSTABLE_PARAXIAL_RESULT, null, rather than invented output |
| Valid A-only, verifyNative:true | **calculation stays conditional**, but plan.native required=true, canRun=false; explicit NATIVE_SCENE_REQUIRED diagnostic; preflight **blocked**, exit 2; run report and coverage **blocked-native-verification**, native.status **not-run**, report native reason contains NATIVE_SCENE_REQUIRED, nativeCalls **0**, run exit **2** |
| A plus detector-crossings request with no authored scene | A stays conditional; detector request needs-information and null; no invented apparatus/native call; run exit 2 |

For valid A the planner copies **method**, assumptions, limitations, **qualification** and warnings, native.status not-run, nativeObservation:false, nativeImageDetected:false and interpretation/questionSupport not-assessed-by-engine. The stored analytical-results record contains the fully typed standalone calculation; the plan/report retain the separate authored-request and native-gate outcomes. On rejected facts, the existing generic planner creates a typed null refusal row rather than a successful analytical calculation. This is distinct from falsely reporting the original JEE interpretation as solved.

**Native-free persistence.** The unmodified preflight CLI reads and SHA-256 hashes the original bytes without executing/building PhyDemo or writing output. The unmodified run CLI writes **input.json** as the original Buffer; **analytical-results.json** carries the input hash, typed calculations and authored interpretation; **report.json** carries the hash, planned/observed distinctions and dispatch counts. The bounded new reduced-facts branch leaves scene null, so the run CLI cannot create a qualified-scene.json, native-evidence.json, native package or native observation. Its trusted executor is never entered. The new tests assert byte-for-byte retained input, SHA equivalence, exact four A-only output files, no native execution via an injected throwing executor, native-request blocking and the mixed missing-detector case. I reviewed source and CI records; I did **not** independently run the CLI under Node 24.

**Legacy compatibility and freeze.** The historical run CLI's report.status continues to derive from resultCoverage. The new planner adds nativeVerificationUnfulfilled only to **conditional A** rows on **A-only reduced facts with explicit verifyNative:true**; resultCoverage detects that marker and returns blocked-native-verification while still counting the separately calculated scalar. For all old result families it takes the old branch and retains the old coverage meaning. This narrowly solves the previously failing status problem **without altering historical transfer evidence or modifying the public CLI**.

## 4. CI evidence, including failures and rerun distinction

**First failed source — a real gate, not erased.** Initial HEAD [693f84a20899c55129cf4163af54488411108d61](https://github.com/physicsvigilante/opticsim/commit/693f84a20899c55129cf4163af54488411108d61) had **five** changed files relative to production, including **scripts/run-problem.mjs (+12/−2)**. In [first Node24 CI #44155490022](https://github.com/physicsvigilante/opticsim/actions/runs/44155490022), the log reports **802 tests, 801 pass, 1 fail**. The failing existing test is **test/detector-hit-transfer.test.mjs:34**: “Unexpected change to an unrelated historically frozen path: scripts/run-problem.mjs,” with an actual SHA different from the frozen SHA. It was a legitimate byte-freeze violation, not an apparent-depth native-physics failure. Final source returns that file to the original blob; the historical test and fixture are untouched.

**Exact final-source CI.** Queried the GitHub Actions run collection with head_sha filtering and inspected run and job records. It returns **exactly 11 completed workflows, all conclusion=success**, each with HEAD 5dc594400a3c8d537c180d1162379b5bfda5e3b1. Run IDs: 44156145321, 44156145655, 44156145356, 44156145361, 44156145394, 44156145317, 44156145325, 44156145414, 44156146951, 44156145547, 44156145539. This is **11 workflow conclusions, not 11 independent physical experiments**.

[Full planar-refraction/native/browser run #44156145655](https://github.com/physicsvigilante/opticsim/actions/runs/44156145655) has actual log checkout **refs/pull/133/merge = d3dda63d6d079048e8b144d89ce6dcd92f8710b2**, whose Git tree equals the source tree. The job installed **Node v24.19.0**, pinned **PhyDemo 811f508d2b070898c241a568b0c167dcb8645251**, built its test core, and logged **802/802 Node tests pass, zero fail**. Native planar/composition and existing Chrome/UI regression job steps show success. These legacy native/browser steps **do not** test a new apparent-depth observer or browser visualization.

**Transparent retry.** [Qualified-authoring run #44156145539](https://github.com/physicsvigilante/opticsim/actions/runs/44156145539) had first job attempt **failure** despite **802/802 Node pass**, at the browser-acceptance step with the exact error **“Chrome/Chromium unavailable; no browser validation performed.”** The source was **not changed**. Only its failed job was retried; run **attempt 2** succeeded. That job's log confirms qualified browser acceptance **8 checks, 2 screenshots** and supported demonstration browser **29 checks, 7 screenshots**, with Chrome **157.0.8103.50**; the surrounding native/CLI steps also show success. The first runner/environment failure remains part of the record. Its precise infrastructure cause is not proven.

**Evidence interpretation.** I independently inspected GitHub objects, raw job logs, test source and job-step conclusions. These are **builder/CI executions inspected by a separate reviewer**, not an independent rerun of the Opticsim application. No independent PhyDemo, Chrome, or Node24 CLI run was performed during this review. The only independently executed computations were the scalar mathematics above.

## 5. Ranked findings, severity and recommendations

**P0 — none.** No altered native optics, unsound admitted ray formula, untracked merge-tree change, lost raw-input identity or silent native execution found in the reviewed source.

**P1 — none identified in this exact bounded A contract.** The historical byte-freeze failure is **resolved in final source**; the valid A-only explicit native-verification request is visibly blocked rather than incorrectly reported as fulfilled.

**P2-1 — minor cross-level error-taxonomy precedence gap (nonblocking refusal).** The D-01 wording says unknown fields should take invalid-input precedence over missing fields. The helper **fields()** does this *within* a record, but the evaluator returns immediately on missing top-level required keys before inspecting unknown keys in a different nested record. For example, remove **physical.object** and add an extraneous **physical.media.unexpected** field: the top-level check returns MISSING_FACTS/needs-information before inspecting media, rather than INVALID_FACTS/invalid-input. **Both paths refuse and return no scalar or native work**, so this is not a false physics success. If global precedence is a public contract rather than local per-record precedence, tighten structural validation in a separately reviewed follow-up and test cross-level simultaneous missing/unknown fields. The existing test covers priority within viewing only.

**P2-2 — test-boundary enhancement (not a demonstrated implementation defect).** The new suite checks both sides of the 1% model rule (2.084° admitted, 2.087° refused for 4→1), depth/index endpoints and units. It does not establish an exact **1.000000%** boundary policy via a constructed threshold case, nor a concrete numerically-indeterminate derived result within the current admitted finite input bounds; the latter is plausibly unreachable given the input domain and should be documented as defensive, not claimed as executed. A follow-up can add solver-independent metamorphic/threshold and nested-error-priority cases without changing physics or loosening the scope.

**P3 — consumer labels.** Standard old report coverage can say **all-requested-quantities-available** for a successful A-only *mathematical* request with verifyNative:false, while its actual result status is only **conditional**. The report meaning, warnings, method and native:not-run make the distinction, and verifyNative:true is correctly blocked. Downstream displays and teaching labels must retain those qualifications; do not abbreviate coverage to “image found” or “native verified.” Similarly, the angular envelope is a difference between stipulated constructions only.

These findings do **not** justify enlarging A's scope to a native ray/observer feature, changing the frozen run CLI, weakening historical tests, or creating a new scene schema. PR #129 aperture safety, issue #123 main protection, held v14–v19 physics, and candidate B finite-window research stay separately gated.

## 6. Decision and independence declaration

**CLEARED FOR OWNER DECISION — exact source HEAD 5dc594400a3c8d537c180d1162379b5bfda5e3b1, Git tree d02d23e598d8211830928414fb5a1ae232d450f7, only.** The implemented paraxial formula, explicit 5° AND 1% gate, strict reduced-facts refusals, deterministic A registration, preserved historical CLI/freeze, truthful conditional reporting, native verification refusal and exact-source final CI are consistent with the reviewed bounded A design. P2 findings above are recommended hardening, not independently observed successful-result errors. A different source HEAD or incomplete refreshed CI would require a new review; this clearance cannot be transferred by name.

**Read-only review of Opticsim:** no Opticsim files, branches, pull requests, tests, CI runs, native pin or browser artifacts were modified, retried or merged by me. Publishing this review file in **physicsvigilante/review_sandbox** is the only intended write. Builder-provided claims were checked against GitHub metadata and source; no independently executed native/browser run, new image capability, original-textbook-fidelity validation, or owner release approval is claimed.
