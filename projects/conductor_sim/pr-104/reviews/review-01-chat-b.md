# Independent Chat B review 01 — conductor_sim PR #104

**Outcome: PASS (strictly scoped to the post-M40b corrections, not permission to merge).**

Reviewer: separate ChatGPT conversation, GPT-6, 2026-11-20 (Asia/Kolkata). This is an LLM review in a separate context, not independent human subject-matter certification. Risk class: R2, physical correctness and evidence integrity. No production repository changes, merges, workflow reruns or dependency installations were made.

## Source identity and exact inspected evidence

- Production: https://github.com/physicsvigilante/conductor_sim/pull/104 (DRAFT / UNMERGED at final verification).
- Pinned candidate HEAD: **d35149d89b049a4b3db59ada558145798eff958b**; reconstructed Git TREE: **25e91e0fd53749bf6c6c578583310b219e1ecb4f**.
- Released M40b baseline HEAD: **4bae2f6be5a1689b9e1dc80d2dd146b77d366a3e**; independently reconstructed TREE: **5ea6098d463eec12fbc184ab3a6fca2f27699e9a**.
- Source archives: baseline from workflow [44577369591](https://github.com/physicsvigilante/conductor_sim/actions/runs/44577369591), artifact 14556359640; candidate from workflow [44586426053](https://github.com/physicsvigilante/conductor_sim/actions/runs/44586426053), artifact 14562245243. The candidate archive ZIP SHA256 was 0bf79936775e8361a2a1a4cd0a0567a6993a37c90564c8d0e68464f32414a2e8. I extracted both archives, performed git init/add/write-tree locally against their complete content and obtained exactly the two specified tree hashes. I also compared the tracked-file inventories: **15 modified + 7 added = 22 changed files** and no deletions.
- Original PDF SHA256, verified from both extracted archives and hosted audit hash files: 02_conductors_half_size.pdf = **9dff3c02a9f1848d2c3d99cb1a6e7a44dc7f5a51f7a3a2b8cc92d10ce1fbca5d**; POTENTIAL_CONDUCTORS1.pdf = **8d0d9b5cf821219058cfc4b7685a39b777e460944df44c3f9cffcb68157a60e5**.
- The M40a raw-query ray/kernel source (src/conductor_sim/spherical_multicavity.py), native atlas generator (src/conductor_sim/spherical_sigma_atlas.py), and independent Decimal reference (tools/m40a_spherical_reference.py) are byte-identical between baseline and candidate.

The source repository had no AGENTS.md at the pinned HEAD (GitHub returned 404). The hub's AGENTS.md, PROTOCOL.md and REVIEW-RISK-POLICY.md governed this report.

## Reviewer-owned native experiments

I executed a fresh, external reviewer script against **both unmodified extracted source trees**, in separate Python 3.13.5 processes, importing their actual modules via PYTHONPATH. I did not reuse the candidate's developer fixtures for the novel geometry. The script's corrected version SHA256 is **49e110853a9fead42055d7d551b4b9daf0753a37b0a9c3664954c1800add3de2**. It uses explicit reflected-charge geometry and source positions for expected V, E, force and surface density, *not* the production plane-image constructor. Numerical comparison: relative tolerance 7e-13; default absolute tolerance 2e-19, tightened to 1e-25 for force components. The production tolerance/domain was never changed.

**A1: New signed, oblique, translated two-source plane.** Raw direction = (-7, 5, -2) times ulp(0.0). Independent unit normal = (-0.792593923901217, 0.5661385170722979, -0.22645540682891913). Physical plane origin = (0.42, -0.73, 0.21) m. Two unlike signed sources: +1.7 nC at (-0.1188567688247277, 0.03585781098669314, 0.16882724150066664) m; -0.63 nC at (-0.8020424737815374, -0.1520493850260777, -0.29436621509094474) m; intended signed heights = 0.87 and 1.41 m. Observation = (0.21422951257768008, 0.05600879656768081, -0.28421521448070264) m. Surface probe = (0.49414869117017846, -0.5248935928245629, 0.4632455988429677) m.

| Quantity | Independent reference | Candidate native | Released baseline native |
| --- | ---: | ---: | ---: |
| Physical normal length | 1.0 | 1.0 | 0.9813067629253164 |
| V (volts) | 15.099373043652975 | 15.099373043652975 | 15.477634284247328 |
| E_x (V/m) | 26.192165156482243 | 26.192165156482236 | 27.288222415329603 |
| E_y (V/m) | -1.688765916212954 | -1.6887659162129536 | -1.8411365456608393 |
| E_z (V/m) | -36.483737303550335 | -36.483737303550335 | -37.99445214820406 |
| F_x on +1.7 nC (N) | -5.1611233144587435e-9 | -5.161123314458747e-9 | -4.714957251923609e-9 |
| F_y (N) | -6.550575785268928e-9 | -6.550575785268927e-9 | -6.801773599431346e-9 |
| F_z (N) | -5.533680246695301e-9 | -5.533680246695302e-9 | -5.379443121442088e-9 |
| sigma at surface (C/m2) | -3.055593301191373e-10 | -3.055593301191373e-10 | -2.998474371208388e-10 |

The native backend canonicalizes charge sites by position, so the reviewer selected the +1.7 nC source by actual position, not by original list index.

Four corrected consumers (ConductingPlane.normal, Motion1DSpec.axis, motion_2d._unit and visualization.unit) gave length 1.0 on the new encoding; the baseline gave length 0.9813067629 for the consumers it completed. Three fresh ordinary vectors retained exact preexisting binary64 division results in both trees. All three directly checked normalization consumers refused zero, NaN, infinity and overflowing norm.

**Native motion / metre-scale slice.** For a separately authored one-charge/one-grounded-shell system (shell radii 0.9/1.2 m, charge 0.7 nC, mass 0.002 kg, initial speed 0.16 m/s), the actual Native NestedShellBackend + integrate_motion_1d ran four saved samples through 0.018 s using the tiny signed-oblique axis; final scalar displacement = **0.0028800000004697516 m**. The same-ray ordinary axis produced the same native displacement and position to roundoff. The released baseline's tiny-axis investigation refused with "transverse electrostatic force breaks one-dimensional motion", while its ordinary-axis run completed. SliceSpec world/project roundtrip at local (0.29, -0.18) m returned (0.29, -0.18) m, plane-normal length 1 and 3D distance **0.3413209633175202 m** for the candidate; baseline projected the first coordinate as 0.27925925925925926 and physical distance as 0.33672716728114643 m. No tolerance was relaxed.

**A2: New authentic signed/empty/charged cavity arrangements.** I authored an independent spherical geometry with isolated/grounded native solutions using cavities A (two opposite signed charges), B (one negative charge), and E (empty), non-origin-centered spheres and three raw surface rays per face. Fully valid **one-, two- and three-cavity** manifests all passed the candidate's actual standalone checker, with unchanged source IDs, ray records and units. For each of the different three-cavity orders (last E empty; last B charged), I removed the final displayed cavity row and the corresponding isolated/grounded per-face witness entry but retained every original authoritative void/Gauss record. The original baseline checker **accepted both omissions** as two-cavity evidence, while the candidate refused both with "displayed cavity inventory must include every native cavity". On each complete three-cavity case the checker verified 3 cavities, 3 genuine sources and 18 signed inner image samples. Separately, duplicate and reordered visible cavity rows, Boolean charge substitution and Boolean metadata coercion were refused by the candidate.

**A4 additional checks.** Beyond the developer's 20 regression pairs, I independently tested 18 different downstream source/reference/config path examples against the actual PR filter globs of all seven touched workflows. Baseline had **2/18** covered; candidate had **18/18**. Inspection of workflow diffs showed only additive PR path triggers, preserving the existing native, independent-reference, browser and FEMM tasks. The added source-pinned post-M40b audit workflow preserves baseline red negative controls and requires the candidate green result. This is not an assertion that every possible future workflow dependency was exhaustively enumerated.

**A3 navigation.** README.md, docs/current_capabilities.md and docs/architecture.md describe released M40b versus unmerged post-M40b corrections and charter-only M40c. Previous root README.md (45,612 bytes; SHA256 **44744749f54f77f3edd37c4b4486bd3f7da3cf21dd39cc8f595e3dab0d197ffe**) equals the new README-MILESTONE-HISTORY.md byte-for-byte. All scanned relative Markdown links resolved in candidate: 19 current README, 62 historical README, 16 map, 2 architecture. Documentation avoids new scanned-question success claims; legacy Boolean-coercion and JSON-versus-edited-HTML trust limitations are visibly retained.

## Hosted runner evidence independently inspected

- Audit workflow: [run 44586426375](https://github.com/physicsvigilante/conductor_sim/actions/runs/44586426375), jobs 135780488559 (Python 3.10) and 135780489102 (Python 3.12). Downloaded the actual archive artifacts **14561676338** and **14561775492**, inspected both JUnit suites, logs, head.txt, tree.txt and hashes.txt. Each runtime reports baseline **43 tests / 37 failures / 0 errors** (EXPECTED negative controls), candidate **43 tests / 0 failures / 0 errors** (43 passes). Both archived HEAD/TREE and PDFs exactly match this report. No red baseline control was rebranded as a passing scientific test.
- Independently ran the candidate's targeted 43 pytest regressions locally: **43 passed in 0.26 s** (Python 3.13.5; supplemental only).
- GitHub reports **30 associated current-head PR-triggered workflow runs, all completed-success** for this source. Sample hosted jobs directly inspected: [Python checks 44586425700](https://github.com/physicsvigilante/conductor_sim/actions/runs/44586425700) (3.10/3.12); [real FEMM 44586426017](https://github.com/physicsvigilante/conductor_sim/actions/runs/44586426017); [M40b real Chromium and native sigma 44586426581](https://github.com/physicsvigilante/conductor_sim/actions/runs/44586426581); [M38b browser 44586426787](https://github.com/physicsvigilante/conductor_sim/actions/runs/44586426787). These are **hosted** acceptance results; I did not personally execute FEMM or Chromium locally.

### Preserve first reviewer attempts (do not rewrite history)

1. The first baseline reviewer run exited with a reviewer-harness FileNotFoundError: it incorrectly attempted to read README-MILESTONE-HISTORY.md from the **released** tree, where that future relocation does not exist. First stderr retained. Corrected only the external reviewer script to skip release-inapplicable navigation links.
2. The first candidate script completed but recorded an apparent force mismatch. The reviewer had assumed source list index 0 survived the backend's documented native site canonicalization; the correct source was index 1 after spatial sorting. First candidate JSON retained. Corrected only reviewer indexing, recalculated the exact physical force for the +1.7 nC source, then reran both extracted trees; candidate E/V/force/sigma agreed with the separate analytic reference. This is **not** a production defect.
3. First and corrected probes, JSON results, hosted 3.10/3.12 JUnit XML and identity files were retained as a conversation evidence ZIP. No production source was changed. Reported outcomes above are the corrected, explicit reviewer-owned second execution, not misrepresented as first-attempt perfection.

## Scoped findings and judgments

**No demonstrated outstanding blocker or major defect in A1–A4.** The novel numerical and evidence omissions fail on unmodified M40b and pass/refuse appropriately on the pinned candidate; preservation of existing qualified scope and current-head CI is supported. The source and semantics checks are bounded, not a full audit of every historical module.

| Dimension | Verdict | Basis |
| --- | --- | --- |
| Original-source fidelity | PASS in changed scope | Both PDFs byte-hash matched; no newly solved source JEE item was asserted. |
| Physical and numerical correctness | PASS in changed scope | Fresh signed-oblique independent E/V/force/sigma, real native motion and SI slice agree. |
| Native investigation and output | PASS in changed scope | Fresh native model-based runs; inherited hosted native/FEMM gates successful. |
| Evidence integrity | PASS within stated JSON contract | Omission of charged/empty cavities is rejected; identity/hosted controls checked. |
| Teacher-facing usefulness | PASS within declared scope | Current M40b map, honest partial/refusal boundaries, readable examples. |
| Textbook-answer completeness | NOT CLAIMED | No new original scanned JEE solution claimed by this correction. |

**Non-blocking residual limitations:** Standalone JSON self-consistency does not authenticate arbitrary external HTML or historical provenance; the project retains older constructor Boolean/coercion behavior intentionally; path filters are conservative rather than formally complete; locally this reviewer used Python 3.13.5 rather than re-running real FEMM/Chromium (their original current-head hosted runs succeeded). This review does not prove the entire 87-module project is error-free or certify M40c's future implementation.

## Release advice

**Scoped PASS for the unchanged literal candidate HEAD/TREE, not source-PR merge permission.** Keep production PR #104 draft/unmerged until separate explicit owner approval. Any new HEAD invalidates this PASS and requires targeted re-review and exact-head CI. A source merge requires expected-head protection, equality of the reviewed tree on main, and genuinely successful postmerge main-push CI. No auto-merge.

All cited hosted runner artifacts and links are from actual downloaded or queried GitHub Actions evidence. This report and its associated reviewer probe description are append-only and review-hub only.
