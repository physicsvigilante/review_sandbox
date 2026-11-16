# PR #25 — implementer response 01 to independent Chat B R1 review-01

**Disposition: BOTH findings REPRODUCED BY THE INDEPENDENT REVIEWER; CORRECTIONS COMMITTED ON DRAFT SOURCE; FRESH EXACT-HEAD CI / TARGETED RE-REVIEW REQUIRED.** (2026-11-16, Asia/Kolkata)

This is an implementer response **not** a Chat B review verdict or source merge approval. The original independent [review-01](../reviews/review-01-chat-b.md) is unchanged and remains **CHANGES REQUESTED** on its exact source SHA. Original reviewer first red attempts, negative reproduction receipts and earlier Linux/Windows release artifacts remain historical and unmodified.

## Identity and scope

- [Source PR #25](https://github.com/physicsvigilante/emfeeld/pull/25), qualified base/main `bf6a18399c604136dd363ad94d40557dbe2c2543`, original reviewed **failing** head `4fe896ff6bb98d21a090bc16a84fe26145f9f5e7`, original canonical tree `4df3703346ec7cba1ab74fcd6daa40796a535bf3`.
- Narrow F1/F2 source, regression and README correction committed as **`ec9df22bf822df7e33c2542b5dc059c9b59e7716`**, tree `29fc8167da9ed9ef24aea476aa22f8f64c41fcfa`, a direct child of failing head.
- Follow-on **test-fixture-only** correction **`a56b4680a90647ad4af03a52a0b9053807d10a7b`** (direct child of `ec9df22...`), presently the **current PR #25 head**. It creates an independent test's selected home directory before invoking the existing `imported` fixture, which writes files into that directory. There was no second source-logic change and no newly claimed test pass from this correction.
- Compared original failing head to new current source head via GitHub: **two commits, exactly three paths**: `src/emfeeld/scenario_ensembles.py` (+40/-10), `tests/test_scenario_ensembles.py` (+110/-2), `README.md` (+20). No fields/forces, solver, integrator, stored native inspector, model-store history, existing viewer code, CI workflow or numerical tolerance changed.
- Source PR remains **OPEN, DRAFT, UNMERGED** on this new head; pending CI completion and new independent focused re-review.

## F1 — foreign sealed evidence screenshot corruption: corrected in bounded preflight

**Reviewer evidence:** a genuinely new screenshot folder nested in another sealed native T1 run was allowed under former head; presentation subsequently added frame.png/presentation.json into a foreign sealed run and caused its unchanged original integrity inventory check to fail. This is an actual integrity failure even without overwriting any existing file; no numerical law or physics retargeting was implicated.

**Change:** new `_checked_view_screenshot` executes before `model_runs.present_run` and rejects:

1. Existing screenshot directories or symlinks, and any output inside the selected original ensemble/store/template.
2. **Every resolved ancestor** containing a recognizable completed saved-evidence seal `integrity.json`, even when it is a different unrelated ensemble, native run or sealed comparison.
3. Any recognizable model store root (`model.json`, `revisions/`, `proposals/`), older native run root (`run.json`, `summary.json`) or unfinished ensemble attempt root (`started.json`, `inputs/ensemble.json`).
4. Parent symlink aliases into those roots are resolved and rejected. A genuinely fresh external screenshot folder remains available; the existing real native presentation implementation still owns creating the directory.

**Regression:** added reviewer-derived 6-way parametrized negative test creating **two independent fully sealed ensembles** and challenging foreign native template, saved member run, sealed ensemble root, model store, sealed comparison and symlink-to-foreign-template, with complete original input path/bytes inventories plus foreign inspector validation. Also one negative test for a pending/unsealed ensemble root. The existing explicit external-output positive and current-store/ensemble/template negative tests remain unchanged.

**Limit:** path resolution plus no-clobber mkdir is not a malicious concurrent-writer or distributed crash-safe ACID guarantee. No claim of cryptographic protection if an attacker rewrites and reseals every file.

## F2 — member literally named baseline: distinct new run IDs plus full source-bound selection receipt

**Reviewer evidence:** saved physical runs/path/reference were *correctly different*, but the old `selection` label and `run_id` coincided for the fresh baseline and a valid member named `baseline`. Reporting ambiguity did not show physical selection of the wrong run.

**Change:**
- For **newly constructed** saved native members, the deterministic run-ID generator now uses `ensemble-{ensemble_id}-m-{member_id}`. The common fresh baseline remains `ensemble-{ensemble_id}-baseline`. These namespaces cannot collide, even when `member_id=baseline`, and the longest valid 25+25-character inputs produce a 62-character native ID within the existing 64-character grammar.
- View receipts expose `selection_kind` (`fresh_baseline` / `member`), `member_id` (null for fresh baseline), exact verified output-relative `run_path`, and SHA-256 of the selected native run's original `integrity.json`, alongside existing `run_id` and exact model revision reference. Display `selection` is now `baseline` versus `member:baseline` so even the human label is distinct.
- The change does not edit, rename, migrate, or recompute historical sealed run files. When a historical run has an inherited colliding `run_id`, the new view receipt still makes the actual selection unambiguous with kind, member, run path, reference and original seal hash.

**Regression:** new full **four-member** native ensemble case places the actual valid member named `baseline` at nontrivial **index 3**, runs both actual CLI selectors, validates source-bound path/references/receipt hashes and distinct stored new native run IDs. Directly tests longest legal native ID and preserved inspect semantics. Existing CLI and member selection assertions were tightened to the explicit new `member:` label, member kind, member ID, run path and intact native integrity hash.

## Qualification and next gate

Original exact **failing** head was fully author/CI qualified but independently **CHANGES REQUESTED**; those earlier green results do **not** qualify this new head. At this response publication the GitHub PR had advanced to `a56b4680a90647ad4af03a52a0b9053807d10a7b`, and **fresh exact-head Linux/Windows clean-install, separate real-PyVista, source snapshot, archive verification and targeted independent review are not yet claimed to have passed**. The new focused suite contains eight additional tests from two new test functions plus the six-way parametrization (original 54 -> prospective 62); expected future total headless test count increases from 1,456 to 1,464 if no other changes. These numbers are **anticipated suite definitions, not observed passing test results**.

After exact-head author qualification, publish a new narrow follow-up handoff pinning the final reviewed source/tree/CI, and ask Chat B independently to retest the foreign-sealed-run corruption and baseline-named member identity. Preserve the entire first review unchanged; do not merge without a new scoped PASS or explicit owner risk disposition.

No source production merge, model/physics API rewrite, user-machine Conda installation or original saved-study mutation was performed.
