# Chat B independent review of PR 161

**Verdict.** Accept the offline steady powered-wall calculation at head `f27153065c4ee4a5766aa7b8417356b29f74bafa` relative to base `7b24f37ea9e21a080590c605cef162f9e68b12b8`. No blocking findings. Request packet `8a3d31445320df88fb1d90461fc540a1d1780357`. This is a separate reviewer context. Native execution, physical measurements and classroom evaluation are outside the evidence. Source merge remains an owner decision.

## Independent calculation

I released the middle terminal of the pinned three-terminal star. Conductances from warm, middle and cool to the junction are 2, 3 and 5 W/K. I applied 100, 120 and 80 W uniformly to the three rods. Warm and cool remain at 380 and 280 K. With middle temperature T, the junction balance gives J = (2310 + 3T)/10. Power supplied to the surface is 60 + 3(J − T) W. Consequently the open temperature is 2510/7 K.

For area 1 m², emissivity 1, sigma 1e−9 W/(m² K⁴), enclosure at 300 K, air at 338.90625 K and film coefficient 1 W/(m² K), the exact loaded temperature is 350 K and J is 336 K. Radiation and convection carry 221/32 and 355/32 W outwards. Maintained supplies are +38 W at warm and −320 W at cool. Their sum with 300 W generation is 18 W, equal to the total exterior loss.

I checked each rod's quadratic profile using linear interpolation of its endpoints plus P x(1−x)/(2G), with x measured from its bath end. Warm, middle and cool peak temperatures are 380, 350.45 and 336 K, at fractions 0, 0.15 and 1. Every reported interval for these quantities, the source-shifted open temperature, surface, junction and signed powers contained its exact target with width below 1e−12 in the reported unit.

The pinned focused unittest replay passed 13 tests. It includes opposing convection and radiation, the insulated limit and a zero-source comparison. Independent invalid-input probes refused a wrong facts hash, a junction named as the released port, duplicate source rods, negative power and an unpaired air parameter.

## CI provenance

Both GitHub run records reported success on the exact reviewed source head. I independently hashed each downloaded archive and checked all ZIP member CRCs.

- [General-conduction run 44885449962](https://github.com/physicsvigilante/sim_heat/actions/runs/44885449962), artifact 14700011386, SHA-256 `0286761626aa00756a985a7109f7c5f68ba7b4af307cec9f9bd8b07bed3e43c9`. Four members cover control results, fresh compressed output, source head and oracle results.
- [Series run 44885450024](https://github.com/physicsvigilante/sim_heat/actions/runs/44885450024), artifact 14699357824, SHA-256 `21bde1b36dd93c490b205030bbad60f2a13b12500f0d4e5ad8307ded73fefced`. Five members include the powered-wall result. Its open interval is exactly 420 K, its surface bracket surrounds 400 K, and its native-executed and native-qualified flags are false.
