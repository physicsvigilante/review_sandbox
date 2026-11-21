# R2 independent review of mixed exchange at a radial shell

**Verdict — accepted for the bounded offline observer.** No blocking or major findings. Reviewed [source PR 173](https://github.com/physicsvigilante/sim_heat/pull/173), base `8b1df407721fdc242626ae85acc81490ca8eed8b`, head `43e57c28c1033222aacbe8f2aa3236880f42975e`, against the request at hub commit `dd23037a8e121e58e3e3806830d1aa9b15b943ea`.

## Balance and radius

For fixed open temperature and positive resistance R the scalar residual is T − Topen + RA f(T), where f(T) = h(T − Tair) + εσ(T⁴ − Tenv⁴). It increases strictly with nonnegative T. As area increases the surface approaches external equilibrium without crossing it, so both T and Q = (Topen − T)/R are enclosed by endpoint evaluations. Evaluating each external exchange over the full temperature and area intervals preserves the sign convention even under cancellation. With m = 1 for the cylinder or 2 for the sphere and R′ = 1/(kA), implicit differentiation yields Q′ = Q(m/r − f′/k)/(1 + RA f′). Multiplying the same factor by |Q| gives the magnitude derivative. Opposite resolved endpoint slopes certify an interior extremum. This claim requires neither a unique turning point nor a prescribed final bracket width.

I independently solved the scalar balance at 100 decimal digits with a 0.75 m cylinder, inner radius 0.1 m, outer radius 0.18 m, k = 4 W/(m K), 380 K open temperature, 0.5 K/W backing, 500 K air, h = 7 W/(m² K), 300 K enclosure, ε = 0.7 and σ = 0.0000000567 W/(m² K⁴). The source intervals contained T = 397.981514884205 K, Qair = −605.745989169568 W, Qenc = +571.894165682230 W and Q = −33.8518234873383 W. Independently differentiating the numerical root gave −5.09419015543641 W/m for signed Q. Searching 0.11 to 1 m enclosed the independently solved maximum of |Q| between 0.234626817259982511 and 0.234626817259982512 m.

## Evidence and boundaries

I verified the [CI archive](https://github.com/physicsvigilante/sim_heat/actions/runs/44908313235/artifacts/14708467201) SHA-256 `93190aaf90ccee026a6ab388c7976894d5747adb448970fc74b88d12fc27d8c9`, exact head.txt and 247 passing tests in regression.log. The archived radial JSON matched a local replay of the pinned source across every field. In a local 34-test focused run the historical pure-radiation sphere and cylinder, pure-convection stationary limits, reflector, malformed geometry, incomplete film and radius-search refusals passed. [CI job](https://github.com/physicsvigilante/sim_heat/actions/runs/44908313235/job/136858535320).

This independent Codex context assessed steady radial conduction and the specified uniform film and diffuse-gray boundary law. The archive and replay both record nativeExecuted=false and nativeQualified=false. The review grants no native qualification or source merge approval.
