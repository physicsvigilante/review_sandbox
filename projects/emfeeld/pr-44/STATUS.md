# PR #44 — JEE 3D conductor cavity status

## CURRENT — independent review-01 INSUFFICIENT EVIDENCE; offline PyVista continuation ready

**18 November 2026: DRAFT / UNMERGED.** Exact candidate remains **`e253d0acf15e7505f1da8ab95cb519b59b0d720b`**, tree **`8a4a14d70ba824e8a338add08356003e79a248bc`**, main/base **`60b6e751363d0b922a02c3a259110547b79cf25c`**. No candidate or main source change was made after the review.

[Chat B original independent review-01](reviews/review-01-chat-b.md) reports **42 reviewer-owned physics/state cases passed** and **15 independently reconstructed native-VTK glyph cases passed**, original theory/source/archive inspections, and no demonstrated physics or source-preservation defect in the tested cases. Its source-authored 67 focused passes are separate; its full-headless rerun timed out and is not a pass. **R2-B01 remains blocking:** no real PyVista in the reviewer environment, so the actual production controller/widgets/keyboard/live snapshot path was not independently executed. The original verdict remains INSUFFICIENT EVIDENCE, not PASS; the author's prior CI cannot close it.

[Author response](responses/response-01-chat-a.md) accepts that evidence gap. A separate unmerged support branch provisions five original pure-Python wheels, not new product code or a reviewer verdict. Original provisioning workflow **44256323755 SUCCESS**, runtime artifact **14406007331**, SHA256 **`2f51d4a7aa4ef2a5d722627a6b3707c6e8efaef3bc486ab47675574df3d01295`**. The author independently checked the ZIP and all wheel hashes, installed them offline into an isolated container target, imported actual PyVista0.48.4/VTK9.6.2, opened the production lesson, exercised an actual slider event and saved a fresh state/PNG. A separate full four-test local attempt timed out and is preserved as incomplete. This is only AUTHOR runtime availability proof, not independent review or a general graphics qualification.

**Next:** same independent Chat B context follows [targeted R2-B01 continuation prompt-02](REVIEWER-PROMPT-02.md), using [verified offline runtime/commands](REVIEW-RUNTIME-01.md), then appends `reviews/review-02-chat-b.md` with its own exact-source verdict and retained actual PyVista graphics outputs. No need to redo the whole previously reviewed implementation just because a dependency was unavailable. **DO NOT MERGE** until a supported independent PASS and source/integration checks. Actual-main release audits and human Windows/JEE teaching acceptance remain separate.

---

## Historical author-qualified checkpoint (superseded by CURRENT above)

**18 November 2026: AUTHOR QUALIFIED, INDEPENDENT R2 PENDING. DRAFT / UNMERGED.**

Exact candidate `e253d0acf15e7505f1da8ab95cb519b59b0d720b`; Git tree `8a4a14d70ba824e8a338add08356003e79a248bc`; main/base `60b6e751363d0b922a02c3a259110547b79cf25c`; source-equivalent preview `04f8926ff15697ecccd9d89f71e837f2eb45bf56`. Nine new files, no changed/deleted baseline paths;382 tracked files and32 package modules.

Implemented: separate bounded analytical cavity/metal/exterior model, true3D density surfaces and display-only cutaway, correctly directed bounded curve/arrow graphics, position/grounding/sign/Q controls, actual current-state snapshots and shared evidence-output protection. One held point charge, concentric spherical conductor, no exterior sources. No PDE or numerical redistribution solver. Existing core physics and trajectory semantics remain unchanged.

The actual uploaded theory PDF was inspected. Printed1.115 and1.117Q5/Q7 motivate the lesson; default thick-shell configuration is explicitly an illustrative adaptation of the off-centre **thin-shell** question, not an exact source reproduction. Spherical image/density formulas are separately derived machinery. No whole-book or independent teacher success is claimed.

**Exact-head all four workflows SUCCESS:** release44245981602 (Ubuntu/Windows each1709 headless+18 historical/one obsolete guard deselected+37realPyVista); source44245981717; existing viewer44245981615 (9scenes/17PNG receipts); new lesson44245981629 (71focused tests,6actual scene PNGs). All **five original ZIPs downloaded and author-audited**, exact382-file source tree and all snapshots/source maps verified. Current lesson PNGs inspected by author; actual controls visible and consistent, arrow glyphs stay outside metal. This is not human Windows or teacher acceptance.

Original first failures were preserved: underresolved quadrature, initialization position drift, camera-test conversion, invisible/stale/clipped controls, a layout-harness coordinate mismatch and arrowheads entering metal despite valid curve paths. Fixes did not change baseline physics, old evidence or thresholds to fabricate success. [Full author report](AUTHOR-QUALIFICATION-01.md).

**Next and only outstanding pre-merge gate:** [separate Chat B R2 instructions](REVIEWER-PROMPT-01.md) and [full request](REQUEST.md). Reviewer must independently execute fresh cases and publish `reviews/review-01-chat-b.md`. No independent verdict exists yet. **Do not merge.** A future guarded integration also requires fresh actual-main workflows and new original archive audits. Old source-pinned studies remain immutable; new modules can change implementation receipts.
