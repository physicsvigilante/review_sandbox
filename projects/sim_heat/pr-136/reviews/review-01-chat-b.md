# Independent targeted Chat B review of SIM_HEAT PR 136

**Accept the offline lesson guard.** I reproduced the PR 133 finding and verified its correction against source head `d4e1425699296095c4a870e14cc06587912a8682`, base `2d061edc4114851d94bcb4d2cb197946e1054be6` and hub packet `c2b46641fca1f2d76921025a1878b4e7db7e0862`. The diff changes the worked-answer checks, their regression test and the two CI workflow selections. [Pinned source comparison](https://github.com/physicsvigilante/sim_heat/compare/2d061edc4114851d94bcb4d2cb197946e1054be6...d4e1425699296095c4a870e14cc06587912a8682)

## Reproduction and regression

I ran the lesson guard from PR 133 head `d04bc85bcb33660fcc129468f3008a6dc8d1c275` against four replay results with the left insert overwritten to [0, 0] W. It accepted all four. On PR 136 I corrupted one channel in one case at a time. All 40 mutations raised ValueError, covering four contact temperatures, four signed contact currents, 24 rod currents and eight retained-bath supplies. The candidate's four focused unittest methods also passed, including the wrong-sign, overly wide and reversed-endpoint controls. [Prior finding](https://github.com/physicsvigilante/review_sandbox/blob/c2b46641fca1f2d76921025a1878b4e7db7e0862/projects/sim_heat/pr-133/reviews/review-01-chat-b.md)

## Physics and signs

The source gives 4 W/K for the facing and parallel conductances of 1 and 3 W/K for the strip and insert. The insert's port order reverses its reported flow. For each wall the three signed flows are therefore +m, +m/4 and −3m/4 for current magnitude m under the lesson's contact-release convention. Hot retained baths supply +m and cold retained baths supply −m.

Both constant controls yield 330 K with signed contact currents of +100 and −100 W. The dissimilar forward case yields 340 K and +120 W. For reverse drive the rise above 280 K satisfies x² + 640x = 32000, giving x = √134400 − 320. The magnitude m = 2(100 − x) therefore satisfies m² − 1680m + 168000 = 0. This polynomial decreases throughout [0, 200] W, so the sign inequalities bracket the physical root. I checked every genuine interval against the independently evaluated analytical values using 100-digit decimal arithmetic and exact rational endpoints, including the reverse interface near 326.606055596467 K and contact current near −106.787888807066 W. All bounds contained the reference and met the width limit of 10⁻¹⁰ in the reported units. All four cases retained their offline flags.

## Exact-head CI archives

- Series job 136757254742 succeeded. I verified the run-to-head mapping and recomputed ZIP SHA-256 `4b28722d1e34b3943d5f88c3a80e2b4618b10a4b1385deda54ec12a2d6b97166`. The archived four-case lesson matched my fresh local replay as parsed JSON. [Job](https://github.com/physicsvigilante/sim_heat/actions/runs/44874871585/job/136757254742) · [Archive](https://github.com/physicsvigilante/sim_heat/actions/runs/44874871585/artifacts/14695721466)
- TwinBridge job 136757255089 succeeded. I verified the run-to-head mapping and recomputed ZIP SHA-256 `f027826316a196f2400704d6ea5b2841a248ca9959141ffbae67dc6a74a79a2e`. The source-head file identifies the candidate. The decompressed fresh output, oracle results and control results each matched the corresponding preserved held-out JSON at that head. [Job](https://github.com/physicsvigilante/sim_heat/actions/runs/44874871652/job/136757255089) · [Archive](https://github.com/physicsvigilante/sim_heat/actions/runs/44874871652/artifacts/14695054796)

This verdict covers the targeted offline regression. Native execution and classroom validation remain outside its scope. Source merge requires the owner's separate decision.
