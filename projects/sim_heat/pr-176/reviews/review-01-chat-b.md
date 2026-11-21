# Independent R2 review of two-environment thermal calibration

**Verdict — pass for the offline inverse at b1644ded744476b2fee49b97e863cfe3a1bdbc30.** No blocking findings. The review covers the common film coefficient and emissivity inferred from two steady observations of the same assembly. Native execution, measured calibration accuracy and source merge approval are outside this verdict.

I reviewed the four changed files from base db59710a2c2962b49efbc9c9555293d768c55ba8, the radial geometry and decimal-input helpers, and the R2 packet at hub 27feeef3a455a88d0454704a9449f24937937cd8. The signed heat balance is linear in the two unknowns once a trial's surface temperature is supplied. Factoring the common product of outer area and total thermal resistance leaves a two-by-two inverse with consistent units. Outward-positive radiation and convection can have opposite signs. Interval evaluation encloses both fourth-power endpoint values at nonnegative Kelvin temperatures. A determinant band crossing zero or an inferred parameter band extending outside its physical limits triggers refusal. This conservative test can decline to return an estimate for wide reading bands.

## Independent mixed-transfer challenge

Using the composite-wall cold port (380 K open, 0.5 K/W), I prescribed h = 6 W/(m² K), emissivity = 0.7 and sigma = 0.0000000567 W/(m² K⁴). I used two materials, with radial boundaries 0.10, 0.15 and 0.20 m and conductivities 1 and 2 W/(m K). A separate 100-digit mpmath forward root calculation used the integrated radial conduction resistance (inverse radii for a sphere, logarithmic radius ratios for a 3 m insulated-end cylinder). I balanced wall conduction against the sum of signed radiation and film transfer at the exposed area. Air/enclosure pairs were 410/285 K and 303/425 K. Each trial has both exchanges active, with their signs reversed in the second trial. The second surface is hotter than the open port.

| Geometry | Surface bands across the two trials (K) | Returned h bounds (approx.) | Returned emissivity bounds (approx.) |
|---|---|---|---|
| Sphere | 356.369703–356.371703 and 380.309337–380.311337 | 5.996835–6.003169 | 0.699639–0.700362 |
| Cylinder | 353.081097–353.083097 and 380.347857–380.349857 | 5.988734–6.011315 | 0.698691–0.701315 |

I checked the reference values against the full rational endpoints for both trial orders and geometries. The two pinned unit tests passed separately. Additional negative controls refused overlapping dependent trial bands, a negative film coefficient, negative emissivity, emissivity above one and reversed thermometer bounds. The first local test launch failed during test discovery because its temporary checkout did not survive across shell invocations. The executed checks above used a fresh extraction from the pinned git object.

## CI and provenance

I checked the successful run and job, downloaded artifact 14708872704 and hashed its ZIP bytes. SHA-256 was 5ec8f78924f4fdcfcfc9ecc2bd1443f0259d04a40e3530a407fd4fdf2dbbba38. Both the run metadata and head.txt identified the reviewed head. The archive logs recorded 251 top-level, 152 H1 and 4 analytical tests passing, and 63 adapter tests run with one skip. The viewer job step also passed. Replaying the archived pair on the pinned source reproduced the complete parsed two-environments.json including its source pins and offline status fields. No native job was run in this review. [Pinned CI job](https://github.com/physicsvigilante/sim_heat/actions/runs/44909222240/job/136861250208) · [Artifact](https://github.com/physicsvigilante/sim_heat/actions/runs/44909222240/artifacts/14708872704)