# Chat B independent R2 review 01 — emfeeld PR #33

**Verdict: CHANGES REQUESTED** — exact frozen candidate, not an approval to merge. **Reviewer:** Chat B, separate conversation and independently executed probes, 2026-11-17. This is a source-bound review of evidence provenance and physical-source interpretation, **not** human physics or teacher certification.

**Reviewed:** [source PR #33](https://github.com/physicsvigilante/emfeeld/pull/33), [Issue #30](https://github.com/physicsvigilante/emfeeld/issues/30), central [REQUEST](../REQUEST.md), [REVIEWER-PROMPT-01](../REVIEWER-PROMPT-01.md), [author archive audit](../AUTHOR-ARCHIVE-AUDIT-01.md), [protocol](../../../../PROTOCOL.md) and [R2 risk policy](../../../../REVIEW-RISK-POLICY.md). Read pinned AGENTS.md, the new contract and all four new files; consulted source physics, studies, validation, capability and viewer guidance.

## Exact source boundary and source CI

| Identity | Exact value / independently observed status |
| --- | --- |
| Source PR head | **ee54e96488e5cd9d2eb904abf65811627bfcc006** |
| Reconstructed Git tree | **b8581afb8816052980dc03be27a3ad8acf1dd447** |
| Original qualified PR #29 base | **3f1ec44a54b24b9f8275a98abf81126a9386bf61** |
| Original PR-CI merge preview | **821a1ffb85cdf1c57113531e70cb26f5b77ae5c1**, same exact tree, ordered parents [old base, reviewed head] |
| Later current main | **a18c26f050f5320ce8a9d61f7169e32cd6e31f38** (PR #32 already integrated independently) |
| PR state when reviewed | **OPEN / DRAFT / UNMERGED** |

The PR-to-base comparison shows **four added files, no edits to existing production physics, solver, sealed comparison, store or viewer**: one frozen question JSON, one evaluator, one test file, one contract. The only commit after original candidate 820c226... changes **tests/test_teacher_transfer_pilot_v1.py, +13/-1**. This is a test-harness correction, not a correction of native physics.

I verified [corrected Linux/Windows CI #44025432673](https://github.com/physicsvigilante/emfeeld/actions/runs/44025432673) against original per-job logs, not just PR text. Both Ubuntu and Windows completed successfully: **1,511 headless passed, 18 historical passed (one obsolete all-file freeze deselected), 33 real-PyVista passed**, per OS. Those counts do not double-count the 96 scenario-ensemble tests. [Separate real-PyVista #44025432632](https://github.com/physicsvigilante/emfeeld/actions/runs/44025432632) and [source snapshot #44025432672](https://github.com/physicsvigilante/emfeeld/actions/runs/44025432672) were successful at the corrected head.

Preserved negative history: the **earlier** [Windows run #44024622664](https://github.com/physicsvigilante/emfeeld/actions/runs/44024622664) at head 820c226... was genuinely **FAILURE: 1,510 passed, 1 failed** at the synthetic literal-backslash ZIP filename test. The original fixture was normalized by Windows ZipInfo, so the validator had been given safe metadata. Later success never retroactively changes that outcome. The +13/-1 corrected test supplies literal unsafe name metadata through the validator, with no changed production reader.

## Independently downloaded original artifacts and source reconstruction

I downloaded the actual GitHub Actions ZIP bytes to a disposable Linux reviewer environment, computed SHA256 for each **whole ZIP**, tested every member's CRC, checked unique/case-folded filenames and unsafe paths, and examined the original contents.

| Exact artifact | GitHub artifact ID | Independent raw ZIP SHA256 | CRC and inventory |
| --- | ---: | --- | --- |
| **Original PR #29 Linux release** | 14300302937 | 0654fa7d39249c4026945295ce15a18eae46a8598325e66d321cd515aa1e7f55 | **PASS**, 2,161 entries |
| **Original PR #29 Windows release** | 14301401780 | be72aef030afef113758a671aa93363b7e01af51ad9e79d942b91ea508c9a27e | **PASS**, 2,161 entries |
| Corrected PR #33 Linux | 14303630672 | 73e420e2e0a1993d1f96c429c7db5836106df3acd28eceb25e2bf807bf0ea1b4 | **PASS**, 2,161 entries |
| Corrected PR #33 Windows | 14302868857 | 4132455d5a0c0b8491ff236b15105a012d16720dbe3354fb9c9f01dc48979278 | **PASS**, 2,161 entries |
| Corrected PR #33 source snapshot | 14302339387 | 36daa3b71f09a7482e2c76555293bafce426e62cda12e2d4b0bb07fba3ad7eee | **PASS**, 4 entries |
| Corrected PR #33 viewer | 14302244999 | 509f2920e25c0aa88db921c50a79ec21bb952123e088b50a073e907da1ce3fd3 | **PASS**, 22 entries |

The **tested-source.tar** inside the actual source snapshot had SHA256 **b50e944c7025b1c9b748b575fd247207350d3d27b4413a9f4daf1f7123c6e914**. Independently extracting it, staging **352 tracked files** and running **git write-tree** produced exactly **b8581afb8816052980dc03be27a3ad8acf1dd447**. The frozen JSON fixture independently hashes to **536ada6775aa3effb7abafaef742f7cb0030ce4428bcecf1d4664e1025436008**.

The corrected Linux/Windows releases contain head-sha.txt **821a1ffb...** (the exact-tree merge preview); the **original** PR #29 releases contain head-sha.txt **3f1ec44...**. I did not confuse these distinct artifact families or review floating current main. The viewer report identifies preview **821a1ffb...** and **nine PASS offscreen cases**; all **17 PNG SHA256 receipts** match the original archived PNG bytes. Its own visual_inspection field remains **PENDING**. None of this demonstrates manual Windows mouse/pointer behavior, human visual acceptance or teacher effectiveness.

## Native transfer replay, original source receipts, independent physics reference

Reviewer environment: **Linux, CPython 3.13.5, NumPy 2.3.5, SciPy 1.17.0, pytest 9.0.2**; no Modelica, browser or user's local computer involved. Each original OS-produced artifact was **replayed on reviewer Linux** using the exact corrected-source evaluator, not executed on a new reviewer Windows machine:

    cd /tmp/review33-src
    PYTHONPATH=src python verification/teacher_transfer_pilot_v1.py /mnt/data/original-linux.zip --platform linux > /tmp/review33-linux-output.json
    PYTHONPATH=src python verification/teacher_transfer_pilot_v1.py /mnt/data/original-windows.zip --platform windows > /tmp/review33-windows-output.json

Both exit codes **0**, no stderr. Whole stdout SHA256 independently reproduced **Linux 0e0d0db21e19b5075df9be3069937f88156dbe914cd1cd0e987a0ba7cba3aab7** and **Windows 20615a519c9f674387ce6d9e29f307f8227c5e1f372441f077f2877a09e483bb**. I separately checked **43 direct original-archive SHA/field/receipt assertions per platform (86 total)**: parent run, selected per-member comparison request/result/integrity raw SHA, original left and right run bytes, corresponding signed original result and unit/context. Native inspection was not mocked on these real-release runs.

| Requested result | Original Linux and Windows measured outcome | Independent check |
| --- | --- | --- |
| E1 hypothesis-A | **-0.05458851160751549 N/C** | Analytic line-plus-uniform field magnitude, exact to shown precision |
| E1 hypothesis-B | **+0.18513207463551812 N/C** | Independent math gives +0.18513207463551817 N/C (difference about 5e-17 from float evaluation order) |
| G1 hypothesis-B newly introduced body_4 | **unavailable / unknown_operand / null**, global **partial** | Body absent in original baseline; right native run complete; not zero |
| T1 hypothesis-A | **+1.1741058461436236 V** | Independent static shell-plus-point potential, exact to shown precision |
| T1 hypothesis-B | **+1.513997527981914 V** | Independent static shell-plus-point potential, exact to shown precision |

E1's common fresh baseline absolute field magnitude is approximately **0.27591172093403593 N/C**; the signed changes are not negative field magnitudes. For T1, the recorded ordered endpoints are from **(0.4, 0.6, 0.3) m** to **(2.8, 0.25, 0.4) m**, and the source expression is **V(to) − V(from)**; both prescribed shell and point charge change in each independent alternative. I used the independently expressed analytic field of an infinite line plus a uniform field, and shell **kQ/max(r,R)** plus point **kq/r**, not the evaluator's physics engine. G1 preserves the single genuinely missing operand. **Four available signed measurements and one unavailable** are the complete scoped result, not five solved answers. Independent alternatives are not successive physical times or real charging/conductor polarization.

## Reviewer-owned adversarial execution (first-attempt evidence retained)

The first combined reviewer-authored **49-case** pytest invocation hit the execution timeout **without a completed suite verdict**; its progress log recorded **two failed test constructions**. Isolated replay preserved the two failures: (1) my reviewer-only malformed-backslash ZIP test replaced a three-byte name with a longer name without rebuilding ZIP metadata, leading to **BadZipFile: Bad magic number**, not proof about the evaluator; (2) my reviewer CRC test incorrectly expected **ZipFile.testzip()** to raise, although it **returns the failed member name** (ZipFile.read raises). I retained the original reviewer test source and logs in disposable local work. I corrected only those reviewer harness expectations, not production code or original artifacts, and split execution into bounded groups.

Subsequent reviewer-owned runs completed **49 distinct test cases PASS**, with **50 test executions** because one case matched two selective run filters. Independently replayed existing project tests:

    PYTHONPATH=src python -m pytest -q -W error tests/test_teacher_transfer_pilot_v1.py tests/test_scenario_ensembles.py

Outcome **109 passed**. These 109 are existing tests and are **not** presented as new reviewer-created cases. Original full cross-platform repository counts are the separately evidenced GitHub CI results above, not local reviewer reruns.

Scope of independently executed adversarial probes:

- **Correctly refused:** wrong original ZIP SHA on disposable altered copies, Linux/Windows platform mismatch, archive absolute/traversal/drive/backslash paths (direct ZIP validator with literal raw headers), exact and case-folding duplicate filenames, symlink, oversized member/total/entry count, bad member CRC, malformed question count/version/case, changed original measurement ID, wrong SI unit, changed electric field location, swapped potential endpoint convention, nonexistent member, changed G1 status/code/global partial requirement.
- **Correctly refused by the strict original native inspector:** separately modified saved comparison bytes for both selected and **unselected** siblings; stale integrity receipts; tampered baseline native packet; absent selected comparison, unselected run receipt and original ensemble input. The original whole-ensemble inventory preflight rejected these before a filtered member could hide the damage. These are **direct native-inspector probes on copied extracted trees**; an unmodified official fixture would reject any changed outer ZIP before this layer.
- **Preserved:** genuinely unavailable G1 missing baseline body_4/null; exact original hash after execution; no overwrite of original downloaded artifact bytes; ASCII-safe JSON transport even with Unicode in an alternate question.
- **Unexpectedly accepted (demonstrated defects below):** an untrusted replacement fixture falsely claiming teacher/conductor/Maxwell interpretations; a re-pinned **nonoriginal** release ZIP; a re-packed ZIP with a **false release commit** and matching custom fixture. A malformed fixture containing three strings rather than question objects produced an uncaught **AttributeError traceback** rather than the normal controlled refusal.

These tests did **not** mutate source PR files, original GitHub artifacts, saved user studies or historical CI evidence. Neither ZIP structural direct tests nor a mocked test fixture are represented as a complete public evaluator run when the actual public path would first refuse an incorrect immutable outer ZIP hash.

## Blocking findings

### B1 — Untrusted --fixture replaces the very provenance trust anchor being validated (BLOCKER)

**Source:** [verification/teacher_transfer_pilot_v1.py](https://github.com/physicsvigilante/emfeeld/blob/ee54e96488e5cd9d2eb904abf65811627bfcc006/verification/teacher_transfer_pilot_v1.py#L37-L47), lines 73–87, 161–169, 179–186.

The advertised frozen fixture SHA256 is **computed and reported**, never checked against a trusted expected fixture digest. The CLI accepts **--fixture**. More critically, **qualified_archive_sha256** and **qualified_main_sha** both come from that same caller-controlled JSON. They are not independent immutable admission anchors.

**Reproduced, actual public entrypoint:** Starting with a disposable copy of the original Linux ZIP, I appended an unrelated file, changed only the custom fixture's expected ZIP digest to the resulting digest, and obtained **exit 0** with normal original-source-qualified output. In a second separate copy, I **re-packed** the original archive, changed head-sha.txt to the false commit **ffffffffffffffffffffffffffffffffffffffff**, and changed the custom fixture's claimed release SHA and ZIP SHA accordingly. Again **exit 0** with intact four signed source observations and one unavailable; output claimed the **false original_release_commit**. No native physics or nested saved measurements needed modification.

This is not a break in the original strict native inspector; it is a **trust-boundary error in the outer wrapper**. The claim that this path admits *only* the original PR #29 exact release fails when a caller selects another fixture. A self-reported SHA for user-controlled bytes does not authenticate source provenance. It is not necessary for an attacker to defeat a cryptographic SHA or completely re-seal the scenario store to exploit this narrow outer-label flaw.

**Required narrow response:** In the official qualified frozen mode, pin and independently check the canonical **fixture digest, original source commit and both original release ZIP digests** outside caller-mutable fixture data (for example, code constants or a separately trusted immutable manifest). The simplest V1 correction is to remove --fixture from qualified mode or reject all noncanonical fixture bytes. If custom fixtures are useful for future experiments, keep them in a **separately named, explicitly UNVERIFIED interpretation mode** and do not label their release/source identities or interpretation fidelity as original qualified. Add regressions for changing ZIP digest, head-sha and fixture together; verify the official two archives still pass unchanged.

### B2 — Arbitrary question prose and interpretation notes can falsely claim verified physics/teacher acceptance (BLOCKER within the evidence-labeling contract)

**Source:** evaluator lines 37–47 and 111–169, especially **153/159/168**; [frozen fixture contract](https://github.com/physicsvigilante/emfeeld/blob/ee54e96488e5cd9d2eb904abf65811627bfcc006/docs/TEACHER_TASK_EVIDENCE_TRANSFER_V1.md).

The evaluator checks measurement ID, unit, status and explicit context against the native saved result, which is good. **It does not establish the truth of an arbitrary edited question or notes string**. Three reviewer-created custom fixtures respectively claimed (i) reversed E1 meaning/negative absolute magnitude and teacher certification, (ii) G1 zero baseline displacement and teacher certification, and (iii) conductor polarization/Maxwell time evolution/reversed potential sign and teacher certification. All three yielded successful native transfers of genuine numbers, while the output **echoed the false claims** as developer_question / interpretation_caveat under a generic author-selected interpretation-fidelity statement.

The top-level evaluation still correctly says educational usefulness not evaluated; it does **not** make each individual mutable question scientifically faithful. The three original default questions are bounded and truthful, but letting new prose inherit their evidence labels makes a false verified-answer impression possible.

**Required narrow response:** Bind **the canonical original text/notes or their digest** for the qualified pilot. For any editable question, separate **user-supplied unverified question text and claimed provenance** from source-verified measurement/units/context, with an explicit unverified-interpretation status and no teacher-verified badge. Do not infer conductor dynamics, field motion, textbook completeness or teacher acceptance from a successful source measurement lookup. Add negative test inputs for the three semantic spoofs above.

### N1 — Malformed custom question types cause an uncaught traceback (NONBLOCKING if B1 removes custom mode)

**Source:** evaluator line 45 and main exception handling lines 185–190. With questions = ["E1", "G1", "T1"], the set comprehension calls q.get on a string; main does not catch **AttributeError**. Reproduced as nonzero with traceback and no result JSON. If custom fixtures remain supported, validate that every question is an object with the exact expected shape and provide the normal controlled refusal. This is input-hardening and error presentation, not numerical correctness.

## Six separately evaluated review dimensions

| Dimension | Scoped assessment |
| --- | --- |
| **Question/source interpretation fidelity** | Default three retrospective developer questions correctly match original saved identifiers, context and status; **untrusted custom-question truth is NOT verified and can be mislabeled (B2)**. No blind teacher question has been tested. |
| **Physical/numerical correctness** | **PASS for bounded original E1/T1 sources**: independent static formula checks, exact native sealed values and receipts; no new solver physics. No external human physics certification or general-law guarantee. |
| **Requested native measurement coverage** | **Four original signed available results plus one honest G1 unavailable/null**; E1/T1 global complete, G1 global partial. No zero substitution, no missing-baseline retarget. |
| **Evidence and qualification integrity** | **PASS for canonical fixture + original two ZIPs**, original 352-file source tree, raw receipts and tested viewer PNG hashes; **FAIL for editable fixture provenance boundary (B1)**. Unkeyed hashes alone cannot authenticate hostile full resealing or concurrent writers. |
| **Educational usefulness** | **NOT EVALUATED** — no human teacher/student test, classroom study or usefulness assessment. |
| **Textbook-answer completeness** | **NOT EVALUATED** — three selected historical measurement questions are not a blind textbook-answer benchmark. |

## Gate and narrow next actions

**CHANGES REQUESTED for reviewed exact SHA ee54e964...**: resolve **B1 and B2** and test the explicit trusted/untrusted fixture distinction. Preserve real original ZIP/SHA, signed values, one G1 unavailable and the historical failed Windows test. The native comparator, field laws, immutable store and viewer need **no redesign on the evidence examined**. N1 can be included if custom fixture support continues.

After a source correction: freeze a **new** head and tree, rerun the focused negative/positive transfer checks and relevant **full Linux/Windows exact-head CI**, and request **targeted independent re-review of the affected provenance/labeling paths**. The separately advanced **PR #32 main** still needs combined-source integration proof and a fresh actual-main-push release/archive audit after any owner-authorized merge. This central review neither merges PR #33 nor acts as an owner/source merge approval.

**Report independence limitation:** reviewer ran native transfer and adversarial tests independently in this separate ChatGPT context, not as a different human/teacher or a second Windows machine. Historical author/CI results remain separate claims; original negative logs are retained as negative evidence.