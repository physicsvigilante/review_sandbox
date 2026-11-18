# M36b PR #85 — Independent R2 source-JEE physical replay and honest visualization review

**Production target (DRAFT / OPEN / UNMERGED):** https://github.com/physicsvigilante/conductor_sim/pull/85

- **Exact candidate commit:** `5cfa02c2b22ad1d488778653d63f54b4f9a06d1d`
- **Actual native Git TREE:** `3db298498bdd30b701ced59d3952eb529e835add`
- **Released M36a main/base:** `4e5fd2044a171bc889edf626f2c7795e15d5188c`, tree `fff1c03417c857b6cce04156427e3eeaf9919a65`
- **Charter frozen before implementation:** `6e3be20c83a26318b3b5147268e545a338fa71fb`
- **Risk:** R2 — genuine native original-problem physical observation, independent numerical-reference claims, display truthfulness; no production field law changed.
- **Review purpose:** certify a **bounded pilot** of seven preselected original JEE physical apparatus (three actual elapsed-time trajectory cases and four static-observer cases), plus one explicit unsupported local 3D cavity case. These are *not* 7 out of 30 random solved exam prompts nor automatically LLM-parsed problems.

## Full source to examine

[Preregistered M36b charter](https://github.com/physicsvigilante/conductor_sim/blob/5cfa02c2b22ad1d488778653d63f54b4f9a06d1d/docs/m36b_charter.md) · [candidate methods/limits](https://github.com/physicsvigilante/conductor_sim/blob/5cfa02c2b22ad1d488778653d63f54b4f9a06d1d/docs/m36b.md) · [native-source runner](https://github.com/physicsvigilante/conductor_sim/blob/5cfa02c2b22ad1d488778653d63f54b4f9a06d1d/tools/m36b_jee_replay.py) · [NO-production-import reference checker](https://github.com/physicsvigilante/conductor_sim/blob/5cfa02c2b22ad1d488778653d63f54b4f9a06d1d/tools/m36b_jee_reference.py) · [actual Chromium inspector](https://github.com/physicsvigilante/conductor_sim/blob/5cfa02c2b22ad1d488778653d63f54b4f9a06d1d/tools/check_m36b_jee_browser.py) · [new adversarial regressions](https://github.com/physicsvigilante/conductor_sim/blob/5cfa02c2b22ad1d488778653d63f54b4f9a06d1d/tests/test_m36b_jee_replays.py) · [full source-pinned workflow](https://github.com/physicsvigilante/conductor_sim/blob/5cfa02c2b22ad1d488778653d63f54b4f9a06d1d/.github/workflows/m36b-jee-source-replays.yml).

Read [M36a original 30-case matrix](https://github.com/physicsvigilante/conductor_sim/blob/5cfa02c2b22ad1d488778653d63f54b4f9a06d1d/docs/m36a_jee30_coverage.json) and [teaching evaluation contract](https://github.com/physicsvigilante/conductor_sim/blob/5cfa02c2b22ad1d488778653d63f54b4f9a06d1d/docs/evaluation_contract.md). The original scanned source PDFs are checked into conductor_sim; their frozen SHA-256s are in M21a/M36a. Where possible reopen the actual original PDF page and diagrams, not just the earlier author's summary. Never claim newly visually inspected pages if tool limits prevent it.

## Preselected source-backed observed systems and independent challenge

1. `p02-single-19` workbook scanned p2 Q19: original 100eV electron, charged metal surface `sigma=-2e-6 C/m2`. Actual one-sided E and **native** velocity-reversal event, distinct terminal early encounter. Independently derive `E=sigma/epsilon0`, `v=sqrt(2K/m)`, `s=K/(e|E|)`, signed acceleration, event times and noncollision bounds. Teacher adds start clearances. Test what occurs if the source field sign or a native event time is forged.
2. `p03-single-30` workbook p3 Q30: symbolic electron transit between ideal biased plates from rest. Native first terminal upper event and energy `eV`; use `t=sqrt(2 m d^2/(eV))` for disclosed illustrative d=.01m and V=100V. Do not infer postimpact interaction.
3. `p05-single-47` workbook p5 Q47: rigid dipole starts parallel to uniform E; static four *illustrative* angles. Independent `Delta U=pE(1-cos theta)` and torque/finite endpoint consistency. A true static orientation observation is **not an elapsed-time rotation**, and source gives neither inertia nor numeric initial angular state.
4. `p12-linked-40` workbook p12 Q40: two stationary charged rings (+10/-20 microC, .30m radius, separation .40m), +10microC probe, uniform E up 1e5V/m. Independent axial potential/endpoint work `~3.5950207 J`; upward qE is real **1 N transverse force** but does zero horizontal endpoint work. Must not invent a free axial trajectory under upward force.
5. `p15-archive-02` workbook p15 IIT-JEE 2012 proton released from rest between **vertical** parallel plates: simultaneous horizontal qE and downward mg. `qE=mg` yields 45 degree acceleration and voltage `~1.04375e-9 V` for explicitly rounded constants. Review **actual multiple saved native time states, electric/gravity force and kinetic energy**, preview ends before plates.
6. `p02-single-15` workbook p2 Q15: far-separated connected conducting spheres under explicit `self-capacitance-leading-order`, `Q_i proportional R_i`, `E1/E2=R2/R1`, group-charge conservation. This is two **static** equilibria, no exact mutual induction or wire current. Its R/d admission threshold is heuristic, not a proven physical relative error bound.
7. `jee2021-p1-q09-q10-equipotential`: official 2021 Paper 1 Q9+10 **ONE** fixed charge-pair apparatus. Do not accept an analytically drawn circle pasted over unrelated viewer: inspect actual numerical zero-volt contour segments, source positions/masks. Independently verify `(x-3)^2+y^2=3`; Q=1nC added by teacher, no moving body.
8. `p70-three-cavities`: source apparatus intentionally **REFUSED** for local nonconcentric 3D sigma/E; Gauss totals alone do not qualify local distribution. An honestly reported refusal is not an eighth success.

## Developer's initial literal source execution (NOT independently authored review)

[First exact-head M36b workflow #44243111752](https://github.com/physicsvigilante/conductor_sim/actions/runs/44243111752) completed **SUCCESS**, at the pinned source SHA on push. Its job log records **14 new focused tests PASS**, **seven real source native observations exported**, **seven separately expressed standard-library physical checks PASS**, and **seven actual real offline Chromium viewer checks PASS**, with retained screenshots/JSON/CI results. Artifact ID `14400163983`, provider-reported ZIP SHA-256 `bdf2310cc3d534d4d702504b8f6b06cdae713f83443107e82c009ad73e3b807f`; ZIP not independently downloaded or rehashed by author. This is *developer-controlled acceptance*, not independent Chat B science or visual expert signoff.

**Full source-head PR and push CI must be independently rechecked LIVE.** When this request was authored, associated Python 3.10/3.12, dedicated real FEMM5, all inherited Chromium and scientific workflows were still running/queued; do not count them green in advance. The older historical M36a postmerge main push was **15/15 all actual main workflows SUCCESS**; this is not a substitute for PR #85 CI.

## Original independent reviewer obligations

- Verify exact HEAD, actual Git TREE, base and source diffs. If changed, stop as **STALE-HEAD**; do not review moving main as candidate.
- Invent **new** out-of-sample source-preserving physical variations (e.g. sheet electron energy or surface sigma change, dipole angle and field reversal, independent ring analytical endpoint, proton mass/charge revision, signed far-sphere charge sharing); execute original new tests against actual supported engine APIs where possible, not merely check the author's hard-coded expected numbers.
- Verify real native time states, event termination, root time, force vectors and energies, and independent numerical/mathematical expressions. For static sources, validate actual observer data and never call it elapsed-time dynamics.
- Attack manifest tampering, fake event/energy data, changed source labels/given-vs-teacher provenance, fake analytically drawn circle and unsupported 3D pass. Detect overclaims of universality or textbook completeness. Reviewer should examine actual browser screenshots/HTML where available; differentiate automated label checks from visual legibility/educational usefulness.
- Check *all* current-head Python 3.10/3.12, **real FEMM** and complete historic **Chromium** jobs (not skipped tests). Check actual new dedicated replay/reference/browser workflow logs and hashes. If any required CI cancelled, failed or incomplete, no PASS.
- Publish an original report to `projects/conductor_sim/pr-85/reviews/review-01-chat-b.md` with verdict **PASS / CHANGES-REQUESTED / INSUFFICIENT-EVIDENCE**, original tests and clear evidence status. Distinguish a separate GPT context from independent human scientific certification.

Do not modify source production, mark PR ready, merge or grant owner authorization. Only after a genuine exact-head scoped PASS, still-green CI and **separate explicit owner approval** may Chat A expected-head merge and verify actual main source tree/postmerge workflows.

**Important denominators:** seven apparatus replayed (3 dynamic plus 4 static), seven separate authored analytic checks and seven browser openings; one deliberate refusal. This is a *selected seven-appartus pilot*, **not a measured 7/30 or 24/30 JEE solve percentage**. Original 30-case cohort remains provisional pending broader case-by-case validations.
