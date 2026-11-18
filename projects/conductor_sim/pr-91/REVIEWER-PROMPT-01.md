# Independent reviewer prompt #01 — conductor_sim M38a / PR #91

**Request issued only after all exact-HEAD developer preflight CI passed.**
This document is an author-prepared request, **not** an independent review or a PASS.

## Exact source target and review boundary

- Production draft PR: https://github.com/physicsvigilante/conductor_sim/pull/91
- Exact reviewed candidate HEAD: \`b482aaab716bbfb5a06984d4e8678707c5235d15\`
- **Actual native Git TREE:** \`7873a982c19f597bde4cad205d4f39ba199d5038\`
- Release base \`main\`: \`f187dede846d441dd5928ccb6521d67443ead72b\` (M37b merged and postmerge 22/22 SUCCESS; same independently reviewed source tree \`44b754e005c3d720cb3e59c1debd363ca2d8d639\`)
- Frozen preregistered charter BEFORE code: \`docs/m38a_charter.md\`, committed at \`1eaf5286ad6ebc58e86c45d613aeda518072e8fc\`.
- Developer exact-head preflight **24/24 COMPLETED SUCCESS**: 22 pull_request + 2 push, including Python 3.10/3.12, real FEMM5 and retained source/Chromium visualization. Dedicated 3.10 and 3.12 focused source tests each showed **149 passed**, all 41 physical example states checked with an independent **stdlib-only** Kelvin reference. The first genuine red development CI attempts are preserved; they were fixed in subsequent commits (test-function syntax, mutation of tuple rather than JSON-decoded arrays). None is evidence of an independent PASS.
- Production PR #91 must remain **DRAFT, OPEN, UNMERGED**. No owner authorization to merge M38a has been granted. **Do not merge** or modify production PR source.

Use a **fresh exact-SHA checkout** and verify native \`git rev-parse HEAD\` and \`git rev-parse HEAD^{tree}\`; check the PR head has not moved. Enumerate the diff from the exact released M37b base: it should contain only the **seven new M38a files** (frozen charter, new module, reference oracle, test, example, docs, workflow); the original workbook PDF, M37a native Kelvin model, M37b radial source and original Chromium viewer must remain byte-identical. Do not review code from a moving branch name and claim that it is the pinned head.

## Scientific question and important source-honesty distinction

The **original** \`02_conductors_half_size.pdf\` physical p8 Multiple Correct Q21 is a positive charge moving **radially toward** a grounded sphere at **externally maintained constant small speed**. Its original options (1),(3), source geometry and attribution were independently reviewed/released in M37b; **do not repeat the full original-p8 or Kelvin/browser review if those files remain unchanged.**

M38a is a **new teacher-authored off-axis physical extension**, not a second original workbook problem or a higher JEE-30 coverage score. A point charge travels at **constant 3D Cartesian velocity** along a prescribed straight line past one stationary grounded *solid* metal sphere. The supplied path requires an **unspecified external actuator**; it is **not a free Newtonian orbit**, moving conductor, resistive-wire response, microscopic surface current, radiation or fully time-dynamic Maxwell simulation.

Independently derive, with \`r(t) = x0+vt-c\`, \`d(t)=|r(t)|\`, \`a\` sphere radius, \`q\` source charge:
\`\`\`
Q_sphere(t)             = -q*a/d(t)
v_radial(t)             = (r(t) . v)/d(t)
I_sphere_to_ground(t)   = -q*a*(r(t) . v)/d(t)^3
I_ground_to_sphere(t)   = -I_sphere_to_ground(t)
F_source_radial(t)      = -k*q^2*a*d(t) / (d(t)^2-a^2)^2
U_induced_mechanical(t) = -k*q^2*a / (2*(d(t)^2-a^2))
k = 1/(4*pi*permittivity)
t_closest = clamp( -[(x0-c).v]/|v|^2, 0, T )
\`\`\`
For positive q, approach gives **positive** sphere-to-ground *conventional* current; exact tangential passage has **zero net ground-wire current** (without implying no local surface redistribution); recession makes it negative. Check force is always radially attractive, and the interaction energy includes the factor **1/2**. M37a/M37b public observer semantics are unchanged.

## Must execute and independently challenge (do not just read author CI)

1. **Fresh actual native execution**: install the project on a clean checkout and run \`python -m pytest tests/test_m38a_prescribed_line.py -q\`, \`python examples/m38a_line_approach.py --output review-outputs/m38a/line.json\`, then \`python -m tools.m38a_line_reference --input review-outputs/m38a/line.json --output review-outputs/m38a/oracle.json\`. Independently recompute at least several actual JSON rows without importing any production physics and validate all 41 when feasible. Check actual reported initial/end current signs, exact closest distance 0.2m at physical time 2s, ordinary physical source dimensions and honest teacher labels. Re-execute source reference code in the production checkout only as one supporting check—not as your independent mathematical derivation.
2. **Unfamiliar genuine 3D case**: invent a physically admissible off-axis trajectory with **nonzero x,y,z velocity components**, a translated or rotated sphere centre, ideally nonzero q with reversed sign. Create it with the public model and M38a authoring APIs; check every actual distance/time/velocity and Kelvin scalar current/sign and force direction by a separate calculation. Verify unchanged baseline and radial special-case agreement with M37b where applicable.
3. **Continuous hidden-crossing attack**: construct a path where start/end and **every stored sample** are outside the sphere+guard, but the line between frames intersects metal/guard. Suggested seed x0=(-0.4, 0.05,0)m, v=(+0.2,0,0)m/s, T=4s and **only four saved frames** with sphere radius 0.1m and guard 0.01m. Check refusal uses actual continuous closest approach, not a test-only trap or sample-only scanning. Independently vary closest point to near-tangent, just-clear, and to exactly start/end of interval. Do not accept numeric uncertainty as a safe trajectory.
4. **Hostile data and authoring integrity**: challenge genuine JSON and native typed runs by changing (separately) zero timestamp to Boolean \`false\`, sample index, signed terminal current, charge sign, force, energy, 3D coordinate, exact closest time/distance, SI unit, \`source_role\`/original-p8 attribution, and physical status. Confirm **the actual native validator or separate stdlib reference rejects each for the intended physical/type/provenance reason**, not unrelated harness errors. Include one attack on a nested typed spec using \`object.__setattr__\` after construction and one on a \`dataclasses.replace\` fake result. Construct **valid JSON-decoded list/dict attacks**; do not falsely count Python tuple immutability as validator rejection.
5. **No unsupported scope creep**: confirm no new browser viewer; M37b original SVG/JavaScript source bytes untouched. No force law or Euler/RK integration added. Source PDF unchanged. Off-axis data remain teacher cases, never silently counted as official JEE answers. The output is not externally cryptographically signed; native re-execution and a standalone SI recomputation do not prove arbitrary historical provenance.

Retain independently generated first-attempt logs and actual output/forgery evidence, with SHA/TREE. You may use a reviewer-owned fresh GitHub Actions workflow in \`review_sandbox\` with exact checkout and explicit fail-fast; **do not rerun developer CI and call that alone an independent review**. The review is a **single narrow scientific/typed-authoring/evidence boundary**, not a general conductor/FEMM/Chromium recertification. Only expand scope if novel evidence exposes a cross-boundary defect.

## Verdict and separate release gate

Publish \`projects/conductor_sim/pr-91/reviews/review-01-chat-b.md\` in \`physicsvigilante/review_sandbox\`, preferably as a review-sandbox PR. Include literal exact HEAD/TREE, true independent execution and first-run evidence, typed/numerical/JEE-source observations, reproducible unfamiliar attacks, and one of:

- **PASS** — no remaining scoped scientific/geometry/SI/provenance blocker.
- **CHANGES REQUESTED** — precise reproducer, severity and corrected expected behavior. Keep old red report historically; after source correction use one **targeted re-review** only of affected boundary, reusing unchanged physics evidence.

Reviewer PASS is **not merge authority**. Production PR #91 stays DRAFT/UNMERGED until the owner explicitly approves, then an expected-HEAD guarded merge, exactly matching source Git TREE on \`main\`, and real postmerge \`main\` CI all succeed. If PR HEAD or tree has changed, do not issue a PASS for the old head.
