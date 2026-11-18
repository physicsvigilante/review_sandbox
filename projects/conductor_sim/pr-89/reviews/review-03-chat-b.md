# conductor_sim PR #89 — Chat B independent targeted F4 re-review #03

**Verdict: CHANGES REQUESTED** — on the corrected source a new, independently testable false turning-event claim is accepted by the standalone exported-JSON checker. The three original F4 defects ARE corrected, the previous F1–F3 suite passes, and production CI is entirely green. This review is a scientific-evidence gate, **not** a GitHub merge approval.

**Reviewer:** independent Chat B (18 November 2026).  
**Scope:** targeted offline scientific-export integrity and inherited independent R2 replay. No production edits, no native physics redesign, no full new PDF interpretation.

## 1. Exact candidate and trust boundary

| Item | Independently verified |
|---|---|
| Production | [physicsvigilante/conductor_sim PR #89](https://github.com/physicsvigilante/conductor_sim/pull/89), LIVE open / draft / unmerged |
| New HEAD | `630f6d320a1b4cb00bf7bb0780cd3deca4ec0f7e` |
| Native Git TREE | `796f319edf5829455e842d9bad63b770d17ff9fa` |
| Prior independently reviewed HEAD | `adfe9098742c663e9f4132c3e29e86dddf7ecc1e` / tree `43f8ebae4937eacc25143fdace324115edcfb2d0` |
| Exact intervening changed files | `tools/m37a_ground_wire_reference.py`; `tests/test_m37a_grounded_wire_current.py`; `docs/m37a.md` |
| Physics/M16a/Kelvin/renderer/FEMM/PDF change | **None**, verified via full native diff |
| Original workbook | Git blob `90d8869b0f01cc2ea13f83721985a5d8419f1d0e`, SHA-256 `9dff3c02a9f1848d2c3d99cb1a6e7a44dc7f5a51f7a3a2b8cc92d10ce1fbca5d`, unchanged |

A live API PR query in the actual independent workflow verified the exact candidate and draft/unmerged state. Fresh source checkout verified `git rev-parse HEAD` and `HEAD^{tree}`, zero tracked changes, exact three-file delta and original PDF hash. No broad re-review of unchanged physical code was necessary. The workbook p8 Multiple Correct Q21 uses an externally prescribed constant-speed approaching positive source, answer (1),(3), established by prior independent source inspection; the free native M16a motion is **not** represented as the literal source trajectory.

## 2. Actual FIRST independent execution

**[Reviewer-owned workflow run #44320918820 — FAILURE](https://github.com/physicsvigilante/review_sandbox/actions/runs/44320918820).** Ubuntu GitHub Actions, Python 3.12.16, original first attempt retained. The independent execution did not rewrite or relabel the earlier failed reviews.

- Original reviewer-authored [R2 script](https://github.com/physicsvigilante/review_sandbox/blob/review/conductor-pr89-r2-20261118/projects/conductor_sim/pr-89/reviews/challenge_r2.py), replayed with only the HEAD/TREE identity pins changed: **99/99 met expectations** — 27 genuine successes, 71 deliberate scientific/schema/provenance refusals, 1 explicitly accepted JSON-only ODE-proof limitation. F1–F3 and all three previously reported F4 mutants now refuse as intended.
- New [R3 reviewer-owned script](https://github.com/physicsvigilante/review_sandbox/blob/review/conductor-pr89-r3-20261118/projects/conductor_sim/pr-89/reviews/challenge_r3_f4.py): **43 observations** = 3 real genuine duration/turning/guarded histories accepted, **38 intended refusals**, 1 separately documented intrinsic export-proof limitation, and **1 unexpected acceptance** of a locally provably false event.
- Real native examples were regenerated from the production CLI, plus two native M16a integrations; snapshots were JSON-serialized and re-parsed. The adversarial checker remained import-isolated: AST imports only `__future__`, `argparse`, `json`, `math` and `pathlib`, no production physics imports. Bad mutations are counted as correctly rejected only for the intended `ValueError` physical assertion, not a harness error.
- The R3 source and evidence exist in a **dedicated reviewer branch** and its run artifacts: [full first-run F4 result JSON](https://github.com/physicsvigilante/review_sandbox/blob/review/conductor-pr89-r3-20261118/projects/conductor_sim/pr-89/reviews/evidence/r3-run-44320918820-attempt-1/f4/r3-f4-results.json), [replayed R2 result JSON](https://github.com/physicsvigilante/review_sandbox/blob/review/conductor-pr89-r3-20261118/projects/conductor_sim/pr-89/reviews/evidence/r3-run-44320918820-attempt-1/r2-replay/independent-results.json), [F4 first-run text](https://github.com/physicsvigilante/review_sandbox/blob/review/conductor-pr89-r3-20261118/projects/conductor_sim/pr-89/reviews/evidence/r3-run-44320918820-attempt-1/f4-first-attempt.log), and [workflow](https://github.com/physicsvigilante/review_sandbox/blob/review/conductor-pr89-r3-20261118/.github/workflows/conductor-pr89-chat-b-03.yml).

## 3. New blocker: F4 continuation — fabricated turning event at a known nonzero-velocity instant

**P2 scientific-export integrity; reproducible, not a time-integration proof question.**

A genuine CLI-exported `duration` trace has first sample `time_s=0`, `displacement_m=0` and `velocity_m_s=-0.05`. A *single fabricated event* at that exact sample is added:

```python
from copy import deepcopy
from tools.m37a_ground_wire_reference import validate_examples

forged = deepcopy(genuine_cli_json)
m = forged["actual_elapsed_time"]["motion"]
r = m["samples"][0]
assert r["time_s"] == 0 and r["velocity_m_s"] == -0.05
m["events"].append({
    "kind": "turning-point",
    "time_s": r["time_s"],
    "displacement_m": r["displacement_m"],
    "position_m": r["position_m"],
    "description": "Invented turning point at initial nonzero speed",
})
validate_examples(forged)  # ACTUALLY ACCEPTED by the corrected checker
```

The event is geometrically and chronologically well-formed, outside the guard, and does not change one authentic sample. But it directly contradicts the saved velocity at **the same exact timestamp**: a classical turning point cannot have a nonzero speed at that instant. No native ODE re-integration, interpolation or trust in author data outside this document is required to detect the inconsistency. The R3 novel case `novel/false-initial-turn-with-nonzero-saved-velocity` returned `UNEXPECTED_ACCEPTANCE`; not a regex matcher error.

**Required bounded correction:** validate a turning-point event against the locally exported kinematics when possible. At minimum, reject an event coincident with a saved sample having clearly nonzero velocity; for between-sample events use a conservative bracketing/sign-change consistency rule rather than inventing an ODE solver. Reject obviously duplicate/impossible turning claims as warranted. Retain acceptance of the genuine off-grid M16a turning event. Add this exact mutation and corresponding genuine case as regression tests, then run an independent targeted new-source replay. Do not reopen Kelvin physics or demand a new full source audit.

## 4. What the corrected F4 checker gets right

The following R3 hostile checks generated **actual intended physical/schema ValueError refusals**; these are real corrections, not static promises.

| Family | Independently observed |
|---|---|
| Original R2 F4 trio | 1e9-J forged max drift, negative 0.3-m guard, and spurious surface-guard event on completed-duration trace **all rejected** |
| Drift metadata | negative, Boolean, NaN, Infinity and false zero maxima rejected against checked saved drift samples |
| Guard metadata | negative/zero/Boolean/NaN/Infinity guard and clearance-inconsistent guard refused |
| Event structure | non-list/null history, non-record event, unrecognized/Boolean kind, blank description refused |
| Event timing | negative/future/Boolean/NaN/out-of-order time refused |
| Event geometry | Boolean/NaN/wrong displacement, non-axial or Boolean/NaN position, near-surface intrusion refused |
| Termination metadata | duration with surface event, surface termination without event, guarded labelled duration while retaining guard event refused |
| Authentic guarded terminal event | omission, duplication, not-last position, wrong time, and **geometry-consistent but false final displacement** refused at intended assertion |
| Genuine data | duration, real turning and real guarded histories all accepted as JSON |

The checker does **not** import the production solver. The public native typed observer additionally re-integrates the genuine qualified M16a dynamics; these are distinct proof levels.

## 5. Honest bounds and distinct CI gates

The separate JSON-only checker cannot prove that an otherwise internally plausible sequence came from a genuine ODE execution. A deliberate probe erased the real terminal guard event and relabelled its early-stopped trace as `duration`; **this was accepted as a documented proof limitation** because the JSON motion schema does not export the original requested duration/provenance against which a completed-duration claim could be checked. This is distinct from the blocker above, which contradicts a simultaneously saved velocity and is locally decidable. An eventual export-contract enhancement could include the authored requested duration; do not describe the existing checker as cryptographic authentication.

Independently inspected [live exact-HEAD CI inventory](https://github.com/physicsvigilante/review_sandbox/blob/review/conductor-pr89-r3-20261118/projects/conductor_sim/pr-89/reviews/evidence/r3-run-44320918820-attempt-1/ci-live-summary.txt): **25/25 completed SUCCESS**, exactly 23 PR runs and 2 branch push runs, including Python checks, dual Python 3.10/3.12 M37a focused checks, **real FEMM 5**, historical **Chromium/source** workflows. This does not change the **red** scientific reviewer run. Production success and an independent negative finding are simultaneously valid.

The [R1 first-run failure #44307096311](https://github.com/physicsvigilante/review_sandbox/actions/runs/44307096311), [R2 first failure #44314994267](https://github.com/physicsvigilante/review_sandbox/actions/runs/44314994267) and [R2 corrected matcher run **still FAILED** #44315235077](https://github.com/physicsvigilante/review_sandbox/actions/runs/44315235077) remain historical red evidence for their respective earlier sources.

## 6. Verdict and owner release boundary

**CHANGES REQUESTED** for the new locally checkable turning-event false acceptance. The original F4 trio and inherited F1–F3 are corrected at this exact source; no broader physics or architecture objection is raised. The production pull request should remain **DRAFT, UNMERGED**. No merge, mark-ready action, source code write, or waiver has been performed by this reviewer.

When this one narrow export defect is repaired, pin the new HEAD and real Git tree, demand exact-head full production CI, re-run the original reviewer mutation plus genuine turning/guard history at least, and preserve all earlier red evidence. A later independent PASS is **not** owner merge authorization: require a separate explicit owner decision, expected-head guarded merge, exact merged Git tree verification, and actual postmerge main CI.
