# SIM_HEAT PR #37 — targeted R2 review-02: offline staging/readback integrity corrections

**Reviewer:** Chat B, independently in a separate conversation. **Source draft PR:** [physicsvigilante/sim_heat #37](https://github.com/physicsvigilante/sim_heat/pull/37), historical F0-only, **NEVER MERGE TO MAIN**.
**Original independent review-01:** [CHANGES REQUESTED](reviews/review-01-chat-b.md), source `d1d6a32252b41dabad832668de642ecaf475a2a3`, tree `af85a6f1848a0f1231612144a1230689be8cf0f2`; this report must remain unchanged.
**Exact NEW correction HEAD to review:** **`2f2b8d5008f51b9972897058328aed8cbcbfbbce`**, Git tree **`de397fe3af9bb3385c4ef55354e49c33571dc99b`**.
**Immediate original reviewed PR #37 base:** PR #36 HEAD `7cfa35a1cd5cc858e48bcdc4da453bf2dc22b7f2`. Original frozen F0 source `dd8c9432abe97563414bb3ed809e61e673473812`.
**Risk:** R2 (staging evidence/permission identity), *not* new physical method or runnable native adapter.
**Targeted output:** NEW independent `projects/sim_heat/pr-37/reviews/review-02-chat-b.md`, scoped **PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE** only for F-01–F-04 corrected readback contract. Chat A must never write a purported Chat B verdict.

## Exact source change boundary

Against original independently reviewed PR #37 head, new candidate changes **five F-02-only paths**:

1. `qualification/h1_c1/f02/stage_immutable_inputs.py` (strict JSON metadata, independent disabled plan pin, staged attempt-label equality and parent symlink refusal, strict integer metadata);
2. `qualification/h1_c1/f02/test_stage_immutable_inputs.py` (on-disk adversarial regressions);
3. `qualification/h1_c1/f02/offline_control_preflight.py` (strict frozen original source-pin count JSON integer);
4. `qualification/h1_c1/f02/test_offline_control_preflight.py` (bool and float pin-count negative regressions);
5. `qualification/h1_c1/f02/IMMUTABLE_INPUT_STAGE_SCOPE.md` (history/limits).

There are **no changes** to the original first authored Modelica, first study or notes, separate evaluator-modal study, frozen thermal library/H1 runner/checker, original reference input/bundle, reviewed V2 scientific reference archive/manifest, owner checking-only adoption record, original unlaunched native plan, previous CI runs, or CI workflow. [GitHub old-to-new compare](https://github.com/physicsvigilante/sim_heat/compare/d1d6a32252b41dabad832668de642ecaf475a2a3...2f2b8d5008f51b9972897058328aed8cbcbfbbce) shows five scoped modifications.

Original first-author model SHA-256 `9a165e5ce2cc85da84ecc8bc4e63e2990f2066f3547dc6ba8508fa1afbe5f435`; evaluator-assisted modal study SHA `b43e85b6b10afd6550a43322cf98097fe9781a606ee01bc031eadbfd4783b31b`; frozen library SHA `e57955b6c32cb34321a6b1908306c4ea9a63ae259b95a5fd48c7e8d3b4da10ea`; adopted original PR31 archived V2 **4,409,800 raw JSON bytes** SHA `0db511dd8dba023d16518667de256029cf3e073463ea21e2478aeac8afd1f368`, canonical seal `d2b8e2ca8e1f929cac7b028dcc3f7d0b453921d193f877eb091e23ac70aa4ce9` — unchanged.

## Reviewer findings and corrective tests to evaluate

**F-01 MAJOR (duplicate-key bypass):** At old source, contradictory on-disk manifest/state JSON such as `"nativeAllowed": true, "nativeAllowed": false` could pass because default `json.loads` used last key. New `strict_metadata()` refuses duplicate keys in any JSON object (including nested SHA maps), malformed/nonfinite `NaN`/`Infinity`, symlinked/oversized metadata. Stage state false flags must be literal `is False` rather than numeric zero. Reviewer should *personally* try all 4 top-level duplicate fields (`nativeAllowed`, `nativeExecuted`, `ownerNativeLaunchApproved`, `status`), and a nested repeated source SHA in **actual on-disk** staged files. Confirm all refuse even if a permissive downstream reader might keep a safe last value.

**F-02 MAJOR (coordinated plan + manifest substitution):** The old stage reader only compared plan SHA against a simultaneously mutable manifest, accepting both changed together. The corrected readback calls `f02.load_preview(root/f02.PLAN)` (independent exact approved plan Git-blob identity `2c01301d1c493f33c9eb4bfb9778190adbb6d0bc`), invokes `f02.validate_preview`, and separately demands code-literal original raw SHA-256 `7e03896563ae8b4762b56bb8807612a93cddb759145a23fa94326363ea706326`. An on-disk test modifies the disabled preview bytes **and** updates staged manifest `disabledPreviewSha256`; readback must REFUSE. Also try a mocked parser that returns an apparently valid plan but a different raw SHA: independent SHA pin must still refuse. **Neither this readback nor original stage can ever call native runner/OMC or regenerate scientific reference.**

**F-03 MINOR (attempt and parent provenance):** The original completed stage could be copied/renamed and accepted under a different label; the staging parent could be a symlink. New stage persists original valid label in **both state and manifest** and requires equality with requested readback label. Parent and leaf symlink checks are present. Reviewer should create a valid stage, rename/copy it to another safe label and verify it refuses. Independently create a symlinked `STAGE_PARENT` to actual staged bytes and verify it refuses, not merely leaves. Document residual limits of any local mutable label/TOCTOU check: this is **not** an authenticated global attempt identity, crash-safe atomic one-shot ledger, or protected concurrent-writer surface.

**F-04 MINOR (evidence JSON types):** The prior PR36 F-06 launch-budget and grid strict typing stays intact. Corrected stage readback requires `type(sourcePinCount) is int`, new disabled plan predicate requires `type(frozenCheckerAndSourcePinsCount) is int`. Negative tests inject `23.0` and `true` and require refusal. State numerical `0` must not impersonate `false`; nonstandard constants should refuse. Check type/bool and full plan-pin interplay without claiming global schema generality.

## Exact HEAD CI and preserved history

- **Exact correction source [CI #44028343008](https://github.com/physicsvigilante/sim_heat/actions/runs/44028343008) = completed/SUCCESS.**
- [**Artifact #14304102592**](https://github.com/physicsvigilante/sim_heat/actions/runs/44028343008/artifacts/14304102592): **1,190,731 bytes**; whole ZIP SHA-256 **`256da986efc326fe806185dd36cf42ba5c652c268efef7d28ec2351dafa53191`**, **35/35 CRC-valid ZIP members** independently downloaded/rehashed by Chat A. Original staged inputs and their SHA values were independently recomputed, exact stage label persisted, stage readback receipt `OFFLINE_STAGED_EXACT_INPUTS_NOT_NATIVE` with all false native/owner/one-shot flags.
- **217/217 offline test methods PASS:** 24 staging incl new readback tamper controls, 16 disabled-plan/type, 11 offline owner consumer, 8 original binding, 9 immutable archive and 149 original frozen H1. Original 14 frozen F0 source-pin checks and old 23 plan input pins PASS; no compiler query, build, executable launch, Modelica simulation/MAT or observed nine readings. Artifact carries stage data **only**, not native trace.
- Previous successful source CI [#44024037373](https://github.com/physicsvigilante/sim_heat/actions/runs/44024037373) is **correct only for original reviewed SHA**. Earlier initial stage [CI #44023899014](https://github.com/physicsvigilante/sim_heat/actions/runs/44023899014) remains **FAILED** for three expected-refusal-message test expectation mismatches (not native/physics failure). New interim CI runs may be cancelled by unfiltered concurrency; record their actual outcomes, do not relabel.

Original F0 reference accuracy remained **80× vs mandatory ≥100× FAIL** (original hotLead.G), and PR32 two-host regeneration of original reviewed PR31 seal remains **bitwise FAIL**. The adopted V2 archived `d2b8…` is **not** interchangeable with regenerated `c30e…`; no policy waiver or new reference is made.

## Independent review and strict stop

1. Independently confirm exact source SHA/tree, five changed paths only and **all historical byte identities**, avoiding floating main.
2. Download actual current CI artifact, recompute ZIP SHA/CRCs and staged source/reference raw hashes; inspect 217 test logs and both original/historical failed and current successful job outcomes. Independently reproduce a focused selection of the on-disk F-01–F-04 attacks and distinguish personal execution vs CI records.
3. Inspect readback behavior and malformed JSON/plan/type/symlink/label refusals, **including test controls that previously passed improperly**. Verify the new source produces no compiler/runtime/authorization functionality and has no `reference.prepare` fallback.
4. Report any remaining loophole in the corrected offline evidence meaning, and distinguish local file protections from a genuinely authenticated durable across-run native lock/owner ref. Do not treat green staged-file CI as release/native readiness.
5. Give **scoped PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE** for *corrected offline staging readback*, and list all unfulfilled release/native gates: owner-authenticated protected/durable immutable reference ref and backup; independently reviewed non-regenerating runtime adapter and approved exact plan/source, actual OMC/MSL/compiler/host hashes, persistent one-shot reservation, **distinct explicit owner OMC version/build/launch approval**, and post-native MAT/observation independent review.

**No OpenModelica version query/build/launch. No historical source/PR merge. No first author data/source edits. No tolerance loosening, native readings or new qualified result.** Follow [PROTOCOL.md](../../../PROTOCOL.md), [REVIEW-RISK-POLICY.md](../../../REVIEW-RISK-POLICY.md) and [REVIEW-TEMPLATE.md](../../../REVIEW-TEMPLATE.md). [Chat A response](responses/response-01-chat-a.md) records every finding; original [review-01](reviews/review-01-chat-b.md) is immutable historical review.
