# EM Fields draft PR #40 — independent Chat B R2 review 01

**Date:** 2026-11-17  
**Independent verdict: CHANGES REQUESTED — DO NOT MERGE.**  
**Reviewer role:** separate-context technical source, evidence-integrity and adversarial reviewer. This is not a human physicist/teacher sign-off, malicious-filesystem audit, or general correctness certification.

## Exact identity and review boundary

- PR: https://github.com/physicsvigilante/emfeeld/pull/40 ; Issue #39.
- **Pinned candidate HEAD:** `9fa09dec92b8925591505d1da0bc2639a53a30d9`.
- **Pinned candidate Git tree:** `9491d39d3f0415a5e90f1848173cf73af5d02584`.
- Base: `066c94e4953c3ef29302c0bb6d0ee2f6cb8b8ca0`; base tree `33b58fb55b387ec2b7c1bdd61bf1af7764db97cd`.
- Workflow's source-equivalent preview `4b72af81ca7e0579c8b232c76143e0af8e008e03`: fetched independently from GitHub and verified **tree equals candidate** and **ordered parents equal [base, candidate]**. The preview is not a post-merge main commit.
- At review: PR draft/open/unmerged, one candidate commit, 21 changed paths; 371 tracked source files, including 30 `src/emfeeld/*.py` modules. Historical recorded tests/source/question files are not among the changed paths.
- Read `projects/emfeeld/pr-40/{REVIEWER-PROMPT-01.md,REQUEST.md,AUTHOR-ARCHIVE-AUDIT-01.md}`, exact-head `docs/PROJECT_AUDIT_2026_11_17.md`, candidate code and relevant base/source diff. **Author claims were not counted as reviewer-executed tests.**

## Verdict and required corrections

**The 1,629-test headless suite and all four original ZIP/archive audits passed**, but fresh tests independently reproduced **one newly introduced false-overflow regression**, **an inherited but scientifically consequential small-radius wrong-answer boundary**, and **a requested-only invalid-grid telemetry gap**. A passing existing suite does not erase fresh red evidence. Required corrections are scoped; no architecture reopening is proposed.

### R2-01 — BLOCKER, introduced by PR #40: finite solid-sphere interior potential is rejected as overflow

In `src/emfeeld/fields.py`, the new piecewise assignment evaluates

```python
result[inside] = self.coefficient * (3 - (r[inside] / self.radius) ** 2) / (2 * self.radius)
```

The changed multiplication order can overflow an intermediate despite a finite final analytic value. Independent counterexample:

```python
from emfeeld.fields import SolidSphere
from emfeeld import observations
s = SolidSphere('electric', 1e298, radius=10.0)
expected = (s.coefficient / 10.0) * 1.5  # finite ~ 1.3481327679256195e307 V
got = observations.evaluate_observations(s, [{
    'id':'interior', 'type':'potential', 'position_m':[0.,0.,0.]
}])[0]
# On pinned HEAD: got['status']=='numerical_error' rather than 'ok'.
```

The **base** version computes `self.coefficient * np.where(..., (3 - (r/R)**2) / (2*R), ...)`, so at the centre this case multiplies `coefficient` by the already scaled finite factor, rather than eagerly multiplying by three. The regression is specifically in PR #40's new arithmetic ordering; the proposed improvement for an unused overflowing exterior branch is valuable but incomplete. Preserve the intended lazy inside/outside selection while using overflow-robust order of operations. Test **both large finite interior and small-radius finite exterior cases** under `np.errstate(over='raise',divide='raise',invalid='raise')`, including scalar and array probes. Retain explicit typed numerical failures for actually undefined/nonfinite results; do not silently substitute zero.

**Preserved original reviewer failure:** `reviewer_additional.py::test_finite_inside_potential_unnecessary_intermediate_overflow`, `additional_first_attempt.log` (**2 passed, 1 failed**).

### R2-02 — material inherited numerical-domain gap: exterior field/potential at representable tiny radii

This edge case is **not established as newly caused by #40**; it exercises the existing `np.linalg.norm` underflow and radius-cubing strategy, despite the new branch fix. A finite exterior probe can be misclassified as interior because squaring `1e-170` to form its norm underflows.

