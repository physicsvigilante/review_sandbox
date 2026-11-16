# EM Fields PR #25 — author-side exact-head CI and original ZIP evidence audit 01

**Recorded 2026-11-16 (Asia/Kolkata). Status: AUTHOR-QUALIFIED; INDEPENDENT R1 REVIEW PENDING.** This is a Chat A-side read-only verification and **not** an independent Chat B or human certification. Do not merge on the basis of this report.

## Exact source identity and frozen review boundary

- [Source PR #25](https://github.com/physicsvigilante/emfeeld/pull/25) is **OPEN/DRAFT/UNMERGED** on `feature/verified-ensemble-view-v1`; base qualified `main` SHA **`bf6a18399c604136dd363ad94d40557dbe2c2543`**, head **`4fe896ff6bb98d21a090bc16a84fe26145f9f5e7`**, Git tree **`4df3703346ec7cba1ab74fcd6daa40796a535bf3`**. Pull-request CI merge-preview **`75f818bdb199ad97ae036bd1dea380f03d7e71f6`** independently queried: parents precisely qualified base then source head, exact same tree. No source or PR-merge mutation in this audit.
- Four changed paths: `src/emfeeld/scenario_ensembles.py` (Git blob `d351d19fca5026f848411ec7a9b16395a66a25e1`), `tests/test_scenario_ensembles.py` (`2d01fbff7a045b17cc2d18701e97e22468a6ddb4`), `.github/workflows/release-candidate.yml` (`bc24774d53749b9c0ff3d1a55577c94de4d5a773`), and `README.md` (`3c83ab002f19f67e3a87e91876bd739f0e113716`). All originally uploaded blobs matched locally tested files.
- Source snapshot [#43886746421](https://github.com/physicsvigilante/emfeeld/actions/runs/43886746421) **SUCCESS**, artifact ID **14235101355**. Original downloaded ZIP SHA256 **`c23454c0d0993202bf4b717fb4524f5b8fc56849a32ca131b9228d720d77596f`**, `tested-source.tar` SHA256 **`230a9655255aaa49420a0e25cb5b13e2f75d26e79d4f3fe3a014ac735dbc2d44`**. The 346 tracked files were reconstructed into a disposable Git index and `git write-tree` independently reproduced **`4df3703346ec7cba1ab74fcd6daa40796a535bf3`**; 180 relevant regressions and compilation were rerun from this extracted exact-hosted source with no source patches.

## Fresh CI at exact PR head/identical-tree merge preview

| CI | Original workflow | Host result and recorded tests |
|---|---|---|
| Linux clean install | [#43886746384](https://github.com/physicsvigilante/emfeeld/actions/runs/43886746384), job **133366826330**, Ubuntu 24.04 / Python 3.13.5 | **SUCCESS**, 1,456 current headless, 18 historical behavioral (1 old whole-file guard deselected), 33 real-PyVista, 54 focused ensemble re-run |
| Windows clean install | same workflow, job **133366825905**, Windows 2022 / Python 3.13.5 | **SUCCESS**, 1,456 current headless, 18 historical behavioral (1 old guard deselected), 33 real-PyVista, 54 focused ensemble re-run |
| Separate Linux real-PyVista | [#43886746161](https://github.com/physicsvigilante/emfeeld/actions/runs/43886746161), job **133366824764** | **SUCCESS**, 1,456 headless tests, nine offscreen rendered scenes, real VTK slider-event checks; not a manual Windows UI test |
| Exact source snapshot | [#43886746421](https://github.com/physicsvigilante/emfeeld/actions/runs/43886746421) | **SUCCESS**; source artifact reconstructed to exact Git tree |

The 54 focused definitions include the 33 previous ensemble definitions plus 21 added R1 tests; the 54 focused rerun is **already within** the 1,456 headless definitions and is not 54 new distinct tests. Cross-OS execution repeats the same definitions, rather than creating new independent test definitions.

## Original downloaded artifact SHA256 / ZIP audit

The original GitHub Actions ZIPs were downloaded **after CI**, hashed over their raw downloaded bytes, and compared to each upload SHA256 in the **original job logs**; archive member uniqueness, CRC and path traversal were checked read-only.

| Original ZIP | Artifact ID | ZIP SHA256 | Entries | Result |
|---|---:|---|---:|---|
| [Linux RC](https://github.com/physicsvigilante/emfeeld/actions/runs/43886746384/artifacts/14236425127) | `14236425127` | `573b23020f3b2d5471152242352a017b18e05761cb6afdbb7ad7fea714ca44ec` | 2,157 | all unique / CRC clean |
| [Windows RC](https://github.com/physicsvigilante/emfeeld/actions/runs/43886746384/artifacts/14235259284) | `14235259284` | `6182044d7b103ba4e8e0f46e1c9501228977d760259508cd08f295bfc7417ad8` | 2,157 | all unique / CRC clean |
| [Separate viewer](https://github.com/physicsvigilante/emfeeld/actions/runs/43886746161/artifacts/14235366567) | `14235366567` | `cd2161bd32869fd03acfddcc8fd321d68f6d84fb620708fa57b7c875d0fc0acb` | 22 | all unique / CRC clean; 17 saved screenshot SHA256 bindings |
| [Source snapshot](https://github.com/physicsvigilante/emfeeld/actions/runs/43886746421/artifacts/14235101355) | `14235101355` | `c23454c0d0993202bf4b717fb4524f5b8fc56849a32ca131b9228d720d77596f` | 4 | CRC clean; embedded tracked TAR and Git tree verified |

For **each** Linux and Windows release ZIP, a separate local read-only verification independently rehashed **21 sealed top-level inventories**, **12 native integrity inventories**, **60 saved native run input SHA256 bindings** across **12 complete native runs**, and the six source-pinned sealed cross-scenario comparison requests/results. Original native-store proposal JSON bytes and stored decision SHA256 matched for all accepted siblings. E1 complete, T1 complete, G1 expected partial because two baseline bodies are truly absent: exactly **32 fulfilled / 2 unavailable** measurements per OS. Same-author E1/G1/T1 source/RK4 checker recorded **20 static +12 trajectory reference comparisons and two expected unavailable** per OS; this checker is not re-labelled as a separate independent reviewer numerical investigation.

### Two NEW recorded native-view captures on both operating systems

Both original OS archives contain six new files: two fresh PNG images `frame.png`, their native `presentation.json` receipts and their CLI stdout logs. Each PNG is 1200×850, decoded, nonblank, and has an exact raw-byte SHA256 match to `presentation.json.frame_sha256`. The saved `presentation.json.run_integrity_sha256` matches the **original recorded native run/integrity.json bytes**; native `run_id` and physical `reference` match the same sealed run and echoed CLI selection. The captured time is the actual saved **0 s** state, not reintegration.

| Captured view | Source native run | Linux PNG SHA256 | Windows PNG SHA256 |
|---|---|---|---|
| E1 **`--baseline`** | E1 original-root fresh ensemble baseline, complete | `8ca503af4673d9d547b4ce919140a3afd1d6638f3112fbe02ac1fe62132b2b8f` | `364b2018f3db54ee5a3d7c5d4d28891ff985f96e7c041d4c4cbac3bb3794013a` |
| G1 **`--member hypothesis-B`** | G1 accepted child **`G1-siblingB`** whose native run is complete; ensemble comparison remains legitimately partial | `e1d683d0dd49d9b87d1766258888e749815054b612de6af2a493ca0fae6b72d9` | `cff5f498218f3e9bf13c8625748e00a0421512aae3c754e86acaadf45ba123ca` |

The original Linux E1/G1 rendered frames were also inspected visually in-chat; both show correct model and revision labels and a paused physical time state. Offscreen Windows capture is successful numerical/renderer evidence, **not** demonstrated mouse or pointer behavior on a user's Windows machine. Different PNG hashes across operating systems are not scientific quantity drift.

### First-attempt preservation and boundary

- First local new focused test run: **53 passed / one test failed** on an incorrectly authored expected screenshot-directory assertion; the directory was deliberately pre-created to test refusal. After correcting the **test assertion only**, original source unmodified, **54/54 passed** with warnings-as-errors.
- Two local full-suite attempts reached the sandbox execution timeout before finishing, with no observed test failure. These are **incomplete**, not full-suite passes. Hosted exact-head Linux and Windows logs provide full current-suite results.
- First version of the separate **author audit script** erroneously asserted viewer report `status=='passed'` rather than actual documented `status=='PASS'`. Original Linux audit already passed; the viewer assertion stopped that first combined local audit. The script-only parser was corrected to the actual original archive schema, and the final read-only recheck succeeded on Linux, Windows and viewer. The original artifacts, original source and CI logs were not edited.
- The local machine-readable author audit result is `emfeeld-pr25-author-qualification-audit.json`, SHA256 **`50a24afac7a98d940b75386957d5b7712a0dfdcc7787cdea09ba3d9f475db0da`**; it is a report of this chat's audit, **not** GitHub-required status or a separate Chat B test suite.

## Disposition

**Author-side qualification: PASS** on the exact tree, Linux/Windows/real PyVista CI and original ZIP evidence. All original PR #23 numerical fingerprints remain intact. The next mandatory gate is a **separate-context targeted independent R1 review** of exact head `4fe896ff6bb98d21a090bc16a84fe26145f9f5e7` and canonical tree `4df3703346ec7cba1ab74fcd6daa40796a535bf3`, requiring new reviewer-owned adversarial tests before any source merge. Preserve review first negatives and do not mistake author checks for independent sign-off.

**Unqualified:** independent human physicist certification, manual Windows desktop/mouse pointer operation, actual teaching usefulness, adversarial fully rewritten unkeyed evidence files, crash-safe distributed transaction semantics, general electromagnetic or responsive-conductor physics, and LLM-created physical source provenance. No user's local Conda or saved study changed.
