# SIM_HEAT PR #65 — independent Chat B R2 review-02

**Verdict: SCOPED PASS** for the two N4 checking-only admission corrections **R2-01** and **R2-02**, at the exact corrected source HEAD. **This is not a native qualification, reference-adoption approval, or merge approval.**

**Reviewed:** 2026-11-19  
**Source PR:** https://github.com/physicsvigilante/sim_heat/pull/65 (DRAFT / UNMERGED)  
**Exact corrected HEAD:** `f533d10fd38dc38710bba223e0bdb88f264e4398`  
**Documented complete source tree:** `a83cfce4fa303bbf173b6b0e387e9734cb3c5f8b`  
**Old rejected HEAD:** `a704e100d6760423b08cb07eca131ada8a629db2`  
**Fail-first tests-only HEAD:** `b11bfccf06f352ab6b93c57e8effa752e7519f4f`  
**Stacked PR64 base:** `0cf275241e718fbcd2b2d2c1f7761565c7c06a92` (DRAFT / UNMERGED)

## Scope and identity checks

I followed [REVIEWER-PROMPT-02](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-65/REVIEWER-PROMPT-02.md), read the complete [CORRECTION-REQUEST-02](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-65/CORRECTION-REQUEST-02.md), the historical [independent review-01](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-65/reviews/review-01-chat-b.md), [response-01](https://github.com/physicsvigilante/review_sandbox/blob/main/projects/sim_heat/pr-65/responses/response-01-chat-a.md), and examined the new N4 source, new tests, README, and production `h1/model.py` identifier grammar at the pinned SHA.

* GitHub PR metadata independently returned `head_sha=f533d10fd38dc38710bba223e0bdb88f264e4398`, `draft=true`, `merged=false`. Comparing old reviewed SHA with corrected SHA gives **two commits and exactly three modified N4 paths**: `qualification/h1_n4/static_physical.py`, `qualification/h1_n4/tests/test_static_physical.py`, and `qualification/h1_n4/README.md`. The intermediary `b11bfcc...` changes **only** the tests; the final `f533d10...` source patch adds physical port incidence and reserved component-name checks (plus documentation), without changing the `_constant`/C/G/A calculation or evidence-status fields.
* I reconstructed the **exact 14,622-byte / 303-line** corrected `qualification/h1_n4/static_physical.py` in an isolated local Python-only inspection directory and verified its Git blob hash: **`03f235f4d47fdbd576c7e5966c90c0223d77369b`**, matching GitHub's fetched blob for the pinned HEAD. The separately computed file SHA-256 was `f7b356e8c42dc356b52817514cdf3a053f16d0da3247145ff182eed4a4939fba`. Thus the personal tests below executed the actual corrected source, not a behavioral rewrite.
* The original review-01 remains a **CHANGES REQUESTED** result about the **old** SHA. I independently fetched its Git blob `0a2f14619da7e2017446171cba279df65ffebdd4` before publication. This report does not amend or supersede that historical verdict for the old commit.
* The recorded whole-tree SHA is from the review packet/status; I did **not** independently recompute the entire repository tree or download/rehash CI artifact ZIPs. The PR's exact head, source blob, changed-file scope and workflow identities were checked directly.

## Independent executed probes: 40/40 PASS

I wrote **40 independent adversarial/positive offline cases**, each using newly serialized `sim_heat.reference/1` JSON bytes with its own SHA-256, invoking the pinned `create_static_candidate` and checking both admission outcome and returned status fields. These were not the developer's N4 test functions. **40 passed, 0 failed.** No OpenModelica query, installation, build, launch, native simulation, reference generation or repository source edit was performed.

### R2-01 — ownerless physical rod-port incidence: CLOSED

**Source anchor:** [`static_physical.py` lines 116–160](https://github.com/physicsvigilante/sim_heat/blob/f533d10fd38dc38710bba223e0bdb88f264e4398/qualification/h1_n4/static_physical.py#L116-L160), with connectivity anchoring at [185–201](https://github.com/physicsvigilante/sim_heat/blob/f533d10fd38dc38710bba223e0bdb88f264e4398/qualification/h1_n4/static_physical.py#L185-L201).

The code initializes a count for every declared node and increments **once for each physical endpoint of each rod**, after verifying both endpoints exist and differ. Every node not owned by a body or fixed-temperature boundary must have at least **two real rod-port incidences**. Existing `used==nodes`, boundary-connected and component-anchoring checks remain in place.

**Six negative probes refused as required:** a steady thermostat→dangling area rod; a transient body→dangling circular rod; two disconnected anchored assemblies with a dangling port only in the second; a connected transient branch with a third rod ending at a free degree-one node; an unanchored closed loop alongside a valid anchored circuit; and a self-connected rod that might otherwise try to manufacture two endpoint counts. The first four failed specifically with `open ownerless rod end`; the unanchored loop and self-rod failed by the relevant existing guards.

**Six positive probes admitted as required:** a genuine degree-two serial junction; **two parallel rods** with the same two endpoint nodes (two physical ports, only one distinct neighbour); an anchored three-rod closed loop; a branched degree-three junction with an additional back edge; a transient assembly plus an isolated body; and an isolated transient body with no rods. Each returned only its expected C/G/A candidate export names.

**Conservation implication:** Distinct-neighbour graph degree would incorrectly treat the valid two-parallel-rod junction as one connection; counting real rod ports avoids that mistake. Conversely, accepting a single ownerless rod port would silently admit an open connector forbidden by the H1 connection contract. The new check closes that admission gap without inventing an insulating boundary or claiming that N4 itself solves junction energy conservation. A body- or maintained-boundary-owned node is correctly allowed to have a single rod port.

**R2-01 finding:** No blocker or unexpected refusal found in this scoped attack. **PASS.**

### R2-02 — Modelica-reserved component names: CLOSED

**Source anchor:** [`static_physical.py` lines 20–34, 76–82, 119–125](https://github.com/physicsvigilante/sim_heat/blob/f533d10fd38dc38710bba223e0bdb88f264e4398/qualification/h1_n4/static_physical.py#L20-L34) and [H1 `h1/model.py` production identifier rules](https://github.com/physicsvigilante/sim_heat/blob/f533d10fd38dc38710bba223e0bdb88f264e4398/h1/model.py#L25-L49).

I compared the complete **66-element `COMPONENT_RESERVED` set** against the set specified in the pinned production `h1.model.RESERVED` source: **exact parity**. `_component_ident` is called on each body, boundary and rod **instance name** before insertion in the cross-group component-name inventory; `_ident` remains in use for metadata `id` and graph node labels.

**Twenty-one negative probes refused:** each of `model`, `flow`, `SimHeat`, `time`, `class`, `Real`, and `false` used separately as a **body name**, **boundary name**, and **rod name**. All returned `PhysicalRefusal` for invalid/reserved component identity. Cross-group duplicate component names also still refused.

**Five positive identity controls admitted:** metadata `id=flow` with graph node `model`; metadata `id=model` with graph node `flow` and legal case-sensitive component `Model`; ordinary component `CustomConductor`; uppercase `MODEL` (not a reserved production identifier); and a conventional rod with `id=flow`. I also verified a normal candidate retained its non-native flags. No artificial restriction was introduced on synthetic node labels or study metadata.

**R2-02 finding:** No reserved-word bypass or metadata/node false refusal found in this scoped attack. **PASS.** The standalone set remains a synchronization dependency, but the committed parity regression test addresses drift; no change is required now.

## CI cross-check and preserved boundaries

I independently fetched the two GitHub Actions job records and decoded job logs:

* [Corrected PUSH CI 44512437693](https://github.com/physicsvigilante/sim_heat/actions/runs/44512437693): job `checking-only` **SUCCESS**, on exact `f533d10...`.
* [Corrected PR CI 44512447651](https://github.com/physicsvigilante/sim_heat/actions/runs/44512447651): job `checking-only` **SUCCESS**, using synthetic merge `ad37f358dce61d53a98e879cde15ba8a75787e74` whose recorded second parent is exact `f533d10...`.
* Each decoded log reports test-suite totals **15 N4 + 12 N3 + 16 N2 + 17 N1 interval + 34 N1 plan + 152 H1 = 246 distinct offline tests**, all OK. These are **the same 246 test cases run twice**, not 492 distinct cases, and are hosted CI evidence rather than the 40 tests personally executed here. The original first-red run `44512178952` is preserved as fail-first historical evidence, not retrospectively called green.

The output schema remains `sim_heat.h1_n4.static_physical_candidate/1`. In personally admitted samples I checked `nativeExecuted=false`, `nativeQualified=false`, `runtimeReady=false`, `referenceBundleWritten=false`, and `independentlyCertifiedReference=false`; inspection confirms the remaining native/certificate/general-dynamics/owner-approval fields are still explicitly false. No source patch touched the rational Pi, RN-even binary64 or 0.64-ULP mathematical budget routines, so I **inherit, without re-proving**, the numerical observations in the first independent review.

The **seven original legacy physical-100× checking-centre refusals** and **eight native readiness blockers** are documented in the prior review and retained by the published offline regression gate; I did not independently rerun the old N1 plan or rehash native evidence in this narrowed review. These defects/holds are **not resolved or authorized away by a scoped N4 admission PASS**. Original T1 source digests and the unsealed private scorer remain outside this correction.

## Decision and limits

**SCOPED PASS — R2-01 and R2-02 are adequately corrected at `f533d10fd38dc38710bba223e0bdb88f264e4398`.** No further N4 admission change is requested based on the inspected source and independent probes. This is permission to record **targeted correction-review closure only**, subject to the project's existing release gates.

This is **not** independent certification of all physics, source authenticity beyond caller-supplied hash, full 77+8+5 dynamic evidence, native execution, compiler/MSL behavior, externally trusted reference seals, unfamiliar LLM-authored composition qualification, or runner readiness. **PR65, PR64, PR63, PR62, PR60 and PR59 remain draft/unmerged; no merge, reference promotion, historical C1 rewrite, OpenModelica operation, or production deployment is approved.**

**Publication discipline:** new `reviews/review-02-chat-b.md` only; historical `reviews/review-01-chat-b.md` must retain its original content and blob.
