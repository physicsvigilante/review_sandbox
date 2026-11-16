# Independent R2 review — conductor_sim M28b, PR #66 — Chat B / review 01

**Verdict: CHANGES-REQUESTED (two demonstrated release blockers).** This is a separate-context, adversarial review of a frozen snapshot, not the implementer's assessment. Neither source PR #66 nor source main was changed, approved, or merged.

| Field | Reviewed value |
| --- | --- |
| Project/source | [physicsvigilante/conductor_sim](https://github.com/physicsvigilante/conductor_sim) |
| Source PR | [draft #66](https://github.com/physicsvigilante/conductor_sim/pull/66), open and unmerged when checked twice on 2026-11-16 |
| Base SHA | abb085d41399b0a17429aa207614aad357ccd77c |
| **Exact reviewed head** | **414e69bd960bc71f3df65c7346e81bf58c1540b8** |
| **Exact source tree** | **ac06b4990b8002394fa7965fa2391eda8ca9f16e** |
| Reviewed diff | [base...head](https://github.com/physicsvigilante/conductor_sim/compare/abb085d41399b0a17429aa207614aad357ccd77c...414e69bd960bc71f3df65c7346e81bf58c1540b8) |
| Reviewer | Chat B, GPT-6, independent conversation (not independent human/other-model-family attestation) |
| Review date | 2026-11-16, Asia/Kolkata |
| Risk | R2: event identity, censoring, scientific timing evidence, source fidelity and offline HTML |
| Source edits made | **None**. Temporary Python probes and extracted CI archive were used outside the source tree. |
| Source root AGENTS.md | Absent in the exact archived source and absent at pinned GitHub ref |

## Outcome and release gate

**CHANGES-REQUESTED**, because a source-guard-censored run can be presented as one uniquely resolved cross-scenario event pair (F-01), and a valid, independently executed M24a two-terminal observation fails the M28b HTML renderer (F-02). These are real reproductions with the pinned code; a green CI dashboard does not exercise these edge cases. Existing M24a physical laws / RK code were not changed by M28b and are not accused of incorrect force integration. Preserve PR #66 as draft; fix the local issues with explicit regression tests, rerun appropriate current-head CI, and request focused re-review on the new head. No new general architecture is needed.

## Findings

### F-01 — MAJOR / BLOCKER — Pairing incorrectly claims unique event under truncated source-guard observation

**Sources:** [event_sweep.py lines 39–73](https://github.com/physicsvigilante/conductor_sim/blob/414e69bd960bc71f3df65c7346e81bf58c1540b8/src/conductor_sim/event_sweep.py#L39-L73); [motion_events.py lines 176–190](https://github.com/physicsvigilante/conductor_sim/blob/414e69bd960bc71f3df65c7346e81bf58c1540b8/src/conductor_sim/motion_events.py#L176-L190).

**Independently executed reproduction:** Use the existing gravity/point-source guard *physical* plan as a fixed starting model, but replace its far unobserved detector with a new passive, direction=+1 detector at x=0.05 m:

~~~python
from examples.m28b_event_sweep import make_plan
from conductor_sim.motion_events import PlaneEvent
from conductor_sim.event_sweep import EventSweepPlan, run_event_sweep
original = make_plan("gravity-guard")
q = PlaneEvent("before-guard", (.05,0.,0.), (1.,0.,0.),
               "Early detector before guard", direction=1)
result = run_event_sweep(EventSweepPlan(original.sweep, (q,), original.policy))
print(result.as_dict()["entries"][0]["event_time_comparisons"])
~~~

Observed: baseline has one genuine +1 crossing at **0.062499194145202636 s** and then terminates **source-guard**; independently solved child has one +1 crossing at **0.07752344608306884 s** and terminates **duration**. Both M24a outcomes say 'located' since a crossing happened *before* each observation ended. M28b reports **one-resolved-pair**, positive estimated shift **0.015024251937866204 s**, bracket shift **[0.015024242401123038, 0.015024261474609377] s**.

The shift arithmetic is valid **for those observed roots**, but the source-guard baseline does **not** establish that the detector has exactly one crossing over the requested full time horizon. The result silently conflates "one observed preguard root" with "uniquely resolved root for the whole study". This conflicts with the frozen charter's censor/uniqueness requirements and the request's explicit guard-unpaired challenge. **No later crossing is claimed or fabricated here**: its unknowability is precisely the issue.

**Fix/test:** For the existing unique-event shift, mark a nonterminal detector **unpaired** when either run is source-guard/event-unresolved censored (and consider terminal-event censoring explicitly). Alternatively introduce a separately named "first *observed* crossing comparison" with an explicit observation-horizon qualification, rather than silently redefining the frozen unique-root rule. Add the exact guard-after-early-root regression; preserve the underlying observed root and bracket in JSON. Severity confidence: **high**, native reproduced.

### F-02 — MAJOR / BLOCKER — Offline event timeline rejects an M24a-valid coincident terminal event alternative

**Sources:** [event_sweep_viewer.py lines 81–95](https://github.com/physicsvigilante/conductor_sim/blob/414e69bd960bc71f3df65c7346e81bf58c1540b8/src/conductor_sim/event_sweep_viewer.py#L81-L95); [motion_events.py lines 387–402](https://github.com/physicsvigilante/conductor_sim/blob/414e69bd960bc71f3df65c7346e81bf58c1540b8/src/conductor_sim/motion_events.py#L387-L402) and [lines 430–447](https://github.com/physicsvigilante/conductor_sim/blob/414e69bd960bc71f3df65c7346e81bf58c1540b8/src/conductor_sim/motion_events.py#L430-L447).

**Independently executed reproduction:** Starting with the already qualified uniform-field model (E=1000 V/m, q=1 µC, m=0.001 kg), keep the ordinary mass sweep and ask two separately identified, signed, terminal, ideal-stop observations: x=0.0500000000 m and x=0.0500000005 m. Use EventPolicy(max_step_s=0.01, time_tolerance_s=1e-8, position_tolerance_m=1e-10, velocity_tolerance_m_s=1e-8).

Native `run_event_sweep` **succeeds and validates** the baseline, with two original overlapping numerical terminal brackets and `ordering="coincident-or-order-unresolved-within-time-resolution"`. Reported terminal time **0.31622776627540594 s**; another retained terminal candidate has sample **0.3162277674674988 s**, inside the permitted overlapping bracket/tolerance rule. However `render_event_sweep(result)` throws **ValueError: event is outside real observed horizon**.

M24a correctly allows alternate terminal candidates whose numerical brackets overlap the observed terminal crossing; it does not authorize a poststop physical trajectory. M28b wrongly asserts **every** event sample time must be at or before the terminal event representative time. This makes a scientifically legal native result impossible to present.

**Fix/test:** Render both native brackets in the table, retain their original identities/directions, and show coincident alternatives at the true terminal-boundary observation without drawing a physical line after the stop. Do not change M24a or fabricate later particle states. Add a native-render and 390px Chromium regression with two distinct near-coincident terminal IDs. Severity confidence: **high**, native reproduced; a second tolerance/distance setting also failed.

### F-03 — QUESTION / NONBLOCKING SCIENTIFIC SEMANTICS — Opposite-direction bidirectional roots are silently paired

**Source:** [event_sweep.py lines 45–73](https://github.com/physicsvigilante/conductor_sim/blob/414e69bd960bc71f3df65c7346e81bf58c1540b8/src/conductor_sim/event_sweep.py#L45-L73); [viewer lines 125–151](https://github.com/physicsvigilante/conductor_sim/blob/414e69bd960bc71f3df65c7346e81bf58c1540b8/src/conductor_sim/event_sweep_viewer.py#L125-L151).

Independently authored a stable, symmetric source arrangement: **two +2 µC point sources at x=−0.5 and +0.5 m**, test q=+1 nC, m=1e-5 kg, baseline release at x=−0.08 m, child revised release at x=+0.08 m, both from rest; observation duration 0.32 s; bidirectional passive detector x=0, normal +x. Both experiments end by duration, each has one genuine crossing at **0.2031308264732361 s**, but directions are **+1** and **−1**. M28b emits a **one-resolved-pair with 0 s shift**.

This may be defensible if the declared teacher question is strictly "time of crossing the plane, either way." It is **not** equivalent for a directional-entering/exiting question. The saved JSON retains both signed directions, but the HTML root-details and shift table do not visibly show the direction. **Required decision for the correction:** either explicitly regard opposite directions as unpaired, or label both signed directions and qualify the comparison as bidirectional time-to-plane (not identical directional events). Document and test the chosen semantics. No claim is made that the underlying trajectories are wrong.

### F-04 — MINOR / EDUCATIONAL PROVENANCE — Generic viewer contains a ring-specific sentence

**Source:** [event_sweep_viewer.py lines 187–192](https://github.com/physicsvigilante/conductor_sim/blob/414e69bd960bc71f3df65c7346e81bf58c1540b8/src/conductor_sim/event_sweep_viewer.py#L187-L192).

An independently authored **two-uniform-electric-source + gravity** arrangement is labeled in the generic viewer with "... not a time-dependent change of **ring charge**." The model contains no ring. This is not a false source attribution in the audit, but it weakens the source-agnostic teaching contract. Replace with "not a time-dependent change of a model parameter" or comparable source-neutral language. Confirm with the unfamiliar no-ring case. Confidence: **high**, independently rendered and inspected.

## Tests and independent evidence

### A. Exact-head evidence integrity

- Downloaded [GitHub visualization artifact #14217990023](https://github.com/physicsvigilante/conductor_sim/actions/runs/43849798098/artifacts/14217990023) **myself**; computed **SHA-256 dc05d29f011ad5cf8581eb5a9279585765b64254e2a1814da6f7cb9f81150cf0**. It matches the digest supplied as GitHub-reported, not an unperformed rehash assertion.
- Extracted artifact's `source.zip` (395 archive members) and reconstructed Git's tracked-file tree using a temporary Git index; `git write-tree` returned **ac06b4990b8002394fa7965fa2391eda8ca9f16e**, exactly the committed source tree independently fetched from GitHub. `commit.txt` was not relied upon to identify source HEAD, because PR checkout may be synthetic merge.
- Independently read the original scanned `02_conductors_half_size.pdf`, printed page **3.44** (PDF page 12): for Q40–41 it visibly gives ring A +10 µC and B −20 µC, R=30 cm each, separation 40 cm, upward E=10^5 N/C, probe q=+10 µC, and *symbolic* mass m, release from rest at A and an axially guided question. Source charges and geometry match the authored claims. The .01 kg free-plane moving launch, finite duration, detector, variations and event numerical policy are **teacher hypotheses**, and are not the original released-from-rest axial Q41 solution. This is direct source-PDF inspection, **not** reliance on the implementer's paraphrase.
- Verified GitHub workflow metadata: **15 PR-triggered workflow runs completed successfully** on exact head, plus **one separate successful push Python run** [43849788853](https://github.com/physicsvigilante/conductor_sim/actions/runs/43849788853). Specifically checked [Python 43849797928](https://github.com/physicsvigilante/conductor_sim/actions/runs/43849797928), [real FEMM 43849797863](https://github.com/physicsvigilante/conductor_sim/actions/runs/43849797863) and [visualization 43849798098](https://github.com/physicsvigilante/conductor_sim/actions/runs/43849798098); all reported success. The archived `python.xml` contains **1,835 tests, zero failures, zero errors** for that visual-job run. The complete Python 3.10/3.12 and 97 FEMM5 results are **CI evidence**, not tests I personally reran.
- Read native artifact JSON for ring-detector, uniform-mass, multi-crossing and gravity-guard, along with mobile screenshots and HTML. The original cases preserve native signed directions, brackets, sample positions/forces/energies, original source identities and guard-specific termination/outcomes. Existing multi-crossing x=.25 m has two roots per run and correctly stays **unpaired**; a far detector under source-guard correctly reports **search-truncated** versus the duration child's **not-found-at-requested-resolution**.
- Historical first failed candidate runs are [43849386943](https://github.com/physicsvigilante/conductor_sim/actions/runs/43849386943) (Python import syntax error) and [43849638674](https://github.com/physicsvigilante/conductor_sim/actions/runs/43849638674) (browser tuple/JSON expectation). They are not retconned as first-pass successes.

### B. Tests personally executed (native and browser)

1. **Local pinned targeted source tests:** `PYTHONPATH=src:. pytest -q tests/test_m28b_event_sweep.py` — **9 passed, 1 PytestCollectionWarning**, in Python 3.13.5. This includes exercised baseline/child M24a runs, finite policy/duplicate-ID refusal, wrong-side valid-physical terminal-study refusal, incompatible ring-source revision refusal, synthetic two-crossing unpairing, provenance, hostile text escaping and 90° rotation. These are developer-authored assertions that I executed, **not** independent novel reference proofs.
2. **New unfamiliar native physical assembly:** two perpendicular named uniform E fields, `Ex=240 V/m`, `Ey=−90 V/m`, additional downward gravity `gy=−2 m/s²`; q=5e-7 C, m=2e-5 kg, launch `v=(0.05,0.2,0) m/s`, `p=(0,0,0)`, motion plane z=0, `duration=0.45 s`, oblique detector **x+y=0.1 m** (normal (1,1,0)), positive crossing. Revisions: stable ID `review:Ex` changes only to 180 V/m or 300 V/m; second field, gravity and everything else unchanged. No problem-specific production code was added.
3. **Independent analytic reference, not production force/root code:** normal-direction coordinate obeys `x+y = 0.25 t + 0.5[(q/m)(Ex+Ey)+gy] t²`. Solve its positive root at 0.1 m. Expected **0.22414950224757513**, **0.3416407864998738**, **0.18279912332514048** s (baseline, 180, 300); native M24a returned **0.22414950226619837**, **0.34164078648015855**, **0.18279912331700324** s, each with a single +1 root, fully completed duration, same bound source IDs and correct immutable parent revision. Worst absolute time difference **1.972e-11 s**; analytic root lies inside each saved numerical root bracket. Full shared-time audit returned **31 exact matching saved timestamps per child**; no grid index interpolation.
4. For 180 V/m, estimated shift **+0.11749128421396018 s**, interval **[+0.11749128416180613,+0.11749128426611424] s**; for 300 V/m, estimated shift **−0.04135037894919513 s**, interval **[−0.04135037900507449,−0.041350378893315776] s**. The analytic differences also fall inside these intervals. General proof: if the numerically localized base root `b∈[b_lo,b_hi]` and child root `v∈[v_lo,v_hi]`, monotonic subtraction gives `v−b∈[v_lo−b_hi, v_hi−b_lo]`. This is a valid bound on differences of localized numerical roots, **not** a validated global ODE or exact-physical-root enclosure.
5. **Preserved first self-authored novel trial:** I originally set duration=0.32 s, so the 180 V/m analytic root (0.3416407865 s) lay **outside the requested observation horizon**. The engine correctly classified that case **not-found-at-requested-resolution**; my first test's inappropriate expectation of three pairs failed. I corrected **only the independent trial duration to 0.45 s**, preserving the original negative observation in this report. This was not a source defect or an unrecorded retry.
6. **Additional new adversarial native cases:** preguard located root (F-01), two co-located terminal stop alternatives (F-02, two failing numerical settings), and opposite signed single crossings from symmetric point sources (F-03). M24a source guards and exact native terminal-event branches were retained.
7. **Independent local Chromium 390px on new unfamiliar HTML** using installed executable at /usr/bin/chromium: `innerWidth=390`, document scroll width **390**, SVG timeline width **348**, **3** root circles, **3** table rows, parseable detached native v1 JSON, **zero page errors, zero console errors, zero network requests**. Independently inspected the PNG and the native HTML. The implementation's other four original CI browser cases are *artifact-inspected*, not individually rerun by me.
8. Source escapes HTML-visible strings with `html.escape` and escapes `<`, `>`, `&` inside embedded application/json. The local 9-test run exercised its hostile provenance `</script><script>...` case. This supports, but cannot formally prove, injection resistance to all inputs.

## Separate scope judgments

| Dimension | Judgment | Evidence and boundary |
| --- | --- | --- |
| Source interpretation fidelity | **PASS for bounded authored use** | Directly inspected scanned page 12; original ring facts separated from teacher-selected mass, off-axis launch, detector and variations; unrelated teacher scenarios do not claim workbook origin |
| Physical / numerical correctness | **PARTIAL — release blocked** | Unfamiliar two-field + gravity kinematic reference passed to ~2e-11 s and bracket shift algebra sound; F-01 misstates *unique* pairing under censor; F-03 requires explicit bidirectional semantics |
| Native simulation / observable coverage | **PARTIAL — release blocked** | Real distinct M24a integrations, refusals, 1 vs multiple roots, source guard and outcomes preserved; F-02 prevents rendering a valid coincident-terminal observation |
| Evidence integrity and provenance | **PASS with documented limits** | Artifact downloaded and rehashed; frozen Git tree verified; native JSON inspected; full CI results not independently rerun; PDF provenance explicitly an author assertion, not authentication |
| Teacher-facing usefulness | **PARTIAL** | New offline timeline and 390px browser work; root sign not visible in table, F-02 renderer error and F-04 irrelevant generic ring-charge wording need attention; timeline is not apparatus/ring geometry |
| Textbook-answer completeness | **NOT ATTEMPTED / NOT REQUIRED** | Q41 axial, symbolic-mass, released-from-rest answer is deliberately outside M28b's free-plane hypothetical |

## Smallest correction / re-review request

- **Blocker 1:** Tighten uniqueness/censor eligibility in `_root_pair`; preserve located preguard evidence while unpairing nonterminal censored comparisons (or explicitly amend the scientific contract and label a distinct first-observed comparison). Test the x=.05 preguard crossing with baseline source-guard/child duration.
- **Blocker 2:** Support valid overlapping terminal-event alternatives in `_timeline` without plotting poststop motion; regression on two near coincident signed terminal planes with 390px browser output.
- **Scientific UI decision:** Expose every root's signed direction visibly, and decide whether a bidirectional detector may pair opposite directions; test the mirrored two-point-source case.
- **Minor:** Make source-agnostic viewer text truly neutral (remove generic "ring charge" phrase).
- Then rerun focused native/browser regressions plus required current-head CI and perform **targeted independent re-review of the new SHA**. If those corrections broaden physical/evidence semantics, escalate the affected paths under R2. Do **not** merge PR #66 on this report; no production files were changed during this review.

**Reviewer signature/context:** Chat B, GPT-6, independent new conversation; independent tests and observations are distinguished from the implementer's source, existing tests and CI. This is a separate-context LLM audit, not independent human scientific certification.
