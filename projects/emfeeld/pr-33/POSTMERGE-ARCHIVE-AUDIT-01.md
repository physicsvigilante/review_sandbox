# PR #33 — direct original merged-main artifact audit 01

**Disposition: PASS — all declared exact-source, automated main-push and original-archive release gates closed for Teacher-task Evidence Transfer V1 (2026-11-17).** This is an **author-performed read-only verification** of original downloaded GitHub Actions ZIPs, not a second independent Chat B review, human physicist certification or classroom usability study. The separate independent R2 correction review is [review-02-chat-b.md](reviews/review-02-chat-b.md).

## Actual merged main and workflow identity

- Source [PR #33](https://github.com/physicsvigilante/emfeeld/pull/33) is CLOSED/MERGED, GitHub main merge commit **`1b0149d773f924e67e0cd1f950da8b5d0ffacaa2`** with Git tree **`88364f2394dd84e6270681b3efd1ff879fc397dc`**; ordered parents **[`a18c26f050f5320ce8a9d61f7169e32cd6e31f38` (qualified PR #32 main), `73a61aaa16f79df12a54231b738074bb2826e66f` (independently reviewed corrected PR #33 head)]**. Fresh GitHub live main-ref and PR reads confirm this exact merge SHA, not just a preview. This source tree is **identical** to the original source-equivalent pre-merge preview `ac33369acfef282e50748e9221426b11237d2b9d`, whose 356-file source snapshot had already been independently reviewed/reconstructed.
- Actual [merged-main push Linux/Windows run #44041409744](https://github.com/physicsvigilante/emfeeld/actions/runs/44041409744), **`event=push`**, head exactly `1b0149d...`, attempt 1 **COMPLETED SUCCESS** on **both** original jobs: Ubuntu 24.04 job `133896623648` and Windows 2022 job `133896623458`. Each archived real test logs independently say **1,526 headless passed**, **18 historical behavioral passed and one obsolete all-file freeze assertion deselected**, **33 real-PyVista passed**. Repeated scenario-focused tests are within the 1,526 full headless total; no double counting.
- Actual [merged-main separate real-PyVista #44041409891](https://github.com/physicsvigilante/emfeeld/actions/runs/44041409891), **`event=push`**, head exactly `1b0149d...`, **COMPLETED SUCCESS**. The original offscreen viewer ZIP was downloaded and independently inspected, including its embedded exact merged-source TAR.

## Fresh original post-merge ZIPs, downloaded, rehashed and CRC-audited

| Actual new main artifact | GitHub artifact ID | Independently recomputed whole-ZIP SHA256 | Original ZIP inventory |
|---|---:|---|---|
| Ubuntu release | **`14309359462`** | **`ff9108bd75040a9052dccb00e44ef0ab860c9e5ac82947029ac6aef2a1fd0bc1`** | **2,166 unique CRC-clean entries** |
| Windows release | **`14309789192`** | **`9374c936af39d0f8611c306c9b4f5e324c38f4e4d55b2d9d2ab1d5bc3bf2f652`** | **2,166 unique CRC-clean entries** |
| Separate real-PyVista | **`14308889594`** | **`6c06be750cf102447786be29cc4091bcafe6bf5e6c807d9611c3356d1d9708f7`** | **22 unique CRC-clean entries, including 17 PNGs** |

All three computed whole-ZIP SHA256 values match GitHub's **original artifact digest** metadata. Every ZIP entry was checked for duplicated/casefold-colliding names and unsafe paths, and original uncompressed bytes read with a full ZIP CRC check. Original ZIPs and sealed studies were not changed. Do **not** conflate these actual new main-push artifacts with pre-merge corrected-head ZIPs `14307743114` / `14308247410`.

### Verified original Linux and Windows physics/engine evidence

Independently opened the *new* original files inside each OS archive rather than accepting workflow success alone:

- `head-sha.txt` is exactly the **actual merge `1b0149d...`** on both OSs.
- `physics-demo-v1/manifest.json` original bytes have SHA256 **`f6321e4fb220cb6b2a5aca895a81337a2e6b650e3c39e2bbed7d0f4089ff63e8`**, matching the frozen reviewed source. `physics-demo-v1/uniform_electric_v1/input.json` matches published source byte-for-byte, SHA256 **`ff9ce129f906b4cb6b68fa27819e33fa6d54637a8c3412d4f6fb1970c11ecf52`** on both OSs.
- Original numerical `result.json` reports **17 distinct named observations**, all `ok`, 41 saved samples across t=0..4 s, correct indices/times t=0,2,4 s, correct SI units and original solver configuration (DOP853, rtol `1e-10`, 1e-9 position/velocity absolute tolerances, `max_step_s=0.02`). Original `summary.json` has exactly one case with **64/64 individually passed** status/physical-value/unit/sample/time comparisons; the audit also independently recalculated each declared reference check and separately applied the closed-form uniform electric acceleration/energy equations. No fake numerical zero was accepted for an absent operand.
- Across those exact original native physical results, the observed worst absolute differences from separately derived analytic values were **Linux position 1.8874e-15 m, velocity 9.8532e-16 m/s, energy 1.2197e-19 J**; **Windows position 1.9984e-15 m, velocity 9.8532e-16 m/s, energy 1.2197e-19 J**. These are sampled measured errors, **not certified global integration-error bounds**.
- Both original `summary.json` engine-inventory maps contain **29 original `src/emfeeld/*.py` SHA256 hashes**, each independently matched to the source-equivalent reviewed Git tree, accounting for ordinary **Windows CRLF Python checkout** (authored input JSON stays LF and byte-identical). All original `headless-tests.log`, `pilot-behaviour-tests.log`, `viewer-tests.log` and `physics-demo-v1.log` were inspected.
- In each original ZIP, `ensemble-measurements-E1.json` correctly retains **global complete**, two independent sibling members and 5/5 `ok` original signed comparisons each. `ensemble-measurements-G1.json` still reports **global partial**, 7 valid signed comparisons plus exactly **one `unavailable/unknown_operand/null`** (new body absent from baseline); no fake zero or promotion to complete.

### Actual original viewer archive and source-tree reconstruction

Downloaded viewer archive `14308889594`, recomputed ZIP SHA256 and CRC/22-member inventory. Original `report.json` pins actual merged commit **`1b0149d...`** and records **nine `PASS` real-offscreen source/field/trajectory rendering and programmatic slider-event cases**. Independently verified **all 17 original PNG SHA256 receipts** against actual embedded image bytes and exact frame inventory. The original `tested-source.tar` SHA256 **`959e4e104b094d5279570f2f3b816df68909d3d8f12730f455c65676d19beb7e`** was extracted into a disposable directory; staging all **356 original tracked files** with Git and running `git write-tree` independently reconstructed the **exact actual merge tree `88364f2394dd84e6270681b3efd1ff879fc397dc`**. This is actual original release-source identity, not just a claimed source archive label.

The report's `visual_inspection` field remains explicitly **PENDING**, so do **not** call this expert screenshot acceptance, classroom assessment or manual Windows mouse qualification.

### Independent replay of original fixed three-question evidence transfer

On the exact reconstructed source tree, executed the **real corrected read-only pilot CLI** on the two ORIGINAL separately qualified **PR #29** main release ZIPs, not on these newer PR #33 CI release ZIPs. Whole original stdout SHA256 remains **byte-identical** to the pre-correction qualified output:

- Original PR #29 Linux ZIP `14300302937` → stdout SHA256 **`0e0d0db21e19b5075df9be3069937f88156dbe914cd1cd0e987a0ba7cba3aab7`**.
- Original PR #29 Windows ZIP `14301401780` → stdout SHA256 **`20615a519c9f674387ce6d9e29f307f8227c5e1f372441f077f2877a09e483bb`**.

Each returns **three frozen retrospective developer-authored questions, four original source-bound signed E1/T1 measurements and one genuinely unavailable G1 `unknown_operand/null`**, preserving original source/result/request/integrity/left/right-run receipts and `educational_usefulness=not_evaluated_without_teacher`. Both original PR #29 raw archives were byte-identical before/after execution. Additional ad-hoc negative source-interface probes refused (a) an extra-file modified ZIP under canonical mode, and (b) attempted `--fixture` override, both **exit 2 and zero verified JSON stdout**. Neither adversarial copy changed an original release.

## Historical review and evidence qualifications

Original source review-01 was genuinely **CHANGES REQUESTED** for B1/B2 on the older head; that original report remains unchanged. The narrower corrected source `73a61...` passed subsequent separate-context [Chat B R2 review-02](reviews/review-02-chat-b.md), 28 reviewer-owned B1/B2/N1 executed tests with recorded original first harness discrepancy; original canonical source/ZIP and physics receipts verified. This author-side post-merge audit **is not a new independent review or teacher certification**.

**All declared automated post-merge release and original artifact-audit gates PASSED.** Remaining deliberately unsupported claims: no external teacher-authored unseen question, classroom educational acceptance, arbitrary natural-language physics interpreter, Maxwell dynamics/conductor polarization, full source feedback, manual Windows pointer/slider verification, certified global numeric-error bounds, hostile all-hash/whole-code rewrite authenticity or hostile distributed filesystem ACID. Original independent hypotheses are **alternatives**, not a temporal physical process. Any claim of Linux/Windows original JSON numerical byte identity would be incorrect (normal native platform differences); the original authored packet bytes and independently pinned question fixture identities remain exact.
