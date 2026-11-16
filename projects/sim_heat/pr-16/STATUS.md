# SIM_HEAT H2-03S PR #16 — central R2 review status

**Status: `merged` — owner-approved 2026-11-16 IST.** Chat B's original [Review 01](reviews/review-01-chat-b.md) found F-01 major, F-02 minor and F-03 trust-boundary question at original source SHA; it remains immutable with `changes-requested`. Chat A corrected the three-file scope, obtained passing exact-new-head CI and documented its [response](responses/response-01-chat-a.md). Chat B independently authored [Review 02](reviews/review-02-chat-b.md), Git blob `ed33aeec36c8e1b1f627f59c3a69e7637bce899d`, **scoped R2 `pass`** on the unchanged corrected SHA `099bd4330a56e129f35493b42231830209a9e964`. **The owner explicitly approved the merge; GitHub merged PR #16 via merge commit `a6f0881236201e3ad7b9dd27d8fd0974c7972f56` on 2026-11-16 09:23:17 UTC. The source PR is closed and merged; `main` matches this commit exactly. Post-merge workflows are being verified independently and are not yet represented as successful in this record.**

| Field | Exact value / current status |
| --- | --- |
| Project | `sim_heat` |
| Source PR | https://github.com/physicsvigilante/sim_heat/pull/16 — **closed and merged** |
| Base commit | `c977773578b04a571dfefebe615350b9ed1dcf3e` (main after PR #14) |
| Original independently reviewed HEAD | `e76df818fcbb9b6826b03db776b6140dd40c4be4` — Chat B Review 01 `changes-requested` |
| **Current corrected HEAD** | **`099bd4330a56e129f35493b42231830209a9e964`** |
| Original reviewed tree | `7bf42b21ce11a27083a23cfe7eb85fae86ab6df9` |
| **Current source tree** | **`85a62320977092f47cf5d100bf98c4b2bf955599`** |
| Review class | **R2**, mode-specific native-evidence interpretation and user-visible quantity meaning |
| Original author CI | [43826695620](https://github.com/physicsvigilante/sim_heat/actions/runs/43826695620) — SUCCESS on first reviewed head; original Review 01 still found F-01 |
| **Final correction author CI** | [43834101967](https://github.com/physicsvigilante/sim_heat/actions/runs/43834101967) — **SUCCESS** on exact corrected head |
| Correction CI tests | **151 H1, 4 analytical, 11 Python adapter, 14 Node**, all passed; real Chromium desktop/mobile **PASS** with no changes to existing original evidence UI |
| Final correction CI artifact | [14210406363](https://github.com/physicsvigilante/sim_heat/actions/runs/43834101967/artifacts/14210406363), ZIP SHA-256 **`015ee3b1874996df29e70f2ec2aefa33902704b271fe60e3d11b183c9159a92d`**, 3,544,109 bytes; independently downloaded and ZIP SHA/CRC/head marker/logs checked |
| Exact-correction-head source snapshot | [14210401348](https://github.com/physicsvigilante/sim_heat/actions/runs/43834101967/artifacts/14210401348), ZIP SHA-256 **`d7a0b09fcdbb1a25649cf1b0e0f7b30bccbe8a862056c1e9cd5b6f424e1c0220`**, CRC verified; original valid S1 + eight adversarial repacked ZIPs executed against this exact snapshot |
| Source-selected S1 model/study | Unmodified `h1/cases/S1/{model.mo,study.json}`; original SHA-256 pins in [REQUEST.md](REQUEST.md) |
| Actual new S1 native run | [43820600508](https://github.com/physicsvigilante/sim_heat/actions/runs/43820600508) — **success**, executed SHA `337ef554fb40da9408485bda8f2a4024c84720f6`, 1 build, 1 launch, 1 explicit version query |
| Native diagnostic results | 56/56 checks, maximum allowance ratio 0.03125; `diagnostic_checks_passed_not_native_qualified` / `nativeQualified=false` |
| Native artifact | [14204656273](https://github.com/physicsvigilante/sim_heat/actions/runs/43820600508/artifacts/14204656273), ZIP SHA-256 `82b4a87b66e0022d582da931253649b3829f6633119a57081c02dc253dc5dbd9`, 235,746 bytes; verified 89/89 archived file hashes and CRC |
| Authentic native values | Algebraic eval index 1 (not time): junction `366.4562880324543 K`, rod `+1.0792824946508015 W`; no native body storage |
| Derived steady case JSON | `viewer/network/data/S1.json`, SHA-256 `eacab37b499a47c094cbd642acfee269a1bea7c82d16b15b9217a8c13ef1e4e7` from exact-byte offline original-archive replay |
| New native builds from viewer CI | **0** — saved S1 native work is on separate experiment workflow |
| Reviewer Review 01 | [reviews/review-01-chat-b.md](reviews/review-01-chat-b.md) — **`changes-requested`** at first source HEAD; remains unchanged |
| **Targeted Review 02** | **SCOPED `pass`** — [reviews/review-02-chat-b.md](reviews/review-02-chat-b.md) independently authored at exact corrected source HEAD; Git blob `ed33aeec36c8e1b1f627f59c3a69e7637bce899d` |
| Owner merge approval | **Granted explicitly by owner 2026-11-16 IST** |
| Merge commit | [`a6f0881236201e3ad7b9dd27d8fd0974c7972f56`](https://github.com/physicsvigilante/sim_heat/commit/a6f0881236201e3ad7b9dd27d8fd0974c7972f56); GitHub merged=true, state=closed |
| Post-merge main identity | **Verified**: `main` identical to merge SHA; zero ahead/behind |
| Post-merge CI | **Pending verification**, three `main` push runs: [43839286206](https://github.com/physicsvigilante/sim_heat/actions/runs/43839286206), [43839286437](https://github.com/physicsvigilante/sim_heat/actions/runs/43839286437), [43839286528](https://github.com/physicsvigilante/sim_heat/actions/runs/43839286528) |
| Post-merge CI | Not applicable; source PR is draft/unmerged |

## Source and previous evidence preservation

- Original [H1 S1 MATv4 workflow 43689753800](https://github.com/physicsvigilante/sim_heat/actions/runs/43689753800) **FAILED** and was later reanalysed post-hoc without backdating its run outcome.
- First H2-03S one-shot [43757179599](https://github.com/physicsvigilante/sim_heat/actions/runs/43757179599) **FAILED in preflight** due a mistyped developer pin, no native builds/launches. Later owner-approved fresh successor [43820600508](https://github.com/physicsvigilante/sim_heat/actions/runs/43820600508) is separately successful.
- Earlier viewer CI [43825373851](https://github.com/physicsvigilante/sim_heat/actions/runs/43825373851) failed legacy transient returned-object compatibility; [43825490516](https://github.com/physicsvigilante/sim_heat/actions/runs/43825490516) failed steady SVG hiding; [43826111440](https://github.com/physicsvigilante/sim_heat/actions/runs/43826111440) and [43826333500](https://github.com/physicsvigilante/sim_heat/actions/runs/43826333500) failed mobile width. All are retained as failed. Intervening cancelled runs are also preserved; they are not counted as passing.
- Original reviewed candidate [43826695620](https://github.com/physicsvigilante/sim_heat/actions/runs/43826695620) passed its source-specific suite, but independent Review 01 demonstrated an archive-admission defect at that SHA.
- First correction CI [43833850755](https://github.com/physicsvigilante/sim_heat/actions/runs/43833850755) **FAILED** at old adapter tests after mandatory external run/commit parameters were added, before tests were updated. This is preserved as failed. Final correction [43834101967](https://github.com/physicsvigilante/sim_heat/actions/runs/43834101967) **PASS** 151+4+11+14 and real Chromium on the corrected head. Original native S1 and all three transient case bundle bytes remain unchanged.
- Original PR #14's Review 01 findings and Review 02 scoped PASS remain their own immutable historical files. PR #16 is a **new** R2 evidence contract, not a replay of PR #14's verdict.
- **Independent PR #16 Review 02 completed:** Chat B independently downloaded three SHA-pinned ZIPs, replayed the original genuine S1 archive and H1 receipt, and performed **38 adversarial repinned-ZIP probes**: 36 correctly typed refusals and two intentional admissions showing documented external trust/non-attempt-directory scope limits. F-01 and F-02 resolved; F-03 is a mandatory externally checked run/commit assertion rather than an adapter-side GitHub attestation. Reviewer concluded **scoped R2 PASS, no additional code change required**. A future nonblocking documentation refinement may explicitly say the complete member manifest covers the **native attempt subtree**, not unrelated outer CI-evidence files.

## Final review and merge disposition

- [Review 01](reviews/review-01-chat-b.md): immutable original `changes-requested` at `e76df818fcbb9b6826b03db776b6140dd40c4be4`. F-01/F-02/F-03 original source findings remain documented; do not relabel.
- [Response 01](responses/response-01-chat-a.md) and [FOLLOW-UP-02.md](FOLLOW-UP-02.md): scoped correction and pinned CI evidence.
- [Review 02](reviews/review-02-chat-b.md): independently authored **scoped R2 PASS** at unchanged corrected SHA `099bd4330a56e129f35493b42231830209a9e964`. 36 adversarial refusals and two explicit trust-boundary tests, original native S1 archive and numerical-checker replay independently examined. No further code correction or repeated broad R2 review required for this source.
- Owner explicitly approved the merge. GitHub changed draft PR #16 to ready, then successfully merged the **identical reviewed source head** with expected-head guard, preserving the PR review history. Merge SHA `a6f0881236201e3ad7b9dd27d8fd0974c7972f56`; GitHub reports `merged=true`, source PR `closed`, merge timestamp 2026-11-16 09:23:17 UTC. `main` equals merge SHA, ahead=0 behind=0.
- Three `main` post-merge workflows were triggered at the merge SHA; verify their **final** conclusions before claiming post-merge CI success. Exact-head source CI [43834101967](https://github.com/physicsvigilante/sim_heat/actions/runs/43834101967) was SUCCESS before merge (151 H1, 4 analytical, 11 Python adapter, 14 Node, real Chromium desktop/mobile).
- The one-shot S1 OpenModelica evidence workflow and its source branch were **not** merged as a production trigger. The original native output remains `diagnostic_only`, `nativeQualified=false`; no independently measured sensor data, full H1 qualification, R3 reference accuracy certification, unfamiliar-author C1 transfer, symbolic/inverse solver or classroom trial is claimed.

**Next:** Check the three post-merge workflows on `main` and update this record with their exact conclusions. This post-merge evidence task is not another code-review or merger approval gate.
