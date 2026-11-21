# PR #81 independent review · changes requested

**F-01 (major)**. A caller that passes a Windows short study path together with its long case root receives `path: study outside case root` for a valid nested revision. The two paths identify the same files that pass with other spellings. This blocks sign-off on equivalent-root handling. The defect concerns admission of a valid study. The tested outside-root controls continued to refuse.

Reviewed [source head 538fbb097f81d3c66b458fa7cf99bd35a9ed7aac](https://github.com/physicsvigilante/sim_heat/commit/538fbb097f81d3c66b458fa7cf99bd35a9ed7aac) against base `6904ec8219be0ddb8ec1635a9d000ddda80307c9`, tree `664d64151d09c9cd5cb092ece44dd71876974559`. The R2 scope covers Windows offline path admission and preservation of N1 source evidence. I reviewed the five-file delta, source instructions, domain contracts, historical record, pinned CI logs and [request at hub 785cf2c](https://github.com/physicsvigilante/review_sandbox/blob/785cf2cb6fe123eef2facff1da02809af4b79d83/projects/sim_heat/pr-81/REQUEST.md). This is a separate Codex reviewer context. It provides no independent human assessment.

## F-01 reproduction

Run from the candidate checkout on a Windows volume with a distinct 8.3 spelling for the checkout or an ancestor. This probe reads the checked-in D2 conductivity revision and its parent.

```python
from ctypes import create_unicode_buffer, windll
from pathlib import Path
from h1.model import Refusal
from h1.study import load_study

long = (Path.cwd() / "h1/cases").resolve()
buf = create_unicode_buffer(32768)
assert 0 < windll.kernel32.GetShortPathNameW(str(long), buf, len(buf)) < len(buf)
short = Path(buf.value)
q = Path("D2_K2/study.json")
assert short != long and short.samefile(long) and (short/q).samefile(long/q)
for path, root in [(long/q, long), (short/q, short), (long/q, short), (short/q, long)]:
    try:
        print(load_study(path, root).sha256)
    except Refusal as exc:
        print(str(exc))
```

The local `Documents` directory had the short spelling `DOCUME~1`. The first three calls returned `ab3741a80e94b32a8f6d050f34baf9c773763fdd3ed6df71ccdcdbe2214a0d87`. The fourth refused. My first temporary directory had no distinct short spelling and all four calls there passed, so that first probe provided no 8.3 coverage. An independent temporary fixture with an ordinary sibling directory also reproduced the asymmetry. Given `alias = p/"sibling"/".."/"cases"` and `canonical = p/"cases"`, `load_study(alias/q, canonical)` refused and the reversed root/path spelling passed. A Windows extended-length path paired with an ordinary root also refused in either order.

The loader selects a base using lexical ancestry before calling the filesystem containment check. With a long root, both bases are the long spelling, so the short study path fails `relative_to` immediately. The checked-in alias case passes the same spelling for both arguments on entry. Accept equivalent caller spellings while preserving inspection of the original path components and resolved containment. Add a public-entry regression that verifies a distinct alias and exercises both mixed directions. Targeted re-review of that correction is sufficient. [Loader under review](https://github.com/physicsvigilante/sim_heat/blob/538fbb097f81d3c66b458fa7cf99bd35a9ed7aac/h1/study.py#L122-L136)

## Independent checks and evidence limits

- I checked the head and tree with Git and ran `python -s -B -m unittest -v h1.tests.test_study_paths qualification.h1_windows_study.test_source_admission` on Windows CPython 3.13.5 with NumPy 2.3.5, SciPy 1.17.0 and mpmath 1.3.0. All four tests passed. On disposable copies of D2 and D2_K2, authored backslashes in each path field refused, changes to either parent hash refused as stale, and an outside study, outside model and outside parent all refused. The admitted child retained its model identity `8d57b06b2e46d7ccca44da784acc433f3297b94871e65ad590881d4fc75531e3`.
- Windows denied symbolic-link creation with error 1314. The symbolic-link refusal remains unverified here. An in-root directory junction to D2_K2 admitted the identical study. Junctions and symbolic links are distinct Windows reparse points. This observation establishes neither escape from containment nor coverage of every reparse-point type.
- I hashed the raw N1 manifest and compared each entry to the bytes from `git show <revision>:<path>` on both revisions. The manifest SHA-256 was `28e249bbda68fba3a511caede4dfdec8cd5254e3a02b5eda5025bba82dbb6766`. All 18 read-only entries and three original inputs matched the base. On the head the only difference was the loader, SHA-256 `e32b28258ce93c9a055dab5f5b1982f1ad2b56841ef626d3745d5a1d08f75c45`. The historical checker refused exactly `source drift: h1/study.py`. Original T admitted and bound to the reference facts, exposing 77 internal exports and eight public requests marked `not_computed`. Increasing T_Collar mass by 0.01 in an in-memory reference copy produced `reference_binding: reference fact differs: T_Collar.m`.
- I read both Windows job logs. The first checked out `99389140a2993bc8c0db6e4f99b24a5a839959de` and recorded one error in four tests on RUNNER~1 versus runneradmin. The successor explicitly checked out the reviewed head and passed all four in 0.626 s. Its workflow runs the two named modules. The 334/338 Windows full-suite result belongs to loader revision `7a31937e7676bb1927def52234f0e4232e7e36b9`. I did not run the full suite at the successor. [First job](https://github.com/physicsvigilante/sim_heat/actions/runs/44845390162/job/136663700127) · [Successor job](https://github.com/physicsvigilante/sim_heat/actions/runs/44846214173/job/136666440136)
- The source-identity and offline admission claims above are supported within this scope. The seven historical reference failures and eight native-readiness blockers remain open. This review performed no OpenModelica operation, numerical acceptance assessment, source-fidelity assessment against the original physical problem, or classroom evaluation. Both source PRs remain outside this review's merge authority.
