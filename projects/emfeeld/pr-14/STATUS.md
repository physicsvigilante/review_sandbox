# EM Fields PR #14 — final central review and release status

**MERGED and POST-MERGE QUALIFIED (2026-11-15 UTC).** Exact main/merge commit `8fe6331aefa252585b3b90f54b8ee7cbbac5e605`, Git tree `c274d94dd2185dcecdfca735e2951edae3e3d835`. The merge tree is identical to approved and independently reviewed source head `d46d04e23a142ea1c969b964ae5e1780110264c9`. [Source PR #14](https://github.com/physicsvigilante/emfeeld/pull/14) is closed/merged after explicit owner approval.

**[Final append-only merge and post-merge qualification report](MERGE-REPORT.md)** — complete source identities, Linux/Windows and PyVista CI links, ZIP artifact SHA-256, qualified E1/G1/T1 results, failed/refused evidence preservation, limitations and next merge gates.

## R2 review history — preserved

- Original [REQUEST.md](REQUEST.md) and [REVIEWER-PROMPT-01.md](REVIEWER-PROMPT-01.md) pin pre-merge head and risk class R2.
- Independently authored [Chat B review 01](reviews/review-01-chat-b.md) **scoped pass**, reviewed exact head `d46d04e23a142ea1c969b964ae5e1780110264c9`; Git blob `3b115f30ef1b17f350103eb21c67ba1c6a012d5b` **unchanged**. No demonstrated production blockers. Nonblocking notes: OS LF/CRLF raw-file hash differences versus identical canonical Git tree; local structural lock not tested as distributed/crash-recovery lock.
- [Chat A response 01](responses/response-01-chat-a.md) records disposition and user-approval gate, not a replacement reviewer opinion.
- Owner approval → guarded exact-head merge → fresh `main` CI → audited archives → final central record. Original reviewer harness failures and source evidence remain historically intact.

## Post-merge CI — green

- [Linux+Windows release](https://github.com/physicsvigilante/emfeeld/actions/runs/43746291562) **passed** per OS: **1,308 headless + 18 historical + 33 real-PyVista = 1,359 tests**. One unchanged obsolete historical file-freeze assertion explicitly deselected.
- [Separate real-PyVista workflow](https://github.com/physicsvigilante/emfeeld/actions/runs/43746291552) **passed**.
- Linux artifact ID `14174408661` SHA-256 `e8877dd69abe0cdf56d39b7fa447988b27f53ea103ecfe5e4b5c001ad833110d`; Windows ID `14175016636` SHA-256 `46bc735bb61cdbf49439a53dc8bf95bece292ce26e01a648145c650a27b7e92a`. Both verified directly: **1,451 ZIP entries, CRC clean, exact merge checkout pin**. E1/G1/T1 reference checks passed with one deliberate G1 old-body request rejection.

## Evidence boundaries

This R2 pass is independent **conversation context**, not independent human subject-matter adjudication. Model stores have local locking and unkeyed exact-byte integrity, not proven crash recovery or malicious-writer authentication. Test particles remain nonrelativistic and independent, with no backreaction or new field regime. No real classroom usefulness, manual Windows desktop interaction or unseen textbook interpretation is claimed.

**PR #14 release is complete.** Teaching evaluation remains paused, and the user's local Conda installation and preserved recordings were not changed. Any subsequent milestone must use its own source branch, risk/CI/review qualification and separate owner merge approval.
