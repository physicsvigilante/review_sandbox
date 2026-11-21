# Independent Chat B review of SIM_HEAT PR #87

**Verdict — pass for the illustrative offline steady bridge.** Both junction temperatures, the signed transverse flow and the effective resistance reproduce at the pinned head. I found no blocking discrepancy. The source PR was open and draft at review time.

I reviewed head `72b78aeef1e0fbd57b31876f3d92934de0b95790` against its parent `cc34d0e026358f7631044bd7eca7db127a5efc5e` from the separately supplied packet. The diff adds the case, tests and offline CI wiring. The two Modelica files have identical connections and rod geometry. The single physical revision doubles feed conductivity from 20 to 40 W/(m·K). I checked the authored inputs, revision bindings, test and workflow diff, and matched 185 relevant checkout text files against pinned Git blobs with checkout line endings accounted for. [Packet](https://github.com/physicsvigilante/review_sandbox/blob/fdf1d0679080197a3314e1ac680105d13bf15d23/projects/sim_heat/pr-87/REQUEST.md) · [Source](https://github.com/physicsvigilante/sim_heat/tree/72b78aeef1e0fbd57b31876f3d92934de0b95790/studies/steady_bridge)

## Independent calculation

I opened the transverse link analytically. Let a,b and c,d be upper and lower arm conductances from hot to cold, and h the link conductance. The open-link upper-minus-lower temperature difference is 100[a/(a+b) − c/(c+d)] K. The heat rate on closing the link equals this difference divided by 1/h + 1/(a+b) + 1/(c+d), in K/W. Thus equal arm ratios balance the bridge even when their absolute conductances differ. Applying the resulting signed heat rate to each midpoint and summing the two hot-terminal contributions gives the following predictions.

| Inputs | Upper (K) | Lower (K) | Upper to lower (W) | Hot / cold supply (W) | Resistance (K/W) |
|---|---:|---:|---:|---:|---:|
| Baseline | 330 | 330 | 0 | +150 / −150 | 2/3 |
| Doubled upper feed | 345 | 335 | +10 | +185 / −185 | 20/37 |

## Execution and challenges

Both committed bridge tests passed locally, including refusal of baseline facts for the revised study. In temporary baseline-derived cases I recomputed every file binding and exercised the same offline preparation entry point.

- With feed and inlet conductivities set to 40 and 20 W/(m·K), respectively, the two arm ratios are both 2. Both computed midpoints matched 1040/3 K and the transverse flow was exactly 0 W.
- With feed reduced to 10 W/(m·K) and inlet at 10 W/(m·K), the lower node was hotter. The predicted upper and lower temperatures were 3480/11 and 3580/11 K. The returned flow was −9.090909090909092 W, agreeing with −100/11 W. Temperatures and flow agreed to within 1e−12 in their respective SI units.
- Swapping only the link endpoints in the facts and supplying a freshly computed facts hash caused both temporary cases to refuse with `reference_binding: reference physical connectivity differs`. The erroneous orientation did not pass through hash renewal.

## Hosted evidence and claim limits

I verified both GitHub job conclusions, head-bound artifact metadata and downloaded ZIP byte hashes. All four archived bridge JSON documents matched the entire local preparation or resistance result after JSON parsing. Both resistance intervals collapsed to the exact fractions tabulated above. All four outputs reported false for native execution, native qualification, independent reference certification and runner consumption. [Bridge CI](https://github.com/physicsvigilante/sim_heat/actions/runs/44856879122/job/136701033512) · [Bridge archive](https://github.com/physicsvigilante/sim_heat/actions/runs/44856879122/artifacts/14687677406)

- Bridge ZIP SHA-256 `e5c5d095101ad0319ba78a9f07a392562a8d699c9c453141b53f799485d389d9`.
- Inherited N13/TwinBridge ZIP SHA-256 `4797533f237020a1df37c59c1963fc8f147a0273d83665d3ce94d5a97950b7be`. The archive contains the pinned source head, controls, oracle and compressed output. Its scope is inherited regression coverage. [TwinBridge CI](https://github.com/physicsvigilante/sim_heat/actions/runs/44856879126/job/136701033315) · [TwinBridge archive](https://github.com/physicsvigilante/sim_heat/actions/runs/44856879126/artifacts/14688047631)

The authored physical data are illustrative and the repository identifies its checking transcription as same-author. My separate calculation checks these specific offline predictions. The case supplies a prediction exercise with a worked revision. Classroom effectiveness and native execution of this bridge remain untested. This report confers no source merge approval.
