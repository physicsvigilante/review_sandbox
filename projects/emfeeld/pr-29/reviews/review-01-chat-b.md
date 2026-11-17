# Independent Chat B R1 review 01 — emfeeld PR #29

**Verdict: PASS (scoped R1), not merge authorization.** Date: 2026-11-17 Asia/Kolkata. Independent reviewer-authored executable checks; original GitHub artifacts. No source PR change, merge, or historical-review overwrite.

## Frozen source
- PR: https://github.com/physicsvigilante/emfeeld/pull/29 — checked OPEN, DRAFT, UNMERGED.
- Head: `1ae4e327caf2c600466185b17c68521f5217bd0c`; exact Git tree: `3d9fa4c8b594e46837e6825590e4e5d72db9a030`; qualified base `fbdf66e56b3a89a5cf1bea6c0b403c9fc8d9ebcd`.
- Preview `f20da4c198b542257d60f8e0264b73364d48d750` has the same tree, ordered parents [qualified base, corrected head]. Original correction changed only scenario_ensembles.py (+8/-1) and its tests (+47). Verified source/test Git blob SHA values `73dd762753463ed38c167fb3337cca9c93dfb10c` and `0708e9e79234c11999f2ed9e652a90ee8eeac1c6`.
- Read complete REQUEST.md, reviewer prompt, author response and archive audit, Issue #28, PROTOCOL.md, REVIEW-RISK-POLICY.md, source AGENTS.md and exact-head table contract, plus prior PR #27 B1 review. Scope is strictly formatting after the original verified native comparison readout, not new physics.

## Independently downloaded original artifacts
| Artifact ID | Verified original ZIP SHA256 | Reviewer check |
|---|---|---|
| Source snapshot 14261874488 | `c6957f35865eb92d4e35154ac95cce70432463e26fab0ee08f9156700a01349a` | CRC clean, inner tar SHA `196223971ac045774c3a7bf617d0ac3829ce0fceccc33e348b84e6700d786c89`, 348 tracked Git files independently reconstructed to pinned tree |
| Linux release 14263541683 | `0ce585126fc538fefe8f09a5d26968b5caa2958cf11b6d9330554c4905d8ccfb` | 2,161 unique CRC-clean entries |
| Windows release 14265405493 | `44b93d0bf5070c41479c9f58be47480d1e1a3de5f252d9ec2f9b4cf2f596f226` | 2,161 unique CRC-clean entries |
| PyVista 14262848668 | `1903765021f9b287f5ffffa53111f93f84ceb9379d2b2bbe9e9098573909a471` | 22 CRC-clean entries, 9 recorded offscreen cases, all 17 1200x850 PNG hash receipts matched (16 distinct images) |

Each original OS archive independently audited: **33 valid original inventories / 450 file hash bindings, 12 complete native runs, 60 five-input native hashes, 6 original accepted proposal hashes and store bytes, 6 sealed comparisons, 32 signed numeric ok results and 2 genuine unavailable/unknown_operand/null results**. Original native operands independently subtracted right-minus-left; units, IDs, vector ordering, sample/time/endpoint/particle contexts and saved request/result/integrity and left/right run hashes checked against each displayed row. This confirms saved-source arithmetic/provenance, not independent field law or integrator certification.

Original hosted exact-head CI metadata checked: Linux/Windows #43941771034 SUCCESS (each original log: 1498 headless + 18 historical behavioral + 33 real-PyVista; 96 focused subset of headless), PyVista #43941771047 SUCCESS; source snapshot #43941771200 SUCCESS. These are author/hosted, not reviewer-written test counts.

