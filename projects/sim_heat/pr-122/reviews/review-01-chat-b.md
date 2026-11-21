# Independent R2 review of SIM_HEAT PR 122

**Verdict — accept the offline inverse-balance scope at `9b874afda17f968b8ab8af9d0cb65922d854fe16`.** No blocking or major findings. The source PR was open, draft and unmerged when inspected. Merge approval remains with the owner.

I performed this review as a fresh Codex reviewer subagent under the owner's substitution for external Chat B. I worked from the review packet, pinned source and archived evidence and independently chose the numerical probes. This is model-based review. The common source base was `c914a4da93ecb6eafe70176ff0d12fcd9a0f4dd3`. [Request](https://github.com/physicsvigilante/review_sandbox/blob/eec90d4a01782fd257b8d658a3e8d3ecbdc0bbc5/projects/sim_heat/pr-122/REQUEST.md) · [Source diff](https://github.com/physicsvigilante/sim_heat/compare/c914a4da93ecb6eafe70176ff0d12fcd9a0f4dd3...9b874afda17f968b8ab8af9d0cb65922d854fe16)

## Independent physical and numerical checks

I changed the three conductances on a disposable triangle and regenerated the model, study and facts pins. Conductances from bath to surface, bath to support, and surface to support were 2, 4 and 3 W/K. With the support at 280 K and bath at T, zero bath flow gives surface temperature S = 3T − 560 and heat entering the surface from the enclosure Q = 13(T − 280) W. I used 2 m², emissivity 0.75 and sigma 0.0000000567 W/(m² K⁴). I checked each reported surface and flow interval against the exact rational result. I raised both enclosure bounds to the fourth power and compared them with S⁴ + Q/(area × emissivity × sigma) using rational arithmetic.

| Bath K | Surface K | Q W | Enclosure K, approximate | Forward checks, freezing / melting |
|---:|---:|---:|---:|---|
| 275 | 265 | −65 | 254.0759412475018 | 253 K / 255 K |
| 280 | 280 | 0 | 280 exactly | 279 K / 281 K |
| 295 | 325 | +195 | 340.5460167983933 | 339 K / 341 K |

The two nonintegral enclosure intervals were each 10⁻¹⁸ K wide. At 150 K the surface would be negative and the solver refused. At 275 K with emissivity 0.001 the fourth power would be negative and the solver refused. Removing the direct bath-to-surface rod left the maintained support between them. The solver refused this case at both 275 K (unsatisfiable) and 280 K (no unique enclosure).

I also injected broad response-coefficient intervals at the terminal-response interface to exercise uncertainty propagation separately from source ingestion. At T = 300 K with support at 280 K, bath-to-surface coupling in [−3,−2], bath-to-support in [−5,−4], surface diagonal in [5,7] and surface-to-support in [−3,−2] W/K, all 16 endpoint combinations fell within the reported surface, power and enclosure bounds. Moving the upper bath-to-surface coupling to zero produced a refusal. The 11 pinned inverse, supported-bath, radiating-wall and radiating-surface tests also passed locally.

## CI evidence

- The wall job succeeded. I downloaded artifact 14693166225 and verified SHA-256 `673b6d9d7188ea7264f7db961db0a652cec31112b6df2206749f7b9bccfb9077`. Regenerating the star result reproduced the archived threshold JSON, including source hashes and all four false qualification/execution flags. Its surface and heat bounds enclose 350 K and +100 W, with an enclosure temperature of approximately 362.2017035894 K. [Job](https://github.com/physicsvigilante/sim_heat/actions/runs/44869343765/job/136740119930) · [Artifact](https://github.com/physicsvigilante/sim_heat/actions/runs/44869343765/artifacts/14693166225)
- The general conduction job succeeded. Artifact 14692184833 had SHA-256 `5b1b2296ed196ca29f16e49b8f05115af3b3e293cae7311eff201fb5519729be` and contained the reviewed source SHA. Its decompressed output, oracle results and seven control results matched the corresponding frozen JSON records. I reran the pinned TwinBridge checker on the archived output and reproduced its oracle summary. [Job](https://github.com/physicsvigilante/sim_heat/actions/runs/44869343755/job/136740119295) · [Artifact](https://github.com/physicsvigilante/sim_heat/actions/runs/44869343755/artifacts/14692184833)

These checks qualify the stated offline calculation and evidence at this head. Native OpenModelica execution, independent certification of a production reference, source-image interpretation and classroom effectiveness are outside this review.
