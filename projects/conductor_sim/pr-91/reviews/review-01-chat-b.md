# Independent Chat B review 01 — conductor_sim M38a / PR #91

**Verdict: PASS (bounded M38a scientific / geometry / SI / typed-evidence boundary).**

This is a **reviewer-authored independent first-attempt native execution**, not a developer CI endorsement. Production PR #91 must remain **OPEN, DRAFT and UNMERGED** until separate owner approval. No production files, commits, reviews, or workflows were changed by this review.

## Frozen target and proof of source identity

| Item | Literal identity |
| --- | --- |
| Production PR | https://github.com/physicsvigilante/conductor_sim/pull/91 |
| Candidate HEAD | `b482aaab716bbfb5a06984d4e8678707c5235d15` |
| Actual native Git TREE | `7873a982c19f597bde4cad205d4f39ba199d5038` |
| Released M37b base | `f187dede846d441dd5928ccb6521d67443ead72b` |
| Prespecified charter | `docs/m38a_charter.md`, originally frozen in `1eaf5286ad6ebc58e86c45d613aeda518072e8fc` |
| Reviewer-run workflow | https://github.com/physicsvigilante/review_sandbox/actions/runs/44375948929 |
| Reviewer first-attempt evidence artifact | `m38a-chat-b-pr91-first-attempt-independent-evidence`, artifact ID `14461875544` |

A fresh GitHub Actions Ubuntu 24.04 runner checked out the **literal candidate commit**, asserted both `git rev-parse HEAD` and `git rev-parse HEAD^{tree}`, and separately checked out the exact released M37b base. It found exactly **seven new files** and zero changes to existing files. Direct `cmp` checks confirmed the PDF and M37a/M37b observer, radial source, and model files byte-identical to the released base. Consequently the existing original-question viewer JavaScript/SVG was not modified. The production PR HEAD was rechecked after the native run and remained the pinned SHA, still draft/unmerged.

## True native execution: one reviewer-owned attempt, successful

The independent workflow was authored and pushed in **review_sandbox**, not in production. It ran to completion on its **first attempt**, with every step successful. The reviewer-generated workflow and probes are separately inspectable:

