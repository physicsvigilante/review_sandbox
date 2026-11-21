# Chat B review of SIM_HEAT PR 141

**Verdict — accept the bounded offline calibration at the pinned head.** No blocking findings. The review covers an isothermal calorimeter and a single material of constant specific heat, with the same temperature endpoints and heat-transfer law in both trials.

I reviewed the six-file change in a fresh reviewer context. GitHub showed draft PR 141 open with base `095c97c035a78102b0654b85b58ade591848687e` and head `9d8a1feb7a48827a612d5cd86064a41bf8321c91`. My local source checkout was clean at that head. The packet was pinned at `d362e8924e123aadae5054a4f560225cd2804f79`. [Source diff](https://github.com/physicsvigilante/sim_heat/compare/095c97c035a78102b0654b85b58ade591848687e...9d8a1feb7a48827a612d5cd86064a41bf8321c91)

## Calibration and independent reference

The heat balance gives a single transit factor U = integral of dT/P(T) for both trials, with t = U(C_empty + m c). For the documented example, U = ln(2)/2. I computed this reference at 60 decimal digits and verified inclusion in the emitted unit interval. At each of the eight corners of the two timing intervals and the common U interval, I divided each trial time by U, solved for both capacities, and took the extrema using exact rational arithmetic. These extrema equal the tool's reported marginal endpoints exactly. For the documented example the resulting sample interval is approximately 399.53730–400.48559 J/(kg K), and the empty calorimeter interval is 19.92400–20.08684 J/K. Values of the two parameters share timing inputs and a transit factor, so independent choices from the two intervals need not form an attainable pair.

I repeated the eight-corner and reversed-order checks for a zero sample mass, exactly zero calorimeter capacity, and masses 0.4 and 0.400000000000000001 kg with exact times 1 and 1.000000000000000001 s. The closely spaced case retained a positive bounded result. Widening both times to [1, 1.1] s correctly refused unresolved positivity. Negative mass, zero slope, necessarily negative tare, partially negative possible tare, zero measured time and reversed time endpoints all refused. Both focused test modules also passed locally, five tests total, including duplicate masses and regressions for the older single-mass entry point.

## Current-head CI and replay

Both jobs succeeded. Their workflows checked out the PR head explicitly. I downloaded the archives and hashed the ZIP bytes.

- TwinBridge archive 14696013759, SHA-256 `382f17167d4932d348f10636f1d7c1951163ec0c95f060dac0e49008470f5831`. The source-head file matched the reviewed SHA. I compared the decompressed fresh output and the oracle and control JSON with the pinned held-out first output and both frozen results. All matched as parsed JSON. [Job](https://github.com/physicsvigilante/sim_heat/actions/runs/44876857408/job/136763348108) · [Archive](https://github.com/physicsvigilante/sim_heat/actions/runs/44876857408/artifacts/14696013759)
- Series archive 14696018626, SHA-256 `4671e1adf2caaa6070c7f4914114e8ccee637254d85a19f611324bb1f1c91475`. I executed the five generating CLIs in the pinned checkout. Fresh wall, revised wall, series, full-network and two-mass calorimeter outputs each matched the corresponding archived JSON object. [Job](https://github.com/physicsvigilante/sim_heat/actions/runs/44876857399/job/136763348105) · [Archive](https://github.com/physicsvigilante/sim_heat/actions/runs/44876857399/artifacts/14696018626)

The lesson's values and units agree with the independent reference. The reported native execution, native qualification, runner consumption and independent reference certification fields were all false. The reference checks an idealized offline model. No physical measurement or OpenModelica execution was performed. The source PR remains a draft awaiting owner disposition.
