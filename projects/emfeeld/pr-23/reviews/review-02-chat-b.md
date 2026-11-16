# EM Fields PR #23 — second targeted independent Chat B R2 review (review-02)

**Verdict: CHANGES REQUESTED** on corrected source commit **`5738fec0d22deb59d0f146dc75b8a9b33db64486`**, canonical Git tree **`0d1591d4aca5e5131429b55857814e641fed3993`**. Date: **2026-11-16 (Asia/Kolkata)**. **R2-02 and R2-03 pass the independently tested corrections; R2-01 remains a BLOCKER for a newly demonstrated cross-field native grammar mismatch.** This does not reopen the field laws, numerical integrator, or already qualified comparison semantics. **Keep source PR #23 draft/unmerged.**

This is a **new, independently authored, executed follow-up**. The original [review-01](review-01-chat-b.md) remains **CHANGES REQUESTED** on its own old source SHA `38773a546d76616fe815eb302c418281bded7c1d`; its blob **`e2ceb284c7183b91dcbd24ee2c9eb6b97ffcd814`** was checked unchanged. The author's [correction response](../responses/response-01-chat-a.md) and exact-head CI are attributable author evidence, **not independent tests**.

## Pinned source, boundaries and provenance

- [PR #23](https://github.com/physicsvigilante/emfeeld/pull/23) was verified **open, draft, unmerged** with requested head `5738fec0…` and qualified base `f0fc993dae1831432ca43b651a12e64fa0b2fdd5`.
- GitHub Git-commit metadata binds `5738fec0…` to the exact tree `0d1591d4…`. Compared against the first-reviewed head, **two commits, only two changed paths**: `src/emfeeld/scenario_ensembles.py` (138 changed lines) and `tests/test_scenario_ensembles.py` (73 additions). No existing field/solver/renderer/physical tolerance file changed.
- Independently downloaded the **original exact-head source-snapshot ZIP**, GitHub Actions artifact **14226006072**, from [run 43866219481](https://github.com/physicsvigilante/emfeeld/actions/runs/43866219481). Measured ZIP SHA256 **`78fe133f303c4fe51b554ed9600730b053001710d979c37c4aa953ab31251d8d`**, CRC clean; embedded `tested-source.tar` SHA256 **`7465409295eb264dd0c9a5baa1bd5df86cb0f39075a11a9bb240d32cfecd9955`**. Extracted the source and reconstructed its Git tree with `git add --all; git write-tree`: **exactly `0d1591d4aca5e5131429b55857814e641fed3993`**. This pins the actually executed code, not merely a floating branch.
- Independently queried GitHub run/job metadata: [Linux+Windows full clean install 43866219517](https://github.com/physicsvigilante/emfeeld/actions/runs/43866219517) **success** at the requested head, with Ubuntu 24.04 and Windows 2022 jobs both successful; [real PyVista 43866219510](https://github.com/physicsvigilante/emfeeld/actions/runs/43866219510) **success**; source-snapshot run successful. The reported **1,433 headless + 18 historical + 33 PyVista** suite memberships per OS and the author E1/G1/T1 numerical checks are **author qualification**, not Chat B's independent executions. No full-suite or manual Windows viewer execution by this reviewer.
- Read the new [FOLLOW-UP-02](../FOLLOW-UP-02.md), [review-01](review-01-chat-b.md), correction response, central [protocol](../../../../PROTOCOL.md), [risk policy](../../../../REVIEW-RISK-POLICY.md), exact source's `AGENTS.md` and bounded ensemble/native grammar implementations. Scope is original **R2-01, R2-02, R2-03**, no new scientific capability claims.

## Independent test execution, including the first failed attempts

**Environment:** isolated Linux container, Python **3.13.5**, NumPy **2.3.5**, SciPy **1.17.0**, pytest **9.0.2**. No dependencies installed, no changes to the hosted source PR, no edits to the user's local environment. All new test scripts and logs were kept **outside** the extracted source. Existing project helpers were reused **only** for initial model import, analysis configuration and V3 proposal construction; the probes, mutations, assertions and reviewer expectations were independently authored. In particular, the tests do not invoke the author's `_spec`, `_run`, or author regression functions.

Independent setup: a sealed, fresh electric two-solid-sphere native parent; two same-root V3 alternatives with independently written observation positions `[0.41,-0.18,0.33]` and ordered potential endpoints ending at `[3.1,0.49,-0.3]`; separate field/potential comparison pairs. At every intended preflight refusal the test independently compares **all original native store file bytes and every original template run file byte** before/after, and requires **no output directory, no proposal directories, and only the original root revision**.

| Reviewer-owned batch | Parametrized pytest executions | Pass | Fail | Immutable first-log SHA256 |
|---|---:|---:|---:|---|
| `reviewer02_tests.py` | 35 | 34 | 1 | `fdcd373a6d8dba4cbe36c1557cddbb5ddca164fd9201e5f539fdb22e222d0c88` |
| `reviewer02_supplement.py` | 4 | 2 | 2 | `d17dba8fff20dee120530a97e1c3d9c9267b0906d5ad2dc5dd741669d46fef6d` |
| **Combined** | **39** | **36** | **3** | combined log `19a18a38ea5dde76477774729e5d6e8cc68f2a5dd323675dfd1e795ccf5d7d80` |

Test script SHA256: `reviewer02_tests.py` **`289e7a9ef54b9b99233013c57318201679df3cbb6850fe44849ffbc2abc31cc0`**; `reviewer02_supplement.py` **`3786d0a61d91db0c6a0ff9c5141d21019892e4ce8a265efdc0fad425bec5e4a5`**. Scripts, unmodified first-attempt logs, combined log and the separate positive characterization log were packaged as the review-conversation evidence ZIP (SHA256 **`1d65732c773826dfb50fcb69e8e01dd7008d9e8cd95d6a788207ab0aeb0e29fc`**). The exact source artifact itself is independently retrievable by its GitHub artifact ID. **Three red tests represent two variants of one residual cause, not three unrelated production defects.**

Reproduce after extracting the pinned artifact source under `source/` and placing the reviewer scripts adjacent to it:

```bash
PYTHONPATH=source/src:source/tests:. python -m pytest -q reviewer02_tests.py reviewer02_supplement.py
```

The first-batch `static_with_trajectory_sample` case used index 6, which the *synthetic dummy scene's two-sample grid* refused for an **independent grid-range reason**. This apparent green result **is not evidence of a mode/observation compatibility check**; the supplementary valid index-0 case exposed the gap. The first attempt was preserved and not rewritten to hide that mistaken inference.

## R2-01 — BLOCKER remains: native analysis/observation compatibility bypasses preflight

**Verified corrected subset (20 independent negative cases passed).** Unknown keys at the top of `analysis`, `investigation`, `presentation` and within an individual observation/expectation; duplicate observation IDs; malformed bounds/camera, nonpositive replay, unsupported analysis mode; missing/extra trajectory-check keys; malformed trajectory-sample quantity/time selectors; invalid event direction/occurrence/accuracy shape/normal; disallowed positional particle index and a wrong-role static observation. All refused with **zero new ensemble output or model-store proposal/revision writes** in these tests. These directly confirm that the original unexpected-nested-key failure is repaired for the tested cases.

**New independent failing case: cross-field analysis grammar.** Give **member 2**, while retaining member 1 as a completely valid sibling, the following native authoring combination:

```json
"analysis": {"analysis_version":1,"id":"chatb-2-analysis","mode":"static"},
"investigation.observations[2]": {
  "id":"cross-mode-sample","type":"trajectory_sample",
  "particle_id":"probe","quantity":"position","sample_index":0
}
```

Separately replace that last observation with a **fully well-formed `trajectory_event`**: `particle_id="probe"`, plane at `[0,0,0]` with normal `[0,1,0]` and direction `either`, `occurrence="first"`, `max_step_s=0.1`, `min_normal_speed_m_s=1e-7`, `accuracy={time_atol_s:1e-5,position_atol_m:1e-5,velocity_atol_m_s:1e-5,rtol:1e-8}`. All referenced physical bodies exist; each observation is independently syntactically valid. The violation is **not an absent physical body or stale proposed source identity**: native `mode: static` prohibits trajectory observations categorically.

**Required behavior:** early `unsupported_analysis` or equivalent preflight error **before** output creation or V3 reservations, preserving both siblings' proposal identities for correction/retry.

**Observed, independently executed twice with distinct observation types:** no early exception. A **sealed partial ensemble** is created; baseline and member 1 are complete; **both V3 siblings are accepted and reserve native proposal IDs**; member 2 native run is **rejected** with `unsupported_analysis`; **three revisions** remain including root and **two proposals** remain. `inspect_ensemble` accepts this as a *truthfully partial* result. This is not a false complete claim or a corrupted physics result; it is a **preflight contract/identity-consumption defect**. The separate characterization command produced, for each observation type:

```text
ENSEMBLE partial  MEMBER-2 accepted rejected  REVISIONS 3  CODE unsupported_analysis
```

Characterization log SHA256: **`0a1015f2d666d3f677696b49b222da4b2d64c32f3c93134274c79beacfca43ed`**.

**Why:** [`scenario_ensembles._native_grammar` lines 84–136](https://github.com/physicsvigilante/emfeeld/blob/5738fec0d22deb59d0f146dc75b8a9b33db64486/src/emfeeld/scenario_ensembles.py#L84-L136) separately validates the mode and parses an observation packet using a dummy scene, but **never checks whether a motion request requires `analysis.mode == "trajectory"`**. The normal native [`model_runs.lower` line 103–105](https://github.com/physicsvigilante/emfeeld/blob/5738fec0d22deb59d0f146dc75b8a9b33db64486/src/emfeeld/model_runs.py#L103-L105) *does* enforce that cross-field rule, but [ensemble execution](https://github.com/physicsvigilante/emfeeld/blob/5738fec0d22deb59d0f146dc75b8a9b33db64486/src/emfeeld/scenario_ensembles.py#L301-L334) calls `store.revise` before reaching it.

**Required narrow correction:** in the new ensemble `_native_grammar`, explicitly reject any `trajectory_sample` or `trajectory_event` under `mode != "trajectory"` **during preflight**; do not rely on synthetic grid side effects. Add regressions for **sample index 0 and a complete valid event selector as member 2** asserting no output, no proposals, no new revisions and byte-identical root/template. Preserve physically valid syntax but **stale `presentation.entity_order`** as a positive per-member case: the independently executed control accepted both V3 proposals, completed member 1 and truthfully marked member 2 native **rejected/partial**. Another positive control of a physically wrong-role V3 proposal rejected only that member. Do not move genuinely physical admission failures into global grammar preflight.

## R2-02 — PASS on tested correction: literal exponent overflow refused before writes

Six independent cases passed: **literal JSON `1e400`** injected in member 1 field coordinate, member 2 V3 proposed physical value, member 2 nested field expectation tolerance, member 2 camera coordinate, and member 2 event `max_step_s`; plus a JSON integer exceeding float64 range. The raw numeric exponent, not an `Infinity` token, was substituted into serialized UTF-8 JSON; the shared decoder did parse it to nonfinite Python float before the new guard rejected it. **Every run raised before output creation** and retained identical store/template bytes, zero proposal reservations and only the root revision. The corrected [`_finite_tree` and `validate_spec`](https://github.com/physicsvigilante/emfeeld/blob/5738fec0d22deb59d0f146dc75b8a9b33db64486/src/emfeeld/scenario_ensembles.py#L43-L65) also pre-encode input. This meets the requested new-boundary refusal for these probes, without claiming the legacy shared decoder's semantics were changed.

## R2-03 — PASS on tested correction: original proposal raw-byte binding

Five independent tampering/ordering cases passed. In an ensemble with **member 1 accepted, member 2 physically rejected**, changed **only** the native store's `proposals/<sha256(proposal_id)>/proposal.json` for each of the **accepted and rejected** members, using (a) appended whitespace leaving decoded JSON unchanged and (b) a one-token semantic JSON change. With ensemble evidence and native `decision.json` untouched, **`inspect_ensemble` raised `RevisionError(code="ensemble_integrity")` in every tampered case**, not a complete or partial acceptance. The original store proposal bytes matched the exact retained member proposal, `decision.proposal_id` and `decision.proposal_sha256` before mutation; restoring the **exact original bytes** restored successful inspection without ensemble rewrite. A fifth ordering case placed the *rejected* member first and the accepted member second, again detected whitespace-only drift and recovered upon restoration. This exercises the new [native store proposal binding](https://github.com/physicsvigilante/emfeeld/blob/5738fec0d22deb59d0f146dc75b8a9b33db64486/src/emfeeld/scenario_ensembles.py#L397-L419) in both decision states.

## Scope, limitations and merge gate

This follow-up **does not** provide new blind physics references or independent execution of the full 1,433-case headless suite, viewer interactions, Windows desktop pointer tests, broad crash recovery or distributed atomicity. GitHub workflow metadata checks and the archive tree/byte audit are independently observed **provenance**, not a second independent author/CI physical qualification. Unkeyed SHA inventories do not prove authenticity against an actor who rewrites and re-seals *all* evidence. Physical arrangements remain alternative prescribed static sources, not time transitions, coupling or conductor physics. Separate-chat LLM review is not human physics certification.

**Disposition:** **R2-01 = CHANGES REQUIRED (remaining BLOCKER); R2-02 = PASS within targeted tests; R2-03 = PASS within targeted tests. Overall: CHANGES REQUESTED on exact SHA `5738fec0…`.** Make one bounded R2-01 correction and regression; publish **new source SHA/tree**, rerun proportionate **exact-head full Linux/Windows and real-PyVista CI**, and request a **narrow re-review of the mode/observation preflight gate**. Preserve this report and review-01 separately. **No source PR files, branch, metadata or merge were changed by this reviewer; do not merge on this verdict.**
