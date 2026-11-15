# Opticsim PR #88 — R2 pre-implementation design-review request: v9 finite-hit numerical qualification

**Review scope:** independent-context Chat B R2 **DESIGN-ONLY** critique of a **proposed** native geometry qualification safeguard. There is **no production implementation** in PR #88 and no request to merge it. A favorable design verdict would allow the owner to separately authorize *another* narrow production implementation PR with fresh native/browser tests and a new full R2 code/evidence review.

## Immutable source candidate

- [Draft source PR #88](https://github.com/physicsvigilante/opticsim/pull/88), exact **HEAD: 28c4aa94bbbf6b5a63a8bef433c80186e08a3d35**.
- Current production base/main **fa158fc78da7a35b6a02eaed58c0cdbd4b699220** (owner-approved PRs #83/#86 merged, post-merge 750 Node + 11/11 workflows).
- [Exact base→candidate change](https://github.com/physicsvigilante/opticsim/compare/fa158fc78da7a35b6a02eaed58c0cdbd4b699220...28c4aa94bbbf6b5a63a8bef433c80186e08a3d35): **four research/docs files only**; new proposal doc, test-only shadow and README, **temporary** unified workflow CI stage. **No src/, vendor, saved-scene schema, numerical cutoff, simulator or public-output changes.**
- [Pinned normative design proposal](https://github.com/physicsvigilante/opticsim/blob/28c4aa94bbbf6b5a63a8bef433c80186e08a3d35/docs/NATIVE-FINITE-FORWARD-QUALIFICATION-PROPOSAL.md).
- [Pinned test-only study README](https://github.com/physicsvigilante/opticsim/blob/28c4aa94bbbf6b5a63a8bef433c80186e08a3d35/evaluation/finite-hit-forward-qualification-v1/README.md) and [native shadow script](https://github.com/physicsvigilante/opticsim/blob/28c4aa94bbbf6b5a63a8bef433c80186e08a3d35/evaluation/finite-hit-forward-qualification-v1/shadow.mjs).
- PhyDemo upstream pin unchanged: ricktu288/ray-optics **811f508d2b070898c241a568b0c167dcb8645251**, Node 24.19.0.

## Prior pinned physical evidence (same-assistant development, not new independent review)

[Research-only PR #87](https://github.com/physicsvigilante/opticsim/pull/87) at head 6822c110997bfd70ac9dae7ad96d76b144f6d3b8 conducted **80 synthetic actual native scenes / 160 actual native executions** across v5 planar, v7 circle, v8 triangle and v9 quadrilateral; 71 completed, eight incomplete (trapped circle TIR), one failed. Two observed v9 exact-computed critical same-ray interactions conflict with an independent *exact represented binary64* line reference on their actual incident faces:

1. Translated v9 run: reported native short hit **0.000168931960388 mm**, while exact represented intersection is at the start (t=0), below the untouched 1e-6 mm native cutoff; native run failed for an additional observer ambiguity.
2. Rotated-37° v9 run: reported native short hit **0.000582185612597 mm**, while the exact represented intersection is **behind** the incoming ray start (t≈−4.2871338283e−7); native run **completed**. Hence completion alone can overstate the reliability of native-derived v9 measurements.

[PR #87 GitHub CI 43750460379](https://github.com/physicsvigilante/opticsim/actions/runs/43750460379) and [raw research artifact 14176101242](https://github.com/physicsvigilante/opticsim/actions/runs/43750460379/artifacts/14176101242). The original 80-case physical scope and first answers were not altered to make this feature easier.

**Important**: this is a represented ray/finite-edge geometric inconsistency, not proof of which real optical critical-limit branch ought to occur, a universal Glass bug, complete path reconstruction, or authorization to fix pinned PhyDemo.

## New PR #88 shadow evidence and negative history

The test-only new experiment generates **24 existing-v9 synthetic configurations** (20 exposed PR #87 critical stress cases plus four normal-incidence controls), **two real native executions each**, plus **16 additional alternating canonical and read-only-observer native repeats** at the two exact-critical configurations. The second-level exact reference demands independently checked forward progress **and exact finite-segment parameter u**, not only supporting-line intersection.

**Final pinned HEAD CI:** [unified workflow 43753292106](https://github.com/physicsvigilante/opticsim/actions/runs/43753292106) and the ten sibling GitHub Actions: **11/11 workflows passed, 750/750 Node tests**, 24 authored cases, **64 actual native executions**, 55 exact finite-hit event checks, one unknown near-vertex event correctly withheld, and actual rotated native run with two contradictory hits withheld in the *SHADOW* result only. [Raw study artifact 14177321360](https://github.com/physicsvigilante/opticsim/actions/runs/43753292106/artifacts/14177321360), GitHub ZIP SHA-256 **5a1ceda61fe4d33158049ccc8705f46d79dea8f51ee45739182a8715d2e896e1**; Chat A downloaded/rehashed the ZIP and inspected input.json/report.json. Existing native canonical public outcomes **were not changed by this research**.

**Preserve all original research negatives** rather than reporting first-time green:
- First [unified run 43752308258](https://github.com/physicsvigilante/opticsim/actions/runs/43752308258) **FAILED**: one v9 exact-critical ordinary/extra-observer native status disagreement; preserved [artifact 14177015738](https://github.com/physicsvigilante/opticsim/actions/runs/43752308258/artifacts/14177015738).
- Second [unified run 43752585277](https://github.com/physicsvigilante/opticsim/actions/runs/43752585277) **FAILED**, retaining detailed original vs observed native event evidence; [artifact 14176609234](https://github.com/physicsvigilante/opticsim/actions/runs/43752585277/artifacts/14176609234).
- Third [unified run 43752839859](https://github.com/physicsvigilante/opticsim/actions/runs/43752839859) **FAILED** under the earlier incorrect inter-run parity assertion; its [artifact 14176908008](https://github.com/physicsvigilante/opticsim/actions/runs/43752839859/artifacts/14176908008) adds independent repeated plain-native executions. **Even without extra instrumentation**, the same translated physical input alternated between 3-hit completed and 4-hit failed; the same rotated input completed with 4–6 actual interface hits. Run-to-run **native critical numerical variability** is now **observed**, not a hypothetical. The precise cause (native global state, timing/order, JS optimization, numerical conditioning, or wrapper influence) remains unknown.

The corrected shadow test **does not** insist that two separate exact-critical runs follow an identical trajectory, nor does it call an unqualified actual native run 'completed' by changing it. It judges only the event stream *actually captured in that run*, preserving inter-run discrepancies. **A passing shadow test does not prove read-only wrapper behavior-neutral under exact-critical sensitivity** or production safety.

## Proposed physical and evidence semantics to challenge

- First production applicability **only** to existing v9 convex four-vertex homogeneous Glass with 1–4 exact SingleRay sources, 0–2 passive external detectors. No other schema or native physics change.
- At each actual native Glass onRayIncident, capture **real pre-mutation incoming JS ray p1/p2** and engine incident point, identify a **unique finite face** outside existing 0.01 mm vertex ambiguity and within pre-existing 1e-5 mm residual. Test exact represented binary64 rational **positive forward**, step strictly beyond the untouched native minimum segment cutoff, and **exact finite edge u between 0 and 1**.
- **Contradiction** -> refuse v9 native-dependent measurement qualification with machine reason while preserving truthful native terminal status. **Unknown/instrumentation/cap/ambiguity** -> withhold for insufficient evidence without accusing native optics of an observed defect. **Clean** -> necessary finite-forward consistency only, not proof of complete physical correctness. Potential first-release limit 128 actual Glass incidents per run, fail-closed after overflow without stopping propagation.
- Proposed mandatory safety gate changes previously qualified v9 readouts in narrowly demonstrated cases. **Production output publication across checker, CLI, browser, exports and Session A→B→A is UNIMPLEMENTED** and needs separate authorization/R2 code review.
- A physically trapped circular TIR with native truncation is not the same defect, and an exact critical angle by itself cannot be used as a refusal rule. No nudge, snapping, branch rewrite, threshold lowering, alternate colorMode, or independent rays invented.

## Targeted independent Chat B questions

1. Is a mandatory v9 numerical-consistency gate warranted, or should an unproven observer-neutrality guarantee force an **opt-in diagnostic-only** first release?
2. Does the **exact native incoming ray + unique finite edge + exact rational forward/cutoff/u** rule provide a conservative necessary condition? What positive small-step/near-vertex/finite-endpoint counterexamples would falsify it?
3. Can a **single owning callback wrapper** prove no observer-induced change when **plain native runs themselves vary** at exactly critical? Which actual independent native tests and same-run invariants must precede code?
4. What should be **suppressed, unavailable or separately raw** if native.status is completed but this necessary geometry qualification fails? Avoid leaking incomplete trusted measurements through summary.observations, detector power, interface first/face events, CLI/browser and exports.
5. Does the 128-callback cap and possible expensive BigInt work create a new silent false pass, denial of legitimate full-Fresnel scenes or browser stall? What lower-cost exact predicate, if any, is justified?
6. Do the successful controls genuinely cover behavior outside the two exposed exact-critical scenes, including 1–4 sources, detectors and Fresnel true? What residual risks require withholding rather than scope expansion?

**No new feature exists to test in production**; Chat B should inspect source and historical actual CI, challenge the design independently, and may run new test-only research if tools permit. Correct conclusion may be changes-requested or insufficient-evidence if the current evidence does not justify a mandatory gate. Do not merge PR #88 or any other PR, or change native optics.

Publish a NEW Chat B report under the central hub: **projects/opticsim/pr-88/reviews/review-01-chat-b.md**. Preserve all original failed runs and PR #87 research; a design pass would not approve future code.
