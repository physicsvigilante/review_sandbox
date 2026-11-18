# PR #44 — JEE 3D conductor-cavity author qualification 01

**18 November 2026: author pre-merge qualification PASS; independent R2 review PENDING.** [PR #44](https://github.com/physicsvigilante/emfeeld/pull/44) remains **DRAFT / OPEN / UNMERGED**. This is a bounded JEE teaching lesson, not a general numerical conductor solver, a teacher acceptance verdict, or proof of all numerical domains. All counts below refer to actual completed executions and original files.

## Exact source and unchanged baseline

Candidate **`e253d0acf15e7505f1da8ab95cb519b59b0d720b`**, canonical tree **`8a4a14d70ba824e8a338add08356003e79a248bc`**. Base/main **`60b6e751363d0b922a02c3a259110547b79cf25c`** adds only the owner's theory PDF atop released PR40 `88324210`. Original CI preview **`04f8926ff15697ecccd9d89f71e837f2eb45bf56`** independently read from GitHub has identical candidate tree and ordered parents [base, candidate]. It is not a production merge.

**Nine added files, no modified/deleted baseline files; 382 tracked files, 32 package modules.** Existing analytic source laws, trajectory/event policies, solver tolerances, original PDFs and old workflow files are unchanged. New lesson physics and display live in separate opt-in modules. Actual source TAR was safely extracted and fresh-indexed to the exact candidate Git tree. Original source index and every locally tested byte matched. A supplied patch applied to a separate reconstructed base also reproduced this exact tree; patch SHA256 `d5eae4bf3d46f3781bc542d43529f8991ddeee6d6d3f197e1e84de94c60f8b7b`.

The two new package modules enlarge implementation receipts. Old implementation-pinned studies may legitimately refuse a changed inventory; preserve their original environment/receipts or replay unchanged inputs into new outputs. Do not reseal old evidence to force compatibility.

## Original theory reference and adaptation

Actually inspected `01_theory_elec.pdf`: original SHA256 **`dfed5a5cf241a365a2d94ebfeb73a9473aad66184d73af38be7fbfd81e6876ab`**, Git blob `e8bf45cb2bc8206be0681d5c5367d0943e8b6c95`, 140 pages. Exact source bytes were extracted from the original GitHub source archive, with text and relevant rendered pages inspected.

Printed **1.115** discusses conductor-cavity induced totals. Printed **1.117, question 5** concerns a central charge/thick shell; **question 7** asks for field-line sketches for a charge at R/2 inside a neutral **thin shell**. Printed **1.123–1.124** introduces images with grounded-plane examples. The current R=1m, B=1.25m, q=1nC view is an explicitly **illustrative thick-shell adaptation**, not an exact numerical reproduction of question 7. Spherical image/density expressions are separately derived implementation machinery, not attributed to those pages. No whole-PDF solved-corpus or blind-question claim.

## Bounded functionality

One held point charge in a concentric spherical vacuum cavity/conductor; no external charges. Cavity field comes from the exact spherical image construction only inside the cavity, metal field is zero, exterior field is separately determined by Q+q or zero when grounded. Potential references and one-sided surface fields are explicit. Centre and zero-charge limits are handled without an infinite virtual charge. V1 admits offset a/R<=0.9 and documented finite size/charge ranges; unsupported inputs are refused.

The PyVista scene is genuinely 3D and rotatable, with a display-only cutaway, sampled physical surface-density shading, actual field-direction curves, bounded arrow glyphs and charge-balance panel. Four sliders set offset, polar angle, azimuth and isolated-Q preset. Keyboard grounding/sign/cutaway/line controls choose static equilibria, not time-dependent redistribution or grounding history. No physical image charge is drawn. Cutaway never opens the physical conductor. Sampling/curve stepping does not calculate unknown surface charge and is not particle dynamics or calibrated flux.

Exact induced total -q stays distinct from an **unrenormalized sampled integral and its error**. Fresh snapshots retain current model, optional original input separately, camera/control settings, arrays, PNG receipts, implementation identities and explicit incomplete failure outcomes. Old sealed evidence is protected before writing/rendering.

## Completed exact-head tests and original workflows

| Execution | Actual result |
|---|---|
| Final local full headless, warnings as errors | **1,709 passed**, including 67 new headless cases |
| Final local historical behavioural replay | **18 passed; one obsolete all-file guard deselected** |
| Compilation and patch/tree reconstruction | PASS |
| Fresh Ubuntu and Windows release, run [44245981602](https://github.com/physicsvigilante/emfeeld/actions/runs/44245981602) | **Both SUCCESS; 1,709 headless +18 historical +37 real-PyVista passes per OS**, original logs checked |
| New lesson run [44245981629](https://github.com/physicsvigilante/emfeeld/actions/runs/44245981629) | **71 passed** (67 headless +4 real graphics), **six retained scene PNGs**, actual VTK interaction and control/geometry assertions |
| Existing viewer run [44245981615](https://github.com/physicsvigilante/emfeeld/actions/runs/44245981615) | SUCCESS; nine original offscreen cases, 17 PNG receipts, 1,709 headless |
| Source snapshot [44245981717](https://github.com/physicsvigilante/emfeeld/actions/runs/44245981717) | SUCCESS; exact 382-file tree reconstructed |

Counts overlap as stated; the 71 focused tests are not additional to the full product/viewer totals. Original V6 ten-case, discovery two-case and Physics Demonstration 17-observation/64-check replays passed. Local environment: Python3.13.5, NumPy2.3.5, SciPy1.17.0, pytest9.0.2. Dedicated hosted graphics used PyVista0.48.4/VTK9.6.2; OS native reports record NumPy2.5.5/SciPy1.18.1. Environments were observed, not assumed identical. Local PyVista was unavailable and isolated installation failed DNS; no local real-render or user-environment modification is claimed.

## Five ORIGINAL exact-head ZIPs downloaded and read-only audited

| Artifact | ID | Original whole-ZIP SHA256 | Entries |
|---|---:|---|---:|
| Source | 14401692570 | `33059d044eb2b8ce824ecd6c7b65e3e05033b2fd30ca1f77676cd2f8e0437367` | 4 |
| New lesson | 14402305972 | `6f3e8cb68c2624593c077edb15fe8ac4d0502eb0b47fc5d6e612a4277fc98c55` | 49 |
| Existing viewer | 14401798242 | `0ac15d5de6585251345dd637836e658c929ccc1e13d14fb9aa1e571ca015a1c2` | 22 |
| Ubuntu | 14402041927 | `5ae9758ebbd3b8995c300f57a5702d929900f13921d47b3bfb9c4ee9b7274f96` | 2,186 |
| Windows | 14402262223 | `895306335a7931b0c31d766526ca0f93c84a45e17dbb8af498d79938cf10bc65` | 2,186 |

Each whole ZIP matched original GitHub digest; all members were read/CRC/path/duplicate checked. Original source TAR SHA256 **`ffafd8907459cfc32e3408e66bccdd2aea89608b8639eb3d47ef92c5ef8396f5`** is identical in source, existing viewer and new lesson archives, and reconstructs the exact candidate. Original OS head-sha files correctly name the PR preview.

**New lesson:** six state-bound snapshots (off-centre, centre, grounded, negative, isolated charged, rotated full shell). Every original PNG hash and snapshot inventory matched; all32 source receipts matched the exact TAR. All stored curve coordinates stay in the cavity and their orientation was independently recomputed using a separate direct two-image Coulomb expression. Actual sliders agree with saved physical state/preset; quadrature errors are retained, not normalized away. All six original PNGs were visually inspected by the author: controls/labels visible, state text legible and field/charge changes appropriate. This is **author image inspection**, not independent R2 or human desktop acceptance. Dedicated new PNGs are from Linux; Windows separately runs the four actual viewer tests, not an asserted equivalent six-image collection.

**Both OS archives:** checked173 inventories/1,750 referenced hashes, exact membership, all32 modules in105 complete source maps (100 implementation/five engine; repeated maps are not independent runs). Windows CRLF checkout receipts are computed in memory, never rewritten. There are172 intact inventories and one deliberate corrupted child in `derived-001/G1/review-challenge-resealed-native/native/integrity.json`; its downstream unavailable/null refusal is verified and it is explicitly **EXPECTED_NEGATIVE_NOT_VALIDATED_EVIDENCE**, not counted intact. Existing gravity5/NASA1 native source/packet/report chains, Physics Demo17 values/64 checks and signed E1complete/G1partial comparisons remain correct. No original stored evidence was rewritten.

## Preserved first failures and corrections

The development history is retained, not recast as first-pass success. Initial96-node near-wall quadrature was under-resolved; refinement to256 satisfies the unchanged assertion without rescaling density. First real tests on3c8c0ff recorded68pass/2fail: initialization callbacks changed exact authored position, and a separate camera-test object conversion was wrong. The callback guard and numeric comparison fixed those issues.

Later callback tests passed but screenshots revealed invisible sliders, stale slider values and clipped labels; renderer-only clearing, explicit widget synchronization and correct viewport layout were added and tested. One new layout test initially compared different coordinate systems (69pass/1harness failure), then corrected its conversion without changing physics or margins. A final geometric probe found fixed-length arrow glyphs entering metal despite valid curve paths; bounded glyph size and half-arc-length placement now pass actual mesh-vertex checks at the maximum admitted offset for both signs. Earlier images/logs remain limited evidence, not complete visual acceptance.

The release-audit script was first invoked with incorrect argument flags and exited before auditing. Correct positional invocation subsequently passed on unchanged artifacts. No such harness mistake is called a product defect or a completed audit.

## Remaining gate

[Independent R2 request](REQUEST.md) requires fresh reviewer-owned numerical, source-reference, graphics/state and preservation challenges on this **exact candidate** and its original artifacts. Publish `reviews/review-01-chat-b.md` with an attributable verdict. **Do not merge before independent PASS and guarded integration.** Fresh actual-main workflows/new original archives will be required after a future merge. Human Windows usability, teacher usefulness, unseen independent JEE question and arbitrary conductor/scale correctness remain unqualified.