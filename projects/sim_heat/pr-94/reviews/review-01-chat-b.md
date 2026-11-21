# Independent Chat B review of PR 94

**Verdict: accept for the requested offline one-body relaxation scope.** I found no blocking or major defects. I reviewed base `28471ad23c944ba182e3ec7fcb8ac8b547a19c6c` through head `2306a342137329a075786ffeaaa070970967b61e` in a fresh, owner-authorized reviewer subagent. This is independent-in-context computational review. [Pinned request](https://github.com/physicsvigilante/review_sandbox/blob/be42ee17fae3eb9a763619029dae0caee37e4a81/projects/sim_heat/pr-94/REQUEST.md) · [Source diff](https://github.com/physicsvigilante/sim_heat/compare/28471ad23c944ba182e3ec7fcb8ac8b547a19c6c...2306a342137329a075786ffeaaa070970967b61e)

## Physical reduction and admission

The authored three rod conductances are 2, 3 and 5 W/K. Conservation at their massless joint gives its temperature as (2 × 380 + 3T + 5 × 280)/10. The middle body therefore receives 3 times the joint-to-body temperature difference, or 648 − 2.1T watts. Its heat capacity is 210 J/K. At 350 K the body loses 87 W. The equilibrium is 2160/7 K and the time constant is 100 s. Each archived numerical interval contains the corresponding exact result. The study requests the middle body’s temperature and stored-energy change with SI units.

The implementation checks for a single connected transient component, exactly one body and at least one maintained bath. It calls the existing source-bound preparation path, computes the negative slope of body inflow by applying a unit increment through the whole network and applies the actual bath offsets in the same terminal order. It refuses a conductance enclosure that fails to establish positivity. The generic junction and flow operations use the assembled rod graph. [Implementation](https://github.com/physicsvigilante/sim_heat/blob/2306a342137329a075786ffeaaa070970967b61e/tools/body_relaxation.py)

## Complete archived histories

Using a separate 85-digit decimal calculation, I checked the recorded timestamps against every half-second from 0 through 500 s, the units and both array lengths. With ΔT = (290/7)(exp(−t/100) − 1), my reference is 350 + ΔT K and 210ΔT J. I compared every archived binary64 value against the analytic curve and checked the maximum discrepancy against its archived per-series radius, as rational numbers.

| Requested series | Samples | Maximum absolute discrepancy | Time of maximum |
|---|---:|---:|---:|
| Temperature | 1,001 | 2.83714 × 10⁻¹⁴ K | 134.5 s |
| Energy change | 1,001 | 9.08924 × 10⁻¹³ J | 447.5 s |

Both maxima lie within the archived radii, themselves below 10⁻⁸ K and 10⁻⁵ J respectively. I recomputed the checked-out model, study and facts hashes and matched each to both archived relaxation outputs. All four offline provenance flags are false in both.

## Alternate topology and refusal

I executed the law CLI on the pinned H1 D1 model, a single rod connecting a cold body directly to one hotter maintained bath. The physical inputs give G = 100 × 0.001/0.5 = 0.2 W/K, C = 500 J/K, equilibrium 353.15 K, τ = 2500 s and initial inflow +12 W. The returned intervals had exactly those endpoints. This exercises heating, a single bath, and a network without an internal junction. The focused test module also passed both tests locally, including refusal of a two-body network with a bath.

## CI and scope

GitHub identifies both requested runs as successful for the reviewed SHA. I downloaded both archives and matched the ZIP bytes to the pinned SHA-256 values. The TwinBridge archive contains the matching source-head record, fresh output, oracle results and refusal controls.

- H1 and study archive `da7a9865664a6c525f25884efe40fecb5da20a575ca388f6bea2648ef8ecf0ba`. [Job](https://github.com/physicsvigilante/sim_heat/actions/runs/44861860989/job/136716801143) · [Artifact](https://github.com/physicsvigilante/sim_heat/actions/runs/44861860989/artifacts/14690365861)
- N13 replay archive `2b3b8a705d1dd9931f15d3d5652803c6df29232eece0d4a17a4750d6f126657b`. [Job](https://github.com/physicsvigilante/sim_heat/actions/runs/44861861028/job/136716800956) · [Artifact](https://github.com/physicsvigilante/sim_heat/actions/runs/44861861028/artifacts/14690735094)

Acceptance covers the specified offline constant-property model with maintained baths. The exercises use illustrative inputs. Native execution, native qualification and classroom effectiveness are outside the evidence. Source merge remains an owner decision.
