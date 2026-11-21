# Independent R2 review of component calorimetry

**Verdict: accept the offline observer at source head `38063a51ec3a33445aea658d68e4eaadbec0ac3f`.** No blocking findings. The source base is `882cbe875d76a7d689f56dfa06d2e143d81e08fd`. I worked in a fresh reviewer context with the [pinned request](https://github.com/physicsvigilante/review_sandbox/blob/9e68d83892e2f95cf50093158592e75a2da8f6bc/projects/sim_heat/pr-90/REQUEST.md) and [PR #90](https://github.com/physicsvigilante/sim_heat/pull/90).

## Archived evidence

I downloaded both Actions ZIPs. Their SHA-256 digests matched the request in full. The N13/TwinBridge archive records this source head, 7 refusal or corruption controls, and its own oracle results. In the study archive I checked the model, study and facts SHA-256 fields in both calorimetry outputs against the pinned Git blobs. Each output identifies one isolated component containing cold and hot, and all four native, certification and runner flags are false. [Study archive](https://github.com/physicsvigilante/sim_heat/actions/runs/44859652816/artifacts/14689507127) · [N13 archive](https://github.com/physicsvigilante/sim_heat/actions/runs/44859652863/artifacts/14689227367)

The original and revised source facts give heat capacities of 500 and 1500 J/K. Their initial stored-energy balance gives a common limit of 308.15 K in both cases. For each rod I formed G = kA/L and x = tG(1/C₁ + 1/C₂) at 9375 s. To check the archived spread without sharing the CI exponential calculation, I used rational alternating Taylor partial sums of orders 39 and 40 for exp(−x/16), raised the positive interval to the sixteenth power and multiplied by 60 K. Both reported rational intervals enclosed the resulting interval.

| Study | x | Independent final spread, K (rounded) | Archived interval width, K (rounded) |
|---|---:|---:|---:|
| D2 | 5 | 0.404276819945128 | 1.13545 × 10⁻¹³ |
| D2_K2 | 10 | 0.00272399578574909 | 1.13586 × 10⁻¹³ |

Both archived maximum stored-energy residuals are zero, with radii of approximately 3.636 × 10⁻¹² J. The observer sums binary64 centres exactly as fractions and uses the sum of the per-body maximum joule error radii. It checks every sample. Its spread bounds use the individual kelvin enclosures and are conservative even if the identity of an extreme body changes. [Observer source](https://github.com/physicsvigilante/sim_heat/blob/38063a51ec3a33445aea658d68e4eaadbec0ac3f/tools/network_calorimetry.py)

## Independent component challenge

I added a separate isolated pair to a temporary copy of D2. The new bodies had capacities of 1000 and 1500 J/K, initial temperatures of 250 and 300 K, and a connecting conductance of 0.08 W/K. With freshly bound model, study and facts pins the normal observer returned the separate equilibria of 280 K and 308.15 K with the correct body memberships. I then injected opposing 1 J offsets in the two components at sample 500 of a prepared candidate. The global offsets cancel. The observer correctly refused the component imbalance with `isolated component stored-energy changes exclude zero`.

All three focused tests passed locally, including the disconnected maintained reservoir and modified-facts refusal. I used the hosted Linux output for the original nested revision descriptor as documented. This review covers offline reference observations. Native execution, independent native qualification and classroom outcomes remain outside the review. Source merge authorization remains with the owner.
