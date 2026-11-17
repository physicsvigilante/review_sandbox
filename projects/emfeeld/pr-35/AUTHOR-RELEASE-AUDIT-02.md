# PR #35 — corrected B1 exact-source final author release-audit 02

**2026-11-17, author-side result: PASS for corrected-source pre-merge CI and all four original evidence ZIP audits.** This is **not** independent R2 re-review, user approval of merge, post-merge release, independently authenticated teacher provenance, or external physical/educational certification. **PR #35 remains DRAFT / UNMERGED** until a new separate-context reviewer verdict on corrected source.

## Immutable source and CI provenance

- PR: https://github.com/physicsvigilante/emfeeld/pull/35
- Corrected HEAD **`72873b800db9b57051e1587aafd7ba5d938e1e41`** (one direct descendant of original reviewed/rejected `addb6ab3e76e4465649211305ae1a19e73537791`). Canonical exact source tree **`a82188148568653311581d9d4c02e8c96a37d3cf`**.
- Prior qualified main/base **`1b0149d773f924e67e0cd1f950da8b5d0ffacaa2`**. Exact CI merge-preview **`c2e26e7d164e499f32710ee07031a5919b803705`** has the **same tree** with ordered parents [base, corrected HEAD]. No actual `main` merge has occurred.
- Corrected-source original [Linux/Windows clean-install release #44066177397](https://github.com/physicsvigilante/emfeeld/actions/runs/44066177397) completed **SUCCESS** attempt 1, **both** Ubuntu 24.04 job `133980318679` and Windows 2022 job `133980318137` completed **SUCCESS**, each **1,580 headless + 18 historical behavioral (one obsolete all-file freeze guard deselected) + 33 real-PyVista passed**. The existing 43 question-first tests and new 11 B1 focused cases are included within the 1,580; never double-count.
- Separate original [real-PyVista #44066177344](https://github.com/physicsvigilante/emfeeld/actions/runs/44066177344) **SUCCESS**; original [source snapshot #44066177280](https://github.com/physicsvigilante/emfeeld/actions/runs/44066177280) **SUCCESS**.

## Original GitHub artifact ZIPs, downloaded and verified by author

| Artifact | ID | Original ZIP SHA256 | Independently read ZIP content |
|---|---:|---|---|
| Ubuntu release | `14320228516` | `62124d3fb08d52a66730a9d27a7c02708cb0be844a432cf9ea02775a1b12f068` | 2,176 unique CRC-clean, casefold-unique path-safe entries |
| Windows release | `14320798872` | `5eb877861e40d576a6b4b9b958a12ef6ac4d2a9d1de7a534f55d23ef544704ed` | 2,176 unique CRC-clean, casefold-unique path-safe entries |
| Separate real-PyVista | `14321185879` | `6db662118ac9fdd2d3833e61b965cdc855c5c9d22b1789b3213b3d954ea97e74` | 22 CRC-clean entries, 9 offscreen scenes PASS, 17 individually checked original PNG/hash receipts |
| Source snapshot | `14320032824` | `9d4b7158ee2207460a7e6d39961726db459c21afd1837b721da2a9c8a39d2b1f` | 4 CRC-clean entries, source `tested-source.tar` SHA256 `a498c5a880b13e26013eaf7bd2de0f127ed6359efd1d7daea95bf36362880880` |

Original ZIP SHA256 values were recomputed over the actual downloaded original bytes and compared to GitHub's original artifact digests. All included ZIP members were CRC-tested, with unsafe paths and duplicate/casefold-duplicate filenames rejected. Author safely extracted original `tested-source.tar`, rebuilt the full **362-tracked-file exact Git tree** and obtained `a821881...` by `git add -A; git write-tree`. The viewer source tar was byte-identical to the snapshot source tar; 17 original viewer PNG receipts matched actual PNG bytes. Original `head-sha.txt` in each OS ZIP records the CI **merge-preview** `c2e26e7...`, **not** a false claim of post-merge production commit. Original source SHA and viewer/ZIP archives were unchanged during this audit.

## Actual archived native evidence and preservation

Author parsed and checked the **original files inside both different OS ZIPs**, rather than trusting CI green alone:

- Source bytes: `question-first-v1/lock/question.json` = `attempt/question.json` = committed original developer fixture, SHA256 **`36f56dcc11d6347a1db47adfb103b16472a8e1270641869f52c7220bd086a361`**. `attempt/packet.json` = committed original packet bytes, SHA256 **`6fe25bf6c738ee13fa837793414b343feeb53116737bcfafcf19c56c36adac5d`**. Original receipt duplicated byte-for-byte, requested IDs ordered exactly and source origin `developer_authored`, authenticity `not_authenticated`.
- Actual native result: `field_launch=(0,-2,0) m/s²`; final `position=(1.8,0.4,0.2) m` and `velocity=(0.4,-2.8,0.1) m/s` at **saved physical t=2 s and sample index 20**; initial/final `total_energy=12.0125 J` at sample 0/20. All five distinct native statuses `ok`, aggregate `status=ok`, correct units and preserved native request IDs. Author checked numerical values against independently written closed-form uniform-gravity equations at bounded tolerance (same-author check, not independent scientific certification).
- Original Ubuntu native report SHA256 **`bf11cc7a6abd598bba0ae1746ca934eaf2ebc8c383aff79373676d5b4b06b947`**, original Windows native report SHA256 **`6638d653fdc757a8420d3c04f60c7a5a400ce3176ad88f3d3434afef8fb79145`**. Both per-OS original `assessment.json` cite the **correct corresponding SHA**, original question and packet. **The OS-native bytes differ, which is expected and not mislabeled identical.**
- Original assessment and `state.json`: `execution_complete=true`, `native_measurement_coverage=complete`, `issues=[]` for **these five illustrative requests only**. Explicitly separate `interpretation_fidelity=not_verified`, `independent_physics_correctness=not_evaluated`, `educational_usefulness=not_evaluated`, `textbook_answer_completeness=not_evaluated`. The question is intentionally **developer-authored**, not an independently supplied unseen teacher task.
- Original prior `physics-demo-v1` retained **17 real native observations and 64/64 analytic-reference checks passed** on each OS. Both original summaries' **29 individual `src/emfeeld/*.py` engine SHA256 receipts** independently checked against the extracted original source bytes (allowing ordinary Windows checkout CRLF conversion).
- E1 original sealed ensemble evidence: global `complete`, **10/10 signed comparison measurements ok**. G1 original sealed ensemble: global `partial`, **7 ok + 1 `body-4-absent` typed `unavailable/unknown_operand/null`**, never zero. Old saved source/revisions/stores and user's local Conda were not modified.

## Local author adversarial and historical tests

On safely extracted actual corrected original source ZIP (Python 3.13.5; NumPy 2.3.5, SciPy 1.17.0, pytest 9.0.2; with warnings as errors):

- `PYTHONPATH=src python -m pytest -q -W error tests/test_question_first_saved_time_v1.py tests/test_question_first_trial_v1.py` → **54 passed** (11 new B1 cases + 43 original source-first cases).
- `PYTHONPATH=src python -m pytest -q -W error pilots/authorability_v1/test_pilot.py -k 'not test_all_available_parent_files_remain_frozen'` → **18 passed, one historical all-file freeze guard deselected**.
- `PYTHONPATH=src python -m compileall -q verification/question_first_trial_v1.py tests/test_question_first_saved_time_v1.py` → successful syntax compilation.
- GitHub clean-install original full suites, not this local focused test run, establish the **full** 1,580 per OS. The first old local full-suite attempt on prior candidate timed out; no retroactive local full pass is claimed.

## Independent review and release gate: NOT satisfied

The prior [Chat B review-01](reviews/review-01-chat-b.md) is preserved as **CHANGES REQUESTED** against old head, including its first failed B1 test. The corrected B1 change is only wrapper/docs/new small regressions; no solver or field law alteration. [Author response-01](responses/response-01-chat-a.md) and [reviewer prompt-02](REVIEWER-PROMPT-02.md) are author-generated, **not reviewer verdicts**. Request separate-context reviewer-owned *fresh execution* and original archive audit of corrected `72873b8...`, publish `reviews/review-02-chat-b.md` with scoped R2 PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE. **Do not merge until independent R2 PASS and owner/source gates.** After any authorized merge, separately run real `main`-push Linux/Windows and viewer workflows and audit their **new** original artifacts; do not reuse this PR archive as a post-merge release.

Nonclaims: no teacher provenance or authenticated chronology, no complete natural-language interpretation, no general physical/numerical certification, no educational usefulness verdict, no manual Windows desktop mouse trial, no adversarial filesystem ACID guarantee.
