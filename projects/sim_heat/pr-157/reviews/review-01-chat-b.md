# Independent R2 review of SIM_HEAT PR 157

**Verdict.** Accept the offline finite-body target-time and pathway-energy calculations at `ccc3ea256a3e2f1123379a72ae777b5d196f349d`. I found no blocking issue in the reviewed scope. The source PR was open and draft against `5a43df5821389472681a4724443e7557134158a1`. I reviewed as a separate Codex Chat B against packet `dd8fe19ec2d5e2c7d9a864a6288f6f6d68a5e72b`. [Pinned source](https://github.com/physicsvigilante/sim_heat/commit/ccc3ea256a3e2f1123379a72ae777b5d196f349d)

## Independent calculations

I integrated the temperature and all three signed energy rates as four time-domain states with SciPy DOP853, relative and absolute tolerance 1e-12, and a terminal target-temperature event. Each independent time and each energy fell within its reported interval. Positive energy enters the body. In all rows the heat capacity is 100 J/K, the wall bath is 380 K, and the film conductance is 2 W/K.

| Conditions | Time (s) | Rod (J) | Air (J) | Radiation (J) |
|---|---:|---:|---:|---:|
| 430 to 395 K, air 400 K, radiation disabled | 51.986039 | −2789.720771 | −710.279229 | 0 |
| Archived 430 to 400 K case, air 400 K, enclosure 410 K, two black shields | 35.591811 | −2194.034537 | −770.362097 | −35.603366 |
| 330 to 390 K, air 450 K, enclosure 360 K, two black shields, conductivity slope +0.002/K about 300 K | 32.062370 | 895.473381 | 5285.245234 | −180.718615 |

The linear cooling case also agrees with the exact time of 25 ln(8) s and signed film energy of 20 times the time in seconds minus 1750 J. In the warming case, both radiation and conduction reverse during the trajectory. I used rod power 2(380−T)[1+s((380+T)/2−300)] and shielded radiation power (410⁴−T⁴)/300000000 for the archived enclosure, replacing 410 by 360 for warming. The three independently integrated energies sum to the body's storage change within 1e-8 J in each case.

Passive rods with positive conductivity, a nonnegative film coefficient and grey radiation give decreasing net heating power. This justifies the endpoint test in either direction. The panel bounds include all four signed flux and residence-time endpoint products, including a reversal within a panel. Subtracting the upper and lower bounds of both external pathways in reverse order encloses conduction by energy conservation.

## Controls and evidence

From 430 K, equilibrium at 390 K, a target beyond it at 385 K and a target in the wrong direction at 435 K all returned unreachable with null time and energy. An initial target at 430 K returned exact zero for time and all three energies. The focused suite passed all 11 tests, including film arity, zero area, and negative coefficient refusals. Omitting the film reproduced the base implementation's returned objects for the linear case and both shielded cases. Setting the film coefficient to zero preserved the tested cooling times.

Both pinned GitHub Actions jobs succeeded. I downloaded each ZIP, recomputed SHA-256 and checked every member's CRC. The twin-bridge archive has four members and digest `c34230c529a63f4e96756f7b638fbfc0f8be2ffdad30d9a0c99e13ee1ba96ad8`. The series archive has five members and digest `80bcca51dd04205d8cfdefe71fe8bfb8dd47e1c9ec3dc2379155558d5a86edd5`. On replay the complete mixed-body JSON object equaled its archived counterpart, including source identities and all four false execution/qualification flags. The first replay could not open the archive member via the sandbox's private temp directory. Reading the downloaded member at its actual location completed the comparison. [Twin-bridge CI](https://github.com/physicsvigilante/sim_heat/actions/runs/44884428886) · [Series CI](https://github.com/physicsvigilante/sim_heat/actions/runs/44884428815)

The complete top-level Linux suite and the Windows replay job were skipped by their branch conditions. Full Windows discovery on the head produced 4 failures and 19 errors. Separate clean archives of the base (213 tests) and head (216 tests) produced the exact same failing and erroring test/subtest names, all in authoring workbench and source preview. Each new test passed. This review covers offline result semantics only. Native OpenModelica execution and qualification remain outside the evidence.
