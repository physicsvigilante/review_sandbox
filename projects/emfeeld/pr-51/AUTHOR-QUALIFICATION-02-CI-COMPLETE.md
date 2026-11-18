# PR #51 — final exact-source CI and original Windows archive audit

**18 November 2026. AUTHOR QUALIFICATION COMPLETE; R2 REVIEW STILL REQUIRED.**

## Source identity

- [Draft PR #51](https://github.com/physicsvigilante/emfeeld/pull/51), head `f7cdf370fa44c40e6b5cb6d0c3ff580a7a364e52` on `feature/jee-dipole-v1`.
- Released base/main `6bfeb2c314841ef861d7d66b67c894a6295b705e`.
- Candidate/CI-preview Git tree `00592c7cc15d5013b4702951ff0db9baa7376b25`, preview commit `d14d78886ba366e6d0115e583cfcc25c7e7f9a80` with ordered parents [base, candidate]. GitHub's live commit endpoint verified that tree and the ordered parents. Nine added files; all 394 baseline paths unchanged (403 tracked files, 36 source modules).
- The five originally audited source TAR archives were byte-identical with SHA256 `805b06d1014f7574f879e583ebb82880223b55585a2ee4858974fdd807e106c0`, and their 403 files reconstruct to the candidate Git tree. No baseline law, solver, existing workflow, PDF or historical evidence was modified.

## Full hosted CI — final current candidate

**All six PR-triggered workflows completed SUCCESS**, including full [Linux/Windows release workflow #44319905997](https://github.com/physicsvigilante/emfeeld/actions/runs/44319905997). Original Ubuntu job `134855776278` and Windows job `134855777052` both returned final success. Each OS passed **1,894 headless tests + 18 historical behavioral tests (one preexisting obsolete guard deselected) + 62 actual PyVista tests**, and all downstream saved-evidence steps completed. The dedicated dipole workflow #44319905924 separately passed 83 focused tests and ten actual PyVista teaching scenes; these tests overlap the full suites and are not an extra 83 unique tests. Existing Gauss, conductor and viewer workflows also passed.

Author-side original artifact audits:

| Workflow / OS | Original artifact ID | Whole original ZIP SHA256 | Result |
|---|---:|---|---|
| Source #44319905552 | 14435605157 | `46e885c79cc4d011a5845156b676b372267a041508e5ecd8f2b608832b3d2b0e` | PASS; 403 source blobs/tree |
| Dipole #44319905924 | 14434077716 | `68794fc92d7f460f3d8014df3e96f654a823da7c8a85e383e921b8b30abf78d2` | PASS; 83 focused, 10 scenes |
| Gauss #44319905664 | 14434253713 | `8d9b6cbcec82b0e5dd6dd9ba1be5e7dce9bf96e55eb53ee8e07fe08b18781224` | PASS; existing lesson |
| Viewer #44319905714 | 14434576422 | `263cd16529749298c0ef328285797a217e8eb803e205f5baa2801f5bf333d417` | PASS; existing viewer |
| Conductor #44319905520 | 14434592015 | `6a81d30b8eff5d867872c7cb27d60747075dd3aca11f207262504a3bdf522ebf` | PASS; existing lesson |
| Ubuntu #44319905997 | 14436020601 | `76950977e6083aec8c255a43a22b735b2fa12acb806e6e959ea874a01a3a500b` | PASS |
| Windows #44319905997 | 14435833145 | `ac45c2d45ee18745b6b65d5a6cda9e0f52a2f4eb65d4f5dc0b3886da49d57dc1` | PASS |

The **new Windows ZIP** was downloaded after earlier Windows-in-progress status, whole-file SHA256 matched GitHub's original artifact metadata, and ZIP CRC/safe unique entries passed. Each of the two complete OS ZIPs had **2,186 members**, **173 integrity inventories**, **1,750 referenced hashes**, **1,749 matching references**, and **one known deliberate corrupted negative fixture** at `derived-001/G1/review-challenge-resealed-native/native/result.json`; it was deliberately *not* treated as valid evidence. Both checked original preview `head-sha.txt` and the exact 403 source files. All 82 implementation receipt sets per OS matched all **36 module hashes** (2,952 comparisons per OS; Windows checkout CRLF handled without rewriting the archive). Signed ensemble E1 remained complete and G1 remained genuinely partial. All scheduled original stage outputs were present.

The dedicated dipole ZIP had 97 members, 11 integrity manifests/171 matching references, ten PNG/state/implementation receipts (10 × 36 module hashes), and all ten physics/work measurements replayed exactly against the source code. The ten scenes include original Illustration 35, parallel/perpendicular/antiparallel, zero field, zero charge, changed work constraints, prediction, and translation/origin. This is a *visible* textbook example with separately documented SI assumptions, not an unseen JEE question or a teacher usefulness verdict.

## Original failures and limitations remain attributed

Original author test and graphics failures, interrupted local full runs and corrected harness mistakes are retained in [author qualification 01](AUTHOR-QUALIFICATION-01.md). Successful later exact-source runs do not retroactively certify those incomplete attempts. All archive checks here are read-only **author-side technical verification**, not independent R2 scrutiny, human Windows mouse/keyboard acceptance, or evidence of classroom usefulness. Artifact hashes are drift/integrity receipts, not independently authenticated external authorship.

**Next gate:** one separate-context independent R2 technical review of the exact candidate, using independently expressed endpoint-force, orientation-energy and geometry references, real production PyVista events/screenshots, authored-source preservation/refusals and original CI/source artifacts. Leave PR #51 draft/unmerged. After an accepted independent verdict and owner standing-direction integration guard, obtain **fresh actual-main** Linux/Windows/viewer/Gauss/conductor/dipole jobs and new original release archive audits before closing Issue #50.
