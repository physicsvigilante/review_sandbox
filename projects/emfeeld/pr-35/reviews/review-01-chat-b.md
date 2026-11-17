# EM Fields PR #35 — independent Chat B R2 source/evidence review 01

**Verdict: CHANGES REQUESTED (one reproduced R2 measurement-coverage blocker).**  
**Review date:** 2026-11-17. **Reviewer:** separate-context Chat B, automated source/evidence reviewer; not the implementer, an independently supplied teacher, or a human scientific adjudicator. **Merge authorization:** NONE. Source PR remains DRAFT/UNMERGED.

## Pinned scope and source identity

- Source [PR #35](https://github.com/physicsvigilante/emfeeld/pull/35), [Issue #34](https://github.com/physicsvigilante/emfeeld/issues/34); central [request](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/emfeeld/pr-35/REQUEST.md) and [reviewer prompt 01](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/emfeeld/pr-35/REVIEWER-PROMPT-01.md).
- Exact **head**: `addb6ab3e76e4465649211305ae1a19e73537791`, Git **tree**: `117fe65e64097d8dc3d4f6ff80ef57d7ae04d6cf`.
- Qualified **base**: `1b0149d773f924e67e0cd1f950da8b5d0ffacaa2`, tree `88364f2394dd84e6270681b3efd1ff879fc397dc`. Exact CI **preview merge**: `9120ce19c72468af1b1cfe37e1fdfef4e5392191`, SAME tree; independently queried Git commit parents in order `[base, head]`. Head parent is base.
- Independent Git compare confirms **one source commit, six changed paths**: `.github/workflows/release-candidate.yml` (+24), `docs/QUESTION_FIRST_TRIAL_V1.md` (+57), two `examples/question_first_v1/` data files (+21/+89), `tests/test_question_first_trial_v1.py` (+353), `verification/question_first_trial_v1.py` (+354). **No changed `src/emfeeld`, physical source law, integrator, historical saved studies/revisions, or viewer behavior.**
- Original source-snapshot ZIP contained `tested-source.tar`, `git-tree.txt`, `identities.txt` and `archive-sha256.txt`. Extracting and indexing that tar with Git reproduced the **exact tree** above; **361/361 recorded file-blob SHA-1 identities matched**, and the internal tar SHA-256 matched the snapshot manifest. The separate viewer archive contains the **same byte-identical** source tar.

## B1 — R2 blocker: non-exact physical saved time is accepted as complete

**Location:** [`verification/question_first_trial_v1.py` lines 292–299](https://github.com/physicsvigilante/emfeeld/blob/addb6ab3e76e4465649211305ae1a19e73537791/verification/question_first_trial_v1.py#L292-L299), particularly line 298:

```python
if type(measured) not in (int, float) or abs(measured - target) > 1e-12:
    issues.append(expected['id'] + ': actual saved time disagrees with frozen context')
```

An **absolute** 1e-12-second acceptance window can cover many different native saved instants when the authored simulation is shorter than 1e-12 s. This violates the contract's requirement to bind the frozen original question to its **actual physical saved time**.

**Fresh, actual public-CLI repro, not a mocked result:** From the pinned developer fixture, author a *new* question asking for velocity **exactly at t = 0 s**, with a frozen observation `id="wrong_time"`, `native_type="trajectory_sample"`, `native_quantity="velocity"`, context `{"particle_index":0,"sample_index":20,"time_s":0}`. Author a gravity packet with 21 samples, horizon `5e-13 s`, one 1 kg particle at rest at the origin, and a fixed uniform acceleration `[2e16,0,0] m/s²`, then request velocity at **sample index 20** under the same ID. All parameters are finite, the particle stays nonrelativistic, and no special physics engine feature is needed. Freeze and assess via:

```sh
PYTHONPATH=src python verification/question_first_trial_v1.py freeze q.json --output fresh-lock
PYTHONPATH=src python verification/question_first_trial_v1.py assess fresh-lock --packet p.json --output fresh-attempt
```

**Observed:** Both CLIs exited **0**. Actual native `wrong_time` had `status=ok`, `sample_index=20`, `time_s=5e-13` and `value≈[10000,0,0] m/s`. However, `assessment.json` reported `native_measurement_coverage="complete"` and `issues=[]`; `state.json` was `execution_complete=true`. The frozen request was for **t=0**, where the true velocity is **[0,0,0] m/s**, not the value at the later native sample. Independent closed form: `v(t)=v0+gt` gives `(2e16)(5e-13)=10,000 m/s`; displacement `0.5*g*t²=2.5e-9 m`. The raw **first** reviewer repro is preserved unchanged in the reviewer evidence bundle with:
- question SHA-256 `cfb8f9ed136f512588d31f7afb02dfe2e7574cd628b4cd719e93fd9844abebea`;
- packet SHA-256 `12715f6ab1667f63b032da7416dcf619d398a8d93bb051378bd1e1db47f1b847`;
- native-result SHA-256 `eb3d88d3825bc40fba37c7464ffafe62fd96295deb33ed047352adfc0344ea2d`.

A **second novel case** with the normal 1.5 s horizon, frozen `time_s=1.5000000000005` and actual `time_s=1.5`, likewise gave `complete` with zero issues. In the 57-case reviewer suite, this is preserved as **case 35 FAIL**, not silently corrected to pass. A larger difference (frozen 1.4 s versus native 1.5 s) correctly yields `incomplete`.

**Required correction:** Reject a saved sample whose actual physical instant differs from the frozen instant. If floating-point accommodation is necessary, make it finite-checked and tied to representation precision (e.g. a tightly justified ULP-based comparison that cannot span distinct grid samples), **not** a universal 1e-12 s tolerance. Add negative regressions for sub-picosecond horizons, t=0 versus another sample, near-but-different times, and a legitimate representational-rounding case. Verify the authoritative returned `time_s` and output `state`/coverage, not only CLI exit. The initial rejected first attempt and this report must remain preserved across any corrected commit. **Do not accept this pinned head for merge.**

## Independent execution: 57 reviewer-owned adversarial cases

**Environment:** offline Linux container, CPython 3.13.5, NumPy 2.3.5, SciPy 1.17.0, pytest 9.0.2, no local PyVista installation. Executed against source extracted from the original pinned Git archive, with `PYTHONPATH=src`. All reviewer case directories were fresh and outside the source checkout; no source PR or original CI evidence changed.

- **56 PASS, 1 FAIL** (the substantive B1 false-complete time gate). This count includes **two reviewer-authored 11-observation native gravity runs** (direct Python + separate public CLI), plus original-source malformations, unsupported laws, packet retargeting, actual native domain errors, forged native-result boundary tests, alias/overwrite checks, interrupted state and provenance-laundering attempts. It is **not** an unseen teacher study or 57 independently sourced textbook questions.
- The new gravity model used `g=(1.25,-0.75,0.4) m/s²`, potential zero at **O=(2,-1,0.5) m**, initial `r0=(-1,0.2,0.4) m`, `v0=(0.3,-1.1,0.8) m/s`, `m=3.2 kg`, `T=1.5 s`, 16 saved samples. **All 11** native values agreed with a separate direct algebra reference: `r(T)=(0.85625,-2.29375,2.05) m`, `v(T)=(2.175,-2.225,1.4) m/s`, speed `3.4119276077 m/s`, `Phi(P)=2.2 J/kg` for `P=(0.3,-0.1,2) m`, ordered `Phi(B)-Phi(A)=6.1 J/kg` for `A=(1,-2,3), B=(-0.5,1.5,-1) m`, separate 1.6 kg probe force `(2,-1.2,0.64) N`, `U(T)=-0.514 J` and `K+mPhi=18.112 J` at both endpoints. No reference answers were embedded in the observation packet.
- **Good preflight failures with zero attempt writes:** duplicate or unknown question keys, unsafe/duplicate IDs, forbidden verified origin, malformed/nonfinite/oversized/invalid UTF-8 JSON, unresolved givens, declared conductor/Maxwell/Lorentz requirements, absent or extra native IDs, total versus potential energy substitution (both J), speed versus velocity substitution (both m/s), moved static world point, swapped ordered endpoints, changed saved index, nearest-time retargeting, answer-bearing packet expectation, and invalid native source mass/NaN. Source lock was retained on rejected assessments.
- **Good executed incomplete outcomes:** incorrect requested unit, a clearly wrong actual physical time, actual electric point-source center `domain_error`; injected (and explicitly **mocked**, not actual physical cases) `no_event`, `domain_error`, wrong native quantity/unit/world point/endpoints/time, absent/extra/duplicate native result IDs and failed aggregate status. None was allowed to fulfill frozen native coverage. Unexpected injected `run_packet` exception preserved exact original question and packet bytes and `execution_complete=false` with no fabricated final assessment.
- **Good file-integrity guards:** changed lock bytes, missing or forged receipt, existing output overwrite, nested output within lock, symlink-parent alias. All refused and preserved prior bytes.
- **Honest provenance limit:** an unkeyed full rewrite of both question and receipt *can* be re-sealed, as documented. A malicious `external_unverified` teacher label/Maxwell claim or a physically wrong authored field with the same measurement IDs can still yield `complete`, **but** all interpretation/correctness/teacher fields remain `not_verified` or `not_evaluated`. This confirms that **native coverage is not source interpretation or scientific certification**. Honest requirement declaration is a human/author responsibility.

In addition, the exact-head author's **43 focused tests** were locally rerun independently as a separate regression: **43 passed, 0 failed**; do not add these to the 57 novel reviewer cases.

## Independently checked physics references

For prescribed uniform acceleration `g`: `r(t)=r0+v0t+(g t²)/2`, `v(t)=v0+gt`. For an explicit potential-zero reference O: `Phi(r)=-g·(r-O)`, `U=mPhi`, `K=(m/2)|v|²`, `K+U=constant` for the static conservative field. The signed ordered potential difference is `Phi(B)-Phi(A)=-g·(B-A)`. These equations and sign/reference conventions were evaluated independently rather than copying expected numerical arrays from the source packet. Cross-check with [OpenStax University Physics, constant acceleration](https://openstax.org/books/university-physics-volume-1/pages/3-key-equations) and [OpenStax potential difference/negative field integral](https://openstax.org/books/university-physics-volume-2/pages/7-2-electric-potential-and-potential-difference); gravitational potential here is **J/kg**, not electric potential in V.

The developer-only original gravity fixture independently gives `r(2)=(1.8,0.4,0.2) m`, `v(2)=(0.4,-2.8,0.1) m/s`, with initial `K=2.0125 J`, `U=10 J` and final `K=10.0125 J`, `U=2 J`; both totals are `12.0125 J`. All five original archived native named measurements and original saved `time_s=2` agree with these relations. These checks are **bounded analytic comparisons**, not general physical or teacher validation.

## Original exact-head CI and ZIP audit (not conflated with reviewer runs)

All runs were actually queried for **final** status, jobs, artifact metadata, and original artifacts were downloaded; each ZIP passed a full CRC scan. Original **Linux/Windows release** [#44047993001](https://github.com/physicsvigilante/emfeeld/actions/runs/44047993001), **separate real-PyVista** [#44047993015](https://github.com/physicsvigilante/emfeeld/actions/runs/44047993015), and **source snapshot** [#44047993130](https://github.com/physicsvigilante/emfeeld/actions/runs/44047993130): each `status=completed, conclusion=success`, original run attempt 1.

| Original downloaded ZIP | Artifact ID | ZIP SHA-256 |
| --- | ---: | --- |
| Ubuntu release, `rc-ubuntu-24.04-9120ce19…` | `14312822406` | `a34c05152e54431587afd9c681ee2e73e3bbf90628530dd8138eef27ca274203` |
| Windows release, `rc-windows-2022-9120ce19…` | `14312519677` | `0c888764288414acf553b82518716de2f62edc7db063980f43ca70659c7ac223` |
| Separate real viewer, `viewer-qualification-9120ce19…` | `14312297704` | `7dd81e69fb6aef7ea81ed7170bf1b25c52cf6eb62569127904089fa65e4a86ae` |
| Source, `source-9120ce19…` | `14312556893` | `1a40525c36c3d848c2ad7ac5cf12db526e8c934fa99ced7308bebd9fcc063ec7` |

The source ZIP's `tested-source.tar` SHA-256 was `e659aeab260eaa3576a5b615760f666cf319e07d79012b868bcb6004be4ee05a`; the viewer ZIP's tar matched **byte for byte**. Both OS release ZIPs contained **2,176** members and retained all 10 named `question-first-v1` original source/receipt/packet/native/assessment/state/log files. Each passed raw byte identity: archived frozen original question = archived attempt copy = pinned source fixture (question SHA-256 `36f56dcc11d6347a1db47adfb103b16472a8e1270641869f52c7220bd086a361`); archived authored packet = pinned fixture (SHA-256 `6fe25bf6c738ee13fa837793414b343feeb53116737bcfafcf19c56c36adac5d`). Receipts matched captured question bytes and requested ID order. Each `assessment.json` reported 5/5 native measurements, complete coverage, zero issues, pending separate interpretation/physics/teaching fields; archived `state.json` had `execution_complete=true`. Both OS archives recorded the same original native report SHA-256 `bf11cc7a6abd598bba0ae1746ca934eaf2ebc8c383aff79373676d5b4b06b947`. Equality was observed here, **not** assumed as a cross-platform requirement.

Read—not independently rerun—the original Linux/Windows artifact test logs: **1,569 headless passed per OS**, **18 historical behavioral passed / 1 obsolete guard deselected per OS**, and **33 real-PyVista passed per OS**. The separate viewer archive recorded **1,569 passed** and actual offscreen render/slider checks; **visual inspection = PENDING** in its own report. This is neither a manual Windows mouse/desktop trial nor classroom usefulness validation. The original workflows being green does **not** absolve the independently reproduced R2 blocker.

## First failures and scientific/teacher boundary

- **Preserved author-reported original unsuccessful attempts:** a local cumulative suite timed out near **23%** (no full local verdict) and an early test-harness event-refusal assertion mismatch was corrected in later **test-only** work. These are **author report statements**, not new reviewer-observed logs; do not retroactively call them passed. The final exact-head original CI is separately described above.
- **Preserved reviewer first failure:** new case 35 `B1_exact_saved_time_subps_violation` failed its expected `incomplete` assertion because actual status was `complete`. A second direct public-CLI sub-picosecond reproduction and raw first attempt remain retained as independent evidence; they have not been converted into an xfail/pass or overwritten.
- **Scope separation:** original and new native measurements can be checked against analytic physics **for these cases**, but frozen source wording was **not** independently authenticated; unknown implicit requirements may be omitted; prospective source interpretation fidelity is **not verified**; general numerical correctness is **not certified**; teacher usefulness, textbook completeness, and a truly unseen externally adjudicated student question are **not evaluated**. A passing offscreen viewer is not teaching validation.

## Required next action and gate

1. **Fix B1** in the source wrapper, add regression for physically distinct times separated by less than 1e-12 s, preserve this report and failed first attempts. Avoid relaxing native statuses or changing solver physics to make the test pass.
2. Record a **new exact head/tree**, rerun focused and historical negative checks and fresh Linux, Windows, source snapshot and real-viewer CI as required for the new SHA; audit retained original ZIP/byte receipts again.
3. Request **targeted independent R2 re-review** of the corrected saved-time gate and evidence. The owner—not this report—controls integration. **Do not merge PR #35 on this head.**

**Final R2 verdict for the pinned candidate: CHANGES REQUESTED.** Other observed source-integrity, physical-reference and refusal behaviors are encouraging but do not outweigh a demonstrated false **complete native coverage** assertion.
