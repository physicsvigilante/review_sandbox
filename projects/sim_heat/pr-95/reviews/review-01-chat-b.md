# Chat B R2 review of per-rod thermal resistance sensitivity

**Verdict — accept the bounded offline observer at the reviewed head.** I found no blocking physics, numerical, or evidence defect. This review covers the incremental observer on the stacked base. Source merge requires a separate owner decision.

I independently reviewed [PR 95](https://github.com/physicsvigilante/sim_heat/pull/95) at head `39b9b2a940eb1df58aa3faddeb5a6d70bb9aafe4`, base `2306a342137329a075786ffeaaa070970967b61e`, against [the pinned request](https://github.com/physicsvigilante/review_sandbox/blob/716b95b48750e37a4a57f36ec0b49adde0f385ce/projects/sim_heat/pr-95/REQUEST.md). GitHub reported this pair on the draft PR. My fresh reviewer context received these coordinates and the interpreter path. This is model review with independent calculations.

## Physical and numerical check

With unit terminal throughput, conservation makes the normalized flows feasible for every positive resistance vector. The steady flows minimize the quadratic dissipation over those feasible flows. At the minimizing flow the first-order change from any conserving flow perturbation vanishes, so differentiating the minimum with respect to one resistance gives its squared normalized flow. Multiplication by the rod resistance and division by the total resistance gives that rod's fraction of dissipation. The shares sum to one. A unit temperature-drop solve yields the same normalized flows after division by its throughput. This also defines the intrinsic sensitivities when both authored temperatures coincide.

The pinned implementation computes the signed flow with the rod orientation and terminal injection with the opposite sign to incoming flow. Its square handles wholly negative and zero-straddling intervals. The fixed-point interval operations floor lower endpoints and ceil upper endpoints, and division requires an interval excluding zero. The new observer requires a positive lower bound on terminal throughput. Facts are hash-checked on both reads and the generic preparation path independently binds model, study, graph, and parameter values. I found no new topology-specific solve or native result construction. [Observer source](https://github.com/physicsvigilante/sim_heat/blob/39b9b2a940eb1df58aa3faddeb5a6d70bb9aafe4/tools/resistance_sensitivity.py)

## Independent execution

I ran the four PR regressions using the supplied interpreter. All passed, including the balanced crossbar and finite perturbations. I also generated a fresh admitted bridge from the baseline bridge model. Both terminals were at 280 K. I changed feed conductivity to 30 and outlet conductivity to 50 W/(m K), exchanged the two crossbar ports in the model and facts, and regenerated all three input identities. The facts SHA-256 was `b9a875bdba04a2c16ff4d5d8c582ab3be44ae4f371afd07539f6c352810ac559`.

For a unit left-to-right temperature drop, the independent node equations are 6u − v = 3 and −u + 7v = 1. Thus u = 22/41, v = 9/41 and R = 41/89 K/W. In feed, drain, inlet, outlet, crossbar order, the unit-throughput flows are (57, 44, 32, 45, −13)/89. I checked every reported derivative against the square of its corresponding fraction and every relative sensitivity against that square divided by GᵢR, using conductances (3, 2, 1, 5, 1) W/K. All eleven intervals, including the resistance, contained the exact fractions with widths below 10⁻¹². The exact relative sensitivities summed to one. All four offline provenance flags were false.

I then supplied the wrong facts hash and observed a hash refusal. Changing only the feed value in facts to 31 and recomputing its hash produced a binding refusal naming feed.k. A three-terminal star and the D1 transient body case both produced the two-terminal steady-domain refusal. These are observed public-entry-point outcomes.

## CI, provenance and limits

The GitHub jobs API showed success at the pinned head for every study/replay step, including the observer, and every general-conduction step, including the frozen TwinBridge comparison. I matched both unexpired artifact IDs and service-reported SHA-256 digests to the request. I verified the metadata and ran local checks; I did not independently hash the downloaded ZIP bytes. [Study job](https://github.com/physicsvigilante/sim_heat/actions/runs/44862445285/job/136718623606) · [TwinBridge job](https://github.com/physicsvigilante/sim_heat/actions/runs/44862445284/job/136718623677)

The worked wall example correctly describes a first-order fractional resistance change, and the independent zero-temperature-difference challenge supports the documented unit-drop interpretation. There is no classroom outcome measurement. This change reuses the existing offline solver and extends neither native execution nor native qualification. Frozen evidence retains its original scope. I left the source PR unmerged.
