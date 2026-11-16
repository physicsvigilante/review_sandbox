# Chat B independent-context R2 review — EM Fields PR #20

**Outcome: changes-requested (scoped R2).** The pinned source has strong ordinary-regression, provenance, and independently reproduced physical-value evidence, but its comparison preflight can certify an internally inconsistent trajectory selection as complete. **Do not merge on this review.**

## Identity, scope and independence

- **Project/source:** physicsvigilante/emfeeld, [draft PR #20](https://github.com/physicsvigilante/emfeeld/pull/20).
- **Reviewed base:** 1b7d5c652bb635723746b3c6ce77baee536b997e.
- **Exactly reviewed head:** 4b51a833c0ed5ef189becf5881064d1b516df21b.
- **Canonical source Git tree:** 8e8999b40949d1128050cf66c0440fb07bb08670, confirmed against GitHub's Git-commit object and the source snapshot. [Pinned comparison](https://github.com/physicsvigilante/emfeeld/compare/1b7d5c652bb635723746b3c6ce77baee536b997e...4b51a833c0ed5ef189becf5881064d1b516df21b).
- **Reviewer:** Chat B, separate-context ChatGPT GPT-6; not an independent human or a proven different underlying model family.
- **Date/time:** 2026-11-16, approximately 14:20 IST.
- **Risk:** R2, saved measurement/evidence meaning. Source PR remains draft and unmerged. **No source repository files, branches, PR metadata, native originals, or historical evidence were modified.** All tampering experiments operated on disposable local copies extracted from qualified artifacts.
- **Review sources:** central REQUEST.md and REVIEWER-PROMPT-01.md, protocol/risk policy, source AGENTS.md, physics/model/contracts, actual pinned 449-line comparison module, existing lower/inspect/sample selection code, and the six-file PR change list. No other Chat B reviews were used.

## Verdict rationale

**Confirmed blocker F-01:** A native result can still carry the exact authored selector in its selection receipt while claiming an entirely different actual saved sample. The comparison verifies that the substituted values and times are in the NPZ, but never verifies that the reported sample index was the sample selected by the immutable native request. Re-sealing both copies produced an overall **complete** comparison and a **complete** deterministic inspection at **0.0 s**, although the native packets requested **2.0 s**. This is not merely floating-point time ambiguity; it changes the physical measurement being compared.

The attack assumes a writer able to regenerate **unkeyed** native and outer SHA inventories, a limitation already disclosed by the project. It does **not** allege a cryptographic authenticity guarantee. The actionable defect is narrower: the implementation advertises internal native request/result/NPZ consistency checks even after re-sealing, but omits one necessary selection constraint. Repair that constraint and add its test before acceptance.

## Findings

### F-01 — BLOCKER — The selected NPZ row is not bound to the authored time selector

**Source:** src/emfeeld/scenario_comparisons.py lines 159–166, 230–256, 303–327, 347–415; compare src/emfeeld/trajectory_samples.py lines 69–92 and 160–179.

**Reproduction (new Chat B test A1 and A2, actually executed):** Start with the Linux archived **scenario-comparisons/E1** input runs and untouched comparison/request.json (release artifact 14208856524). LEFT packet requests position and velocity at sample index 50 = 2.0 s; RIGHT requests sample index 25 = 2.0 s. Copy both native runs to disposable paths. In the copied native/result.json trajectory_sample rows, change reported sample_index, time_s and value to those from the **same particle and quantity at index 0** in each original saved trajectories.npz. **Leave native/packet.json and each result's selection field unchanged** (still 50 and 25). Recompute native/integrity.json's result.json digest and each outer integrity.json, leaving both run.json files and their SHA-pinned comparison request untouched.

**Expected:** Hard invalid_native_run, before output publication: saved result selection conflicts with the immutable native request, even though its substituted time and state exist in the NPZ. In particular, an exact sample_index request is not a request for any arbitrary index.

**Observed:**
- **A1** (RIGHT only changed to index 0): source preflight succeeded; result was **partial / different_saved_time**, instead of rejecting the inconsistent source.
- **A2** (both sides changed to index 0): **compare returned complete; inspect returned complete; motion context time_s = 0.0**, and both motion differences became zero. At original requested 2.0 s, E1 has nonzero differences in position and velocity. No source GitHub files were touched.
- The source compares row.selection to the packet's selector, and row.sample_index/time_s/value to the NPZ, but never checks **packet selector → selected index/time/offset**.

**Reproducible minimal script** (execute from a checkout of the pinned source with numpy installed; set ROOT to the extracted Linux release archive's scenario-comparisons/E1 directory):

~~~python
from pathlib import Path
from tempfile import TemporaryDirectory
import shutil
import numpy as np
from emfeeld.model_revisions import decode, encode, sha256
from emfeeld.model_runs import _inventory
from emfeeld.scenario_comparisons import compare, inspect

ROOT = Path("/path/to/extracted/scenario-comparisons/E1")
with TemporaryDirectory() as temp:
    t = Path(temp)
    runs = {}
    for side in ("left", "right"):
        folder = t / side
        shutil.copytree(ROOT / side, folder)
        native = folder / "native"
        report_path = native / "result.json"
        report = decode(report_path.read_bytes())
        with np.load(native / "trajectories.npz", allow_pickle=False) as npz:
            for row in report["results"]:
                if row["type"] != "trajectory_sample":
                    continue
                idx = row["particle_index"]
                component = "position_m" if row["quantity"] == "position" else "velocity_m_s"
                row["sample_index"] = 0
                row["time_s"] = float(npz[f"p{idx}_time_s"][0])
                row["value"] = [float(x) for x in npz[f"p{idx}_{component}"][0]]
        report_path.write_bytes(encode(report))
        inventory_path = native / "integrity.json"
        inv = decode(inventory_path.read_bytes())
        inv["files"]["result.json"] = sha256(report_path.read_bytes())
        inventory_path.write_bytes(encode(inv))
        (folder / "integrity.json").write_bytes(encode({"files": _inventory(folder)}))
        runs[side] = folder
    out = t / "new-comparison"
    result = compare(ROOT / "comparison/request.json", left=runs["left"],
                     right=runs["right"], output=out)
    assert result["status"] == "complete"             # Observed wrong acceptance
    assert result["comparisons"][3]["context"]["time_s"] == 0.0
    assert inspect(out, left=runs["left"], right=runs["right"])["status"] == "complete"
~~~

**Required correction:** In source-native preflight, independently rederive each reported trajectory sample selector against the captured NPZ time grid and immutable native packet. For direct index require row.sample_index = requested sample_index. For exact requested time require exact saved-time membership. For nearest, reproduce the native earlier-index tie-break, selected index, requested tolerance, time_s and time_offset_s; verify all recorded selection receipts. Reject contradictions as invalid native run, not different_saved_time or numeric_range. Test both one-sided and coordinated changes (A1/A2) and ensure no new comparison directory is created on invalid preflight.

### F-02 — MAJOR — Global complete-run preflight does not validate unselected native result/NPZ contradictions

**Source:** src/emfeeld/scenario_comparisons.py lines 90–175 and 259–344.

**Reproduction (new Chat B tests A3/A4):** Using a copied complete E1 RIGHT run, alter a native result's saved **trajectory position component by +100 m**, leaving its NPZ unchanged; re-seal both inventories. Submit a valid comparison spec requesting **only an unrelated field_vector**. Observed **complete**, although the claimed complete source run contains an internally contradictory trajectory result. In a separate copy, multiply the first RIGHT field observation's reported magnitude by 20, re-seal, and compare **that field as a vector only**; observed **complete** despite inconsistent saved vector/magnitude. When a corrupted magnitude was actually chosen as a magnitude pair, it correctly returned **partial/numeric_range**.

**Expected:** The globally complete native-run preflight should not accept internally contradictory native outcomes simply because those particular observations are not selected. Otherwise the same re-sealed source is accepted or refused depending on the arbitrary comparison pair list. This particularly weakens the claimed distinction between a *globally malformed run* and an *item-level unavailable* comparison.

**Required correction:** During global source preflight, validate all recorded successful trajectory_sample rows against their actual selected NPZ time/values and selector (not only pairs that happen to be motion comparisons), and check field vector/magnitude consistency for eligible native field rows. Preserve the distinct valid behavior of **unknown_operand** for genuinely absent observations in an otherwise sound run. Add field-only-versus-corrupted-unselected-trajectory and vector-only-versus-corrupted-magnitude regressions. An implementation may choose a bounded optimized verification, but must uphold the complete-source meaning in the frozen contract.

### F-03 — MINOR — False-looking nonboolean check receipt slips past native completion validation

**Source:** src/emfeeld/scenario_comparisons.py lines 148–157; boolean test uses identity with False.

**Reproduction (new Chat B test A6):** Add **{"passed": 0}** to a copied successful E1 field native-result check, re-seal native and outer inventories, and compare that field. Observed **complete**. The code recognizes the integer 0 as neither a malformed check flag nor a failed boolean, because **0 is False** is false in Python. This is malformed/ambiguous saved check evidence; the same field with explicit boolean false is rejected as intended.

**Recommendation:** If a check is present, validate its allowed structure and require passed to be a boolean with true value (or a strictly documented native check shape), rather than only rejecting identity-equal False. This is a narrowly scoped evidence-hardening correction; no claim of ordinary untampered numerical failure is made.

## Independent tests, physics checks and evidence

1. **Exact-source provenance (executed by Chat B).** Downloaded source snapshot artifact **14208610779**. Original ZIP SHA256: **30aa83f6c0c1abe38bd6848c891929ebb6a9ae95d5217fd13d13ee56dedb923c**; inner tar SHA256: **657ef97b3c41ebf08cf653f90ed2fead563d774bab9e86758fcea9e0fcd1f502**. Verified **all 341 archived regular source files** against the 341 expected Git blob SHA-1 identities (zero missing/mismatched), and verified GitHub commit's tree **8e8999b40949d1128050cf66c0440fb07bb08670**. Snapshot checkout is a merge-preview of the identical tree, not a different source implementation.
2. **Tests actually rerun.** Linux container, **Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0, pytest 9.0.2**: exact archived source **33/33 focused tests passed**; independently invoked **python -m pytest -q -W error tests**: **1,375/1,375 passed in 98.13 s**. These are **replays of author-authored tests**, not novel Chat B test design. Novel A1–A6 and separate path/interruption probes described here were authored and executed by Chat B against the extracted source. No code changes made in the source snapshot beyond disposable copied run evidence.
3. **Release artifacts (independently inspected).** Linux artifact **14208856524**, raw ZIP SHA256 **fd48cb2a38cadcf155b59f2c5e6ae4ac263d3cd5acb2425b4cba815796b53afd**; Windows artifact **14208673470**, SHA256 **bb81092317fa9fcb7d1ea0268727eaefd963e5a94aa4afb6fc05c0a7346b712c**. Both exact hashes verified; **1,803 entries in each**, no duplicate names, all CRC checks passed. Executed pinned **inspect_run** on each of six retained source-native runs per OS and pinned **scenario_comparisons.inspect** on all three archived comparisons per OS. Per OS: **E1 5/5 complete**, **G1 7 fulfilled + 1 correctly unavailable/unknown_operand (added body_3), overall partial**, **T1 4/4 complete**. Both comparisons' run pins and inventories survived the read-only replay.
4. **Independent physical calculation (not Chat A's checker).** Authored separate numpy/SciPy reference formulas directly from archived packets: electric infinite line + uniform field, gravity point + homogeneous solid sphere (interior/exterior), and charged thin shell + central point (interior/exterior), with corresponding potential functions. Independently integrated nonrelativistic test-particle equations using newly written right-hand sides and a high-accuracy DOP853 solve_ivp. Across the two OS archives: **48 static native observation rows**, **28 motion observation rows**, **32 independently reconstructed successful signed comparison values** verified. Maximum absolute discrepancy versus archived records was **4.44e-16 static**, **2.44e-15 trajectory**, and **3.33e-15 signed differences**, in the respective SI quantities; these are **not** rigorous solver error bounds or 108 distinct physical experiments (OS copies share authored cases). E1 axial position z=0.5 m and velocity v_z=0.4 m/s at t=2 s also follow analytically from q/m=1, E_z=0.15 N/C, z0=0 and v_z0=0.1 m/s.
5. **Positive fresh adversarial checks.** Injected a simulated I/O exception exactly when writing comparison result.json: output retained **request.json + started.json (pending)**, no result/integrity success marker, unchanged input run hashes; second attempt to reuse output was refused. Symlink aliases from a fresh output parent into (i) one source run and (ii) an append-only model store were both refused. Corrupting the *actually selected* field magnitude was correctly typed **unavailable/numeric_range**, and the inspector recomputed saved successful/partial aggregates in ordinary archives.
6. **First attempts / negative evidence preserved.** A preliminary magnitude test changed **R-field-0** but requested the different **R-field-1** magnitude, so the observed complete response was **a reviewer test setup mistake**, not a production bug. Repeating with R-field-1 yielded the expected partial/numeric_range refusal. A1–A4/A6 outputs above remain adverse results; they have not been relabelled passing. First failures in the author packet (including interrupted local full replay) are not overwritten or promoted to a pass.

**Hosted CI independently checked by querying GitHub workflow records:** [clean Linux/Windows #43829796171](https://github.com/physicsvigilante/emfeeld/actions/runs/43829796171), [real-PyVista #43829796174](https://github.com/physicsvigilante/emfeeld/actions/runs/43829796174), [source snapshot #43829796198](https://github.com/physicsvigilante/emfeeld/actions/runs/43829796198) all show **completed/success, exact head 4b51a833...**; Linux and Windows job metadata are successful. Their CI execution is **author-authored/hosted**, not personally rerun Windows desktop or independent browser manipulation.

## Separate scope judgments

| Dimension | Judgment | Basis |
| --- | --- | --- |
| Source interpretation fidelity | **Qualified/limited** | Named model root, explicit comparison pairs, world point and ordered endpoints, no positional particle retargeting for unchanged genuine runs; no teacher independently adjudicated the source hypotheses. |
| Physical/numerical correctness | **Pass for tested E1/G1/T1 values** | Independent ideal-source fields/potentials and fresh equations-of-motion integration closely reproduce 48 static, 28 saved motion rows and 32 signed comparisons across two OS evidence sets. Does not establish arbitrary horizons or solver error bounds. |
| Native simulation/observable coverage | **Pass within bounded E1/G1/T1 coverage** | Six complete source native runs per OS, archived inspector replay; no new native integration was performed as part of comparison. New source arrangements beyond these cases remain untested. |
| Evidence integrity and provenance | **Fail (F-01 blocker; F-02 major)** | Original byte inventories and SHA bindings validate, but internally inconsistent re-sealed selector/result evidence can still produce complete comparisons and complete inspection. |
| Teacher-facing usefulness | **Unknown** | No fresh classroom use, manual Windows mouse testing, or teacher interpretation evaluation. |
| Textbook-answer completeness | **Not applicable** | This is a bounded read-only cross-scenario measurement feature, not a textbook-answer solver. |

## Limits and smallest next gate

The fresh adversarial tests intentionally re-signed **copied unkeyed** source inventories to test semantic coherence; they do not claim the original Linux/Windows artifacts are corrupt, and they cannot prove malicious-data authentication. They also do not prove a general physics failure in the unchanged field or integrator engine. Linux local tests used Python 3.13.5; Windows behavior was read from hosted CI and saved ZIPs, not independently executed on Windows. No UI or classroom acceptance is inferred.

**Minimum fix/gate:** Correct selector-to-sample preflight and complete-native-record consistency, add regressions corresponding to A1/A2/A3/A4 and malformed check flag A6, rerun focused and full exact-new-head tests plus archive qualification, and request **targeted Chat B re-review** of those bindings. Preserve this report bound to head **4b51a833...**, all first failures, and all existing released artifacts. Any new source head requires new exact-head CI. **The owner must separately authorize any future source merge; this review neither approves nor performs one.**