## New independent reviewer execution
Host Linux Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0, pytest 9.0.2; no local PyVista installation. Extracted original pinned source; all reviewer scripts/test fixtures **outside frozen source and saved originals**. Tests use `PYTHONPATH=<pinned>/src`, `PYTHONDONTWRITEBYTECODE=1`, `pytest -W error`. **42 NEW parametrized reviewer-written cases PASSED** in three disjoint completed batches:
- 13 archive/source/numerical/CLI/novel-native probes, log SHA256 `f94a9e8910cc15e1de8cf73c381b183bade302e89aa1e80d9c7feb3e49a21d42`.
- 15 tamper/invalid CLI/no-write probes, log SHA256 `5186172f89de5eaae71a5df8c06a8fde2720393346a06e8c1026c5e665c1dd2d`.
- 14 late integrity, Markdown injection, codepage, history/compatibility probes, log SHA256 `498a0e2c60654da27ded28acd3c491bf89d0afb6fb25d233fa7ac113c8c5d84b`.
Reviewer-generated native fixture first-run log SHA256 `6a8781c190bb295f00886ca16a78be5e828665ac2de7105feb9f0d55c6e932b8`.

**Observed:** independently authored four-member native ensemble, with a genuine *third* member literally named `baseline`, produced 20 comparisons and distinct right member vs fresh left baseline; selected member table correct. Separate three-member native fixture retained one complete, one native-incomplete, one rejected sibling without invented results; selecting healthy member still exit 1/global partial. Both original OS E1 (exit 0), G1 selected B (exit 1 and unavailable operand), T1 (exit 0) readouts passed real CLI under redirected `PYTHONIOENCODING=cp1252`; original E1/G1 Markdown reproduced byte-for-byte **within each OS**, not falsely across OS (G1 4721/4720 bytes). Strict CP1252 `TextIOWrapper(BytesIO)` and text-only `StringIO` fallback also passed, retaining signs.

The original Windows old-head failure was separately checked in original workflow #43937937426 job 133547385832: `'charmap' codec can't encode character '\\u2212'`, exit 2 at redirected output. This is preserved historical genuine failure, not a current-head bug.

Five *presentation-only in-memory* adversarial sets (pipes, CR/LF, Markdown/JS links, HTML/script/image tags, backticks, www. autolinks, Unicode, email, extreme floats and -0.0) produced single-line inert cells and fixed 12-column measurement / 9-column receipt tables with original number spelling. Original sealed files were never injected/changed. Actual selected/unselected comparison/proposal/store/template tampering and falsified outer hash binding refused with exit 2/empty stdout; no extra writes. Two original PR #27 B1 timing windows independently injected post-inspection whitespace drift in selected comparison integrity.json; both refused with zero table output, as did late outer manifest drift. Invalid flags/selectors, static/trajectory mismatch, raw JSON `1e400`, foreign saved evidence screenshot destination refused. Existing inspect/measurements behavior rechecked.

## First attempts and limitations
Preserved reviewer early ad-hoc `AttributeError` while incorrectly assuming a missing operand was a dict; G1 genuinely contains null. First combined run timed out with no summary (log SHA `a0da5c4ab7de46a4f35c8f58ad634728c6824a1481951110d7610117a6b5fc38`). First targeted tamper batch **3 passed, 1 failed** (log SHA `a8084de1a955788a942dce54cd19d5c4cbcf0efb519315ff341edfc573c85edf`): reviewer test incorrectly demanded that whitespace appended to the *initial, externally unauthenticated root integrity manifest* be detected. It is not promised by the documented unkeyed seal. Reviewer-only test was corrected to falsify an actual root hash binding; source unchanged, full targeted green batch passed. A later all-in-one suite also timed out with no final summary (partial log SHA `fe306aa2f8ad07f4abb196292f14762bd388b47d55b83d91a796b4c7719e9cac`). These timeouts are **not** counted as full passes.

Remaining limits: unkeyed root manifest cannot authenticate malicious complete re-sealing; no distributed concurrent filesystem ACID; no fresh local real-PyVista or manual Windows mouse/slider; static Markdown checks are not an interactive renderer certification; no new law/integrator qualification, human physicist or classroom usefulness claim.

## Decision
**PASS — focused R1 presentation, UTF-8 Windows codepage correction, signed sealed evidence meaning, read-only/integrity refusal**, on pinned source only. No confirmed source blocker; no evidence meaning change warranting R2. **Source PR stays draft/unmerged.** Chat A must separately check exact head/base/CI, obtain owner merge authorization, and perform fresh post-merge main Linux/Windows/PyVista qualification and original archive audits. A moved head requires renewed source-bound evaluation.

**Owner handoff:** return to Chat A and say **“review done”**.
