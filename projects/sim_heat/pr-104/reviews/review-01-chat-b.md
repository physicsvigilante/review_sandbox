# Chat B targeted R2 review of PR 104

**Accept the signed-power enclosure correction at `f2fd86455d682e7e127585cb5b47c1fb0ddeb3a8`.** I found no blocking defect in the bounded offline calculation. GitHub showed an open draft against `020e123b7a94b4aa103ae335b813f3a957b8b9cc`. I reviewed the pinned packet in a separate model context. [Source diff](https://github.com/physicsvigilante/sim_heat/compare/020e123b7a94b4aa103ae335b813f3a957b8b9cc...f2fd86455d682e7e127585cb5b47c1fb0ddeb3a8) · [Request](https://github.com/physicsvigilante/review_sandbox/blob/e00919af4dcb560ab6a17103d7e02f262de97930/projects/sim_heat/pr-104/REQUEST.md)

## Reproduction and independent balance

My first history check assumed the PR 101 and PR 104 base surface modules were byte-identical. That assertion failed before any physics checks ran. The intervening refactor extracted the physical-port calculation. I then executed both historical module blobs with the pinned checkout's dependencies. Their full results agreed for all three wall inputs.

Releasing the cold face leaves a 380 K bath and a series resistance of 1/4 + 1/(1+3) = 1/2 K/W. For net outward power q the face temperature is T = 380 − q/2. I evaluated the signed residual q − εσA(T−E)(T+E)(T²+E²) with exact rational arithmetic at each reported endpoint. This function increases with q on the physical branch. Its opposite endpoint signs certify containment independently of the temperature bisection.

For E = 999999999999 K, A = 1 m², ε = 1, σ = 0.0000000567 W/(m² K⁴), both historical modules returned approximately [−1.2294853 × 10²², 0] W. The candidate gives a lower endpoint of exactly −1999999999238 W and a width of 1.0842022 × 10⁻⁷ W. Both endpoints are negative and bracket the energy balance. Results for the ordinary 280 K and 450 K cases were exactly equal as parsed objects across all three implementations, with signed powers near +12.15844249 and −16.57910373 W.

## Interval uncertainty and controls

For open temperature U, surface T and positive resistance R, the physical power is (U−T)/R. Subtracting the endpoint intervals outward and taking the extrema of the four quotient corners encloses every allowed conductive power, even when the numerator crosses zero. Nonnegative absolute temperatures and εσA make the radiation expression monotone in T. Both intervals therefore contain the same physical power and their intersection contains it. Shared uncertainties may widen the result. This argument gives containment without a uniform precision guarantee across the whole input grammar.

I injected U ∈ [299,301] K and R ∈ [1/3,7/4] K/W at the physical-port boundary. With A = 3 m², ε = 0.7 and the same σ, I checked 45 exact signed residual brackets, using three environments, three resistances and five open temperatures including 300 and 300 ± 10⁻¹⁸ K. Approximate reported power intervals were [26.0411,111.5792] W at 250 K, [−2.4321,2.4330] W at 300 K and [−132.9053,−27.2335] W at 350 K. These synthetic checks exercise the interval calculation. The wall comparisons exercised the original study entry point. All 11 repository surface, gap and shield tests passed locally with Python 3.13.5, including reflection, equilibrium and invalid-exterior controls.

## Exact-head CI and evidence limits

Both pull-request runs succeeded at the reviewed head. I downloaded both ZIPs, recomputed SHA-256, checked ZIP integrity and inspected their contents.

- Study replay archive SHA-256 `a5b3b2c451b00e08ead4d76f2ae4ae8668a9de9b7b3d931d2629de568821ce15`. All three archived single-surface JSON objects matched my local runs exactly. Each reports false for native execution, native qualification, independent reference certification and runner consumption. [Job](https://github.com/physicsvigilante/sim_heat/actions/runs/44864757798/job/136725831410) · [Archive](https://github.com/physicsvigilante/sim_heat/actions/runs/44864757798/artifacts/14690594216)
- Frozen replay archive SHA-256 `dd564cdcb0553eed9fd87bc182ab0d727119d26b75350ce44f692d61548523a8`. Its source-head member matched the reviewed SHA. The fresh output, control results and oracle results matched the three corresponding frozen records after JSON decoding. [Job](https://github.com/physicsvigilante/sim_heat/actions/runs/44864757753/job/136725830945) · [Archive](https://github.com/physicsvigilante/sim_heat/actions/runs/44864757753/artifacts/14691611057)

The evidence covers a steady offline calculation. Native radiation execution and educational or classroom outcomes remain unverified. Source merge requires a separate owner decision.
