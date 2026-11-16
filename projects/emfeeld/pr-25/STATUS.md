# CURRENT PR #25 STATUS — R1 REVIEW 01 CHANGES REQUESTED; CORRECTIONS UNDER QUALIFICATION

**2026-11-16 (Asia/Kolkata): [independent Chat B review-01](reviews/review-01-chat-b.md) = CHANGES REQUESTED** on original head `4fe896ff6bb98d21a090bc16a84fe26145f9f5e7` / tree `4df3703346ec7cba1ab74fcd6daa40796a535bf3`. Two independently demonstrated findings: **F1** screenshot inside a foreign sealed saved run corrupts its inventory; **F2** fresh baseline and legal member literally called `baseline` share ambiguous selector display/run_id. Prior R1 reviewer evidence and negative attempts remain unchanged.

**Implementer correction:** [response-01](responses/response-01-chat-a.md), current source PR #25 **OPEN / DRAFT / UNMERGED** at head **`a56b4680a90647ad4af03a52a0b9053807d10a7b`**, corrected Git tree **`ce20aa49d978c94150edbbf017d8fae1e2f6f896`**, unchanged qualified base **`bf6a18399c604136dd363ad94d40557dbe2c2543`**, current CI merge-preview **`7b04fc27b6a4e0efaf74045734389af416ec9223`** with same tree. Correction rejects screenshots under any recognizable sealed evidence ancestor, distinguishes baseline/member IDs and returns exact run path/reference/hash, and adds reviewer-derived regressions. Earlier native records are never edited or renamed.

