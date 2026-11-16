# EM Fields PR #27 — independent focused R1 review request 01

**AUTHOR-QUALIFIED SOURCE CANDIDATE; INDEPENDENT REVIEW PENDING; DRAFT / UNMERGED (2026-11-16 Asia/Kolkata).** Review the exact corrected source and original native evidence, not a floating branch, guessed output directory or implementer claim. This is a bounded *evidence-presentation* R1 feature: if any source/evidence/measurement meaning is altered, escalate to R2. The independent reviewer must write its own findings and never modify the source PR.

## Pinned source and contract

- [Source PR #27](https://github.com/physicsvigilante/emfeeld/pull/27), [Issue #26](https://github.com/physicsvigilante/emfeeld/issues/26).
- **EXACT head**: `2dc5e1d90a1cec2809d536f725474eac0ae4dd2d`.
- **Canonical source Git tree**: `45df8622888b841333d7242caf410e7449900cfc`.
- **Qualified base main**: `9e5924efa60dea56606e0b8eef591f94711b666d`, Git tree `ce20aa49d978c94150edbbf017d8fae1e2f6f896` (PR #25 [final release](../pr-25/MERGE-REPORT.md)).
- GitHub **PR CI merge-preview**: `d230d97d9d3b300688ed0796f01f686b57d53cc0`. Git-commit object independently reports tree **`45df8622888b841333d7242caf410e7449900cfc`**, parents **exactly qualified base then current head**. This is a PR preview, *not* a production merged source.
- Exactly five affected paths: `src/emfeeld/scenario_ensembles.py`, `tests/test_scenario_ensembles.py`, `.github/workflows/release-candidate.yml`, `README.md` and new `docs/VERIFIED_ENSEMBLE_MEASUREMENT_READOUT_V1.md`. Existing physical field laws, integrator, source model, native comparison inspector, source V3 revision engine, renderer, numerical tolerance and old run evidence were not modified.
- [Frozen bounded source contract](https://github.com/physicsvigilante/emfeeld/blob/2dc5e1d90a1cec2809d536f725474eac0ae4dd2d/docs/VERIFIED_ENSEMBLE_MEASUREMENT_READOUT_V1.md).

### Feature and scientific meaning

A new strict read-only command:

```bash
python -m emfeeld.scenario_ensembles measurements ENSEMBLE_OUTPUT --store EXACT_STORE --using ORIGINAL_RUN
python -m emfeeld.scenario_ensembles measurements ENSEMBLE_OUTPUT --store EXACT_STORE --using ORIGINAL_RUN --member EXACT_MEMBER_ID
```

It runs the existing full `inspect_ensemble` on the original immutable parent/store/native template and *every member* **before** applying the filter, then re-inspects existing sealed per-member comparisons using the qualified `scenario_comparisons.inspect`. It projects only original saved `id,type,status,unit,value,code,reason,error_bound,context,left_observation_id,right_observation_id,particle_id` fields and source-bound request/result/integrity/run SHA256 references. It does not evaluate a field, integrate a trajectory, create a new comparison, choose a missing body, round any result, convert units, invent zero values or write a cache. The original comparison signs remain **right minus left** (member minus *fresh common* baseline); hypotheses are **distinct prescribed alternatives**, not temporal evolution.

The original **global** ensemble complete/partial status controls CLI exit code and is not replaced by filtered member status. A complete selected G1 native run may coexist with a legitimately partial cross-comparison; absent baseline body has `status=unavailable`, `code=unknown_operand`, `value=null` and original reason. Rejected/native-incomplete members have no fabricated measurements and retain their explicit decision/reason. A literal member named `baseline` is distinct from the fresh left baseline and must be selected via `--member baseline`. Refuse `--output`, `--sample-index`, `--baseline` in this command. The old `run/inspect/view` commands remain supported. Exit 0 complete, exit 1 honest global partial, exit 2 invalid/integrity failure.

## Independently executed adversarial review required

1. **Exact original value/meaning preservation:** independently inspect pinned native comparison request/result source bytes (not only the author's projected output). Check each signed scalar/vector, unit, physical point/endpoints/time, pair/particle ID and typed field against the new readout. Include positive and **negative** signed E1 field differences, gravitational G1 values, matching true `null` for unavailable, and exact saved evidence SHA256. If value rounding, changed sign or arbitrary unit filling is found, request changes and escalate risk.
2. **Global partial vs member filtering:** filter `--member hypothesis-B` in actual G1 partial and a complete sibling in another partial ensemble; output and CLI must retain **global** partial while selected native member may be complete. Check all/one/specific member `baseline` identities, ordered 2–4 siblings and no replacement by positional guess. Rejected source V3 or accepted-but-native-partial member remains a truthful no-measurement outcome.
3. **Strict read-only and fail-closed integrity:** independently construct positive and negative sealed native fixtures; compare path and full original file-byte inventories before/after each call and refusal. Tamper an **unselected** sibling while selecting a healthy one, original accepted/rejected stored proposal raw bytes, sealed comparison request/result/inventory, source template, outer ensemble, stale revision, malformed selector. Include mutation of result/request **between** full ensemble inspection and readout projection (TOCTOU ordinary race observation); prohibit presentation or output writes and do not claim distributed crash-safe ACID/malicious hash resealing resistance.
4. **CLI/evidence regression:** invalid `--output`, `--baseline`, `--sample-index`, non-string or unknown member; preserve `run`, `inspect` and `view`, F1 unrelated sealed screenshot prohibition, F2 member named baseline source-bound receipts, earlier R2-01 static-mode+trajectory zero-write rejection, R2-02 raw JSON `1e400` nonfinite rejection and original proposal-byte guards.
5. **Real native E1/G1/T1 evidence:** independently download at least relevant original Linux and Windows release ZIPs below. Validate original bytes, seals and run/comparison source hashes, and the two new E1/G1 stdout JSON readouts against saved original comparison values; audit legitimate unavailable body, no fabricated zeros, screenshot receipt original sources and recorded saved physical time. Do not relabel author CI or offscreen screenshots as independent numerical derivation, manual Windows desktop interaction or actual classroom usefulness.
6. **Reviewer-owned tests:** execute genuinely novel fixtures/negative probes outside the pinned source, preserve first failing attempts and harness errors, cite environment and exact command. The 79 author-defined focused tests are a replay only, not independent novel work.

## Exact-head author qualification and immutable original archives

**Exact source snapshot:** [workflow #43913225024](https://github.com/physicsvigilante/emfeeld/actions/runs/43913225024), SUCCESS; original uploaded artifact **14249076188**, independently downloaded original ZIP SHA256 `c805342eab615b0ef43a28ea63cac513b120e5dc26653d123e089a6cea406076`; embedded source tar SHA256 `ffb70b457202832b560a0645d38c34910b84ee4e64197e6e118109e3d9ff6582`. **347 original tracked files** recreated an independent Git index; `git write-tree` exactly returned the pinned head Git tree `45df8622888b841333d7242caf410e7449900cfc`. **79/79 focused tests** passed `-W error` from that untouched downloaded source.

**Original exact-head Linux/Windows CI:** [clean-install #43913225233](https://github.com/physicsvigilante/emfeeld/actions/runs/43913225233) **SUCCESS on both OSs** at PR preview `d230d97d9d3b300688ed0796f01f686b57d53cc0`. Original Ubuntu job **133460397109**, original Windows job **133460397794**. Direct GitHub original logs per OS: **1,481 headless passed, 18 historical behavioral passed** (one frozen whole-file guard intentionally deselected), **33 real-PyVista passed**, and separately repeated **79 focused ensemble tests** (already part of the 1,481 headless). Actual E1 full and G1 partial readout commands completed. The full local author run earlier exceeded an execution limit at about 24% and was **not** declared a local full pass or a failure; exact-head hosted CI establishes current-source full test success.

**Separate real-PyVista:** [workflow #43913225195](https://github.com/physicsvigilante/emfeeld/actions/runs/43913225195), render job **133460400998 SUCCESS**, original log **1,481 passed** plus actual offscreen rendering/slider events. Local PyVista not installed; no live manual Windows pointer qualification claimed.

**Original new release artifacts, downloaded and independently byte-audited by Chat A:**

| Artifact | GitHub artifact ID | Original ZIP SHA256 |
|---|---|---|
| [Linux release](https://github.com/physicsvigilante/emfeeld/actions/runs/43913225233/artifacts/14247794085) | 14247794085 | `a8ec0e8697e43e5ef23892d3e3dc0fe7de3e830bb97d7db175e4393e74cdb014` |
| [Windows release](https://github.com/physicsvigilante/emfeeld/actions/runs/43913225233/artifacts/14250075846) | 14250075846 | `703f05bc03e2bb411c66a0637a675b59da312f9c65e0566a3a4e3a094a288d86` |
| [Separate viewer](https://github.com/physicsvigilante/emfeeld/actions/runs/43913225195/artifacts/14247663796) | 14247663796 | `a7660e661947a7eeaa8a285e7975df48f071e6640b386d988fdb1ff74f386bf0` |

**Original archived native audit on EACH OS:** 2,159 unique CRC-clean entries; **33 complete SHA256 inventories** (21 top-level +12 nested native), **12 complete native runs**, **60 original input-hash bindings**, **six sealed comparisons**, six stored original accepted proposal hashes, **32 ok +two genuine G1 unavailable** comparisons. Original saved E1/G1 PyVista screenshots each source- and run-seal-bound. **New** `ensemble-measurements-E1.json`: E1 **complete**, two members with 5+5 original `ok` readings. **New** `ensemble-measurements-G1.json`: global **partial**, filtered to hypothesis-B native-complete member with 7 original `ok` and one true `unavailable/unknown_operand/null` reading. Both readouts verified against *every original projected field*, original request/result/integrity SHA256 and original left/right run hash. Separate viewer ZIP: 22 CRC-clean entries, **all 17 original 1200×850 PNG-to-report SHA256 file bindings** verified, with 16 unique PNG digests because the flat/nested composition frames are legitimately identical. Original ZIPs are the **source CI** evidence, not an independent Chat B finding. Audit JSON `emfeeld-pr27-exact-head-audit.json` SHA256 `20c54c440229fb0372edbe2099e5af76945bd330925b2f4dfaac241cd0f46dbc`, generated locally, not a GitHub required status check.

**Evidence limitations:** source authors' E1/G1/T1 separate formulas/RK4 checker reports 20 static, 12 trajectory and two expected unavailable per OS; same-author reference is not a new independent human numerical certification. Unkeyed SHA256 checksums are not malicious-writer authentication. Local path integrity is not hostile concurrent distributed ACID. Offscreen real PyVista renders are not manual Windows pointer testing or classroom learning outcomes.

## Review outcome and gate

Please conduct independent scoped **PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE** review on the **exact head/tree** and publish a NEW reviewer-owned report at:

`physicsvigilante/review_sandbox/projects/emfeeld/pr-27/reviews/review-01-chat-b.md`

Preserve the prior PR #23/#25 review records, their first failures and source SHA binding unchanged. **Do not write to source PR #27, modify or merge its branch, alter original saved experiments, or turn review packet into a production approval.** Chat A will retrieve your report after owner says “review done”, address any blocker, and only separately perform owner-authorized guarded merge plus fresh post-merge main qualification.
