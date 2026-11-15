# EM Fields PR #13 — owner-approved merge and final post-merge qualification

**Release status: MERGED and POST-MERGE CI PASSED, 2026-11-15.** This report is a new append-only record in the central review hub; no independent reviewer report was overwritten.

## Source and authorization

- Project: [EM Fields / emfeeld](https://github.com/physicsvigilante/emfeeld); [source PR #13](https://github.com/physicsvigilante/emfeeld/pull/13), now **merged/closed**.
- Owner explicitly approved merging after the independent review follow-up passed. No blanket approval of unrelated milestones is inferred.
- Qualified and approved source head: `e7c772af39c6271cd7a033ec2a006d617a51b442`, parent main `c67d1115ad6fc982f29fe113583430e676938902`.
- Merge commit / exact new `main`: **`7e6bd8c72cac7708ab3c2355cc1a98db09762133`** ([view](https://github.com/physicsvigilante/emfeeld/commit/7e6bd8c72cac7708ab3c2355cc1a98db09762133)).
- Merge parents: `c67d1115ad6fc982f29fe113583430e676938902` and `e7c772af39c6271cd7a033ec2a006d617a51b442`.
- Git tree at merge: **`ea4efcc21e101be8ceb11cbae5c14924e45d172b`**, identical to both the approved corrected head and the earlier qualified CI merge-preview tree. **No additional source changes entered through merge.**

The merged capability processes existing fully sealed native run observations into explicitly authored compatible scalar ratios or same-saved-time two-particle separation. It does not introduce new force laws, a different integrator, new viewer behavior, frame interpolation or automatic source-model mutation.

## Preserved R2 independent-context review history

- [Original Chat B review 01](reviews/review-01-chat-b.md) — **changes-requested**, reviewed source head `766633a60679208f534c5d299578b100d2d29eea`, immutable Git blob `bc527fb081446faef8e37714d331c0bf7cc8455d`. Four findings were documented and independently reproduced; the original negative evidence remains unchanged.
- [Targeted Chat B review 02](reviews/review-02-chat-b.md) — **pass strictly for F-01–F-04**, reviewed exact corrected head `e7c772af39c6271cd7a033ec2a006d617a51b442`, reviewer-authored blob `ca547f158a0216d41659dad356e4c6a0a16895e0`. Reviewer reran 46 existing derived tests and executed 83 independent adversarial cases. It is a separate ChatGPT context, **not an independently accredited human physics review**.
- [Developer correction response](responses/response-01-chat-a.md) and [final review triage](responses/response-02-chat-a.md) remain separately attributed. The corrections prevent nonzero ratio underflow from masquerading as successful zero, reject contradictory completion even if a copy is re-sealed, reject invalid physical magnitudes, and handle unrepresentably large/malformed saved times without an unhandled overflow.
- There were no further source changes between targeted review 02, owner approval and merge.

## Accepted pre-merge qualification (same exact tree)

- [Linux and Windows release CI](https://github.com/physicsvigilante/emfeeld/actions/runs/43729059256): passed, **per OS** 1,265 headless + 18 historical behavioral + 33 real-PyVista tests.
- [Separate real-PyVista workflow](https://github.com/physicsvigilante/emfeeld/actions/runs/43729059279): passed.
- Source-bound CI evidence and all reviewer limitations remain recorded in [FOLLOW-UP-02.md](FOLLOW-UP-02.md) and in the original reviews.

## **Fresh post-merge main CI — completed and independently audited**

- [Post-merge Linux/Windows release workflow](https://github.com/physicsvigilante/emfeeld/actions/runs/43733310019) — **completed successfully on both Ubuntu 24.04 and Windows 2022**, checking out exactly `7e6bd8c72cac7708ab3c2355cc1a98db09762133`.
- [Separate post-merge real-PyVista workflow](https://github.com/physicsvigilante/emfeeld/actions/runs/43733310048) — **completed successfully**.
- **Per platform:** 1,265 headless tests passed with warnings as errors; 18 historical behavioral tests passed; 33 real-PyVista tests passed. **1,316 test definitions across suites per OS**. The extra 46 focused derived tests also passed as a rerun of tests already included among the 1,265 headless cases, and are **not** added to the unique test count. The historical whole-file freeze assertion remained unchanged and explicitly deselected (one).
- The same test definitions were exercised across two operating systems, **not 2,632 distinct tests**.

**Downloaded and hashed original post-merge artifacts, with all ZIP entries passing CRC:**

| Platform | GitHub Actions artifact ID | ZIP SHA256 | Count |
|---|---|---|---|
| Linux / Ubuntu 24.04 | `14169451891` | `7462e7ead27f409a66539544b7079f5837fa6942d4a19df1d2c2fe6b6d3159f9` | 1,250 entries |
| Windows / Windows 2022 | `14169552449` | `11bb10c0da1c8825e0d1f6e69eca48549ec0795713858ad96df534d0284dc340` | 1,250 entries |

Both archive digests exactly match GitHub's artifact digests. Both archives' `head-sha.txt` equals `7e6bd8c72cac7708ab3c2355cc1a98db09762133`. The retained test logs explicitly report 1,265 / 18 / 33 passing results per OS.

A separate read-only audit of the *original archived* E1/G1/T1 derived outputs checked their integrity manifests, exact `run.json` and native packet SHA256 bindings, physical units, saved-time/index identity, named operand arithmetic, and null-valued unavailable outcomes:

- **E1:** successful dimensionless field ratio; aggregate `complete`.
- **G1:** successful field ratio and valid same-time two-body separation, plus intentionally unsupported mismatched-time observation with `unavailable/different_saved_times`; aggregate correctly **`partial`**, not a release failure. The archived disposable re-sealed status-forgery and invalid-source-magnitude challenge outputs are present. The original native run is unchanged.
- **T1:** two successful electric static field ratios; aggregate `complete`.

The read-only audit did not run another native integration or add an independent research-author reference calculation. The **same-author** source/trajectory reference checks and negative controls ran as part of the successfully completed hosted CI. No real Windows desktop/classroom interaction is inferred from offscreen rendering.

## Release boundaries and next tasks

**Final status:** approved source PR merged, exact tree preserved, all required post-merge CI green, and final central record updated. There is no outstanding PR #13 release blocker among the four independently reviewed findings.

This does **not** establish cryptographic authentication of model/run evidence (inventories are unkeyed hashes), independent human numerical certification, source-interpretation fidelity on unseen textbooks, or classroom learning effectiveness. The user's local Conda installation, preserved teaching source documents, and original recorded runs were not modified by the GitHub merge.

Future capability changes require their own source branch, risk classification, CI, review scope and separate owner merge approval under [PROTOCOL.md](../../PROTOCOL.md) and [REVIEW-RISK-POLICY.md](../../REVIEW-RISK-POLICY.md).
