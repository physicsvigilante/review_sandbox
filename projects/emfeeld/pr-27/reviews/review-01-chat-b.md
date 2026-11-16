# Independent Chat B focused R1 review — EM Fields PR #27 — review 01

**Verdict: CHANGES REQUESTED (one evidence-provenance/fail-closed blocker).**
**Date:** 2026-11-16 (Asia/Kolkata). **Scope:** Verified Ensemble Measurement Readout V1, read-only evidence presentation. **Reviewer:** Chat B, independent conversation and reviewer-authored experiments. **Source PR:** https://github.com/physicsvigilante/emfeeld/pull/27. **Review request:** ../REQUEST.md. This is *not* a production merge or physics certification.

## 1. Exact source identity, independently checked

- **Head:** 2dc5e1d90a1cec2809d536f725474eac0ae4dd2d.
- **Git tree:** 45df8622888b841333d7242caf410e7449900cfc.
- **Qualified base:** 9e5924efa60dea56606e0b8eef591f94711b666d.
- **CI merge preview:** d230d97d9d3b300688ed0796f01f686b57d53cc0, Git tree **exactly identical** to the head; Git API lists parents in order: qualified base, then exact candidate head. This preview is not a merged production commit.
- Independently downloaded source snapshot GitHub Actions artifact **14249076188** from run **43913225024**. Original ZIP SHA256: c805342eab615b0ef43a28ea63cac513b120e5dc26653d123e089a6cea406076; embedded tested-source.tar SHA256: ffb70b457202832b560a0645d38c34910b84ee4e64197e6e118109e3d9ff6582. Extracted **347 tracked files**; a new disposable Git index and **git write-tree** independently reproduced **45df8622888b841333d7242caf410e7449900cfc**.
- GitHub independently reported the PR **open, draft, unmerged**, and exactly five changed paths: src/emfeeld/scenario_ensembles.py, tests/test_scenario_ensembles.py, .github/workflows/release-candidate.yml, README.md and docs/VERIFIED_ENSEMBLE_MEASUREMENT_READOUT_V1.md. No changed field-law, integrator, tolerance, source model or renderer file was listed.
- Read the central REQUEST, reviewer prompt, PROTOCOL, risk policy, source AGENTS.md, bounded readout contract, Issue #26, exact-head source implementation and relevant existing comparison and ensemble inspectors. All findings are tied to **this SHA/tree only**, not floating main or earlier PR #25.

## 2. Blocker B1 — modified comparison integrity receipt is presented after a read-time change

**Severity:** changes requested; R1 evidence-provenance and read-time fail-closed contract. This does **not** demonstrate altered numerical values, units, physics, malicious cryptographic forgery, or a distributed concurrency/ACID guarantee.

**Exact affected code:** https://github.com/physicsvigilante/emfeeld/blob/2dc5e1d90a1cec2809d536f725474eac0ae4dd2d/src/emfeeld/scenario_ensembles.py#L515-L591, especially lines 550–582.

**Expectation:** The readout claims a verified original comparison integrity receipt. The contract requires strict original source binding, and a comparison changed during inspection/projection must fail closed. The parent ensemble's sealed full inventory contains a SHA256 binding for each member's comparison/integrity.json. The new readout must not silently substitute an integrity receipt that its full-ensemble preflight did not validate.

**New reviewer reproduction, from a four-member sealed native fixture:** full ensemble has one healthy member named literally "baseline" (index 3), one healthy ordinary member, one rejected revision, and one native-complete member with a legitimately unavailable cross-comparison. Select member_id="baseline". Inject only a trailing ASCII space into **member-03/comparison/integrity.json**, leaving the request, result, original native observations, physics, and receipt's parsed JSON *unchanged*. Two independently tested timing windows:

1. After **inspect_ensemble** successfully validated the full original ensemble but before the selected comparison is re-inspected.
2. After the selected comparison's **second** scenario_comparisons.inspect has returned successfully but before read_ensemble_measurements reads its comparison files to make the projection.

