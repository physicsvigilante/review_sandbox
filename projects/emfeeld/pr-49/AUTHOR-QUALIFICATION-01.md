# PR #49 — author qualification of bounded Gauss presentation follow-up

2026-11-18. **Author evidence, not an independent review. Draft/unmerged.** Tracks Issue48 after PR47's actual-main release completed and Issue46 closed. This report records the current completed local/source/lesson/viewer/Ubuntu gates; the final full Windows gate and any additional original archive audit must be recorded separately rather than inferred.

## Source and change boundary

Candidate `9963c09d169a04cea488886db5f04c0de4074886`; tree `4da6b80f53d78b2394c8516b9463e442fffb50fe`; fully released base/main `f6a078354ec2a657ca010c5c92ea578a0f55a2ad`, tree `65935bb395552d3dfb466a6e48d03230f18b6b66`. GitHub CI preview `7635a3e96079f54167dbbb14f96299e8397555a1` has the candidate tree and ordered [base,candidate] parents. Local reconstructed source has394 tracked files and34 package modules.

Exactly six changed paths: modified `src/emfeeld/gauss_view.py`, `.github/workflows/gauss-lesson.yml`, `docs/GAUSS_LAW_LESSON_V1.md`; added `tests/test_gauss_lesson_presentation.py`, `viewer_tests/test_gauss_usability.py`, `tools/qualify_gauss_usability.py`. All388 other baseline files remain byte-identical. No field law, Gaussian integral, boundary guard, old test, source PDF, historical evidence or general release workflow changed. Existing numerical `save_snapshot` output semantics and availability remain; additional display metadata is explicitly informational.

## Intended behavior

Sphere sampling advice is shown when abs(sample-minus-exact) exceeds0.01*sum(abs(all prescribed charge strengths))/epsilon_0. This is a **teaching attention threshold**, not an integration tolerance, rigorous error bound, pass/fail gate or certificate. Zero enclosed charge does not cause division by zero; all-zero charges give no caution. Signed cancellation can conceal individual errors, so the docs explicitly deny that absence of a warning establishes accuracy. Exact/sample/error values are never rescaled. Prediction hides the banner; undefined boundary/cube states clear it; refinement can leave the warning visible.

The viewer has a wider panel, a separated scalar bar/keyboard footer/axes inset, more legible slider titles and distinct0.9999/1.0001 displayed coordinates. Annotation size settings respond to native VTK render-window events without recomputing physical state, field arrays, flux or camera. Supported minimum840x560/default1440x960 were tested and actual images inspected. Below-minimum windows are not claimed readable. Snapshot display metadata includes actual window size, font settings and caution data/visibility. Offscreen software rendering is not manual Windows use.

## Completed local execution on current source

Linux isolated environment: Python3.13.5, NumPy2.3.5, SciPy1.17.0, pytest9.0.2, VTK9.6.2, PyVista0.48.4. Existing declared graphics dependencies were installed only into `/mnt/data/gauss_followup/overlay` from the preserved optional PR44 five-wheel offline overlay; no user-computer environment changed. Runtime ZIP SHA256 `2f51d4a7aa4ef2a5d722627a6b3707c6e8efaef3bc486ab47675574df3d01295`.

Environment: `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1`, `PYVISTA_OFF_SCREEN=true`, `VTK_DEFAULT_OPENGL_WINDOW=vtkEGLRenderWindow`, `LIBGL_ALWAYS_SOFTWARE=1`, `MPLBACKEND=Agg`, with overlay and exact-source/src on PYTHONPATH.

- `python -W error -m pytest -q tests`: **1,822 passed in211.49s**.
- Historical `pilots/authorability_v1/test_pilot.py -k 'not test_all_available_parent_files_remain_frozen'`: **18 passed,1 deselected in0.98s**. The exclusion is the existing obsolete baseline guard, not a new test relaxation.
- Complete rerun `python -W error -m pytest -q viewer_tests`: **51 passed in242.43s**, returncode0. The preceding240s-limited attempt produced48 passing progress markers and then timed out: **incomplete**, not51 passes. Both logs remain.
- New display cases:39 headless passed0.63s;5 actual-PyVista cases passed20.89s. They are included in the full suites, not additional unique tests.
- Six new real usability scenes completed in12.46s; eight original Gauss scenes completed in45.89s. Both used the actual production controller and retained state, arrays, image and implementation receipts.

The new graphics cases use actual native window SetSize/Render and slider EndInteractionEvent. They check text bounds/separation, source/result/field/camera preservation on resize, outside-zero exact total, prediction, refinement, boundary clearing, cube clearing and changed-current-state snapshots with original input retained. No surrogate scene or substitute widgets are called real PyVista.

