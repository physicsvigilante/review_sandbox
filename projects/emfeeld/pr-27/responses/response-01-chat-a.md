# EM Fields PR #27 — Chat A response 01 to independent R1 review-01 blocker B1

**Disposition (2026-11-16 Asia/Kolkata): B1 REPRODUCED AND NARROWLY CORRECTED; NEW EXACT SOURCE HEAD LOCAL-QUALIFIED; FRESH EXACT-HEAD CI IN PROGRESS; INDEPENDENT TARGETED RE-REVIEW NOT YET PERFORMED. PR #27 REMAINS DRAFT AND UNMERGED.** This is the implementer's response, not a Chat B report or source merge permission.

## Historical independent finding, preserved unchanged

- [Independent review-01](../reviews/review-01-chat-b.md) is historically **CHANGES REQUESTED** on former source **`2dc5e1d90a1cec2809d536f725474eac0ae4dd2d`**, exact old Git tree **`45df8622888b841333d7242caf410e7449900cfc`**.
- Reviewer tested 42 novel cases (**40 passed, two failing B1 time windows**). After original full `inspect_ensemble` accepted a comparison integrity receipt and a later nested comparison inspect had run, append-only trailing whitespace to **the selected original `member-XX/comparison/integrity.json`** changed its raw SHA256 without changing parsed data, request/result bytes, or physical values. Original readout could output the *drifted* integrity hash as if it were original parent-sealed evidence. Neither input values nor numerical physics were shown to be incorrect; this is an evidence-provenance fail-closed gap.
- The reviewer did not edit source or old saved records. Preserve the entire [original review-01](../reviews/review-01-chat-b.md), original red report and original CI archives unchanged.

## Author first red attempts and independent reproduction

- Before any source correction, on the pinned prior source snapshot, added **two reviewer-derived timing-window regression executions** to a disposable source copy. First local run: **2 failed**, one genuine "DID NOT RAISE" plus a **test-harness NameError (`Path` not imported)** in the second case. Preserved raw stdout-log SHA256 **`6d522c3da88b3666e8ea0acd82edd3d55a6022207e9421741d59c18ebbc3992f`**. This first reviewer-derived *author-run* harness error is not reclassified as a source defect.
- Corrected **only** the new test harness (`folder == target.parent`, both Paths). On **unchanged old source**, the two cases both returned successfully when refusal was required: **2 failed / 79 deselected**, original second red log SHA256 **`738baf0a690b1811045103146230a4a8c67827065f78324ed9cc061b5d62fe56`**. This separately reproduces each independently identified B1 window.
- The tests intentionally mutate **only a disposable copied comparison integrity file** after the entire sealed source has been validated, leaving original archives, root model store, source template and other ensemble files byte-identical. They explicitly assert nonpublication of a drifted source receipt. No actual user's saved study was changed.

## Minimal source correction — exact new code identity

- New source commit **`e4437e288e057d8551862980f1351044c621838b`**, canonical Git tree **`c3bf1a28f0b97f80b722d40f9616711e1587a1f1`**, unchanged qualified base/main **`9e5924efa60dea56606e0b8eef591f94711b666d`**. PR CI merge preview is a GitHub transient artifact, **not** the final source/production merge. Commit is applied only to draft [PR #27](https://github.com/physicsvigilante/emfeeld/pull/27), never to main.
- GitHub original-to-new comparison: **one commit, two changed files only**, `src/emfeeld/scenario_ensembles.py` **+17/-0**, `tests/test_scenario_ensembles.py` **+74/-0**. Exact new source blob SHA **`5c266f78da394028d707d95e129d4024906bcdc3`**; new test blob SHA **`20825b3fb1147e90eb4c82c75d062a23a7ad5f50`**. Both created GitHub blob SHA IDs matched the exact files tested locally, and the new Git tree matched the independently built local disposable Git tree.
- Corrected `read_ensemble_measurements` now retains the **raw original outer `ensemble/integrity.json`** bytes before invoking the unchanged `inspect_ensemble`, which validates all files and all siblings. Immediately after that preflight it confirms the outer inventory has not changed. When projecting each saved comparison, it checks the **raw SHA256 of the selected `member-XX/comparison/integrity.json`** against the **matching exact path hash in that preflight-validated outer manifest**. Existing inner `request.json`/`result.json` raw-hash and parsed authoritative comparison inspector checks remain unchanged. Before returning, it rechecks the original outer seal bytes. Any drift rejects with original `RevisionError` integrity codes, rather than exporting a different integrity receipt.
- No field law, integration, signed comparison arithmetic, SI unit, error tolerance, source IDs, physical model store, original native inspector, PyVista renderer, immutability or historical record is altered. Remaining concurrent hostile-writer/TOCTOU/ACID and malicious re-sealing limitations are explicitly unchanged.

## Author locally executed corrected regressions

- Reviewer-derived two B1 cases: **2 passed** after source fix, first green log SHA256 **`0891244bd1bace80028950a0707ee781a24d2ebfb43f7cc8ac92d4080f00ef93`**.
- Added a third negative regression: the **outer ensemble inventory itself** changes after original preflight; hard `ensemble_integrity` refusal, no extra protected-file writes.
- All focused ensemble tests: **82 passed**, warnings-as-errors, log SHA256 **`dddb2e29224e370339de919e6555502b4ba0e0e23afd371e51bd53dd82bda9d0`** (79 previous +3 new).
- All local headless tests: **1,484 passed**, `-W error`, log SHA256 **`afe9b1ee60a880b67ff2849064957d27928c11bb0b63af461e8a59c8e200f5af`**. Original older local full suite at old head had timed out without a verdict; **this is a freshly completed full run on the new exact locally tested source**.
- Current historical behavioral replay: **18 passed, one unchanged obsolete whole-file-freeze check deselected**, `-W error`, log SHA256 **`7320a25c755a7ab07f64d0ff43b5d78845c8f3ef0864973eb6778d7e9006a593`**.
- Python 3.13.5 / NumPy 2.3.5 / SciPy 1.17.0 / pytest 9.0.2, Linux disposable container; local PyVista unavailable, so no locally run real rendering is inferred.
- These are **author-run**, reviewer-derived cases and test definitions. They are NOT a new independently authored Chat B verdict.

## Fresh exact-head CI and next gates

GitHub automatically started new source [Linux/Windows clean-install workflow #43923137346](https://github.com/physicsvigilante/emfeeld/actions/runs/43923137346), [separate real-PyVista #43923137263](https://github.com/physicsvigilante/emfeeld/actions/runs/43923137263), and [exact source snapshot #43923137279](https://github.com/physicsvigilante/emfeeld/actions/runs/43923137279) for the corrected draft source. **All were IN PROGRESS when this response was first authored.** Final results must be checked from their actual original jobs and original ZIPs, not inferred from earlier reviewed-head green CI.

After exact-head Linux/Windows/PyVista and original release archives are qualified, Chat A should publish a NEW narrow request, e.g. `FOLLOW-UP-02.md` and `REVIEWER-PROMPT-02.md`, asking Chat B to independently execute **both** B1 comparison-integrity timing windows and positive original-source signed/unit/unavailable controls, plus representative original-request/result and CLI regressions. Chat B must author a **new** `reviews/review-02-chat-b.md` without overwriting review-01. The PR stays **draft/unmerged** pending that independent scoped R1 verdict and separate owner/source integration gates.

No user's local Conda environment, saved physical study, original archived release ZIP, original reviewer report or production main branch has been changed.
