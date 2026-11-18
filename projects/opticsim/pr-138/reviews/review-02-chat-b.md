# Chat B — Opticsim PR #138 independent B1a source/native-physics R2 review

**Date:** 2026-11-18  
**Verdict: CLEARED FOR OWNER DECISION — B1a SOURCE ONLY.** This is a bounded technical source-review clearance, **not** a merge, release, authenticated proof of native execution, physical-accuracy calibration or authorization for B1b/image/eye/observer claims.

## 1. Exact reviewed identity and protected scope

| Item | Independent GitHub observation |
| --- | --- |
| [Draft PR #138](https://github.com/physicsvigilante/opticsim/pull/138) | Draft, open, unmerged at review; authored HEAD still pinned at final check |
| **Authored HEAD** | `98c410692d9478068d26591304d8a4b4ab00a817` |
| **Authored Git tree** | `fdbc02adff1dc539ebda2fd72027a65d32a54e21` |
| **Production base** | `d3509e82fb65d81aabe336666851f8f2962623f4`; tree `45ff3bcd9093a527652f13f76c3cc0b02826642f` |
| **Synthetic tested merge** | `273910bb24cf4c8f484b5c59f95a096b360dbf9d`; tree **identical** to authored tree |
| **Merge parents, in order** | Base `d3509e82...`, then authored HEAD `98c41069...` |
| **PhyDemo pin** | `811f508d2b070898c241a568b0c167dcb8645251` |
| **Base-to-HEAD comparison** | 19 ahead, 0 behind; exactly **six added files**, 1,400 additions, zero deletions |

I fetched raw Git commit objects for HEAD, base and synthetic merge (not merely the PR's descriptions), the live PR metadata and GitHub's base/HEAD comparison. The complete changed-file set is:
1. `src/detector-pair-json.js`
2. `src/detector-pair-plan.js`
3. `scripts/detector-selected-pair.mjs`
4. `test/detector-pair-evidence-integrity.test.mjs`
5. `test/detector-selected-pair.test.mjs`
6. `examples/jee-detector-selected-native-pair-v1.json`

There are **no edits** to existing/native solver code, pin, historical CLI, saved scene schema, browser/UI or workflow files. As an independent spot-check, the historical `scripts/run-problem.mjs` blob remains `2efecbf3eddcd9322782cc1667b02fe495fd4fa8`, and `scripts/author-scene.mjs` remains `0d2ecff53aa03575f96390622ac438fb87aa4a30`. The unchanged `src/contract.js` explicitly pins the above PhyDemo commit.

Reviewed the complete [R2 request](../REQUEST-02.md), [R2 reviewer prompt](../REVIEWER-PROMPT-02.md), immutable [R1 report](review-01-chat-b.md), all six new files at exact HEAD, the baseline `src/observables.js`, `src/planar-media.js`, `src/qualified-utils.js`, `scripts/author-scene.mjs`, `scripts/authoring-evidence.mjs` and the underlying native checker source; compared native and browser CI raw logs. Original R1 is preserved **unchanged**: its **CHANGES REQUESTED** verdict applies to old HEAD `936f7d8bca9af0db950ab258e6df2f0e3a37914a` / tree `182a8c51dfcc9cd618e9d92f25ea0d5cb49edc30`, not to this corrected R2 source.

## 2. P1 evidence-integrity blocker: independent code-path disposition

**R1 P1-F1 is fixed for the defined selection-bearing saved evidence.** The old verifier checked file checksums without ever checking the contents of `native-A/B.json` and `readouts-A/B.json` against the corresponding authored scenes and report. The R2 verifier is now asynchronous and materially different; I inspected [the exact verifier lines 273–419](https://github.com/physicsvigilante/opticsim/blob/98c410692d9478068d26591304d8a4b4ab00a817/scripts/detector-selected-pair.mjs#L273-L419), not only its assertions.

It checks an exact whitelist of **nine** hashed/byte-counted inputs and evidence artifacts, separate from final `manifest.json`; distinct scene SHAs; the original exact UTF-8 request; and a fresh **planning-only**, strict re-authoring of *both* v5 scenes from the saved original request. It reconstructs the full family hash and expected plan and verifies each serialized scene's **exact bytes**, SHA, authoring role and native pin. No PhyDemo run or synthetic ray is used during verification.

Most importantly, for **each** lettered native file it parses the actual JSON and requires `sceneText` to be the matching exact scene, `scenePin` the original pinned commit, and `summary.canonicalSha256` the matching scene hash. It cross-checks `summary.native`, `summary.observations`, `summary.executionPassed`, native status/warnings/errors and the row's recorded native fields. Each saved readout must match its role, input/scene/family SHA, authored heading, schemaVersion and full corresponding `report.runs[i]` record. The verifier independently re-evaluates all four **read-only observables from its own saved native summary**, normalizes the records, reclassifies each run and recomputes the two-run aggregate and withholding status. This directly closes the R1 omitted-native/omitted-readout code path.

The new [seven targeted R2 tests](https://github.com/physicsvigilante/opticsim/blob/98c410692d9478068d26591304d8a4b4ab00a817/test/detector-pair-evidence-integrity.test.mjs#L43-L136) do **not** rely solely on stale manifest checksums:
- `native-B.json` is copied over `native-A.json`, then the target manifest entry's **SHA-256 and byte count are recalculated**. Rejection must cite the scene/role/pin mismatch.
- `readouts-B.json` is copied over `readouts-A.json` with the **correct updated** manifest digest/count. Rejection must cite readout association.
- Separately rehashed edits to a saved detector crossing count or readout result are rejected.
- The test source asserts these rejection outcomes, and the exact-merge **raw Node24 CI log actually records all three passing** (lines 304–306 of job `134646459233`).

This is **internal selection-evidence consistency**, not an independently signed ledger or a guarantee that an adversary cannot rewrite the entire mutually agreeing bundle. The public verification result must never be described as proof of optical physics or origin by hash alone. A narrower optional raw-report consistency limitation is recorded under P2 below.

## 3. Physical authoring, native observations and refusal

**Bounded supported model.** [Input parser](https://github.com/physicsvigilante/opticsim/blob/98c410692d9478068d26591304d8a4b4ab00a817/src/detector-pair-json.js) rejects invalid UTF-8, >1 MiB input, nested/escaped duplicate keys, malformed JSON and nesting beyond 40 levels. [Planner](https://github.com/physicsvigilante/opticsim/blob/98c410692d9478068d26591304d8a4b4ab00a817/src/detector-pair-plan.js) checks supplied invalid/unknown facts before missing facts, then unsupported scope. One explicitly authored v5 point-source with single-ray emission, one planar interface and one **real** finite detector are allowed. All physical parameters, run policy, source/detector/plane IDs and second **absolute** heading must be provided. Canonical mm conversion precedes the 2–10 mm detector-length bound. Planar signed half-spaces, whole detector clearance ≥1 mm, tangent orientation modulo 180°, and distinct source headings modulo 360° are checked. The second run changes only the source heading in a cloned validated scene; the shared family hash is order-stable. It reuses native PhyDemo; there is **no second Snell solver** or B1b numerical backprojection.

**Native execution boundary.** Each of the two separate native invocations requests `source-emissions`, `interface-first-event`, `detector-crossings`, and opt-in `detector-hit-events`. Selection requires original scene/native pin identity, completed execution, zero truncation/undefined behavior, no unqualified native warning, exactly one emitted ray, transmitted first encounter with correct signed-side refractive indices, one transmitted branch, one finite detector crossing and complete one-hit capture. The hit must be strictly inside the physical detector and its unit incoming direction must agree with the actual first transmitted branch within an explicitly **same-run** `1e-8` tolerance (not an optical accuracy certificate). Full Fresnel-off only earns **qualified**, not silently available. Actual TIR, aim-away, short-window miss, shifted miss and missing/stale native capture remain unavailable/suppressed rather than manufactured rays.

**Independent scalar optics check.** For the [example](https://github.com/physicsvigilante/opticsim/blob/98c410692d9478068d26591304d8a4b4ab00a817/examples/jee-detector-selected-native-pair-v1.json), source `(-120,0)` mm, interface `x=0` at indices `1.5→1`, detector center `(40,0)` mm of length 5 mm, and headings `±0.5°`:
- Independently computing Snell's law gives transmitted angular magnitude `0.7500118999902258°`, `|y|=1.5708611274685715` mm and finite endpoint margin `0.9291388725314285` mm.
- Raw pinned-native CI reports distinct A/B hits `(40,-1.5708611274685678)` and `(40,+1.5708611274685678)`; transmitted/incoming unit direction `(0.9999143248553549,±0.013089803247560816)`; one emission, first transmission, one crossing and one captured hit **per run**. Their canonical scene SHAs are `bf785bcde6f7f5ae8b47f7c5214519ff04f696cd2dee24df8d4fb80d8ca96444` and `01e8e811a7c7f6d4f4c39298c2c4f6c913e657e38fbd18ec746252500e2f1423`.
- The native reflected Fresnel branch has about 4% relative power versus about 96% transmitted. With equal indices, independently computed `|y|=1.3962988465214063` mm agrees with registered native controls. The 2 mm detector misses both typical rays, while 10 mm detects both. A genuine 37° rotated plane/source/detector test verifies transformed **native** hit positions, not merely re-labelled arithmetic.

**Non-image boundary.** Successful public results retain `geometry:{status:'withheld',value:null,reasonCode:'B1B_NUMERICAL_GATE_NOT_RELEASED'}`; failure/negative results also retain `geometry.status='withheld'` and `value=null` with their refusal reason. Observer/image assessments remain `not-assessed`, interpretation and question support remain `not-assessed-by-engine`. Two sequential sampled rays do **not** establish simultaneous visibility, a virtual image, eye/pupil acceptance, an image plane, continuous irradiance, apparent depth, uniqueness or calibrated physical accuracy.

## 4. P2/P3 correction disposition and explicit residual limits

**P2 from R1 addressed.** [`normalizeReadouts`](https://github.com/physicsvigilante/opticsim/blob/98c410692d9478068d26591304d8a4b4ab00a817/scripts/detector-selected-pair.mjs#L47-L56) materializes nullable reason, reasonCode, method and a warnings array on every B1a readout without changing the baseline `src/observables.js`. Original raw native warnings/errors are separately retained in run records. There is no `qualified→available` promotion. The pinned core is built **before** the first native-attempt count; failed setup records **0 attempted/0 completed**, an infrastructure error and **no manifest**. Tests separately establish first/second executor-failure counts **1/0** and **2/1**, as appropriate. The injectable JS executor/setup is labelled `test-injected-untrusted`, and the verifier reports `test-injected-non-authoritative`; the standalone CLI uses built-in pinned PhyDemo. The authority label is **self-reported metadata**, not a cryptographic authentication primitive.

**P3 from R1 addressed.** Run records expose `schemaVersion=5`. The new 37° rotated valid normal/source/finite detector test executes genuine native measurements; source direction changes from 36.5° to 37.5° and detected positions agree with the 37° rotation of the observed finite-window hits.

**P2 advisory, nonblocking for this narrow clearance — raw-report redundancy is not fully cross-verified.** The saved `native-[A/B].json` also contains an ancillary `report` object returned by `checkCandidate` (including `report.native.diagnostics` and `report.executionPassed`). The R2 verifier validates `native.summary` and the scene/readout/selection fields, but does not compare every redundant field in `native.report` with that summary. By static inspection, a modified *ancillary report only* with a recalculated manifest digest would not necessarily be rejected, even though the **selection-bearing** summary/readouts remain untouched. Therefore describe `verified-finalized-evidence` precisely as **verified selection-bearing semantic associations**, not total validation of every diagnostic field. If consumers will treat the nested raw report as independently authoritative, add explicit internal summary/report concordance checks and a rehashed raw-report-only negative test **before that stronger claim**. This finding does not recreate the R1 full-native/readout role-swap acceptance or change a verified B1a selection.

**P3 optional follow-up.** Consider documenting exactly which native-report fields are normative, plus tests for rehashed mismatches of those fields and for entire-bundle rewriting to demonstrate the intentionally limited threat model. Do not claim signatures, native mathematical calibration or B1b geometry from these tests.

## 5. CI actually inspected, including real failure history

- GitHub commit-associated workflow API for **authored HEAD `98c41069...`** returned **11/11 completed SUCCESS** (not a conflation with old source). All 11 include the same PR source identity.
- [Plane-mirror inverse run #44258686271](https://github.com/physicsvigilante/opticsim/actions/runs/44258686271), job `134646459233`: raw checkout was synthetic merge `273910bb...` and its tree equals authored source; Node `v24.19.0`; pinned PhyDemo `811f508...`, headless build **1,164 modules**; **817 tests / 817 pass / 0 fail / 0 cancelled**. Raw log lines 304–310 record the R2 swapped-rehash, setup, warning, 37° and injection tests; line 312 contains genuine pinned-native hit/direction evidence. Earlier 810-test runs are **not** substituted for these 817 tests.
- [Optical composition/Chrome run #44258686331](https://github.com/physicsvigilante/opticsim/actions/runs/44258686331), job `134646459427`: checkout the same merge, Node24/pinned PhyDemo/817 passing tests, full build/native workflow steps successful, and **Google Chrome 157.0.8103.50** existing regression results **27 browser checks / 15 screenshots** and **5 hosted smoke checks / 1 screenshot**. These are legacy-browser compatibility checks, **not** newly implemented B1a eye/image UI.

The regression/failure archive remains truthful:
- First source `f657b9762e4b30b847a0d69cfb47546a0366b1cb`: **11 failed workflows**, raw 804-test CI **803 pass / 1 fail**, with the cm/m preconversion detector bound issue and `0 !== 2`; the final source applies the bound **after** canonical unit conversion.
- Old R1 source `936f7d8...`: **11 successful workflows, 810/810 tests**, but its **P1 semantic-integrity defect remained**, hence [R1 CHANGES REQUESTED](review-01-chat-b.md). CI success did not erase the source defect.
- Intermediate test migration `2a5abf07ec54d837b91233724765c65f644143ec`: commit-associated CI showed **9 failures and 2 cancellations**. The raw log from [run #44258234153](https://github.com/physicsvigilante/opticsim/actions/runs/44258234153), job `134644993759`, contains **`SyntaxError: Unexpected token ')'`** from `assert.equal(verified).status,'verified-finalized-evidence');` in the test file. Later source corrected the syntax. It is a genuine historical test-file failure, not a native physics result.

**What I personally performed:** remote raw Git object and diff comparisons; source/baseline code-path review; independent scalar Snell/finite-window calculation; raw builder CI job/step/log examination; independent reasoning through rehashed-swap/partial-executor refusal and authority boundaries.

**What I did not independently execute:** PhyDemo, the Node24 test suite, Chrome or a new local mutated-bundle replay. The executed results above are **builder GitHub Actions CI**, inspected independently, not independent reruns. The additional ancillary-report observation is a source-path finding, not a claimed executed exploit.

## 6. Ranked decision

- **P0:** None found in the six-file source; no public image/eye geometry, native/pin replacement or forbidden old-code modification.
- **P1:** **R1-F1 resolved for the specified selection-bearing artifact integrity.** Exact swapped-and-rehashed native/readout evidence is refused semantically; no remaining blocking P1 found for the reviewed bounded B1a selection claim.
- **P2:** R1 negative shape, 0/1/2 attempt accounting and executor-test provenance corrected. A **nonblocking assurance limitation** remains for ancillary native-report redundancy and self-asserted provenance; do not promote the verifier to external authenticity or exhaustive raw-diagnostic certification.
- **P3:** Schema/run completeness and real rotated native test added; optional explicit normative-field specification and extra tamper tests may strengthen future evidence semantics.

**Final verdict: CLEARED FOR OWNER DECISION — B1a SOURCE ONLY**, pinned to authored HEAD `98c410692d9478068d26591304d8a4b4ab00a817`, tree `fdbc02adff1dc539ebda2fd72027a65d32a54e21` and tested synthetic merge `273910bb24cf4c8f484b5c59f95a096b360dbf9d`. Any head/tree change requires a new review identity. The owner may decide separately whether to integrate the bounded B1a source under repository policy; **this report does not merge PR #138, override main protection issue #123, touch held PRs, or authorize B1b numerical coordinates, an eye/pupil model, image detection, continuous illumination or native accuracy claims.**
