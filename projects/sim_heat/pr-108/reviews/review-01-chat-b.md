# PR 108 independent R2 review

**Verdict — accept the offline radial-radiation scope at `f23ad0a33a4f25eee411c970ce5f495aafc43ee6`.** I found no blocking discrepancy in the coupled balance, sign, profile, enclosures or evidence. GitHub reported PR 108 open and draft, based on `493af36ef95f945a0ae3891f3191554c11572ea9`. I reviewed in a fresh Chat B context using the pinned packet and clean source checkout. [Source PR](https://github.com/physicsvigilante/sim_heat/pull/108) · [Review request](https://github.com/physicsvigilante/review_sandbox/blob/cea2c2bd713da2693cb1ad2f1d8406dd1552132a/projects/sim_heat/pr-108/REQUEST.md)

## Energy balance and outward bounds

The inputs describe steady radial conduction with perfect contact and one exterior facing a large isothermal enclosure. Only the cylinder's lateral area participates. Each shell resistance and the backing resistance carry the same signed rate. For nonnegative temperatures the scalar residual increases strictly with surface temperature. The root increases with open temperature and moves toward enclosure temperature as resistance or emitting area grows. At fixed open temperature and resistance the rate varies monotonically with area, with direction set by the hot side. This justifies evaluation at the bounding areas, including uptake from a hotter enclosure. Intersecting conduction and radiation bounds retains the common rate. Interval subtraction of each upstream drop and division by the area at each radius enclose the local values.

I independently bisected in heat rate, substituting the conductive surface temperature into the emitted power, using 110-decimal-digit arithmetic and 350 subdivisions. For each case I checked containment of the rate, exposed area, every layer resistance, every surface temperature and local outward flux against the reported rational endpoints.

| Case | Outward rate (W) | Outer surface (K) | Quantities enclosed |
|---|---:|---:|---:|
| Archived emitting sphere | 98.49456998237758 | 291.5629708077962 | 10 |
| Archived absorbing cylinder | −101.4874670415526 | 447.5375446697903 | 10 |
| New three-layer absorbing cylinder | −16.2498087087678 | 320.1238964218834 | 13 |

The new case released the middle port of the three-terminal star. Its 2 and 5 W/K arms maintain 380 and 280 K, yielding an open temperature of 2160/7 K. Its 3 W/K middle arm gives a backing resistance of 1/3 + 1/7 = 10/21 K/W. Radii were 0.073, 0.089, 0.137 and 0.210 m, conductivities 3.7, 0.83 and 1.2 W/(m K), length 0.63 m, enclosure 327 K, emissivity 0.37 and sigma 5.67e−8 W/(m² K⁴). All four offline provenance flags were false in all three cases.

## Controls and inherited behavior

A reflecting pipe facing 820 K and a unit-emissivity pipe facing its 380 K open temperature both returned exactly zero rate and flux and exactly 380 K at every radius. Eleven negative requests refused a stale facts pin, unknown port, zero inner radius, empty layers, 33 layers, equal successive radii, zero conductivity, negative enclosure temperature, emissivity above one, zero sigma and zero cylinder length. All 13 local tests across the radial-radiation, radiating-surface, spherical-conduction and cylindrical-conduction modules passed.

## Exact-head CI archives

Both GitHub jobs succeeded at the reviewed head. I downloaded both ZIPs, independently hashed their bytes and parsed their contents.

- The radial archive matched SHA-256 `1488a9fc3d616f7c937b4e67595a03257da828f814aeb99abcc0105fcb412be1`. Both archived worked examples matched fresh observer JSON in full, in addition to the independent physical checks above. [Job](https://github.com/physicsvigilante/sim_heat/actions/runs/44865783919/job/136729002553) · [Archive](https://github.com/physicsvigilante/sim_heat/actions/runs/44865783919/artifacts/14692060879)
- The general-conduction archive matched SHA-256 `9469f2488ea3c5cebc9ce7f5747cd80c0b7315578e97ba076adce5c676d68c74`. Its embedded source head matched the PR. The decompressed replay, oracle results and control results each matched the corresponding frozen JSON in the pinned checkout. [Job](https://github.com/physicsvigilante/sim_heat/actions/runs/44865783857/job/136729001823) · [Archive](https://github.com/physicsvigilante/sim_heat/actions/runs/44865783857/artifacts/14691384015)

This verdict covers the offline observer and the reviewed source revision. Native execution, qualification and classroom outcomes are outside the evidence reviewed. Source merge requires a separate owner decision.
