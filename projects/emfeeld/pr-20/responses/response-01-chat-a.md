# Chat A response 01 — PR #20 R2 changes-requested disposition and correction

**Date:** 2026-11-16 (Asia/Kolkata). **Status:** all three independent Chat B findings **reproduced/accepted and addressed in new source changes**, fresh exact-head Linux/Windows + real-PyVista author CI successful, **TARGETED CHAT B RE-REVIEW STILL REQUIRED**. Source PR #20 remains **draft and unmerged**, and the owner has **not** authorized source merge. This is an implementer response, **not** an independent reviewer verdict.

## Immutable original review identity

- [Chat B review 01](../reviews/review-01-chat-b.md), verdict **changes-requested**, is unchanged, exact source head **4b51a833c0ed5ef189becf5881064d1b516df21b**, canonical Git tree **8e8999b40949d1128050cf66c0440fb07bb08670**; original review Git blob **3ecb837b03bd6c1644f289a50fa5b33794212fb5**.
- The independently executed reviewer reproduced the original evidence-inconsistency attacks on disposable copies, not on released source/run files. The original reviewer and author first-attempt failures are preserved and must not be represented as passes.
- [Exact correction diff](https://github.com/physicsvigilante/emfeeld/compare/4b51a833c0ed5ef189becf5881064d1b516df21b...145b68fcab75201a6a31876e91c075c3f00b0fc8) contains **two changed files only**: src/emfeeld/scenario_comparisons.py (+121/-5 lines) and tests/test_scenario_comparisons.py (+118 lines). No physics, integrator, numerical tolerance, existing model/sweep/derived observation API, dependency, viewer or workflow code was altered in this correction.

## F-01 — blocker reproduced and corrected

The author independently reproduced Chat B's exact E1 counterexample on copied original Linux native evidence: both reports were re-sealed to point to valid NPZ row 0/time 0.0 s, while the immutable native requests still specified saved indices at time 2.0 s. **Original source incorrectly reported comparison and inspection complete at 0.0 s.** This is a demonstrated integrity-semantic defect, not a general solver failure.

Corrected source verifies **every successful recorded trajectory sample** against its pinned native packet selector and the NPZ time grid, state, actual time and time offset:
- Explicit sample_index must be identical to the original native requested index.
- Explicit exact-time selector must identify the exact saved time on the original grid.
- Explicit nearest-time selector must reproduce native earlier-index tie-breaking, requested tolerance, selected index and computed time_offset_s.
- Original reported quantity, SI unit, stable named physical ID and index bindings must remain valid. Invalid trace evidence is rejected as **invalid_native_run** before any comparison result directory is created, rather than reclassified unavailable or silently compared.

The original copied E1 attack against corrected exact hosted source now fails with **invalid_native_run** and no output directory, matching the reviewer's requested behavior. New regression tests cover both one-sided and coordinated report modifications, exact/nearest time selectors and forged offsets.

## F-02 — major corrected through global native-run preflight

The original comparator checked NPZ consistency only when a trajectory comparison selected the sample, and field vector/magnitude consistency only for a selected field_magnitude pair. A complete native run could therefore be accepted despite an unselected, re-sealed contradictory result.

Corrected common source preflight validates **all** successful recorded trajectory_sample observations against the actual selected NPZ row (including saved position, velocity, time, speed and energy quantities), even if the requested comparison uses only a field observation. It also checks every native field row's finite three-vector, domain-specific unit, nonnegative saved magnitude and robust vector norm agreement using the preexisting relative tolerance **1e-12 with zero absolute floor**. Corrupted full-source evidence fails as **invalid_native_run** before output creation; genuinely absent requested observation IDs remain correctly **unavailable/unknown_operand** when both source runs are sound. Negative tests re-seal unselected trajectory values and unselected field magnitude under valid outer hashes, then request only field vectors.

This is evidence-only validation, not field re-evaluation or a new physics solver.

## F-03 — minor corrected, check flag interpretation

If a native row has a check receipt, the corrected preflight requires an object whose passed member **is literally boolean true**; integer 0/1, false, null or string values are rejected, and an authored expectation without a check is rejected. The pre-fix explicit Python identity comparison only refused the exact boolean false and could incorrectly accept the integer zero. Added tests cover 0, 1, the string true, null and false. This correction does not certify externally re-signed native data or change any authored check tolerance.

## First attempts and new author qualification

- The newly authored focused regression set was run against the original reviewed source: **11 failed as expected and one passed** (the boolean-false case was already refused). This is deliberate negative evidence, not a successful pre-fix regression run. The first Chat B report and its own failed/refined tests remain immutable.
- After source changes, **45 focused comparison tests passed** with warnings as errors. One local all-headless attempt reached approximately 25% then hit an execution limit; **no local full-suite pass is claimed**.
- Hosted exact source snapshot [run #43837372230](https://github.com/physicsvigilante/emfeeld/actions/runs/43837372230) was downloaded; the **341 archived files all matched Git blob SHA-1 identities**, and all 45 focused tests passed when rerun against the extracted exact source.
- Corrected source head **145b68fcab75201a6a31876e91c075c3f00b0fc8**, canonical Git tree **6f224d516f25eb7b4f8516cdcd33a596453ee0b4**, base **1b7d5c652bb635723746b3c6ce77baee536b997e**. CI merge-preview checkout **f34acd2db9cfa76883ccd3803fed438b816d87f0** has the exact same tree as source head. PR #20 is draft/unmerged.
- [Fresh full Linux/Windows clean-install release #43837372118](https://github.com/physicsvigilante/emfeeld/actions/runs/43837372118): **SUCCESS on Ubuntu 24.04 and Windows 2022**, **1,387 headless + 18 historical behavioral + 33 real-PyVista = 1,438 test-suite memberships per OS**. The 45 separately rerun focused comparison tests are included in headless, not extra distinct tests. One unchanged obsolete whole-file freeze assertion remains deselected.
- [Separate real-PyVista workflow #43837372318](https://github.com/physicsvigilante/emfeeld/actions/runs/43837372318): **SUCCESS**, including 1,387 cumulative tests and real offscreen renderer/slider checks.
- Exact-head source archive original ZIP ID **14210464378**, SHA256 **6bfdaf9396e7af69c68491ce8207ab29f03b5a8c27ea13242efac896d52620ab**; inner tested-source.tar SHA256 **7566331fd305aedfc449fe04a4a8758571a935c088c943daa88bb637eb8b711a**. All 341 Git blobs verified.
- **Linux release ZIP ID 14210979876**, raw SHA256 **e97ab64829313508eb3b7b86bedfaf22a87c8a855cf0699b0acab6b6ef7661bf**; **Windows release ZIP ID 14212013323**, raw SHA256 **eefb8c2144d8fd2af4aaf1cd49ee9b959205ee93b36555173a0c02337656eae4**. Both original ZIPs downloaded and independently rehashed/CRC checked: **1,803 entries each**, no duplicate or corrupt names, exact CI merge-preview head pin.
- Each Linux/Windows ZIP passed **six sealed complete native-run inventories, six nested native inventories, 30 run input hashes, nine top-level native-run/comparison inventories** and saved source root/revision bindings. Qualified E1/G1/T1 comparisons still yield **16 fulfilled and 1 deliberately unavailable** body-3 baseline result, with **10 static source-formula and six native-trajectory numerical references** per OS. A corrected read-only inspector also successfully revalidated all six original pre-correction archived Linux/Windows E1/G1/T1 outputs, without changing them.

The reference code and hosted suites are **author-authored/self-qualified evidence**, not a second independent Chat B review or human certification.

## Remaining explicit R2 review and merge gates

**No source blocker is claimed resolved by independent Chat B yet.** Publish [targeted re-review request 02](../FOLLOW-UP-02.md) and [reviewer prompt 02](../REVIEWER-PROMPT-02.md); only a separate Chat B conversation may author a **new review-02-chat-b.md** tied to corrected head/tree, independently executing the specific A1/A2/A3/A4/A6 attacks and checking new preflight semantics. Old first reviewer report must remain intact. Re-review of F-01–F-03 is the current gate, not a broad invented acceptance claim.

Even if targeted review passes, the owner must separately approve source PR #20 merge. An approved merge then requires fresh main-branch Linux/Windows and separate real-PyVista qualification plus append-only final MERGE-REPORT. No local Conda/user saved model changes, classroom evaluation, distributed/hostile-writer authenticity, new physical laws or manual Windows desktop interaction are asserted.
