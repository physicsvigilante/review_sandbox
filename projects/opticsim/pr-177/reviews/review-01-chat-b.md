# Opticsim PR #177 — independent physics and evidence review (Chat B, review 01)

**Review date:** 2026-11-19  
**Final verdict: CHANGES REQUESTED**  
**Reason:** one release-evidence provenance blocker, not a demonstrated failure of the new paraxial formulas or archived native ray traces. Do not treat this as owner approval or merge authorization.

## 1. Scope, immutable source, and independence

- **PR:** https://github.com/physicsvigilante/opticsim/pull/177 (draft, open, unmerged at inspection).
- **Exact reviewed source SHA:** **f981be4750f60a6bd5a9f5fc0fb003e82013a5a9**.
- **Actual source commit Git tree, obtained directly from GitHub's Git-object API:** **df49aa4114479ac2462bfa67682b4c9b6ef3e37b**.
- **Production base:** f0235bc5dabce50df81192d4fd7807c62cab4edd.
- **CI synthetic merge:** f39a7240bab504af348dcb0e93af946f4ea6851d; actual tree **df49aa4114479ac2462bfa67682b4c9b6ef3e37b**, ordered parents [base, reviewed source].
- **Pinned PhyDemo:** 811f508d2b070898c241a568b0c167dcb8645251.

