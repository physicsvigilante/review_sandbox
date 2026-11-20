# SIM_HEAT PR73 — targeted independent R2 correction review: PR72 N-01/N-02

**Decision requested:** SCOPED PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE. Assess only the two PR72 reviewer-identified hardenings to the SOURCE→PREEXISTING ARCHIVED DIAGNOSTIC presentation bridge and the minimal CI adaptation. No new physics, numerical solver, native execution or physical reference is proposed.

## Immutable review subject and lineage
- [DRAFT source PR73](https://github.com/physicsvigilante/sim_heat/pull/73), source **HEAD `ba625afe3223d4c0fda5d23b88445d08d64771c6`** on `teaching/t3-archived-diagnostic-hardening`, base branch `teaching/t2-source-archived-diagnostic-handoff` at **`617cfee3b91d7acf567ecad779f133b7429a8611`**.
- [Independent PR72 R2 review-01](../pr-72/reviews/review-01-chat-b.md) is **SCOPED PASS** at its unchanged exact HEAD, and records N-01 and N-02 as non-blocking improvements. Its original report and source commit remain untouched. PR71/70/69 and earlier stack remain DRAFT/UNMERGED.
- [GitHub comparison PR72→PR73](https://github.com/physicsvigilante/sim_heat/compare/617cfee3b91d7acf567ecad779f133b7429a8611...ba625afe3223d4c0fda5d23b88445d08d64771c6) shows exactly FOUR modified paths: `tools/published_diagnostic_bridge.py`, `tests/test_authoring_workbench.py`, `tests/browser_authoring_workbench.py`, `.github/workflows/teacher-archive-handoff-ci.yml`. No H1 model/study/grammar/physics, historical native-case JSON, original MAT/CSV/archive, reference, native runner or C1 source changes.

## N-01 — runtime byte-accurate published index gate
The PR72 runtime compared parsed Python `generated == published` structures for `viewer/network/data/compare_index.json`. The new runtime instead requires:
```python
generated = compile_pair_index(ROOT, SOURCE_MANIFEST, CASE_INDEX)
if stable_json(generated) != safe_file(PAIR_INDEX, ROOT):
    return {}, None
```
`stable_json` is the existing canonical archived compiler serializer, and the ORIGINAL published index is unchanged (SHA-256 `34f6abac6948fd5c70b3b91d13a72336c5d768ce235f0108f26c57731ef134c3`). This is additional fail-closed byte-integrity for an index within a trusted local source checkout; it is **not** external owner/GitHub provenance attestation.

The new unit regression feeds **byte-different but structurally equal** index JSON (`b' ' + original`) into the original in-root index read through a scratch patched `safe_file` function. It tests that the correct server-admitted D2→D2_K2 remains source-only, with a 404 historical viewer route and explicit no published diagnostic, without modifying any committed historical file. The test deliberately does **not** substitute a path outside `ROOT` (which would only exercise path containment).

## N-02 — exact recorded-sample HTTP Chromium regression
The hosted browser script opens the same original D2→D2_K2 archived native diagnostic as PR72. It now explicitly checks `#time-label == '468.75 s'` after one saved-step arrow key; `cold.T` at that time reads **296.468 K** versus **299.052 K** in the archived viewer's four-decimal display. Original full-precision archived case samples are `296.4679940381214` and `299.05204547674595` K; no new numerical result or interpolation is created. The signed initial rod flow +12 W / +24 W and `diagnostic_only/nativeQualified=false` remain inherited checks.

## CI and checks
- [PR73 hosted exact-source CI 44680586259](https://github.com/physicsvigilante/sim_heat/actions/runs/44680586259) is **SUCCESS**. Its real workflow job completed source/PR-parent check, unchanged PR71 nine-file lineage fence, full inherited Python/JS, published index byte parity, six original archived native-diagnostic **offline** replays, documentation parity and actual HTTP Chromium admission/handoff/route/browser refusal journeys.
- Exact test inventory: **152 H1 + 4 analytical + 63 native adapters (62 pass/one existing optional skip) + 61 product + 51 JS = 331 distinct collected; 330 PASS / 1 optional skip**. One extra product test is N-01; browser script exercised N-02. No fresh OpenModelica operation.
- GitHub-hosted PR artifact **14603669026**, workflow archive `teacher-archive-handoff-5894517a41ee528052fa4744e36d57b3721bca90`, GitHub-reported artifact ZIP SHA256 **`9c39229cc44f34604242f64df24838c2a5a7591d22b836e91c6037609f4926bd`**. Developer independently read job logs/API, but **did not download and personally rehash this artifact ZIP or open its screenshots**. Hosted log confirms actual Chromium steps. Never imply independently executed reviewer checks from hosted CI alone.
- The workflow source change adds this push branch and PR72 target branch to CI triggers and compares synthetic PR first parent to exact event base SHA and second parent to head SHA; its immutable PR71 baseline-nine-file fence and original-source-preservation check stay intact.

## Targeted reviewer challenges
1. Independently compare the FOUR path changes to exact PR72 HEAD. Test whether valid original canonical bytes keep the link, while semantic-equal but byte-different JSON loses the archived viewer ONLY, not original admitted source preview. Challenge hidden fallbacks, import/browser hash forgery or changed original archived cases.
2. Verify the negative unit test would *fail* against the OLD parsed-equality code, and that patched read actually exercises in-root index bytes rather than `safe_file` path confinement.
3. Check exact recorded original `468.75 s`, `cold.T` values, rounding and the existing signed initial flows. Ensure chart shows already recorded samples without relabeling them as new computations.
4. Inspect PR73 GitHub Actions log and the four-file scope. Attribute independent actions, developer observations and CI correctly; flag any proof gap (e.g. unopened artifact ZIP) without assuming missing screenshots are a demonstrated failure.
5. Confirm the inherited refusal guarantees, original `diagnostic_only/nativeQualified=false`, source-relative authenticity warning, unresolved **seven static 100× physical-reference failures**, **eight native blockers** and lost private scorer stay as before.

**Output:** ONE NEW Chat B authored `physicsvigilante/review_sandbox/projects/sim_heat/pr-73/reviews/review-01-chat-b.md`, with an exact-SHA SCOPED PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE verdict. No source edits or historical record edits by Chat B. Keep all source PRs DRAFT/UNMERGED. No OpenModelica version/install/query/build/launch, native reference promotion or deployment.
