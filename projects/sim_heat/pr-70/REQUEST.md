# SIM_HEAT PR70 — main-based project audit corrections, R2 review request

**Decision requested:** SCOPED PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE for the five concrete maintenance corrections below. This is NOT another numerical qualification layer, acceptance of PR69, or authorization for native execution/merge.

## Exact source identity

- Source draft PR: https://github.com/physicsvigilante/sim_heat/pull/70
- HEAD: `3f718ce0f1bb3fbc75162f99862796e32d2b0752`.
- Whole tree: `d9bd26ff57b22be20fce9c39ad855b0fa8fe4862`.
- Actual base **main**: `f52613c39c539b2d4543a9838e5658d526fca10e`, tree `0c44961b473d23737b0c9f3b3f2cd3db65b9f264`.
- Synthetic PR checkout `e2646ec13347b10583110197f5b96f7f655599b2` has identical whole tree, parents [main, candidate].
- Eleven paths changed: h1/study.py, h1/source_preview.py, tools/authoring_workbench.py, tools/h1_native_batch.py, h1/tests/test_resolution_campaign.py, two existing source-preview/workbench workflows, two new audit test files, tools/check_project.py and docs/PROJECT_AUDIT_2026_11_19.md.
- Original Modelica components, numerical policies, reference cases, native output archives, C1/frozen files, public observation quantities and prior PR69/N1–N8 sources are unmodified. Original execution plans are NOT repinned. The campaign test changes only its explicitly temporary fixture pins.

Read source AGENTS.md and central PROTOCOL.md / REVIEW-RISK-POLICY.md. Review implementation, source-diff integrity and self-checks, not the implementer's preferred outcome.

## Independently challenge these corrections

**A19-01 portable launch:** direct `python -I /checkout/tools/authoring_workbench.py --help` from an unrelated directory must work without PYTHONPATH. Verify import-root setup does not alter read-only loopback/Host/route behavior.

**A19-02 Windows path boundary:** `load_study` now converts a filesystem-relative Path to `.as_posix()` before portable descriptor validation. Test that Windows separators no longer break valid local paths while traversal/symlink/descriptor constraints remain. The developer's test is PureWindowsPath simulation, not actual Windows native qualification.

**A19-03 source snapshot integrity:** frozen Study objects previously contained mutable dictionaries. Changing an admitted mass to 987, provenance note, request unit or topology could still produce a preview claiming old source hashes. New `verified_snapshot` re-admits disk source under the ORIGINAL retained case root, exactly compares all typed source/derived structures, and returns a detached fresh Study. Test nested mutations, source-file changes, subclass/type tricks, copied objects, output aliasing and sibling-directory conductivity revision paths. A changed in-memory physical fact must never appear under an old source identity. Canonical unchanged TEACH_SPLIT3 JSON must remain byte-identical. This does NOT authenticate truth of the author's original interpretation.

**A19-04 plan hash/parse race:** `load_plan` now captures, bounds, hashes and parses the SAME raw byte buffer. Reproduce scratch-file replacement after the first read; replacement bytes must not become the parsed plan. No native query/build/launch is needed or allowed. Review exact diff to confirm execute/host/permission semantics unchanged and original plans reject successor code rather than being silently repinned.

**A19-05 recurring CI scope:** original introduction-only all-added-file and protected-diff assertions now apply only to their original milestone source branches. Maintenance main PRs still record/check actual GitHub checkout parents and run ALL regression, archive replay and browser checks. Inspect environment-as-data handling and execute the embedded Python scope guards on original vs maintenance branches. Confirm no tests were disabled and no current PR claims an old milestone's immutable qualification.

The new health command runs existing offline suites and optional archived replay/browser tests, never installs or invokes OMC. Review its output/refusal/error handling, and the audit report's distinction between actual tests, old native evidence, draft qualification and unperformed fresh native qualification.

## Evidence: personally executed vs hosted

Local fail-first on unchanged main: ten code-regression methods produced **7 failures +1 error**, two controls passed. Corrected ten pass; two workflow regression methods also pass, including real execution of the workflow's embedded Python guard under both branch kinds.

Corrected product suites: **313 collected,312 passed,1 optional adapter skip**: 152 H1,4 analytical,63 adapters,52 product,42 JavaScript. Documentation parity passes. Separately, frozen PR69 `23172ce2...` ran **147 qualification-specific tests**, all passing; not an integration test or sign-off for PR69. No unchanged historical qualifier pins were modified to accept main changes.

Five original native archives independently downloaded/SHA256/CRC checked: 14152886226,14155084346,14204656273,14215520616,14153251022. Six original diagnostic bundles (D1,D2,DEV_BRIDGE,S1,TEACH_RING4,D2_K2) replay BYTE_IDENTICAL under corrected code. No archived binary executed.

Exact-head hosted workflows ALL SUCCESS:
- source-preview https://github.com/physicsvigilante/sim_heat/actions/runs/44566839120
- project-audit-core https://github.com/physicsvigilante/sim_heat/actions/runs/44566839405
- authoring-workbench https://github.com/physicsvigilante/sim_heat/actions/runs/44566839372

The two downloaded new CI ZIPs were personally SHA256/CRC verified by Chat A:
- 14550034886 / `d52a71cb41fdaaac23c2ca6e5b31478992b7e8ca216ffca3fc58d4289464d6b8`.
- 14551734124 / `d72bdafd5fdab6f0c9a5c6e3c7993e443fe62258517dead85e34875e1f4b9887`.
The workbench source.tar reconstructs EXACT tree `d9bd26ff57b22be20fce9c39ad855b0fa8fe4862`. Logs verify 312 passes/one skip, all six preserved archives, actual HTTP Chromium explorer/source preview/documentation/workbench desktop/mobile/refusal checks. Local browser attempts were environment-blocked (ERR_BLOCKED_BY_ADMINISTRATOR); hosted browser passes are separate, not retrospective relabeling of local results. Repeated workflows are not additional distinct coverage.

## Required publication and STOP

Publish one NEW reviewer-authored report directly to `physicsvigilante/review_sandbox/projects/sim_heat/pr-70/reviews/review-01-chat-b.md`. Pin exact HEAD, describe independently executed controls versus merely inspected hosted evidence and remaining limits. Do not alter source or another review. If there is a concrete blocker, demand a new regression/source SHA and targeted follow-up, not an automatic broad physics re-review.

No OpenModelica installation/version query/build/launch, no native reference promotion, no merging this PR or the existing draft stack, no historical C1/source rewrite. Seven old strict physical-reference failures/eight native blockers and unsealed original author scorer remain. This audit's recommendation is product/runtime consolidation and one complete supported teaching workflow, not more isolated proof milestones.
