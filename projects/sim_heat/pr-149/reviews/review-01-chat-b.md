# Independent R2 review of PR 149

**Verdict — accepted for bounded offline two-contact inference.** No blocking findings. A fresh Codex Chat B reviewer examined [PR 149](https://github.com/physicsvigilante/sim_heat/pull/149) at head `a17b351e0834a56a149b8eda7aa18e3b95d5395d`, parent `653d4bdb0de2b7e3049386d9883e67e1837ebe2e`, using packet `56d43aed8459136f179592dff284e8c36e46501c`. The checked-out source tree was clean. This review covers offline calculations with a known passive joint temperature and measured heat-rate magnitude.

## Identifiability and nonlinear reference

An ideal thermometer draws zero steady heat, so both segments carry the same current. With one unknown resistance per segment, the two measured endpoint temperatures determine that contact's face temperatures by integrating inward through the known materials and contacts. Dividing the residual oriented face-temperature difference by the current determines the resistance. Increasing the magnitude cools each warm-side face and warms its opposing cool-side face. Over the passive branch the inferred resistance decreases, giving marginal endpoint bounds. Both contacts must use the same current to describe one wall.

I independently inverted each layer's quadratic integrated-conductivity law using 90-decimal-digit arithmetic. The four 2 W/K reference conductances used reference temperatures 420, 370, 350 and 290 K with relative slopes +0.002, −0.003, +0.004 and −0.005 per K. At baths 430 and 280 K, probe 360 K and current 40 W, each layer has a 20 K drop centered on its reference temperature. The two contacts have 30 and 40 K drops, giving 0.75 and 1.00 K/W. The implementation enclosed both values, and reversing the complete wall exchanged their positions.

For the same wall at 37–43 W, the first contact covered approximately 0.625974–0.893809 K/W and the third 0.856903–1.165673 K/W. Every integer-current reference lay inside both reported marginal intervals in both orientations. Each interval endpoint enclosed its independent value to within 10⁻²⁴ K/W. The user documentation explicitly explains the shared-current correlation.

## Refusals and CI evidence

Five repository tests passed locally. Separate probes reproduced refusals for a rate band that crosses into negative resistance, a nonideal or unknown thermometer joint, zero or reversed rate limits, and a temperature outside the baths. The repository tests also covered a missing unknown on one side and invalid probe indices.

Both Actions runs succeeded at the reviewed head. I downloaded the ZIP bytes, recomputed SHA-256 and tested all entries' CRCs. The initial sandboxed archive request failed at Git credential-helper startup. The authorized read-only retry succeeded.

- [General offline replay](https://github.com/physicsvigilante/sim_heat/actions/runs/44881883655/artifacts/14698720397) contained four files and matched `f884c45db13ece4c9e53e2d223c42468981eee944c188d32a8821f8b60f9d0da`.
- [Series extension](https://github.com/physicsvigilante/sim_heat/actions/runs/44881883628/artifacts/14697558460) contained five files and matched `032eebb58102e1043930a68cbc5ba859a539a7fd92eb14eb9148467bbc239543`. Its 420/360/270 K fixture recorded 1/2 and 5/4 K/W, with respective face pairs (400, 380) and (340, 290) K. Native execution, native qualification, runner eligibility and independently certified reference flags were all false.

The CI fixture uses constant conductivities. The nonlinear two-contact and reversal evidence above comes from the independent local run. Source merge remains subject to owner approval.
