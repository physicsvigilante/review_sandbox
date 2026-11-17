# PR #35 — author response 01 to independent R2 review-01 B1

**Status at this publication (2026-11-17): corrected source committed, focused/local and original source/viewer archives qualified; new Linux/Windows release CI still running; independent R2 re-review NOT performed.** This is an author response, not a reviewer verdict or release approval.

## Reviewer report and preserved first failure

The unchanged [independent review-01](../reviews/review-01-chat-b.md) **CHANGES REQUESTED** on `addb6ab3e76e4465649211305ae1a19e73537791` (tree `117fe65e64097d8dc3d4f6ff80ef57d7ae04d6cf`). The reviewer independently ran **57 novel adversarial cases: 56 PASS, one B1 FAIL**, plus the prior author 43-case suite. Actual native velocity sampled at **5e-13 s** incorrectly covered a frozen `t=0` request because the old wrapper compared physical times using `abs(actual-target) <= 1e-12`. A second old-head repro accepted `1.5000000000005` as a request for actual saved `1.5` s. Both old failed reviewer attempts, original old source and report remain unchanged. No previously failed attempt is retroactively treated as passing.

## Corrected exact source and bounded change

[Source PR #35](https://github.com/physicsvigilante/emfeeld/pull/35) corrected **head `72873b800db9b57051e1587aafd7ba5d938e1e41`**, Git **tree `a82188148568653311581d9d4c02e8c96a37d3cf`**. One new head commit descends from old failed/rejected head `addb6ab3...`; unchanged qualified main/base `1b0149d773f924e67e0cd1f950da8b5d0ffacaa2`. GitHub source-equivalent PR merge-preview `c2e26e7d164e499f32710ee07031a5919b803705` has exact corrected Git tree, with ordered parents [qualified main, corrected head].

Exactly **three files** changed in this B1 correction:
- `verification/question_first_trial_v1.py`: replace universal absolute `1e-12` seconds gate with `_same_saved_time`. Numeric times are finite/nonnegative; equal values are accepted; zero vs nonzero is rejected; nonzero representation differences can be accepted only if **at most one float64 ULP of each input** and **strictly less than one quarter of the authored scene's native sample interval**. This is a bounded representational allowance, not a physical-time comparison tolerance that can span saved samples.
- `tests/test_question_first_saved_time_v1.py`: 11 independently executed new cases (three named tests plus eight boundary parameterizations), including the **public CLI and actual native** 5e-13 s versus frozen zero with exit 1, `incomplete` assessment, retained original question/packet bytes and `execution_complete=true`; a nearby nonzero wrong time, legitimate same-sample decimal 0.3 rounding, subnormal spacing, NaN/Inf and zero.
- `docs/QUESTION_FIRST_TRIAL_V1.md`: document the bounded saved-instant identity rule and its limitations.

No `src/emfeeld` engine, physical laws, integrator, numerical solver tolerances, old author 43-case file, stored evidence, or viewer behavior changed. This correction must not be interpreted as a new capability to infer arbitrary prose meaning.

## Author local executed qualification

Author re-extracted the **actual original GitHub source-snapshot ZIP** and independently reconstructed its 362-file exact Git tree before executing tests. CPython 3.13.5 local container; `PYTHONPATH=src python -m pytest -q -W error tests/test_question_first_saved_time_v1.py tests/test_question_first_trial_v1.py` **54/54 PASSED** (11 new B1 and 43 original). `PYTHONPATH=src python -m pytest -q -W error pilots/authorability_v1/test_pilot.py -k 'not test_all_available_parent_files_remain_frozen'` **18 passed, one obsolete all-file freeze guard deselected**. Original Physics Demonstration V1 direct replay **17 native measurements / 64 analytical checks passed**; the developer-only original question-first freeze/assess CLI retained five named native measurements and reported complete native coverage (not independently verified question meaning). The reviewer’s original B1 case was not overwritten or altered.

## Exact original new-source archived evidence audited by author

- [Source snapshot workflow #44066177280](https://github.com/physicsvigilante/emfeeld/actions/runs/44066177280) **SUCCESS** on corrected source. Original ZIP artifact **14320032824**, original whole-ZIP SHA256 `9d4b7158ee2207460a7e6d39961726db459c21afd1837b721da2a9c8a39d2b1f` matched GitHub artifact digest; four unique CRC-clean ZIP members, safe paths. Original `tested-source.tar` SHA256 `a498c5a880b13e26013eaf7bd2de0f127ed6359efd1d7daea95bf36362880880` matches archived manifest; **362/362 file-blob identities verified against original git-tree.txt**, independently reconstructed exact Git tree `a821881...`. Original `identities.txt` names preview `c2e26e7...` and same exact tree.
- [Separate real-PyVista workflow #44066177344](https://github.com/physicsvigilante/emfeeld/actions/runs/44066177344) **SUCCESS**. Original viewer artifact **14321185879**, whole-ZIP SHA256 `6db662118ac9fdd2d3833e61b965cdc855c5c9d22b1789b3213b3d954ea97e74`, 22 CRC-clean unique ZIP members. Original 9/9 offscreen scene cases **PASS**, all 17 PNG SHA256 original receipts individually agree with original PNG bytes; embedded source TAR is byte-identical to source snapshot TAR; original full headless log records **1,580 passed**. `visual_inspection=PENDING`; neither physical/classroom usefulness nor manual Windows interaction is implied.

**Still pending at publication:** original corrected-head [Linux/Windows clean-install #44066177397](https://github.com/physicsvigilante/emfeeld/actions/runs/44066177397) was in progress; therefore no both-OS completion, fresh original OS ZIP source/native evidence audit, or independent R2 re-review pass is claimed in this file. Do not merge on this response. A true unseen teacher-authored question and externally judged physical interpretation remain separate future milestones.

## Fresh original Ubuntu release audit (completed after first report)

[Corrected-head Linux/Windows clean-install #44066177397](https://github.com/physicsvigilante/emfeeld/actions/runs/44066177397) **Ubuntu job 133980318679 SUCCESS**; Windows was still IN PROGRESS at this addendum. Downloaded original Ubuntu artifact **14320228516**, whole-ZIP SHA256 `62124d3fb08d52a66730a9d27a7c02708cb0be844a432cf9ea02775a1b12f068` matched GitHub digest. Original ZIP **2,176 unique, CRC-clean, casefold-safe paths**; exact `head-sha.txt=c2e26e7d164e499f32710ee07031a5919b803705` correctly identifies the source-equivalent PR merge-preview, not a post-merge main commit.

Actual Ubuntu original logs: **1,580 headless passed, 18 historical passed (one obsolete all-file guard deselected), 33 real-PyVista passed**. Archived original frozen question, receipt, packet, native-result, assessment and state all hash-bound to unchanged committed question SHA256 `36f56dcc11d6347a1db47adfb103b16472a8e1270641869f52c7220bd086a361` and packet SHA256 `6fe25bf6c738ee13fa837793414b343feeb53116737bcfafcf19c56c36adac5d`. Native report SHA256 `bf11cc7a6abd598bba0ae1746ca934eaf2ebc8c383aff79373676d5b4b06b947`: five named actual `ok` results (launch gravity, final position and velocity at t=2 s, initial/final total energy 12.0125 J). Assessment reports complete **measurement coverage only**, with interpretation and independent physics/teacher usefulness still explicitly unverified/not evaluated. E1 signed ensemble remains global **complete** (10/10 ok); G1 remains honest **partial**, with `body-4-absent` unavailable as typed `unknown_operand/null`, not a fabricated zero. No user Conda or old sealed store changed.

**Windows artifact audit and independent R2 review-02 remain pending in this addendum.**

---

## Required gate

Finish and verify the **original** corrected-head Linux/Windows workflow and release ZIPs (per-OS logs, original source/packet bytes, native trial output/coverage, independent hash/CRC), then request **separate-context targeted R2 review-02** of the corrected B1 gate and its retained evidence. Only the reviewer can publish their own PASS / CHANGES REQUESTED verdict. Any approved merge still requires fresh actual `main` push CI and original post-merge archive re-audit.