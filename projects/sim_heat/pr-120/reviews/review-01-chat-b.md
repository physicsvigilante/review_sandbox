# Independent R2 review of the radiating wall and finite phase bath

**Verdict: accept for offline calculation through first depletion.** I found no blocking defect in the reviewed change. I checked the open draft's base `e17e5bc4b6546fd900a0ebdac446e29111259e74` and head `e590b32e61cf749ae81383e07bc5a082e5149c08` against the request at hub commit `7d6e08c9714dad5d9f25453ade6128227ceda353`. I inspected the five-file diff and ran the four focused test modules on a clean checkout of that head. All 12 tests passed. This is a separate Codex reviewer context. [Source PR](https://github.com/physicsvigilante/sim_heat/pull/120)

## Independent physical checks

I used the five-rod balanced bridge in `studies/steady_bridge` (facts SHA-256 `4cc763729e8d71b0abfc0eb5d1c3cc4d08185225104af8640541adcfdbf10bbf`). The equal temperature of the arm midpoints makes the cross-link flow zero. Two 2 W/K rods in series carry 1 W/K and two 1 W/K rods in series carry 0.5 W/K. Their parallel conductance is 1.5 W/K.

I solved for signed power into the bath using 230 rational bisections on the interval between zero and G(Te−Tb). The residual was q − εσA[Te⁴ − (Tb + q/G)⁴]. I compared both ends of the independent bracket with the reported bounds. I checked the opposite named face, its temperature, the reverse sign of heat to the enclosure, first-depletion time, modeled duration, both masses and signed latent energy. I repeated each test with the bath at either terminal and at 0, 19 and 5000 s. The bath started at 305 K with 0.23 kg solid and 0.17 kg liquid, latent heat 187000 J/kg, face area 1.3 m², emissivity 0.71 and σ = 5.67 × 10⁻⁸ W/(m² K⁴).

| Enclosure | Face temperature | Heat into bath | First depletion | Signed energy at 19 s | Final solid / liquid mass |
|---|---:|---:|---:|---:|---:|
| 225 K | 252.529938 K | −78.705093 W | 403.912869 s | −1495.396770 J | 0.40 / 0 kg |
| 410 K | 399.770498 K | +142.155747 W | 302.555479 s | +2700.959184 J | 0 / 0.40 kg |

The 5000 s requests stopped the energy ledgers at −31790 J and +43010 J respectively. Equal temperatures and zero emissivity each gave exactly zero power, a 305 K face and no depletion time. The public calculation refused an unknown bath port, emissivity 1.1, zero area, zero initial solid mass and a three-terminal network.

## Remote evidence

Both Actions jobs reported success. I downloaded each ZIP separately, calculated SHA-256 over its bytes, tested all member CRCs and inspected the contents.

- Radiating replay, run 44868765414, job 136738331886, artifact 14693380186. SHA-256 `3348810cea8b069d6014136b6e1a2045951141bbdd55acf4519bc61324791ca0`. Five JSON members include the radiating result plus the wall, series, full network and revised wall results. I reproduced the entire radiating result from the pinned inputs and independently checked its bounds with G = 2 W/K. At 1000 s the 273.15 K bath still has both phases. The face is 327.887450 K, absorbed power is 109.474901 W, latent input is 109474.900621 J, and the remaining masses are 0.1722308365 kg solid and 0.4277691635 kg liquid. First depletion occurs at 1525.463819 s. [Archive](https://github.com/physicsvigilante/sim_heat/actions/runs/44868765414/artifacts/14693380186)
- General conduction replay, run 44868765413, job 136738332290, artifact 14691964697. SHA-256 `a507d385b2d8f37b49da91f92553031add0542c1e837c238fc7de15f90e04942`. The stored source head matches the reviewed commit. I decoded the 1201-time-point offline output, inspected the seven control entries and verified the 41-entry oracle result was present. Both native execution and native qualification are false. [Archive](https://github.com/physicsvigilante/sim_heat/actions/runs/44868765413/artifacts/14691964697)

The evidence covers a passive storage-free two-terminal conductor, one gray face viewing a large isothermal enclosure, and a fixed transition temperature while phases coexist. Post-depletion temperatures, native simulation and educational effectiveness are outside this verdict. Source merge remains an owner decision.
