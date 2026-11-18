# M36c PR #86 — Targeted second independent R2 science/source-fidelity review

**Production source PR (DRAFT/OPEN/UNMERGED):** https://github.com/physicsvigilante/conductor_sim/pull/86

**Exact source HEAD:** `82de04484006d61f691e1e3a1344f5707729a821` · **actual native Git TREE:** `c43134db1726dc2f1ff48b0b9a560dff090bf56d` · released M36b base/main: `5693aaa4fca42fa996fd0983b95c8a104a45af93`.

**Frozen original charter-only commit:** `8ad08a0971fc1a703ac1fa2cb372eb949fff79c8`. The old charter remains frozen even though the original notes p27 source interpretation in the initial implementation was wrong; the correction and limits are explicitly documented in the candidate `docs/m36c.md`. No original PDFs, production physics, FEMM, browser renderer, M6 historical benchmark or M36a source matrix changed.

### Prior independent review is NOT PASS

Read the original scientific [Chat B review #01 in review_sandbox PR #1](https://github.com/physicsvigilante/review_sandbox/pull/1), source branch `review/conductor-m36c-chatb-r2-01`, original [review-01-chat-b.md](https://github.com/physicsvigilante/review_sandbox/blob/review/conductor-m36c-chatb-r2-01/projects/conductor_sim/pr-86/reviews/review-01-chat-b.md). It inspected **actual original PDF images** and conducted three unfamiliar live conductor physics worlds plus 60 SI/refusal probes. It returned **CHANGES REQUESTED** for source fidelity (old p27 off-centre “source” didn't measure V(A)/V(B), old p26 undeclared hollow proxy for printed solid) and three real saved-evidence false accepts (p69 near/far `theta_rad`, p27 wrong `conductor`, p27 forged `source_anchor`). The original review finding and first source failures must remain visible; old source `1f5bd9fcee30f534e15f874c87f8ff0441a62fe8` with tree `b31fd1843b57de5403d2a36b2cb86fa1385f659a` and **19/19 old CI SUCCESS** does NOT certify any new change.

See [Chat A correction and bounded execution evidence](responses/response-01-chat-a.md) for exact correction provenance; **do not trust it blindly**.

### Inspect corrected source at literal SHA/TREE

- [M36c replay producer](https://github.com/physicsvigilante/conductor_sim/blob/82de04484006d61f691e1e3a1344f5707729a821/tools/m36c_jee_conductor_replay.py)
- [Separate no-engine-import SI checker](https://github.com/physicsvigilante/conductor_sim/blob/82de04484006d61f691e1e3a1344f5707729a821/tools/m36c_jee_conductor_reference.py)
- [Adversarial focused tests](https://github.com/physicsvigilante/conductor_sim/blob/82de04484006d61f691e1e3a1344f5707729a821/tests/test_m36c_jee_conductors.py)
- [Real offline Chromium checker](https://github.com/physicsvigilante/conductor_sim/blob/82de04484006d61f691e1e3a1344f5707729a821/tools/check_m36c_conductors_browser.py)
- [Documented known textbook mismatches and correction](https://github.com/physicsvigilante/conductor_sim/blob/82de04484006d61f691e1e3a1344f5707729a821/docs/m36c.md)
- [Original fixed cohort charter](https://github.com/physicsvigilante/conductor_sim/blob/82de04484006d61f691e1e3a1344f5707729a821/docs/m36c_charter.md)
- [M36a 30 apparatus / 29 original workbook anchors](https://github.com/physicsvigilante/conductor_sim/blob/82de04484006d61f691e1e3a1344f5707729a821/docs/m36a_jee30_coverage.json)

### Required independently authored tests and scientific conditions

**F-01: Actual printed p27 V(A)/V(B).** Original `POTENTIAL_CONDUCTORS1.pdf` physical p27 Illustration 4 has **CENTRAL point q** inside concentric charged shells q1/q2. A is in central cavity and B in intershell vacuum gap. Original formulas:
[
V(A)=k(q/r+q_1/a+q_2/b),qquad
V(B)=k((q+q_1)/r_1+q_2/b).
]
The corrected source FIRST state authors real central q and calls `NestedShellBackend` `potential_at` at separately labelled teacher numeric A r=.04m and B r1=.15m. Compare actual **finite metal thickness** (1µm) to independent Gauss face charge formula; do not demand exact equality to ideal infinitesimal shell formulas. With teacher values q=1nC, q1=2nC, q2=3nC, a=.10m, b=.20m, ideal V(A)≈539.2531075 V vs actual 539.2515347 V; ideal V(B)≈314.5643127 V vs actual 314.5636387 V. The **SECOND** state is a separately marked TEACHER off-centre q at z=.02m, never a valid original A/B formula. Verify in actual source viewer HTML that teachers visibly see original V(A), V(B), ideal formula comparison, original/teacher state distinction, not just an invisible detached manifest. Independently vary q, q1, q2 or observation points in a true admitted model, predict before looking at native output, and inspect actual source screenshots if possible.

**F-02: Solid original vs hollow visual proxy.** Notes p26 Illustration 1 has a **SOLID** conducting sphere. Existing historical `pdf_benchmark` example draws a 0.09–0.10m hollow metal shell. The corrected M36c intentionally **DOES NOT change that production representation or claim it is a literal solid**; it explicitly labels the hollow drawing a limited **radial potential/field observer-equivalent proxy** for only V(R/2), V(3R/2), E=0, with the actual source SOLID and hollow cavity **NOT part of the source**. Check the visible HTML notice `id="original-solid-sphere-proxy-disclosure"`, the strict `source_shape_fidelity` metadata and sample consistency. If a visually literal original solid is scientifically essential to PASS, flag as a specific remaining scope limitation rather than silently misclassifying the proxy as a solid.

**F-03: Three real attribution forgeries.** On authentic **new corrected source** native results, mutate p69 `native_observations[5/6].theta_rad` to swapped near/far 0/π while retaining true magnitude, p27 original named inner-shell result `conductor=outer` with unchanged number, and p27 `source_anchor="Unrelated illustration"`. All **must reject** in independent source-free checker. Independently attack wrong observation point, shuffled A/B, forged central source z=.02, or false source PDF illustration. Confirm original correct values pass. p69 angular `theta_rad=0` is near side, `pi` far side; charge total observers do not carry a defined angular theta.

**Actual separate source-first developer acceptance, not independent reviewer result:** [review_sandbox source-pinned run #44264857366](https://github.com/physicsvigilante/review_sandbox/actions/runs/44264857366) completed **SUCCESS** on literal `82de04484006d61f691e1e3a1344f5707729a821`/`c43134db1726dc2f1ff48b0b9a560dff090bf56d`: 30 new focused tests, seven original static conductor apparatus and eight source-question anchors, seven independent-form SI math references, seven real offline Chromium views with actual A/B and p26 disclosure, and two non-success controls. Evidence artifact **14409961298**, provider-reported ZIP SHA256 `1ee9bf592cdcd7760647bea39a6c8f53c9d9278f022dfd4a706d0b3581e29719`, **NOT independently rehashed** by Chat A. Reviewer should independently verify the actual run and author/execute original new physics/refusal probes rather than infer independence from this developer-controlled job.

**Full source-head CI mandatory before PASS:** Python 3.10/3.12, real FEMM5, full 73-step historical Chromium, prior M36b scientific regression and new M36c native/reference/browser workflows. They were **QUEUED / IN PROGRESS** at this request's publication. Check live exact HEAD and actual native Git tree; any head move makes this reviewer packet STALE. Do not claim 19/19 current-source green unless they really finished; the 19 old-green refers to earlier source.

### Original reviewer-report and release authority

Publish an ORIGINAL separate-context R2 report at `projects/conductor_sim/pr-86/reviews/review-02-chat-b.md` in `physicsvigilante/review_sandbox` (direct main write or a separate review PR). Include exact source HEAD and native TREE, independent new physics and hostile tests, source PDF page reading actually accomplished, actual Chromium/visual assessment, first failures and original review #01 CHANGES REQUESTED, and **PASS / CHANGES-REQUESTED / INSUFFICIENT-EVIDENCE** scoped to original conductor source interpretation and evidence. Do **not** edit source production, mark PR ready, merge or grant owner approval.

**After** an exact-source no-blocker R2 PASS, Chat A still needs **separate explicit owner merge approval** and expected-head guarded merge with the identical reviewed source Git tree on `main`, followed by all actual postmerge `main` push workflows completed success.

Selected **seven** conductor apparatus and **eight** historical linked question anchors plus two honest partial/refusals are not a statistically justified 7/30 or 8/30 exam solved rate, nor a general irregular conductor 3D, wire-current-time or automatic PDF-to-simulation capability.
