# PR #122 — held v18 physics + directional detector footprint integration

**Research-only source-CI verified, independent integration review NOT YET RECEIVED. DRAFT / UNMERGED / NOT RELEASED.**

Exact source HEAD `70cf502d19e243e4a8d7d1e0795f008c101c582d`, tree `df9282da11ff416d0033cdf7e09509ba8dc24bc9`; synthetic main-target CI merge `1ec478b5a84dcae89a23e613103f7b98f9bc1f6c` has identical tree. Correct PR dependency base restored to held `feature/native-thick-lens-aperture-v18`. Neither original reviewed source was changed.

All **865/865 Node tests and 11/11 standard workflows** passed exact-source CI, including **5/5 public detector-footprint CLI acceptance cases**, **7/7 real Chrome footprint checks**, **13/13 v18 native aperture Chrome checks**, and four new combined native tests. True v18 return has one real native crossing per signed group, N=1 and sample RMS=0 (not an image). Aperture blocking yields no crossings with N=0 and null centroids/RMS. Shallow incomplete trace suppresses both derived and original samples. Standalone footprint-only request correctly captures existing hits.

First attempt failed because the independent v18 viewer's historical source blob SHA was not the combined app blob; fixed in research branch only by adding a separate integration source pin and preserving both original feature viewer pins and the historic R1 freeze. No physics or native cutoff code changed.

[Review request](REQUEST.md) · [Ready-to-paste Chat B prompt](REVIEWER-PROMPT-01.md). Chat B report pending. No release authorization or independent PhyDemo re-execution is claimed.

**HOLD** all dependent/unrelated PRs #107, #110, #113, #116, #118, #119, #120, #121 and this research-only #122. #120 original v18 physical R2 review is still a separate pending requirement.
