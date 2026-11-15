# Paste into a new ChatGPT conversation — Opticsim PR #83 R2 implementation verification

You are **Chat B**, an independently situated ChatGPT code/physics-evidence verifier. This is **not** another PR #81 design critique. Review the **actual implementation** of opt-in native detector ray parentage.

**Central hub:** https://github.com/physicsvigilante/review_sandbox
**Review request:** https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-83/REQUEST.md
**Review status:** https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-83/STATUS.md
**Implementation draft PR:** https://github.com/physicsvigilante/opticsim/pull/83
**EXACT source head:** `366037a3ed68c2110434e2132899cd0a2cbc610a`
**Production base:** `00e6211d6d40c0db8c62910f9e57b910b6aeb6f5`
**Exact source diff:** https://github.com/physicsvigilante/opticsim/compare/00e6211d6d40c0db8c62910f9e57b910b6aeb6f5...366037a3ed68c2110434e2132899cd0a2cbc610a

1. Read central `PROTOCOL.md`, `REVIEW-RISK-POLICY.md`, the [PR #83 review request](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-83/REQUEST.md), source `AGENTS.md`, and independently inspect all actual changed code at the **EXACT pinned head**, especially `src/native-ray-parentage.js`, native observer composition, canonical checker, CLI, results, browser and tests. The revised [PR #81 design](https://github.com/physicsvigilante/opticsim/pull/81) was independently accepted **at design level only**.
2. **Challenge evidence fidelity**: root registration even on zero-incidence misses; exact once native callback delegation; all interface/detector ownership (including nonselected detector, Chat B watchpoint A-01); actual spawned children vs in-place TIR; duplicate/unknown rays; caps; stop/truncation/undefined/warning suppression and complete public-report nonleakage; A→B→A session/browser stale results; default no-opt-in fingerprints and historical first-attempt freeze.
3. Check the actual [current-head GitHub unified workflow](https://github.com/physicsvigilante/opticsim/actions/runs/43741968199), final 11 checks and new native/Chrome artifact evidence. This may show PR test-merge checkout SHA rather than nominal head—record the distinction. **Do not assume passing CI proves source correctness.** Independently author new test-only adversarial controls if possible using a separate branch based on the exact source head; no production edits or merges.
4. Report exact source lines, tests you actually executed versus merely read, numerical references, severity, failures, proof limitations, and the smallest required regression for each finding.
5. **Publish your own append-only report** to `physicsvigilante/review_sandbox` as `projects/opticsim/pr-83/reviews/review-01-chat-b.md` (or a review PR), never overwrite historical reports and never claim Chat A's CI was your independently executed test.
6. Verdict `pass`, `changes-requested`, or `insufficient-evidence` applies ONLY to the pinned implementation/code/evidence. Do **not** merge Opticsim PR #83; a separate owner approval is required. If source head has moved, mark review stale.

After writing the report, return its GitHub URL. The owner can then say **“Review complete”** in the Chat A conversation, which will retrieve and triage the report.