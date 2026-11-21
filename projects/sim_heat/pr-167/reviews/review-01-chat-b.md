# Independent Chat B review of SIM_HEAT #167

**Verdict — pass for the offline correlated bath-supply prediction at the reviewed head.** I found no blocking or major defect. The source PR was open and draft during review. This report grants no merge or native qualification approval.

Reviewed packet `f0a7cadce251e22aeed8dc0f46c1c5b6b54eddbe`, base `0485355c9669e8943210b1f6f009e1f0fbe734a1`, and exact head `10d2a04d22c16cf498f4e0e4428911c16eb64413`. I checked the PR metadata, the three-file diff, the exact local checkout and the offline scope. [Source PR](https://github.com/physicsvigilante/sim_heat/pull/167)

## Independent thermal challenge

I used the normal Python module CLI on the pinned three-terminal star. Its conductances are 2, 3 and 5 W/K and its baths are 380, 330 and 280 K. I specified 60 W of known uniform generation on the middle rod, leaving the warm and cool rods unknown. Reference powers of 40 and 100 W on those two rods give a joint at 325 K and bath supplies of 90, −15 and −275 W. Positive supply enters the network. This choice changes the known rod, unknown heater pair and predicted bath relative to the CI example.

For each rod, the bath supplies its conductance times the bath-to-joint temperature difference minus half its own generated power. Combining these three equations with joint energy balance gives the joint temperature in kelvin as (5340 − Qwarm − Qcool)/17 with supplies in watts. Middle bath supply is 960 − 3 times that temperature in watts. For warm readings [88,93] W and cool readings [−276,−273] W, the exact attainable middle interval is [−264/17,−240/17] W.

I executed all four combinations of measured-bath and unknown-heater order. Every CLI result enclosed both rational endpoints with less than 10⁻¹² W excess at each end. The determinants were exactly +17/40 or −17/40 with the expected permutation signs. All four provenance flags (native execution, native qualification, independently certified reference and runner consumability) were false. Changing the warm reading to [190,200] W produced the nonnegative-power refusal, nonzero exit and no JSON output.

## Source and evidence

Each new gain is a component of the target bath's unit-source row multiplied by the inverse two-reading sensitivity matrix. Subtracting the resulting weighted deficits from the known-background bath supply preserves the signed convention. The preexisting determinant guard excludes zero before division. Both interval expressions enclose the same physical quantity, so intersecting them preserves containment. Rod peaks and input preparation use their previous paths.

I downloaded and independently hashed the archived ZIP. Its SHA-256 was `9ad4667d43673eb08db2abe9082d59d3a26eadd785c4744d5207944d923a3f56`. The archived head matched the reviewed commit, the regression log recorded 238 passes, and the prediction JSON enclosed the CI example's −245 ± 2/3 W with native execution and qualification false. The pinned job checkout, offline suite, CLI replay and upload all succeeded. [Job](https://github.com/physicsvigilante/sim_heat/actions/runs/44906568186/job/136853327071) · [Artifact](https://github.com/physicsvigilante/sim_heat/actions/runs/44906568186/artifacts/14707883969)

The independent challenge exercises one fixed-property topology. General containment also relies on the upstream interval and network preparation contracts. Neither the archived replay nor my runs supply native measurements, classroom evidence or external-author qualification.