**Actual:** The readout returned successfully in **both** cases. Its exported evidence.integrity_sha256 identified the newly altered integrity file, not the integrity bytes bound to the previously verified outer ensemble inventory. This is a provenance drift / fail-open gap. The equivalent newly authored request.json and result.json single-file mutation probes **correctly refused**.

An explicit independent reproduction at window 2 recorded:

- **Original SHA256 in outer verified manifest:** 4195429b449e8f3acc3a036b1487022cd9f0afdcb6cd2d12c593ea2a32bb8dde.
- **Mutated integrity.json SHA256:** 7039e09867396d6f62215a3f624b7825c2cceed961cd721e3048ab73e73029fe.
- **Readout evidence.integrity_sha256:** 7039e09867396d6f62215a3f624b7825c2cceed961cd721e3048ab73e73029fe.
- **Readout status:** global partial; selected member complete; no refusal. The original outer manifest still pinned the first hash.

**Cause:** after a successful full ensemble preflight and selected comparison inspection, the new projector re-reads integrity.json and verifies *its parsed file inventory* against raw request/result hashes and checks decoded result equality. It does **not** confirm that the raw integrity.json bytes (and thus the exported integrity receipt SHA256) still equal the previously verified original parent ensemble inventory. Whitespace-only integrity drift is invisible to the nested inventory content check.

**Required correction:** Add an explicit original-source-bound comparison-integrity byte/hash check around projection: retain/establish the expected SHA256 of each selected comparison's integrity.json from the already validated outer ensemble seal, and reject if the later read differs; keep request/result original-byte and native comparisons checks. The original outer receipt's trust must not be replaced by an unverified post-preflight receipt. Add negative regressions for **both** injection windows; assert refusal, no output writes, unchanged source-native measurements, and original rather than drifted evidence bindings. Protect the complete sibling/global preflight as before. A small read-only validation correction can receive **targeted R1 re-review** on a NEW exact head; if any source/evidence/measurement meaning must change, **escalate to R2** under the central risk policy.

The test modification was performed solely on an ephemeral reviewer fixture. The readout itself performed no write. This is a bounded ordinary timing probe, **not** a claim that unkeyed hashes resist hostile re-sealing or that the application should provide transactional filesystem isolation.

## 3. Independently executed positive results and negative probes

**Reviewer-owned suite:** Python **3.13.5**, NumPy **2.3.5**, SciPy **1.17.0**, pytest **9.0.2**, Linux. Suite stored outside pinned project source as reviewer_probes_01.py. Reused only the author's fixture **constructors** for a compatible native model/store; all four-sibling arrangements, mutations, test expectations, and assertions described here were reviewer-authored. Full command:

    PYTHONPATH=<pinned-extract>/src:<pinned-extract>/tests python -m pytest -q -W error reviewer_probes_01.py

**Full outcome: 40 passed, 2 failed.** Both failures are the newly discovered B1 integrity.json race windows above (expected fail-closed RevisionError, actual returned readout). There were no other test failures after correcting an initial *reviewer harness* error documented below.

The 40 passing cases independently covered:

- Four mixed siblings, exact indexed selection of a member literally named baseline, retention of the original fresh baseline and global partial status when filtering a complete sibling, correct available/unavailable/empty measurement distinction; no native/template/store/ensemble writes during readout.
- Tamper of an **unselected** sibling (accepted and rejected raw store proposal bytes, comparison result/request/integrity, accepted decision, child revision, native run, source template and original ensemble specification). Original outer summary tamper, re-signed summary that contradicts native truth, and nested+outer re-signed numerical alteration all refused. Healthy-member filtering never bypassed the complete original preflight.
- Unknown, empty, non-string member selectors; prohibited CLI --output, --baseline, --sample-index and invalid sample-index values. Proper exit 2/no output writes.
- Late request/result changes both after full ensemble inspection and after the selected comparison's second inspection, with appropriate refusal. **Only late integrity.json byte changes fail B1**.
- Physically rejected source revision and accepted-but-native-partial analysis as truthful no-measurement outcomes, not zeros; complete original member with globally partial comparison; absence of invented baseline operands.
- Existing **run** and **inspect** CLI, native **view** receipt for a literal member baseline, exact saved member run path, and F1 rejection of screenshot output inside an unrelated sealed original evidence root.
- Historical PR #23 R2-01 late-sibling static-mode/trajectory preflight refusal before native write and R2-02 raw JSON 1e400 non-finite-number preflight refusal, plus original proposal raw-byte checks.

