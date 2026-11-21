# Chat B review of PR #89

**Verdict — accept for the scoped offline observer.** No blocking findings. This review covers base `5734127a32b0b9d6d096ccdc264fc121d91f6c8b` through head `882cbe875d76a7d689f56dfa06d2e143d81e08fd` and the [pinned review request](https://github.com/physicsvigilante/review_sandbox/blob/29729e96adf5308e3dabb444eb7b60e984508e03/projects/sim_heat/pr-89/REQUEST.md). I reviewed the diff and exercised the clean tracked source at that head in a separate reviewer context.

## Signed flow and analytical evidence

The shared observer obtains the prepared export `rod.Q_flow`. The solver assigns it the same sign as heat entering port_a and the opposite sign from heat entering port_b. The maximum per-series enclosure ratio multiplies the frozen absolute W budget of 1e-8 W. The observer converts each emitted binary float exactly to a fraction and uses the resulting W radius for both sides of zero. Sample index times are rational multiples of stopTime/intervals on the admitted zero-start grid.

I used the pinned source facts to calculate the four flow histories independently. The bodies have equal 60 J/K capacities. Their average temperature exceeds 305 K by 10 exp(−t/60) K, their half-difference is 40 exp(−t/15) K, and the junction excess is half the average excess. With a = exp(−t/60) and b = exp(−t/15), the signed rates in W are lower −10a+80b, upper 10a+80b, link −80b and feed −20a. At 90 decimal digits, all 4,804 archived flow values agreed within their respective reported radii plus a 1e-82 W decimal comparison allowance. The maximum lower-rod centre error and its bound both round to 7.085e-15 W.

Lower samples 415 and 416 were +0.022290076078208976 and −0.002790992457355639 W. Their strict signs bracket the analytical root 20 ln(8) s between 83/2 and 208/5 s. The pinned regression that actually rewires the rod and updates its facts produced the reverse direction at the same indices. A strict-sign bracket establishes at least one passage by continuity. It cannot count every passage or resolve contacts with zero.

## Independent challenge and regressions

In a temporary reviewer-created variant I changed amber's initial temperature from 355 K to 335 K and recomputed the model, descriptor and facts pins. With blue at 275 K, the body deviations from the bath are equal and opposite throughout the transient. Heat moves between the bodies while the junction stays at bath temperature. The feed rod must carry zero throughout. The public observer reported 1,201 overlapping samples, no reversals and status `no_certified_reversal`.

All eight temperature and reversal regressions passed locally, including the wrong-kind refusal, ambiguous samples, two temperature passages, orientation swap and monotone heating control. Inspection of the extraction retained the temperature direction names, exact bounds, per-series radius and provenance booleans. The temperature rejection remains a ValueError with revised wording for an invalid mode or body.

## CI and evidence scope

Both exact-head jobs succeeded. I independently downloaded the ZIPs and hashed the bytes. The series artifact matched SHA-256 `3606588aae2b14a8b614cc19282fbb43a65ddfb0063ce9677f93ac98a342fe0d`; the reversal JSON and both temperature JSONs matched fresh local results field for field. The TwinBridge artifact matched `088eb89a9fbba9812b05b66b182e9b70c0449e389f4e9a94ef56f5878366a509`; its source-head file matched, and its decompressed candidate matched the permanent first-output archive as JSON. [Series job](https://github.com/physicsvigilante/sim_heat/actions/runs/44858717606/job/136706886945) · [TwinBridge job](https://github.com/physicsvigilante/sim_heat/actions/runs/44858717663/job/136706887044) · [Permanent archive](https://github.com/physicsvigilante/sim_heat/blob/882cbe875d76a7d689f56dfa06d2e143d81e08fd/qualification/h1_n13/heldout/first-output.json.gz).

The tested outputs retain false for native execution, native qualification, independently certified reference and runner consumption. This review exercised the offline reference only. Source merge remains an owner decision.