## Hosted completed gates and original archive audits

| Gate | Run | Artifact | Original ZIP SHA256 |
|---|---:|---:|---|
| Source |44302715755|14427545169|`7ae28db3a740cd3aeb1feefd31f5a53600773aa130cde6be6858c943376aa4a7`|
| Gauss lesson |44302715942|14426857273|`3dd97ba302defcfe9131b51fbb101afe83b3b25b2c7cb864cd490bdea732e195`|
| Existing viewer |44302715977|14426173064|`de1a0cf6f741eea402c700536359877dd9b6834d3e589dc86d759c7e892544a0`|
| Existing cavity |44302715844|14426358879|`03d203d48948d49fe942cf2e2a3ed54856967db8244e6e8caab206ade7e82f08`|
| Full Ubuntu |44302715851|14427556887|`ad69ab8c8071ba600ba218f1b0b80e481c4123536ae0396a88efef6c939e19ae`|

All five original ZIP payloads were downloaded and their whole digests checked against GitHub, with CRC and safe/unique member checks. Source/lesson/viewer/cavity TARs each reproduce the394 candidate files. Source ZIP contains the exact preview/tree identities; source TAR SHA256 `375c61cbdea9c9fb2f9595fdc475f46f898143f55f22b75f421ed19646c7222e`. A reconstructed local Git index writes candidate tree4da6b80f... .

Dedicated Gauss CI passed **127 overlapping focused tests in59.79s** and retained8 original plus6 new scenes. Its114-member archive contains92 manifest references and476 module references (34 per14 scenes); all match their original stored bytes. Current physical states, authored-input references and image digests are bound to the receipts. Boundary scene remains unavailable with null exact total/no field arrays. Actual small/default usability images and the six-scene contact sheet were inspected by the author.

Existing viewer CI passed1,822 headless and its9 legacy scene cases;17 PNGs are retained. Existing cavity CI passed71 focused tests and6 scenes;49 archive members/36 manifest references and current-state/module/image receipts verified. These do not certify new human operation.

Ubuntu original ZIP has2,186 safe unique members,173 integrity manifests/1,750 references,1,749 matching hashes and the known deliberate corrupt negative. All82 implementation-receipt sets match34 candidate modules. It records1,822 headless+18 historical+51 real-PyVista passes and exact CI preview SHA. E1 remains complete, G1 partial; a renderable G1 member does not upgrade the ensemble. Windows and its original ZIP remain a separate gate at this report entry.

## Cross-version physical preservation and retained audit correction

The first comparison harness incorrectly demanded **bitwise equality across separate hosted runs**. It stopped on a centre-scene E component difference of4.440892098500626e-16. Its script/log are retained. No production source or established physics-test tolerance was changed in response.

A separate completed comparison checked all8 matching released-PR47/candidate scenes: authored physical states, analytic probe positions and normals are bitwise equal. All numerical physics modules are byte-identical. Six result dictionaries are exactly equal; the dipole sphere sum/error differs by1.3322676295501878e-15 N m^2/C, and the rotated-cube sum differs by5.329070518200751e-15 N m^2/C, with face rounding differences up to7.105427357601002e-15. Maximum saved-field difference is7.105427357601002e-15 N/C, at most about1.14e-16 relative to the respective array maximum. These observed roundoff-scale differences are recorded explicitly rather than calling arrays byte-identical. They are not alterations of archived hashes or a new physics acceptance rule.

## Earlier implementation failures retained

Initial prototype used an array name instead of the actual scalar-bar title and raised KeyError. Corrected before the candidate commit. The next prototype screenshot still clipped one readout line and crowded the axes/footer; the panel was widened and the axes moved before this commit. Both first logs and prototype images remain. The source-first layout checks, new tests and all current-source full passes were run after those corrections. The separate240s local graphics timeout remains incomplete even though a new longer run passed.

## Review and remaining gates

This is proposed **R1 bounded presentation work**, requiring focused independent scrutiny of caution meaning, native resize/control behavior and receipt accuracy. It does not warrant re-reviewing unchanged solid-angle physics merely because UI code changed. Escalate any actual change to measurement/admission semantics. No independent approval is asserted in this author report.

Keep PR49 draft/unmerged pending complete exact-source hosted qualification/original Windows archive and focused review. Guarded integration and fresh actual-main CI/new original archive audits are later gates. Issue48 stays open. Issue50 is separately scoped future dipole physics, not implemented here. Human Windows, teacher usefulness and unseen JEE evaluation remain unestablished.