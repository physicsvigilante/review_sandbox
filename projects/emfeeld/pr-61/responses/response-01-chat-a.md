# EMFEELD PR #61 — author response to independent review-01 (20 November 2026)

**Historical reviewer verdict remains [CHANGES REQUESTED](../reviews/review-01-chat-b.md).** No earlier review record has been edited, and this author response is not an independent PASS.

## Exact bounded correction

- Initial reviewed feature HEAD `d7151a35ecddace3f79786315fb4f07858e398cc`, tree `9886308b8a036eb65ca8e37dc86ef173c6e91e12`.
- New corrected feature HEAD **`76edda620213710e80860c3ee8abe312228b6c10`**, tree **`047eca847cfc6bacfc3afebd51cf912a2f9deb18`**, parent exactly old reviewed head.
- Main stays `d2f90afbf6c8910c410c41147925e311320f96b0`, tree `95f6f0b09cb24daaa0c9b1dd064fc68e3d09dced`. PR #61 remains DRAFT and UNMERGED. Six narrow paths changed; no existing 441-file physics/other-lesson baseline changed.

### F1 BLOCKER — corrected positive Ampère loop orientation

In `src/emfeeld/wire_view.py` the blue Ampère loop now has a clearly visible **blue positive-traversal arrow** and legend. The arrow is geometrically derived from the **existing immutable renderer-neutral physical `tangent_unit` samples**, not magnetic-field arrows or current sign. A short blue 3D arrow is centred on a polygon segment; its schematic length is not used for the physical integral. It persists in the same positive direction at positive, negative and **zero** current, even when the green B arrows reverse or vanish. The actual sampled SI vector field, physical tangents, loop weights, numeric circulation and exact `mu_0 I` are **unchanged**.

Snapshot `display` now exposes positive loop arrow position/direction as presentation metadata. The existing wire qualification tool checks invariant blue geometry across four current/radius cases and produces native source-bound reversed/zero screenshots. New independent-of-field genuine PyVista test `test_native_positive_ampere_arrow_persists_through_negative_and_zero` changes current with VTK key events, compares the real named blue arrow PolyData/actor colour and tangent alignment, confirms green B signed/zero behaviour, and saves three fresh current-state PNG+integrity receipts.

### F2 advisory — hardened direct Python probe admission

`src/emfeeld/wire_magnetism.py` now checks original Python list, tuple, NumPy boolean and object-array entries for raw booleans **before NumPy can coerce a mixed vector**. A mixed `[True, 0, 0]` now raises `ValueError` for both zero and nonzero current. Numeric coordinate vectors remain valid. This does not pretend it can reconstruct a Boolean that was *already coerced* to an integer by an external array constructor. Authored JSON Boolean refusal was already correct.

New focused tests cover ten mixed signed/zero-current probe refusals plus ordinary numeric arrays. This is a bounded direct-Python API correction, not a new magnetic solver.

## Author and hosted qualification (NOT independent reviewer execution)

- Author-owned **108 focused headless+genuine PyVista tests PASS**, with warnings as errors; genuine six-scene local native qualification **PASS**. The larger local full-suite execution was **interrupted by the local 130-second execution limit at ~33%**, not a completed full pass; leave the earlier whole-suite result on the original head separate.
- Corrected locally reconstructed **452-file Git tree** matches `047eca847cfc6bacfc3afebd51cf912a2f9deb18`.
- Fresh GitHub source workflow **44616482180** SUCCESS, original ZIP artifact **14575915283** SHA256 `5e7c23c341891e33e6ad28157a722b79b64af9c2bfe74c0d704f7c6c96ee7f09`; original source TAR SHA256 `5c3d55e810946aa22ce97ec779cc053d4b409702deecc28ec118614dd1ebe7ce`. Git tree reconstructed from all 452 original source files exactly; byte-for-byte equal to the local candidate.
- Fresh dedicated wire workflow **44616482262** SUCCESS, original wire artifact **14574399195** SHA256 `fe8f58380aff5928678c1acffa34df38db44cc26cb0d9013095f3ed5419259d1`. Hosted tests **108 PASS**; seven actual PyVista scenes have 49 valid file SHA256 receipts. Verified current state and source SHA, physical SI `B` samples against unchanged evaluator, signed Ampère reports and blue positive tangent in all seven states. Original reversed and zero images show a fixed blue arrow, with green B arrows reversed or absent.
- Other corrected-head full Linux/Windows and historical-lesson workflows must be checked independently for final status; author CI success is not a reviewer-owned native test or classroom acceptance.

## Scoped next review

Follow [REVIEWER-PROMPT-02.md](../REVIEWER-PROMPT-02.md). Review **only F1, F2 and directly affected native 3D correspondence** on corrected HEAD; personally execute a fresh PyVista negative/zero view or state explicitly if unavailable, and check actual blue actor geometry/label, field sign and physical integral. Preserve original review-01. Publish `reviews/review-02-chat-b.md` with a supported scoped verdict. **Do not merge before independent PASS, final exact-source CI, and guarded actual-main qualification.**
