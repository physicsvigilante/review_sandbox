# Chat B independent R2 review of PR 109

**Verdict: accept the offline outer-radius sensitivity at the reviewed head.** I found no blocking findings. The PR was open and draft when checked. Source base `f23ad0a33a4f25eee411c970ce5f495aafc43ee6`, head `f17fa7d67f01bdf269423d04a5c8d4c43b271274`. [Packet](https://github.com/physicsvigilante/review_sandbox/blob/3eaed18454bbbe7e3cec7e0d8d447d58fbab855a/projects/sim_heat/pr-109/REQUEST.md) · [Source diff](https://github.com/physicsvigilante/sim_heat/compare/f23ad0a33a4f25eee411c970ce5f495aafc43ee6...f17fa7d67f01bdf269423d04a5c8d4c43b271274)

## Physics and units

For signed outward power Q, the balances are Ts = Topen − QR and Q = A εσ(Ts⁴ − Te⁴). Here R includes the released port and every layer. Vary only the outer boundary of the last layer, with fixed material, emissivity, backing law, inner boundaries, enclosure temperature and cylinder length. Then R′ = 1/(kA) and A′/A = m/r, with m = 2 for a sphere and m = 1 for the lateral surface of an insulated-end pipe. Substitution of Ts′ = −RQ′ − QR′ in the radiation balance gives Q′(1 + AhR) = Q(m/r − h/k), where h = 4εσTs³. The denominator is dimensionless, and each term in parentheses has units of inverse metres. The reported derivative is W/m. For nonzero power, multiplying by sign(Q) gives the magnitude derivative. Zero drive and zero emissivity give identically zero transfer as radius varies.

## Independent calculations and controls

I reconstructed the released cold port from the wall facts. The hot boundary is 380 K and the three rod conductances give 1/4 + 1/(1+3) = 0.5 K/W. I evaluated the spherical reciprocal-radius and cylindrical logarithmic resistances separately, solved the scalar surface equation with 95-decimal-place Newton arithmetic, and differentiated signed power by adding an imaginary radius step of 10⁻³² m. The calculation used no production solver, interval helpers or derivative routine. I checked the rational bounds against the reference before rounding for display. The two archived JSON objects also matched complete local replays.

| Case | Q (W) | dQ/dr (W/m) | d abs(Q)/dr (W/m) | Reported trend |
|---|---:|---:|---:|---|
| Archived sphere, 0.12 m | 64.09359382179 | 474.1712771921 | 474.1712771921 | increasing |
| Archived sphere, 1.4 m | 113.6883326662 | −0.7647439700549 | −0.7647439700549 | decreasing |
| Absorbing two-layer pipe, outer k = 7.6 | −67.58818749655 | −2.59932222948 | 2.59932222948 | increasing |
| Absorbing two-layer pipe, outer k = 0.21 | −63.53506608471 | 172.9292062532 | −172.9292062532 | decreasing |

Pipe radii were 0.10, 0.17 and 0.31 m, length 0.73 m and enclosure 455 K. I swapped conductivities 0.21 and 7.6 W/(m K) between the two cases. Both pipes and archived spheres used ε = 0.8 and σ = 5.67 × 10⁻⁸ W/(m² K⁴).

For the archived sphere family the independently located nonzero-power peak was at 0.9794829782137639507273984 m. At 0.979482978212763951 and 0.979482978214763951 m the respective slopes were +5.22609 × 10⁻¹² and −5.22609 × 10⁻¹² W/m, and each trend resolved in the correct direction. Changing conductivity to 2.24 W/(m K) and taking r = 1.101718320160933940 m produced a reference slope of +1.86590 × 10⁻¹⁹ W/m. The bounds enclosed it and the tool returned `unresolved`. The equilibrium and reflecting cases both returned exact zero and `stationary`. Equal consecutive radii, zero conductivity and zero cylinder length were each refused through the sensitivity entry point. All four committed tests across the sensitivity and radial-radiation modules passed locally.

## CI and scope

Both workflows explicitly check out the PR head. GitHub recorded success for the insulation job including its derivative step and the general conduction replay including frozen evidence checks. I downloaded both ZIPs and matched their SHA-256 digests against the packet and GitHub metadata. The general archive's source-head file independently named the reviewed commit.

- Insulation study archive `14691836709`, SHA-256 `69765d84c982811e8cfb6e9bf4059cc69b7e5c4ed9d1c240c2016df96e6dc24c`. [Job](https://github.com/physicsvigilante/sim_heat/actions/runs/44866171437/job/136730206170)
- General conduction archive `14692115625`, SHA-256 `11ad83ff0d74d3613f662828f986625be7436acce3fd5021ab1291eb627ed255`. [Job](https://github.com/physicsvigilante/sim_heat/actions/runs/44866171423/job/136730206103)

The examples demonstrate a local derivative under a specified load. Predicting the effect of a finite addition requires a new balance at the revised radius. This separate-context review covers offline calculation and evidence only. No native execution or classroom evaluation was performed.