Reviewed the seven actual newly added source/test/document/example files by immutable source SHA, not merely the PR description; checked the base-to-source GitHub comparison (12 commits ahead, zero behind; seven added paths, zero modifications/deletions); read the [full builder verification](https://github.com/physicsvigilante/review_sandbox/blob/95b90bbd06a43506f8a2d32f341addc460788de8/projects/opticsim/pr-177/BUILDER-VERIFICATION-01.md), final workflow/job log and actual downloadable evidence ZIPs.

Relevant source anchors:
- [Analytical implementation](https://github.com/physicsvigilante/opticsim/blob/f981be4750f60a6bd5a9f5fc0fb003e82013a5a9/src/spherical-interface-paraxial-query.js); [byte-bound CLI](https://github.com/physicsvigilante/opticsim/blob/f981be4750f60a6bd5a9f5fc0fb003e82013a5a9/scripts/spherical-interface-query.mjs).
- [Analytical tests](https://github.com/physicsvigilante/opticsim/blob/f981be4750f60a6bd5a9f5fc0fb003e82013a5a9/test/jee-spherical-interface-paraxial-query.test.mjs); [native witness test](https://github.com/physicsvigilante/opticsim/blob/f981be4750f60a6bd5a9f5fc0fb003e82013a5a9/test/jee-spherical-interface-native-witness.test.mjs).
- [Analytical contract](https://github.com/physicsvigilante/opticsim/blob/f981be4750f60a6bd5a9f5fc0fb003e82013a5a9/docs/JEE-SPHERICAL-INTERFACE-PARAXIAL-QUERY.md); [native study](https://github.com/physicsvigilante/opticsim/blob/f981be4750f60a6bd5a9f5fc0fb003e82013a5a9/docs/JEE-SPHERICAL-INTERFACE-NATIVE-WITNESS.md).

**Independent work actually performed:** Git-object provenance comparisons, raw ZIP SHA-256/CRC validation, all archived native-input byte-hash comparisons, checks against archived native fixture geometry and actual callback positions/directions, independent scalar/vector Snell and Gaussian calculations, event/terminal-status examination, and public-v7 result/negative-control examination. **Not performed:** an independently operated fresh PhyDemo/Node 24/Chrome simulation. The native and browser executions examined here were builder-operated GitHub CI. The numerical checks below recompute archived outputs; they are not another independent native run.

The previous unchanged merged v22/v23 implementations are outside this review.

## 2. Blocking finding — B1: false source-tree identity in release handoff

**Severity:** blocking evidence/provenance defect. **Disposition:** correction required before clearing for owner decision.

Both the PR description and its immutable builder-verification report assert source Git tree **0475daae3f1fd028a6672e243635eb2c67993961**, and assert that the synthetic merge has that same tree. Direct GitHub Git-object reads show otherwise:

| GitHub Git-object query | Observed tree |
| --- | --- |
| [Source commit f981be...](https://api.github.com/repos/physicsvigilante/opticsim/git/commits/f981be4750f60a6bd5a9f5fc0fb003e82013a5a9) | **df49aa4114479ac2462bfa67682b4c9b6ef3e37b** |
| [Synthetic merge f39a724...](https://api.github.com/repos/physicsvigilante/opticsim/git/commits/f39a7240bab504af348dcb0e93af946f4ea6851d) | **df49aa4114479ac2462bfa67682b4c9b6ef3e37b** |
| [Handoff-claimed tree 0475da...](https://api.github.com/repos/physicsvigilante/opticsim/git/trees/0475daae3f1fd028a6672e243635eb2c67993961) | GitHub API **404 / Not Found** on inspection |

The good news: the **actual** source and CI synthetic-merge trees agree, the source SHA is the requested one, and the final CI job checked out the claimed synthetic-merge commit. This is not evidence of a source or binary substitution. Nevertheless, immutable-tree identity is an explicit release gate; the two governing handoff documents presently claim an incorrect Git object.

**Required correction:** independently re-read both Git commit objects; correct the source-tree and merge-tree entries in the PR's handoff text, and publish a traceable correction/erratum to the builder verification in review_sandbox (preserve the old pinned report as historical evidence). Bind the corrected statements to the same exact source/merge SHAs and already identified artifacts. No formula alteration, new source commit or rerun of otherwise valid CI is indicated solely by this metadata correction, provided the source and artifact identities remain unchanged. Until the correction is published and verified, **CHANGES REQUESTED**.

## 3. Signed single-surface paraxial physics — PASS for declared scope

The implementation uses positive signed coordinates **along incident light**, with incident-side real axial object u<0 and positive R when the centre lies on the transmitted side. Its defining equation is:

**n2/v − n1/u = (n2 − n1)/R**, with surface power **P = (n2 − n1)/R_m** and Gaussian transverse magnification **m = n1 v/(n2 u)**.

Independent numerical substitutions:

| Case | Result | Assessment |
| --- | --- | --- |
| J15 conditional single interface: n1=1, n2=4/3, R=+100 mm, parallel input | P=+10/3 D; image-side focal distance +400 mm | Correct signed power/focal distance |
| J16 conditional meridional example: n1=1.5, n2=1, R=−150 mm, u=−100 mm | v=−600/7 mm; m=+9/7 | Correct virtual conjugate; added exterior n=1 is disclosed |
| Parallel lower-index entry: n1=1.5, n2=1, R=+100 mm | image-space focal distance −200 mm | Correct virtual focal sign |
| Finite real object: n1=1, n2=1.5, R=+100 mm, u=−300 mm | v=+900 mm | Correct finite real conjugate |
| Exact zero index contrast | zero canonical power, afocal; real-object conjugate v=u, m=1 | Correct no-interface limit |

These results are **strict paraxial/first-order** calculations. They do not assert a physical detected image, a complete two-surface sphere, a 3D apparent depth, a JEE source question solved without missing facts, or finite-angle equality. The numerical J16 exterior index is an added assumption; the source record is not silently completed.

## 4. Input validation and numerical safeguards — PASS for declared bounded API

Checked actual implementation and adversarial regressions. The root must be an object with exact known/required keys and an explicit format, query kind, sign convention, unit, both indices and radius. The conjugate query additionally requires the signed object distance; power rejects it. Finite JSON numeric types are required; material indices are in [1,4], radius magnitude in [1,10000] mm, and admitted real-object distance u≤−0.01 mm with magnitude ≤10000 mm. Unsupported units and novel/extra fields reject. The final code **explicitly checks typeof lengthUnit === 'string'** before enum lookup, closing the demonstrated JavaScript ["cm"] key-coercion bug; adversarial array, boxed-string and coercion-object regressions exist.

Exactly equal indices are handled separately from extremely weak **nonzero** contrast (relative threshold 1e−12). Near-focus denominator cancellation (relative threshold 1e−10), nonfinite calculations and focal/image magnitudes exceeding 1e9 mm return **numerically-indeterminate** with null value rather than falsely certified finite predictions. These are conservative declared guardrails, not general forward-error proofs.

The CLI copies unmodified input bytes, records SHA-256 in successful and rejected evidence, reserves a fresh directory, and never turns the analytical calculation into native output. The query and CLI retain **native.status = not-run**, observations null and nativeImageDetected false. A separate native test cannot retroactively change this status.

**Nonblocking hardening consideration:** JSON.parse accepts duplicate object member names using its parser semantics, and the near-axial two-detector research intercept tests exactly dy=0 rather than an independent near-zero conditioning limit. Neither is a demonstrated defect within the currently stated, bounded use of the analytical API, but both deserve explicit contract language if future work promotes these research operations to public arbitrary-input authoring.

## 5. Genuine native geometry, completion, exact Snell — PASS for archived research evidence

Reviewed event wrapper source: original onSimulationStart/onRayIncident callbacks are saved; each wrapper calls the original with the same receiver/arguments **exactly once** and returns its result. Only before/after direction, hit position, type, absorption and new-ray count are recorded. There is no authored ray steering, injected analytical angle, manual clipping or deletion of the glass boundary.

**Entry research fixture:** raw native closed Glass contains the true R=100 mm circular entrance with centre (100,0) and pole (0,0), including retained far closure at x=600 mm. Native inside-medium detectors at x=20 and x=40 mm are followed by a real Blocker at x=60 mm, before that closure. Every usable run had a real four-event sequence **Glass → Detector → Detector → Blocker**, one emission, no secondary rays, absorption at the screen, completed terminal event, zero errors/warnings/truncation/undefined behaviour. Controls with screen removed or moved beyond closure instead record additional real boundary encounters and do **not** qualify. The closed material geometry was not silently changed into an open single surface.

**Exit research fixture:** an actual inside source exits the **full retained CircleGlass** (centre −150 mm, radius 150 mm), then reaches detectors and blocker. The source is inside, not an externally incident two-interface circle disguised as one interface. The native ratio of material indices is set consistently for entrance/exit cases, and a TIR-trapped control is excluded.

**Independent audit of the downloaded final archive:** ZIP SHA-256 **38b309f328c523485ae90049b9cb16a761d76e513bb1d9da99f73049aea445a2** matches GitHub metadata; all member CRCs passed. All **31** raw native-input files match the SHA-256 claimed in their associated research reports. Classification is **25 usable completed single-crossing runs**, including **one axial run with no identifiable intercept**, hence **24 nonaxial mathematical intercepts**; plus **three completed but disqualified**, **two incomplete**, and **one stopped** control, all six with derived=null.

For the 25 usable traces, independently recomputed maximum first-surface circle residual is approximately **1.28×10⁻¹³ mm**; maximum signed Snell invariant residual **3.32×10⁻¹⁴**; detector-line collinearity residual approximately **3.41×10⁻¹⁴**. Reconstructed intercepts match stored detector-point derivations. For exit cases, a separate vector-based geometric circle-intersection/Snell calculation, distinct from the test's entry scalar formula, matches all five archived intercepts within **2.12×10⁻¹² mm**. Parallel-entry archived values independently match exact Snell to about **2.6×10⁻¹¹ mm** at worst. These tiny residuals are **floating-point consistency checks on the archived trace**, not external experimental accuracy guarantees.

Convergence evidence is consistent with finite-angle aberration rather than a forced paraxial answer:

| Witness and smallest tested input | Archived two-detector axis intercept | Paraxial limit | Discrepancy |
| --- | ---: | ---: | ---: |
| Entry 1→4/3, h=0.25 mm | +399.999296874119 mm | +400 mm | 0.000703126 mm |
| Exit 1.5→1, angle=0.25° | −85.714198292065 mm | −600/7 mm | 0.000087422 mm |
| Entry 1.5→1, h=0.25 mm | −199.998593746157 mm | −200 mm | 0.001406254 mm |

Successive halving of input height/direction reduces the discrepancy by approximately fourfold. The previously failed 0.5 mm and 1 mm finite-angle expectations remain as explicit nonzero-error checks; physics and native propagation were not altered to force equality. Finite-real-object archived rays approach +900 mm (at 0.1°: 899.946389507 mm). The x=20/40 detector line is **extrapolated mathematically**: no focal-plane detection or image observation is asserted. The exactly axial two-hit ray correctly yields **no identifiable intercept**.

## 6. Research/public separation and CI provenance — PASS, subject to B1

The raw native fixtures explicitly mark researchOnly=true, canonicalAuthoringAvailable=false, originalProblemSolved=false and nativeImageDetected=false; the canonical compiler rejects the raw fixture in the test. This work does not add a public single-spherical-interface schema or alter existing production/native/qualification code.

A separate **existing public schema-v7** inside-circle document, using prepareScene, evaluateDocument and evaluateObservables, is archived with the original request, canonical document, asked observables, native summary and negative controls. The completed case records exactly one from-inside interface interaction and two detector hits: **all three observations qualified**. Changing the material index makes **all three stale observations suppressed/null**; depth exhaustion makes **all three incomplete observations suppressed/null**. These existing-public measurements are not conflated with the raw research fixture or the standalone analytical query.

At final source SHA, GitHub reports **11/11 successful PR workflows**. The [final optical run](https://github.com/physicsvigilante/opticsim/actions/runs/44535274231), [job 135598887701](https://github.com/physicsvigilante/opticsim/actions/runs/44535274231/job/135598887701) checked out synthetic merge f39a724..., with **938/938 Node tests passed, zero failed/skipped**. Existing public v19–v23 native/browser steps passed, but are regression evidence for unchanged code rather than a new single-surface browser UI.

Downloaded and independently verified the final [llm-authoring-evidence artifact 14535373214](https://github.com/physicsvigilante/opticsim/actions/runs/44535274231/artifacts/14535373214) above, the [browser acceptance artifact 14535213201](https://github.com/physicsvigilante/opticsim/actions/runs/44535274231/artifacts/14535213201) (ZIP SHA-256 **2e6b1c8c8d52745b42e090d0a35e1a5763de651adf9782395a1db03e6af5df41**; 27/27 reported checks, 15 PNG screenshots, no recorded errors), and the [hosted smoke artifact 14535542834](https://github.com/physicsvigilante/opticsim/actions/runs/44535274231/artifacts/14535542834) (ZIP SHA-256 **29d7575f474525e42202236a931df5ddfc6c7e34cd6cd01d0705c92d5869982e**; 5/5 reported checks, one PNG, no recorded errors). All downloaded ZIP CRCs passed. Actual Chrome version in these two reports and CI log is **157.0.8103.78**. The builder handoff gives **157.0.8103.50**: correct that lower-severity execution-metadata discrepancy alongside B1.

The initial 936/938 red-test history cited in the handoff is recognized as history, **not substituted for** this final 938/938 run. No historical v22/v23 review was repeated.

## 7. Required action and final decision

**Required (blocking):** correct and republish the actual exact **df49aa4114479ac2462bfa67682b4c9b6ef3e37b** tree identity for **both** source commit f981be... and synthetic merge f39a724... in the PR's release handoff and a traceable builder-verification correction/addendum. Correct the minor Chrome version discrepancy while updating provenance. Preserve immutable prior reports/artifacts and the existing source/CI identifiers; verify the correction by reading the updated GitHub content back.

**Not required on currently inspected evidence:** altering the paraxial equation, clipping or rewriting native rays, converting research geometry to public canonical admission, repeating merged v22/v23 review, creating a second independent review, or claiming an independently run native solver.

**Final verdict: CHANGES REQUESTED.** Physics, bounded numerical policy, native archived witnesses, source-byte binding, public/research separation and final CI are satisfactory **within their explicitly limited scope**. The handoff's incorrect immutable Git-tree identity prevents an unqualified release-evidence clearance. Owner retains the sole release/merge decision; PR #177 must remain draft/unmerged pending evidence correction and owner review.
