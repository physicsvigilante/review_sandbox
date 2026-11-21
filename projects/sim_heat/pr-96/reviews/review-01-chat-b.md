# Chat B R2 review of PR 96

**Verdict: accept the offline finite conductivity-change bounds at `a6e667663153145782cf132f8e71a204b6326b65`.** No blocking findings. The reviewed base was `39b9b2a940eb1df58aa3faddeb5a6d70bb9aafe4` and the review packet was `19bcc9bdd43611a1c2a171534f7a671a8c507c2b`. This is an independent review in a separate agent context of the five-file diff. [Pinned source](https://github.com/physicsvigilante/sim_heat/tree/a6e667663153145782cf132f8e71a204b6326b65) · [Review request](https://github.com/physicsvigilante/review_sandbox/blob/19bcc9bdd43611a1c2a171534f7a671a8c507c2b/projects/sim_heat/pr-96/REQUEST.md)

## Variational bounds and independent exact calculation

An imposed unit current makes the old flow admissible after a single resistance changes. Its trial dissipation gives the upper resistance bound. An imposed unit temperature difference makes the old nodal temperatures admissible after a single conductance changes. Their trial dissipation gives an upper conductance bound, hence the reciprocal lower resistance bound. Normalization cancels in each rod's energy share. For positive multiplier m, both trial factors are positive throughout the physical share interval [0,1]. The implementation maximizes each linear factor over the clipped sensitivity endpoints. Division of the baseline lower resistance by the largest conductance factor and multiplication of the upper resistance by the largest resistance factor therefore preserve enclosure for either direction of change.

I independently chose an asymmetric bridge with conductances 3, 5, 7, 2 and 11 W/K (upper feed/drain, lower feed/drain, crossbar). I adapted the public bridge input topology in a temporary directory, repinned its model/study/facts, and set both physical baths to 280 K. I solved the two interior junction balances by a rational 2-by-2 determinant under normalized terminal temperatures 1 and 0. The exact baseline was 259/1017 K/W. I computed the baseline shares from squared temperature drops and each revised resistance by solving the changed equations afresh. I checked all five rods at factors 1/9, 5/2, 1, a 32-digit all-nines integer and its reciprocal. All 25 results enclosed the independently evaluated trial endpoints and revised resistance. For the crossbar, the exact revised values were 835/2993 K/W at 1/9 and 1079/4344 K/W at 5/2.

## Refusals and provenance

The four committed feature tests passed in the pinned local Python environment. Separate calls through the public prediction function refused a stale facts hash, an absent rod, a 33-digit denominator, a negative rational, zero decimal, a three-terminal star and the D1 transient case. All 25 accepted predictions retained the fresh input hashes and false values for native execution, native qualification, independent reference certification and runner consumption. The selected rod and hypothetical multiplier stay distinguishable from authored baseline properties.

## Exact-head CI and downloaded artifacts

Both jobs completed successfully, including the finite-change step in the wall job and frozen-evidence checks in general conduction. Both workflow checkouts select the PR head. I verified both artifact-to-head associations, downloaded both archives, recomputed their complete SHA-256 digests, and checked member CRCs.

- Study archive 14690053563 had 28 members and SHA-256 `a0c7e2e6d860723875eccb83e2cfa0a2a9aead240a7bb5a803b4493617e1c5c5`. I reproduced the complete parsed contents of `wall-change-bounds.json` and `revised-wall-output.json` locally from their respective source pins. The predicted endpoints enclose 1/3 and 11/28 K/W. The recomputed revised interval contains 3/8 K/W and lies inside the prediction. [Study job](https://github.com/physicsvigilante/sim_heat/actions/runs/44862754351/job/136719579292)
- General conduction archive 14690088653 had SHA-256 `3a3cef03ec4053f6ce5e1574922572226d0ca3b6946ce69e7931c8f556027d83`. Its source-head file contained the reviewed SHA alongside the fresh output, oracle and control results. [General conduction job](https://github.com/physicsvigilante/sim_heat/actions/runs/44862754426/job/136719579533)

This verdict covers the offline observer on the admitted steady, connected, two-terminal grammar. Native qualification and classroom effectiveness remain outside the evidence. No native job or source merge was performed.
