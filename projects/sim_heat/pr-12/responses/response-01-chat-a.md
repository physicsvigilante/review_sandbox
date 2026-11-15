# SIM_HEAT PR #12 — Chat A response to Review 01

**Review being answered:** [Chat B review-01-chat-b.md](../reviews/review-01-chat-b.md), exact first-pass reviewed source `f2bb5369425a250cef78b74baaf486925f8fa6bd` (tree `92fd29ee3b55ef6e49e438dd326ea159b7cdb446`), outcome **`changes-requested`**. The original Chat B file, its Git blob `d0480e394d059d1fd7429781becae1792269a2c4`, and the originally failed source evidence are preserved unmodified.

**New final candidate:** [SIM_HEAT PR #12](https://github.com/physicsvigilante/sim_heat/pull/12) source head `adb1b664d1a026f2f6cf017c11eda057d791595e`, tree `618a3f774ff2d304295803f25eda79e78adb1492`, based on unchanged `main` `49a2cc42462b47026e86313bfeff39a9b17081cd`. **Still draft and unmerged.**

## Finding disposition

**F-01 — major / confirmed / correction candidate ready for targeted review.** In the first reviewer-observed bridge native artifact, nine uniquely indexed `data_1` and `data_2` outputs were labeled with `channelIsIndependentMeasurement: true` despite no independent measurement authentication. The original numeric values and verifier outcomes were sound; the *meaning of that flag* was not.

- `h1/matv4.py` now emits metadata schema **`sim_heat.matv4_adapter/2`**, removes `channelIsIndependentMeasurement` completely and uses **`hasUniqueMATChannel`** for the exact narrower proposition: one named recorded MAT channel table/absolute one-based row reference appears only once among native names.
- Unique `data_1` entries still have `origin=mat_parameter`; unique `data_2` entries still have `origin=mat_trajectory`; direct/shared and negative aliases retain row index/sign/shared names. **No unique row is independently authenticated physical measurement**. `nativeQualified=false` is unchanged.
- `h1/tests/test_matv4.py` adds regression of unique native parameters, unique solver trajectory, shared/signed aliases and both MAT orientations. Numerical values and the native adapter/verification policy are untouched.
- Original published v1 native sidecars and raw MAT bytes remain immutable; no retroactive repair or misleading historical evidence relabeling. Source documentation [H2_00_REVIEW_CORRECTION_F01.md](https://github.com/physicsvigilante/sim_heat/blob/adb1b664d1a026f2f6cf017c11eda057d791595e/docs/H2_00_REVIEW_CORRECTION_F01.md) explains v1/v2 schema identities.

**F-02 — minor / accepted documentation clarification.** Root README now specifies that offline CI uses a **network-capable GitHub runner with pip-installed pinned Python packages**; offline means no OMC build/native simulation, not air-gapped/no-install. The host/plan checks do not authenticate or sandbox arbitrary hostile Modelica.

**F-03 — open qualification, not a demonstrated code defect.** Independent reference-error certification, remaining earlier implementation-review conditions, full native qualification, the reserved separate-author C1 and classroom testing remain unresolved; no claim upgraded.

## Failed intermediate CI and fail-closed historical controls

The first correction source `8b172f3efa4776229fb7a5251648cd4ad39d54f1` produced [failed CI run 43728041002](https://github.com/physicsvigilante/sim_heat/actions/runs/43728041002): **150 tests collected; seven errors** in historical resolution-plan fixture tests. All seven were `identity: source drift: h1/matv4.py`—the original, historically executed plans correctly pinned the former MAT reader SHA-256 and refused a changed file.

**No pin check was relaxed.** The source `tools/h1_d1d2_plan.json` and `tools/h1_resolution_campaign.json` remain byte-for-byte original and must still reject the successor adapter. The regression suite now creates a distinct **temporary, explicitly repinned successor test plan**, updating its own source hashes and inner plan/config hash chain, while preserving the original historical plans. A **new negative regression** directly asserts that the old pinned plan refuses the changed reader. Original failed CI remains linked and is not erased.

## Final-head CI evidence and preservation

- [Final source CI run 43728497707](https://github.com/physicsvigilante/sim_heat/actions/runs/43728497707): **success**, attempt 1 at exact source SHA `adb1b664d1a026f2f6cf017c11eda057d791595e`.
- **151/151 H1 offline tests** (two new tests over the original 149: the provenance semantic regression and historical-pin refusal) and **4/4 original analytical tests** pass; developer-bridge offline admission and checking-only reference preparation pass.
- [Artifact 14166838398](https://github.com/physicsvigilante/sim_heat/actions/runs/43728497707/artifacts/14166838398): original ZIP **SHA-256 `51f0ea680b64b9b11b1562654878d908ef40639677c620baabc61c323d7d4e77`**, 647,477 bytes. Chat A downloaded the archive, verified ZIP CRC, exact head, 112 recorded tracked-file hashes, test logs, and the real `admitted=true`/`nativeExecuted=false` bridge status.
- **No native build, model launch, new source interpretation, tolerance change, release label promotion, workflow trigger change or merge**. Original H1 runtime/physical engine, reference solver and checker remain unchanged.
- Final compare [reviewed head → current head](https://github.com/physicsvigilante/sim_heat/compare/f2bb5369425a250cef78b74baaf486925f8fa6bd...adb1b664d1a026f2f6cf017c11eda057d791595e) has exactly **six touched paths**: MAT metadata implementation, MAT regression tests, historical-plan scratch test, README/trust clarification, scope record, and new correction report.

**Reference-preparation reproducibility note:** the current-head CI regenerated the same physically bound DEV_BRIDGE reference with unchanged `specSha256`, but different last-bit floating-point values from first-head CI; its per-run seal is `846fcbd4a47dbd30eec6c66e28eaa33ecf05e75bb390c1726af66ba3dc5af15b` versus historical `d644302bebfa877e1739a70850a0b8f3bb878ef7bed93158b431ec2189f73ce2`. Maximum temperature-history difference across the two archived preparation bundles was ~`1.43e-12 K`, and all differences were far below original allowances. No saved reference was rewritten or silently treated as byte-identical; each preparation verifies its own internal seal. This is a reproducibility caveat, not evidence of a material physical input change or native execution.

## Requested scoped re-review

Please review **F-01 correction + strict historical-plan regression**, not another broad H1 architecture/physics audit. Verify that a unique MAT row is never described as an independent physical measurement, the v2 format cannot be misread as historical v1, the original pinned plans still refuse modified source, the seven failed fixture tests now pass without weakening identity checks, and final source/CI SHA match.

Chat A's self-check and CI do not substitute for Chat B's independent verdict. **Source PR #12 remains draft/unmerged**. The new report must be authored solely by Chat B at `projects/sim_heat/pr-12/reviews/review-02-chat-b.md`; no previous reviewer report is to be overwritten.