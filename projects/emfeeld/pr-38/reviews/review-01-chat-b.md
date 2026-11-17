# EM Fields PR #38 — Chat B independent R2 review 01

**Date:** 2026-11-17  
**Verdict: PASS — STRICTLY SCOPED TO THE NON-BLIND PUBLIC NASA SOURCE REHEARSAL AND ITS HONEST NATIVE-EVIDENCE BOUNDARY.**  
**Source PR:** https://github.com/physicsvigilante/emfeeld/pull/38  
**Disposition:** Review only. PR remains **DRAFT / OPEN / UNMERGED**. This review is **not** an instruction or authorization to merge.

## 1. Review scope, pinned provenance, and limits

This is the independent Chat B review described in `projects/emfeeld/pr-38/REVIEWER-PROMPT-01.md` and `REQUEST.md`. I read the original author release audit and directly downloaded **all four original GitHub Actions artifact ZIPs**; I did not treat its assertions or its test counts as my own execution. This is expressly the **non-blind, publicly answered** NASA *Space Math* Problem 1 exercise with a **separately disclosed** 0.7-mm spacing supplied by adjacent Problem 2. It is not Issue #36's prospective, unknown teacher task with an independent withheld judge.

Identity checked directly through the GitHub Git commit/tree API and reconstructed from the source TAR:

| Identity | Independently established value |
|---|---|
| Feature HEAD | `68241b9b971c793506a3f0014725f03bb1a8899e` |
| Canonical source Git tree | `33b58fb55b387ec2b7c1bdd61bf1af7764db97cd` |
| Qualified base `main` | `510014fc078c73d37146b9804763e29d04ac0018` |
| Base Git tree | `a82188148568653311581d9d4c02e8c96a37d3cf` |
| CI merge-preview | `78fbe5143d0714b928ed54e25e755a612c37bbf9` |

The preview commit has **exactly the same source tree** as the feature and ordered parents `[base, feature]`; it is a CI source-equivalent preview, **not** an actual merge to main. The PR's complete changed-file list contains exactly six paths: `.github/workflows/release-candidate.yml`, `docs/NASA_ION_PUBLIC_REHEARSAL_V0.md`, `examples/nasa_ion_public_v0/{question,receipt,packet}.json`, and `tests/test_nasa_ion_public_v0.py`. It contains **no `src/emfeeld/` engine, field law, integrator, numerical tolerance, viewer, saved model or historical corpus changes**.

Actual ordered Git parent commits and tree membership independently verify:

1. `b1faed6a75fa61b90614a494c837937626296826`: original question alone, blob `9024beac10c74974fdc90d7bee8dbb3331a40ff0`; no receipt, no packet.
2. `a5a11dd36a16bc5b7560d8e3e43f882320b7bbba`: same question blob and receipt blob `664874cc5f1a621a80985f8851349af5c4bb6eb7`; **still no packet**.
3. `e0a008119fca8289607ec2c337722da0bd3861dd`: same question and receipt blobs and **first packet** blob `f643a5e51e225aa3a62a1dbc7d991ed900a29c4d`.
4. Pinned HEAD still carries those same three blobs.

Independent SHA-256 of raw source bytes: question `cd797751a84d86caa57c2024620215895c1414169c6682b96933e4b4cf25cc23`; packet `f86211065ec99e3e82181de256d321a6ebb054f9b397440996529a3ec6ccfeda`. The receipt is a **local, unkeyed byte checkpoint**, explicitly `external_unverified` / `not_authenticated` / `not_verified`: local source-first chronology **does not establish external NASA delivery, teacher provenance, or blind authorship**.

## 2. Independent original artifact audit (not merely CI status)

Original ZIPs downloaded using their **GitHub artifact IDs**, whole-file SHA-256 checked, every member read for CRC, and member paths checked for traversal and case-insensitive duplicates:

