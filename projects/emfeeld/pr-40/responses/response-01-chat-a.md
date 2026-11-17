# EM Fields PR #40 — author response 01 to independent R2 review-01 findings

**Status on first publication, 2026-11-17: three review findings corrected in a NEW, independently unreviewed source commit; local full suite PASSED; fresh hosted Linux/Windows, viewer/source archives and independent R2 review-02 remain PENDING.** This is the implementing author's response, **not** the reviewer’s own PASS or merge permission. PR #40 remains DRAFT / OPEN / UNMERGED.

## Preserve the original failed review unchanged

[Independent Chat B R2 review-01](../reviews/review-01-chat-b.md) issued **CHANGES REQUESTED / DO NOT MERGE** on **old head `9fa09dec92b8925591505d1da0bc2639a53a30d9`**, Git tree **`9491d39d3f0415a5e90f1848173cf73af5d02584`**, qualified base/main `066c94e4953c3ef29302c0bb6d0ee2f6cb8b8ca0`. The old full 1,629 test suite and all four pre-merge archives passed; fresh reviewer-owned adversarial tests found real failures anyway. Preserve independently reported first failures and the original old candidate/ZIPs. A reviewer harness regex mismatch and earlier full-suite environment setup errors are separately documented in the original report and are NOT source defects. No initial failing source attempt is relabeled PASS.

## Bounded exact new correction

New PR #40 feature HEAD **`f56ce83e791e3fcd3b1f17609c38a2f98a999c41`**, canonical Git tree **`48baa0d760a2e99d0e953d6df5d7b999801d48cd`**, one additional fast-forward commit atop the preserved failed/reviewed head `9fa09...`. Exactly **three changed files** from the reviewed source:
- `src/emfeeld/fields.py`: **R2-01** sphere centre/interior finite potential now avoids `coefficient * (3 - ratio^2)` overflow before dividing by the radius. **R2-02** norm uses stable `np.hypot.reduce`; sphere and shell potential/field use exponent-split `math.frexp` / `np.frexp` / `np.ldexp` to avoid spurious radius-squared/radius-cubed underflow and preserve finite physical outputs when an intermediate field coefficient underflows. Same existing analytic Coulomb/Newton inside/exterior/zero-reference formulas; no softening, new physical laws, numerical-tolerance relaxation or forced zero for nonzero undefined values. An actually overflowing final physical result remains a typed `numerical_error`.
- `src/emfeeld/trajectory_samples.py`: **R2-03** the requested-only invalid saved-time-grid short-circuit now calls the same cached per-particle no-solver failure record already used by full-scene capture, retaining `integration_attempted=false`, `unresolvable_time_grid` and `diagnostics_key`. Ordinary selection-only failures still do not fabricate trajectory run entries.
- New `tests/test_project_audit_r2_corrections.py` (13 new parametrized regression executions) covers reviewer finite-large interior, shell/solid tiny-radius exterior, electric/gravitational scalar+array potentials/fields, underflowed gravitational coefficient with finite true result, genuinely nonfinite output, undefined shell surface and zero-strength behaviour, invalid grid with two particles and solver spy both requested-only/capture, plus ordinary off-grid selection behaviour. No older tests/history/reviews were edited.

All three remote Git blobs were compared with **exact locally executed bytes** (SHA-1 IDs `dc2d1561abd46d7acfe8ae8b46f82ae55d92c0f0`, `ecb5308359bb05b428176dfd850be1ca618c2e9a`, `cf02b373bd7396cde36ba95319c74a54ac5ff615`), and locally rebuilt Git tree `48baa0d7...` exactly matches GitHub tree. Existing field implementation source SHA legitimately changes, so old source-locked studies may correctly refuse opening under new code; keep their original source environments or replay unchanged inputs into fresh outputs, **never reseal historical evidence**.

## Author-run original negative and corrected source qualification

From exact prior reviewed source, the new correction test file yielded **11 FAIL / 2 PASS**, preserving original red case evidence separately from reviewer-owned independent red logs. **Audit-harness ordering note:** an initial test invocation passed an absolute test path located in the *corrected* checkout, so pytest imported that checkout's code and incorrectly showed 13 green cases despite the old-source PYTHONPATH. I detected the wrong import provenance, copied the same test file into the unchanged prior-source checkout for a real old-source run, and retained the genuine 11-fail/2-pass log. No source or original reviewer evidence was modified. Most red cases were real finite potential/field wrong results, false overflow and the no-integration telemetry gap; the two already passing controls stayed passing. From corrected working tree: **13/13 new regressions PASS**; focused combination of new and old field/sample/audit tests **160 PASS**.

Actual corrected full local Linux source, CPython **3.13.5**, NumPy **2.3.5**, SciPy **1.17.0**, pytest **9.0.2**; warnings as errors and plugin autoload disabled for consistent environment:
```sh
PYTHONPATH=src:tests PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -W error -m pytest -q
# 1642 passed in 134.53s; exit 0
PYTHONPATH=src:tests PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -m pytest -q -W error pilots/authorability_v1/test_pilot.py -k 'not test_all_available_parent_files_remain_frozen'
# 18 passed; one obsolete all-file snapshot guard deselected
python tools/replay_packets.py verification/v6_published.json --output NEW_V6_OUTPUT
# 10/10 original cases pass
python tools/replay_packets.py verification/physics_demonstration_v1.json --output NEW_DEMO_OUTPUT
# 1/1 original case, 17 native observations / 64 independent-expression checks pass
python tools/replay_packets.py verification/discovery_examples.json --output NEW_DISCOVERY_OUTPUT
# 2/2 original cases pass
```
Compileall passed. Initial author attempt to replay discovery used nonexistent `verification/discovery_published.json`; corrected the command to the actual `discovery_examples.json` without changing code or claiming that first command succeeded. Counts are separate: the 13 new regressions are **included in** 1,642 headless, not added again.

## Qualification still required

Fresh exact-corrected-head GitHub PR workflows triggered automatically: [Linux/Windows clean-install #44143094109](https://github.com/physicsvigilante/emfeeld/actions/runs/44143094109), [source snapshot #44143094100](https://github.com/physicsvigilante/emfeeld/actions/runs/44143094100), and [separate real PyVista #44143094009](https://github.com/physicsvigilante/emfeeld/actions/runs/44143094009). They were IN PROGRESS at first author response. **Do not call the new head Linux/Windows/viewer/archive-qualified until these completed outcomes and original downloaded ZIP contents are checked.** After author archive qualification, request **separate-context targeted R2 review-02**, with new reviewer-owned cases and a `reviews/review-02-chat-b.md` verdict. No reviewer PASS on corrected `f56ce83e...` yet. PR stays DRAFT/UNMERGED; after a future guarded merge, actual `main` push CI/ZIP audits are separate gates.

No full Maxwell physics, generalized scientific certification, blind teacher interpretation, classroom usefulness, manual Windows interaction, malicious concurrent-filesystem security or proof of all extreme-magnitude validity is established by this fix.