**Independently verified corrected source snapshot:** [GitHub workflow #43896101372](https://github.com/physicsvigilante/emfeeld/actions/runs/43896101372) SUCCESS, original snapshot ZIP artifact **14238767336**, ZIP SHA256 **`adb773b583db0f94d61c75c230cb98574378e6ca53d444650ef86e6a5a0e8c4a`** matches direct original upload log and downloaded bytes, CRC clean. Original tested-source.tar SHA256 **`d92de608f8aa2e9e66a99fe9164f2dc3fda6e516396635095c52a6be02503725`**; isolated 346-file Git reconstruction yields exact corrected tree. From the extracted **unchanged** source, **62 focused tests passed `-W error`**, first local focused log SHA256 **`afcf59fa9ebb338ef7c616ee23697602e34ff85f43633573e1753413c682d328`**. The new full headless/historical local regression is in progress at this status revision.

**Fresh exact-head source CI:** [Linux/Windows clean-install #43896101641](https://github.com/physicsvigilante/emfeeld/actions/runs/43896101641) and [separate real-PyVista #43896101195](https://github.com/physicsvigilante/emfeeld/actions/runs/43896101195) were **IN PROGRESS** at this status revision. No final green CI or new release ZIP/visual audit may be inferred yet. The original earlier-head 1,456/18/33 and screenshots are historical and not substitute for new-source qualification.

**Next required gate:** after current-head full CI and original release archive audit, publish an exact-head focused follow-up for Chat B to independently retest the two corrections and representative read-only viewer regressions. **Do not merge while reviewer finding remains changes-requested.** Manual Windows pointer, classroom usefulness, cryptographic adversarial sealing and distributed ACID remain outside scope.

---

## Historical preceding statuses (preserved)

# CURRENT PR #25 DISPOSITION — AUTHOR-QUALIFIED, INDEPENDENT R1 REVIEW PENDING (2026-11-16 Asia/Kolkata)

**Source [PR #25](https://github.com/physicsvigilante/emfeeld/pull/25) remains OPEN / DRAFT / UNMERGED.** Its source head is exactly `4fe896ff6bb98d21a090bc16a84fe26145f9f5e7`, Git tree `4df3703346ec7cba1ab74fcd6daa40796a535bf3`, qualified base `bf6a18399c604136dd363ad94d40557dbe2c2543`, preview `75f818bdb199ad97ae036bd1dea380f03d7e71f6` with identical tree. **Do not merge until focused Chat B review.**

**All exact-head author CI has now passed**: [Linux/Windows clean install #43886746384](https://github.com/physicsvigilante/emfeeld/actions/runs/43886746384) SUCCESS on both Ubuntu 24.04 and Windows 2022 (each **1,456 headless +18 current historical +33 real-PyVista; 54 repeated focused ensemble tests already counted inside headless**); [separate real-PyVista #43886746161](https://github.com/physicsvigilante/emfeeld/actions/runs/43886746161) SUCCESS; [source snapshot #43886746421](https://github.com/physicsvigilante/emfeeld/actions/runs/43886746421) SUCCESS and its original 346-file Git tree reconstructed.

The two **original post-CI release ZIPs** have been independently downloaded and verified by Chat A (not Chat B): Linux SHA256 `573b23020f3b2d5471152242352a017b18e05761cb6afdbb7ad7fea714ca44ec`, Windows SHA256 `6182044d7b103ba4e8e0f46e1c9501228977d760259508cd08f295bfc7417ad8`. Both: **2,157 unique CRC-clean files**, 21 sealed inventories, 12 nested native seals, 60 run input-hash bindings, six sealed comparisons, 32 successful and two legitimately unavailable G1 measurements, plus E1/G1 native baseline/member view screenshots hash-bound to complete recorded runs. Separate viewer ZIP passes its 17 screenshot hashes. [Detailed original artifact and first-attempt audit](AUTHOR-ARCHIVE-AUDIT-01.md).

**CURRENT targeted independent handoff:** [REVIEWER-PROMPT-02.md](REVIEWER-PROMPT-02.md). Earlier [REQUEST.md](REQUEST.md) and [REVIEWER-PROMPT-01.md](REVIEWER-PROMPT-01.md) were recorded while Windows was still running and their pending-CI statements are **historical**, superseded by the verified outcomes above. **No Chat B report is recorded yet; do not self-label author qualification as independent R1 pass.** Manual Windows mouse/desktop use, real teacher acceptance, malicious hash-sealer threat resistance and distributed ACID are not qualified.

---

## Earlier provisional statuses (preserved unchanged)

# EM Fields PR #25 — initial R1 review status (2026-11-16 Asia/Kolkata)

**DRAFT / UNMERGED. INDEPENDENT REVIEW PENDING.** Exact source head `4fe896ff6bb98d21a090bc16a84fe26145f9f5e7`, qualified base `bf6a18399c604136dd363ad94d40557dbe2c2543`. [PR #25](https://github.com/physicsvigilante/emfeeld/pull/25) adds read-only verified native ensemble view selection; changes four files, no solver/field-law changes. Initial [REQUEST](REQUEST.md) and [Chat B reviewer prompt](REVIEWER-PROMPT-01.md) record explicit adversarial scope and physical/evidence limitations.

**Original exact-head PR CI observed:** [Linux/Windows release #43886746384](https://github.com/physicsvigilante/emfeeld/actions/runs/43886746384): Linux SUCCESS (1,456 headless, 18 historical, 33 real-PyVista, 54 repeat focused included in headless); Windows **IN PROGRESS** at creation of this status. [Separate real PyVista #43886746161](https://github.com/physicsvigilante/emfeeld/actions/runs/43886746161) SUCCESS; [source snapshot #43886746421](https://github.com/physicsvigilante/emfeeld/actions/runs/43886746421) SUCCESS. Original workflow logs were inspected, but new release ZIP contents have not been audited here.

**No independent review report is yet published.** No R1 PASS may be inferred from author tests, green CI or these handoff files. Require exact-head completed Windows qualification and a scoped independently executed review before any non-draft or merge transition; post-merge main-push CI and artifact re-audit would then remain separate.

Historical prior milestone PR #23 **is merged and fully post-merge qualified** within its declared automated and archive evidence scope; [final release record](../pr-23/MERGE-REPORT.md). No manual Windows pointer, human independent physics certification or classroom outcome was established.

## Follow-up 01 — exact-head Windows qualification completed (2026-11-16 Asia/Kolkata)

The status at initial packet creation above was accurate at that moment. Subsequently, the [exact-head Linux/Windows clean-install workflow #43886746384](https://github.com/physicsvigilante/emfeeld/actions/runs/43886746384) **COMPLETED SUCCESS on both OSs** for merge preview `75f818bdb199ad97ae036bd1dea380f03d7e71f6` from source head `4fe896ff6bb98d21a090bc16a84fe26145f9f5e7` and qualified main `bf6a18399c604136dd363ad94d40557dbe2c2543`. Directly fetched original logs for both jobs:

- **Ubuntu 24.04 job 133366826330:** 1,456 headless passed, 18 historical behavioral passed (one historical whole-file freeze guard deselected), 33 real-PyVista passed, 54 focused ensemble passed (subset of 1,456); both E1 baseline and G1 native-complete partial-comparison member screenshot commands completed.
- **Windows 2022 job 133366825905:** same accounting: 1,456 headless passed, 18 behavioral passed (one deselected), 33 viewer passed, 54 focused rerun passed; both new screenshot command steps completed.
- Original job upload-log release ZIP digests: Linux artifact `14236425127`, SHA256 `573b23020f3b2d5471152242352a017b18e05761cb6afdbb7ad7fea714ca44ec`; Windows artifact `14235259284`, SHA256 `6182044d7b103ba4e8e0f46e1c9501228977d760259508cd08f295bfc7417ad8`.
- Separate real-PyVista job **133366824764** and source snapshot job **133366825776** passed; original viewer ZIP artifact `14235366567`, SHA256 `cd2161bd32869fd03acfddcc8fd321d68f6d84fb620708fa57b7c875d0fc0acb`; original source ZIP artifact `14235101355`, SHA256 `c23454c0d0993202bf4b717fb4524f5b8fc56849a32ca131b9228d720d77596f`.
- These digest values are read from the **upload logs**, not independently rehashed downloaded ZIP bytes in this conversation. Archive internal CRC/native receipt audit and independently executed reviewer cases remain outstanding.

**Disposition: AUTHOR CI GREEN on exact head; R1 INDEPENDENT REVIEW PENDING, PR DRAFT/UNMERGED.** No source merge authorized by CI or this status note.

