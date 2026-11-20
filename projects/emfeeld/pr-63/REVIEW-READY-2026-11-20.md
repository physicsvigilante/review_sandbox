# PR #63 — final independent-review readiness checkpoint (20 November 2026)

**Status: READY FOR A SEPARATE REVIEW, NOT REVIEWED, NOT MERGED.**

Candidate source HEAD: `b2e19bad89bc70fdae7602478c55cc4002f64bf2`, Git tree `84b8b33364cd8b700984d0c51a15b7df1539c7d2`.
Qualified base/main: `52aecd34338662e269fba091c0ff6664e8e1eca7`.
PR synthetic test-merge commit: `6ab145376b198a21375f5ed976ac1b98821eaedf`; verified its ordered parents [base, candidate] and exact same candidate tree; **not production main**. Only nine new feature paths.

The full **ten exact-head premerge workflows all completed SUCCESS**, including circular-loop native 3D, general PyVista, Gauss, cavity, dipole, capacitor, wire, browser, source snapshot, and clean-install Linux+Windows. Full OS workflow [44678141157](https://github.com/physicsvigilante/emfeeld/actions/runs/44678141157) has both Ubuntu and Windows jobs SUCCESS. This updates earlier interim status without rewriting those historically accurate observations.

## Independent additional Windows source-bound archive audit

Original GitHub Actions Windows artifact **14604631415**, downloaded as a separate, unmodified ZIP from the full clean-install workflow. Whole ZIP SHA256:

```text
fd936d2b7f358b16d585f048fa9c4804bc5815775e87cd1d98490a9cc504c1e0
```

An independent ZIP pass over the genuine downloaded bytes found **2,186 unique entries**, zero duplicate members, **zero bad ZIP CRCs**, **173 JSON integrity manifests** with **1,750 explicitly listed file-hash references**, **1,749 matching SHA256**, **zero missing referenced files** and **one deliberate negative-test mismatch**:

```text
derived-001/G1/review-challenge-resealed-native/native/result.json
```

This is the previously documented intentionally corrupted comparison-negative artifact, not an unexpected data-integrity regression. The original archived `head-sha.txt` identifies the GitHub synthetic test merge `6ab145376b198a21375f5ed976ac1b98821eaedf`, whose Git tree and parent identities were separately checked via the Git object endpoint as matching the exact HEAD candidate. Archived `headless-tests.log` records **2,195 passed**; `viewer-tests.log` records **106 real-PyVista passed** (Python 3.13.5). The CI Windows job SUCCESS was separately checked through job steps and its full original job log.

Original Linux artifact **14604210671** was already audited in [AUTHOR-QUALIFICATION-01](AUTHOR-QUALIFICATION-01.md), with **2,195 headless + 106 PyVista PASS** and the same expected corruption negative-test result. The dedicated lesson artifact **14603906976** has **30 focused tests**, **9 genuine scene PNGs**, checked screenshot slider visibility, and **63/63 authentic file-hash references** in the prior independent-of-test-code *author-side* source audit. Native result/screenshot inspection remains subject to external reviewer challenge.

## Separate reviewer handoff

Use [REVIEWER-PROMPT-01](REVIEWER-PROMPT-01.md), now with full exact-source premerge gates verified. The reviewer should independently evaluate the physical equation, strict off-axis refusal and mixed-Boolean validation, immutable SI versus schematic scene data, rendered R×2 geometry, actual VTK sliders/key events and **new reviewer-owned native screenshot**, original artifact identity and interpretation of classroom scope. Produce a separate `reviews/review-01-chat-b.md` with an honest **PASS (scoped)**, **CHANGES REQUESTED** or **INSUFFICIENT EVIDENCE**. Author's original screenshots/CI checks alone are not independent review.

**Do not merge on this readiness note.** Await supported independent review of exact candidate and preserve original failures. After independent PASS, guarded merge to main requires fresh actual-main cross-platform qualification and archive checks. Human classroom effectiveness remains unassessed.
