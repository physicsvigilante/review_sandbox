# SIM_HEAT H2-00 — owner-approved PR #12 merge and post-merge verification

**Recorded:** 2026-11-15. **Status: MERGED, POST-MERGE OFFLINE CI PASS**, scoped to H2-00 source integration. This is a developer merge/evidence record, **not a new independent Chat B review** or general H1 native qualification.

## Authorization, merge and source identity

- The owner explicitly replied **“approved”** to Chat A's specific request to merge [SIM_HEAT PR #12](https://github.com/physicsvigilante/sim_heat/pull/12). No approval was inferred from a reviewer report or CI result.
- Before merging, Chat A rechecked that PR #12 was unmerged and mergeable, the original `main` was `49a2cc42462b47026e86313bfeff39a9b17081cd`, the PR head was `adb1b664d1a026f2f6cf017c11eda057d791595e`, the final-head [CI run 43728497707](https://github.com/physicsvigilante/sim_heat/actions/runs/43728497707) passed, and the second independent-in-context report was a scoped PASS for the exact corrected head.
- PR #12 was marked ready for review as a GitHub prerequisite and then merged with GitHub's **merge-commit** method, using `expected_head_sha=adb1b664d1a026f2f6cf017c11eda057d791595e` to refuse intervening head changes. The GitHub API returned `merged=true`.
- **Final merge commit:** [`ecebc38dd3f6eaffd297bd3df97a0883e591c6ac`](https://github.com/physicsvigilante/sim_heat/commit/ecebc38dd3f6eaffd297bd3df97a0883e591c6ac), with exactly these parents in order:
  1. old `main`: `49a2cc42462b47026e86313bfeff39a9b17081cd`;
  2. reviewed head: `adb1b664d1a026f2f6cf017c11eda057d791595e`.
- **Merge tree:** `618a3f774ff2d304295803f25eda79e78adb1492`, **identical** to the independently reviewed final-head tree. No new physical source edit occurred during the merge. The GitHub branch `main` and PR #12 `merge_commit_sha` were verified to equal the merge commit. PR #12 is now closed/merged.

## Post-merge CI (actual fresh main run)

- **CI run:** [43731531075](https://github.com/physicsvigilante/sim_heat/actions/runs/43731531075), GitHub Actions workflow `.github/workflows/h2-h1-offline-ci.yml`.
- **Triggered by:** push of the merge commit on `main`; **head SHA** `ecebc38dd3f6eaffd297bd3df97a0883e591c6ac`; **attempt 1**.
- **Outcome:** `completed / success`, one successful offline job. All required job steps succeeded, including checkout, Python setup, dependency installation, source/runtime identity capture, H1 tests, bridge admission and separate reference preparation, and evidence upload.
- **Observed test logs:** **151/151** H1 tests passed and **4/4** separate analytical arithmetic tests passed. The preserved bridge admission says `admitted=true` and `nativeExecuted=false`; a checking-only bridge reference was prepared, not simulated. This run used pinned Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0 and checking-only mpmath 1.3.0 on GitHub-hosted Ubuntu 24.04. Dependency install uses network-capable pip; "offline" does **not** mean air-gapped.
- **Post-merge CI artifact:** [14168921188](https://github.com/physicsvigilante/sim_heat/actions/runs/43731531075/artifacts/14168921188), named `h2-h1-offline-evidence-ecebc38dd3f6eaffd297bd3df97a0883e591c6ac`, **647,604 bytes**, original ZIP **SHA-256 `03d7ea5fe62bf699b4677f9e30fd022ac41de7f90e2647af88600a99f939ac7d`**.
- **Download inspection by Chat A:** ZIP size/digest recomputed and matched GitHub artifact metadata, ZIP CRC passed, `head-sha.txt` exactly matched `main` commit; logs independently read from ZIP report `Ran 151 tests ... OK` and `Ran 4 tests ... OK`. The `source-files.sha256` manifest is included for reproducibility; comparing a digest and CRC is an integrity check of the downloaded evidence, **not independent authentication of native host execution**.
- **Native OpenModelica calls from this integration CI:** **zero**. No compilation, native model launch, extra measurement, missing-output repair or false native-qualification promotion.

## Independent review chain and disposition

- Original first-pass [Review 01](reviews/review-01-chat-b.md), pinned to `f2bb5369425a250cef78b74baaf486925f8fa6bd`: **changes-requested**, confirmed F-01 misleading independent-measurement field. Review file remains unchanged.
- [Developer response 01](responses/response-01-chat-a.md): versioned MAT provenance `sim_heat.matv4_adapter/2`, narrow `hasUniqueMATChannel`, regression coverage and F-02 wording clarification. Intermediate [failed CI 43728041002](https://github.com/physicsvigilante/sim_heat/actions/runs/43728041002) remains intact, reflecting strict old-hash refusal.
- Targeted independent-in-context [Review 02](reviews/review-02-chat-b.md), pinned to final corrected source `adb1b664d1a026f2f6cf017c11eda057d791595e`: **PASS only for that correction**, no new demonstrated blocker. The report was authored in a separate ChatGPT conversation; it did not re-run all native experiments, does not certify a different independently trained model or human expertise, and never grants merge permission by itself.
- [Developer response 02](responses/response-02-chat-a.md) records closure of demonstrated F-01 and preserves original reviewer findings and remaining limitations. No other independent review was invented.

## Scope and open gates after merge

The mainline now holds the curated H1 restricted Modelica grammar, lumped-capacity/conduction/fixed-temperature components, studies/provenance/requests, MATv4 numeric decoder and provenance v2, separate numerical reference and checker, fixed host-guarded native batch helper, the original demonstration cases and offline-only CI. Historical one-shot native workflow triggers were deliberately **not** installed on `main`; original experiments and failed/passing cloud artifacts remain on their historical branches and in Actions storage.

**This was a bounded integration promotion, not scientific acceptance of arbitrary topology or general user-supplied Modelica.** Numerical/native observations remain `diagnostic_only`, `nativeQualified=false`; independent R3/reference error certification, remaining original review conditions, a post-freeze unfamiliar-author C1 attempt, broad charter transfer, classroom usefulness and a teacher-facing viewer are still separate work. Native evidence previously gathered for D1/D2, conductivity/resolution, and a developer-authored thermal bridge remains historically valid only for its tested source and scope.

No other experimental PRs were merged as part of this authorization. An explicitly scoped next feature PR is required for the viewer or new physics. The original `01_heat.pdf` remains unchanged and is not relicensed.

## Closure

**H2-00 source integration is merged and post-merge offline regression-verified.** The central review packet and all original independent reports, original CI failures, immutable native evidence, and developer responses remain linked and preserved. No further action is required for this exact reviewed/merged candidate; new features require their own risk classification and CI/review workflow.
