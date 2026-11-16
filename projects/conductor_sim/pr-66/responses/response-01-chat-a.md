# Chat A response to independent M28b PR #66 review #01

**Developer response to CHANGES-REQUESTED — all four findings addressed in a separate corrective source commit; full current-head CI and targeted independent re-review required.** This is NOT an independent Chat B verdict or merge authorization.

- Original independently authored [review-01](../reviews/review-01-chat-b.md) remains **CHANGES-REQUESTED** for exact source head `414e69bd960bc71f3df65c7346e81bf58c1540b8`, tree `ac06b4990b8002394fa7965fa2391eda8ca9f16e`. Preserve reviewer native findings, alternate experiment and original failures.
- Corrected source head: **`b23ebade71e8a2b276fc20fbd86bf656140f2fe2`**, Git tree **`19a5b2acffa105ffa62a81dadd13477cb8853675`**, same original M28a merged base `abb085d41399b0a17429aa207614aad357ccd77c`. Source [PR #66](https://github.com/physicsvigilante/conductor_sim/pull/66) is **DRAFT and UNMERGED**.
- Frozen [preimplementation charter](https://github.com/physicsvigilante/conductor_sim/blob/b23ebade71e8a2b276fc20fbd86bf656140f2fe2/docs/m28b_charter.md) was committed at `d6959425783bed00a5f76f3ba2ebb8b6f5a4ec24`, before M28b production. No new field E/V, M24a locator, RK, physical symmetry admission or surface guard changes occurred in this remediation.

## F-01 — MAJOR: 'unique root' incorrectly paired after source guard

**Independent result:** One *observed* before-guard plane crossing exists in each of baseline and child. The guard-censored baseline cannot demonstrate its uniqueness over the requested **whole duration**; the child reaches duration. Original cross-scenario `one-resolved-pair` and time shift were overstated.

**Correction:** `src/conductor_sim/event_sweep.py::_root_pair` now pairs only when both M24a `outcomes` are exactly `located`, both have **exactly one** native event with the same source-bound event ID, both runs **complete the requested duration**, and both root directions agree. A genuine early root can remain `located` in its original authoritative native M24a event run yet be **unpaired** at the sweep comparison layer if later roots are unknowable after source guard, terminal stop, or unresolved termination. The original complete M24a data (root bracket, signed direction, force/energy and censoring) remains intact and detached in JSON. New unpaired record exposes each termination, root count and signed direction, never fabricates a shift interval.

**Regression:** `tests/test_m28b_event_sweep.py::test_r2_f01_unique_root_before_guard_is_not_whole_horizon_unique` exactly recreates Chat B's `x=.05m` early detector with M28a reviewer gravity/point-source plan. It asserts both early native roots still exist, baseline `source-guard`, child `duration`, unpaired shift with no numeric estimate and no lost root/bracket.

## F-02 — MAJOR: valid coincident terminal alternatives rejected by HTML

**Independent result:** M24a considers multiple terminal-plane root candidates whose numerical brackets overlap the chosen terminal stop time. Another candidate's representative numerical time may be slightly *after* the stopped trajectory's final time within M24a's event time resolution. Original M28b renderer rejected an otherwise valid native result.

**Correction:** The `event_sweep_viewer.py` timeline now calls the original `validate_event_run` to verify these retained alternatives satisfy M24a's strict overlapping-terminal event invariants. For a candidate with representative time after the terminal stop, the chart draws an explicitly dashed **numerical alternative marker at the true stop boundary** (not at its later candidate sample time) with a tooltip declaring no post-stop motion. Original candidate ID, direction, bracket, representative time and residual appear in the table, formatted with enough significant digits to distinguish close alternatives. The run observation horizon line remains truncated at the original terminal time; no new states, collisions, or field samples are invented.

**Regressions:** The frozen model's uniform-field mass study now has a dedicated `coincident-terminal` example with separate signed terminal planes x=.0500000000m and .0500000005m. Native `test_r2_f02_coincident_terminal_alternatives_render_without_poststop_motion` checks the alternate root time is slightly later than the physical stopping time, authentic native events are retained, HTML marks the boundary alternative, and terminal-censored event shifts remain unpaired. Real Chromium `tools/check_m28b_browser.py` includes this additional offline 390px case with visible original IDs, signed direction, and alternative marker.

## F-03 — Scientific ambiguity: opposite crossing directions paired under bidirectional query

**Explicit scientific choice:** **Unpaired**. A negative-direction crossing and a positive-direction crossing are distinct oriented physical events, even when one `PlaneEvent(direction=0)` observes both. Two separately complete runs with opposite signed directions do not yield a `one-resolved-pair` time shift merely because the numerical crossing times are equal. Original per-root directions and ID remain in native audit; new comparison data exposes baseline/child direction arrays; HTML table and tooltips show the signed directions.

**Regression:** `test_r2_f03_opposite_direction_bidirectional_crossings_remain_unpaired` uses the reviewer-disclosed mirror-symmetric +2 μC point charges at x=−.5m and x=+.5m, with test q=+1nC released from x=−.08m versus +.08m; one center-plane root per duration-complete run, opposite +1/−1 signs. Both native roots remain, but no eligible shift is created.

## F-04 — Minor generic ring-charge wording

**Correction:** Reusable HTML now says each model is a separate teacher-authored hypothetical, **not a time-dependent change of a model parameter**, without assuming unrelated fixed-point/uniform/gravity scenarios contain a ring. Added source-agnostic regression to `tests/test_m28b_event_sweep.py`.

## Acceptance and review next

New corrective head reuses the entire original source model/ODE/event law unchanged, with only M28b pairing conditions, renderer semantics, new explicit example and focused native/browser tests. The new `docs/m28b.md` describes conservative duration-complete, direction-matched unique pairing, overlapping terminal-boundary alternatives, and root-localization limitations.

**Full exact-new-head CI required** before repinning a fresh Chat B prompt. The previously reported **16/16 green** workflows apply only to the older reviewed source; the corrected current head's tests are running and must be checked. Preserve original syntax/browser failed runs and independently authored first review. Then request a **targeted independently authored `reviews/review-02-chat-b.md`** on the new source head/tree. Under the owner's standing authorization, only a **PASS** and green exact-head release gates permit routine merging; no new per-merge approval question is needed.


## Final corrected-head CI acceptance addendum

**Corrected source head `b23ebade71e8a2b276fc20fbd86bf656140f2fe2` and Git tree `19a5b2acffa105ffa62a81dadd13477cb8853675` remained unchanged. All 16/16 GitHub runs observed for the corrected head finished SUCCESS.** This is developer-controlled CI, not an independent R2 sign-off.

- [Python run 43855150059](https://github.com/physicsvigilante/conductor_sim/actions/runs/43855150059): **1,839 passed + 97 real FEMM-only skipped + 11 warnings**, independently on Python 3.10 and Python 3.12.
- [Real FEMM5 run 43855149882](https://github.com/physicsvigilante/conductor_sim/actions/runs/43855149882): **97 passed** retained conductor nonregressions.
- [Real Chromium/retained visualization run 43855149862](https://github.com/physicsvigilante/conductor_sim/actions/runs/43855149862): **PASS** five M28b HTML reports. The new **coincident-terminal** case retains six native event candidates over three runs, including legal terminal alternatives. All five had 390px page/document widths, 348px timeline, no console/page/network errors, and all prior visualizations ran successfully.
- [Artifact 14220977049](https://github.com/physicsvigilante/conductor_sim/actions/runs/43855149862/artifacts/14220977049), **GitHub-reported** digest `sha256:14436fdd484d6132e56d4242e209589f5b0a5528ca1e842d3e144d15e6bb7bf1`. Chat A did not independently download/recompute the ZIP digest. Reviewers should verify archive source-tree identity separately from GitHub's synthetic merge-checkout SHA.
- [Targeted Chat B re-review prompt #02](../REVIEWER-PROMPT-02.md), pinned to the corrected exact head/tree, is ready. No new independently authored verdict is yet available and PR #66 remains DRAFT/UNMERGED.
