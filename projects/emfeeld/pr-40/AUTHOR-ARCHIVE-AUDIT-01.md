# PR #40 — exact-source original GitHub archive audit 01

**2026-11-17 — AUTHOR pre-merge qualification PASS; independent R2 review is NOT YET COMPLETE.** The candidate is [draft PR #40](https://github.com/physicsvigilante/emfeeld/pull/40), tracking [Issue #39](https://github.com/physicsvigilante/emfeeld/issues/39). This is an author audit of actual original GitHub-hosted artifacts; it is **not** an independent Chat B verdict, permission to merge, or proof every possible defect is absent.

## Pinned source identity

Released qualified main/base: `066c94e4953c3ef29302c0bb6d0ee2f6cb8b8ca0`, tree `33b58fb55b387ec2b7c1bdd61bf1af7764db97cd`. Candidate exact head: **`9fa09dec92b8925591505d1da0bc2639a53a30d9`**, canonical Git tree **`9491d39d3f0415a5e90f1848173cf73af5d02584`**. GitHub source-equivalent PR preview `4b72af81ca7e0579c8b232c76143e0af8e008e03` is the source tested in the PR workflows, not an actual post-merge main commit.

Source ZIP contained four CRC-clean members including `tested-source.tar` SHA256 **`77bef7944ba6456a6904ce8c771b7a27c0077f21d940798ffa17960082b82e3a`**. The original tar was safely extracted with no links or parent escapes. All **371 tracked files** were re-indexed in a fresh local Git repository. `git write-tree` reproduced exact `9491d39...`; the independent `git ls-tree -r` bytes matched original `git-tree.txt` byte for byte. Original viewer archive embeds **byte-identical** source tar. This qualifies the tracked tree identity, not untracked environments or human review.

## Completed original GitHub Actions workflows

- Fresh exact-source [Linux/Windows clean-install #44131680713](https://github.com/physicsvigilante/emfeeld/actions/runs/44131680713): **COMPLETED SUCCESS on both Ubuntu-24.04 and Windows-2022**. Each *original ZIP's test logs* records **1,629 current headless passed; 18 historical behavioral passed with one obsolete all-file snapshot guard deselected; 33 real-PyVista tests passed**. The 44 new audit cases are **included** in 1,629, not counted separately.
- [Separate real-PyVista #44131680696](https://github.com/physicsvigilante/emfeeld/actions/runs/44131680696): COMPLETED SUCCESS; original viewer report **9/9** offscreen render and programmatic slider case statuses PASS, **17/17** PNG SHA256 receipts verified against valid original PNG bytes, original viewer test log **1,629 headless passed**. `visual_inspection=PENDING`: neither full human visual assessment nor manual Windows mouse interaction is claimed.
- [Exact source snapshot #44131680742](https://github.com/physicsvigilante/emfeeld/actions/runs/44131680742): COMPLETED SUCCESS; original source TAR/index identity reconstructed as described.

## Original artifact ZIPs independently downloaded and rehashed by author

| Exact-source original artifact | Artifact ID | Whole original ZIP SHA256 | Audit |
|---|---:|---|---|
| Source snapshot | `14348834555` | `9f256818a0b84f26d7a3246640622cfbc644747fdac14c291fab7c00a19a94ab` | 4 members, all CRC-clean, 371 tracked Git files |
| Separate viewer | `14349439448` | `d2badd4f8deb872b6e022711a8279ca44c5e4d2ce5975be7e8befbe12d5f3694` | 22 members, all CRC-clean; 9 scenes/17 PNG receipts |
| Ubuntu release | `14350906584` | `47ef95e9be09b1c30b521daec16a9f30564e51cca6c8d48b6ebc33a67a552b5e` | 2,186 unique, casefold-safe, path-safe, CRC-clean entries |
| Windows release | `14351741780` | `7f22e02f1785f3c697b1b8a09ffa9919d8eb8955312d3aae081773da5a30c3b0` | 2,186 unique, casefold-safe, path-safe, CRC-clean entries |

Every original whole ZIP SHA256 was recomputed from downloaded bytes and matched GitHub's original artifact digest. Every member was actually read for CRC; absolute/traversal paths, unsafe separators and duplicate/casefold duplicate names checked. Both OS `head-sha.txt` report **`4b72af81ca7e0579c8b232c76143e0af8e008e03`**, correctly identifying the source-equivalent **PR preview**, not post-merge main.

## Source-bound native physical evidence in both ORIGINAL OS archives

- Original question-first developer gravity fixture: frozen raw question SHA256 `36f56dcc11d6347a1db47adfb103b16472a8e1270641869f52c7220bd086a361`, packet SHA256 `6fe25bf6c738ee13fa837793414b343feeb53116737bcfafcf19c56c36adac5d`. In each OS ZIP, original frozen and retained question bytes, original receipt and original packet match the exact *tracked source* files, both hashes and native receipt bind correctly. The native report contains **five named status=ok measurements** and assessment **native_measurement_coverage=complete for those five only**; interpretation `not_verified` and independent physics/educational usefulness `not_evaluated` remain separate.
- Original public NASA NON-BLIND fixture: question SHA256 `cd797751a84d86caa57c2024620215895c1414169c6682b96933e4b4cf25cc23`; packet SHA256 `f86211065ec99e3e82181de256d321a6ebb054f9b397440996529a3ec6ccfeda`. Again exact frozen and retained bytes/receipts match source. Each original native report has one `exit_speed_native`, `status=ok`, `quantity=speed`, unit `m/s`, saved index 20; physical speed about **43,484.58452036887 m/s**, and assessment gives complete **native coverage only**, with the same separate unverified science labels.
- Original native report JSON bytes may vary across OS, and this audit **does not require cross-OS byte identity**. Per-OS report SHA256 in the original assessment was rehashed and matched that OS's actual native bytes: developer gravity Ubuntu `bf11cc7a6abd598bba0ae1746ca934eaf2ebc8c383aff79373676d5b4b06b947`, Windows `6638d653fdc757a8420d3c04f60c7a5a400ce3176ad88f3d3434afef8fb79145`; NASA Ubuntu `ab928b94cbb930d8589352a1ba180f81e4d7dda67997b57473bc35c05242ec20`, Windows `20854e0f07a98af4a6b3eba3b6318b73f9ee8672a4b36175d4239242a16ba038`.
- Original Physics Demonstration V1: one passing case, **64/64 analytic checks** in each OS archive; all **30** `src/emfeeld/*.py` file SHA256 receipts verified against exact reconstructed source. Original Windows line-ending conversion was explicitly accounted for (CRLF checkout versus canonical LF source).
- Both archives preserve signed ensemble **E1 complete** and **G1 partial** rather than fabricating zeros or promoting unavailable values.

## Original first audit-harness issue and nonclaims

On the **first local ZIP audit command**, a script incorrectly treated the engine receipt basename `__init__.py` as a repository-root path and raised an AssertionError. After correcting the **audit-only** lookup to `src/emfeeld/__init__.py`, all 30 source hashes independently verified; no project file, original ZIP or source identity was altered. The initial partial run is not reclassified as a full PASS.

**Source changes still require independent R2:** new shared evidence-output boundary, corrected field implementation, admissible numeric/camera/proposal behavior and historical pinned source compatibility all need reviewer-owned adversarial re-execution. These original archive checks establish author-side provenance and recorded outcomes—not semantic review of all new code, general physics correctness, an independently authored teaching question, human Windows desktop qualification or an authorized merge. Keep PR #40 DRAFT / UNMERGED until reviewed and accepted. After any guarded merge, requalify **new actual main-push** CI and source/native ZIPs separately.

Author audit script and resulting machine-readable report were preserved in the originating chat container, not misrepresented as already uploaded to GitHub.
