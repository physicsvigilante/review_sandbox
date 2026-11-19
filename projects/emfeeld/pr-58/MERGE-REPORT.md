# EMFEELD PR #58 — actual-main release report (2026-11-19)

**TECHNICAL RELEASE COMPLETE.** [PR #58](https://github.com/physicsvigilante/emfeeld/pull/58) merged as production commit **`d2f90afbf6c8910c410c41147925e311320f96b0`**, canonical Git tree **`95f6f0b09cb24daaa0c9b1dd064fc68e3d09dced`**, **exactly equal** to independently accepted corrected head **`635c4985cf45c634ccc8b481e71c4ae65f4d7043`**. Ordered merge parents: qualified main `51eee59836aac801c989e31712960571ceb94f39` and reviewed head `635c4985cf45c634ccc8b481e71c4ae65f4d7043`. All 441 tracked files reconstructed byte/mode-exact from actual-main original hosted source TARs.

The historical [independent review-01 CHANGES REQUESTED](reviews/review-01-chat-b.md) remains intact: nonrepresentable nonzero Q/V underflow (F1), dielectric slider κ model/UI mismatch (F2), missing independent native replay (A1). These were corrected in the exact reviewed source; [independent review-02 scoped PASS](reviews/review-02-chat-b.md) executed 73 fresh reviewer-owned checks/groups including genuine PyVista 0.48.4 / VTK 9.6.2 mouse, native slider `EndInteractionEvent`, keyboard, negative/zero polarity, κ9/10, refusal/recovery, changed-state PNG/source/sample receipts, and separate numerical admission tests. No previous failure was relabeled a pass.

## All SIX actual-main workflow gates SUCCESS

- [Capacitor 3D 44577098072](https://github.com/physicsvigilante/emfeeld/actions/runs/44577098072): 96 overlapping focused physics+native tests PASS, nine genuine saved PyVista scene states.
- [Conductor cavity 44577097861](https://github.com/physicsvigilante/emfeeld/actions/runs/44577097861) SUCCESS.
- [Gauss law 44577097801](https://github.com/physicsvigilante/emfeeld/actions/runs/44577097801) SUCCESS.
- [Dipole 44577098056](https://github.com/physicsvigilante/emfeeld/actions/runs/44577098056) SUCCESS.
- [General PyVista 44577097760](https://github.com/physicsvigilante/emfeeld/actions/runs/44577097760) SUCCESS.
- [Clean-install Linux/Windows 44577097749](https://github.com/physicsvigilante/emfeeld/actions/runs/44577097749): **BOTH OS SUCCESS**, original retained logs per OS: **2,074 headless** and **89 real-PyVista** tests passed, separate overlapping test suites.

## Original actual-main ZIP audit

Downloaded full GitHub archives and independently checked whole-ZIP SHA256 against GitHub digest, unique safe member names, ZIP CRC, all original per-file digest manifests, and source Git tree derived from all 441 TAR entries including modes.

| Original artifact | Whole ZIP SHA256 | Source/manifest check |
|---|---|---|
| Capacitor 14557287188 | `d09df0ed01a1b6da0d55c5af676c2476a3492b9e25d6e62c2bce108c549cb9f9` | 9 scene states, **63/63** file hashes |
| Gauss 14556658105 | `b50070486a16780707cb001a21aa80fe157b05e86a8f7e16592f3c3b5a3130a6` | **148/148** hashes |
| Dipole 14558010812 | `0e3b43451bda55a38116fcc240036e04e476cab45439dddde6d09eee9c0ac07b` | **239/239** hashes |
| Cavity 14556302991 | `f7cf4fbc693cec171a00fac9582469ff887c6b33a0fef0e7b1450255dc3b409f` | **36/36** hashes |
| General viewer 14558690260 | `1f4eaa789f2fd2a82d2c58727e42223f5593cf4f450bb9e0cc884be9d20122bc` | source exact, PNGs retained |
| Linux RC 14556698799 | `1e7c93233b22205ed1a9dc5501af4716694c86e80a14b1c3cec260ed8a821023` | **2186 unique files, 1749/1750** references |
| Windows RC 14559385755 | `550f3965fb2778caaf523ed2c0c8c1b06ae07ba9f5b37897c44255b0ceb1660f` | **2186 unique files, 1749/1750** references |

The *one* mismatched checksum reference on each OS is the **deliberately corrupted negative-test specimen** `derived-001/G1/review-challenge-resealed-native/native/result.json`, retained and not presented as a positive. Neither run has an unexplained mismatch. All five graphics archives contain the *same original source TAR bytes*, SHA256 **`1cd0b4ddcd22fd1703d91949a1413c2e05e2bad8ab79fd9d7988648066b2efd9`**, whose Git object identities produce the exact reviewed tree **`95f6f0b0...`**. The Linux/Windows archives contain actual merged `head-sha.txt` `d2f90af...`. The premerge synthetic CI merge is NOT substituted for actual-main success.

## Scope and future acceptance

The newly released interactive PyVista lesson is for **ideal homogeneous full-gap dielectric parallel-plate capacitors**, exact school-level `C=ε₀κA/d`, isolated signed free charge or ideal battery voltage, corresponding E, V, polarization/bound-charge, and stored *field energy*. Finite-looking plates and an exaggerated drawing gap are schematic; no finite-plate fringe field, partial dielectric insertion, capacitor network, battery-work/force dynamics, conductor PDE solver, or browser-based capacitor solver was introduced. Exactly 13 added capacitor-related files; 428 previous files unchanged.

**Not certified:** independent human Windows mouse usability or teacher/student instructional effectiveness, exact reproduction of an original examination answer, physical unsolved edge effects. Technical integration Issue #57 may close; the **genuine predict-then-reveal JEE usability trial [Issue #59](https://github.com/physicsvigilante/emfeeld/issues/59)** stays open. The hands-on demo is in [docs/CAPACITOR_V1_TRY_IT.md](https://github.com/physicsvigilante/emfeeld/blob/main/docs/CAPACITOR_V1_TRY_IT.md). No new physics development is necessary to perform that pilot.
