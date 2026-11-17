# Chat B independent R2 review 02 — emfeeld PR #33

**Verdict: PASS (targeted corrected boundary only).** **Reviewer:** separate-context Chat B, independently executed on 2026-11-17. **Reviewed source:** [PR #33](https://github.com/physicsvigilante/emfeeld/pull/33), exact corrected head `73a61aaa16f79df12a54231b738074bb2826e66f`. This is **not** an owner merge approval, human physicist review, classroom certification or post-merge release qualification.

**Scope:** R2 re-review of B1 (untrusted fixture/source/ZIP identity), B2 (false E1/G1/T1 question/teacher interpretation), and N1 (malformed question) after [review-01](review-01-chat-b.md) reported **CHANGES REQUESTED** on **old** head `ee54e96488e5cd9d2eb904abf65811627bfcc006`. The original review is retained unchanged. Read [REQUEST-02](../REQUEST-02.md), [author response-01](../responses/response-01-chat-a.md), original review, [AGENTS.md](https://github.com/physicsvigilante/emfeeld/blob/73a61aaa16f79df12a54231b738074bb2826e66f/AGENTS.md), [protocol](../../../../PROTOCOL.md), [risk policy](../../../../REVIEW-RISK-POLICY.md), exact source, frozen fixture and test/contract diff.

## Exact identity, changed surface, source reconstruction

| Boundary | Independently verified identity |
| --- | --- |
| Corrected feature commit | `73a61aaa16f79df12a54231b738074bb2826e66f` |
| Corrected feature Git tree | `61f11a2d749a6dcbabba8f1555381abc642b3378` |
| Parent / original failed-review head | `ee54e96488e5cd9d2eb904abf65811627bfcc006` |
| Released PR #32 main (preview parent 1) | `a18c26f050f5320ce8a9d61f7169e32cd6e31f38` |
| Corrected feature head (preview parent 2) | `73a61aaa16f79df12a54231b738074bb2826e66f` |
| Original GitHub PR merge-preview | `ac33369acfef282e50748e9221426b11237d2b9d` |
| **Reconstructed 356-file combined preview Git tree** | **`88364f2394dd84e6270681b3efd1ff879fc397dc`** |
| Original unchanged question fixture SHA256 | `536ada6775aa3effb7abafaef742f7cb0030ce4428bcecf1d4664e1025436008` |

GitHub commit/tree metadata establishes the corrected one-parent commit and exact two-parent merge-preview. Independent [old-to-new comparison](https://github.com/physicsvigilante/emfeeld/compare/ee54e96488e5cd9d2eb904abf65811627bfcc006...73a61aaa16f79df12a54231b738074bb2826e66f) changes **exactly three paths**: `verification/teacher_transfer_pilot_v1.py` (+32/-14), `tests/test_teacher_transfer_pilot_v1.py` (+57), and `docs/TEACHER_TASK_EVIDENCE_TRANSFER_V1.md` (+2/-2). No original fixture, `src/emfeeld/*` field law, numerical solver, comparator, native scenario, saved store, or viewer production change. PR is still **open/draft/unmerged**.

Downloaded **original GitHub source-snapshot artifact 14307373325**, not a floating `main` checkout. Its `tested-source.tar` SHA256 is `6e717fc893347ed0fd3de0516a780393d59250795adee5b26d0921f1b674b71a`. Extracted and staged **356 source files** in a disposable local Git index; **`git write-tree` reproduced `88364f2394dd84e6270681b3efd1ff879fc397dc`**. The canonical question JSON raw SHA matches the code-pinned expected digest.

## Source-hosted exact-head CI and independently downloaded originals

GitHub workflow metadata and jobs were inspected independently at head `73a61aaa...`:

- [Linux/Windows clean-install #44036897079](https://github.com/physicsvigilante/emfeeld/actions/runs/44036897079): **completed/success**, Ubuntu job `133881836352` and Windows job `133881836605`. **Each original archived** `headless-tests.log`: **1,526 passed**, historical `pilot-behaviour-tests.log`: **18 passed, 1 obsolete test deselected**, `viewer-tests.log`: **33 passed**. Neither OS is inferred from the other.
- [Source snapshot #44036897098](https://github.com/physicsvigilante/emfeeld/actions/runs/44036897098): **completed/success**, source job `133881836654`, exact reconstructed Git tree above.
- [Real-PyVista #44036897018](https://github.com/physicsvigilante/emfeeld/actions/runs/44036897018): **completed/success**, render job `133881836363`, independently checked original viewer artifact below.

All **six actual GitHub Actions ZIPs** were independently downloaded; whole-ZIP SHA256, every member's CRC, member count and exact/case-folded filename uniqueness were checked:

| Original artifact | GitHub ID | Whole-ZIP SHA256 | Members | Result |
| --- | ---: | --- | ---: | --- |
| PR #29 Linux | 14300302937 | `0654fa7d39249c4026945295ce15a18eae46a8598325e66d321cd515aa1e7f55` | 2,161 | PASS |
| PR #29 Windows | 14301401780 | `be72aef030afef113758a671aa93363b7e01af51ad9e79d942b91ea508c9a27e` | 2,161 | PASS |
| Corrected PR #33 Linux | 14307743114 | `9cc3fd7c1e850806a244b583b9d43d9403d520e353685bf7548420c0f5a35320` | 2,166 | PASS |
| Corrected PR #33 Windows | 14308247410 | `20aac01267a5ce0e394b35f14aae7eb1e7deb215fc7136360011692b2249234f` | 2,166 | PASS |
| Corrected original source snapshot | 14307373325 | `7947830aba61f7effed1b7e46346eedda021f608dfd1ee24696cdbc0b648a653` | 4 | PASS |
| Corrected original viewer | 14308250369 | `96c61af59939c2674415cb9ed53ca93a2417e386a72ff699d8e1e8fff8515ecb` | 22 | PASS |

Corrected OS releases both contain `head-sha.txt = ac33369...` (the tested PR merge-preview, **not** the old PR #29 main commit). Both have preserved original Physics Demonstration evidence: **17/17 original native observation statuses `ok`; 64/64 archived analytical checks passed**. The separate viewer report cites `ac33369...`; its **nine offscreen cases PASS and all 17/17 original archived PNG SHA256 receipts match**. The report's `visual_inspection` is still **PENDING**. I did **not** visually certify those screenshots or perform new manual Windows mouse tests.

## Fresh reviewer-owned B1/B2/N1 attack results — **28/28 PASS**

Executed **28 distinct new reviewer-authored assertions** in a disposable Linux CPython 3.13.5 environment, against the **original GitHub source-snapshot checkout**, **not** just author-provided test results. Breakdown: **11 B1** admission/source-anchor checks, **10 B2** semantic-spoof checks, **5 N1** type/refusal checks, and **2** original archive non-mutation checks. The source and the original GitHub ZIPs were never edited.

**B1 (11 PASS)**:
- Verified hardcoded `FROZEN_FIXTURE_SHA256`, independently pinned `QUALIFIED_MAIN_SHA` and **separate Linux/Windows `QUALIFIED_ARCHIVE_SHA256`** against authentic bytes. The fixture's own provenance is checked against these code constants; it is not itself the trust anchor. `transfer` exposes **no** `fixture_path`.
- Recreated review-01's **extra-file** original Linux ZIP with a forged custom `--fixture` re-pinned to its changed ZIP hash. Actual public CLI: **exit 2, empty stdout, argparse `unrecognized arguments: --fixture`**. Calling canonical CLI without the flag instead gives **exit 2, empty stdout, `archive ZIP SHA256 does not match qualified original release`**.
- Recreated review-01's separate **repacked ZIP with false `head-sha.txt = ffff...ffff`**, and matching false-source/false-ZIP custom fixture. Same actual public refusal: **exit 2, empty stdout** with `--fixture`; canonical command refuses changed ZIP hash. Private `_frozen_fixture` rejects both forged fixtures before archive opening.
- Independently mutated claimed original main SHA, Linux ZIP SHA, Windows ZIP SHA and both main/ZIP SHA together; each private canonical-loader preflight raises **`ValueError: fixture SHA256 does not match the qualified original questions`**. Direct `transfer` of a temporary modified default fixture plus an intentionally nonexistent archive confirms fixture SHA rejection **before attempted archive access**.

**B2 (10 PASS)**: independently changed *original question/notes bytes*, leaving the real native measurement identities unmodified, to claim **negative E1 absolute field magnitude; teacher approval of E1; G1 zero missing-body displacement; teacher approval of G1 zero; T1 conductor polarization; Maxwell time-dependent evolution; reversed potential endpoint sign; T1 teacher/classroom certification; false provenance teacher-validation; false provenance blind authorship**. All ten are rejected by `_frozen_fixture` as a **changed original fixture SHA**, with additional `transfer` preflight against a nonexistent archive. They cannot be echoed as qualified `developer_question` or `interpretation_caveat` through the supported interface. This does **not** certify truth of arbitrary future author-written prose: it restricts the qualified V1 interface to its source-grounded original development questions.

**N1 (5 PASS)**: three-string `questions=['E1','G1','T1']`, a dictionary in place of the question array, and a primitive instead of a question object all fail canonical fixture preflight. Actual public CLI with malformed custom fixture returns **exit 2, zero stdout, no traceback** because `--fixture` is not accepted. A separately isolated **reviewer-only in-memory re-pin** was used *solely* to reach the post-digest private type guard: it raises controlled **`ValueError: frozen questions must be objects`**, not the old `AttributeError`. This private test did **not** alter GitHub source or demonstrate a public hash override.

**First-attempt preservation:** the new 28-case adversarial run completed **28/28 PASS on first execution**, without a failing adversarial assertion. In my **separate original-artifact audit harness**, the first run had an **incorrect reviewer assertion**: it compared `original_parent_run_sha256` with `ensemble/baseline/run.json` rather than the correct `parent-template/run.json`. First audit invocation therefore failed at that assertion, **not** in production. I retained that local first failure, corrected only the disposable reviewer harness, then reran the audit successfully. I do **not** re-label that first harness attempt as pass.

Existing tests, executed separately on the reconstructed combined-source snapshot:

```text
PYTHONPATH=src python -m pytest -q -W error tests/test_physics_demonstration.py tests/test_teacher_transfer_pilot_v1.py tests/test_scenario_ensembles.py
124 passed in 13.24s
```

These **124 existing project tests are not counted among the 28 fresh reviewer-authored probes**. No complete independent reviewer execution of all 1,526 tests is claimed; the full counts are directly checked original GitHub CI archive logs.

## Canonical original native transfer — both real PR #29 releases

Actually ran the corrected public CLI on **each authentic unmodified PR #29 original** ZIP, with `PYTHONPATH=src`:

```text
python verification/teacher_transfer_pilot_v1.py /mnt/data/original-pr29-linux.zip --platform linux
python verification/teacher_transfer_pilot_v1.py /mnt/data/original-pr29-windows.zip --platform windows
```

Both returned **exit 0** and original stdout SHA256 **byte-for-byte unchanged**:

- Linux: `0e0d0db21e19b5075df9be3069937f88156dbe914cd1cd0e987a0ba7cba3aab7`
- Windows: `20615a519c9f674387ce6d9e29f307f8227c5e1f372441f077f2877a09e483bb`

Directly inspected the **original saved archive JSON bytes** rather than relying solely on evaluator output: **54 source/measurement/receipt assertions per OS, 108 total**, including the **actual parent-template run SHA**, each original selected **comparison request/result/integrity**, left baseline run and right member run raw SHA256, matching **native saved signed measurement/status/unit/context/code**, ensemble global status, and source-release identities. Selected original results are identical on both OS artifacts for this frozen pilot:

| Original saved comparison | Confirmed value / state | Qualification |
| --- | --- | --- |
| E1 hypothesis-A field magnitude delta | **-0.05458851160751549 N/C** | **Signed change**, not negative absolute field |
| E1 hypothesis-B field magnitude delta | **+0.18513207463551812 N/C** | Signed right-minus-left |
| G1 hypothesis-B body_4 | **`unavailable / unknown_operand / null`** | Global **partial**; missing baseline operand, **not zero** |
| T1 hypothesis-A potential-step delta | **+1.1741058461436236 V** | Static `V(to_m) - V(from_m)` signed comparison |
| T1 hypothesis-B potential-step delta | **+1.513997527981914 V** | Same ordered endpoints/convention |

T1 endpoints remain from **(0.4, 0.6, 0.3) m** to **(2.8, 0.25, 0.4) m**. These are independent prescribed-source alternatives, **not** a physical time sequence, conductor response, or solved Maxwell evolution. The original source archive SHA256 values remained unchanged after all tests. Native extraction used only temporary review paths; original stores were not written. Windows-origin artifacts were **replayed on reviewer Linux**, not on a new reviewer Windows machine.

## Findings, residual limits and gate

- **B1 — RESOLVED in scoped qualified V1:** no caller-selected public fixture; original raw fixture SHA, source commit and **both separate original OS ZIP hashes** pinned and checked; false re-pinned archive/source claims fail.
- **B2 — RESOLVED in scoped qualified V1:** original question and notes bytes are frozen; edited physics/teacher claims fail before release/native admission. No arbitrary-question truth certification is added.
- **N1 — RESOLVED/REMOVED public attack surface:** malformed custom input is not a qualified public mode; private post-digest type guard refuses primitives.
- **Numerical/source evidence — PRESERVED:** original signed E1/T1 and one unavailable G1, exact full output SHA256, original sealed receipts and global status preserved. No new physics engine change.
- **Remaining nonblockers and explicit limitations:** a fixed SHA does **not** authenticate malicious full source-code replacement or a fully resealed malicious trust root; no unverified/custom fixture mode exists; no independent human expert/teacher/classroom judgement, blind authoring benchmark, manual Windows GUI qualification, physics beyond these original static cases, or post-merge `main` CI is demonstrated. The old failed Windows test run and **review-01 CHANGES REQUESTED** remain historical facts about older source.

**Gate verdict: PASS for the exact corrected `73a61aaa...` source and current GitHub merge-preview `ac33369...` only.** No outstanding B1/B2/N1 blocker was reproduced. **Do not merge on this report alone.** Owner must separately approve guarded integration after verifying unchanged head/base and required release gates. Following any merge, obtain **fresh actual main-push** Linux/Windows/real-PyVista workflows and downloaded original artifacts; PR preview CI is not a released main qualification. A later source-head movement invalidates this source-specific PASS.

**Owner handoff:** return to Chat A and say **“review done.”**