- [Reviewer-owned workflow](https://github.com/physicsvigilante/review_sandbox/blob/review/conductor-sim-pr91-chat-b-01/.github/workflows/m38a-pr91-chat-b-review01.yml)
- [Reviewer-authored native scientific and hostile probes](https://github.com/physicsvigilante/review_sandbox/blob/review/conductor-sim-pr91-chat-b-01/projects/conductor_sim/pr-91/reviews/review-01-chat-b-probes.py)

After `python -m pip install -e ".[test]"`, the actual `python -m pytest tests/test_m38a_prescribed_line.py -q` produced **56 passed** on Python 3.12. The real `python examples/m38a_line_approach.py --output ...` produced the 41-row teacher case. Then `python -m tools.m38a_line_reference --input ... --output ...` genuinely executed the developer-provided, stdlib-only oracle and reported **41 independently checked Kelvin states, zero newly solved original-workbook items**.

**Crucially, the reviewer did not stop there:** a separately written test script recalculated, without importing the project physical solver or reference formula code, every position, actual time, distance, radial velocity, signed terminal current, charge, force vector and half-factor mechanical energy directly from the electrostatic constants and the analytic line. This separately checked **41 original teacher example rows**, **23 novel noncoplanar reversed-charge rows**, and **13 M37b radial-special-case rows**, plus other geometric cases. Differences outside the declared numerical tolerances would have failed the workflow.

First-run logs, the real 41-sample JSON, stdlib oracle, reviewer-authored JSON outcomes and hashes are retained as the Actions run artifact. Neither an unsigned arbitrary historical file nor the production oracle was represented as an external authenticity signature.

## Physical and SI results

For one grounded **solid** sphere, source `q`, sphere radius `a`, centre `c`, and prescribed `x(t)=x0+v*t`, the independently derived quantities used were:

```text
r = x(t) - c; d = |r|; v_radial = (r·v)/d
Q_sphere = -q*a/d
I_sphere_to_ground = -q*a*(r·v)/d^3
I_ground_to_sphere = -I_sphere_to_ground
F_source = [-k*q^2*a/(d^2-a^2)^2] * r
U_induced_mechanical = -k*q^2*a/[2*(d^2-a^2)]
k = 1/(4*pi*permittivity)
t_closest = clamp(-((x0-c)·v)/|v|^2,0,T)
```

For the real example `q=+1e-9 C`, `a=0.1m`, `x0=(-0.4,0.2,0)m`, `v=(0.2,0,0)m/s`, `T=4s`:

| t (s) | d (m) | Conventional sphere-to-ground current (A) |
| ---: | ---: | ---: |
| 0 | 0.4472135955 | +8.94427190999916e-11 |
| 2 | 0.2 | 0 |
| 4 | 0.4472135955 | -8.94427190999916e-11 |

The zero is **net wire current**, not a claim that local surface charge stops redistributing. Force remains strictly radially **attractive** for either source charge sign. The induced **mechanical** interaction energy includes the necessary factor `1/2`. This is a quasistatic Kelvin observation at externally imposed positions; no Newtonian path integration is claimed.

The independently invented unfamiliar case had `c=(0.75,-0.45,1.2)m`, relative `x0-c=(-0.4,0.26,0.18)m`, `v=(+0.19,-0.06,+0.04)m/s` (all three components nonzero), `q=-1.7e-9 C`, `epsilon=1.3 epsilon_0`, `T=3.6s`. It returned physical closest `t=2.0435835351089593s`, `d=0.2958404124469879m`. Independent SI recomputation confirmed the entire 23-row history and the sign reversal from `-1.0822593488317941e-10 A` initially to `+1.3451994095170082e-10 A` finally. Reversing `q` reversed both current terminal signs but preserved force and energy. The original radial M37b observer agreed on all 13 independent radial rows.

## Continuous guard and hostile integrity attacks

The deliberately hidden crossing used `x0=(-0.4,0.05,0)m`, `v=(0.2,0,0)m/s`, `T=4s`, `a=0.1m`, guard `0.01m`, and **four** stored frames. Every saved frame was safe (`d = 0.4031128874, 0.1424000624, 0.1424000624, 0.4031128874 m`), but the continuous closest point at `t=2s` is `d=0.05m`: **the new native typed constructor rejected the entire path** for the intended continuous-path reason. Exactly tangent and numerically unresolved barely-tangent cases also refused; a demonstrably separated near-tangent path was accepted and recomputed. Closest-approach minima at `t=0` and at exact interval endpoint `t=T` were both checked.

The reviewer injected **20 independently authored hostile or geometric refusal cases** into genuine JSON-decoded lists/dicts or native typed objects. Actual rejection reasons were checked, not merely arbitrary exceptions:

- Boolean `false` at time zero and index zero; wrong sample order/index.
- Forged positive and negative terminal current, reversed charge sign, force component and half-factor mechanical energy.
- Forged Cartesian position, continuous closest time and distance.
- Fabricated SI unit, workbook-source attribution, grounded constraint and solid-metal status.
- `dataclasses.replace` false native result and export, rejected by actual native re-execution.
- `object.__setattr__` mutation of nested frozen source charge to Boolean, rejected when the spec was revalidated.
- Hidden between-frame crossing and unresolved tangencies.

This is **not** a claim that arbitrary JSON has a cryptographic origin guarantee. It shows strict physical/type/provenance consistency checks in the supported native authoring/export and stand-alone numerical checking boundaries.

## Source attribution, scope, and outstanding gates

The original physical p8 Multiple Correct Q21 is a **radially approaching** positive charge at externally maintained small speed. Its original answer remains M37b. The new off-axis line is consistently marked `teacher_hypothetical_off_axis_transfer_not_original_workbook_p8_Q21`; it adds **zero** original JEE problems to the coverage count. No new browser, electromagnetic transient solver, resistive-wire field, radiation model, nonconservative current law, or integrated orbit was introduced.

I did **not** rerun original M37b browser/FEMM suites as part of the independent reviewer run: the seven-file additive diff and byte-for-byte protected baseline comparisons place them outside this narrow review. Separately, the developer's **24/24 exact-SHA CI runs** (22 PR plus two push, including historical Chromium/FEMM) were inspected as developer preflight, **not** substituted for this independent native review. The preserved earlier red developer CI attempts are development history, not this review's first-run result.

**Blocking findings: none. Required source changes: none. Optional future milestone:** a separate M38b viewer should honestly depict the 3D off-axis geometry and synchronized time-dependent current; it should not relabel M37b's original radial picture.

**PASS applies only to the literal HEAD `b482aaab716bbfb5a06984d4e8678707c5235d15` and TREE `7873a982c19f597bde4cad205d4f39ba199d5038`.** It is **not** merge permission. Keep production PR #91 draft/open/unmerged until owner explicitly authorizes release. Then guard merge by expected head, verify the merged `main` source tree matches the reviewed tree, and require real postmerge `main` CI. Any changed candidate SHA/tree requires an appropriately scoped re-review.
