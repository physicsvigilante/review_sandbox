# Opticsim PR #177 — final builder verification and independent-review handoff

**Date:** 2026-11-19. **Builder verification only; not an independent review, merge approval, blind benchmark, or original-question solved score.**

**Target:** [Opticsim PR #177](https://github.com/physicsvigilante/opticsim/pull/177). Status at verification: **DRAFT, OPEN, UNMERGED**. One focused independent physics/evidence review is now due. Production main and every other held branch are unchanged by this verification.

## 1. Exact identity and release boundary

| Object | Verified SHA |
|---|---|
| Final source commit | `f981be4750f60a6bd5a9f5fc0fb003e82013a5a9` |
| Final source Git tree | `0475daae3f1fd028a6672e243635eb2c67993961` |
| Production main / base | `f0235bc5dabce50df81192d4fd7807c62cab4edd` |
| GitHub synthetic merge | `f39a7240bab504af348dcb0e93af946f4ea6851d` |
| Synthetic merge Git tree | `0475daae3f1fd028a6672e243635eb2c67993961` — identical |
| Pinned unmodified PhyDemo | `811f508d2b070898c241a568b0c167dcb8645251` |

Direct Git-object reads confirm synthetic-merge ordered parents `[main/base, exact source]`. The final optical CI log checks out the synthetic merge and explicitly checks its tree against the source commit. Main's branch ref was read back as the stated base. The [base-to-source comparison](https://github.com/physicsvigilante/opticsim/compare/f0235bc5dabce50df81192d4fd7807c62cab4edd...f981be4750f60a6bd5a9f5fc0fb003e82013a5a9) is 12 commits ahead, zero behind, **seven files added and no existing file modified/deleted relative to main**:

- `src/spherical-interface-paraxial-query.js`
- `scripts/spherical-interface-query.mjs`
- `examples/jee-spherical-interface-power-v1.json`
- `test/jee-spherical-interface-paraxial-query.test.mjs`
- `test/jee-spherical-interface-native-witness.test.mjs`
- `docs/JEE-SPHERICAL-INTERFACE-PARAXIAL-QUERY.md`
- `docs/JEE-SPHERICAL-INTERFACE-NATIVE-WITNESS.md`

There is no change to existing native adapters, public scene schemas, qualification/session code, workflows, frozen source audit or upstream pin. No new public native optical family or browser UI is introduced. The earlier v22/v23 independent review need not be repeated for unchanged source.

## 2. What the capability means

The new standalone analytical query implements the explicitly requested paraxial, single-spherical-interface relations `n2/v - n1/u = (n2-n1)/R` and surface power `(n2-n1)/R_m`. Positive signed distances follow incident light; a real incident-side object has `u<0`. Indices, curvature sign, units and model choice are explicit. Missing/unsupported/nonfinite facts are rejected; near-equal indices, near-focal cancellation and unbounded results are withheld. Source-byte-bound CLI output retains original input SHA-256 and never fabricates a native scene.

The query **always** states `native.status=not-run` and `nativeImageDetected=false`. Separately authored native experiments do not mutate that status. J15's stated n1=1, n2=4/3 and R=+10 cm conditionally produce +10/3 diopters and +40 cm image-space focal distance. J16's meridional illustration explicitly **adds** exterior index 1 to glass index 1.5, signed R=-15 cm and u=-10 cm; its conditional conjugate is -60/7 cm. Neither a missing source convention nor a verified 3D apparent image is inferred.

The frozen 20-case audit in PR #165 is untouched. These results are not retrospective original-question successes, independent interpretation grades, detected images or evidence of complete textbook solutions. No Solutions entries were consulted.

## 3. Genuine native witnesses, not a substituted ray tracer

### Entry: one actual encounter and a real absorbing screen

A research-only native `Glass` region has a true circular-arc entrance of radius 100 mm, pole (0,0), centre (100,0), and an **explicit retained remote closure at x=600 mm**. A real `SingleRay` enters from x=-60 mm. Two passive native detector segments at x=20 and x=40 mm lie inside the region. A genuine native opaque `Blocker` at x=60 mm absorbs the ray before the closure.

The raw experiment must finish with exactly one emission and the native callback sequence **Glass → Detector → Detector → Blocker**, no secondary rays, and normal completion. No ray is steered, rewritten, manually cut off or told its route. Each observation wrapper calls its saved original method exactly once with unchanged arguments/return. Both detectors and screen are before the mathematical paraxial focus: there is **no focal-plane detection**.

Removing the screen, or moving it beyond the closure, causes genuine extra material encounters. These runs can complete, but are excluded from single-crossing evidence. Inside-medium detectors and this closed cap/screen composition are **raw research geometry, not a new canonical admission**; a test confirms the raw JSON cannot be compiled as a canonical document.

### Exit: an internal source legitimately crosses a complete circle once

A native `CircleGlass` retains its full geometry, centre (-150,0) mm and radius 150 mm, with a source at (-100,0) mm **inside** it. Selected outgoing source directions cross the right curved boundary once before the external detectors/screen. This is not an externally illuminated two-interface circle with its later surface silently discarded.

A separate public schema-v7 case uses existing `prepareScene`, native execution and `evaluateObservables` for this internal-source circle with two external detectors and no blocker. Its three requested measurements are qualified. A post-run index change suppresses all three stale measurements; depth-limited execution suppresses all three incomplete measurements. This public-v7 evidence is distinct from the raw research fixture.

## 4. Exact-source execution results

**All 11/11 PR workflows completed successfully at the final source.** The [optical composition run 44535274231](https://github.com/physicsvigilante/opticsim/actions/runs/44535274231), [job 135598887701](https://github.com/physicsvigilante/opticsim/actions/runs/44535274231/job/135598887701), reports **938 tests, 938 passed, zero failed, zero skipped**. All ten additional native-witness/input-policy tests passed.

The same optical job passed existing public native v19–v23 acceptance and their dedicated Chrome checks (11, 8, 9, 8 and 10 checks respectively), base browser acceptance **27 checks / 15 screenshots**, and hosted-demo smoke **5 checks / 1 screenshot**, using Chrome 157.0.8103.50. Those browser checks are regression evidence, not a browser interface for the new analytical query or public deployment.

**Execution provenance:** Node, pinned-native and Chrome executions were builder-operated GitHub CI. The builder retrieved their job log and downloaded evidence; no fresh local Node24/native execution or independent reviewer replay is claimed. Scalar Python rechecks of archived native numbers are additional builder analysis, not another native run.

## 5. Final artifact verification and quantitative checks

Downloaded [llm-authoring-evidence artifact 14535373214](https://github.com/physicsvigilante/opticsim/actions/runs/44535274231/artifacts/14535373214), from the final optical run. Its ZIP SHA-256 was locally recomputed and matched GitHub metadata:

`38b309f328c523485ae90049b9cb16a761d76e513bb1d9da99f73049aea445a2`

All ZIP member CRCs passed. **All 31 raw-native-input.json byte hashes matched their associated reports.** The archive contains:

- **25 usable complete single-crossing raw experiments**, including one exactly axial control with two genuine hits but **no identifiable axis intercept**. Thus there are 24 identifiable nonaxial mathematical intercepts, not 25 observed images.
- **Six excluded experiments**, all with `derived:null`: three completed runs unsuitable for this witness (second-surface or branching controls), two incomplete runs (depth/TIR controls), and one stopped run.
- Separately archived public-v7 source, document, requests, native summary, three qualified measurements, three stale suppressions and three incomplete suppressions.

A line through the two measured detector points is extended **mathematically** to the axis. This is not a native backward ray or image observation. Representative final comparisons:

| Native experiment | Last tested paraxial approach | Derived native-ray axis intercept | Paraxial limit | Absolute discrepancy |
|---|---|---:|---:|---:|
| Entry, n1=1 to n2=4/3, R=100 mm | Parallel height 0.25 mm | +399.999296874250 mm | +400 mm | 0.000703126 mm |
| Exit, n1=1.5 to n2=1, R=-150 mm, u=-100 mm | Source direction 0.25 degrees | -85.714198292065 mm | -600/7 mm | 0.000087422 mm |
| Entry, n1=1.5 to n2=1, R=100 mm | Parallel height 0.25 mm | -199.998593746224 mm | -200 mm | 0.001406254 mm |

Entry heights 8, 4, 2, 1, 0.5, 0.25 mm and exit directions 4, 2, 1, 0.5, 0.25 degrees show decreasing finite-angle discrepancies. Additional finite-real-object rays approach the +900 mm conjugate. Signed heights, propagation reversal, translation, remote closure position and screen position preserve the relevant local results.

Parallel-entry native points are also compared with a separate exact scalar Snell reference, rather than being required to equal Gaussian optics at finite height. A separate local Python recomputation of all nine such archived samples agreed with measured intercepts to approximately **2.6e-11 mm**; all are comfortably within the declared test tolerance 1e-7 mm. Across 25 usable raw cases, locally recalculated maximum radial residual was about 1.28e-13 mm and maximum signed Snell residual about 3.32e-14. Reconstructing the intercept from both detector points reproduced each stored intercept. **These are floating-point numerical consistency checks, not physical metrology accuracy or universal forward-error bounds.**

Research archives explicitly mark `researchOnly=true`, `canonicalAuthoringAvailable=false`, `originalProblemSolved=false`, `nativeImageDetected=false`; unusable observations are retained as diagnostics without a derived comparison.

## 6. Corrections and retained failure history

**Strict unit validation:** the new query initially accepted an array such as `["cm"]` because JavaScript object-key lookup coerced it to a string. The final query requires `typeof lengthUnit === 'string'` before enum lookup. Regression tests reject arrays, boxed/coercing objects and other nonstring values. No optical formula or legacy contract was changed.

**Finite-angle expectation correction:** initial native-study source `68507b7a0183786cb1677a66fde91463ef68a69d` passed **936/938** tests. Two newly written expectations underestimated actual finite-angle departure from the paraxial limit: the h=0.5 mm 1→4/3 case differs by about 0.002812514 mm, exceeding the proposed 0.002 mm; the h=1 mm 1.5→1 case differs by about 0.022500984 mm, exceeding 0.02 mm. Native observations satisfy exact Snell refraction.

The correction **retains both cases and explicitly tests their nonzero paraxial error**, adds independent exact-Snell comparisons, and adds smaller-height samples meeting the original paraxial-accuracy goals. It does not modify native propagation or the analytical formula to force agreement. The raw witness gate now also explicitly requires the terminal completion event and archives the processed-ray limit.

The initial failing [optical run 44534020519](https://github.com/physicsvigilante/opticsim/actions/runs/44534020519), job 135594595993, and artifact 14533699646 remain part of the history. Its ZIP digest `c25583d8d179115d0ca2e1450e51d30ee2a10c33c6d39b6c171afcbf68e0f4a3` was independently rehashed and CRC-checked; all 28 initial raw-input hashes matched. The earlier pre-native-study 928-test result is historical, not the final 938-test evidence.

## 7. Required single independent review

Review **only this exact final combined candidate**: source `f981be4750f60a6bd5a9f5fc0fb003e82013a5a9`, tree `0475daae3f1fd028a6672e243635eb2c67993961`. Do not repeat the full review of unchanged merged v22/v23 or request separate reviews for the analytical query and its native verification.

Focus on signed single-interface paraxial physics; real/virtual and zero-contrast cases; unit/type validation and numerical singularity withholding; source-byte/hash evidence; genuine original native delegation and complete-run guards; retained closure versus actual absorption; exact Snell versus paraxial convergence; and strict separation of raw research evidence, existing public-v7 qualification and original-source interpretation. Inspect actual source and final CI artifacts, not only this builder summary. Explicitly distinguish any independent calculations from builder native/Chrome executions.

**Required deliverable:** commit a complete independent Markdown review to the default branch of `physicsvigilante/review_sandbox` at:

`projects/opticsim/pr-177/reviews/review-01-chat-b.md`

Read the committed report back from GitHub. Return its immutable permalink, actual review commit SHA, exact reviewed source SHA and final verdict **CLEARED FOR OWNER DECISION** or **CHANGES REQUESTED**. A chat-only verdict is not the required published review. If publishing fails, explicitly say the GitHub review was not published. Do not modify Opticsim source, approve on behalf of the owner, or merge the PR.

**Builder disposition:** exact-source verification complete; independent review **pending**; PR #177 remains draft and unmerged. This document is the builder's evidence and handoff, not an independent sign-off.
