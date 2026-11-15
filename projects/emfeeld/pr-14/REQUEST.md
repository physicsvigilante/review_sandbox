# EM Fields PR #14 — R2 independent review request

- projectId: `emfeeld`
- sourceRepo: `physicsvigilante/emfeeld`
- sourcePR: https://github.com/physicsvigilante/emfeeld/pull/14
- baseSha: **`7e6bd8c72cac7708ab3c2355cc1a98db09762133`**
- headSha: **`d46d04e23a142ea1c969b964ae5e1780110264c9`**
- sourceTreeSha: **`c274d94dd2185dcecdfca735e2951edae3e3d835`**
- qualification CI checkout: `014d74123551cd1ab0ce5fbc335082663d160352`, same exact Git tree
- reviewClass: **R2**, physical initial conditions, stable structural identity and saved numerical-evidence meaning
- current source status: **draft, unmerged**; no Chat B review yet
- reviewer report destination: `projects/emfeeld/pr-14/reviews/review-01-chat-b.md`, new Chat B-authored file only

## Code and contract to review

Read [pinned AGENTS.md](https://github.com/physicsvigilante/emfeeld/blob/d46d04e23a142ea1c969b964ae5e1780110264c9/AGENTS.md), [particle revisions V1 contract](https://github.com/physicsvigilante/emfeeld/blob/d46d04e23a142ea1c969b964ae5e1780110264c9/docs/PARTICLE_STRUCTURAL_REVISIONS_V1.md), [developer validation record](https://github.com/physicsvigilante/emfeeld/blob/d46d04e23a142ea1c969b964ae5e1780110264c9/docs/PARTICLE_STRUCTURAL_REVISIONS_V1_VALIDATION.md), and [exact PR diff](https://github.com/physicsvigilante/emfeeld/compare/7e6bd8c72cac7708ab3c2355cc1a98db09762133...d46d04e23a142ea1c969b964ae5e1780110264c9).

Production changes are limited to new `src/emfeeld/particle_revisions.py` and narrow dispatch in `src/emfeeld/model_revisions.py`. Tests: `tests/test_particle_revisions.py`. Native transfer and independent-formula/RK4 tools: `tools/qualify_particle_revisions.py`, `verification/check_particle_revision_runs.py`. Frozen docs and release workflow additions only. No new solver, force law, integrator, energy diagnostic, viewer, dependency, or relaxation of numerical tolerances.

Expected behavior: add/remove a **named independent test particle** from one existing same-domain, immutable, exact-parent model using proposal_version 2. Add requires explicit physical mass (>0), three-position and velocity vectors, electric charge in electric systems; gravity charge omitted or exactly zero, with omitted default provenance recorded. Remove requires exact canonical particle payload, preserving all other sources and particles. Reject historically reused or wrong-role IDs, stale refs, dangling computed dependencies and invalid physical inputs. Preserve previous runs byte-for-byte; recompute analyses fresh. A removed particle's old named observation must fail instead of retargeting via changed native index. No particle-particle forces or source feedback. The last particle may be removed, leaving static sources. Shell/plane trajectories remain unsupported.

## Exact source CI evidence

- [Full Linux/Windows clean-install](https://github.com/physicsvigilante/emfeeld/actions/runs/43740900095) **PASSED on both**: **1,308 headless + 18 historical behavioral + 33 real-PyVista = 1,359 tests per OS**. Historical whole-file frozen assertion is unchanged and explicitly deselected. Same cases across OS, not 2,718 distinct tests.
- [Separate real-PyVista CI](https://github.com/physicsvigilante/emfeeld/actions/runs/43740899982) passed.
- [Source snapshot](https://github.com/physicsvigilante/emfeeld/actions/runs/43740899969) passed, provenance only.
- Linux artifact ID **14172094227**, ZIP SHA256 **`a56b4b1352fcdcc31089ceca9b54ffb3e23910587f828ecc66b48b2e6830fed1`**.
- Windows artifact ID **14172751162**, ZIP SHA256 **`aa975b9ff5cd309df360b2f618c6b6b4163b6d1ca41b5a05612fa33baee29d08`**.
- Both artifacts (1,451 entries each) downloaded, ZIP checksums and CRC verified; native `qualification.json` status complete and separate reference report status passed. CI preview's Git tree matches exact PR head.

Cases: **E1** add charged particle to negative line + axial field, check both trajectories and unchanged original. **G1** remove Body 1 from two gravitational sources, verify named Body 2 reindexes p1→p0 without changed physics, refuse old Body 1 observation. **T1** static electric shell/point with no original particles: add/remove illustrative particle; field/potential probes unchanged and no unsupported motion claimed. **Seven complete native runs + one intentionally rejected analysis, four accepted revisions, six checked trajectories (606 states), and 34 static checks** per platform. Same-author independent-formula/RK4 checker is not independent Chat B certification.

## Preserved failures and uncertainties

First local authored-test attempts had 35 pass/2 fail and 42 pass/1 fail due to test expectations, not claimed engine defects. Initial non-editable-install full run had 1,296 pass/6 subprocess import failures; fully installed isolated environment later passed 1,308. All documented in developer validation. No original source/model files are rewritten. T1 was selected by the same author, not a hidden benchmark.

The reviewer should independently challenge structural identity lifetime and race handling, particle physical schema/provenance, G1 stable-ID remapping, missing observations, dependent computation receipts, source-only operations remaining intact, and numerical-source evidence. Distinguish independently executed tests from Chat A CI. Hashes are byte-integrity checks, not signatures. Separate-chat LLM review is not independent human expertise or classroom assessment.

## Output

Following [REVIEW-TEMPLATE.md](https://github.com/physicsvigilante/review_sandbox/blob/main/REVIEW-TEMPLATE.md), Chat B independently authors **new** `projects/emfeeld/pr-14/reviews/review-01-chat-b.md` (or a central review-only PR), giving exact source SHA/tree, reproducible failures, limitations, and scoped **pass / changes-requested / insufficient-evidence**. Do not modify or merge the production PR. The owner may say **“Review complete”** to Chat A after the GitHub report exists; independent review and explicit owner merge approval are separate gates.
