# Owner setup: protect Opticsim main without weakening physics gates

**Owner/admin action required. Prepared 18 November 2026.** This is a configuration checklist, not an assertion that the settings have been changed. Production `physicsvigilante/opticsim` is a **public** repository, branch `main` at `d3509e82fb65d81aabe336666851f8f2962623f4` as of last independent check. GitHub returned `main.protected=false`, repository rulesets `[]`, issue [#123](https://github.com/physicsvigilante/opticsim/issues/123) open; the connected GitHub app cannot change protection (403).

## GitHub UI actions for the owner

1. Open [Opticsim Settings → Rules → Rulesets](https://github.com/physicsvigilante/opticsim/settings/rules), choose **New ruleset → New branch ruleset**, give it a name such as `Protect main — JEE physics CI`, target default branch `main`, and set **Enforcement: Active**. Exact UI wording may vary. If Rulesets is unavailable use Settings → Branches → Add branch protection rule for `main`.
2. Require all changes to be made **through a pull request**, block **force pushes** and **deletion**, and limit bypass permissions. Make explicit owner merge decisions the release gate; Chat B's independent external report is **not a native GitHub PR approval**. If requiring a GitHub approval as well, ensure a real eligible repository reviewer can provide it; do not inadvertently prevent all owner merges.
3. Enable **required status checks** for the same GitHub Actions workflows currently protecting physical correctness and browser evidence. The exact observed GitHub Actions **job check names** (not just workflow display names) at the reviewed [PR #161](https://github.com/physicsvigilante/opticsim/pull/161) commit were:
   - `test` — Optical composition checks, full Node/native/Chrome acceptance;
   - `refraction` — Planar refraction checks and real browser acceptance;
   - `unified` — Unified problem and teaching-fidelity browser workflow;
   - `qualified` — Qualified authoring and Chrome;
   - `motion` — Quasi-static source motion;
   - `curved` — Curved mirror native/browser;
   - `angular` — Deterministic planar angular query browser/provenance;
   - `audit` — Numerical ray reliability;
   - `mirror-angle` — Plane-mirror angular controls;
   - `experiments` — Parameter experiment controls;
   - `original-pair` — Original refraction problem pair.
4. Select these statuses from **GitHub Actions** as their source if the UI offers source pinning. Confirm each selected check exists and has succeeded on the current target PR head/base. It is safer to have a genuine required status than a label or a manually asserted pass. GitHub may display the workflow and job together (for example `Optical composition checks / test`).
5. Consider **Require branches to be up to date before merging**, or GitHub's equivalent merge-queue validation, so a changed `main` triggers new combined checks. If new source or target changes, independently compare the new Git tree and run real tests before an owner merge.
6. Save/enforce the ruleset, then reopen the ruleset page and verify it is **Active**, targets **main**, has intended bypass rules, and actually prevents an unapproved PR merge with missing checks. Confirm GitHub's API/branch UI shows protection applied. **Do not test by pushing directly to production main.**

## Approved source and merge ordering

- [PR #161](https://github.com/physicsvigilante/opticsim/pull/161), HEAD `09ad081a34ced0fa969affc1bf54766cabffb04a`, Git tree `1b2caf6186c8eaf678963238d2292001b2fa9667`, is **independently CLEARED FOR OWNER DECISION, no P0/P1** (not merge approval), with **832/832 Node tests, 11/11 GitHub Actions** on its exact synthetic CI tree. It remains draft/unmerged.
- The code-safety improvements for PR #161 are already part of this **one** exact source; do not merge separate historical PR #144, #150, #151, #153, #155, #157, or #159 to obtain them.
- A separate, unmerged CI safety branch [PR #162](https://github.com/physicsvigilante/opticsim/pull/162) proposes extending all 11 workflows' `pull_request` base filters to feature/research/fix/study/integration/design branches while **retaining main-only push, read-only permissions, full Node 24 and native/Chrome steps**. This is release-process work, not the source code or clearance of PR #161. Complete CI and a feature-base smoke test before any owner approval of this separate change.
- **Recommended sequence:** Protect `main` first. With a **separate explicit owner instruction**, merge **PR #161 alone** if its reviewed SHA/tree/required checks still match and the rules are active. Verify actual post-merge source and rerun post-merge CI/native/Chrome. Then assess PR #162's fully tested CI workflow improvement for a separate explicit owner integration decision. This avoids invalidating the reviewed planar source tree by changing its target `main` before that integration.
- No merge is authorized by this checklist or by "continue." All other stacked optical feature lines remain individually held. Any new native v19/thick-lens integration must be checked on the then-current `main` and against its actual dependency base, and independently reviewed only when physical/result semantics or cross-feature safety changes.

## What counts as safe evidence

Passing Node tests and actual builder native/Chrome workflows on a matching Git tree are mandatory builder evidence; an independent reviewer checks the source/physics/provenance separately. A measured detector zero is legitimate native data but not invisibility; an analytical conditional ray is not a native hit or physical image. Test-injected native-shaped records are classifier tests, not real PhyDemo output. SHA-256/exclusive files are freshness, not tamperproof authentication. These distinctions must stay intact across CI policy changes.
