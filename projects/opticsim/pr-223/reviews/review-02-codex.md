# Opticsim PR #223 independent focused review R2

**CLEARED for owner-authorized integration at this exact candidate.** All three numerical blockers in the single-mirror query are resolved.

| Identity | SHA |
|---|---|
| Candidate | `e887d868d8023472585c83b4cc771f3cdf0773ac` |
| Candidate tree | `c665bb720785d6c29153de948dc19e51b437e2db` |
| Production base | `3313624ae9173ebf8dad738ac27f246e235389a9` |
| GitHub PR test merge | `a4b1b526d8b60e7ef77dab573ecf9dedb0ed6369` |
| PhyDemo pin | `811f508d2b070898c241a568b0c167dcb8645251` |

The PR test merge has the corrected head and production base as parents and exactly the candidate tree. [Initial blocked review](https://github.com/physicsvigilante/review_sandbox/blob/c9ec2a94625983fd97b257406a1b5036de29961f/projects/opticsim/pr-223/reviews/review-01-codex.md).

## Source and analytical scope

I read the two original Problems images. Their SHA-256 values match the frozen record: A01 `bc419ed8858e6674a6b1061c0387f8e19ff6e12508b5991af5411d4da3be35c5`, A02 `d8c5dfb3c70b0dcf4462414faf807c2313405811f35656738a89235737d43e36`. Solutions stayed unopened. A01 gives two directed headings and asks for incidence from the normal, yielding 30°. A02 supplies two crossed parallel line relations and the order of reflections. The acute inclination is 60°. Its principal heading change has magnitude 120°, while the two local turn magnitudes total 240°. The result preserves these distinct measures and the signs of each directed branch.

For a first mirror tangent at 0° and second tangent at θ, the crossed endpoint relations imply 3θ = q−p modulo 180°, with p,q each 0° or 90°. I independently enumerated the orientations, checked all vector reflections and signed turns, and confirmed the perpendicular and parallel cases yield four accepted directed branches per relation pair. The perpendicular-line orientation that grazes one mirror is excluded. The result is conditional on finite interception in the requested order.

## Numerical correction

The exact raw dot and cross products supply the scale-free grazing test. For a positive dot product, the stated squared chord cutoff is equivalent to comparing the squared dot with the exact squared cosine threshold times the product of squared norms. The acute normal comes from the perpendicular to the large sum of the normalized headings; the obtuse normal comes from their large difference. Incidence is evaluated directly using the complementary atan2 arguments, with finite-ratio scaling and explicit withholding below the qualified resolution. The original grazing-band input is withheld, the admitted near-grazing normal reproduces its near-parallel headings, and the tiny positive incidence near normally opposed headings stays positive.

I independently checked 1,407 direction pairs across both sign regions, exact and near grazing, exact and near normal, and a 10¹⁶ range of relative vector scales. Of these 1,193 qualified and 214 withheld. Each qualified normal reproduced the outgoing unit heading, with a maximum Euclidean residual of 1.08e−15. The independent incidence reference agreed within 1.43e−14 degrees.

## Native and hosted evidence

- The five frozen runs passed independently and in hosted CI. Each uses actual pinned finite Mirror callbacks and native absorption by a finite Blocker. A01 observes 30° incidence. The four A02 orientations and headings observe the two contacts in the stipulated order and reach their declared target.
- I separately traced 16 finite native controls, one for each directed two-mirror branch across the four parallel/perpendicular combinations. Actual headings, contact order and final native absorption matched in each synthetic control. These controls establish the observed finite outcomes for their authored arrangements.
- Independent execution passed 18 focused A01/A02/A04 tests and 30 historical mirror/A08/A07/A09 checks. Both normal CLI runs returned conditional analytical results and native status `not-run`. Local report SHA-256 values were A01 `9b65ff2c9530cc9d4e59e86667d02a2b2ea5ad0786a76d25ca5834542201d651` and A02 `ff854af15eb4d4f59358fb7c57cee3eb5c7ec0ae142334c0e27aa6bd44f1b444`.
- All 11 exact-head workflows passed. The [optical composition job](https://github.com/physicsvigilante/opticsim/actions/runs/44875592813/job/136759478147) recorded 1,308 passing Node tests, including the five A01/A02 native assertions. The [hosted authoring archive](https://github.com/physicsvigilante/opticsim/actions/runs/44875592813/artifacts/14695648283) matched SHA-256 `6a2bd64ddb38a2bb6a2c4c2fff027e1e918e2a04a529cf418c5620c314fc0d63`. All 35 inherited A04/A08/A07/A09 records matched the independent replay byte for byte. The A01/A02 comparison uses the exact hosted test log and separate native and CLI replays because those tests do not emit records into the hosted archive.

The release verdict applies to the exact reviewed source. Integration and post-merge verification remain separate gates.
