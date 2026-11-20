# EMFEELD PR #63 — independent scoped scientific + artifact review (Chat B, review 01)

**Verdict: CHANGES REQUESTED.** The on-axis formula, numerical outputs and currently hosted screenshots are substantially supported. However, source/provenance binding is not enforced by the public snapshot API (F1), and an explicitly resolved off-axis point can be accepted as on-axis under the current tolerance (F2). This is **not** an independent native-PyVista acceptance or merge authorization. Review date: 2026-11-20.

## Pinned source and candidate identity

- PR: https://github.com/physicsvigilante/emfeeld/pull/63 (draft, unmerged at review).
- Feature HEAD: `b2e19bad89bc70fdae7602478c55cc4002f64bf2`.
- Feature Git tree: `84b8b33364cd8b700984d0c51a15b7df1539c7d2`.
- Main/base: `52aecd34338662e269fba091c0ff6664e8e1eca7`, tree `047eca847cfc6bacfc3afebd51cf912a2f9deb18`.
- Synthetic GitHub PR merge: `6ab145376b198a21375f5ed976ac1b98821eaedf`, parents **base, HEAD** in that order, tree exactly `84b8b33364cd8b700984d0c51a15b7df1539c7d2`. The synthetic merge is **not** merged main.
- GitHub PR change list contains exactly nine **added** files; no existing baseline files modified. The feature HEAD was rechecked just before publication.

## Independent evidence actually performed

1. Downloaded the original current-head native loop artifact **14603906976** from run https://github.com/physicsvigilante/emfeeld/actions/runs/44678141388. Independently SHA-256 hashed the original 79-member ZIP: `ec704ab083d3fdeb7792c103c1846ecbfaf36bfc2888274ab870fc6c510851c4`. ZIP CRC passed.
2. Extracted the original source TAR **from the artifact**; its SHA-256 is `83bd189fe15ed62305b8a415b1636f202c2c413634957ccd4ee86ad732d229c2`. Independently reconstructed the Git tree from **461 original tracked file bytes and modes** (SHA-1 Git blob/tree construction), yielding exactly `84b8b33364cd8b700984d0c51a15b7df1539c7d2`.
3. Rehashed **63/63** per-scene declared file hashes in all nine original scenes. Verified each source input against its authored state, source-input SHA-256, reported current state, and the three module source-code SHA-256 values. These **particular hosted receipts are internally consistent**; F1 below concerns the API's missing enforcement, not a discovered alteration of these originals.
4. Independently recomputed all nine scenes' centre/probe signed SI fields and xyz vectors (36 scalar/vector comparisons), and checked each scene's NPZ field vectors, physical ring radius/plane/centre, dimensionless rendered radius, probe coordinate, signed arrow data, and reports. No disagreement found.
5. Ran **reviewer-authored**, separate Python tests against the reconstructed exact candidate source: 700 randomized admissible translated and rotated models with fields, frame handedness, geometry, reversal and immutable-array checks; scaling metamorphisms at fixed z/R and fixed SI z; 17 malformed/domain JSON refusals; Boolean/object/NumPy Cartesian probe refusals. Four independent pytest functions passed; two independent contract-challenge tests failed (F1, F2). The author's own 22 pure magnetic tests also passed locally but are **not classified as independent**.
6. Independently inspected the nine original actual rendered PNGs (including zero, negative current, doubled radius, offset probe, rotated normal). Measured long **green and dark-blue horizontal slider rails separately in the right lower pane** in all nine original screenshots, rather than only counting arbitrary dark pixels that could be text. Visually confirmed ring size, green/orange arrow reversal, the fixed blue normal, and omission of orange/green arrows at zero current.
7. Independently fetched the specified ten exact-current-head GitHub workflow statuses. All completed successfully, including dedicated loop/source/general viewer, Windows-2022 and Ubuntu-24.04 full-suite jobs, straight wire, Gauss, cavity, dipole, capacitor and browser. These are **author/CI results**, not new reviewer native execution.

Scientific reference: for I=+5 A, R=0.20 m, the exact B·u at z=(0,+R,-R,3R) is respectively **(+15.7079632659, +5.55360367196, +5.55360367196, +0.496729413224) μT**, using the repository's stated SI mu0. Reversal changes all signs; z sign alone does not. Doubled R gives one-half at the centre and at fixed z/R, not generally at fixed nonzero SI z.

## Findings

### F1 — BLOCKER: snapshot can declare an unrelated original input as source-bound

**Location:** `src/emfeeld/circular_loop_view.py`, `save_snapshot()`, at the `source_bytes` selection and `authored-input.json` / `report.json` writes (approximately lines 307–340).

