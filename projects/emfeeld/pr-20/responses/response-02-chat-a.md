# Chat A response 02 — PR #20 targeted R2 review-02 finding disposition

**Date: 2026-11-16 (Asia/Kolkata). Status: R2-NEW-01 independently demonstrated, reproduced locally, corrected in a NEW source head and author-qualified; targeted Chat B review-03 PENDING.** This is the implementer's attributed response, **NOT** an independent reviewer verdict or owner merge approval. Source PR #20 remains draft and unmerged.

## Preserve the original independent review record

- [Original Chat B review 01](../reviews/review-01-chat-b.md) reports **CHANGES REQUESTED**, source head 4b51a833c0ed5ef189becf5881064d1b516df21b; immutable original review blob **3ecb837b03bd6c1644f289a50fa5b33794212fb5**.
- [Chat B review 02](../reviews/review-02-chat-b.md) reports **CHANGES REQUESTED**, exact reviewed corrected source head **145b68fcab75201a6a31876e91c075c3f00bfc8**, tree **6f224d516f25eb7b4f8516cdcd33a596453ee0b4**; original review-02 blob **9cbe288105c0b31f4848ec71f1bd34bbcb6316a0**. Chat B independently closed original F-01 selector binding and F-02 global native consistency and tested F-03's nonboolean controls, but demonstrated **NEW-01 MAJOR** authored numerical-check incoherence. Both reviewer reports remain **byte-for-byte untouched** and tied to their original source heads.
- No source-release, credential, local model or evidence mutation is claimed. This response does not reclassify either review as a pass.

## NEW-01 — reproduced and corrected without new physical laws

**Original demonstrated defect:** The native source check's literal `passed: true` was trusted without re-evaluating its original authors' expected_value and atol/rtol. A re-sealed result could claim a complete field check for a vector **[200,200,200]** against an authored reference **[0,0,0]** with absolute tolerance **100**, even when every component failed the native criterion. A truncated check receipt, forged expected_value or tolerance metadata, or an unattributed check on an otherwise unrequested field also passed the original native preflight. The post-processing comparator and inspector both incorrectly accepted contradictory saved evidence. This was an internal evidence-coherence defect, not a demonstrated force-law/integrator error or a proof of malicious-data authenticity.

