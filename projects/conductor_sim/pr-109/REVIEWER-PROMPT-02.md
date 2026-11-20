# JEE-12 PR #109 — independent review #02: close only source-access/native-execution blockers

**AUTHOR'S REVIEW REQUEST, NOT AN INDEPENDENT VERDICT OR MERGE APPROVAL.** The first independent review is published in [review_sandbox PR #29](https://github.com/physicsvigilante/review_sandbox/pull/29), with [review #01 findings](https://github.com/physicsvigilante/review_sandbox/blob/review/conductor-pr109-chat-b-20261120/projects/conductor_sim/pr-109/reviews/review-01-chat-b.md): **CHANGES REQUESTED** because B1 and B2 could not be verified in its restricted execution environment. It found **no demonstrated production-physics regression**. This is a deliberately *narrow* evidence-closure review, not another M40a/M40b/FEMM or full JEE-12 redo.

## Immutable target and release boundary

Production [conductor_sim PR #109](https://github.com/physicsvigilante/conductor_sim/pull/109) HEAD **`975e2e23a86fe29bbaafebc20e684312d2aa5b6d`**, Git tree **`ddcc0b9923584495f78e2ea05a7f1ff56622e8d2`**, based on released main **`337001f2e0d1ce62c87fa4352993c4a074cfbde6`**. Reconfirm live head/tree and that PR remains draft/unmerged; if either source identity moves, stop and request new pinning. At review #01: **21/21 successful head workflow runs and 24/24 head checks**, already validated there. The 12 frozen source cases remain **zero newly independently certified full original answers**, pending source-page/native evidence. Source PDFs and released solvers must remain unchanged.

## B1 — inspect and hash the *real* source PDFs, not textual summaries

You need actual original binary PDFs:
- `02_conductors_half_size.pdf`, SHA-256 **`9dff3c02a9f1848d2c3d99cb1a6e7a44dc7f5a51f7a3a2b8cc92d10ce1fbca5d`**.
- `POTENTIAL_CONDUCTORS1.pdf`, SHA-256 **`8d0d9b5cf821219058cfc4b7685a39b777e460944df44c3f9cffcb68157a60e5`**.

If your conversation/file tools cannot fetch ~21 MB / ~9 MB binary GitHub files, **use an independently authored GitHub Actions workflow in your review_sandbox branch**. A hosted Ubuntu job can use `actions/checkout@v4` with `repository: physicsvigilante/conductor_sim`, `ref: 975e2e23a86fe29bbaafebc20e684312d2aa5b6d`, `path: conductor_sim`. Have it assert `git rev-parse HEAD` and `git rev-parse HEAD^{tree}`, run `sha256sum` over **actual PDF bytes**, use Poppler or a verified PDF renderer to save legible page-specific PNGs into a retained workflow artifact, and record page indices/figure anchors. You must **personally inspect** those actual rendered pages, not just the workflow's claimed success; if necessary download the image artifact and open the images. Do not upload whole PDFs or 12 full-resolution pages to a public issue unnecessarily.

Inspect all **12 actual source-page anchors** and their figures/options, treating PDF page index and printed page label distinctly:
- Workbook printed/PDF pages **1 Q8**, **2 Q19**, **3 Q27**, **7 Q13**, **8 Q21**, **11 Q28**, **12 Q40**, **16 archive Q1**;
- Notes pages **26 Illustration 1**, **27 Illustration 4**, **69 Illustration 7**, **70 Illustration 9** (and distinguish Illustration 8).

Independently check signs, geometry, wording, original-versus-teacher inputs and printed answer choices against `docs/jee12_evaluation_cohort.json`; record a compact source-page/option checklist with actual inspected evidence. Do not promote a workbook exercise/teaching-note illustration to an official JEE examination item. Source p11 really has an **exterior point q**; p70's 2D shapes do not uniquely establish all 3D boundaries. Actual source p26 is a **solid** conductor, not a shell.

## B2 — execute released native APIs independently

In the **same reviewer-owned hosted checkout** (or true local checkout) install the package and narrowly required tests, e.g. `python -m pip install -e . pytest`. Write your **own independent native-replay code** importing actual released engine APIs; do not treat `tools/jee12_*_probe.py` / existing authored test files or stored CI JSON as your independent oracle. Store executable scripts, stdout/pytest logs, source head/tree, and enough native witness values in reviewer-owned artifacts.

At minimum demonstrate:
- Workbook p1: public `PrescribedField`/`endpoint_field_work`, external **+40 eV** vs field **-40 eV**, no simulated free trajectory;
- p2: actual M36b electron stopping event under **one-sided metal** `|sigma|/epsilon0`, distance **0.442709 mm**, teacher 1 mm clearance not a printed given;
- p3: actual released M36c **solid sphere + shell** static before/after field energies, release about **8.98755 J**, no invented time/current waveform;
- representative p8 grounded sphere source-prescribed current, notes p26 true solid sphere potentials, p27 two concentric thin-shell original values versus finite-thickness teacher values, p69 spherical teacher cavity center/off-center signed sigma and whole-face totals;
- p11 external-charge/irregular local sigma **refusal**, p70 underdetermined 3D original versus qualified spherical teacher variant; no claim of unrestricted E/V.

Use at least **three unfamiliar signed/translated physical teacher variations** that your reviewer code actually executes through relevant native released interfaces, checking against independently derived SI equations. Existing [review #01 arithmetic and Chromium evidence](https://github.com/physicsvigilante/review_sandbox/pull/29) can be cited for already validated mathematics and JS-on presentation; it is not a substitute for your own required B1/B2 execution.

If any hosted workflow is red, preserve initial logs, distinguish setup from scientific failure, repair only the evidence harness when appropriate, rerun exact review branch and report all failures. No need to rerun full 21-production-workflow matrix unless production source moved.

## Advisory findings and verdict

Review #01 additionally noted **F3**: inherited p26/p27/p2 offline viewer loses diagrams/results in JS-disabled mobile mode without adequate notice; **F4**: existing p26 title should say notes/illustration, not imply an official JEE original examination. These are real *existing-viewer* advisories rather than a demonstrated regression introduced by evidence-only PR #109. Keep them explicit; the inherited p2/p26/p27 viewer fixes are tracked separately in [issue #111](https://github.com/physicsvigilante/conductor_sim/issues/111); new p1/p3 walkthroughs remain scoped in [issue #110](https://github.com/physicsvigilante/conductor_sim/issues/110) with a clear no-JS fallback/notice and source labeling. Do not claim F3/F4 fixed or silently waive a defined release requirement.

Publish **review #02 report and a true reproducer** on a reviewer-owned `review_sandbox` branch/PR in `projects/conductor_sim/pr-109/reviews/review-02-chat-b.md` (or equivalent with reviewer attribution), containing B1/B2 raw-hash and actual page-inspection evidence, independently run native logs, exact HEAD/TREE, first failed attempts if any, and final **PASS** or **CHANGES REQUESTED** with scoped caveats. A PASS is only appropriate if **both** B1 and B2 close; source-specific errors must be reported and corrected rather than explained away. No production writes or merges by the reviewer.

**Release restriction:** PR #109 stays DRAFT/UNMERGED until independent PASS and separate explicit owner approval, guarded merge at exactly the reviewed commit, exact reviewed Git tree on main, and actual successful postmerge CI. Independently reviewed M40c PR #105 remains a *separate* DRAFT/UNMERGED owner-approval gate.