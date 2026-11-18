# PR #164 — owner decision packet (JEE planar + native parallel-beam)

**Prepared 18 November 2026. Owner merge authorization: NOT RECEIVED. No merge or release has occurred.**

## 1. What has been independently cleared

[Opticsim draft PR #164](https://github.com/physicsvigilante/opticsim/pull/164), **HEAD `58ec0c237950d71e7b93b9b1639a52ada243e262` / Git tree `f371366765c8aa96029a0b29d6ae3f770e9b0eb2`**, has an independent [Chat B combined integration review](reviews/review-01-chat-b.md) verdict **CLEARED FOR OWNER DECISION, no P0/P1**. This verdict covers only this 33-file exact integrated source tree; it does **not** authorize GitHub merging.

The source is **main-based, single-parent, not a merge of the held PRs**. It exactly copies 31 existing Git blobs from separately independently reviewed-but-held [planar PR #161](https://github.com/physicsvigilante/opticsim/pull/161) (13 blobs) and [native parallel Beam v19 PR #141](https://github.com/physicsvigilante/opticsim/pull/141) (18 blobs). Two further files are the rehearsal-only integration test and audit documentation. A main comparison shows 25 additions, eight existing modified files, zero deletions. Source and synthetic CI merge **`fae01061165da6f9c1113caeff0d9404595da1df`** have identical Git trees. Production main was `d3509e82fb65d81aabe336666851f8f2962623f4` when this packet was prepared.

**Combined exact-tree builder evidence:** all **11/11 standard GitHub Actions workflows SUCCESS**, **860/860 Node tests PASS**. Real pinned PhyDemo and Chrome are builder CI results, not independently rerun by the reviewer. [Optical composition #44344350702](https://github.com/physicsvigilante/opticsim/actions/runs/44344350702), job `134942601780`: JEE Beam public acceptance (7 cases, four completed native), Beam Chrome (11 checks/six screenshots), standard browser (27 checks/15 screenshots), hosted smoke (five checks/one screenshot). [Plane mirror #44344351018](https://github.com/physicsvigilante/opticsim/actions/runs/44344351018) verifies 30 signed/rotated/unit mathematical cross-contract cases and genuine native Beam+pre-lens aperture+ideal-lens detector readings (eight emitted, six absorbed, two detector crossings and two actual hit events).

## 2. What the owner would release — limited JEE scope

1. **Analytical one-plane queries:** an explicitly stated incident-angle apparent-depth calculation and an independently typed source-to-observer conditional Snell ray. Predicted interface crossing and virtual-axis extrapolation are **mathematical**, `native:not-run`, not physically detected images.
2. **Opt-in single-ray real-native witness:** separately fully authored brightness, Fresnel setting, run preset, finite detector and tolerances; real native one-ray hit/complete measured detector zero/refusal, with source/first-interface integrity and actual detector callback provenance. It is **not** a general native inverse ray solver or perceived image.
3. **Native finite parallel-beam v19:** real pinned PhyDemo Beam emission through a bounded pre-lens aperture and ideal thin lens, or explicitly declared planar slab, with actual sampled detector crossing counts/positions. Conservative refusal of downstream post-lens aperture layouts where refracted corner geometry cannot be qualified. No continuous irradiance, PSF, full optical source ancestry, arbitrary mixed optical systems, thick-lens chain or model eye is implied.

The integration uses version-isolated v5 SingleRay and v19 Beam scene families. The review does **not** certify simultaneous Beam+SingleRay co-propagation in one scene.

## 3. Recommendation: ONE integration, not multiple source merges

If the owner wants to incorporate these tested JEE capabilities into production, **prefer authorizing PR #164 alone** after the release controls below. Do NOT also merge PR #161 or #141 (nor their original research/changes-requested ancestors): PR #164 already contains the exact selected source blobs. Redundant merges can generate conflicts, duplicate CI, or change reviewed ancestry. Original PR #141, #161 and older draft source branches remain frozen as historical review sources; the owner can later decide how to archive/close them **without merging**, separately from release.

A PR title or description saying **REHEARSAL ONLY / DO NOT MERGE** was intentionally used while no owner authorization existed. This packet does not silently remove that restriction. The owner must explicitly name **PR #164** and authorize integration under the confirmed controls; no assistant should interpret "continue" or "review done" as merge approval.

## 4. Mandatory release-process protection — still outstanding

The repository's [issue #123](https://github.com/physicsvigilante/opticsim/issues/123) is OPEN. At review, GitHub reported **`main.protected=false`** and repository rulesets **`[]`**. The connected GitHub integration cannot administer branch protection (GitHub's branch protection endpoint returned a 403). This is a **release-process safety gap**, separate from optical physics.

Repository-owner steps:
1. Open [Settings → Rules → Rulesets](https://github.com/physicsvigilante/opticsim/settings/rules). Create/activate a branch ruleset targeting `main` (or equivalent branch protection). Require pull requests and successful GitHub Actions checks, block unwanted force-pushes/direct pushes and deletion, and define narrowly scoped bypass privileges. Check that the ruleset **actually applies to main**.
2. Use the real GitHub Actions **check job names** observed for the approved head, selecting their correct source as GitHub Actions where possible: **`test`, `refraction`, `unified`, `qualified`, `motion`, `curved`, `angular`, `audit`, `mirror-angle`, `experiments`, `original-pair`**. The specific source workflow/job may be displayed as `Optical composition checks / test`, etc. Avoid accidentally weakening native/Chrome gates when selecting required checks. A Chat B review stored in `review_sandbox` is **not** a GitHub PR approval; enforce actual review rules only when a real eligible human reviewer can satisfy them.
3. Verify GitHub indicates protection is active and the required jobs/check sources are correct. Do NOT test protection by direct-pushing to production.
4. Before the owner's separate explicit merge authorization, confirm PR #164 **still** has HEAD `58ec0c237950d71e7b93b9b1639a52ada243e262` and tree `f371366765c8aa96029a0b29d6ae3f770e9b0eb2`; main base has not changed or has been retested on the new base; full required checks are green; the release scope remains these exact versioned JEE capabilities.
5. Only with separate owner approval and an effective release process should PR #164 be marked ready and merged. Verify the **actual resulting merge commit/tree** and execute post-merge Node 24/native/real-Chrome CI; do not substitute pre-merge CI as post-merge evidence.

## 5. What follows a successful owner-authorized release

A **separate draft [CI-safety PR #162](https://github.com/physicsvigilante/opticsim/pull/162)** is builder-tested (11/11 workflows on main-target and on a real feature-target smoke PR #163), adding safe stacked-branch PR base triggers without reducing any native/browser checks. It is **not included in PR #164**. If #164 is merged, revalidate #162 against the *new* main before seeking a separate owner integration decision. It is process work, not a new optics feature. A main ruleset should remain independent of CI source changes.

Later, the thick-lens v14–v18 chain and detector-directional-footprint work need separately planned cross-source integration because they overlap adapter/contract/observables/app changes. Their old independent reviews and current draft/held status do not become release approval via PR #164.

## 6. Nonblocking follow-up tests

- **N1:** explicit negative cross-version test that Beam cannot stand in for the v5 SingleRay witness, alongside a positive v5 witness in the same integration test.
- **N2:** expand the 30-case cross-contract analytical matrix to varying refractive indices, normal distances, translation and near-axis/critical-boundary refusals.

Chat B classified both as **nonblocking**. Preserve this independently reviewed exact source tree; implement as a future test-only hardening change with builder verification, rather than forcing an unnecessary new independent review of unmodified physics.

**Current decision: HOLD.** No release/merge authorization, no installed main protection and no deployed code claimed by this packet.