The raw input bytes are SHA-256 hashed and saved, but are never parsed and compared to the provided validated `authored` state. A caller may supply a completely valid lesson JSON describing **-5 A** and pass a validated `authored` state describing **+5 A**. `save_snapshot` returns a completed receipt with `authored_state.current_A=+5`, `physics.current_A=+5`, an authentic SHA-256 of the contradictory -5 A raw JSON, and a valid integrity manifest. It also accepts invalid raw JSON similarly. This directly violates the requested source-bound evidence contract; hash correctness alone does not establish semantic association.

**Reviewer reproduction (no PyVista needed):**

~~~python
import json, tempfile
from pathlib import Path
from emfeeld.circular_loop_magnetism import CircularLoopState
from emfeeld.circular_loop_view import save_snapshot

plus = CircularLoopState(current_A=5)
minus = CircularLoopState(current_A=-5)
raw = json.dumps(minus.to_dict()).encode()
with tempfile.TemporaryDirectory() as d:
    path = Path(d) / "contradictory"
    save_snapshot(plus, path, source_bytes=raw)  # incorrectly succeeds
    assert json.loads((path/"outcome.json").read_text())["completed"]
    assert json.loads((path/"authored-input.json").read_text())["current_A"] == -5
    assert json.loads((path/"report.json").read_text())["physics"]["current_A"] == 5
~~~

**Required correction:** before writing a successful receipt, strictly parse source bytes using the same duplicate/unknown/nonfinite/domain rules as `load_lesson`; require their normalized state to equal `authored`. For `lesson is not None`, require `lesson.initial == authored` too. Preserve the exact raw input bytes in the receipt. Add tests both for valid-but-contradictory JSON and malformed JSON; both must refuse without a `completed=true` outcome. Keep the existing exact original source artifact and evidence unchanged.

### F2 — bounded but real axis-domain violation: nonzero resolved transverse displacement accepted

**Location:** `src/emfeeld/circular_loop_magnetism.py`, `field_at_point()`, at approximately lines 199–205.

For `centre_m=(100,0,0)`, `normal_direction=(0,0,1)`, the Cartesian point `(100+1e-13,0,0)` is **representably different** from the loop axis: actual transverse displacement `9.947598300641403e-14 m` (seven float64 ULPs at 100 m). Nevertheless, `field_at_point` returns a nonzero axial field instead of refusing it. Its current `64*eps*(|point|+|centre|+|displacement|)` tolerance is `2.842170943040404e-12 m` for this case.

~~~python
from emfeeld.circular_loop_magnetism import CircularLoopState, field_at_point
s = CircularLoopState(centre_m=(100,0,0), normal_direction=(0,0,1), current_A=4)
field_at_point(s, (100+1e-13, 0, 0))  # returns [0, 0, 1.25663706127e-05] T
~~~

Physical significance at this microscopic offset is negligible, but the **strict off-axis refusal** promise is stronger than “nearly on-axis within tolerance”. Either tighten the admissibility rule (e.g. reject resolved transverse offsets in the axis-aligned case while continuing to tolerate only necessary rotation arithmetic noise) or explicitly contract/document a quantitatively bounded approximate-axis input region, and test both construction-induced roundoff and independently supplied off-axis offsets. Never label that region as an off-axis solver.

## Native-render acceptance boundary (not independently completed)

The original nine CI-hosted PyVista PNGs genuinely show both slider rails and coherent observable graphics, and the archived source contains native VTK event handlers and tests. **I did not create a fresh reviewer-owned PyVista PNG or independently execute real VTK KeyPressEvent/EndInteractionEvent**: this review runtime has VTK 9.6.2 but lacks PyVista, and external package installation was unavailable. Therefore I cannot award the prompt's required complete *native* acceptance. Screenshot analysis of CI originals is not a substitute for new native execution. Do not reclassify the superseded prior screenshots or author event tests as reviewer-owned.

## Recommendation / re-review criteria

**CHANGES REQUESTED** for F1; resolve F2 with a precise numerical acceptance boundary, or a documented bounded concession explicitly approved by the owner before claiming strict axis-only refusal. On a new pinned source identity, run the two reviewer counterexamples as negative regression tests; recheck normal rotation, signs, scales, storage provenance, and visible controls; then obtain at least one **new, reviewer-owned actual PyVista screenshot**, with both native slider end events and native key events observed in that same independent environment. Revalidate original ZIP/TAR hash/tree identity and the exact-head dual-OS gates after changes. No production code modified, no existing review overwritten, no merge authorized, no claim of general off-axis Biot–Savart capability or classroom effectiveness.
