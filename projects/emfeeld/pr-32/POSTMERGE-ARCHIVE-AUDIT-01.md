# PR #32 — author post-merge original-archive audit 01

**Disposition: PASS for the declared automated/documented Physics Demonstration V1 release gates on actual merged `main`.** This is a read-only author-side audit of *new original* GitHub Actions artifacts, not a claim of independent human physicist review, manual Windows GUI acceptance or classroom effectiveness. Independent Chat B R2 review of the identical source tree passed **before** merge: [review 01](reviews/review-01-chat-b.md). See [merge report](MERGE-REPORT.md) for historical and exact integration evidence.

## Exact release source and actual main jobs (2026-11-17)

Original merge commit **`a18c26f050f5320ce8a9d61f7169e32cd6e31f38`**, Git tree **`9f59fd94a15a1f0c2759ab8662b23a36a41810da`**, identical to reviewed head `fb2ebe0c65425a79dec1482bc26162756f72f5d5` and independent source checkout/tree reconstruction. GitHub merge commit parents were [PR #29 qualified main `3f1ec44a54b24b9f8275a98abf81126a9386bf61`, PR #32 exact reviewed source `fb2ebe...`]. Main ref was verified at this exact merge SHA at the audit.

- [Actual main-push Linux/Windows release workflow #44030140577](https://github.com/physicsvigilante/emfeeld/actions/runs/44030140577) original GitHub `event=push`, head SHA `a18c26...`, attempt 1, **completed SUCCESS** on both jobs:
  - Ubuntu 24.04 job **`133859825450`**: 1,502 headless passed (102.83 s); 18 historical behavioral passed, one obsolete all-file freeze assertion deselected; 33 real-PyVista passed; Physics Demonstration V1 archived replay `{"passed": true, "cases": 1}`; all native qualification steps passed.
  - Windows 2022 job **`133859824990`**: 1,502 headless passed (115.06 s); 18 historical behavioral passed, one obsolete freeze guard deselected; 33 real-PyVista passed; Physics Demonstration V1 archived replay `{"passed": true, "cases": 1}`; all native qualification steps passed.
  - No additive double counting of repeated focused tests, which are already part of the headless definitions.
- [Actual main-push separate real-PyVista #44030140648](https://github.com/physicsvigilante/emfeeld/actions/runs/44030140648): job **`133859824987`** **completed SUCCESS**, nine scene real offscreen render/programmatic time-event cases, 1,502 headless original suite passed in that workflow. This is Linux offscreen, not manual Windows pointer/mouse qualification.
- No new main-push source-snapshot workflow is expected because the source snapshot is configured for PR/dispatch; the **actual main real-PyVista original source tar** independently reconstructed to exactly the same Git tree `9f59fd...`.

## Original post-merge archives — independently downloaded and verified

| Original artifact | Artifact ID | Independently computed ZIP SHA256 | ZIP inventory/CRC |
|---|---:|---|---|
| Actual main Ubuntu release | **`14305546256`** | `005de875812ef7392861cc2e95c1aa04dc77621586c43943aa4685e272b624a8` | **2,166 unique, CRC-clean entries** |
| Actual main Windows release | **`14305786418`** | `fd78ea37951a61c214d391b5d2dc16962d35296774d483364b0f76461dd4048f` | **2,166 unique, CRC-clean entries** |
| Actual main real-PyVista | **`14305285724`** | `327d72c8ca76179817caaef85eaf5133ccf4e3fd43ecc5414f3c0b9c10cd77f3` | **22 unique, CRC-clean entries; 17 original PNGs** |

The three independently computed ZIP hashes equal the actual *original* GitHub artifact digests. Original ZIP entries were checked for duplicate names, unsafe path traversal, and CRC/read failures. The original OS releases were not inferred from pre-merge archives. All uploaded files were available only to this audit workspace; **no original source or original GitHub artifact was modified**.

### Direct original per-OS physics replay audit

For both new OS ZIPs, the following archived files were opened and checked, not inferred from workflow logs:

- `physics-demo-v1/manifest.json`, byte-for-byte identical to frozen published source `verification/physics_demonstration_v1.json`, raw SHA256 **`f6321e4fb220cb6b2a5aca895a81337a2e6b650e3c39e2bbed7d0f4089ff63e8`**.
- `physics-demo-v1/uniform_electric_v1/input.json`, byte-for-byte identical to original source `examples/physics_demonstrations/uniform_electric.json`, SHA256 **`ff9ce129f906b4cb6b68fa27819e33fa6d54637a8c3412d4f6fb1970c11ecf52`** on **both** OSs. Original source is fixed electrostatic E=(3,0,0) N/C, q=2e-6 C, m=1e-3 kg, 41 saved samples over 4 s and origin-pinned potential.
- `physics-demo-v1/uniform_electric_v1/result.json`: each original has **17 unique named observations, all `status=ok`, `counts.requests=17`, `counts.evaluated=17`**, zero domain/numerical errors, correct saved indices `0/20/40` and times `0/2/4` s. Native DOP853 run status `ok` with original `rtol=1e-10`, position/velocity atol `1e-9`, max step 0.02 s.
- `physics-demo-v1/summary.json`: one original case `passed=true`; **all 64 distinct saved source/reference comparison checks individually `passed=true`**. Independent audit independently read every declared check, verified each native result status, exact value/type, SI unit, original index and time; did **not** accept summary exit 0 alone.
- The **29 `src/emfeeld/*.py` original hashes** in each `summary.json` independently match the exact reviewed Git-source files; Linux uses Git-tree LF Python bytes and Windows source files use CRLF as normal for platform checkout, while authored `*.json text eol=lf` ensures exact common packet bytes.
- Separately derived kinematics and total-energy expressions (no emfeeld force law or solver imported): at t=4 s predicted `r=(0.648,0.1,0.3) m`, `v=(0.124,0.05,0) m/s`, `K=8.938e-6 J`, `U=-3.888e-6 J`, total `K+U=5.050e-6 J`. Checked t=0,2,4 and signed `U=qV`; worst observed original errors per platform **position 1.8874e-15 m, velocity 9.8532e-16 m/s, energy 1.2198e-19 J**. These are finite observed errors, not certified global solver-error bounds.
- Original `head-sha.txt` inside **each** OS artifact is exactly **`a18c26f050f5320ce8a9d61f7169e32cd6e31f38`**. Original archived `headless-tests.log`, `pilot-behaviour-tests.log`, `viewer-tests.log`, `physics-demo-v1.log` were opened directly and their conclusions matched the original job logs.

An extra **synthetic negative control** modified only one copied original Linux ZIP `result.json` `position_40.value[0]` by +0.1 m and recalculated its ZIP SHA256. The independent archive checker **refused the altered numerical result despite the correct new outer ZIP digest**, demonstrating it does not merely trust the outer checksum or the `summary.passed` field. This deliberately modified test ZIP was **not** any original source/evidence artifact.

### Existing qualified ensemble behavior preserved in new originals

Both new OS archives also retain fresh native E1/G1 measurement records:

- E1: global **complete**, two independent accepted members (`hypothesis-A` and `hypothesis-B`), 5/5 `ok` signed comparisons each, original source receipt present.
- G1: global **partial** with selected native-complete `hypothesis-B`, 7 `ok` comparisons and exactly one honest **`unavailable / unknown_operand / null`**. No synthetic zero or silent promotion to complete.

These are checks of the original new archive's recorded outputs plus original CI success, not a claim of byte identity across OSs or that every historical saved file was externally re-executed.

### Original real-PyVista archive

Original viewer ZIP `14305285724` was downloaded and rehashed, all 22 ZIP entries CRC-tested. Its `report.json` pins actual merge commit `a18c26...`, reports **9/9 PASS offscreen cases** and **17 frames**, each original PNG named/hash-bound in `report.json`. Independently recomputed SHA256 for **all 17 original PNG byte streams** and checked exact frame name inventory. Independently extracted `tested-source.tar`, recreated a Git index and obtained **Git tree `9f59fd94a15a1f0c2759ab8662b23a36a41810da`**, exactly the merged source tree. Nine first-frame and eight later-frame thumbnails were viewed in contact sheets; no obvious blank frames or gross plotting failures observed. This was a limited author-side visual sanity check, **not** fine-grained expert screenshot acceptance, human Windows mouse interaction or teaching-usefulness certification.

## Boundary and disposition

**PR #32 release's declared automated, exact-source and original-archive gates are closed, subject to the retained explicit limitations:** no full Maxwell/magnetic field solver, no interacting test-particle feedback, no general source interpretation proof, no independently certified global numerical-error bounds, no human-physicist sign-off, no classroom usefulness validation, no manual Windows desktop interaction, and no malicious fully re-sealed unkeyed hash authenticity claim. Unrelated PR #33 is separate and was **not** modified or integrated by this release audit.
