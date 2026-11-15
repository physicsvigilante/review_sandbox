# EM Fields PR #13 — centralized review and release status

**Production integration: MERGED with explicit owner approval. Post-merge `main` qualification is PENDING.** Do not interpret pending CI as passed.

- [Source PR #13](https://github.com/physicsvigilante/emfeeld/pull/13) merged on **2026-11-15**, exact approved head `e7c772af39c6271cd7a033ec2a006d617a51b442`, from base `c67d1115ad6fc982f29fe113583430e676938902`.
- Merge commit and new `main`: **`7e6bd8c72cac7708ab3c2355cc1a98db09762133`**; source tree `ea4efcc21e101be8ceb11cbae5c14924e45d172b`, exactly identical to the approved/reviewed head. No additional production-file changes entered in the merge.
- Historical [Chat B review 01](reviews/review-01-chat-b.md): `changes-requested` at original head `766633a60679208f534c5d299578b100d2d29eea`, blob `bc527fb081446faef8e37714d331c0bf7cc8455d`. **Retained unchanged.**
- Independent-context [Chat B review 02](reviews/review-02-chat-b.md): **scoped pass** of F-01–F-04 at corrected head `e7c772af39c6271cd7a033ec2a006d617a51b442`, blob `ca547f158a0216d41659dad356e4c6a0a16895e0`. **Retained unchanged.**
- [Developer response 01](responses/response-01-chat-a.md) and [response 02](responses/response-02-chat-a.md) preserve the independently identified bugs, corrections, and regression evidence.

## Pre-merge qualified evidence

- [Linux+Windows release CI](https://github.com/physicsvigilante/emfeeld/actions/runs/43729059256): passed per OS **1,265 headless + 18 historical + 33 real-PyVista** tests.
- [Separate real-PyVista CI](https://github.com/physicsvigilante/emfeeld/actions/runs/43729059279) passed.
- Linux artifact `14167811270`, SHA256 `b1f32f099f2f5b9494327d7df41cd2fd8014973e0adc4f65c2fffec5a639ed57`; Windows artifact `14167972595`, SHA256 `131af51d9599b02a07fa58f122198314cb4fbca74f39b9173062d2f8448285a9`.

## Post-merge runs (PENDING at this record revision)

- [Main-branch clean-install Linux+Windows qualification](https://github.com/physicsvigilante/emfeeld/actions/runs/43733310019) — queued/running; **no pass claimed yet**.
- [Main-branch real-PyVista qualification](https://github.com/physicsvigilante/emfeeld/actions/runs/43733310048) — queued/running; **no pass claimed yet**.

A separate append-only merge/qualification record will be created after both post-merge jobs complete and their artifacts are audited. Original reviewer reports, negative experiments, failed attempts, and source PR history are preserved. Separate-chat GPT assessment is not independent human physics certification or proof of classroom outcomes. Exact-byte inventories are not cryptographic authentication of malicious writers. The user's local installation and historical saved simulations were not changed by the GitHub merge.
