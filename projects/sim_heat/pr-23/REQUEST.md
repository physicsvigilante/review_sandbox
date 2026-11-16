# SIM_HEAT H3-06 PR #23 — independent R2 review request

**Project:** sim_heat  
**Source PR:** https://github.com/physicsvigilante/sim_heat/pull/23 — **draft, unmerged**  
**Base commit:** 69350dab2a6faf0c10d0c0aa1d2333051f40e0e9  
**Exact review HEAD:** **439c02ae3157f01c8ccc7ab5eb58297af0c17d92** — not the floating branch  
**Git source tree:** 5ee04196a4e9a21f180f63362e1b58acdd793ac2  
**Review class:** **R2**, new native evidence-pair source binding and public comparison semantics, not a new physical law or native solver.  
**Report destination:** projects/sim_heat/pr-23/reviews/review-01-chat-b.md, independently authored by Chat B.  
**Status:** awaiting independent review. The owner's standing merge authorization does NOT waive R2.

## Purpose

Teacher-facing what-if comparisons must be validated against their *actual admitted H1 parent and successor studies* and their *original separately verified native archives*, not an expanding apparatus-specific UI switch or manually entered display numbers. The existing D2 → D2-K2 one-rod doubled-conductivity example is the **only published pair**; this PR introduces generic source-pair authorability/validation, not a second invented native case.

