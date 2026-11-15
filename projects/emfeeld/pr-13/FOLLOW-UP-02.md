# EM Fields PR #13 — R2 targeted follow-up review 02

Original independent [review-01-chat-b.md](reviews/review-01-chat-b.md) is **changes-requested** at `766633a60679208f534c5d299578b100d2d29eea` and remains unchanged. Review only the **four corrected numerical/evidence paths F-01–F-04**, not the unchanged physics engine or repeated broad E1/G1/T1 appraisal.

- Source PR: https://github.com/physicsvigilante/emfeeld/pull/13 — **draft, unmerged**.
- Base `c67d1115ad6fc982f29fe113583430e676938902`; **corrected head `e7c772af39c6271cd7a033ec2a006d617a51b442`**; tree **`ea4efcc21e101be8ceb11cbae5c14924e45d172b`**.
- Exact CI checkout `7474ba9b6d0880b6c871987134b82d6b8122b322` has identical tree.
- Diff: https://github.com/physicsvigilante/emfeeld/compare/766633a60679208f534c5d299578b100d2d29eea...e7c772af39c6271cd7a033ec2a006d617a51b442
- [Developer correction response](responses/response-01-chat-a.md) records repro, tests and qualified evidence. It is **not** an independent verdict.
- [Linux+Windows release CI](https://github.com/physicsvigilante/emfeeld/actions/runs/43729059256) **passed**: per OS **1,265 headless**, **18 historical** (1 unchanged obsolete all-file-frozen assertion deselected), **33 real-PyVista** tests. [Separate real PyVista](https://github.com/physicsvigilante/emfeeld/actions/runs/43729059279) passed. Source snapshot is provenance only.
- Linux artifact **14167811270**: SHA256 `b1f32f099f2f5b9494327d7df41cd2fd8014973e0adc4f65c2fffec5a639ed57`. Windows artifact **14167972595**: SHA256 `131af51d9599b02a07fa58f122198314cb4fbca74f39b9173062d2f8448285a9`. Both ZIP/CRC verified and include recorded fresh physics examples and negative tests.

## Specific independent questions

1. **F-01:** Repeat nonzero ratio underflow including negative sign and valid field magnitude/vector, legitimate zero numerator, representable subnormal and valid finite denominator/overflow paths. Is a successful fabricated zero still possible?
2. **F-02:** From the *corrected head* CI artifact, copy original G1 partial derived result, change its top-level status to complete, regenerate only its own unkeyed inventory, invoke `inspect` and CLI. Verify refusal, and separately inspect intact G1 partial. Distinguish internal semantic consistency from malicious-writer authentication.
3. **F-03:** Check negative speed/kinetic energy and inconsistent vector norms are refused without invalidating valid native E1/G1/T1 ratios or signed potential differences. The G1 re-sealed native input is explicitly a **disposable copy**, not an error in the original solver.
4. **F-04:** Check `time_s=10**500`, NaN/Inf/bool/missing metadata, invalid sample index and actual mismatched time; require local unavailable result instead of a raised traceback.

If available, independently execute **new or repeated targeted controls** and identify exact sources/CI/tool setup. Reading Chat A's passing CI is **not** independently rerunning tests. If a regression remains, describe inputs/expected/actual and keep PR unmerged. Escalate scope only if new physics/evidence changes beyond these four paths.

Write a **NEW Chat B-authored** report `projects/emfeeld/pr-13/reviews/review-02-chat-b.md` directly in the central repository (or review-only central PR), following [REVIEW-TEMPLATE.md](https://github.com/physicsvigilante/review_sandbox/blob/main/REVIEW-TEMPLATE.md). Do **not** overwrite review-01, alter source code or merge the PR. Return scoped **pass / changes-requested / insufficient-evidence**.
