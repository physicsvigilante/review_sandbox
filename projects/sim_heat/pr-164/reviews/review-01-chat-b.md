# Independent Chat B review of SIM_HEAT PR 164

**Accepted for offline prediction of unmeasured bath supplies and rod peak temperatures.** I found no blocking defect at head `fe6ed43691391a7413c473fca44707155dc61695`, reviewed against `1e99769bae1ba9de2748605d29592cc31d104efe` and hub packet `06fa88704a5891058c27d194391f6f7bbde88a13`. I performed this review as the independent Codex reviewer. [Source comparison](https://github.com/physicsvigilante/sim_heat/compare/1e99769bae1ba9de2748605d29592cc31d104efe...fe6ed43691391a7413c473fca44707155dc61695)

## Independent physics and refusals

The star givens imply branch conductances of 2, 3 and 5 W/K and a junction temperature of 315 K plus total rod power divided by 20 W/K. Each signed bath supply equals its conductance times its temperature excess above the junction, less half its own rod's power. For a rod carrying total power P, the axial temperature at fractional position x equals the linear interpolation of its end temperatures plus P x(1−x)/(2G). I checked the two end temperatures and the stationary point when interior. The archived readings give 160 and 120 W, junction temperature 329 K, cold supply −245 W and second-rod peak 334.5125 K.

I used those balances as a forward oracle with independently selected power triples (16,32,1000), (163,117,22.5) and (4,8,0) W. The third power was specified as known. For each of the three measured bath pairs the predictions enclosed the true inferred powers, the omitted signed bath supply and every rod peak. For measurement intervals of ±0.1 W I perturbed the first and second powers separately on a 17 by 17 grid with 0.05 W spacing. All 777 grid cases satisfying the measured intervals across the nine configurations had covered supplies and peaks. The 1000 W background also exercises a maximum inside the known heated rod.

The source uses the two inferred marginal power intervals conservatively. With fixed baths and positive conductances the grounded steady-network inverse is nonnegative, so an increase in any heater increases or preserves each interior temperature. The axial generation term has the same monotonicity at each position. Taking the peak at the two ordered power corners therefore encloses the maximum, including switches of its location. Signed unmeasured supply starts at the loaded background and subtracts each source's bath share. The interval can be wider than the feasible correlated range. Known background powers are single specified values.

Eight focused repository tests passed. Separate predict-mode calls refused a reversed signed interval, duplicate bath, overlapping known and unknown rod, and observations incompatible with nonnegative powers. The inherited tests also checked indistinguishable source partitions. My first test command lost a sandbox temporary export between invocations and failed at module import. I reran the tests and independent checks in the clean, verified source checkout.

## CI and evidence

Both workflow runs reported success at the exact reviewed head. I downloaded each archive and recomputed its SHA-256.

- Series artifact `14700152475` matched `2b72949d08c2e4fe7c9a826fe2e1e7841e165afe3966c32ae9580d72150a10ee`. I regenerated all five JSON files through their respective CLIs and compared the full decoded outputs, including the new prediction, pins and offline qualification flags. [Series CI](https://github.com/physicsvigilante/sim_heat/actions/runs/44886169941)
- TwinBridge artifact `14700286824` matched `5f9e62b0e2c073e4a6a1f68f3e36cfc5431523344bce4ec3dcc98e0ee0eb930f`. Its source-head entry matched the pin. I regenerated the full held-out conduction output, ran the independent oracle against the archived output, and ran the negative controls. Each decoded result matched both the archived and frozen record. [TwinBridge CI](https://github.com/physicsvigilante/sim_heat/actions/runs/44886169918)

The evidence covers steady, uniform volumetric heating in the admitted offline network. Native execution, native qualification and experimental validation were outside the accepted scope. The source checkout was clean and PR 164 was open, draft and unmerged at verification.
