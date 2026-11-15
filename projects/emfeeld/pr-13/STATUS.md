# EM Fields PR #13 — final centralized review and release status

**MERGED and POST-MERGE QUALIFIED (2026-11-15).** Exact main commit: **`7e6bd8c72cac7708ab3c2355cc1a98db09762133`**; tree **`ea4efcc21e101be8ceb11cbae5c14924e45d172b`**, identical to independently reviewed corrected source head **`e7c772af39c6271cd7a033ec2a006d617a51b442`**. [Source PR #13](https://github.com/physicsvigilante/emfeeld/pull/13) is closed/merged with explicit owner approval.

**[Final merge and qualification report](MERGE-REPORT.md)** — exact Git commits, original and post-merge CI runs, artifact IDs and SHA256 hashes, test counts, audited derived results, limitations and preservation statements.

## Review chronology (all original evidence preserved)

- [Review request 01](REQUEST.md) and [reviewer prompt 01](REVIEWER-PROMPT-01.md) pin original candidate `766633a...`.
- [Chat B review 01](reviews/review-01-chat-b.md) — **changes-requested**, original reviewer-authored Git blob `bc527fb081446faef8e37714d331c0bf7cc8455d`.
- [Chat A corrections](responses/response-01-chat-a.md), [targeted re-review request 02](FOLLOW-UP-02.md), [reviewer prompt 02](REVIEWER-PROMPT-02.md).
- [Chat B review 02](reviews/review-02-chat-b.md) — **scoped pass F-01 through F-04** for approved head `e7c772af39c6271cd7a033ec2a006d617a51b442`, reviewer blob `ca547f158a0216d41659dad356e4c6a0a16895e0`.
- [Chat A follow-up response](responses/response-02-chat-a.md) recorded the reviewed correction and explicit owner merge gate.
- Owner approval → exact-head merge `7e6bd8c72cac7708ab3c2355cc1a98db09762133` → **fresh Linux, Windows and real-PyVista success**, [release CI](https://github.com/physicsvigilante/emfeeld/actions/runs/43733310019) and [viewer CI](https://github.com/physicsvigilante/emfeeld/actions/runs/43733310048).

**Counts:** each OS passed 1,265 headless + 18 historical + 33 real-PyVista = **1,316 tests** by suite membership. The 46 focused derived cases were rerun within CI and are not extra distinct definitions. One obsolete unchanged whole-file freeze assertion was explicitly deselected. Original artifact checksums, run result integrity and failure/rejection semantics are documented in the [merge report](MERGE-REPORT.md).

**Limits:** Separate-chat LLM review is not independent human certification; no cryptographic input authenticity, desktop classroom outcome or unseen-source fidelity claim. Teaching evaluation remains paused. User's local Conda installation and prior saved runs were not changed by these GitHub actions. PR #13 release is complete; further development is a distinct milestone under the central risk policy.
