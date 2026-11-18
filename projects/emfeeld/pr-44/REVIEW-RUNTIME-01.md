# PR #44 — offline graphics-runtime provisioning record 01

**18 November 2026: runtime available and checked by the AUTHOR; independent R2-B01 remains OPEN.** The original independent [review-01](reviews/review-01-chat-b.md) remains **INSUFFICIENT EVIDENCE / DO NOT MERGE**. This record remedies dependency availability, not review independence. No reviewer verdict is prewritten here.

## Unchanged source

Candidate HEAD `e253d0acf15e7505f1da8ab95cb519b59b0d720b`, Git tree `8a4a14d70ba824e8a338add08356003e79a248bc`, base/main `60b6e751363d0b922a02c3a259110547b79cf25c`. The exact candidate original source archive was re-extracted, all files indexed and the tree reproduced before the author runtime smoke. Working-tree diff after the smoke is empty. Nothing was committed to the candidate or main. No physics formula, original input, PDF, tolerance, lesson control, test or sealed evidence changed.

## Original runtime artifact

An auxiliary, unmerged support branch `support/pr44-offline-pyvista-review` starts at main and contains only the provisioning workflow `.github/workflows/pr44-offline-review-runtime.yml`. Commit **`b99f832cc48c81984b8c830ada065cf9614ebf46`**. It is not a product/review candidate and is not intended for merge. It downloads third-party dependencies and runs only a basic third-party renderer smoke, never candidate tests or a reviewer verdict.

Original [provisioning workflow 44256323755](https://github.com/physicsvigilante/emfeeld/actions/runs/44256323755) **COMPLETED SUCCESS**, event push, attempt 1. Original ZIP artifact **14406007331**, name `pr44-offline-pyvista-b99f832cc48c81984b8c830ada065cf9614ebf46`, size **3,241,942 bytes**, SHA256 **`2f51d4a7aa4ef2a5d722627a6b3707c6e8efaef3bc486ab47675574df3d01295`**. Download through GitHub's `download_workflow_artifact` action for repo `physicsvigilante/emfeeld`; no network/PyPI access inside the review container is required after transfer. GitHub reports artifact expiry 18 December 2026; preserve original bytes when obtained.

The author downloaded the actual ZIP, checked that whole digest against GitHub, CRC-read all **14 entries**, rejected unsafe paths/duplicates/symlinks, and independently checked every original wheel hash. The package contains only five original pure-Python wheels plus metadata/logs/basic renderer proof, not a full Python environment:

| Package | Version | Original wheel SHA256 |
|---|---|---|
| pyvista | 0.48.4 | `a46eda178e10e279afda550c341676a82dcee607c86db74565fa455ac0bd23e2` |
| scooby | 0.12.1 | `4e3e474a3542fd1d19d775cea70d19ce58a005102c0206955dddbbd33f07eb4e` |
| cyclopts | 5.5.2 | `4fbe863ebace1c65dafc6520c82217915b103d27fbd1d8fcd168f2abcca3a12a` |
| rich-rst | 2.2.0 | `1ea1c43813dc4a8d86475fce27ffb74e0ada3d4656c9f8130ba2a59868055fe9` |
| docstring-parser | 0.18.0 | `b3fcbed555c47d8479be0796ef7e19c2670d428d72e96da63f3a40122860374b` |

These versions match the original lesson's retained dependency versions. VTK, NumPy, matplotlib, Pillow, pooch, rich and their dependencies must already be available in the isolated reviewer container. No installation on the owner's Windows/Conda or system Python is requested. The archive has no source implementation or reviewer assertions hidden in the packages; these are original package wheels. Independently inspect `manifest.json`, wheel metadata and original hashes before use.

## Offline installation, no source changes

Let `RUNTIME` refer to the safely extracted artifact directory, `OVERLAY` a **new** writable directory, and `SOURCE` the reconstructed exact candidate checkout. In a fresh process:

```sh
python -m pip install --disable-pip-version-check --no-index --no-deps \
  --find-links "$RUNTIME/wheels" \
  --target "$OVERLAY" -r "$RUNTIME/requirements-overlay.txt"

export PYTHONPATH="$OVERLAY:$SOURCE/src"
export PYVISTA_OFF_SCREEN=true
export VTK_DEFAULT_OPENGL_WINDOW=vtkEGLRenderWindow
export LIBGL_ALWAYS_SOFTWARE=1
export MPLBACKEND=Agg
export OPENBLAS_NUM_THREADS=1
export OMP_NUM_THREADS=1
export MKL_NUM_THREADS=1
export PYTEST_DISABLE_PLUGIN_AUTOLOAD=1

python -c 'import pyvista, vtk; print(pyvista.__version__, vtk.vtkVersion.GetVTKVersion(), pyvista.__file__)'
```

Do not reuse a process that already imported conflicting modules. Retain installation output and actual import paths/versions. Verify the candidate Git tree/import origin separately. This overlay must remain outside the source checkout and outside previously sealed evidence. If any prerequisite is missing or incompatible, record the failure rather than substituting a fake renderer.

## Actual author-side local availability proof (NOT independent review)

The previously offline author container had VTK but no PyVista. Direct online pip download failed. Offline `--no-index --no-deps --target` installation from these exact wheel bytes succeeded. Actual imports: Python **3.13.5**, PyVista **0.48.4** from the new overlay, VTK **9.6.2**. Existing local NumPy **2.3.5**, SciPy **1.17.0**, pytest **9.0.2**, matplotlib **3.10.8**, Pillow **12.3.0**; this is not falsely described as byte-identical to the hosted dependency environment.

A small AUTHOR availability script instantiated the production `CavityLesson` (zero source strength, four display-line seeds, minimum admitted mesh resolution), confirmed all four real widgets enabled and attached to the right renderer, fired an actual VTK `EndInteractionEvent` to change offset, toggled cutaway without changing the camera, and saved a fresh current-state snapshot and actual PNG. Original/current input distinction was false as expected after interaction. Original PNG SHA256 **`4f33777561e0c8926e70a2b46374890f2e79ac6bcf17914b50b787afb1a5d5ed`**. This proves the runtime path works locally; it does NOT cover the independent review's nonzero-charge physics, all controls/keys, glyph containment or rejection challenges.

**Preserved incomplete author execution:** an initial attempt to request a streaming shell session was refused before execution. A subsequent run of all four source-authored graphics tests timed out at 120 seconds after one progress dot; no completed whole-suite pass is claimed. A smaller real-widget capture then completed with numerical-library threads limited to one. The timeout did not change candidate code and is not evidence of a new physical defect. These checks remain AUTHOR evidence; reviewer must execute its own tests.

## Remaining independent work

Continue in the same Chat B reviewer context. Use the original review's **R2-B01** requirements: actual production PyVista widget and keyboard events, enabled/visible representation membership, model/slider/preset synchronization, camera/cutaway invariance, actual production arrow meshes at near-wall offsets for both signs, and fresh screenshot/current-state/original-input/camera/array consistency plus capture-failure and protected-root checks. Retain first failures, independently inspect the rendered PNG content, and append `reviews/review-02-chat-b.md` pinned to the unchanged candidate. The earlier favorable independent physics/archive work can be referenced without relabeling it.

Neither this bundle nor a passing author smoke closes R2. PR #44 remains draft/unmerged until Chat B supplies an attributable verdict supported by its own real-PyVista execution. Human Windows operation and classroom acceptance remain separate.
