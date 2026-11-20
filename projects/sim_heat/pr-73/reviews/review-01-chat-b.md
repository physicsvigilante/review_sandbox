# SIM_HEAT PR #73 — independent Chat B R2 review-01

**Verdict: SCOPED PASS** — for the bounded PR72 N-01/N-02 hardening and minimal CI adaptation at exact source HEAD **`ba625afe3223d4c0fda5d23b88445d08d64771c6`**, whole Git tree **`4db8dc5e6b054eb4479bca26960e7f49f17c9395`** (20 November 2026). **No blocking defect identified within this review scope.** This is not an approval of new numerical results, native/OpenModelica qualification, physical reference adoption, merging, or deployment.

## 1. Review identity, parent and four-file boundary

I read this PR's [REQUEST](../REQUEST.md), [REVIEWER-PROMPT-01](../REVIEWER-PROMPT-01.md), and the **original** [PR72 independent Chat B review](../../pr-72/reviews/review-01-chat-b.md). I independently fetched [PR73](https://github.com/physicsvigilante/sim_heat/pull/73), the [pinned source commit](https://github.com/physicsvigilante/sim_heat/commit/ba625afe3223d4c0fda5d23b88445d08d64771c6), the PR72 base metadata and the [exact PR72→PR73 comparison](https://github.com/physicsvigilante/sim_heat/compare/617cfee3b91d7acf567ecad779f133b7429a8611...ba625afe3223d4c0fda5d23b88445d08d64771c6). The latter has **five candidate commits but exactly four changed paths** relative to reviewed, unmodified PR72 HEAD `617cfee3b91d7acf567ecad779f133b7429a8611`:

| File | Independently inspected change |
| --- | --- |
| `tools/published_diagnostic_bridge.py` | Runtime canonical compiler output compared to **raw published index bytes** rather than parsed JSON structures |
| `tests/test_authoring_workbench.py` | Valid semantic-equal/byte-different JSON injection into the **actual in-root read**, and source-only/404 refusal assertions |
| `tests/browser_authoring_workbench.py` | Exact next common saved time and both archived `cold.T` display values |
| `.github/workflows/teacher-archive-handoff-ci.yml` | PR73 branch/target trigger coverage and synthetic PR checkout parent checks against event base/head SHAs |

