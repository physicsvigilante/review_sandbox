# Independent Codex follow-up review of Opticsim PR #195

**CHANGES REQUESTED** on `6a6b4ea4a9d81f3e1dbda3d3ba4b602c5f34a8cd`, tree `0f2685ed995f85a5efa9e3938f6870626dba131b`. Codex, independent reviewer, 21 November 2026.

The two original B1 clearance failures are corrected. The new runtime audit passed my mirror and detector checks. One qualification error remains in the exported notebook replay and snapshot interfaces when they consume genuine v27 execution evidence from the earlier adapter.

## Remaining issue · Replay counts an unaudited v27 execution as qualified

On the reviewed source, I ran the standard v27 baseline through the exported `replayExplorationNotebook` interface twice. Each runner invoked `evaluateDocument` and executed a real native simulation. Both cores use the same pinned PhyDemo SHA. One used the corrected Opticsim adapter and one used the original PR adapter at `e7e2d199b6be25265decb6f7ec7826a3477ab24f`. Both executed the identical verified notebook input.

| Result | Reviewed adapter | Earlier adapter |
| --- | --- | --- |
| Endpoint verification marker | true | absent |
| Requested observables | 7 qualified | 7 suppressed, all null |
| Notebook status | all-native-qualified | **all-native-qualified** |
| newNativeQualified | 1 | **1** |
| Native detector crossings in currentNativeSummary | 16 | **16** |

No summary field had to be forged. The earlier runner completed normally and lacks the new verifier. The shared observable gate correctly withholds every value, but the row and overall notebook report certify the run anyway. The ordinary command-line entry point rebuilds its own current core, so the discrepancy is specific to mixed-version programmatic replay and historical summary consumption. The seven requested measurements remain suppressed in the failing case.

To reproduce, construct a baseline notebook using the public example and a verified baseline snapshot. Call `replayExplorationNotebook(notebook, {run: (doc, requests) => evaluateDocument(doc, earlierCore, requests)})` from the reviewed source. The [replay acceptance predicate and row construction](https://github.com/physicsvigilante/opticsim/blob/6a6b4ea4a9d81f3e1dbda3d3ba4b602c5f34a8cd/src/exploration-notebook-replay.js#L8-L45) check generic terminal status and never require the v27 marker. The [snapshot acceptance path](https://github.com/physicsvigilante/opticsim/blob/6a6b4ea4a9d81f3e1dbda3d3ba4b602c5f34a8cd/src/exploration.js#L107-L118) likewise accepts the historical execution envelope before building suppressed results.

I separately fed the genuine original CI baseline `native-evidence.json` and its unmodified qualified bundle to the current `snapshotScenario`. The scene hash matched. The snapshot was accepted, all seven requested values were null, and comparing two such snapshots marked both evidence checks accepted. Reusing that archived execution as a test runner's return value also reproduced the incorrect notebook status. The fresh older-core run above demonstrates that a deliberately cached runner is unnecessary.

**Required correction.** Require affirmative endpoint verification at v27 execution-qualification boundaries, including the snapshot/replay status and counters. Keep an older native terminal status distinguishable from current measurement eligibility. A generic native completion with zero truncation is insufficient. Exercise a genuine pre-audit envelope, a fresh current run, an audit failure, and an unaffected historical schema. Preserve ordinary availability rules for legitimate requests that cannot return a value, such as positions above the disclosure cap.

## Checks passed on this head

- Verified commit and tree locally, read the nine-file delta against the first review, and built the headless and browser bundles in an isolated Git export with Node 24.19.0 and pinned PhyDemo `811f508d2b070898c241a568b0c167dcb8645251`.
- Re-executed the exact original long-span detector and translated-mirror cases through the new focused tests. Both were refused during authoring. Lengthening the corresponding segment by 2 mm restored qualification, with 8 detector crossings in the long slab and 16 in the translated system. The 0.1-mm physical margin and the 0.001-mm per-section agreement budget are distinct. The latter is checked at terminal qualification and makes no global error-bound claim.
- Reviewed the instance-local wrappers. The query wrapper returns the original native candidate. The incident wrapper delegates once. For a selected detector miss, the audit uses the pinned supporting-line intersection on the actual incoming ray. It checks segment membership, forward geometry, endpoint clearance, candidate counts, sorted-section agreement and selected-versus-observed hit ordinates. The data is bounded by the emitter sample count and stays outside portable files.
- Ran 72 additional configurations with varied detector positions, 0°, 13°, 42° and 60° incidence, reversed component order and segment orientation, and translated coordinates. Three were refused by the endpoint guard. All 69 admitted cases qualified and matched the expected finite-segment crossing count. Verified the 1-sample and 100-sample extremes. At 100 emissions the 200-crossing aggregate qualified and the entire position list was unavailable.
- Independently perturbed detector queries for a segment missed by every sample. On **each leg separately**, shifting all its query ordinates by 0.0009 mm completed with zero crossings; 0.0011 mm failed the audit and suppressed all requested measurements. The source tests also covered inside/outside detector endpoint checks on both legs, stop/truncation, stale evidence, and old profile isolation.
- Independently ran 32 focused Node tests, the nine-case public JSON acceptance (four completed/five refused), and a real Windows Chrome run (12 checks/six screenshots). The browser run used a disposable launcher copy supplying the installed Windows Chrome path/version and enabling the Chrome sandbox. The reviewed app and assertions were unchanged, including the new invalid endpoint edits and reopening the valid edited scene.
- Read GitHub's eleven successful exact-head workflow statuses and optical job log reporting 1,144 Node passes plus Chrome 12/6. These full-suite numbers are CI evidence. The focused Node, public acceptance, additional controls and local Chrome results above were executed independently.

The native clearance implementation resolves the original examples. The remaining hold concerns the meaning of **qualified** in replay and saved-scenario evidence. A corrected head needs a focused recheck of those consumers.

[First independent report](https://github.com/physicsvigilante/review_sandbox/blob/151009a6c05fcef033007d96ec5c705d3c580eae/projects/opticsim/pr-195/reviews/review-01-chat-b.md) · [Reviewed source](https://github.com/physicsvigilante/opticsim/tree/6a6b4ea4a9d81f3e1dbda3d3ba4b602c5f34a8cd) · [Optical job](https://github.com/physicsvigilante/opticsim/actions/runs/44842213662/job/136653136927)
