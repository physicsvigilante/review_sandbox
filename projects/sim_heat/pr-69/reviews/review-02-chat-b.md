# SIM_HEAT PR #69 — independent Chat B R2 correction review-02

**Verdict: CHANGES REQUESTED (targeted N8 untrusted-report evidence contract).** The specific old N8-F01 native/owner-certificate promotions and N8-F02 rod-label forgeries are now guarded, but a further **material proof/report-integrity bypass** remains in the corrected verifier: an untrusted report can claim a maximum permitted junction-enclosure width of `10^-6 K` while publishing an arbitrarily wider, internally coherent enclosure, and N8 can still return its OFFLINE PASS. This is **not** a newly discovered N7 mathematical error or evidence of native qualification.

- **Reviewer/date:** Chat B (GPT-6), 2026-11-19, Asia/Kolkata. Independent code review, not independent human/native certification.
- **Source:** [SIM_HEAT PR69](https://github.com/physicsvigilante/sim_heat/pull/69), DRAFT/unmerged; exact corrected HEAD [`23172ce2cd7a18466d2bf176b83064e6cd49bac1`](https://github.com/physicsvigilante/sim_heat/commit/23172ce2cd7a18466d2bf176b83064e6cd49bac1), Git tree `112d8b56e0d6b72fd2dec06628e5f2f58b4665a5`. Git-object inspection confirms PR synthetic checkout `fea898052ffdad02f3d307165d68890c325e693f` has the **same complete tree**, with parents [reviewed base PR68 `4f4bbabc1083f2e1f8a6ced66c00b95fea1a5128`, corrected PR69 HEAD].
- **Baseline:** Historical [review-01](review-01-chat-b.md) remains **CHANGES REQUESTED** on `cccbc8dca8acc65e17054babbb9e5558063c0d4b`; it has not been edited. I read [CORRECTION-REQUEST-02](../CORRECTION-REQUEST-02.md), the [reviewer prompt](../REVIEWER-PROMPT-02.md), prior review and [developer response](../responses/response-01-chat-a.md), inspected both versions of the three N8 changed files, and retrieved exact-head Git/PR objects and GitHub-hosted CI job logs. The old→new commit comparison changes only `qualification/h1_n8/corner_replay.py`, `qualification/h1_n8/tests/test_corner_replay.py` and `qualification/h1_n8/README.md`. The PR relative to PR68 still adds only four N8 files; N1–N7 source, Modelica, native runner, references and C1 are unchanged.
- **Reviewer execution:** I personally performed a separate exact `fractions.Fraction` calculation of the small counterexample below; **I did not execute the checked-in N7/N8 Python APIs**, did not run new unit tests locally, and did not install/query/build/launch OpenModelica. Predictions about `replay` behavior below are established by inspection of its full exact-head control flow, **not** misrepresented as observed API results. Developer-hosted tests are identified separately.

## N8-F01 — original native/certification/owner-authority forgeries: corrected within scope

The new [`_attest_n7_evidence_flags`](https://github.com/physicsvigilante/sim_heat/blob/23172ce2cd7a18466d2bf176b83064e6cd49bac1/qualification/h1_n8/corner_replay.py#L95-L133) requires the exact N7/1 top-level key inventory, expected schema/version/status/stage/assembly/limitation, **13 precise Boolean `False`** authority/native/owner/source/reference/dynamics flags and **four precise Boolean `True`** source-only semantics flags. It rejects removed fields, wrong types (`1` cannot masquerade as `True`), unknown extra authority keys and both promoted/missing nested `proofIsIndependentNativeCertificate` and `nominalCentresArePhysicalAnswers`. The nonempty-junction and zero-junction proof declarations/row inventories are also constrained in [`_check_source_and_node_report`](https://github.com/physicsvigilante/sim_heat/blob/23172ce2cd7a18466d2bf176b83064e6cd49bac1/qualification/h1_n8/corner_replay.py#L139-L195).

Thus the prior combined mutation `independentlyCertifiedReference=True`, `allGrid77Plus8Plus5Certified=True`, `proof.proofIsIndependentNativeCertificate=True` is refused by the first guard rather than overlooked. The new test iterates promote/remove for all 13 fields and the two nested flags, with extra-schema/version/status refusals. The caller's source hash remains **byte-integrity input, not independently approved original-model/owner authority**. **No residual bypass found for the original F01 flag-promotion attack.**

## N8-F02 — original forged rod directions, G, and signed physical evidence: corrected within scope

[`_source_graph`](https://github.com/physicsvigilante/sim_heat/blob/23172ce2cd7a18466d2bf176b83064e6cd49bac1/qualification/h1_n8/corner_replay.py#L365-L402) reconstructs each source rod's `a,b`, exact terminating-decimal `k,A,L,d`, and full rational conductance interval, using the independently computed 40-term Machin Pi bounds for circular conductors, rather than trusting N7's reported `G`. [`_verify_full_physical_report`](https://github.com/physicsvigilante/sim_heat/blob/23172ce2cd7a18466d2bf176b83064e6cd49bac1/qualification/h1_n8/corner_replay.py#L196-L267) requires the exact rod-record keys, source endpoints, `positiveFromTo is True`, canonical `q_from_to=G*(T_from-T_to)`, independently derived **full** rational G interval and entire signed `q` interval. It propagates the signed intervals to **every** node and checks outward sums, conditional body `dT/dt=-q_out/(mc)`, fixed-boundary supply, and the junction's true-zero-by-equation label without mistaking an interval sum for an exactly zero interval.

The source-ID/model/study SHA **strings** must agree with the admitted raw JSON; assumed body Kelvin, prescribed boundary Kelvin, circular/rod/junction inventories, all-node known exact values, junction/all-node aliases and proof-row aliases are checked. This does not externally authenticate the source/model/study SHA identities. Test coverage includes direction-only, G-only, combined direction+G, `positiveFromTo=1`, false labels, malformed/missing rod fields, source/K drift, signed flow/ledger and proof-row forgeries, plus **legitimate source orientation reversals**; the reversed signed interval follows `[-q_hi,-q_lo]` and valid physical solutions are preserved. **No residual bypass found for the original F02 direction/G/source-balance attacks.**

## NEW BLOCKER — declared proof precision can be contradicted by a coherent wide report

**Severity: material N8 evidence-semantics defect (F01-adjacent), not a false heat-law calculation.** The nonempty proof check verifies only that
`F(proof["maximumPermittedEnclosureWidthK"]) == F(1, 10**6)`
in [`_check_source_and_node_report`](https://github.com/physicsvigilante/sim_heat/blob/23172ce2cd7a18466d2bf176b83064e6cd49bac1/qualification/h1_n8/corner_replay.py#L174-L189). The later [universal-envelope comparison](https://github.com/physicsvigilante/sim_heat/blob/23172ce2cd7a18466d2bf176b83064e6cd49bac1/qualification/h1_n8/corner_replay.py#L475-L493) enforces only `reported_lo <= certified_lo <= certified_hi <= reported_hi`; it **does not** enforce `reported_hi-reported_lo <= maximumPermittedEnclosureWidthK`. The signed physical report checker rebuilds flows from whatever wider enclosure is supplied, so updating the duplicated enclosures and dependent flux/ledger ranges consistently can evade all checks. Sixteen-corner containment likewise allows such conservative widening.

**Concrete, reproducible source-path counterexample (existing `area_chain()` fixture):** The one-junction source has fixed `Hot=410 K`, `Cold=300 K`, `G_A=1 W/K` along Hot→J, and `G_B=2 W/K` along J→Cold. Its exact junction temperature is `1010/3 K`, with true oriented heat flows `220/3 W` on both rods. The genuine N7 report has singleton J interval. Starting from it, replace only the following **report data**, leaving the source bytes, SHA, proof midpoint/radius/residual/authority fields and physical rod geometry/G untouched:

```python
from copy import deepcopy
from fractions import Fraction as F
from qualification.h1_n8.tests.test_corner_replay import area_chain, serialize
from qualification.h1_n7 import verified_junctions as n7
from qualification.h1_n8 import corner_replay as n8

raw, pin = serialize(area_chain())
good = n7.solve_snapshot(raw, expected_sha256=pin,
                         body_node_temperatures={})
fake = deepcopy(good)
for key in ("junctionTemperatureEnclosuresK",
            "allNodeTemperatureKExactPhysicalEnclosures"):
    fake[key]["J"] = ["300", "410"]
fake["proof"]["rows"][0]["enclosureK"] = ["300", "410"]
fake["rodHeatFlows"]["A"]["heatFlowWExactPhysicalEnclosure"] = ["0", "110"]
fake["rodHeatFlows"]["B"]["heatFlowWExactPhysicalEnclosure"] = ["0", "220"]
for node, bounds in (("Hot", ["0", "110"]),
                     ("Cold", ["-220", "0"]),
                     ("J", ["-110", "220"])):
    fake["nodeBalanceEnclosures"][node][
        "outwardHeatFlowWIndependentIntervalSum"] = bounds
fake["nodeBalanceEnclosures"]["Hot"]["boundarySupplyWEnclosure"] = ["0", "110"]
fake["nodeBalanceEnclosures"]["Cold"]["boundarySupplyWEnclosure"] = ["-220", "0"]

assert F(fake["proof"]["maximumPermittedEnclosureWidthK"]) == F(1, 10**6)
assert F(fake["junctionTemperatureEnclosuresK"]["J"][1]) - F(
    fake["junctionTemperatureEnclosuresK"]["J"][0]) == 110
# Source-path prediction to verify with a new dedicated regression:
# n8.replay(raw, expected_sha256=pin,
#           body_node_temperatures={}, reported=fake)
# -> OFFLINE_INDEPENDENT_SOURCE_CORNER_AND_SIGNED_BARRIER_CROSSCHECK_PASS
```

I **personally computed** the independent exact values and interval ledger: `q_A=[0,110]`, `q_B=[0,220]`, outward `Hot=[0,110]`, `Cold=[-220,0]`, `J=[-110,220]`. The true physical solution and corner lie inside these intervals; residual and barrier rows are unchanged (zero-width exact area-only case), and the junction interval lies inside the passive source-temperature range. Consequently the current checks have no path to refuse the **110 K** reported enclosure despite the report's claimed **0.000001 K** maximum. This is a **static predicted acceptance**, not a claimed local execution of `n8.replay`.

The problem is not the conservativeness of a wide thermal interval; it is N8 announcing successful verification of a purported **N7/1 report** that contradicts its own declared precision bound. This is the same class of unchecked report-evidence semantics that motivated the review gate.

**Required bounded correction:** In the N8 checking-only path, enforce for **every** nonempty junction `0 <= published_hi-published_lo <= F(proof["maximumPermittedEnclosureWidthK"])` using already validated exact rationals; refuse as `CornerRefusal`. Add a targeted regression that makes all three J aliases, both rod flows and node/boundary ledgers mutually consistent as above, to prove the new width guard is responsible for rejection (not an earlier shape/alias mismatch). Confirm normal four-junction, area-chain, original T1, zero-junction and legitimate orientation-reversal cases still pass. Do **not** rewrite N7 mathematical source or broaden native scope.

## Evidence and gates

I independently fetched GitHub Actions run/job records and decoded logs. The genuine **tests-only** [RED 44552428810](https://github.com/physicsvigilante/sim_heat/actions/runs/44552428810) at `9efc0bffca7069c8bd4a83b619b27a20f3139e97` showed **41 failed adversarial assertions + one malformed-report error** against the old checker; an earlier syntax-only red was not a valid reproduction. The corrected [PUSH 44554633917](https://github.com/physicsvigilante/sim_heat/actions/runs/44554633917) and [PR 44554647695](https://github.com/physicsvigilante/sim_heat/actions/runs/44554647695) both have head SHA `23172ce2...`, conclude **SUCCESS**, and their logs show **16 N8 +13 N7+13 N6+11 N5+15 N4+12 N3+16 N2+17 N1 interval+34 plan+152 H1 = 299 distinct offline tests** per job. These are the developer's hosted tests, **not** tests I ran locally; the second workflow repeats the same test inventory, not 598 unique tests. They do not include the coordinated width counterexample above.

Hosted job artifacts: PUSH `14544661914`, GitHub-reported SHA256 `37ccc620c827f3dd67cc6c1eae35564b4f175d53d59ce0ad0067282cf3d4757a`; PR `14544696768`, GitHub-reported SHA256 `3a15a78162d6fd874cfad0e042c7bab5db07324b167be45db0c705c2c92391eb`. These are metadata digests, **not** personally downloaded/rehashed ZIPs. CI includes inherited source/diff identity, docs parity, seven historical 100× source-physical reference refusals and eight native blocker holds.

**Final disposition:** **CHANGES REQUESTED** for the targeted **N8 evidence-verification contract**, despite the two original forgery classes being materially corrected. Add the one narrow report-width guard and a true coordinated negative test, then seek another exact-head scoped review. Preserve review-01 and this new review as immutable historical decisions. Keep PR69 and stacked PR68/67/66/65/64/63/62/60/59 draft/unmerged. No independent original-source/owner manifest, OMC/MSL/host attestation, native MAT trace, full 77+8+5 trajectory certification, historical C1 rewrite, reference promotion, deployment or merge authority is granted.

**Signed:** Chat B — independent R2 reviewer, pinned to source HEAD `23172ce2cd7a18466d2bf176b83064e6cd49bac1`.