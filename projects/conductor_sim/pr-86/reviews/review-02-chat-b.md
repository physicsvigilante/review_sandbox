# M36c PR #86 — independent R2 review #02 (bounded)
**Verdict: INSUFFICIENT-EVIDENCE for independent R2 PASS.** This is not a physics FAIL or merge authorization.

Reviewed at 2026-11-18. Production `physicsvigilante/conductor_sim` draft PR #86 (open, unmerged). Checked live PR head **`82de04484006d61f691e1e3a1344f5707729a821`**, native Git commit-tree object **`c43134db1726dc2f1ff48b0b9a560dff090bf56d`** from GitHub's actual Git commit API. Released base `5693aaa4fca42fa996fd0983b95c8a104a45af93`. Seven source apparatus, eight historical question anchors, two exclusions; no JEE-wide success percentage.

## Evidence actually inspected by this reviewer
- Fetched exact-SHA source `tools/m36c_jee_conductor_replay.py`, `tools/m36c_jee_conductor_reference.py`, `tests/test_m36c_jee_conductors.py`, `tools/check_m36c_conductors_browser.py`, `docs/m36c.md`, workflow and review request.
- Verified 19 current-HEAD PR workflow runs report **completed/success**, including Python 3.10/3.12 (run **44264604417**, both jobs success), true FEMM5 (**44264604475**, job 134665896746 success), historical visualization/Chromium (**44264604501**, job 134665902191 success, historical browser steps reported successful), M36b (**44264605106**, job 134665899296 success), and dedicated M36c source/native/reference/Chromium (**44264604519**, job 134665897671 success). This is CI evidence, **not independent reviewer-run verification**.
- Developer-controlled source-pinned `review_sandbox` run **44264857366** is reported successful in the correction request, but artifact 14409961298, its claimed ZIP SHA256, and rendered screenshots were **not** independently downloaded, hashed, or visually examined here.
- This environment cannot resolve github.com from its local Git/Python execution container; `git ls-remote` failed DNS. Original book PDFs were not independently opened. Therefore no source-head checkout, no new actual `NestedShellBackend` or `ExternalSphereBackend` model variations, no reviewer-authored detached native-result falsification run, no Chromium visual readability assessment, and no refusal execution occurred in **this independent review**. Do not claim those checks passed.

## F-01 — p27 original central charge and actual A/B
Source is now coded to use a first state with central q at [0,0,0], two actual finite-thickness conducting shells, and `NestedShellBackend.potential_at(A)` for A=[0.04,0,0] and `potential_at(B)` for B=[0.15,0,0]. Second state uses shifted q at [0,0,0.02] and explicitly says TEACHER EXTENSION ONLY. HTML code visibly inserts an original A/B section and actual finite-metal potentials; Chromium source-marker script checks those visible terms. These are **source-code observations**, not independent rendered screenshot certification.

Separately recalculated SI Gauss-law reference for q=1 nC, q1=2 nC, q2=3 nC, a=0.10 m, b=0.20 m, metal width=1 micrometre:
- ideal thin-shell V(A) = **539.2531075356703 V**, V(B) = **314.564312729141 V**;
- genuine finite-face V(A) = **539.2515347017487 V**, V(B) = **314.5636386593863 V**.
These reproduce the distinct formulas coded into the source-free verifier. They do not independently establish a native solver run on a *new* model. The notes PDF p27 Illustration 4 was **not** reopened here; the printed central-charge/AB interpretation is taken from correction request and earlier reviewer, not certified anew against the image.

## F-02 — p26 solid versus hollow
Implementation and checker declare the printed original is a **SOLID** conductor and disclose a **HOLLOW SHELL PROXY** (0.09–0.10 m) for limited radial V/E observations. HTML uses `original-solid-sphere-proxy-disclosure` and explicit words that the hollow cavity is not in the source. This is a science-honest limitation, not a source-authentic solid geometric visualization. Literal solid rendering, if a requirement, remains outstanding. The visible appearance/readability of screenshots has not been independently examined.

## F-03 — source-attribution falsifications
Exact-head checker enforces the original p27 source anchor 'Illustration 4', original state and central position, named shell identity, fixed A/B physical points, teacher/scenario distinction, and SI measurements. For p69 it checks the near-side angular theta=0 and far-side theta=pi rather than accepting numerically plausible, misattributed density. Checked code includes four targeted tampering tests: both swapped p69 angle labels, p27 inner-vs-outer conductor identity, and forged p27 source anchor. These are **present and green in developer-triggered CI**, but I could not run them independently on newly generated detached JSON.

An independent hand-calculation from the Kelvin induced inner-surface law for q=1 nC, cavity radius 0.08 m and displaced source 0.04 m yields near-side sigma **-7.460387957432595e-8 C/m²** and far-side sigma **-2.7631066509009607e-9 C/m²**. This supports the angle semantics, not a live native falsification outcome.

## Independence gate and remaining actions
**Must complete before R2 PASS**:
1. Reviewer-owned executable probe on *exact* HEAD/TREE: at least three unfamiliar qualified physical conductor families, original precomputed SI predictions compared with native API, and unqualified overlap/nonconcentric/3D refusals; preserve first outputs and provenance.
2. Freshly generate detached native JSON on the pinned source; run positive control and old three **plus newly invented** falsifications (wrong A/B position, source-charge displacement, angle/sign/shell identity) against source-free checker; save actual exit codes/rejection.
3. Independently view original PDF p26/27 pages and actual seven browser screenshots/HTML, including genuine first-state A/B and solid/hollow disclosure; distinguish visibility from pedagogical readability; check two partial/unsupported controls are refusals.
4. Verify CI log/artifact fidelity if requiring artifact-byte proof, and recheck PR HEAD and Git TREE before signing off.

## Preservation and authority
Earlier R2 #01 on superseded `1f5bd9fcee30f534e15f874c87f8ff0441a62fe8` / tree `b31fd1843b57de5403d2a36b2cb86fa1385f659a` remains **CHANGES REQUESTED**, notwithstanding old 19/19 green CI. Historical initial-source failures **44257593862** (float coordinate equality) and **44257760238** (assumed HTML title) remain failures; subsequent green runs do not erase them. No production file was changed by this review. PR #86 must remain draft/unmerged pending true independent R2 approval and explicit separate owner approval. Even a later PASS cannot authorize a merge, and the exact reviewed tree and postmerge main push CI must be checked.
