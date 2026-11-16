# Paste into separate Chat B — Opticsim PR #89 full R2 Stage-1 code/evidence review

You are **Chat B**, in a separate ChatGPT conversation, performing an independently situated **R2 review of ACTUAL CODE, pinned native simulations and truthful evidence** — NOT another design review. This is an **opt-in NONCERTIFYING advisory only**, not a mandatory optical-measurement gate.

**Central review hub:** https://github.com/physicsvigilante/review_sandbox
**Review request:** https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-89/REQUEST.md
**Current status:** https://github.com/physicsvigilante/review_sandbox/blob/main/projects/opticsim/pr-89/STATUS.md
**Draft implementation PR:** https://github.com/physicsvigilante/opticsim/pull/89
**EXACT SOURCE HEAD:** `3f2d31aa19a851d92a8d1c46ede2249c52e0e223`
**Base/main SHA:** `fa158fc78da7a35b6a02eaed58c0cdbd4b699220`
**Exact diff:** https://github.com/physicsvigilante/opticsim/compare/fa158fc78da7a35b6a02eaed58c0cdbd4b699220...3f2d31aa19a851d92a8d1c46ede2249c52e0e223
**Actual fixed-head CI:** https://github.com/physicsvigilante/opticsim/actions/runs/43827935628
**Native artifact:** https://github.com/physicsvigilante/opticsim/actions/runs/43827935628/artifacts/14207103860
**Real-Chrome artifact:** https://github.com/physicsvigilante/opticsim/actions/runs/43827935628/artifacts/14207282515

Read central `PROTOCOL.md`, `REVIEW-RISK-POLICY.md`, `REVIEW-TEMPLATE.md`, pinned source `AGENTS.md`, [the exact Stage-1 feature contract](https://github.com/physicsvigilante/opticsim/blob/3f2d31aa19a851d92a8d1c46ede2249c52e0e223/docs/NATIVE-FINITE-HIT-DIAGNOSTIC.md), and both prior **PR #88 design-only Chat B reviews** (initial CHANGES-REQUESTED; second PASS at revised SHA). Design approval did NOT certify this implementation.

**Independently inspect the actual 17-file source diff at the SHA.** Focus on `src/finite-hit-exact.js`, `src/native-finite-hit-diagnostic.js`, sole existing native observer in `src/planar-media.js`, `src/adapter.js`, `check-scene.mjs`, CLI `scripts/author-scene.mjs`, results, snapshots, public workflow, `src/app.js`, `src/qualified-ui.js` and result/evidence viewer. Challenge native callback return identity, same-run start/incident coverage, exact binary64 t/u/cutoff and reported-point checks, true zero-hit and 128/129 cap, warning/stopped/truncated handling, no-opt-in parity, source/interfacing signed power, and stale A→B→A. The point-error bound is intentionally *not invented*: non-exact native vs reference point must become `unknown` unless separately conclusive inconsistency. Report if even this conservatism produces false confidence.

**Challenge advisory-only truth:** `status:'advisory'` must never be counted as an answered optics quantity or implicitly replace canonical existing native values. When a completed critical native run has invalid represented geometry, the UI must prominently say **not independently certified**, while the unchanged preexisting physical measurements remain visible under their historical qualifications. No Stage-2 mandatory withholding, new native ray tracer, inferred path or critical branch is authorized. Confirm no diagnostic results/ray endpoints in exports and no raw geometry leak into public JSON.

**Check actual source-specific CI & artifacts:** 11/11 workflow green, 763/763 Node tests, eight synthetic public native cases, ten real Chrome checks and screenshots, and independently rehash the zipped artifacts if tools allow (GitHub SHA-256 digests are in REQUEST.md). **Preserve first FAILED development tests 43825711560 and 43826462305**; the exact-source green run was a later corrected attempt. GitHub PR CI can check out a synthetic test-merge SHA: distinguish it from the exact actual production head.

**Independently author novel test-only adversarial probes if possible**, in a NEW review-only branch based on the pinned PR #89 head without changing production source. Explore native exact-critical variability, callback registration bypass, a fake native point, valid tiny forward > cutoff, real Fresnel weak branches, missing source on zero-hit and BigInt/browser costs. If execution is unavailable, state evidence limitations precisely; green Chat A tests are not an independent native experiment. A new test should not prescribe a ray route or textbook result.

Write **YOUR OWN** append-only Chat B report under `physicsvigilante/review_sandbox` at `projects/opticsim/pr-89/reviews/review-01-chat-b.md` (or review PR), giving **pass / changes-requested / insufficient-evidence** for **R2 IMPLEMENTATION**, pinned SHA, independent execution vs inspection, findings and the smallest new regression or code correction. Never overwrite older review history.

**DO NOT MERGE** source PR #89, research PRs #87/#88, reviewer-only branches, or silently turn on Stage 2. This independent review is separate from the owner's later merge approval. Return the new review GitHub URL; the owner can then say **“Review complete”** to Chat A.