Original baseline H1_D2 native run 43691263273, artifact 14152886226, full ZIP SHA-256 **8fc38b9e2f040b48ab5cbeab34e8698b7c99c4d462a1e31e8bc33b0395185379**. Hypothetical successor H1_D2_K2 original native run 43693191224, artifact 14153251022, full ZIP SHA-256 **dc32a0a36a27f031ce7a13da83ebdd26a3dd6ac1d14612fa597b36cb439f4843**. The latter is batch 1 / case 1 of the original native conductivity campaign; 592/592 original member SHA values and original MAT/CSV were independently verified by [PR #19 Chat B Review 01](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-19/reviews/review-01-chat-b.md). Both sources remain **diagnostic_only / nativeQualified=false**. Physical time runs 0–9375 s, 1001 native timestamps and 21 genuine preview points at matching times; rod.k 100→200 W/(m K) is the **only** effective physical change.

## Source changes: strict v2 pair contract

The [exact base-to-head diff](https://github.com/physicsvigilante/sim_heat/compare/69350dab2a6faf0c10d0c0aa1d2333051f40e0e9...439c02ae3157f01c8ccc7ab5eb58297af0c17d92) contains **ten changed paths** only: the new H3-06 branch-only CI workflow, docs/H3_06_SOURCE_PAIR_PROVENANCE.md, viewer/network/README.md, compare_core.mjs, data/compare_index.json, data/compare_sources.json, tests/browser_smoke.py, tests/compare.test.mjs, tests/test_compare_source_pairs.py, and tools/build_compare_index.py.

**No change to any H1 file, Modelica law, physics/numerical/temporal checking, native runner, historical native artifact, original six native case JSON bundles, default standalone graph renderer app.mjs or core.mjs.** No new OpenModelica build or launch in this source PR.

- **Input manifest:** viewer/network/data/compare_sources.json, strict schema sim_heat.viewer.compare_sources/1. Each source pair identifies its two approved native case IDs, actual H1 parent/successor study paths, and explicitly **externally checked** original run/artifact IDs, executed SHA, original full ZIP SHA-256, original MAT/CSV hashes, and selected case_XX/normalized.csv entry for both sides.
- **Read-only H1 source validator:** tools/build_compare_index.py invokes the **unchanged** h1.study.load_study on the actual parent and child. The existing H1 revision validator establishes exactly one effective changed existing rod.k with preserved physical owner IDs/topology/other physical parameters and SHA-pinned direct parent. The new generic adapter also checks identical public requests and analysis/time grid, model/study source identity, original native case bytes against the case catalog SHA, truthful original graph/rod port ownership, native K/J/W channel availability, strictly ordered actual saved sample times including initial/final, initial/maintained T and relative energy, and diagnostic-only semantics.
- **Output v2:** sim_heat.viewer.compare_index/2. The revision target, actual before/after conductivity, H1 study/model hashes and reason come from real admitted Modelica/study inputs rather than author-entered output numbers. Both baseline/successor output fields contain the original native source identity tuple. Published index is **reproduced byte-for-byte** by running the new source compiler; exact-head CI checks this with cmp before running regressions.
- **Browser guard:** compare_core.mjs checks the exact original native run ID, artifact ID, full ZIP hash, source commit, MAT/CSV hashes and source archive entry against each already catalog-hashed native case before displaying any original K/J/W. All prior graph/owner/time/initial energy/refusal constraints remain. compare.mjs stays **byte-identical**, with no apparatus dispatch, simulated intermediate observations or hidden native execution.
- **Source output-slot policy:** one real GitHub run/artifact may contain two **different** output slots; different native run IDs are not automatically required. If original artifact ID is the same on both sides, original run ID and full ZIP hash must be the same, but the two selected archive entries must be **different**. The exact same native (run ID, artifact ID, archive entry) slot cannot appear twice as independent cases. These are internal source-consistency constraints, **not** external host attestation.
- **Trust boundary:** A fabricated native case JSON and input manifest, coherently re-pinned with invented matching GitHub metadata, can pass the offline/browser internal consistency checks. The new tests intentionally demonstrate this *test-only* admission, and explicitly do NOT claim to verify a fabricated GitHub execution. Trusted outside verification of every new run/commit/artifact/original whole-ZIP digest remains mandatory.

Full source rationale: [H3-06 contract scope](https://github.com/physicsvigilante/sim_heat/blob/439c02ae3157f01c8ccc7ab5eb58297af0c17d92/docs/H3_06_SOURCE_PAIR_PROVENANCE.md).

## Testing and exact source evidence

[Final CI #43870501998](https://github.com/physicsvigilante/sim_heat/actions/runs/43870501998) is **completed/success at the exact review HEAD**:
- Deterministically regenerated the published compare_index.json from real H1 source and catalog; cmp passed.
- **151 H1** + **4 analytical** passed.
- **32 discovered Python adapter methods: 31 executed/passed, one deliberately skipped optional original native ZIP replay** in generic CI (not counted as a pass).
- **23/23 Node** tests passed.
- **Real desktop/mobile Chromium** passed on original six native cases and the D2/D2-K2 pair, wrong native-pair run ID refusal clearing, and synthetic asynchronous pair-selection race. The race test uses *two menu labels for the SAME approved D2/D2-K2 source pair* — not a new physical system or seventh fabricated native case.

[Original CI artifact 14227156874](https://github.com/physicsvigilante/sim_heat/actions/runs/43870501998/artifacts/14227156874): **5,561,787 bytes**, ZIP SHA-256 **dc9272e8f5b8a14cce3e90c45923994028fbdd2515d91e2846e11525a35e04ff**. Chat A independently downloaded/hashes/CRC-checked it; exact head-sha.txt matched the review HEAD. Visually inspected screenshots whatif-async-pair-race.png and whatif-provenance-refusal.png and the original whatif-desktop.png. Logs and independently rebuilt compare index are in the archive.

**History preserved:** Initial source CI [43869630924](https://github.com/physicsvigilante/sim_heat/actions/runs/43869630924) **FAILED** on an older commit due only a missing parenthesis in one new Python test. This was fixed, followed by passing CI; the original failed status is not relabeled. Other interim cancelled runs retain their original identities.

## Independent adversarial R2 questions

1. Recheck real H1 D2/K2 source files and original SHA pins. Does the new compiler really use **unchanged H1 revision checks** to reject a second changed physical input, wrong parent, changed topology and requests/analysis, rather than trusting arbitrary manually pinned metadata?
2. Independently regenerate compare_index/2 from the **actual** source manifest and original six catalog case files. Challenge SHA-repinned wrong native run/commit/artifact/ZIP/MAT/CSV/entry, misowned graph/temperature/energy fields and altered but still valid H1 saved times. Are rejected cases typed refusals and is a fabricated self-consistent source correctly described as **outside trust**?
3. Inspect pair source relation carefully: same-run/same-artifact but **different** output slot, same artifact ID with inconsistent run/ZIP, identical source slot on both sides. Does it permit only logical comparisons without claiming independent physical measurements?
4. Independently test or inspect new Node/browser refusal and stale asynchronous selection scenarios. Does compare_core.mjs check native source metadata **before rendering**, clear stale values on mismatch, retain saved-time K/J/W, and avoid a fabricated second pair or time interpolation? Distinguish reviewer-operated browser from author CI screenshot inspection.
5. Confirm exact ten changed paths, no H1/Modelica/native runner/original six case JSON/legacy viewer changes, nativeQualified=false and preserved historical native/failed-CI artifacts. No blind H1-C1 transfer, arbitrary symbolic inverse solver, full source-host attestation, scientific native qualification or classroom effectiveness is claimed.

**Output:** Independently author a new review at **projects/sim_heat/pr-23/reviews/review-01-chat-b.md**, following central [REVIEW-TEMPLATE.md](https://github.com/physicsvigilante/review_sandbox/blob/main/REVIEW-TEMPLATE.md). Record exact source head/tree, individually performed tests versus inspected developer CI, defects and scoped PASS / CHANGES-REQUESTED / INSUFFICIENT-EVIDENCE. **Do not edit source or merge PR #23.** After a real independent scoped PASS, the owner's standing permission allows Chat A to merge the unchanged reviewed commit without another routine approval, followed by main/post-merge CI verification.