| Original GitHub artifact | ID | Whole-ZIP SHA-256 | Original verified members |
|---|---:|---|---:|
| Ubuntu 24.04 release | `14334933210` | `774babdd484d233e28deb8b7ca9354c890702a4ac7162a3cc7d18a051b272f5c` | 2,186 |
| Windows 2022 release | `14335977410` | `6364941c412f34a5fc2706ff042c0bbf237081a72c9f2bcc9d89134395edd41f` | 2,186 |
| Separate real-PyVista viewer | `14334383850` | `322b305d3e38e5a175a81a1d7fa7ba48bc6b6e22af0097d93bb44a3b0e9980dd` | 22 |
| Exact source snapshot | `14334468187` | `0712ceef3b00214f334ec049f3ca59f0bd93952a19c614b2a42b170fbf1da8ac` | 4 |

In the exact-source snapshot I rehashed `tested-source.tar` to `22a496e3ca60ce8a84f23102290aeb21841b9b101aaf2cc45a3731e17700133f`, extracted the safe 367-file source snapshot, constructed a **fresh local Git index/tree**, and obtained the exact expected `33b58fb55b387ec2b7c1bdd61bf1af7764db97cd`. The independent recursive `git ls-tree` output matches the original archive `git-tree.txt` **byte for byte**. All 367 tracked file blob hashes remained unchanged after reviewer tests. The viewer artifact embeds the **identical source TAR**.

The original GitHub workflow runs `44098382682` (both OS), `44098382316` (viewer), and `44098382677` (snapshot) have `event=pull_request`, pinned HEAD `68241b9...`, `status=completed`, `conclusion=success`, first attempt. I independently read original release logs, rather than relying on the author summary: **each OS** has **1,585 headless passed; 18 historical passed, one obsolete all-file guard deselected; 33 real-PyVista passed**. These are *original CI tests*, not new reviewer-owned test results.

In **each** original OS archive, `lock/question.json` and `ci-replay/question.json` are exactly the pinned raw question; `ci-replay/packet.json` is exactly the pinned packet; `lock/receipt.json` and `ci-replay/receipt.json` are exactly the original receipt. The source-native assessment binds **both raw hashes** and its own native-result SHA and reports exactly one supported `speed` observation at actual saved **particle 0, sample index 20, `time_s=3.2195317385273e-8 s`, unit `m/s`, status `ok`**, with a complete execution state. Independent physics/interpretation grading stays explicitly **not evaluated / not verified**. Native OS differences are retained, not normalized away:

| Original CI platform | Exact original native-result SHA-256 | Original native speed (m/s) |
|---|---|---:|
| Ubuntu | `ab928b94cbb930d8589352a1ba180f81e4d7dda67997b57473bc35c05242ec20` | 43,484.58452036887 |
| Windows | `20854e0f07a98af4a6b3eba3b6318b73f9ee8672a4b36175d4239242a16ba038` | 43,484.584520368866 |

I verified the original Physics Demonstration V1 has **17 individually `ok` native observations** and **64/64 passed original analytic checks** on both OS. Original `engine_sha256` receipts for all **29 `src/emfeeld/*.py` files** match the exact reconstructed source; Windows expected CRLF checkout translation was checked separately rather than requiring false byte identity with Linux. The archived derived `E1` remains `complete` and `G1` remains `partial`, with its `unavailable` / null result preserved; nothing was upgraded to global complete. The separate real-PyVista report has **9 passed scene cases** and every one of **17 screenshot PNG** hashes matches its original report; it still correctly declares **visual inspection pending**, and this review does not claim Windows manual interaction or classroom testing.

## 3. Reviewer-owned execution (distinct new source and perturbations)

**Actual reviewer environment:** Linux x86-64, CPython `3.13.5`, NumPy `2.3.5`, SciPy `1.17.0`, pytest `9.0.2`; pinned **367-file original source** from the independently verified snapshot, with `PYTHONPATH` set to that source's `src`. No dependencies installed; no source files modified; all reviewer outputs were created outside the source tree. Used the **public** `verification/question_first_trial_v1.py freeze` / `assess` CLI and native `python -m emfeeld.observations`. **11 new reviewer cases: 11 PASS, 0 FAIL on first execution.** These are not the author's five NASA tests or its 1,585 CI tests.

