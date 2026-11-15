# Opticsim PR #81 — independent R2 **design** review status

**State: TARGETED DESIGN REVIEW PASSED; IMPLEMENTATION NOT YET AUTHORIZED OR TESTED.** This is the completion of the bounded **pre-implementation** design-review cycle, not a code/physics certification or a release approval.

## Source freeze and CI

- Source [PR #81](https://github.com/physicsvigilante/opticsim/pull/81) remains **draft and unmerged**. Exactly one **documentation** file; no feature implementation.
- Production base: `00e6211d6d40c0db8c62910f9e57b910b6aeb6f5`.
- Original design v1 head: `df783a3c2f5e51ad5edbacd35f6d82f1a02cfea7` — 11/11 workflows passed; [unified 43730335002](https://github.com/physicsvigilante/opticsim/actions/runs/43730335002).
- **Revised design v2 and exact reviewed head:** `d814455cf823907551cbc7914d1f8b3b508efcab`. [Pinned proposal](https://github.com/physicsvigilante/opticsim/blob/d814455cf823907551cbc7914d1f8b3b508efcab/docs/NATIVE-RAY-PROVENANCE-PROPOSAL.md), [v1→v2 diff (+46/−18 in one document)](https://github.com/physicsvigilante/opticsim/compare/df783a3c2f5e51ad5edbacd35f6d82f1a02cfea7...d814455cf823907551cbc7914d1f8b3b508efcab).
- **Revised-head existing CI:** **11/11 GitHub Actions workflows passed**, [unified 43733303726](https://github.com/physicsvigilante/opticsim/actions/runs/43733303726). This is **documentation-only software regression checking**, not a test of nonexistent native provenance logic.

## Independent-context review history

1. [Chat B review-01](reviews/review-01-chat-b.md), original exact head `df783a3...`: **CHANGES-REQUESTED (DESIGN ONLY)**, three major findings F-01–F-03 and four minor F-04–F-07. This historical report remains unchanged.
2. [Chat A developer response-01](responses/response-01-chat-a.md): proposed v2 contract corrections, not itself an independent acceptance result.
3. [Chat B review-02](reviews/review-02-chat-b.md), revised exact head `d814455cf823907551cbc7914d1f8b3b508efcab`: **PASS (DESIGN ONLY)**. All F-01–F-07 explicitly **resolved at design level**. Reviewer inspected pinned source and source diff, GitHub CI metadata and performed limited independent Snell calculations. **No new native/browser tests were executed during this review.**
4. **A-01 (minor, nonblocking implementation watchpoint)** newly identified in review-02: require **exact preflight handler-installation/ID-to-native-instance ownership for selected and nonselected detectors and the planar interface**, not solely sources. Test a legitimate detector crossing whose provenance detector wrapper is silently missing or nonrecording. Native crossing must not be misrepresented as an available empty attribution. Independently corroborate counts where possible; two numbers from one observer are not independent evidence. Record future actual test results, not only written promises.

Both reviews come from a separate ChatGPT conversation context, not an independent human physics expert or distinct independently trained model. No source merge, deployment, or independent interpretation of original textbook problems was performed.

## Approved design boundary (not an implemented feature)

The proposed `detector-ray-provenance` observable is opt-in and limited to an **existing v5 planar-media-tracing scene**: **exactly one** planar interface, **1–2 exact single-ray sources**, **1–2 passive detectors**, **zero other component types**. It can claim only actually observed per-run source/native parent-child object identity and detector crossings, **not** a complete ray path, optical image, physical irradiance or source-authenticity proof. Failure/unknown and stop/staleness must fail closed; token IDs are ephemeral per run instance, with A→B→A run-epoch safety.

## Release gates / next actions

- **Design stage:** Complete at the reviewed exact head. No third broad design review is needed for the same contract.
- **Implementation stage:** Requires **separate owner approval**. Implement as a new production feature PR, not by merging research workflow PR #79/#80 or docs-only PR #81 automatically. Preserve PhyDemo pin/physics, schemas, historical no-opt-in outputs and source-backed first attempts.
- **Mandatory novel implementation tests:** all-source registration including clean zero-hit vs silently missing root; installed-interface and installed-**both-detector** fault injection **A-01**; one native wrapper/identical args and returns; two-source Fresnel children and all detector counts/power; native TIR and analytical Snell distinction; duplicate/cyclic child and cap fault injection; partial/truncated/stop evidence non-leakage; warning-vs-model caveat priority; A→B→A stale callbacks; browser/qualified export and raw import suppression; wrapped/unwrapped native comparisons, historical fingerprints and all 11 CI workflows.
- **Future release:** a **new full R2 independent Chat B review of actual implementation code and evidence**, resolution of any blockers, and **explicit separate owner merge approval**. Current design pass is not an implementation sign-off.

Both research PRs #79 and #80 remain draft and unmerged. Source `main` and numerical/physical code remain unchanged.
