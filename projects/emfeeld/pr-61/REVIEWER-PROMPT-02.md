# EMFEELD PR #61 — narrow independent follow-up to review-01 (new conversation works)

**You are an independent reviewer; do not modify production source or merge.** First review [review-01](reviews/review-01-chat-b.md) issued **CHANGES REQUESTED**, not a PASS. Preserve that immutable finding, and read the [author response](responses/response-01-chat-a.md). The corrected code and native evidence are in the attached self-contained `PR61_Wire_R2_Review_Kit.zip`.

## Exact source and gate

- Initial reviewed head `d7151a35ecddace3f79786315fb4f07858e398cc`, tree `9886308b8a036eb65ca8e37dc86ef173c6e91e12`.
- **New exact target HEAD `76edda620213710e80860c3ee8abe312228b6c10`**, Git tree **`047eca847cfc6bacfc3afebd51cf912a2f9deb18`**. This is one six-file correction commit on the previous reviewed head. Original qualified main `d2f90afbf6c8910c410c41147925e311320f96b0`, tree `95f6f0b09cb24daaa0c9b1dd064fc68e3d09dced` stays unchanged.
- PR https://github.com/physicsvigilante/emfeeld/pull/61 remains **DRAFT, UNMERGED**. New corrected synthetic test merge, if any, is **not** actual main.
- Corrected **452 tracked Git files**, verified original hosted source ZIP **14575915283** (SHA256 `5e7c23c341891e33e6ad28157a722b79b64af9c2bfe74c0d704f7c6c96ee7f09`), source TAR SHA256 `5c3d55e810946aa22ce97ec779cc053d4b409702deecc28ec118614dd1ebe7ce`; ZIP CRC and all blobs/modes were checked against exact target tree and source used in local tests.
- New dedicated original hosted wire ZIP **14574399195** (SHA256 `fe8f58380aff5928678c1acffa34df38db44cc26cb0d9013095f3ed5419259d1`), seven **actual** PyVista state captures, 49 SHA receipts, saved real SI B, tangents, loop weights and original/current inputs. Author audit confirms exact source and physical outputs; these are **not your independent tests**.

## Review ONLY the two findings and impacted native presentation

**F1 required: fixed BLUE positive circulation direction.** Original blue Ampère circle had no arrowhead, misleadingly labelling a loop as oriented. Corrected renderer draws a **blue tangent arrow** from immutable `WirePresentation.tangent_unit`, independent of magnetic field, signed current or display B glyphs. Examine `src/emfeeld/wire_view.py` and actual native actor `positive_ampere_circulation_arrow`. Verify its geometry and direction equal positive tangent orientation **for positive, negative, and zero I**, including a tilted wire; green B arrows should reverse with I and disappear at zero, while the blue arrow remains clearly visible and labelled. The sampled signed circulation must still arise from **SI `B · tangent · arc_weights`**, not marker geometry. In independent author-created code, verify sign convention `e1 × e2 = u` and inspect at least one **new reviewer-owned** negative/zero screenshot (not the seven author-hosted ones). Verify saved source/current/field samples and screenshot hashes. Keep no-physics-on-camera/reveal behaviour.

**F2 advisory: Boolean pre-coercion at direct Python probe API.** In `wire_magnetism.magnetic_field`, check `[True, 0, 0]`, `[1.0, False, 0.0]`, nested batches, NumPy bool/object-array values, and both zero/nonzero current. These must refuse before NumPy numeric upcast; equivalent genuine int/float probe coordinates must still work. An integer ndarray already manufactured from Boolean input cannot be detected retroactively; do not demand that impossible guarantee. This must not weaken the already independently accepted authored JSON or singular-axis refusals.

**Scope limits:** no need to repeat the previous reviewer-owned 360 held-out axis/current cases, unchanged Coulomb/gravity/Gauss/capacitor/dipole/cavity studies, or whole engine approval. The 3D wire uses one ideal infinitely thin infinite static wire; finite drawn length is schematic; no new Lorentz, induction, circuit or general Biot–Savart solver. No unobserved human classroom or Windows UI certification.

## Native runtime if your review container lacks PyVista

The kit includes original offline PyVista 0.48.4/cyclopts/docstring-parser/rich-rst/scooby pure-Python wheels. Extract wheels and install to a *disposable target* with `pip install --no-index --no-deps --find-links WHEEL_DIR --target OVERLAY pyvista==0.48.4 cyclopts==5.5.2 docstring-parser==0.18.0 rich-rst==2.2.0 scooby==0.12.1`; set `PYTHONPATH=OVERLAY:EXTRACTED_SOURCE/src`. Native **VTK 9.6.2 must be present separately** (wheels do NOT contain VTK). Use EGL/software OpenGL if headless. If real PyVista execution is unavailable, mark the native part **INSUFFICIENT EVIDENCE**, not PASS.

## Evidence status and deliverable

Builder-owned corrected-head local **108 focused PASS** with warnings as errors, genuine local six-scene PyVista qualification PASS; **local full suite timed out after ~33% and is NOT a pass**. New hosted wire workflow **44616482262 SUCCESS** with 108 tests and seven state captures; source **44616482180 SUCCESS**. Other exact-head workflows are being checked; verify **all nine** exact corrected-source workflows and separately both Linux/Windows jobs of release run **44616482245** before claiming premerge CI green. Previous original-head CI applies only to the old reviewed source.

Publish **`projects/emfeeld/pr-61/reviews/review-02-chat-b.md`** with immutable corrected SHA/tree, your **own new challenge/test scripts and fresh real native image provenance**, F1/F2 dispositions, first failed attempts and a scoped verdict: PASS / CHANGES REQUESTED / INSUFFICIENT EVIDENCE. Never edit review-01 or developer receipts. Keep production PR unmerged; a later guarded merge and actual-main CI are separate steps.
