# SIM_HEAT PR #43 — Chat A disposition of independent R2 review-01

**ACCEPT SCOPED PASS** for exactly the **UNTRUSTED OFFLINE stale-snapshot in-memory CAS differential**, at [draft PR #43](https://github.com/physicsvigilante/sim_heat/pull/43) source `4e220a152e702c06b07320850f5caacff1091bb3`, Git tree `4a931c0e017eb650c0b4a63c5dfdf38097ad9d72`, immediate independently reviewed PR #42 source `32cbb7d02b7db0cbc322fb0e7826861fd902a77a`.

[Independent Chat B review-01](../reviews/review-01-chat-b.md), immutable initial report Git blob `d419f7a18b279c4d893d9ec8e0d77bfefb282544`, **SCOPED PASS** at that exact head. Preserve it as an independently-authored review and do not alter its claims. Source PR remains **draft/unmerged**.

## Finding disposition

- **F-01 — PASS for one fake Python object:** a versioned, in-memory `threading.Lock` checks a pre-claim epoch/version/consumed flag together; 16 threads using one stale object yield 1 fictional first claim and 15 refusals. Independent reviewer repeated the *algorithm* in disposable RAM using a barrier (500 ×16 trials), not the exact repository code or a real external CAS.
- **F-02 — PASS as a pedagogical non-atomic counterexample:** two fictional readers reusing one unchecked `already_claimed=false` observation can both logically accept; the source models a double claim without a real interleaved external write schedule.
- **F-03 — PASS, critical real-world limitations:** two separate fake stores can each claim first; reset permits a new claim even when an old epoch is refused. Both prove **lack of a protected, shared, durable cross-host owner-controlled one-shot reservation**.
- **F-04 — PASS within one fake only:** simulated acknowledgment loss after a fake commit retains a consumed flag and refuses the stale retry. It does not prove any native effect, real network behavior or recovery guarantee.
- **F-05 — PASS for denial/absence:** malformed snapshot types/versions and nonnative flags refuse, real native permission always raises `CASRefusal`, and inherited PR41 readiness audit still reports **11 missing** essential owner/release/host/adapter/external-store/pre-native gates. All actual OMC version/build/launch/retry budgets remain integer zero.
- **F-06 — MINOR / nonblocking, explicitly retained:** a copied well-formed fake snapshot's epoch/version has no provenance or owner signature. `validate_receipt` checks literal-false authority/budget fields but does **not authenticate** `status`, `fakeCounts`, prior reviewed source label or origin. Treat the routine as a **denial-field consistency check**, never an authenticated evidence receipt. Consider follow-on negative probes for copy/replay and modified fake status/count; these cannot replace an independently protected real store.
- **F-07 — PASS exact original-source/CI only:** exact [CI #44051422673](https://github.com/physicsvigilante/sim_heat/actions/runs/44051422673) completed SUCCESS; [artifact #14313149095](https://github.com/physicsvigilante/sim_heat/actions/runs/44051422673/artifacts/14313149095), ZIP 30,078 bytes SHA-256 `00d70f397c6e05fd5746583390c92fae3970e635684abb7bac2b99e24958d46c`, 44/44 CRC-valid, **309/309 hosted OFFLINE unittest methods** pass. Original 14 F0 frozen SHA inputs and 23 native-plan source SHA pins retained, original saved PR31 archived scientific reference untouched. No OMC or native observation.

## Scientific/historical status unchanged

Original frozen F0 `hotLead.G` mathematical accuracy margin **80× vs required ≥100× FAIL** remains. PR32 cross-host bitwise regeneration of the reviewed saved PR31 V2 seal **FAIL** remains; alternate seal never adopted. Approved *offline-checking-only* original saved PR31 scientific raw SHA-256 `0db511dd8dba023d16518667de256029cf3e073463ea21e2478aeac8afd1f368`, canonical seal `d2b8e2ca8e1f929cac7b028dcc3f7d0b453921d193f877eb091e23ac70aa4ce9`, original first-author model/study and frozen runner/checker remain byte-preserved. The nine actual C1 native public readings are still `not_computed`.

## Next bounded milestone and permanent hard stops

Advance **only** an offline, read-only **native-result evidence intake firewall**, requiring provenance/owner/host/source/plan/native-artifact policy and refusing missing, partial, mutable, forged or untrusted evidence. Do **not** claim this firewall can authenticate unknown external sources, create observations, call OMC, issue permission, grant real release or certify native qualification. Publish any new evidence-semantic source as a separate draft PR and R2. Incorporate F-06 as an explicit negative test where relevant.

All **11 real native-release requirements** remain genuinely open: protected owner-authenticated source/release and durable backup, fresh trusted ref, independently reviewed nonregenerating executable adapter and plan, actual observed OMC/MSL/host/runtime, owner-controlled shared durable atomic store, no-retry crash/failure receipt, independent pre-native R2/post-native policy and a **separate explicit owner authorization for the named compiler-query/build/one-launch budget**. No native action or merge is permitted.

**Disposition:** PR43 SCOPED PASS for fake-only counterexamples; native F02 HOLD; historical source PR draft/unmerged.