**Author's 79 focused test definitions were not relabelled as new independent tests.** The author's original CI and same-author formula checks are separately cited below.

## 4. Original Linux and Windows ZIP evidence — independently downloaded and audited

GitHub original archives, not copied text from the implementer's readout:

- Linux artifact **14247794085** (CI run 43913225233): exact original SHA256 **a8ec0e8697e43e5ef23892d3e3dc0fe7de3e830bb97d7db175e4393e74cdb014**.
- Windows artifact **14250075846** (same CI run): exact original SHA256 **703f05bc03e2bb411c66a0637a675b59da312f9c65e0566a3a4e3a094a288d86**.

For **each** archive: checked **2,159 unique ZIP entries, all CRC clean**, **33 complete SHA256 file inventories**, **12 original native run inputs with all 60 saved five-field input hash bindings**, **six original sealed signed comparisons**, and **34 original comparison rows = 32 ok + two genuine G1 unavailable**. Independently computed right-minus-left for all 32 numeric scalar/vector values directly from **saved original native result.json** operands and checked native trajectory NPZ arrays, sample times and member/baseline observation correspondence; the two missing baseline operands are genuinely absent and typed **unknown_operand / null / unit null**. The signed values were compared numerically without rounding away the saved readout: independent raw archived readout comparison was **exact equality for every projected source field**, including source-context observation IDs, position/endpoints, unit, method context, signed scalar/vector values and evidence receipt hashes.

Examples checked from original data:

- E1 hypothesis-A field magnitude **-0.05458851160751549 N/C** versus hypothesis-B **+0.18513207463551812 N/C**; E1 hypothesis-A potential difference **-0.11598920858006678 V**; right-minus-left field-vector/trajectory differences preserved with their sign.
- G1 hypothesis-B gravitational field vector starts **-0.013618757987772154 m/s²**, potential difference **+0.0033289658365940333 J/kg**; seven original ok readings plus one **unknown_operand / null**; no value fabricated for absent baseline body. E1 matched samples at saved **2.0 s**, G1 at saved **2.5 s**.
- Screenshot receipts for original **ensemble-view-E1-baseline** and **ensemble-view-G1-member** each bound actual PNG bytes, stored selected run-integrity SHA256, original run ID/reference, with presentation at original saved sample 0 / **time_s=0.0** on both OSs.

The source-equivalent CLI was independently invoked on fresh **extracted copies** of both ZIPs using the actual pinned Python implementation: E1 all/A/B, G1 all/B and T1 all/A — **seven calls per OS, 14 total**, expected exit 0 complete or 1 honest partial, and both published E1/G1 readout JSONs matched exactly. Every file in each extracted 2,159-file archive copy was hashed before/after: **zero mutations**. Replaying a Windows-produced ZIP through the current Linux review container is **not** a new Windows execution; the original hosted Windows job is separately verified below.

Original viewer ZIP artifact **14247663796**, SHA256 **a7660e661947a7eeaa8a285e7975df48f071e6640b386d988fdb1ff74f386bf0**, had 22 unique CRC-clean entries; independently matched **17** original PNG-to-report SHA256 receipts, all **1200×850**, with **16** distinct PNG hashes due to an identical flat/nested pair.