| New independent case | Observation / actual outcome |
|---|---|
| Re-frozen **exact public NASA** question, original packet, fresh output | Native speed `43,484.58452036887 m/s`, sample 20 at actual `3.2195317385273e-8 s`; source/packet hashes match, coverage `complete`, `m/s × 3.6 = 156,544.50427332794 km/hour` **outside** the engine. |
| **Different reviewer-authored** mass `3.6e-25 kg`, charge `+3.2e-19 C`, voltage `650 V`, gap `0.0013 m`, 17 samples | Four native measurements independently checked: exit speed `33,993.46342395181 m/s` (analytic `33,993.46342395189`), KE `2.0799999999999892e-16 J` (analytic `qV=2.08e-16 J`), field `500,000 N/C`, force `1.6e-13 N`; 4/4 complete at calculated `7.648529270389176e-8 s`, index 16. |
| Deliberately **double source field** but keep original NASA packet's fixed exit time | Structural coverage stays **`complete`**, but speed changes to **`86,969.16904073775 m/s`**; crucially **`interpretation_fidelity=not_verified`** and **`independent_physics_correctness=not_evaluated`**. No accidental scientific PASS. |
| Change frozen true saved **time** by 25% | Native sample still `ok`, assessment **incomplete**, specific saved-time mismatch, CLI exit `1`. |
| Retarget frozen native requested **unit** to km/hour | Native sample still `m/s` / `ok`, assessment **incomplete**, explicit `expected unit km/hour` issue, CLI exit `1`. |
| Retarget packet **quantity** from speed to velocity | Rejected **before evidence-directory creation**, CLI exit `2`. |
| Retarget packet **sample index** from 20 to 19 | Rejected **before evidence-directory creation**, CLI exit `2`. |
| Put an authored numerical **expectation** in packet | Rejected **before execution**, CLI exit `2`. |
| Change frozen question bytes while leaving receipt unchanged | Receipt mismatch rejected **before execution**, CLI exit `2`. |
| Declare unresolved necessary source information | Assessment admission rejected **before execution**, CLI exit `2`. |
| Independent **negative-charge direction** native case: `q=-3.2e-19 C`, `m=1.8e-25 kg`, positive uniform field | Signed force `-5.942857142857142e-13 N` and signed velocity `-13,206.349206349187 m/s`, both agree with separate `qE` and `qEt/m` references. |

The wrong-field negative demonstrates a **necessary scientific limitation** rather than a code defect: native coverage is about *whether the declared native observation exists with the correct unit, saved time and status*; it cannot independently verify prose interpretation, authored field strength or the published answer. Retargeted observation/time/unit contexts do fail the admission or coverage check. The independent different-parameter field/force/energy test provides physics evidence not obtained by merely checking the NASA packet's own authored reference.

## 4. Original NASA Problem 1 and Problem 2: independent reference check

**Original public source inspected:** NASA Goddard *Space Math*, “The Mathematics of Ion Rocket Engines,” p. 64, https://spacemath.gsfc.nasa.gov/weekly/5Page64.pdf, **two-page problem/answer-key PDF**. The original statement gives xenon mass `2.2×10^-25 kg`, positive charge `1.6×10^-19 C` and a `1300 V` energy gain in **Problem 1**. The **0.7 mm** spacing belongs to **Problem 2**, not Problem 1. The authored question and explanatory documentation distinguish the two correctly; the exact original NASA PDF binary was **not independently provider-authenticated** in the source project. The official original online PDF's text could be reviewed, but this reviewer could not obtain a PDF page screenshot (source fetch returned 502 for the screenshot), so this is not a separate PDF-byte/visual integrity attestation.