```python
from scipy.constants import epsilon_0
from emfeeld.fields import SolidSphere, SphericalShell
from emfeeld import observations
import numpy as np
K = 1/(4*np.pi*epsilon_0)
q, R, d = 1e-180, 1e-200, 1e-170
expected_potential = K*q/d  # 0.8987551786170799 V
expected_field = (K*q/d)/d   # ~8.98755e169 N/C, also finite
for cls in (SolidSphere, SphericalShell):
    source = cls('electric', q, radius=R)
    print(cls.__name__, source.potential([d, 0., 0.]))
    print(observations.evaluate_observations(source, [
        {'id':'E', 'type':'field', 'position_m':[d,0.,0.]}
    ])[0]['status'])
```

**Pinned actual results:** `SolidSphere` potential `1.34813276792562e30` V; `SphericalShell` `8.987551786170798e29` V; **both field observations** `numerical_error`. Neither potential matches the finite exterior analytic answer. The field can also fail because the denominator `max(r,R)**3` underflows. This is a reproducible incorrect physical classification, not a failure of the analytic sphere law. Correct scale-sensitive norm/division handling for admitted finite inputs **or** explicitly reject outside-qualified representability ranges before computing misleading values; document the real numerical domain, not just float input finiteness.

**Preserved original reviewer failures:** `reviewer_numerical_boundary.py`, `numerical_boundary_first_attempt.log` (**4 failed**: two potentials, two fields).

### R2-03 — reporting-contract issue: requested-only rejected grid lacks explicit no-integration record

Fresh duration/sample pairs `(2e-323,31)` and `(5e-324,2)`, with two particles and requested trajectory samples, correctly return typed `numerical_error` / `unresolvable_time_grid`, status failed, null values, and **never invoke the monkeypatched solver**. But for `run_packet(packet, capture=None)`, `report['trajectory_runs'] == {}`; no per-particle `integration_attempted=false` entry is retained. With full `capture={}`, the same grid yields two per-particle `integration_attempted=false` entries and `(None,None)` trajectories. Both capture test variants PASS.

This mismatch violates the explicit reviewer telemetry requirement across requested-only/full-capture paths. It is **not** evidence that requested-only invalid grids reach the solver or fabricate trajectories. Correct the retained no-attempt reporting in the requested-only short circuit, or formally narrow/document the contract with a reviewed rationale; do not turn `{}` into a claim that integration was attempted. Test the two paths with a solver spy.

**Preserved original reviewer failures:** `reviewer_adversarial.py`, `adversarial_first_attempt.log` (two genuine telemetry assertions).

## Positive independent adversarial source tests

