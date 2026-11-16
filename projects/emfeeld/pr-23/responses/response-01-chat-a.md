# Chat A response 01 — PR #23 independent R2 review corrections

**Status:** Chat B's [review-01](../reviews/review-01-chat-b.md) reported **CHANGES REQUESTED** on original source head **38773a546d76616fe815eb302c418281bded7c1d**, canonical tree **5bcb842ff3f14991cf12f069daa6a3dc3978f7bf**. Three independently reproduced findings were accepted. This file is the implementer's attributed correction report, **not a new independent Chat B verdict**, not merge authorization. PR #23 remains **draft, open, unmerged**.

## Immutable review/source identities

- Original Chat B reviewer file Git blob **e2ceb284c7183b91dcbd24ee2c9eb6b97ffcd814**, original review unchanged. Reviewer authored 20 adversarial pytest definitions (17 passed, 3 failed against the old source), including novel electric solid-sphere and gravitational uniform-field references. The first reviewer failed attempts, concurrency records and original source evidence remain attached to the initial source SHA and were not rewritten.
- Qualified source parent main: **f0fc993dae1831432ca43b651a12e64fa0b2fdd5** (post-merge qualified PR #20).
- **New correction branch head:** **5738fec0d22deb59d0f146dc75b8a9b33db64486**, Git tree **0d1591d4aca5e5131429b55857814e641fed3993**.
- Corrections are limited to new `src/emfeeld/scenario_ensembles.py` and `tests/test_scenario_ensembles.py`, two commits. Existing field/potential source laws, integration, energy diagnostics, viewer, numeric tolerances, native model V1/V2/V3 schemas, older sweeps/derived observations/comparator behavior are unchanged. No saved user store or local Conda changes.

## F-01 — BLOCKER accepted and corrected: strict native grammar preflight

Original scenario could introduce `analysis.unexpected_token`, and the model store accepted a V3 descendant before the later native execution rejected the malformed analysis. This violated the advertised zero-write **input grammar** gate.

The correction adds pure schema-only native V1 preflight to every declared member, before ensemble output creation or any `ModelStore.revise`. It uses the existing `model_runs._presentation` grammar and `observations.packet_from_dict` parser on a temporary **nonintegrated** uniform schema scene. Strict checks cover investigation/analysis/presentation keys and versions, static vs trajectory analysis settings, numeric type/range/array shape, nested observation/expectation/event selectors, particle ID syntax and duplicate requests. A temporary physical-particle placeholder is used ONLY to validate named trajectory observation schema; it is not published or solved. **Actual source/particle membership, physical validity and named presentation entity-order admission remain authoritative at each member execution**, so a well-formed but wrong named/removed-body observation remains an honest partial member, not an erroneously global preflight failure.

Negative tests with unknown nested analysis, investigation, presentation, observation and analysis-check keys now reject **before output, proposal or revision creation**. The original intentionally invalid member presentation remains a partial native outcome under existing tests.

## F-02 — BLOCKER accepted and corrected: JSON exponent overflow in preflight

The shared legacy JSON decoder already refuses explicit `NaN` and `Infinity` tokens but parses the legal JSON float literal `1e400` to Python infinity. The new ensemble path walks all nested JSON numeric operands (dicts/lists), rejecting overflow, nonfinite floats and integers outside representable finite float64, **before** any `put`, output mkdir, or `ModelStore.revise`. It also confirms the whole input can be serialized using existing strict `encode(..., allow_nan=False)` before side effects. The shared legacy decoder/physics parser are **not** weakened or changed.

The two new regressions inject the **literal JSON token `1e400`** into (i) authored field observation coordinate and (ii) nested V3 proposal property value. Both now raise a finite-input error in preflight, leave no ensemble output, and leave original root store with no new proposal or descendant.

## F-03 — MAJOR accepted and corrected: saved rejected proposal binding

Previously the ensemble inspector compared recorded decision.json to the model store decision, but failed to compare the model store's original proposal.json bytes and SHA against `decision.proposal_sha256` and the ensemble's authored proposal.

The corrected read-only inspector now requires **for each member, including rejected/no-op as well as accepted**:
1. Stored decision's proposal ID equals the exact authored member proposal ID.
2. The native store's `proposals/sha256(proposal_id)/proposal.json` raw-byte SHA256 equals the decision's original `proposal_sha256`.
3. Those original native-store proposal bytes exactly match the sealed ensemble member proposal.json bytes.

A changed original store proposal (even an extra whitespace byte preserving parsed values) now raises **ensemble_integrity**. New regressions test this for rejected and accepted members; restoring original bytes permits inspection to succeed. Unkeyed SHA inventories remain evidence-integrity tools, **not cryptographic external authorization**.

## Preserved first failures and initial author checks

- The newly authored **nine** regression variants were first executed against original exact source head. **Nine failed**, as expected: five malformed nested grammar, two literal-overflow preflight and two stored original proposal-byte drifts; no original source files were edited for this first-attempt test. First red pytest log SHA256 **983d7cc51a28fe4c1e93f8d3aec6a759cee272377405138ff757037d77b0fa24**; status 1. The log remains a local first-attempt record and is not mislabelled green.
- After correction, **31 focused ensemble tests passed** (22 preexisting + nine added), warning-as-error, focused log SHA256 **0d03c26519fb98f4ccf0e9c91837c2764c4f9ed9e9ccf4344b508ecfdb5d2832**; status 0.
- Locally the **entire headless regression suite of 1,433 tests passed**, warning-as-error; full log SHA256 **8f613fd99b128034805422aac15e73a30bfdbdba32295ad49a075160d5ac85cb**; status 0.
- GitHub's [exact corrected source snapshot #43866219481](https://github.com/physicsvigilante/emfeeld/actions/runs/43866219481), artifact ID **14226006072**, original ZIP SHA256 **78fe133f303c4fe51b554ed9600730b053001710d979c37c4aa953ab31251d8d**, nested `tested-source.tar` SHA256 **7465409295eb264dd0c9a5baa1bd5df86cb0f39075a11a9bb240d32cfecd9955**. Source archive downloaded/CRC checked; all **346 source files** match the exact git-tree.txt Git blob SHA1 identities with no missing/extra/mismatched files. The **exact hosted source**, separately extracted, passed all **31 focused ensemble tests**.
- **Fresh exact-head Linux/Windows full release CI #43866219517** and **separate real-PyVista #43866219510** are qualification gates for the new head. At the start of this response the separate PyVista workflow is **completed SUCCESS**, while Linux/Windows release workflow is **still in progress**. Do not count earlier old-source CI as new-head qualification or claim Windows passed until it does. Original first failed CI/transfer/refinement attempts remain historical.

## Independent R2 and integration gates

When the complete exact-source Linux/Windows and PyVista workflows pass, audit their original ZIPs, exact source checkout, E1/G1/T1 native sealed ensemble members, run hash inputs and same-author separate reference calculations. Publish a new targeted [FOLLOW-UP-02](../FOLLOW-UP-02.md) and [REVIEWER-PROMPT-02](../REVIEWER-PROMPT-02.md), pinning this correction. Only independent Chat B may create a **new** `reviews/review-02-chat-b.md` with scoped pass / changes-requested / insufficient-evidence after independently challenging the corrected preflight and rejected-proposal evidence. Chat A must never fabricate review results.

Under the owner's standing instruction, routine development/guarded merge may proceed after **independent scoped R2 pass, stable exact-source CI and no unresolved blockers**; material changes to physical laws or unresolvable blockers still require owner attention. After any reviewed merge, check fresh merged-main Linux/Windows and real-PyVista and append the final central MERGE-REPORT. Physical sources/test particles remain prescribed independent and nonrelativistic; the ensemble is a set of alternative static physical scenarios, not a simulated temporal transition. No local Conda install, saved study mutation or resumed teaching evaluation.
