# Chat B — SIM_HEAT PR #52 targeted independent R2, PR51 F-01 provenance integer types

Continue as independent Chat B reviewer for the active-main audit correction.

Your [original PR51 review](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-51/reviews/review-01-chat-b.md) returned **CHANGES REQUESTED** for major F-01: steady S1 and campaign D2_K2 adapters accept incorrectly typed JSON `canonicalSamples`, `samples`, and `duplicateRowsCollapsed` because `True == 1` / `1.0 == 1`. Keep the old PR51 verdict intact.

Review the separate **DRAFT PR #52**:
https://github.com/physicsvigilante/sim_heat/pull/52

**New exact HEAD `e78ec2ccb2f8f97bbc1b282ec6bbe2847c1e1603`**, Git tree `2ad10a1679d528f88030494f0349171502ef8e0f`, immediate base original PR51 `52d693a748ad3709c99215bac0a5840a236937a6`.

Full central request:
https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-52/REQUEST.md

Source diff is **five paths only:** two modified steady/campaign archive adapters + new typed-negative tests/scope/CI. Verify in both real adapter code paths that each of three original integer-valued metadata fields demands **`type(value) is int`** before comparing original expected count, rejecting Boolean, float, missing, null, string, even when equal as Python numbers.

Independently test/reproduce correct integer-positive original archived S1 and D2_K2 and wrong-type mutants **using disposable test-only rehashed ZIP copies**, not a claim of compromised original GitHub evidence. New CI tests use a synthetic D1 campaign fixture to exercise the real campaign adapter; original actual six published diagnostic archives are **separately replayed** unchanged. No real native action. Check emitted results remain `diagnostic_only/nativeQualified=false` and that externally authenticated GitHub archive identity is not inferred from caller-supplied SHA strings alone.

Verify exact-head [CI #44232637466](https://github.com/physicsvigilante/sim_heat/actions/runs/44232637466) and [artifact #14396095895](https://github.com/physicsvigilante/sim_heat/actions/runs/44232637466/artifacts/14396095895): ZIP **5,874,322 bytes**, whole SHA-256 `2c22dd3db778942227acec29364819e73bd0a0822b006a7b5cc9bfc4a1555d36`, **34/34 member CRC valid**, **249 hosted offline tests passed, one optional skipped**, plus nine targeted tests (included in full adapter test total, do not double count); six original native diagnostic case bundles replay **BYTE_IDENTICAL**, full explorer Chromium smoke passed. Preserve the intermediate **FAILED** #44232475551 (test fixture setup) and earlier #44232238318 (PASS with unintended duplicate test collection), and distinguish personally executed tests from inspected hosted records.

Original frozen physical model, scientific output data, checking references, source plan and compiler permissions untouched. Original C1 F0 precision 80× vs required >=100× **FAIL**, PR32 original reference bitwise-regeneration **FAIL**, all 11 real native release gates still missing and nine C1 native values uncomputed. **Do not merge main or historical PRs and never invoke OpenModelica or regenerate frozen references**.

Commit a **NEW independent** report directly to `physicsvigilante/review_sandbox/projects/sim_heat/pr-52/reviews/review-01-chat-b.md` with **SCOPED PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE**, exact reviewed HEAD/tree, personally tested probes and limited verdict. No Chat A-authored independent reviewer outcome. A scoped PASS endorses only correction of F-01 and original data preservation; a production merge remains a separate owner decision.