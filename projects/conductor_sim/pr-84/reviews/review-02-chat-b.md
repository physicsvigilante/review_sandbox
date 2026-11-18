# Chat B R2 independent targeted review 02 — conductor_sim PR #84 / M36a

**Outcome: INSUFFICIENT-EVIDENCE for the specified independent-execution gate.** This is **not** a demonstrated source defect or a request to redo successful CI. The five corrections are supported by source inspection and current-head GitHub CI, with F-01 and F-05 resolved by directly observed evidence. However, I could not execute independently authored F-02/F-03/F-04 hostile inputs **against the pinned Python auditor** or independently stream/hash/tamper the original PDF bytes. My independently executed adversarial reference probes were JavaScript *shadow* assertions against the actual pinned inventory data and literal source contracts, not invocation of the Python implementation. The prompt expressly prohibits a fabricated PASS if these probes cannot be executed. The source PR must remain draft and unmerged pending narrow independent execution and separate owner approval.

| Identity / scope | Observed |
| --- | --- |
| Reviewer | Chat B, separate GPT-6 conversation; automated LLM reviewer, not human scientific certification |
| Review date | 2026-11-18 |
| Project / source PR | [physicsvigilante/conductor_sim #84](https://github.com/physicsvigilante/conductor_sim/pull/84) |
| Risk / scope | R2 targeted **evidence/source-interpretation correction only**; NOT original JEE-30 physics certification |
| Exactly checked HEAD | `527e6cee5f96a011729d2d0a668da9b688ab03d0` |
| Native Git TREE, read via GitHub Git commit API | `fff1c03417c857b6cce04156427e3eeaf9919a65` |
| Released base | `73e076cf7eaf7fefbae2b24afc1f54ff8f0b6fc6` (tree `89363a917e3862d663d934501a1b5cd8a22a84c0`) |
| Preimplementation frozen charter | `13eb3afde0efac049387d90a64eff44227f2acb4` |
| Previously reviewed HEAD / verdict | `b6d7fccad26666100b172097b01738aedc8c9cf6` / CHANGES REQUESTED, retained in [review 01](review-01-chat-b.md) |
| PR state at repeated checks | **Open, draft, unmerged**, with exactly the pinned HEAD/base |
| Production files, source branch, CI actions changed by reviewer | **None**. No merge, mark-ready, source commits, reruns, installations or PR approvals |

Read [REQUEST-03](../REQUEST-03.md), [STATUS](../STATUS.md), [original review 01](review-01-chat-b.md), [protocol](https://github.com/physicsvigilante/review_sandbox/blob/main/PROTOCOL.md), risk policy, report template, pinned source auditor, all 23 Python test instances, workflow YAML, charter, evidence matrix, M21a historical matrix and the evaluation contract. Compared the Git trees, diffs and actual GitHub job steps and logs. Local shell cannot resolve GitHub; connector can read GitHub UTF-8 files and metadata but cannot stream the two binary source PDFs into a runnable checkout.

## F-01 — RESOLVED: actual full visualization, not merely a longer timeout

- Historical full visualization [run 44156812874](https://github.com/physicsvigilante/conductor_sim/actions/runs/44156812874), on `b6d7fcc...`, is **CANCELLED**, not success. Job `134299626630`: step 54, “M15 nested cavity with shell constraints”, was cancelled; steps 55–69 containing late M15/M16/M17/M26/M27 cases were **SKIPPED**. Preserve this historical negative result.
- Current pinned [`.github/workflows/visualization.yml`](https://github.com/physicsvigilante/conductor_sim/blob/527e6cee5f96a011729d2d0a668da9b688ab03d0/.github/workflows/visualization.yml#L1-L157) has `timeout-minutes: 25` at line 13; source comparison to released base changes only three added lines and one removed line in that workflow. Its 60+ previous source/browser steps are retained.
- **Actual current-head full visualization**: [run 44235741394](https://github.com/physicsvigilante/conductor_sim/actions/runs/44235741394), job `134571324726`, completed **SUCCESS**. All **73 reported job steps** were success; **none skipped/cancelled/failed**. Specifically M15 nested/centered/multiple-source work (steps 54–59), M16 electron and timing (60–63), M17 trajectories (64–67), M26a (68), and M27a (69) all actually ran successfully.
- Independent evidence: fetched both jobs and enumerated their exact completed/skipped step conclusions. Other green browser workflows were not substituted for this full-workflow success.

## F-02 — SOURCE GUARD PRESENT; independent Python execution NOT performed

Pinned [`tools/m36a_jee30_audit.py` lines 29–42, 136–141](https://github.com/physicsvigilante/conductor_sim/blob/527e6cee5f96a011729d2d0a668da9b688ab03d0/tools/m36a_jee30_audit.py#L29-L42) uses an exact literal identity for the 30th apparatus: ID, full official 2021 source string, PDF page 16, printed “Paper 1 Questions 9–10 (one two-charge apparatus)”, problem family, 2021 provenance, null historical tier and `official_apparatus={"paper":"JEE Advanced 2021 Paper 1","question_ids":["Q9","Q10"]}`. The 29 historical case identity fields and order are compared fieldwise at lines 114–135.

Independent reference work: fetched both actual pinned JSON inventories, checked all **29 × 7** historical identity-field comparisons with **zero differences**, exactly one new official apparatus, and independently executed JavaScript assertions using a separate literal-contract model. The legitimate original record was accepted by that model; independently modified test records containing `fabricated-source.pdf#legacy-archive`, printed extra Q11, `["Q9","Q10","Q11"]`, 2020 provenance and wrong page were all rejected by the model. **These outcomes do not establish that the Python implementation rejected these new reviewer-authored records.**

Actual source-head GitHub Python 3.10/3.12 log shows **23 dots** for `tests/test_m36a_jee30_audit.py`, including author's 2021 source/member rejection tests (7 parametrized variants). This is genuine CI execution, not Chat B's independent execution. No F-02 defect observed; specified independent Python hostile control is still unexecuted by reviewer.

## F-03 — SOURCE GUARD PRESENT; independent Python execution NOT performed

Pinned auditor lines 44–46 enumerate the three deliberate local-3D refusals: `p11-linked-28`, `p70-cavity-offset` and `p70-three-cavities`. Lines 149–152 reject any non-`unsupported` route for those IDs **before** the 24/3/3 aggregate is accepted. The rejected physical claim is a *local nonconcentric induced field or surface-density distribution*, not a permissible Gauss-law total-charge scalar.

I independently executed count-preserving status-swap probes in the JavaScript reference model for **each** required refusal (change that case to `supported_scoped` and an independently chosen supported case to `unsupported`). Counts remained exactly **24 supported_scoped / 3 partial / 3 unsupported**, yet all three tampered datasets failed the model's frozen-ID contract. The actual Python module was **not** called on these reviewer-authored swaps. Author's corresponding three parametrized cases passed in source-head GitHub CI. No demonstrated F-03 source defect; execution gate remains.

## F-04 — ACTUAL BYTE-HASH CODE AND IMMUTABLE GIT BLOBS VERIFIED; independent binary tamper NOT performed

Pinned auditor lines 22–27 and 74–82 define fixed literal M21a SHA-256 digests and stream real file bytes in 1 MiB chunks. At lines 107–112 it requires *both* metadata records to match the immutable literal values **and** verifies the real PDF bytes. This rejects the prior false equivalence “two matching JSON SHA strings mean the PDFs are genuine”.

Verified source-tree versus base-tree original PDF objects (not just metadata strings):

| File | Source = released-base Git blob SHA | Bytes | Frozen SHA-256 metadata |
| --- | --- | ---: | --- |
| `02_conductors_half_size.pdf` | `90d8869b0f01cc2ea13f83721985a5d8419f1d0e` | 20,685,051 | `9dff3c02a9f1848d2c3d99cb1a6e7a44dc7f5a51f7a3a2b8cc92d10ce1fbca5d` |
| `POTENTIAL_CONDUCTORS1.pdf` | `03e573af4038073a3b1a7b0ae67ef90c93fe1c24` | 9,063,758 | `8d0d9b5cf821219058cfc4b7685a39b777e460944df44c3f9cffcb68157a60e5` |

Historical `docs/m21a_coverage.json` is itself byte-identical to base (Git blob `5c0ecb1633e691b1175c4095b5307bdc1bfa3740`). Neither source PDF is changed by this PR; the entire source diff is six files and contains no production-physics modifications.

An independently authored **metadata-collusion** JavaScript reference probe changed both JSON digest strings to the same false 64-character value and demonstrated disagreement with the frozen literal. Python-head CI actually passed author's metadata-collusion and PDF-copy tamper cases (tests lines 134–157). **I did not calculate the real PDF SHA-256 myself or modify a binary copy and execute the pinned `verify_pdf_bytes` function; original bytes were not available through this GitHub text-only interface.** Git blob object equality + developer CI are strong corroboration, but do not fulfill the prompt's independent byte-tamper execution requirement. No source defect demonstrated.

## F-05 — RESOLVED: correct reviewer packet links

Live [`STATUS.md`](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/conductor_sim/pr-84/STATUS.md) preserves its historical `REVIEWER-PROMPT-02.md` link to **Prompt 02**, not Prompt 01, and the latest handoff section explicitly links `REQUEST-03.md` and `REVIEWER-PROMPT-03.md` as the only current packet. [Prompt 03](../REVIEWER-PROMPT-03.md) pins this exact HEAD/tree. Older review 01 is preserved against its old source; no historical evidence was rewritten.

## Full current-HEAD CI — verified live, all 16/16 success

Live GitHub REST list filtered by **exact `head_sha=527e6cee...`** returned **16 runs and 16 completed/success**, including all relevant PR and push workflows.

| Current-head evidence | Actual observed |
| --- | --- |
| [PR Python checks 44235741497](https://github.com/physicsvigilante/conductor_sim/actions/runs/44235741497) | 3.10 **2076 passed, 97 skipped, 17 warnings**; 3.12 **2076 passed, 97 skipped, 17 warnings**; 23 M36a instances pass in each. Both matrix jobs completed SUCCESS. |
| [Push Python checks 44235736571](https://github.com/physicsvigilante/conductor_sim/actions/runs/44235736571) | Both 3.10 and 3.12 SUCCESS. |
| [Full visualization 44235741394](https://github.com/physicsvigilante/conductor_sim/actions/runs/44235741394) | 73/73 job steps SUCCESS including formerly skipped sentinel cases; non-FEMM pytest **2076 passed, 97 deselected**; genuine Chromium commands executed. |
| [Real FEMM 5 44235741552](https://github.com/physicsvigilante/conductor_sim/actions/runs/44235741552) | Pinned FEMM 5 source `7c31ccfa3d4bcda8123d822cdda31fce929f672e` fetched and built; real electrostatics **97 passed** (not the Python matrix's 97 skips); authored M6b export and Chromium inspection steps SUCCESS. |
| Remaining 12 PR workflows | **All SUCCESS:** M15c, M17c, M18b, M18c, M19a, M19b, M19e, M20a, M21d, M21e, M22a and M35a. |
| [First source Python 44155780188](https://github.com/physicsvigilante/conductor_sim/actions/runs/44155780188) | Historical **failure** at `796d3f31...`; original Python 3.12 had eight M36a metadata failures; the 3.10 job was cancelled. |
| [Previous source full visualization 44156812874](https://github.com/physicsvigilante/conductor_sim/actions/runs/44156812874) | Historical **CANCELLED** with late steps skipped, not silently turned into a pass. |

The 23 test instances are the author's source-pinned automated tests, not 23 independent Chat B cases. Python skips concern unavailable live-FEMM bindings in ordinary matrices; the separate real FEMM run genuinely executed 97 integration tests. None of these CI results is 30 independent JEE source-specific replays.

## Independently authored control script — **PROPOSED, NOT EXECUTED**

The smallest remaining evidence is an independent execution of this *new* clean-checkout Python control, outside the implementer's existing pytest file. The original checks below deliberately differ from the author's cases (extra Q11 while retaining the original two, a different supported-case donor, midpoint byte flip for **both** PDFs). Execute at the pinned HEAD with a local checkout or isolated GitHub-hosted reviewer runner and retain stdout and exact source SHA/tree. No source modification is required.

~~~python
from copy import deepcopy
from pathlib import Path
from tempfile import TemporaryDirectory
import shutil

from tools.m36a_jee30_audit import (
    ROOT, SOURCE_PDF_SHA256, audit_inventory, load_inventory,
    verify_pdf_bytes,
)

original = load_inventory(ROOT / "docs/m36a_jee30_coverage.json")
historic = load_inventory(ROOT / "docs/m21a_coverage.json")
assert audit_inventory(original, historic)["frozen_apparatus_anchors"] == 30

def reject(label, callback, message):
    try:
        callback()
    except ValueError as exc:
        assert message in str(exc), (label, str(exc))
        print("EXPECTED REJECT:", label)
    else:
        raise AssertionError("FALSE ACCEPT: " + label)

for name, field, value in [
    ("fabricated source", "source", "fabricated-source.pdf#legacy-archive"),
    ("printed extra Q11", "printed_anchor",
     "Paper 1 Questions 9–10 and 11 (one two-charge apparatus)"),
    ("2021 plus Q11", "official_apparatus",
     {"paper": "JEE Advanced 2021 Paper 1",
      "question_ids": ["Q9", "Q10", "Q11"]}),
]:
    forged = deepcopy(original)
    forged["cases"][-1][field] = value
    reject(name, lambda f=forged: audit_inventory(f, historic),
           "2021 apparatus identity or grouping changed")

for refusal_id in ["p11-linked-28", "p70-cavity-offset",
                   "p70-three-cavities"]:
    forged = deepcopy(original)
    refusal = next(c for c in forged["cases"] if c["id"] == refusal_id)
    donor = next(c for c in forged["cases"]
                 if c["candidate_route"] == "supported_scoped"
                 and c["id"] != "p01-single-08")
    refusal["candidate_route"] = "supported_scoped"
    donor["candidate_route"] = "unsupported"
    assert sum(c["candidate_route"] == "unsupported"
               for c in forged["cases"]) == 3
    reject("balanced route swap " + refusal_id,
           lambda f=forged: audit_inventory(f, historic),
           "frozen local-3D refusal reclassified")

colluding = deepcopy(original)
colluding_old = deepcopy(historic)
name = "02_conductors_half_size.pdf"
colluding["frozen_baseline"]["original_pdf_sha256"][name] = "f" * 64
colluding_old["source_sha256"][name] = "f" * 64
reject("two matching forged metadata digests",
       lambda: audit_inventory(colluding, colluding_old),
       "historic PDF metadata differs")

with TemporaryDirectory() as directory:
    for filename, frozen_digest in SOURCE_PDF_SHA256.items():
        actual = ROOT / filename
        verify_pdf_bytes(actual, frozen_digest)
        copied = Path(directory) / filename
        shutil.copyfile(actual, copied)
        with copied.open("r+b") as handle:
            handle.seek(copied.stat().st_size // 2)
            old_byte = handle.read(1)
            assert old_byte
            handle.seek(-1, 1)
            handle.write(bytes([old_byte[0] ^ 0x01]))
        reject("midpoint byte flip " + filename,
               lambda p=copied, h=frozen_digest: verify_pdf_bytes(p, h),
               "source PDF bytes changed")

print("ALL NOVEL PYTHON CONTROLS PASSED")
~~~

**Reviewer execution disclosure:** Only the separate JavaScript reference guards against the **actual fetched JSON** were executed in this review: 1 legitimate apparatus acceptance, 5 independently modified official-identity rejects, 3 balanced local-3D route rejects, and 1 matching-false-digest reject. Ten such reference assertions passed. They are not evidence that the proposed Python script above ran. Neither an independent Python CLI nor `pytest tests/test_m36a_jee30_audit.py -q` was executed by this Chat B environment; those commands were exercised through the documented source CI, including its CLI smoke test.

## Scientific/evidence meaning and release recommendation

| Evaluation dimension | Scoped judgment and limit |
| --- | --- |
| Source interpretation fidelity | 29/29 inherited identity records unchanged; one official 2021 Q9+Q10 apparatus, not two solves; exact-label contract present; independent actual-Python mutation still needed. |
| Physical and numerical correctness | **Not evaluated by M36a as original-question replays.** Prior representative analytic checks exist, and existing CI passed, but no fresh original-JEE numerical verification can be inferred. |
| Simulation / observable coverage | **Provisional route hypotheses only:** 24 `supported_scoped`, 3 `partial`, 3 `unsupported`. Achieved source-specific original JEE replays: **0/30**. |
| Evidence integrity / provenance | Historical original failures retained; Git tree and two original PDF blobs equal base; literal SHA-256 byte verifier + CI tests exist; independent binary tamper has not been executed here. |
| Educational viewer usefulness | **Not newly evaluated for any of these 30 original problems.** Existing Chromium regressions do not turn into 30 inspected JEE demonstrations. |
| Optional textbook-answer completeness | Not attempted; distinct from physical fidelity and teaching acceptance. |

**Disposition:** The corrected source has no demonstrated newly found defect on F-01–F-05, and every current-head required CI run is successful. **INSUFFICIENT-EVIDENCE** rather than PASS solely because the requested novel controls have not been run against the actual pinned Python code and binary files independently of the implementer's CI. The minimal next step is to execute the proposed isolated Python script above against this exact source and report unedited expected-rejection output. If all pass, a narrow completion note/review can close the evidence gap without rerunning a broad scientific review unless the source changes. Keep PR #84 **draft/unmerged** until a documented no-blocker review and **separate owner approval**. After any owner-authorized exact-head merge, reconcile main tree and all actual main-push workflows. The original-problem source-specific replay and teacher-viewer exercise remains a separate next milestone.
