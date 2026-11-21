# Independent Chat B review of SIM_HEAT #174

**PASS for the R2 offline calibration scope.** Reviewed head `b19119e49ee4102acfc82dd766641529778c000b` against base `43e57c28c1033222aacbe8f2aa3236880f42975e` under packet `e899042bfbf58e61e3240d0dc710ad9d065e7b1f`.

## Evidence

I downloaded archive 14708528849, computed its SHA-256 as `7de049e0037e88d21097ed52bc20f8abd1f720fb04e2d231f40ee4153372024a`, verified head.txt and read the 249-test successful regression log. Running the archived workflow's calibration command in the clean pinned source worktree produced JSON equal to the archived object, including source pins and all four false qualification/execution flags. [CI job](https://github.com/physicsvigilante/sim_heat/actions/runs/44908554202/job/136859232814) · [Artifact](https://github.com/physicsvigilante/sim_heat/actions/runs/44908554202/artifacts/14708528849)

## Independent calculation

I used 100-digit arithmetic with the composite wall cold port open at 380 K and resistance 0.5 K/W. For each sampled temperature I calculated the wall rate from the series resistance, then subtracted signed enclosure radiation to get air heat in watts and divided by outer area times the surface-to-air temperature difference. I checked all four reported intervals against 101 evenly spaced readings in each of three bands. Source inspection confirms that interval subtraction, products and division with a sign-definite denominator enclose the rates throughout the continuous band. Reusing the surface interval in the quotient can widen the reported bounds.

- Archived spherical shell, 359–361 K. At 361 K the outward wall rate was 27.1838784 W, air received −219.9043732 W and the enclosure received 247.0882517 W. The recovered coefficient was 4.9155713 W/(m² K).
- New two-layer insulated-end cylinder, length 0.7 m, radii 0.10, 0.17 and 0.32 m, conductivities 1.5 and 0.4 W/(m K). I used logarithmic layer resistances and lateral area 2π(0.32)(0.7) m². For 394–397 K, air 330 K and enclosure 500 K, the wall rate at 397 K was −18.0858173 W, the air received 2386.135065 W and the enclosure received −2404.2208823 W. The coefficient was 25.3041838 W/(m² K).
- With the same cylinder, surface 350–355 K, air 290 K and enclosure 360 K, at 355 K the corresponding values were 26.5967901 W, 84.9386546 W, −58.3418645 W and 0.9284620 W/(m² K). All radiation checks used emissivity 0.8 and σ = 5.67 × 10⁻⁸ W/(m² K⁴).

A spherical shell at 380 K with enclosure 380 K, emissivity 0.8 and air 300 K yielded the exact coefficient interval [0,0]. Separate runs refused air at a band endpoint, air strictly inside the band, reversed bounds and a strictly incompatible coefficient sign. These runs cover steady offline inference with a resolved temperature difference. Native execution and qualification remain outside this acceptance scope. No blocking findings.
