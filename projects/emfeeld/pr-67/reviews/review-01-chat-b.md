# EMFEELD PR #67 — independent review 01 (Chat B)

**Verdict: CHANGES REQUESTED (scoped).** Date: 20 November 2026. Independent source, physical/numeric, archive and genuine reviewer-owned native-PyVista review. The single required change is a strict underflow/angle representability correction; no broad architecture reopening is recommended.

## Exact reviewed identity and scope

- Live draft, unmerged [PR #67](https://github.com/physicsvigilante/emfeeld/pull/67), checked both before and after the review; head **6abc5fa30fe96103b9a60e9946c188609fe88197**, base **135e7a6ed86f5130d165debae2921111bc73fc3e**.
- Head Git tree **434af3657105b009f63e73b42f415b571ab6af16**. GitHub compare confirms **exactly ten added files and zero modified/deleted existing files**.
- GitHub synthetic test merge **71a86662ceb57db73139a14f943d11ccdfdaf5b3** has the same tree, parents ordered [base, feature head]; **not actual merged production main**.
- Scope: one rigid perfectly thin one-turn rectangular current filament in a *prescribed uniform static external B*, with signed I/B, exact SI forces/moment/torque/orientation potential and a schematic native 3D adapter. No induction, dynamics, self-field, materials, multi-turns or learner-efficacy claim.

## Independent source and scientific execution

1. Downloaded the **original dedicated** artifact 14621763327 and original snapshot TAR, not a copied author screenshot or locally regenerated equivalent. Its source TAR SHA-256 **ed0c641ab48702f7e054e3b4aa23aff96f39b97f46d7775a0008ec3c7858611b**. Independently extracted and staged all **475** source files: git write-tree returned **434af3657105b009f63e73b42f415b571ab6af16**. Independently compared **475/475** source ledger paths, blob hashes and modes in the source-snapshot archive to the rebuilt Git tree.
2. Reran **100/100** dedicated headless analytic/presentation tests from exact source locally; also reran the **entire headless tests directory: 2,300/2,300 PASS** with warnings-as-errors in Python 3.13.5. Separately exercised **2,000 reviewer-generated valid configurations** across widths/heights, signed current/field, arbitrary B axes, centre translations and tilts away from singular endpoints. SI torque/energy and segment-couple relations passed to numerical tolerance (worst observed relative torque error 1.3e-14, force-couple relative error 2.9e-14).
3. Reviewer-authored sign reference with positive B along +z, translated centre (11,-17,8) m, width .45 m, height .35 m, current +4 A, B +.3 T, theta=60 degrees: segment forces in N **[(+.54,0,0), (0,+.21,0), (-.54,0,0), (0,-.21,0)]**, signed torque **(0,-.1636788013152589,0) N m**, orientation potential **-.0945 J**, zero total force and correct segment-force couple. Tested explicit 0/90/180 endpoint energy ordering, both independent signed reversals, zero I/B, rotated external field axes and source JSON refusal for duplicate/unknown keys, booleans, nonfinite and under/overflow tokens.
4. The accepted nonzero-tilt subnormal issue below was independently reproduced both in the local source execution and in the newly authored remote reviewer native workflow. It is **not** an author-test expectation or CI screenshot issue.

## Reviewer-owned *real* PyVista / VTK challenge

- Created a distinct workflow in review_sandbox: [EMFEELD PR67 independent R1 native reviewer execution](https://github.com/physicsvigilante/review_sandbox/blob/main/.github/workflows/emfeeld-pr67-r1-independent-native.yml), reviewer workflow commit **cb036ea9f2198570d16f5571edce74fa1e4c5ea2**.
- Its independent [GitHub Actions run 44731442654](https://github.com/physicsvigilante/review_sandbox/actions/runs/44731442654) is **SUCCESS**. The workflow checked out the immutable feature commit and verified the exact Git tree before installing **real PyVista 0.48.4 / VTK 9.6.2**. It did not execute the author's tests as a substitute for its own challenge.
- Reviewer exercised actual VTK KeyPressEvent for **1,2,3,4,5,6,n,b,f,v,0**, and actual angle and B-magnitude slider EndInteractionEvent. Preset state changes and zero glyph boundaries passed. Negative signed B survived field slider change (current B=-.42 T, angle 73 degrees), while positive geometric normal stayed fixed on signed reversals. Camera/show/hide-only changes did not rebuild physics; physical edits did. Forged conflicting authored/live/raw source was refused before creating an output directory.
- Newly generated original reviewer PNG at **reviewer-original/view.png**, in [run 44731442654 artifact emfeeld-pr67-reviewer-01-native](https://github.com/physicsvigilante/review_sandbox/actions/runs/44731442654). Original reviewer artifact **14626362996**, whole ZIP SHA-256 **045ff9668b88ff65acb9ceaec577c78b6516b66db0a6b35d711e44d9f26ab0fd**. Independent new PNG SHA-256 **733745b86590ade4c4d6e14f9120243b84f0467a7bfaf12ea4112628e0241fc8**, verified 1200x760 nonblank; manually inspected legible right-hand text without pseudo-column pipe separators and *two visible native slider rails*. No pre-existing author PNG was repurposed.
- Fresh evidence original raw source SHA-256 **9d2735ce95bff665f7b4c46ad34feace6089cfaa44cf3357d2c3786b0ba79e03**, exact recorded initial and current state, 7/7 fresh output integrity hashes, native PNG and NPZ independently checked; all three reported code-file SHA-256 values agreed with the exact pinned source bytes.

## Independent downloaded original author-CI artifact audits

Each original GitHub ZIP below was freshly downloaded and rehashed *as a whole*, its CRC and duplicate paths checked, and contained scene integrity manifests independently checked. The seven lesson source TARs, the source-snapshot TAR and general-viewer TAR are byte-identical to the exact source TAR SHA-256 above.

| Original artifact (ID) | Original whole ZIP SHA-256 | Independent result |
| --- | --- | --- |
| Dedicated 14621763327 | 8c722874bb29cb57c92c99f68401159be5c185d3395fd1d0edfffca74d96c0d7 | 11 genuine scene PNGs, 77/77 scene hashes; authored/raw/current NPZ SI samples, force couples and U verified |
| Source 14621699281 | 3001faa8fcf19a9b13d8a029f1989155c02c9c1e502494f8b151264725b6e6ec | all 475 source ledger entries and source TAR verified |
| General viewer 14622226441 | 2111eec2dd6b1d72c910c8620255e77148996b87a7ea4cec3edb6543fc9f702e | 17 original PNGs decode; same TAR |
| Linux full 14622716999 | ea9aef2836a172f60e328698cba482fcaa90b5484046bcf40bf6a5c5cb26e8ff | 2,300 headless +119 real-PyVista PASS; 1,749 authentic hash refs |
| Windows full 14623088275 | 2b3696b94b30d25b24ee4b27775d6ecb29d31f1a195d3ec18d41e8db013465dc | 2,300 headless +119 real-PyVista PASS; 1,749 authentic hash refs |
| Straight wire 14622635660 | f29b0a9ded7cafe92c815dcbacd9b34d89b022e82f62be6684b94cd969be1093 | 49/49 hashes |
| Circular loop 14622586446 | 62abd6a4f8af79efb23d7364ad08c0398e3aa3f3a75b99f2c54394db55b9199a | 63/63 hashes |
| Gauss 14621947576 | 7f10155620a7511a3788159d1a36cfa21e461deb36b5972b0aaaae81adddf7b1 | 148/148 hashes |
| Conductor cavity 14622275903 | d3b830ee2ce46ec8fc504526032794b661014117ed9df2f399b826200b457404 | 36/36 hashes |
| Dipole 14622850512 | 6d2cffc79f628ec100e07fb2ba22c0004decf0997f2c0d5e90f6814c9fad78c6 | 239/239 hashes |
| Capacitor 14621394101 | 796c876472d0d12342f34f5ca1389867ee16f2c9aee4b0396f448c8fd6b29e1f | 63/63 hashes |

Each full-OS ZIP has 2,186 unique entries, 173 original integrity manifests, 1,749 correct file hashes and **exactly one expected, deliberately corrupted negative-test reference**, at derived-001/G1/review-challenge-resealed-native/native/result.json. No unexpected hash failures. All 11 exact-head premerge workflows independently checked against live GitHub Actions API: **SUCCESS** with head 6abc5fa30fe96103b9a60e9946c188609fe88197. The Linux/Windows head-sha.txt values name the **synthetic merge** SHA, not actual main.

## Required finding F1 — silently lost representable torque (BLOCKER)

**File:** [src/emfeeld/rectangular_loop_torque.py, orientation(), line 176](https://github.com/physicsvigilante/emfeeld/blob/6abc5fa30fe96103b9a60e9946c188609fe88197/src/emfeeld/rectangular_loop_torque.py#L168-L177), with the resulting SI outputs in calculate() and measure().

**Reproduction:** An accepted state with theta = 1e-322 degrees, signed I=+10000 A, width=10 m, height=10 m and B=+10 T produces **torque magnitude 0 N m**, even though the nonzero physical torque for the *actual representable binary64 input tilt* is approximately **1.7246147e-317 N m**, itself representable. The angle-to-radians conversion rounds to zero *before* moment and field scaling; math.hypot at the final torque stage cannot recover the lost direction. The normal frame therefore spuriously becomes exactly aligned. Another admitted near-endpoint input, 179.99999999999997 degrees, produces 5.665538897647979e-9 N m versus 4.960524086056721e-9 N m from the endpoint distance (about **14.2%** relative error).

This lies well outside typical JEE demonstrations; nevertheless the release contract specifically requires **strict underflow/representability** and preservation of **tiny but representable nonzero torque**, so silent zero is not consistent with the stated admitted domain.

**Required correction:** In the analytic state/orientation boundary, either (a) implement stable angle/torque evaluation and consistent representable frame construction, or (b) explicitly reject angles for which their implied nonzero physical orientation/torque cannot be faithfully represented, before producing apparently exact zero outputs. Test the admitted/rejected boundary with 1e-200, 1e-320, 1e-322 and near-180 one-ULP cases, plus reversals and exact endpoint zeros. Keep original source/state provenance and native presentation behavior unchanged. This is a narrowly scoped numeric/validation fix, not a request for new general physics.

## Conclusion and gates

**CHANGES REQUESTED.** Independent normal-range science, strict-source checks, actual reviewer-owned native 3D interaction/screenshots, exact-source integrity and inherited CI regressions passed. F1 blocks a scoped PASS on the *currently advertised numeric domain*. There is no support here for claiming educational/human efficacy or manual Windows desktop usability; [Issue #64](https://github.com/physicsvigilante/emfeeld/issues/64) remains deferred.

Do **not** merge PR #67 on this review. Correct F1 on the feature branch, regenerate a **new exact-head pinned review packet**, and repeat independent verification at the changed source identity. Even a later scoped PASS is not itself a release: guarded integration and fresh **actual production-main** Linux, Windows, real PyVista, and archived evidence checks remain required.
