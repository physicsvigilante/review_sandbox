# Chat A research findings — PR #90 native observer repeatability

**Authorship: Chat A (developer, same assistant as the implementation), NOT Chat B and NOT independent native or human experimental validation.** These are facts directly inspected from actual GitHub Actions raw artifacts at pinned research head `935a62e96fa56c97c1e6cac5fa5444031df559fb`. No claim of a causal effect of the optional observer, correct continuum-optical critical branch or generalized native solver accuracy.

## Frozen implementation and raw evidence

- [Source research-only draft PR #90](https://github.com/physicsvigilante/opticsim/pull/90), exact head `935a62e96fa56c97c1e6cac5fa5444031df559fb`, base/main `50dd0f4d9530d0a61bb4c7064c4326a8ac0ce518`. Three changed files: [prospective native experiment](https://github.com/physicsvigilante/opticsim/blob/935a62e96fa56c97c1e6cac5fa5444031df559fb/evaluation/native-observer-repeatability-v1/run.mjs), [methodology](https://github.com/physicsvigilante/opticsim/blob/935a62e96fa56c97c1e6cac5fa5444031df559fb/evaluation/native-observer-repeatability-v1/README.md), temporary unified CI stage to retain inputs/results; **zero production src/native/physics changes**. This PR remains draft/unmerged.
- [Actual CI unified run 43841830969](https://github.com/physicsvigilante/opticsim/actions/runs/43841830969) at exact PR source head: **all 11/11 GitHub Actions workflows passed; 766/766 Node tests**, research step passed with `research-complete`. Pinned PhyDemo `811f508d2b070898c241a568b0c167dcb8645251`, Node `24.19.0`.
- [Raw native repeatability artifact **14212862598**](https://github.com/physicsvigilante/opticsim/actions/runs/43841830969/artifacts/14212862598): GitHub ZIP SHA-256 `622c799e7df05c2d33664bbc787ac5456b8c56694e4398c3aafbc2e9f0642426`, **downloaded and independently SHA256-verified by Chat A**. It contains `inputs.json` (28,975 bytes) and `report.json` (392,898 bytes), with original complete synthetic authored scenes, per-scene hashes and all native records. `inputs.json` SHA-256 `6e2048bba533d6a5db1399c407995835692e12139472e025a648e516accf40fd`. The raw report records CI checkout `62cf9d614fb601332c7e56ee0bf19846f4fc81b6` (GitHub PR test-merge), not a new production source commit.
- **180 actual native executions = 9 fully specified existing v9 Glass scenes × 20 repeats**; for each 8 OFF/8 ON in four counterbalanced ABBA blocks inside one Node process, plus two OFF/two ON in independently started Node processes. **144 same-process + 36 fresh-process** runs, **90 OFF and 90 ON**, zero execution/setup/invariant errors, no changed authored input SHA. Independent scalar Snell/TIR *first encounter only* for critical±5° had **zero mismatches**.

## Raw distributions, 10 runs per mode per scene

| Synthetic scene | Ordinary native OFF | Opt-in diagnostic ON | Explicit ON advisory |
|---|---|---|---|
| Normal glass, one source/one detector | 10/10 completed; always 2 hits | Same native result | 10 checked |
| Normal glass, two sources/two detectors | 10/10 completed; always 4 hits | Same native result | 10 checked |
| High→low index, critical−5° | 10/10 completed; one transmission hit | Same native result | 10 unknown |
| High→low index, critical−0.001° | 10/10 completed; one transmission hit | Same native result | 10 unknown |
| High→low, computed critical, original coordinates | 10/10 completed; 4 hits, first TIR | Same native result | 10 unknown |
| High→low, computed critical, **translated** | **7 completed, 3 failed** (3 hits for completed, 4 for failed) | **5 completed, 5 failed** (same two native patterns) | 5 inconsistent, 5 suppressed |
| High→low, computed critical, **rotated 37°** | 10 completed; 4/5/6 hits distributed **5/3/2** | 10 completed; 4/5/6 hits distributed **6/2/2** | 10 inconsistent |
| High→low, critical+0.001° | 10/10 completed; 4 hits, first TIR | Same native result | 10 unknown |
| High→low, critical+5° | 10/10 completed; 3 hits, first TIR | Same native result | 10 unknown |

**Detailed process-order split (important):** In the translated case, 8 in-process OFF runs had 5 completed/3 failed; 8 in-process ON runs had 4 completed/4 failed. The two *fresh-process* OFF runs both completed; two fresh-process ON runs had one completed/one failed. Rotated in-process OFF gave 4/5/6 hits in 5/2/1 runs; ON in-process 5/1/2; fresh-process OFF two runs produced 5 and 6, ON two runs 4 and 5. **Ordinary OFF already varies**, so no observer intervention is required to encounter differing terminal status/native interaction count on the identical critical authored input.

## What this actually supports

- **Supported narrow fact:** Under the present pinned PhyDemo/Node configuration, **separate executions** of an unchanged exact-computed critical-angle finite Glass scene have observable native numerical state/count variability. The research reproduces this with the optional adviser **OFF**, and documents similar variants with it ON; it preserves original `failed` runs rather than promoting them.
- **Supported bounded diagnostic behavior:** For the completed rotated scene, the opt-in Stage-1 diagnostic returned **inconsistent** in all 10 sampled ON runs because of observed represented finite-edge disagreement. The translated scene was **inconsistent** only on its 5 genuinely completed ON runs and **suppressed** on its 5 failed ON runs. The existing diagnostic uses a proven represented-forward condition, not a complete traced physical path or critical-branch oracle.
- **Limited normal and far controls:** The two normal controls and far-from-critical native first encounters were stable in **this** small matrix. In ON mode, oblique normal-to-boundary reference cases often returned **unknown / NATIVE_INCIDENT_POINT_AGREEMENT_UNBOUNDED**, reflecting the current **unvalidated hit-point numerical agreement envelope** rather than proven incorrect Snell behavior. A conservative unknown is not a failed optical ray.
- **What it does NOT prove:** Differences between 7/10 and 5/10 translated completions across different runs do not demonstrate a causal side effect of the opt-in observer; the 4–6 rotated native event counts are not proof of a specific upstream numerical root cause. ABBA ordering and fresh-process repeats provide descriptive evidence, not randomized/counterfactual identical ray execution. No independent teacher/student evaluation, original source interpretation, full Fresnel illumination or physics certification is performed.

**Recommendation (not an authorized new feature):** Retain Stage 1 as opt-in/noncertifying and defer any Stage-2 mandatory measurement withholding. If future reliability work is desired, ask separately for a higher-powered source-controlled assessment of observer overhead/variance and an independently validated reported-point error envelope or a narrow native-upstream geometry bug report. Do not change pinned PhyDemo, numerical cutoffs, authoring, original task data or existing readouts on this initial nine-scene descriptive research alone.

**Explicit release hold:** Research PR #90's temporary CI stage MUST NOT be merged into main. The owner approved doing the research, **not** a new production merge or Stage-2 policy. Seek independent Chat B R2 EVIDENCE/METHOD critique via [REQUEST.md](REQUEST.md) before relying on its interpretation to justify future physical/numerical changes.
