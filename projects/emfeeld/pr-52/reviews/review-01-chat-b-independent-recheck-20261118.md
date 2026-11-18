# Supplementary independent recheck — EMFEELD PR52

**Date:** 2026-11-18. **Verdict: CHANGES REQUESTED (two bounded renderer-neutral data-contract defects).** This supplements but **does not replace or overwrite** the preexisting `review-01-chat-b.md`. No merge or candidate edits.

**Pinned source:** draft PR52 `3ea61a4d79d211009fb0b038fa56b7cef1e1e38c`, tree `49afa15dbd3c1e9b15d0a41719eea7bdabd0540a`; base/main `6bfeb2c314841ef861d7d66b67c894a6295b705e`. Independently verified all 398 source blobs and reconstructed the old released tree `4da6b80f53d78b2394c8516b9463e442fffb50fe` by reversing exactly the five-path patch. PR53 excluded.

## R52-A: accepted finite nonzero fields export invalid direction glyph data

Strictly authored gravity uniform fields `(1e-200,0,0)` and `(1e200,0,0)` m/s² yield 343 finite, nonzero physical field samples each. The new `build_visualization` public data contract, however, drops all arrows at the small scale and exports 343 zero-length *unit directions* at the large scale (with an overflow warning). Physical vectors/potential remain correct. The numerical `np.linalg.norm` issue was inherited from the old viewer, but is now a false claim under the **new renderer-independent `FieldSamples` contract**. Require robust direction normalization or explicit unsupported-range refusal, without changing laws/tolerances. New independent reproducer: `reviewer_pr52_vector_norm_reproducer.py`.

## R52-B: inconsistent saved samples admitted by new public builder

A real `Trajectory` truncated coherently to 2 samples while the scene declares 5 is correctly refused by existing `validate_recorded` (`invalid recorded time_s`) yet accepted by `build_visualization(scene,recorded=...)`; the returned snapshot claims 5 frames, and calling legal `data.frame(4)` crashes with raw `IndexError`. This can break a second renderer. Validate at the standalone builder boundary or enforce an equivalent clear typed precondition. New independent reproducer: `reviewer_pr52_recorded_reproducer.py`.

## Independent positive results

- **Five** released-versus-candidate original PyVista 0.48.4 / VTK 9.6.2 software-EGL scenes, with **identical five initial screenshot byte hashes**, **nine identical moving-frame screenshots**, and identical real mesh numeric arrays after disregarding transient VTK actor-pointer names. Native slider EndInteractionEvents, Home/Left/Right/Space key callbacks, timer completion and playback-close behaviour exercised.
- **Three successive real `render_pyvista(snapshot)` calls** produced identical PNG SHA-256 `c2f915143e873b9c85ab4d37c3e8d84e2e2f7397f854ccb334f07a6f942d7c96`, with physics methods and trajectory integration deliberately disabled.
- Eight reviewer-authored headless challenge groups, including electric/gravity SI/units, source roles, x-fastest sampling, NaN/null, nested/unrecognized sources, a non-VTK JSON consumer, valid saved-frame identity, 17 nested export-mutation attempts and both above *defect* reproductions. **16** focused existing author tests and **three** existing real PyVista tests were separately rerun and passed (not new independent test designs).
- Independently downloaded original Ubuntu artifact `14446474306` and Windows `14448317667`; original ZIP SHA-256 verified, CRC/safe/unique 2,186 members per archive; 173 integrity manifests/1,750 references (1,749 correct, one intentionally corrupt refusal fixture), and 82×35 current-source module receipts each. Hosted exact-head reports: 1,833 headless + 18 historical/one deselected + 54 graphics per OS. These are audited *hosted* results, **not** reviewer full-suite or manual-Windows reruns.

## Gates and evidence

Keep PR52 draft; fix R52-A and R52-B; independently qualify the corrected head before owner-directed integration. Actual-main CI/archive audits are later gates. No Windows human-input, all-DPI, teacher or blind JEE claim. Initial reviewer-only harness misassumptions were preserved; no product-source edit or merge.

**Full reviewer-generated evidence:** owner-facing archive `EMFEELD_PR52_Independent_Recheck_Evidence.zip`, SHA-256 `38173dfa3fcbbc2fc9976dad96c29ca5786ab610a9214847d227212b68bb9956` (63 files: scripts, first-failure and successful logs, JSON receipts, original new screenshots for released/candidate/frame parity, original audit outcomes). The original source and OS archives are deliberately not repacked in this ZIP.
