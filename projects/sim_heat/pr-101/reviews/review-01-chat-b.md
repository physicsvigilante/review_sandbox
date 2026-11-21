# Chat B review of PR 101 — one radiating surface

**Verdict: accept the bounded offline calculation at the reviewed head.** No blocking findings. The two archived wall solutions satisfy independent signed energy balances. A numerical precision limitation at extreme inputs is detailed below.

Reviewed source base `b2c053d4ca4fdbecf3ddd56a11fcff2be771d670`, head `e29fbae050e6b0c3a3739d1f6c0cd983f31e0976`, and packet `6d99465e95cfaf03d348993fdde28082976f6cee`. GitHub reported the PR open and draft. This was a separate model context working from the packet and pinned source. [Source diff](https://github.com/physicsvigilante/sim_heat/compare/b2c053d4ca4fdbecf3ddd56a11fcff2be771d670...e29fbae050e6b0c3a3739d1f6c0cd983f31e0976) · [Request](https://github.com/physicsvigilante/review_sandbox/blob/6d99465e95cfaf03d348993fdde28082976f6cee/projects/sim_heat/pr-101/REQUEST.md)

## Physics and interval construction

The retained baths feed a passive linear network. For its released port the supplied heat is (Topen − T)/R in watts. A single uniform diffuse gray face with view factor one to a large isothermal enclosure exchanges εσA(T⁴ − E⁴) watts with that enclosure. This assumes absolute kelvin, exposed area in square metres, a transparent medium, insulated other faces and zero convection. The documented positive direction agrees with energy leaving the network. The supplied σ is an explicit exercise input.

Write c = εσA. The balance F(T) = T − Topen + Rc(T⁴ − E⁴) has derivative 1 + 4RcT³ ≥ 1 for T ≥ 0. Its signs at E and Topen bracket its unique physical root. The root increases with Topen. At fixed Topen the derivative with respect to R has the sign of E − T, so changing R moves the root monotonically toward E. This justifies the four corners even when the Topen interval crosses E. Positive-conductance bath extrema also enclose Topen. Exact rational bisection preserves inclusion and the outward radiation law is monotone on this domain. I checked 27 interior (Topen,R) combinations against four-corner brackets spanning 280–330 K and 1/3–7/5 K/W, for E equal to 279, 316 and 450 K.

## Independent challenges and refusals

I released the triangle's **cool** port. Its two incident rods give heat supply (380 − T) + 1.5(330 − T) W from kA/L in the pinned facts, hence Topen = 350 K and R = 0.4 K/W. The third rod connects the two maintained baths. I used area 0.033 m², ε = 0.65 and σ = 0.000000056704 W/(m² K⁴). For each returned rational bracket I checked both residual signs with the independently factored fourth-power difference, equality of its radiation endpoints to the published power endpoints, and overlap with the conduction power interval.

| Enclosure K | Surface K, rounded | Heat to enclosure W, rounded |
|---:|---:|---:|
| 125 | 343.35665923 | +16.60835192 |
| 515 | 374.63972263 | −61.59930657 |
| 350 | 350 exactly | 0 exactly |

The nonzero triangle intervals were narrower than 1.3 × 10⁻¹⁷ K and 2.5 × 10⁻¹⁸ W. Independent refusals covered negative emissivity, exponential temperature syntax, unknown port and incorrect facts hash. The seven checked-in radiation and loaded-port tests passed locally on Python 3.13.5, including zero emissivity, equal temperatures and invalid exterior inputs.

For the manufactured case, the wall conductances are 4 W/K in series with parallel 1 and 3 W/K rods, giving R = 1/2 K/W. At 200 K the conducted heat is 2(380 − 200) = 360 W and the radiated heat is 4.5 × 0.00000005 × 200⁴ = 360 W to the 0 K enclosure. The exact target is enclosed by both reported intervals in the executed test.

## Exact-head CI and archived replays

I checked both successful jobs, downloaded both ZIPs, computed SHA-256 and checked ZIP integrity. The radiation job ran the inherited H1 baseline, wall checks and focused radiation step. Several historical branch-specific study steps were skipped. The general replay job passed its frozen-evidence, regression and TwinBridge checks. Its archived source-head file matched the candidate, and its seven control results include refusal of a Modelica radiation constructor.

- [Radiation job](https://github.com/physicsvigilante/sim_heat/actions/runs/44864070253/job/136723696843) and [archive 14691196475](https://github.com/physicsvigilante/sim_heat/actions/runs/44864070253/artifacts/14691196475), SHA-256 `fd7c4ddb94c5febb55ca1f76ec0d967a33d6b505535f9466e0e6783e131996bf`.
- [General replay job](https://github.com/physicsvigilante/sim_heat/actions/runs/44864070246/job/136723696842) and [archive 14690967350](https://github.com/physicsvigilante/sim_heat/actions/runs/44864070246/artifacts/14690967350), SHA-256 `a1b053b1f4077f9b28cf6ba2fd92cca5275b29abc3d95c52ca2bdc7568a675b7`.

Both archived radiation JSON objects matched my local replay in every field. Checking 2(380 − T) against 0.016σ(T − E)(T + E)(T² + E²) at the exact archived endpoints bracketed zero residual. At 280 K I found 373.9207787541 K and +12.1584424918 W. At 450 K I found 388.2895518649 K and −16.5791037297 W.

## Limits of acceptance

Fixed 64-step bisection gives a temperature-width guarantee per corner. It gives no uniform absolute power precision across the entire decimal grammar. For example, the wall with E = 999999999999 K, A = 1 m², ε = 1 and σ = 0.0000000567 produced roughly [−1.23 × 10²², 0] W. The conductive balance limits the physical rate to roughly −2 × 10¹² W. This extreme input illustrates a valid but uninformative bound. The documented wall study and the independent triangle challenges had narrow bounds. No accuracy target over the entire grammar was claimed.

All four execution, qualification, independent-reference and runner flags were false. This review covers the single steady offline load under the stated enclosure assumptions. No native job, physical measurement, classroom evaluation or independent requalification of the inherited TwinBridge trajectory was performed. Source merge remains an owner decision.