Independent tests (not imports of the author's two new audit test files) verified the following on pinned source:

1. Real sealed native run and model-store inventories stay byte-unchanged under new nested destinations, including symlink-parent aliases and multiple writer entrypoints; a real original frozen question/receipt lock from the Ubuntu ZIP also rejects a capabilities writer. No proposal reserve/output destination appeared.
2. Root markers for `integrity.json`, model store, question/receipt, completed study/replay, and started+outcome prevent descendant writes, without relying on marker JSON content. Partial/in-progress workflow markers permit intentional children; adding `outcome.json` then seals future descendant outputs. Ordinary non-evidence report replacement remains possible.
3. Oversize finite-input JSON integers in analysis checks, presentation replay speed, bounds and camera are rejected with recorded inspectable analysis rejection and no native results; malformed display ordering is rejected; nonobject revision proposals (null, bool, list, str, huge integer) reject before store mutation.
4. Parallel, antiparallel and zero-length camera bases reject; an oblique valid camera, reordered entity IDs and ordinary analysis admit. Independent presentation-view boundary test ensures invalid camera does not invoke the renderer and does not create a screenshot directory.
5. Analytic electric and gravitational `SolidSphere`/`SphericalShell` centre, interior, exterior, translated centre, potential continuity, shell discontinuity, force units/coupling, large ordinary-distance/small-radius exterior probes, zero-strength subnormal radii, nonzero singular-point errors and valid saved-time control pass at ordinary tested scales.
6. Input/output collision for native packet writes is refused without changing input bytes.

**First adversarial attempt preserved as originally executed:** `48 passed, 3 failed`. One of those three was the *reviewer's own overly narrow exception-message regex* on `model_cli.apply_revision`; the entrypoint legitimately rejected the sealed nested destination with a different `ValueError` message, and no protected bytes changed. That reviewer-test assertion was corrected, with its first failure retained as evidence, **not counted as a product defect**. Follow-up: `49 passed, 2 expected failures (xfail)` (the telemetry issue remains outstanding, not relabelled as a pass). Independent extra camera/input/overflow run: `2 passed, 1 failed`. Numerical-boundary run: `4 failed`.

## Original GitHub artifact audit — independently downloaded and rehashed

Actual original GitHub Actions artifact ZIP bytes were fetched, not reconstructed from author summaries. **Every member** of all four ZIPs was decompressed/CRC-read; checked archive path safety, traversal/absolute names, separators, duplicate names and casefold duplicate names. All original whole-ZIP digests matched the published original artifact digests:

| Original artifact | ID | Whole ZIP SHA256 | Entries | Verdict |
| --- | ---: | --- | ---: | --- |
| Source snapshot | `14348834555` | `9f256818a0b84f26d7a3246640622cfbc644747fdac14c291fab7c00a19a94ab` | 4 | MATCH / CRC-clean |
| Real viewer | `14349439448` | `d2badd4f8deb872b6e022711a8279ca44c5e4d2ce5975be7e8befbe12d5f3694` | 22 | MATCH / CRC-clean |
| Ubuntu release | `14350906584` | `47ef95e9be09b1c30b521daec16a9f30564e51cca6c8d48b6ebc33a67a552b5e` | 2,186 | MATCH / CRC-clean |
| Windows release | `14351741780` | `7f22e02f1785f3c697b1b8a09ffa9919d8eb8955312d3aae081773da5a30c3b0` | 2,186 | MATCH / CRC-clean |

Independent source TAR SHA256 `77bef7944ba6456a6904ce8c771b7a27c0077f21d940798ffa17960082b82e3a` matched. Source TAR **413 members** (371 tracked files +42 directories), safe extraction, no links/traversal. Its original byte-for-byte copy inside viewer archive matched. In a new local Git repository, `git add --all && git write-tree` reproduced **exact `9491d39d3f0415a5e90f1848173cf73af5d02584`**, and `git ls-tree -r` matched original `git-tree.txt` **byte-for-byte**, all 371 entries. Changed `src/emfeeld/fields.py` SHA256 `e71ec69755e1c08e6bc93076a2d09e073e40996ed27c3a6131645a546c5e493f`; corresponding Git blob `186a1fcadc3b8216700bd8a77590808e3ffb0c03`, matched original source index. New `output_safety.py` and `model_runs.py` blob hashes also independently matched the original index.

**Actual original OS evidence, separately opened and verified:**
- Both Ubuntu/Windows native original test logs: **1,629 current headless PASS**, **18 historical behavioral PASS +1 old snapshot-freeze guard deselected**, **33 real-PyVista PASS** each; original source-equivalent preview ID recorded (not a post-merge actual-main HEAD).
- Original real-viewer evidence: **9/9 offscreen/programmatic scenes PASS; 17/17 real PNG-byte SHA256 receipts PASS**. Screenshot contents were not certified by a human observer; report itself says `visual_inspection=PENDING`.
- Developer gravity original frozen raw question SHA256 `36f56dcc11d6347a1db47adfb103b16472a8e1270641869f52c7220bd086a361`, packet SHA256 `6fe25bf6c738ee13fa837793414b343feeb53116737bcfafcf19c56c36adac5d`: compared source, freeze, retained bytes and native receipts; **5/5 named native `status=ok`**.
- Public NASA **NON-BLIND** fixture question SHA `cd797751a84d86caa57c2024620215895c1414169c6682b96933e4b4cf25cc23`, packet SHA `f86211065ec99e3e82181de256d321a6ebb054f9b397440996529a3ec6ccfeda`: source and original retained/frozen bytes matched; **1/1 `exit_speed_native`** (~43,484.58452036887 m/s, saved index 20). Native report hashes are validated per OS rather than incorrectly demanding cross-OS byte-identical JSON.
- Original physics demo: **one case, 64/64 analytic checks each OS**; original per-engine SHA receipts **30/30 each OS** compared against exact reconstructed source. Windows SHA comparison correctly accounts for normal CRLF checkout of 30 engine files. Signed ensemble **E1 complete** and **G1 partial**, not falsely zero-filled or promoted.
- These checks establish recorded native measurements and package identity, **not verified source-question interpretation or independent teacher usefulness**.

## Fresh complete local suite and honest environmental failures

**Reviewer audit environment:** isolated Linux x86-64 container; CPython 3.13.5; NumPy 2.3.5; SciPy 1.17.0; pytest 9.0.2; real PyVista not installed locally. Tests run without changing published project source. Source TAR extracted from original GitHub ZIP, with only an external fresh reviewer test harness.

Actual full suite command, from extracted `pinned-source/`:

```sh
PYTHONPATH="$(pwd)/src:$(pwd)/tests" PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
  python -W error -m pytest -q
# 1629 passed in 124.74s ; exit 0
```

Earlier **independent reviewer setup failures were preserved**: first unqualified `python -W error -m pytest -q` aborted because an unrelated automatically loaded `pytest_asyncio` warning was treated as an error; second disabled plugin autoload but lacked absolute `PYTHONPATH` for spawned subprocess tests, yielding **1621 PASS / 8 FAIL**, all eight `ModuleNotFoundError: emfeeld` in child processes. Both are explicitly **harness configuration problems, not product defects**; no failed log was rewritten. Corrected third command above passed on the **same exact source bytes**.

Reviewer test commands (from `pinned-source/`, with `PYTHONPATH=src:tests` and `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1`):

```sh
python -m pytest -q /mnt/data/r2_emfeeld/reviewer_adversarial.py
python -m pytest -q /mnt/data/r2_emfeeld/reviewer_adversarial_followup.py -rx
python -m pytest -q /mnt/data/r2_emfeeld/reviewer_numerical_boundary.py
python -m pytest -q /mnt/data/r2_emfeeld/reviewer_additional.py
```

Original ZIP audit run via `python /mnt/data/r2_emfeeld/audit_originals.py` and `python /mnt/data/r2_emfeeld/check_original_evidence.py`. All first failing and later corrected logs, original reviewer test files, ZIP-check scripts, machine-readable `archive_audit.json` and `original_evidence_audit.json` are retained in the reviewer execution workspace and attached separately as **`emfeeld-pr40-chat-b-evidence.zip`** in the review conversation (SHA256 `86f25e55090fa28e0042f40cc8b54ff808893c092a180acbfc2767344346b2d1`). This report does **not** misrepresent the chat attachment as a GitHub-hosted artifact.

## Compatibility, scientific/release nonclaims, and next gate

The field implementation hash legitimately changes. Prior source-pinned studies may refuse to display under this changed code; retain historical implementation/source receipt and re-run exact inputs into **new** evidence when needed. Do not rewrite old receipts or historical failures, relax numerical tolerances, or silently coerce nonzero undefined values to zero. No new physical law was established by this patch; the concrete regression concerns arithmetic stability and existing representability limits, not the SI Coulomb/Newton sphere equations.

Not established by this R2: full textbook corpus coverage, general field correctness for all parameter scales, arbitrary-language problem interpretation, authenticated independent science questions, educational usefulness, malicious/racing filesystem security, human Windows mouse-operation qualification, or manual visual correctness. Pinned **pre-merge** Linux/Windows/viewer successes do **not** qualify actual-main push artifacts after a future merge.

**Required next action:** author correct R2-01 and review the numeric-domain decision for R2-02; resolve explicit telemetry semantics in R2-03; add cumulative regression/negative/positive cases; publish a **new corrected source HEAD/tree**, preserve these reviewer red attempts, rerun exact-source Windows/Linux/viewer and original ZIP gates, and request independent review of corrections. This R2 report authorizes **no merge**. PR #40 must remain **DRAFT / UNMERGED** pending the owner's integration decision and independently satisfactory correction review.
