# SIM_HEAT PR #33 — targeted Chat B R2 re-review (review-02, after integrity corrections)

**Review type:** focused R2 corrective source/evidence review of **F-01–F-03 from [independent review-01](reviews/review-01-chat-b.md)**. Historical original review remains unchanged.
**Source PR:** [physicsvigilante/sim_heat draft #33](https://github.com/physicsvigilante/sim_heat/pull/33). **No production merge or OpenModelica permitted.**
**Original reviewed head:** `b8c5152aac86fc1be32f7b98e032f108d8345c66`, Git tree `96623697609c6cd56cf2f1f9c5a646e35a3596c9`.
**Exact NEW candidate HEAD:** **`bf51e7721bca73720aa9b5f5f2de90defee821ec`**.
**PR immediate base (frozen historical experiment):** `502a6e8c392d8b8cfb8a4361cddcae4fafff6f01` (PR #32), original frozen H1-F0 `dd8c9432abe97563414bb3ed809e61e673473812`.
**Risk:** R2 integrity/provenance semantics, no physics change.
**Review output:** new `projects/sim_heat/pr-33/reviews/review-02-chat-b.md` **written by independent Chat B only**, PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE **for corrected candidate storage integrity only**.

## Original independent finding and unchanged history

PR #33 review-01 returned **CHANGES REQUESTED** for two reproduced integrity-contract defects (the original PR #31 archived checking JSON bytes and default unauthorised-use refusal were independently PASS):
- **F-01 MAJOR**: current inspector could accept manifest with forged unchecked lineage/provenance, including forged original ZIP hash, altered member filename, falsified `origin`, erased failed cross-host record, and false permanent retention claim. The raw mathematical JSON remained SHA-pinned, but historical claims were not.
- **F-02 MAJOR**: an otherwise identical raw JSON recompressed to a *different valid* XZ/preset-3 binary (636,796 bytes, reviewer SHA `2b4822fce03a1795d3e48ae266dcd9ef18b5bdc35bda72d055415f842636b322`) was accepted by standalone inspector when `archiveBytes` and `archiveFullSha256` were forged in manifest. The exact Git compressed-object claim was not independently bound.
- **F-03 MINOR**: `LZMADecompressor` lacked a decoder-memory limit despite length-bound input and decompressed output. It was not exploited and must not be labeled a demonstrated DoS.
- Reviewer independently verified original archived PR #31 raw SHA `0db511dd8dba023d16518667de256029cf3e073463ea21e2478aeac8afd1f368` and canonical seal `d2b8e2ca8e1f929cac7b028dcc3f7d0b453921d193f877eb091e23ac70aa4ce9`, while retaining the original frozen F0 **80× FAIL**, PR #32 bitwise generation **FAIL**, and no native result.

## Corrective candidate at exact `bf51e...`

Four **modified paths only relative to the original reviewed head**, all originally new PR #33 candidate files:
1. `qualification/h1_c1/immutable_fixture/inspect_pr31_fixture.py`: before JSON parsing, match **entire manifest raw SHA-256** against **code-trusted independently pinned literal** `50467b138ed64cdb908f2c763bc777e6babf0bb04a0711568acc559112e66f84`. Before decoding, independently check actual compressed binary SHA-256 `fc5a7df5928c3fb8aef2ba4af516dfbd32b42c0450ebef1051ad4fd7efebd17f` and exact size **503,552 bytes**, not merely the manifest's changeable hash/size. Use `LZMADecompressor(format=FORMAT_XZ, memlimit=64MiB)`, maintaining bounded raw length and original raw SHA and JSON seal. Source constants are trusted **only** under an exact independently approved future code commit: floating Git branches or an attacker-edited standalone source cannot authenticate owner authorization.
2. `test_pr31_fixture.py`: add mutation subtests for all reviewer F-01 originally unchecked attributes (including erasing failed cross-host record and retention text), alternate valid XZ/preset-3 compression with forged manifest hash/size, malformed XZ header rejected *before* decoder and positive original decoder `memlimit` assertion. Existing raw hash/source/approval/default refusal regressions remain.
3. `.github/workflows/h1-c1-f0-fixture-verify.yml`: read-only exact-head CI now triggers on **every** new immutable-fixture source/manifest/doc/binary path and on archive-writer workflow policy. No OMC, no write token, no background auto-launch of native.
4. `IMMUTABLE_FIXTURE_CANDIDATE_SCOPE.md`: explicitly records independent finding and correction, limits of code-embedded digest trust, preserves original review history and all default-deny/native HOLD.

**Unmodified:** original 503,552-byte compressed binary, original 37-line manifest, original 4,409,800-byte PR #31 JSON, original frozen H1 physics/checker/runner, first authored task/model/study, PR #31 original 100× sampled mathematical evidence, original failed F0 80× reference, PR #32 two-host bitwise FAIL, all historical CI. **No new reference preparation**, no replacement original artifact, no installed Modelica or native launch.

## Exact-head offline CI/evidence

[Source run #43934967279](https://github.com/physicsvigilante/sim_heat/actions/runs/43934967279) completed **SUCCESS** at exact `bf51e7721bca73720aa9b5f5f2de90defee821ec`.
[Original evidence ZIP #14259763856](https://github.com/physicsvigilante/sim_heat/actions/runs/43934967279/artifacts/14259763856), **12,579 bytes**, whole ZIP SHA-256 `5cc97cd2944d68d55f895fda9ee8668be74967e30f7211fe6906aea5c83aec94`; personally downloaded by Chat A and CRC checked **11/11 members**, preserved `head-sha.txt` exact, frozen **14/14 SHA pins** PASS, **9/9 candidate archive/refusal tests** and **149/149 frozen H1 tests** PASS. Original raw/compressed/canonical seals match; no unauthorized consumer use (`REFUSED_NO_APPROVED_CANONICAL_FIXTURE`), inspection-only report `CANDIDATE_STORAGE_INTEGRITY_PASS_NOT_AUTHORIZED_FOR_NATIVE`. Original failed archival source CI remains failed, no silent reclassification.

## Targeted adversarial independent checks

1. Verify exactly **four modified** scoped candidate paths relative to reviewed source head. The archival 503,552-byte file and original raw manifest SHA/blob are byte-identical, plus all first author/frozen source identities unchanged. No original history overwritten.
2. Independently recompute **SHA-256 of entire committed manifest bytes** and compressed Git blob bytes, compare to constants embedded in corrected inspector; verify exact size and raw JSON roundtrip. Confirm there is no circular trust in manifest's `archiveFullSha256`/`archiveBytes`.
3. Rerun review-01's **five manifest-forgery** cases and valid alternate XZ/preset-3 + forged manifest SHA/size. Confirm each **REFUSES**. Test a forged `approvedForNative=true`, corrupted binary/header, exact raw source/manifest expected data and a malicious/truncated XZ header where possible. Verify no decompression before immutable-compressed-sha validation, check `memlimit` semantics and whether 64MiB is sufficient for original genuine archive. Distinguish new CI assertion coverage from personally run reviewer tests.
4. Check the **default-deny** inspector and the explicit `--inspect-only` audit path. Neither can authorize a reference or native plan, and exported bundle data should never be confused with authentication. New source constant is trusted only for exact pinned code revision; owner policy and protected ref remain unimplemented.
5. Inspect exact-head GitHub CI, source SHA, ZIP SHA+CRC, 9 tests/149 original tests/14 original source pins, preserved original failed archival CI, no executable Modelica/OMC use. Distinguish downloaded evidence from assertions/CI-only results.
6. Report scoped verdict for **F-01/F-02 integrity corrections and F-03 hardening**, separately note open future root-of-trust, branch/ref retention, owner adoption, reference-bound F-02 plan, across-run one-shot gating, host identity, native/post-native R2. **No historical source PR merge, native execution, reference certification, waiver of strict 100×, or retrospective bitwise generation PASS.**

**Chat A disposition:** [response-01-chat-a.md](responses/response-01-chat-a.md) accepts findings, pins new code/CI, requests this targeted review. Read [PROTOCOL.md](../../../PROTOCOL.md), [REVIEW-RISK-POLICY.md](../../../REVIEW-RISK-POLICY.md), [REVIEW-TEMPLATE.md](../../../REVIEW-TEMPLATE.md), and original source contracts. This targeted review is distinct from unchanged original report.