The [hosted PR synthetic merge commit](https://github.com/physicsvigilante/sim_heat/commit/5894517a41ee528052fa4744e36d57b3721bca90) independently resolves to ordered parents **[PR72 `617cfee3...`, PR73 `ba625afe...`]** and **the same complete Git tree `4db8dc5e...`** as the reviewed source HEAD; this is a direct tree-identity check, not an assumption from the CI title. No original H1 `.mo`/study, historical native-case JSON, MAT/CSV archive, physical reference, native runner, or earlier PR source path is in the four-file diff. At review time PRs **#69–#73** remained draft and unmerged.

## 2. N-01 — byte-exact runtime index gate: PASS

In [the pinned bridge](https://github.com/physicsvigilante/sim_heat/blob/ba625afe3223d4c0fda5d23b88445d08d64771c6/tools/published_diagnostic_bridge.py), the runtime recomputes `compile_pair_index(ROOT, SOURCE_MANIFEST, CASE_INDEX)` and now requires:

```python
if stable_json(generated) != safe_file(PAIR_INDEX, ROOT):
    return {}, None
```

`stable_json` is the existing archived canonical serializer; `safe_file` reads the fixed, in-repository `viewer/network/data/compare_index.json` bytes. The comparison precedes any source-pair selection or archived route construction. Consequently **equal JSON objects with different original-index bytes are insufficient**. The existing exact model **and** study SHA matches, unique directed D2→D2_K2 pair, original case-catalog SHA checks, and fixed allowlisted read-only resources are preserved. An index mismatch returns neither archived resources nor a link; it does not cause a fabricated solver, checking-reference fallback or refusal of the separately H1-admitted source preview. This is **source-relative trusted-checkout integrity**, not external source-owner/GitHub authentication.

I examined the actual [new negative test](https://github.com/physicsvigilante/sim_heat/blob/ba625afe3223d4c0fda5d23b88445d08d64771c6/tests/test_authoring_workbench.py). It first proves the committed index bytes are the canonical serialization, then builds `changed = b' ' + original` and proves `json.loads(changed) == json.loads(original)` while bytes differ. Critically, it **does not substitute an out-of-root path**: it patches `bridge.safe_file` to return changed bytes specifically when `path == bridge.PAIR_INDEX`, forwarding all other reads to the original function. This intercepts the runtime index read after ordinary compiler reconstruction. It then asserts `published_diagnostic_pair(...) == ({}, None)`; the correctly admitted D2 preview is still available, the archived comparison route returns **404**, and the source HTML contains `no-published-diagnostic` but not `published-diagnostic-link`.

**Regression sensitivity:** the old PR72 `strict_json(safe_file(...))` and parsed-object equality would admit this same whitespace-prefixed, valid JSON because the parsed value is unchanged; its source/link-positive control is also covered separately. The new test therefore discriminates the intended behavior rather than accidentally passing on path containment. Hosted CI reports this exact named test **OK**, alongside the positive D2→D2_K2 test, reversed/unrelated pair refusals, bad-manifest/source-hash tests and HTTP route restrictions. I did not rerun the unit test locally.

## 3. N-02 — original saved-time and temperature browser regression: PASS

I directly inspected the unchanged, pinned [D2 archived case](https://github.com/physicsvigilante/sim_heat/blob/ba625afe3223d4c0fda5d23b88445d08d64771c6/viewer/network/data/D2.json) and [D2_K2 archived case](https://github.com/physicsvigilante/sim_heat/blob/ba625afe3223d4c0fda5d23b88445d08d64771c6/viewer/network/data/D2_K2.json), including their first two `samples` rows:

| Original saved observation | D2 baseline | D2_K2 successor |
| --- | ---: | ---: |
| `rod.Q_flow` at **0 s** | **+12 W** | **+24 W** |
| Next common saved time | **468.75 s** | **468.75 s** |
| `cold.T` at **468.75 s**, full recorded precision | **296.4679940381214 K** | **299.05204547674595 K** |
| Expected viewer display | **296.468 K** | **299.052 K** |

The [pinned Chromium script](https://github.com/physicsvigilante/sim_heat/blob/ba625afe3223d4c0fda5d23b88445d08d64771c6/tests/browser_authoring_workbench.py) still asserts the initial signed **+12/+24 W**, `diagnostic_only` and `nativeQualified=false`. After advancing the slider **one** saved step, it now checks `#time-label == '468.75 s'`, changes the field to `cold.T`, and checks both exact displayed strings `296.468 K` and `299.052 K`. The unchanged [comparison viewer](https://github.com/physicsvigilante/sim_heat/blob/ba625afe3223d4c0fda5d23b88445d08d64771c6/viewer/network/compare.mjs) formats observed Kelvin readings with at most four decimals; [compareNativeCases](https://github.com/physicsvigilante/sim_heat/blob/ba625afe3223d4c0fda5d23b88445d08d64771c6/viewer/network/compare_core.mjs) requires equal saved timestamps and **forbids interpolation**. The numbers are old recorded diagnostic samples, not new calculations or newly certified physical references.

Inherited checks still deny raw Modelica and unrelated archived native cases (404), deny writes (405), hide the original link after an untrusted/forged browser import, and avoid accepting imported client-side JSON as authority to re-pin the server's archived pair. Unrelated or corrupted historical metadata produces source-only/no-result behavior, not a different result pair. The original source preview remains `not_computed`.

## 4. Hosted exact-source CI and evidence attribution

I independently queried [GitHub Actions run **44680586259**](https://github.com/physicsvigilante/sim_heat/actions/runs/44680586259), job **136102745050**, its step results, **full job log**, and artifact metadata. The event is `pull_request` for **#73**, head SHA **`ba625afe...`**, target SHA **`617cfee3...`**, attempt 1, **completed/success**. Its checkout is the above verified synthetic merge with identical source tree. The workflow parent checks in the log use those exact event SHAs; its original PR71 nine-path fence and protected-source exclusions still pass. The installed executable was **Google Chrome 157.0.8103.50**, and the log shows the actual HTTP browser scripts executed successfully.

The job logs show **152 H1 + 4 analytical + 63 adapter + 61 product + 51 JavaScript = 331 distinct tests**, with **330 passing and one existing optional external-archive adapter skip**. In particular, the positive archived-pair and new byte-reserialization negative product tests are logged **OK**. The workflow's generated archived compare index (reported SHA-256 **`34f6abac6948fd5c70b3b91d13a72336c5d768ce235f0108f26c57731ef134c3`**) passes an actual **byte-for-byte `cmp`** with the unchanged original published index; docs/source-preview byte parity also passes. The workflow replays **six old archived diagnostics offline** from original artifacts, and its real-HTTP Chromium source/workbench, saved-comparison, historical-browser and refusal scripts all exit successfully. The newly added assertions are on the exercised browser path. The workflow installs checker/Playwright dependencies, **not OpenModelica**; no OMC version query, native simulation build or launch is in its commands.

GitHub independently reports artifact **[14603669026](https://github.com/physicsvigilante/sim_heat/actions/runs/44680586259/artifacts/14603669026)**, named `teacher-archive-handoff-5894517a41ee528052fa4744e36d57b3721bca90`, size **14,617,266 bytes**, with **GitHub-reported** ZIP SHA-256 **`9c39229cc44f34604242f64df24838c2a5a7591d22b836e91c6037609f4926bd`**. The upload log agrees. **I did not download, personally rehash, CRC-check or inspect that ZIP's screenshots.** The full browser assertions are supported by their pinned source, GitHub run identity and successful actual script step, **not** by a screenshot I independently opened. Similarly, the archive replays are hosted-CI evidence, not tests or native executions I personally ran.

**Personally performed:** instruction/previous-review reading; GitHub pinned source/base/synthetic merge/tree and four-file diff inspection; direct bridge, new unit test, browser test, workflow, unchanged viewer and archived sample inspection; independent run/job/log/artifact-metadata retrieval; corroboration of exact saved values and the change's negative-test sensitivity. **Not performed:** local tests/Chromium, independent archive/artifact ZIP extraction, OpenModelica execution or installation, solver reruns, deployment, or source/reference promotion.

## 5. Disposition and surviving holds

**No blocking issue in the proposed N-01/N-02 corrections.** N-01 now enforces runtime original-index **byte** parity rather than only semantic equality, with a negative test that targets the correct read. N-02 pins the browser to the correct already-saved common instant and archived temperatures. Hosted CI is green at the exact reviewed tree and retains the inherited allowlist, import/refusal and original-evidence boundaries. Artifact byte/screenshot reinspection would add independent corroboration, but its absence is disclosed, **not** evidence that the hosted browser assertion failed.

The pre-existing **seven 100× static physical-reference checking failures**, **eight native blockers** and **unsealed/unavailable private scorer** are **unresolved**; I did not rerun or amend those historical investigations. Evidence fields and source SHA values are relative historical provenance, **not** an external authenticity seal. The viewer remains `diagnostic_only` / `nativeQualified=false`, and authored requests remain `not_computed`. No novel source composition gains a recorded native trajectory.

**Final decision: SCOPED PASS for PR73 at exact `ba625afe3223d4c0fda5d23b88445d08d64771c6` / tree `4db8dc5e6b054eb4479bca26960e7f49f17c9395` only.** Preserve the original PR72 review and all historical model, archive, reference and evidence bytes; keep PRs draft/unmerged. Any native run, reference promotion, merge or deployment requires separate authorization and qualification.