**Evidence boundary:** the 32 independently checked differences confirm arithmetic/signs and faithful *projection from the separately saved original native values*. They do not independently prove that the source model or numerical integrator represents all external physics perfectly.

## 5. Actual exact-head CI (author-run/hosted, not Chat B independent tests)

Directly inspected GitHub Actions job metadata and original job logs, not merely the PR description:

- Clean-install run **43913225233**, Ubuntu job **133460397109** **SUCCESS**: **1,481 passed headless, 18 passed historical behavioral (one obsolete freeze guard deselected), 33 passed real-PyVista**, plus the separately repeated **79 focused passed** (already included within the 1,481). Native E1/G1/T1 study and native readout stages succeeded.
- Same run, Windows job **133460397794** **SUCCESS**, same **1,481 +18 +33** classifications and **79 focused** repeated. This is genuine hosted Windows execution, not reviewer-run Windows desktop testing.
- Separate PyVista run **43913225195**, job **133460400998** **SUCCESS**, **1,481 headless passed** and real offscreen render/slider checks. Source snapshot run **43913225024**, source job successful.
- No local full 1,481-test replay was claimed by this reviewer. Original author-focused tests and same-author separate formulas/RK4 checks must not be equated with independent physics certification.

## 6. Original first failures, provenance, and retention

The first reviewer test run had **10 passes followed by KeyError: 'id'** when this reviewer incorrectly assumed model reference objects use key id. The actual reference uses model_id / revision_id / sha256. This was a **reviewer harness bug**, not an emfeeld source defect. **The original first failure log was preserved unchanged**, SHA256 **88239b9a2607f903bb74f38d0cca690fd01aa3826430dc9748e865d1357f70bd**. Only the separate reviewer harness code was corrected to select the revision via its saved reference.json; no source project file was edited.

The corrected second reviewer run produced the **first real source failure** (late integrity.json drift) after **25 passes**, and its original log is preserved unchanged, SHA256 **94e6184ac0e70473290a90d69e121c68d7adfff6d5ca5688fda3d303cb8f8667**. The final full reviewer-owned suite log records **40 passed, 2 failed**, SHA256 **4ba7e62a44b9a7cadef23a898fd05b612453d713e9440b4df5f44f9bbd60fef0**. Explicit independent reproduction log SHA256 **0b1f79380c75326dda068015c1ed2ea761d5bdecc4ca19859cf6a1b1b5694d28**. The latest reviewer suite's SHA256 is **1e9d789c23a80c67d8ba97b24908a21359495239e9f081835c0327b8d418214f**.

Archive auditor, separate native CLI replayer, reviewer probe suite, repro code and **the original first logs** are retained as reviewer-owned evidence outside the source repository (downloadable review evidence bundle in the owner conversation). No original GitHub archive, native study, historical review, or PR #27 source file was modified.

## 7. Gate and limitations

**CHANGES REQUESTED** for B1. All executed static signed-value, SI-unit, original comparison, typed unavailable, global-partial, rejected/native-incomplete, path protection and ordinary original input tamper checks passed. The **two mid-read integrity-receipt failure cases** prevent an unconditional R1 PASS for strict original evidence provenance.

Source PR #27 **must remain DRAFT and UNMERGED**. Have Chat A implement the narrow, regression-tested original-manifest/receipt stability guard on a **new head**, rerun current-source applicable CI, then request **targeted independent re-review**. Escalate to R2 if fixing this requires altered numerical/evidence meaning. Any later different head is not covered by this report.

Unkeyed SHA256 is not an authentication scheme against malicious re-signing; this review does not certify hostile concurrent-file attack resistance, ACID transactions, manually operated Windows/Vista/VTK pointer behavior, human scientific review, or real classroom learning outcomes. No teacher acceptance or model/source-interpretation fidelity is inferred from the archival checks.

**Owner handoff:** Return to Chat A and say **"review done"**. Chat A can retrieve this committed report directly; the owner alone controls later merge approval.