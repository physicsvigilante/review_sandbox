# EMFEELD PR #63 — guarded merge and actual-main release audit

**Status at this checkpoint: MERGED, but actual-main technical release NOT YET CLOSED.**
Original independent review-01 [CHANGES REQUESTED](reviews/review-01-chat-b.md) remains historical. Separate [independent R2 scoped PASS](reviews/review-02-chat-b.md) qualified the corrected exact feature source with new reviewer-owned native PyVista evidence, not human teaching efficacy.

## Exact guarded integration

- Pull request: [emfeeld PR #63](https://github.com/physicsvigilante/emfeeld/pull/63), **MERGED**.
- Reviewed feature HEAD: `d3385fc5efa023c9519510ef84207c0741861a45`.
- Previous main: `52aecd34338662e269fba091c0ff6664e8e1eca7`.
- Actual main merge commit: **`cf884b6d91cb685993e07a1c65236b65d185e521`**.
- Merge parents (ordered): [previous main, independently reviewed feature HEAD].
- Actual merge Git tree: **`c15bd147bcd0618253d906b704b06d3d864829d2`**, exactly the independently reviewed HEAD tree, with all **461** Git tracked source files and modes unchanged between HEAD and merge.
- GitHub merge used `expected_head_sha=d3385fc...`, after validating live main still equalled qualified base, all 10/10 exact-head premerge workflows succeeded, and only nine new circular-loop paths were added. No existing electrostatics/gravity/Gauss/cavity/dipole/capacitor/wire source path was modified.

## Actual-main push qualification — seven workflows completed, full dual-OS pending

**Actual main GitHub push workflows (not PR synthetic-merge runs):**

| New main-run gate | Run | Latest verified gate |
| --- | --- | --- |
| Circular loop native 3D | [44701653246](https://github.com/physicsvigilante/emfeeld/actions/runs/44701653246) | SUCCESS |
| Straight wire 3D | [44701653263](https://github.com/physicsvigilante/emfeeld/actions/runs/44701653263) | SUCCESS |
| Gauss 3D | [44701653422](https://github.com/physicsvigilante/emfeeld/actions/runs/44701653422) | SUCCESS |
| Cavity 3D | [44701653264](https://github.com/physicsvigilante/emfeeld/actions/runs/44701653264) | SUCCESS |
| Dipole 3D | [44701653397](https://github.com/physicsvigilante/emfeeld/actions/runs/44701653397) | SUCCESS |
| Capacitor 3D | [44701653336](https://github.com/physicsvigilante/emfeeld/actions/runs/44701653336) | SUCCESS |
| General real PyVista | [44701653458](https://github.com/physicsvigilante/emfeeld/actions/runs/44701653458) | SUCCESS |
| Full clean-install Linux + Windows | [44701653299](https://github.com/physicsvigilante/emfeeld/actions/runs/44701653299) | **IN PROGRESS** |

Each original successful first seven workflow artifact was **downloaded from the actual push run**, its original whole ZIP SHA256 and ZIP CRC checked, the original `tested-source.tar` independently reconstructed into a 461-file Git tree, and the archived source identity reconciled to the **actual main commit** and independently reviewed tree. The seven ZIP archives all contain **the same exact original source TAR** SHA256 `a3cb866685ac7e1f7ed99e0bc831a21543b4c3a0e36b41f7204bbdc28618a52a`.

| Authentic original artifact / GitHub artifact ID | Original ZIP SHA256 | Audit outcome |
| --- | --- | --- |
| Circular loop **14612703454** | `4b398adeaef0a9e2efba882b1b2cb97970fe2205e7730187ac4005246cff981d` | 9 native PNG, 63/63 file hashes |
| Straight wire **14612414519** | `b315a539c3f741c06f9dcfd5b3cf1f40f9039992d8240122dcfea4e003b8cf16` | 7 native PNG, 49/49 hashes |
| Gauss **14613191824** | `88bc591f40f88e21d0bb8af586c10d91776d9b90cca343d696cc60557f3abe64` | 22 PNG, 148/148 hashes |
| Cavity **14613691074** | `0c7ae1232ef608e7c76bf3ba757baa208ef3bb54af6c0bb64b2eac3d63fa32f7` | 6 PNG, 36/36 hashes |
| Dipole **14613012578** | `3f4613a605798523608c8154824772c9b950a8a5a925c3e0d3516e15a4e396cd` | 14 PNG, 239/239 hashes |
| Capacitor **14613356623** | `16319c1a1e65f265301c872720ecb061838fbe819aa2c678c52bdcc59f4ad009` | 9 PNG, 63/63 hashes |
| General native viewer **14613691026** | `6a27c55023f373fd37bce50b378e02783b0126f4b8f2b4593c610ff1f56805c9` | 17 nonblank original PNG, 461-file source tree; no per-scene integrity manifests in this artifact |

Together these first seven original main artifacts contain **84 original PNGs and 598 per-scene SHA256 hash references, all valid**, plus seven CRC-clean source-bound original ZIPs. PNG existence, dimensions and nonblank pixel variance were machine checked; that does not constitute a separate human Windows desktop trial.

## Outstanding final release gate

**Do not assert release completion before full dual-OS workflow is SUCCESS on both distinct jobs and BOTH newly generated actual-main original clean-install ZIP archives pass whole ZIP/CRC/test/source/reference audits.** No historical premerge archive substitutes for current main evidence. After those checks, update this report with authentic artifact IDs/hashes, job test counts and corruption-negative result. Close [Issue #62](https://github.com/physicsvigilante/emfeeld/issues/62) only for **technical qualification**, preserving learner/teacher acceptance as unmeasured.

Scientific limitations remain: single ideal circular steady-current filament in vacuum, exact magnetic field **along its axis only**; no general off-axis Biot–Savart solver, magnetic materials, time-varying fields, induction or force, and arrows/thickness are schematic. Original independent review-02 is scoped technical acceptance, not proof of JEE classroom utility.

## Actual-main Linux clean-install completed and audited

The full push workflow [44701653299](https://github.com/physicsvigilante/emfeeld/actions/runs/44701653299) has **Linux SUCCESS** on actual `main` commit `cf884b6d91cb685993e07a1c65236b65d185e521`; its original logs record **2,200 headless tests and 107 genuine real-PyVista tests PASSED** (warnings as errors). Original Linux artifact **14613742891** was downloaded independently and audited: original ZIP SHA256 **`bab64763afcee3bf522f1cb373e7342166d32249f881412354ccc0ea510da08c`**; 2,186 unique ZIP files, CRC clean, exact `head-sha.txt` on the real production commit, 173 JSON integrity manifests, 1,749 authentic file-hash references matching, zero missing references and **one correctly detected deliberate corruption-negative reference** at `derived-001/G1/review-challenge-resealed-native/native/result.json`. No unexpected mismatches.

**Windows remains IN PROGRESS** on actual-main real-PyVista regression at this interim checkpoint. No complete dual-OS technical release claim yet. Recheck original Windows artifact separately before closing Issue #62.