- **Problem 1:** With zero incident kinetic energy, `0.5 m v² = q ΔV`. Independent calculation gives `v = sqrt(2×1.6e-19×1300 / 2.2e-25) = 43,484.58452036871 m/s`, or **`156,544.50427332736 km/h`**. NASA's printed key gives about **`159,000 km/h`** (~**1.57% higher**). This is compatible with coarse numerical/intermediate rounding, not evidence that a model should be tuned to `159,000`. The native SI result agrees with the exact-input energy relation; no native km/h conversion is claimed.
- **Problem 2, uniform-field-from-rest cross-check:** Under the explicitly disclosed field and initial-state assumptions, `|E|=1300/0.0007=1,857,142.857 N/C`, `|F|=qE=2.9714285714e-13 N`, `a=F/m=1.35064935065e12 m/s²`, and `t=2d/v=3.21953173853e-8 s`. NASA's key instead prints approximately **`a=7.1e11 m/s²`**, **`F=1.6e-13 N`**. Its displayed working uses the **average** speed (~22.1 km/s) to estimate crossing time, then also divides **22.1 km/s** (rather than the full **44.2 km/s** exit velocity change) by that time to calculate acceleration. That double use of the half-speed explains the near-factor-two discrepancy; using `Δv/t` or `v²/(2d)` recovers approximately twice the key's values. This is a **public reference-key-versus-internal-physics discrepancy under the stated model**, not a source-PR solver regression. No Problem 2 result was requested or measured by the published one-observation Problem 1 packet.
- **Additional adjacent sheet warning, outside PR scope:** Problem 3's prompt states `0.90 N`, but the printed answer-key arithmetic begins with `0.090 N`. This reinforces the need to avoid treating this public answer key as a certified independent judge for subsequent problems; it was **not** part of PR #38's native execution or this review verdict.

## 5. Findings and disposition

**Blockers found in the PR #38 bounded scope: NONE.** Positive evidence is sufficiently strong to support the advertised **source-first public-source rehearsal**: exact frozen local question, ordered receipt and packet, unchanged engine, source-equivalent and successful original CI, independently verified original artifact bytes, and independent positive/negative source and physical reference cases. The documented status labels do not falsely certify independent interpretation or NASA grading.

**Non-blocking but mandatory distinctions for any downstream claim:**

1. The NASA **Problem 2 published force and acceleration values disagree** with the uniform-field model and with the original key's own transit-time reasoning. Keep the discrepancy explicit; **do not silently modify** the original source, force a packet to NASA's `1.6e-13 N`, or claim NASA-verified physics.
2. The **0.7-mm gap is cross-problem illustrative geometry**. The Problem 1 speed is independent of gap; the preset `E` and exit instant are **author-derived inputs**. This demonstration does not show automatic inversion of source voltage into a field, general question interpretation, or an ion-thruster plasma simulation.
3. **Complete native coverage is not scientific correctness.** The reviewer doubled-field case returned complete native coverage and a false numerical answer, while retaining independent correctness `not_evaluated`; this separation must remain prominent.
4. Source question is **`external_unverified`** and its local receipt **`not_authenticated`**. Neither an independently unseen teacher input, an independently withheld judge, student/classroom usefulness, nor blanket numerical error certification has been demonstrated. Those belong to the distinct prospective teacher study (Issue #36).
5. The original viewer's nine off-screen cases and 17 PNG checksums are verified, but **visual inspection and manual classroom usability remain unqualified**; PR #38 makes no viewer changes.

**First-run failures preserved (reviewer tooling only, not PR defects):**

- Original independent source audit mistakenly compared `git ls-files --stage` index-format output to the archive's `git ls-tree`-format listing and raised `AssertionError: Git ls-files differs from archived Git tree listing`. I retained this as an audit error, corrected the comparison to `git ls-tree -r <newly-computed-tree>`, and obtained **identical bytes and the exact canonical tree**. The error is not a source-file mismatch.
- Original deeper ZIP audit loop visited `viewer` before `source` and raised `KeyError: 'tar_sha256'` for its own not-yet-populated reference variable. Original failure log was retained, the sequence corrected to source → viewer → Ubuntu → Windows, and the complete deep audit then passed. No ZIP hashes or evidence values were changed.
- The **11 reviewer-owned CLI/native cases passed on their first executions**. Expected nonzero process exits `1`/`2` in adversarial rejection tests are successful *negative-test outcomes*, not unexpected execution failures. No failures or original candidate artifacts were erased, overwritten or promoted to PASS without explanation.

**Decision: PASS (scoped R2, NON-BLIND).** This is **not** authority to merge PR #38. Owner-controlled integration, subsequent *actual-main* CI if merged, and original post-merge artifact auditing remain separate gates. In particular, **do not present this as a result of Issue #36's as-yet-unrun teacher/withheld-judge study.**
