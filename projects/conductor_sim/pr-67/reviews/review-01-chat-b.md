# Chat B independent R2 review — conductor_sim PR #67, M29a

- **Project/source:** [physicsvigilante/conductor_sim](https://github.com/physicsvigilante/conductor_sim)
- **Source PR:** [#67](https://github.com/physicsvigilante/conductor_sim/pull/67), draft/unmerged at review; base/main `61f059f742b449ea53fdc131970f00f0b3be91fc`.
- **Exactly reviewed head SHA:** `32f11b931548dcc5c5f6fd836da8239a265de187`.
- **Verified Git tree:** `28fd4cbca302593c1d0bdd37d26476b546e274c1`.
- **Reviewer:** Chat B, independent separate-context ChatGPT GPT-6; 2026-11-16 (UTC+05:30).
- **Scope/risk:** R2 independent assessment of new M29a cross-inventory structural families, native numerical trajectories, evidentiary identity, censoring and teacher viewer. The source root tree contains **no root AGENTS.md**. Read central REQUEST, PROTOCOL, REVIEW-RISK-POLICY, REVIEW-TEMPLATE and pinned M29a charter, M29a/M22a docs and new source/tests/browser files.
- **Source files changed during review:** None. All tests were carried out against a locally extracted CI source archive; only separate scratch tests/results were created.
- **OUTCOME: CHANGES-REQUESTED** (teacher-facing acceptance deficiencies; independently tested physical/numerical core PASSED). Retain source PR draft until the two viewer issues are corrected and targeted review passes.

## Reproducibility, evidence provenance and first-attempt history

Live PR HEAD and exact Git commit tree were checked directly through GitHub. Downloaded genuine visualization workflow artifact `14227797439` from run [43870161157](https://github.com/physicsvigilante/conductor_sim/actions/runs/43870161157), **independently SHA-256-hashed** downloaded 58,819,667-byte ZIP to `557e891e51615b60b852057f539e6ee7e6f22de96a4ee939fcb051fb14f24623` (matches GitHub-reported digest). Extracted its nested `source.zip` into a local directory, staged source files using git without edits, and **independently reconstructed Git tree `28fd4cbca302593c1d0bdd37d26476b546e274c1`**, exactly matching the pinned tree. Outer `commit.txt` contains `5550047b02f3cdc3987a8c0b990f0195906de0a0`, the synthetic PR test-merge, not the source HEAD; source tree identity, not that file, anchors the review.

Separately read GitHub's completed exact-head jobs: [Python run 43870161439](https://github.com/physicsvigilante/conductor_sim/actions/runs/43870161439), Python 3.10 and 3.12 success; [FEMM 43870161236](https://github.com/physicsvigilante/conductor_sim/actions/runs/43870161236), success; and [Chromium 43870161157](https://github.com/physicsvigilante/conductor_sim/actions/runs/43870161157), success. The artifact's actual `python.xml` contains 1,848 tests, 0 failures, 0 errors, 0 skips for the non-FEMM visualization job. The request documents 1,848 passes with 97 FEMM-only skips per separate Python-matrix interpreter and 97 passes in the FEMM job. These CI results are **read/inspected CI**, not reruns by this reviewer. The separate `43870147134` push-run also reports successful exact-head Python checks. The 15 completed PR-associated workflow runs plus that push run are consistent with the request's 16/16 success count.

Historical failures remain acknowledged: head `388d7b1cc71065c51e73e8e53d58645ab00feecb` Python run [43869414266](https://github.com/physicsvigilante/conductor_sim/actions/runs/43869414266) failed; next head `ae0dd716602d9b0d5dd51eb496b258e473557e03` visualization run [43869621323](https://github.com/physicsvigilante/conductor_sim/actions/runs/43869621323) failed its Python test phase due a custom-title expectation. Neither is recast as first-run success; final head passed.

## Findings

### F-01 — MAJOR, teacher-facing source membership/provenance — source names silently omitted from displayed inventory

**Source:** [`src/conductor_sim/structural_family_viewer.py` lines 24–28, 213–215](https://github.com/physicsvigilante/conductor_sim/blob/32f11b931548dcc5c5f6fd836da8239a265de187/src/conductor_sim/structural_family_viewer.py#L213-L215). The trusted embedded track data correctly stores `{id,label,kind}`, but the actual table writes `s.id+' ('+s.kind+')'` and **never displays `s.label`**. The requirements explicitly call for physical source membership **ID/type/name** and per-source teacher-facing provenance; the actual user interface omits the authored name. The [browser test lines 51–55](https://github.com/physicsvigilante/conductor_sim/blob/32f11b931548dcc5c5f6fd836da8239a265de187/tools/check_m29a_browser.py#L51-L55) checks names in embedded JSON but fails to assert their visibility.

**Reproduction:** New native assembly baseline includes source `rod:rotated` with label `Tilted finite positive rod`, and signed sources `point:A` / `point:B`. In real Chromium 144 at 390px, embedded JSON retains all labels; visible membership table contains only `rod:rotated (UniformRodField)`, etc. Archived real CI `guard-and-refusal.html` similarly omits label `Teacher neutral reference field`. Hostile source label `<img src=x onerror=alert(1)>` is preserved in JSON and inert but absent from that membership cell. **Observed directly**, not a hypothesis. This is not a physical integration defect.

**Required correction:** Display escaped/textContent-rendered source `id`, `kind`, and `label` in the teacher-facing inventory (including correct replacement and original cases). Add a real Chromium assertion that two intentionally distinct source labels are visible as literal text, including one escaped hostile label. Preserve no-script-injection behavior.

### F-02 — MINOR (but release-facing 390px usability), compressed numerical table is technically overflow-free yet materially hard to read

**Source:** [`src/conductor_sim/structural_family_viewer.py` lines 137–148, 168–172](https://github.com/physicsvigilante/conductor_sim/blob/32f11b931548dcc5c5f6fd836da8239a265de187/src/conductor_sim/structural_family_viewer.py#L137-L172). The 5-column full-width table uses `overflow-wrap:anywhere` throughout, while the wrapping `.scroll` region is never given a min-width table. At an actual 390px Chromium viewport, columns measure approximately **68.9, 78.0, 43.7, 101.1, 56.3px**; long IDs, ledger text and 3D `Δr/Δv` values break across many lines and results are difficult to scan. Document width is correctly 390px, SVG width 348px, with no horizontal *document* overflow; therefore the current automated mobile check passes without measuring usability.

**Reproduction:** Open reviewer-generated `novel.html` at 390px, inspect table and dimensions; same layout applies to archived M29a pages. Screenshot examined. **Observed usability deficiency**, not an invented physics failure or violation of the explicit no-document-overflow width metric.

**Recommended bounded correction before teacher-facing acceptance:** Give the inner table sensible readable minimum column widths with a confined horizontal-scroll area, or use stacked per-model mobile cards. Keep outer document width <=390px; add readable-width/scroll usability assertion and visually inspect at 390px. No ODE or underlying source logic changes required.

## Independently executed unfamiliar physical assembly and numerical reference

A genuinely new authoring case was constructed **outside the source tree** using the verified source archive. All physical coordinates are SI metres, q in coulombs, mass in kg and gravity in m/s².

- Original fixed sources: tilted finite rod charge **+1.6 nC** from `(-.20,-.10,0)` to `(-.12,.14,0)`; held `point:A` **+1.2 nC** at `(.18,-.07,0)`; held `point:B` **-0.6 nC** at `(-.06,-.18,0)`. Named source IDs `rod:rotated`, `point:A`, `point:B`, distinct labels.
- Test charge **+0.9 nC**, mass **2e-5 kg**, initial `r=(.025,.045,0)`, `v=(.04,.015,0)`, certified plane normal `(0,0,1)`, duration **0.08 s**, samples every **0.01 s**, source guard **0.006 m**, length scale **0.5 m**.
- New sibling A: add +0.8 nC fixed `point:C` at `(.26,.19,0)` AND separate real uniform gravity `g=(0,-.9,0)`, atomically.
- New sibling B: remove `point:B` entirely.
- New sibling C: retire `point:A`, replace with `field:replacement` uniform electric field `E=(6,0,0) V/m`, new source identity.
- Invalid sibling D: add lone +0.7 nC point at `(.10,.10,.065)` without a mirror; expect whole-model refusal.

**Actual source outcomes:** baseline duration complete; siblings A/B/C all `complete`, exactly 9 saved states each; sibling D `rejected-structural-model` with native `UnsupportedProblem: fixed point-source inventory is not reflection symmetric`, **no assembly/trajectory**, and A/B/C unaffected. Immutable baseline record and revision SHA `4c713156f54601840be1031d60880a40ec98f6beeb06d73c41cc505c30a78c23` unchanged before/after. All real siblings' `ScenarioReassembly.parent is baseline` and their serialized `parent_revision_id` equals original revision. Retained, retired and new IDs, slot order, gravity membership, add/remove/replace ledgers and detached provenance were asserted. No child reused a retired ID. All observed comparison rows have exact shared saved SI timestamps and full world **3D** position/velocity differences; rejected sibling has none.

**Independent reference (not another call to native field or integrator):** separately implemented direct signed point Coulomb sum, tilted finite-rod Coulomb line integral by **200-node Gauss–Legendre quadrature**, independent vacuum constant `epsilon0=8.8541878128e-12 F/m`, plus explicit Newtonian gravitational acceleration for A, and integrated own six-state ODE with **SciPy DOP853** `rtol=1e-12, atol=1e-13` at the identical physical times. No conductor source solver, M29a field evaluator or native RK used in reference. A comparison of 64/128/200/400/800-node direct rod quadrature at initial position also converged to identical displayed field components.

| Run | Native terminal r=(x,y,z) m | Native terminal v=(vx,vy,vz) m/s | Max component pos discrepancy m | Max component velocity discrepancy m/s |
| --- | --- | --- | ---: | ---: |
| Baseline | (0.028214358718233374, 0.04621262520236765, 0) | (0.040351123734046646, 0.015322395826786218, 0) | 8.92e-16 | 3.33e-16 |
| Add point C + gravity | (0.028202553533152937, 0.04332528907219372, 0) | (0.04005080930747102, -0.05686525895743048, 0) | 1.75e-14 | 3.62e-13 |
| Remove point B | (0.028219117106498607, 0.04622508756401379, 0) | (0.04047026175465881, 0.015632782628051956, 0) | 8.29e-16 | 2.78e-16 |
| Replace point A with new field | (0.028248791630110216, 0.046187453998164006, 0) | (0.04121294621945888, 0.014688960491808668, 0) | 5.17e-16 | 3.19e-16 |

**Explicit thresholds:** max `|Δr_component|<1e-8 m`; max `|Δv_component|<1e-6 m/s`; initial `|Δa_component|<1e-7 m/s²`. All passed, with observed maximum initial acceleration discrepancy **2.17e-17 m/s²**. This tests a new composite geometry and new physical source-inventory change, not simply re-running the developer's four examples. It does not establish universal 3D dynamics or conductor induction.

## Native guard, historical tests and real Chromium independently run

- Ran `pytest -q tests/test_m29a_structural_family.py` locally on the exact extracted Git-tree source: **8 passed**, one ordinary PytestCollectionWarning about a dataclass whose name starts with `Test`. Python 3.13.5 for local reviewer tests; this is not a replay of Python 3.10/3.12 matrix.
- Independently executed archived `guard-and-refusal` through exact source. Censored child's true terminal source-guard time **0.19489773173431751 s** is *not* a baseline-grid time. It has **20** literal shared comparison states ending at **0.19 s**, none after guard; baseline and distant-source sibling terminate at **0.25 s**. The other sibling is unqualified and has no native trajectory. Browser's last saved frame shows 2 active and 2 unavailable models; censored marker hidden. No false duration or phantom state.
- Opened both independently generated `novel.html` and archived `guard-and-refusal.html` in actual **Chromium 144** at 390px using Playwright. Both showed `viewport=390px, document=390px, SVG=348px`; native time slider final states and missing-marker semantics checked. No console/page/network errors observed. Visual screenshot independently examined. Confirmed names absent from rendered source cells and cramped table widths.
- New adversarial browser probe: original source label `<img src=x onerror=alert(1)>`, newly added source label `<svg onload=window.pwned=true>`, and hostile teacher provenance `<img...></script><script>window.pwned=true</script>`. Label values remain in embedded JSON, but there is no created hostile DOM element, no `window.pwned` execution and no script/page/network error. Arbitrary `as_dict()` passed to renderer is refused by `type(run) is StructuralFamilyRun` (direct source + existing test). A first adversarial setup tried an over-48-character label and was rightly rejected by pre-existing label length validation; the corrected short-label test passed.
- Native detached JSON and browser do not assert cross-inventory `ΔU` as work, and page clearly identifies the particle trajectory plot as trajectory space, not source apparatus. Source labels are author assertions; no workbook Q40–41 replication is claimed.
- The source module `structural_family.py` calls unchanged M22a `reassemble_scenario` for each sibling, and unchanged `integrate_test_charge` for original and admitted children. Existing `_shared_rows` uses literal time-key lookup and whole-world coordinate differences; independently checked on the guard case. No observed change to native physical solver law, event guard or browser-side numerical integration.

Reviewer scratch evidence created locally only: `novel_reference.py`, `novel-results.json`, `novel-native.json`, `novel.html`, `browser_review.py`, `browser-review-results.json`, two 390px screenshots; not committed to either repository. The pinned archive and CI links are public reproducibility anchors.

## Separate judgments

| Dimension | Judgment | Basis |
| --- | --- | --- |
| Source interpretation fidelity | **PASS within hypothetical scope** | Actual source membership, types, charges and SI geometry checked in native models; no workbook attribution; static prescribed sources, not metal induction |
| Physical/numerical correctness | **PASS for tested scope** | Novel multi-source tilted rod/points/gravity composition matched truly independent Coulomb quadrature+DOP853; certified off-plane refusal; no wrong 3D vectors found |
| Native simulation and observable coverage | **PASS for tested scope** | Baseline + three fresh sibling integrations; real duration vs guard vs refusal; literal-time 3D comparisons; focused 8 tests pass |
| Evidence integrity/provenance | **PASS for reviewed source and native records; UI display condition** | Independent artifact SHA-256 and Git tree, source IDs/lineage revisions and author-origin semantics; display omits source labels (F-01) |
| Teacher-facing usefulness | **CHANGES REQUIRED** | Source labels missing (F-01); 390px five-column table barely readable (F-02), notwithstanding correct outer responsive width |
| Textbook-answer completeness | **Not applicable** | These are explicit teacher hypotheticals, not exercise Q40–41 reproductions |

## Release advice

**CHANGES-REQUESTED** for the bounded viewer corrections F-01 and F-02, **not** for any demonstrated core physics or solver failure. The most important missing acceptance is actual name/label visibility. Keep the source PR draft, correct source label rendering via textContent and add a browser assertion, improve narrow-screen per-case readability while preserving no horizontal document overflow, rerun current-head focused browser + applicable Python CI, and request **targeted** Chat B re-review for those changes. Do not weaken time alignment, admissibility or no-browser-ODE rules. If fixes affect physics/evidence semantics, escalate accordingly; otherwise another broad R2 native review is unnecessary. Prior exact-head physical pass remains evidence for the reviewed SHA only. No source merge or change to source PR was made.