**New correction:** [Draft source PR #20](https://github.com/physicsvigilante/emfeeld/pull/20) current head **fb16a233fb73d7e749e08029c848b4b99c5158a7**, canonical Git tree **a9cee83857195f0c2d4c36d4741559094fad64bd**, base main **1b7d5c652bb635723746b3c6ce77baee536b997e**.

Only the existing new comparison module and its tests changed. For **every** native result, not just a selected pair, the preflight now:
1. Requires a corresponding immutable authored expectation before accepting any native numerical-check receipt; rejects unattributed checks.
2. Requires the complete exact native check structure: passed (literal boolean true), expected_value, atol, rtol, criterion, meaning. A mere `{"passed": true}` is not evidence.
3. Reconstructs finite scalar/vector operands from the **captured native request and saved result**, using the already-existing pure native **Decimal-backed componentwise absolute/relative-tolerance predicate**. No source field is re-evaluated and no trajectory is reintegrated.
4. Requires actual recomputed predicate success and **exact canonical native receipt equality**, including the authored reference/tolerances and diagnostic metadata. Contradictions are hard **invalid_native_run** before creating any comparison output.
5. Preserves original F-01/F-02 selector-to-NPZ, field-magnitude, stable particle ID and unselected-result guards; no change to force laws, integration, numerical tolerances, energy diagnostics, renderer, original compare_runs, sweeps or derived-observations contracts.

## Negative first attempts, focused regressions and local qualification

- Original new regression battery against pre-fix source: **14 adverse failures** (unsupported checks were incorrectly accepted) and **one genuine passing-check control**. The red log is preserved in the implementer's first-attempt evidence; it was **not** counted as a pass. Positive case exercises genuine native-generated check receipt.
- After correction, **15/15 new reviewer-derived regressions** passed; combined **60/60 focused comparison tests** passed, including unselected forged field/check rows and trajectory expectation receipts.
- A previous existing test's expected *error-message* pattern was extended to permit an **earlier, more precise rejection** of an unattributed check; the actual strict rejection requirement was unchanged. The **source-only intermediate first hosted commit** failed the older test assertion (1 failed / 1,386 passed), and was not mislabelled as a production numerical failure or final qualified head.
- **Full locally executed headless suite:** **1,402 tests passed**, warnings as errors, on exact source bytes later verified against GitHub's source blob hashes. A separate direct extraction of the exact hosted source snapshot reran **all 60 focused tests** successfully. No unexecuted tests were reported as passed.

## Fresh exact-head hosted CI and independently audited saved artifacts

- Exact qualifying source tree **a9cee83857195f0c2d4c36d4741559094fad64bd**, CI PR merge-preview checkout **fedcba18a8b5713e0a0666c5bb213484220da7f9**, parents qualified base and head, same exact Git tree.
- [Fresh Linux + Windows clean-install CI #43846152822](https://github.com/physicsvigilante/emfeeld/actions/runs/43846152822): **SUCCESS both Ubuntu 24.04 and Windows 2022** at source head fb16a233fb73d7e749e08029c848b4b99c5158a7. Each OS passed **1,402 headless + 18 historical behavioral + 33 real-PyVista = 1,453 suite-membership tests**. The **60 separately rerun comparison tests** duplicate definitions within headless, not 60 additional distinct tests. One old obsolete whole-file freeze guard remains explicitly deselected.
- [Separate real-PyVista qualification #43846152829](https://github.com/physicsvigilante/emfeeld/actions/runs/43846152829): **SUCCESS** (1,402 cumulative tests, real offscreen rendering and slider-event checks).
- [Source snapshot #43846152824](https://github.com/physicsvigilante/emfeeld/actions/runs/43846152824) **SUCCESS**. ZIP artifact ID **14215386156**, original ZIP SHA256 **710c59861c08284844233c50b897fa76d844bcc9300300a98f012ec29ac1e157**, inner tested-source.tar SHA256 **f9f9b116dc75f2aa74935c3a08e7215a4e883253ada696acce67c3fe38fb6a9b**. The source ZIP was downloaded, CRC verified; **all 341 Git blobs** matched source tree identities with zero missing/mismatched files.
- Linux candidate release ZIP ID **14216510570**, SHA256 **50951b9e91bb55daa3be6063d48565d065267932fc739b4e8f60f252fa9c0170**. Windows candidate release ZIP ID **14216267089**, SHA256 **ca825d0e93e4c07f23fc485e8d36e0f9b082be3468689647deb4c471034d2415**. **Both originals downloaded and independently SHA256 and CRC checked**: 1,803 entries each, no checksum/duplicate-name errors, exact CI checkout pin.
- Per OS a read-only audit checked **six complete sealed native runs**, **six nested native inventories**, **30 native input SHA bindings**, and **nine sealed top-level run/comparison inventories**. Same-author independent-source/RK4 E1/G1/T1 numerical references passed: **10 static source-formula checks + six trajectory comparisons**.
- The corrected read-only inspector was separately rerun against **all six archived model-run/comparison outputs from the new candidate** (Linux and Windows): **E1 5 complete, G1 7 complete + 1 genuinely unavailable added body, T1 4 complete** per OS. Previously archived E1/G1/T1 results also retained their original meaning without modification.
- These are **author-run/source CI and archive-integrity evidence, not Chat B's new independent review**. Independent reviewer-authored cases and physical references remain separately attributed to Chat B's reports.

## Residual scope and next gate

The new native expectation predicate validates **internal consistency between saved result, immutable request and check receipt** under unkeyed file inventories. It cannot authenticate an external source against a hostile writer who can alter and re-seal *every* raw input; no new cryptographic signature, general physics solver, native Windows pointer test or classroom evaluation is claimed. The physical regime remains prescribed static sources with independent nonrelativistic test particles.

**NEXT:** publish [FOLLOW-UP-03](../FOLLOW-UP-03.md) and [REVIEWER-PROMPT-03](../REVIEWER-PROMPT-03.md) for Chat B to independently re-test **NEW-01** on exact head fb16a233... and selectively replay F-01/F-02/F-03. Only Chat B creates **a new reviews/review-03-chat-b.md** with scoped pass / changes-requested / insufficient-evidence; this response is not a substitute.

**No merge authorization exists.** PR #20 remains draft and unmerged until independent targeted re-review is resolved **and** the owner gives a separate explicit merge approval. Post-merge full Linux/Windows and real-PyVista CI and an append-only release report would follow only an authorized merge. User's Conda installation, saved models and teaching evaluation remain untouched.
