# PR #44 — Chat B independent R2 review 01

**Verdict: INSUFFICIENT EVIDENCE — independent R2 NOT PASSED; do not merge.**

**Attribution:** Chat B (OpenAI GPT-6), independent reviewing assistant, **18 November 2026**. This review was prepared independently of the source author and published through the connected GitHub account `physicsvigilante`; it is *not* a separate human reviewer's endorsement. All reviewer executions and their first failures are distinguished from author-run CI.

**Candidate:** [`physicsvigilante/emfeeld@e253d0acf15e7505f1da8ab95cb519b59b0d720b`](https://github.com/physicsvigilante/emfeeld/commit/e253d0acf15e7505f1da8ab95cb519b59b0d720b).  
**Expected/verified Git tree:** `8a4a14d70ba824e8a338add08356003e79a248bc`.  
**Base:** `60b6e751363d0b922a02c3a259110547b79cf25c`.  
**CI source-equivalent preview:** `04f8926ff15697ecccd9d89f71e837f2eb45bf56`, independently verified to have the same tree and ordered `[base, candidate]` parents. This preview is **not** a merge.  
Reviewed [instructions](../REVIEWER-PROMPT-01.md), [request](../REQUEST.md), [author qualification](../AUTHOR-QUALIFICATION-01.md) and [exact source contract](https://github.com/physicsvigilante/emfeeld/blob/e253d0acf15e7505f1da8ab95cb519b59b0d720b/docs/CONDUCTOR_CAVITY_LESSON_V1.md).

## Decision and the missing gate

The independently executed physics, numerical, snapshot-protection and archive-integrity challenges below found **no demonstrated physics or source-preservation defect in the tested domain**. The original six PNG scenes were actually opened and inspected, and reviewer-created VTK arrow-geometry checks passed.

However, this review environment has **VTK 9.6.2 but no PyVista**. I **could not instantiate the original `CavityLesson`/PyVista `Plotter`**, fire its actual four slider widget and keyboard events, inspect its live VTK representation membership, or save a newly rendered PNG from a freshly modified live controller. Inspecting author-produced screenshots and running independent VTK geometry reconstructions do **not** constitute the independently executed **real PyVista/graphics-control** test explicitly required by the R2 instructions. The author's original Linux/Windows real-PyVista CI passes remain valuable *author-qualified* evidence but cannot be counted as a reviewer-owned real-UI execution. A reviewer full-headless rerun also timed out after approximately 25%, not a complete pass.

**This is an independent-execution evidence gap, not a finding that the source controls are broken.** Complete the narrowly scoped reviewer-owned real-PyVista/VTK controls + screenshot capture described below, retain its first failures and raw outputs, then reassess R2. Keep PR #44 draft/unmerged in the interim. Actual-main post-merge workflow/archive qualification, a new unseen JEE problem and human Windows/teacher acceptance remain separate gates.

## Exact source, original PDF, and adaptation

- The *original* GitHub source TAR was reconstructed independently into a temporary working copy and Git index. `git write-tree` exactly returned **`8a4a14d70ba824e8a338add08356003e79a248bc`** across **382 tracked files**. GitHub compare lists **nine added paths, zero modified or deleted baseline paths**, with **32** Python package modules. Existing field/particle laws, source theory PDF, prior workflows and retained studies were not edited.
- Original `01_theory_elec.pdf`: **140 pages**, SHA-256 **`dfed5a5cf241a365a2d94ebfeb73a9473aad66184d73af38be7fbfd81e6876ab`**. Independently extracted text and rendered/inspected **original PDF pages 115, 117, 123, 124**. Printed **1.115** discusses inner `-q`, outer `Q+q`, zero metal field and equipotential conductor. Printed **1.117 Q5** involves a central charge/thick shell. **Q7** involves an off-centre charge at `R/2` in a **neutral thin shell**, asking field-line sketches. Printed **1.123–1.124** discusses image charges with grounded-*plane* examples; it does not present the spherical image/density derivation.
- The lesson's `R=1 m, B=1.25 m, q=1 nC` default is visibly documented as an **illustrative thick-shell adaptation**, **not** an exact reproduction of Q7. Its spherical-cavity image and density formulas are separately derived. **Source fidelity/disclosure: acceptable.** This does not establish a solved textbook corpus or unseen-task capability.

## Independently executed physics and state checks

**Environment:** isolated Linux container, Python **3.13.5**, NumPy **2.3.5**, SciPy **1.17.0**, pytest **9.0.2**, VTK **9.6.2**; PyVista **unavailable**. Reviewer programs, original failure logs, corrected logs, source/scene audits and image proofs are retained in the user-facing evidence archive **`emfeeld-pr44-chat-b-r2-evidence.zip`**, SHA-256 **`e351554c8ee9511a66a1e3cd0c2079b1e41933e18c699c42403ecbf6e637a32b`**, attached to the review conversation. This bundle is reviewer evidence, not a reissued original GitHub Actions ZIP. Reproduction root: original pinned source at `/mnt/data/r2_emfeeld_pr44/source`; reviewer files at `/mnt/data/r2_emfeeld_pr44/reviewer-evidence/`.

```sh
# From the independent, reconstructed source root:
PYTHONPATH=src python -m pytest -q /mnt/data/r2_emfeeld_pr44/reviewer-evidence/test_independent_r2.py
# 42 passed in 1.69 s — reviewer-authored cases, not author tests

PYTHONPATH=src python -m pytest -q /mnt/data/r2_emfeeld_pr44/reviewer-evidence/test_vtk_native_arrow_challenge.py
# 15 passed in 1.14 s — native VTK reconstruction, NOT real PyVista widget/actor execution

PYTHONPATH=src python -m pytest -q -W error tests/test_conductor_cavity.py tests/test_cavity_lesson_io.py
# 67 passed in 3.04 s — source-authored focused tests, counted separately

PYTHONPATH=src python -m pytest -q -W error tests
# ATTEMPTED; environment timed out near 25%; NO whole-suite result claimed

python /mnt/data/r2_emfeeld_pr44/reviewer-evidence/audit_original_archives.py
# PASS — original ZIP/TAR/tree, saved images/arrays, original OS evidence
```

**Independent analytical cases — 42 pass:** independently constructed two-charge Coulomb-image reference against cavity `E,V` for off-axis 3D rotations, `q>0/q<0`, `a/R=.17,.53,.895`, several prescribed `Q` and grounding combinations, 35 seeded random cavity probes per combination and distinct metal/exterior probes. Centre/zero limits; `Q=-q` exterior cancellation; grounded potential/exterior zero and isolated `k(Q+q)/B`; metal `E=0`; conductor equipotential; finite-difference `E=-grad(V)`, 3D rotation covariance; near-wall normal discontinuity `E_n=-sigma/epsilon_0`, vanishing tangential field; regular **physical** exterior at image-location coordinates (no physical virtual-charge singularity); independent SciPy axis-integral and sampled angular orders **8, 16, 32, 64, 256 without normalization or rescaling**; sign-aware field-line directions/terminations; extreme admitted dimensions/charges and charged-boundary, source-point, duplicate-JSON and invalid-domain refusals. Correct reference: inside the cavity use mathematical `q'=-qR/|a|` at `b=R² a/|a|²` **only within the cavity**; exterior field is separately `Q+q` isolated, zero grounded. Induced inner `-q`; outer isolated `Q+q` (grounded zero); surface density `-q(1-t²)/(4πR²|n-v|³)`, with at `t=.5` near/far **local density** ratio 27, *not* a hemisphere integral.

**Independent VTK geometry — 15 pass:** instantiated `vtkArrowSource` **vertex meshes**, used a separately implemented 3D orthonormal frame to apply the production half-arc-length/scale placement prescription, verified entire glyph meshes stay inside the cavity (several 3D directions and `a/R` from centre to approximately **.9**, both charge signs), stay clear of the source, and point along physical `E`; outer arrows likewise remain outside the conductor. **These are independent reconstructed VTK glyphs, not the source's actual `pv.Arrow` objects, not renderer actor-membership tests and not mouse/keyboard interaction tests.**

**Independent fresh output protection:** a new headless snapshot saved the **current state** separately from the immutable original input bytes, correct SHA bindings, seven physical curve arrays, reported state and successful integrity seal. Deliberately injected trace failure left original `started.json`, `lesson.json` and incomplete `outcome.json` with **no false success seal**; fresh and nested retry aliases were rejected without rewriting first-attempt hashes. Independently refused output under sealed evidence, model store, locked question and symlink alias into sealed root. This **does not substitute** for live-controller modified-widget → saved screenshot consistency.

## Original archived evidence — independently audited

Downloaded and read *five original exact-head GitHub Actions ZIPs*. Checked entire ZIP SHA-256, ZIP members/CRC, no duplicate or unsafe paths, source TAR equality across source/lesson/legacy viewer, and all 382 exact source tree members. Source TAR SHA-256 **`ffafd8907459cfc32e3408e66bccdd2aea89608b8639eb3d47ef92c5ef8396f5`**.

| Original artifact | ID | Exact ZIP SHA-256 | Entries |
|---|---:|---|---:|
| Source | `14401692570` | `33059d044eb2b8ce824ecd6c7b65e3e05033b2fd30ca1f77676cd2f8e0437367` | 4 |
| New lesson | `14402305972` | `6f3e8cb68c2624593c077edb15fe8ac4d0502eb0b47fc5d6e612a4277fc98c55` | 49 |
| Existing viewer | `14401798242` | `0ac15d5de6585251345dd637836e658c929ccc1e13d14fb9aa1e571ca015a1c2` | 22 |
| Ubuntu release | `14402041927` | `5ae9758ebbd3b8995c300f57a5702d929900f13921d47b3bfb9c4ee9b7274f96` | 2,186 |
| Windows release | `14402262223` | `895306335a7931b0c31d766526ca0f93c84a45e17dbb8af498d79938cf10bc65` | 2,186 |

**Original scene inspection, not hashes alone:** extracted and personally viewed all six **1400×900** original Linux lesson PNGs — positive off-centre, centred, grounded, negative grounded, negative isolated charged, rotated full shell. The four slider representations, JEE charge-balance panel, legible labels, cutaway/full-shell distinction and changed field/surface states are visible; no virtual image marker appears as a real charge. Reviewed original state-bound `report.json`, `lesson.json`, slider values, camera records, raw PNG hashes, 32-module exact source receipts and **120 original cavity curves (20 per scene)**. These curves remain inside `R`, report physical-field direction (recomputed with independent Coulomb expression), end as `inner_surface_approached`, and explicitly disclaim particle trajectories/calibrated flux. Cutaway is disclosed as **rendering-only**, not a physical hole. Visual inspection does **not** independently certify real-time widget functionality or human teaching acceptance.

**Original release artifacts:** per OS **173** integrity inventories, **172** intact; **one intentionally corrupted negative** `derived-001/G1/review-challenge-resealed-native/native/integrity.json` per OS, with altered `result.json`, remains **EXPECTED NEGATIVE — NOT VALIDATED EVIDENCE**. Checked **1,749/1,750** referenced hashes each; only the deliberate negative was refused. Inspected **82** complete root-level maps of 32 source modules per OS (no claim of verifying all **105** repeated author-mentioned maps), **64** physics-demo reference checks, and Windows CRLF checkout receipt calculation in memory (no rewrites). Existing viewer archive provides nine original scenes/17 PNG receipts. The source ZIP/archive module hashes all matched candidate.

Original workflow logs, **not reviewer execution**, report both Ubuntu/Windows release **1,709 headless, 18 historical with one obsolete guard deselected, 37 real PyVista per OS**; [new lesson run 44245981629](https://github.com/physicsvigilante/emfeeld/actions/runs/44245981629) reports **71 focused** with six scene PNGs and four real graphics tests; [release run 44245981602](https://github.com/physicsvigilante/emfeeld/actions/runs/44245981602), [viewer run 44245981615](https://github.com/physicsvigilante/emfeeld/actions/runs/44245981615), and [source run 44245981717](https://github.com/physicsvigilante/emfeeld/actions/runs/44245981717) are author-qualified. These counts **overlap** and are not summed as independent product passes.

## Preserved reviewer first failures (do not recast as source failures)

1. Original fresh physics execution **39 pass / 3 fail**, `independent_first_run.log` and `test_independent_r2_initial.py` preserved. Two `a/R=.9` three-axis vectors rounded a floating-point ULP **above** the inclusive bound; generated just-admissible equivalent inputs instead. One incorrect reviewer negative-charge trace endpoint demand `<.01R` contradicted the documented illustrative `min(.025R,.08(R-a))` gap; corrected this assertion. **42 pass** on revised independent suite. The production slider has a rounding guard already.
2. First **and second** VTK reconstructions: **13 pass / 2 fail**, logs retained; three-axis offset still rounded above admissible `.9` even after one ULP adjustment. Adjusted test radius a few ULPs below bound; **15 pass**. No VTK arrow mesh entered metal in these executable cases.
3. First archive auditor failed **before audit** due to reviewer helper ordering (`NameError`); preserved file and log. Second failed because reviewer incorrectly assumed a grounded conductor has net conductor charge **zero**; actual induced net is `-q`; corrected the reviewer auditor. Third full archive audit **PASS** on untouched artifacts. Logs and intermediate auditors preserved.
4. Full `pytest -W error tests` **timed out** near 25%; incomplete log retained, **not** counted as a pass. Separate focused **67 passed**.
5. Author's earlier failed quadrature, eager slider initialization drift, camera test conversion, invisible/stale controls, clipped labels, mismatched test coordinate frames, and penetrating arrowheads are preserved in original author/CI history. The reviewer neither edited the source nor reclassified early callback-only runs as rendered/interactive acceptance.

## Findings / correction path

**R2-B01 — BLOCKING EVIDENCE GAP (not a demonstrated code defect).** Independently run pinned-head **real PyVista**: inspect initial model before setup callbacks; four visible/enabled widget representations in the right renderer and slider/model consistency; offset/theta/phi/stored-isolated-Q interactions; G/N/C/L controls and grounded/isolated-Q preset semantics; camera/cutaway invariance; direct `pv.Arrow` **actual mesh vertices** for both signs near the .9R wall; redraw with visible labels; fresh screenshot and `report.json`/arrays/current-`lesson.json`/original-input/camera hashes after widget movement; verify failed capture and protected roots. Retain raw screenshot images, first failures and results. Original author CI alone **cannot close this independent gate**.

**R2-N01 — optional numerical-authoring nuance.** A 3-axis vector intended to have norm exactly `.9` can be rejected when its computed binary norm lies slightly above `.9`. The actual slider normalizes around this; not a current physics defect. Consider revisiting only if real authored JEE inputs need tolerance policy, without allowing physical contact.

**Boundaries:** one fixed point charge, spherical concentric conductor, no exterior charges, bounded `a/R<=.9` and specified scale/charge/probe ranges; curves are illustrative field direction, not motion/flux; sampled surface density is not a general conductor/PDE solver. This review makes **no** claim of arbitrary conductor support, all textbook questions solved, human Windows approval, or actual-main post-merge release.

**Final verdict: INSUFFICIENT EVIDENCE.** Favorable independently executed physics/archival checks; independently executed live PyVista graphics/controls still missing. **Do not merge.**