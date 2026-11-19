# Opticsim PR #177 — builder erratum addressing independent review B1

**Date: 2026-11-19. Builder correction, not an independent clearance or merge authorization.**

This erratum supersedes the incorrect provenance statements identified below in [BUILDER-VERIFICATION-01.md at its preserved historical commit](https://github.com/physicsvigilante/review_sandbox/blob/95b90bbd06a43506f8a2d32f341addc460788de8/projects/opticsim/pr-177/BUILDER-VERIFICATION-01.md). The original report, original CI artifacts and independent review are retained; no Opticsim source change is part of this correction.

The [published independent Chat B review](https://github.com/physicsvigilante/review_sandbox/blob/132d7d668e602360d0ea68e8a2f68b45e0cafc41/projects/opticsim/pr-177/reviews/review-01-chat-b.md) reviewed source `f981be4750f60a6bd5a9f5fc0fb003e82013a5a9` and records **CHANGES REQUESTED** for B1, the builder's incorrect Git-tree identity. It finds the declared physics, numerical guards, native archived witnesses and research/public separation satisfactory within their limited scope. Its verdict is not edited or relabelled by this erratum.

## 1. B1 — corrected immutable identity

The builder re-read BOTH GitHub Git commit objects after receiving the review. They return:

| Object | Actual identity |
|---|---|
| Reviewed source commit | `f981be4750f60a6bd5a9f5fc0fb003e82013a5a9` |
| Source Git tree | **`df49aa4114479ac2462bfa67682b4c9b6ef3e37b`** |
| CI synthetic merge commit | `f39a7240bab504af348dcb0e93af946f4ea6851d` |
| Synthetic merge Git tree | **`df49aa4114479ac2462bfa67682b4c9b6ef3e37b`** |
| Synthetic merge first parent / main | `f0235bc5dabce50df81192d4fd7807c62cab4edd` |
| Synthetic merge second parent | `f981be4750f60a6bd5a9f5fc0fb003e82013a5a9` |

Primary reads: [source Git object](https://api.github.com/repos/physicsvigilante/opticsim/git/commits/f981be4750f60a6bd5a9f5fc0fb003e82013a5a9), [synthetic merge Git object](https://api.github.com/repos/physicsvigilante/opticsim/git/commits/f39a7240bab504af348dcb0e93af946f4ea6851d), and [main branch ref](https://api.github.com/repos/physicsvigilante/opticsim/git/ref/heads/main).

**The prior claimed tree `0475daae3f1fd028a6672e243635eb2c67993961` was incorrect and is withdrawn everywhere it was presented as the governing source/merge identity.** The actual source and CI trees are identical. The PR head, reviewed source and main base remain unchanged; this is a correction to my report, not a source or binary substitution.

**Additional provenance clarification:** the old report also said the optical CI log explicitly checks tree equality. That attribution is withdrawn. The job log identifies the synthetic-merge checkout; the equality is established by the separate Git-object reads above. No new in-job tree assertion or CI rerun is claimed.

## 2. Browser-version correction, tied to unchanged artifacts

The historical report's Chrome `157.0.8103.50` is incorrect for this final run. The actual recorded version is **Google Chrome 157.0.8103.78**.

Both browser archives were downloaded again and SHA-256/CRC-checked. Their `report.json` files directly contain that version:

| Artifact | ZIP SHA-256 | Archived report |
|---|---|---|
| [14535213201 — browser acceptance](https://github.com/physicsvigilante/opticsim/actions/runs/44535274231/artifacts/14535213201) | `2e6b1c8c8d52745b42e090d0a35e1a5763de651adf9782395a1db03e6af5df41` | 27/27 checks pass, 15 screenshots listed, no recorded errors |
| [14535542834 — hosted smoke](https://github.com/physicsvigilante/opticsim/actions/runs/44535274231/artifacts/14535542834) | `29d7575f474525e42202236a931df5ddfc6c7e34cd6cd01d0705c92d5869982e` | 5/5 checks pass, one screenshot listed, no recorded errors |

The browser `report.json` SHA-256 is `7aa4705852cfc7333f5a34926e9893997a4184e158855e6f247edaec6228171f`; hosted `report.json` SHA-256 is `6f0151728d1dd1f04066419138d9f671bf4975793cfef562e45c8d0e78db2654`.

## 3. Existing execution evidence retained and rechecked

All **11/11 existing PR workflows** still report success for the unchanged source. The existing [optical run 44535274231](https://github.com/physicsvigilante/opticsim/actions/runs/44535274231), job `135598887701`, contains the previously recorded **938/938 passing Node tests**, not a new run performed for this correction.

GitHub artifact metadata still associates the final artifacts with that run and source head. The retained native artifact `14535373214` was rehashed locally to `38b309f328c523485ae90049b9cb16a761d76e513bb1d9da99f73049aea445a2`, matching the fresh GitHub metadata; its ZIP CRCs and all 31 raw-native-input hashes pass. Its classification remains 25 usable raw single-crossing witnesses, including one axial case without an identifiable intercept, and six excluded controls. No physics execution or second independent native replay is claimed by these file checks.

For exact transcription, two overly precise displayed numbers in the old report are also superseded by the literal final-archive values: the h=0.25 mm 1-to-4/3 entry intercept is `399.99929687411924` mm; the h=0.25 mm 1.5-to-1 entry intercept is `-199.99859374615662` mm. These are mathematical extrapolations of detector points, not detected images. Their rounded errors and the physical conclusions are unchanged.

[Machine-readable correction record](https://github.com/physicsvigilante/review_sandbox/blob/47dcc729b48ebb4a6db20d8f88ed14edcaa4d9b8/projects/opticsim/pr-177/BUILDER-CORRECTION-01.json) records the actual source/merge identities, artifact/report digests, review identity and limited remediation scope.

## 4. Review disposition and release boundary

B1's requested metadata correction and the minor browser-version correction are implemented by this erratum and the corresponding corrected PR handoff. Publication must be verified by reading both committed files and the updated PR text back from GitHub.

The independent review explicitly states that this metadata-only correction does **not** call for a new source commit, rerunning otherwise valid CI, repeating v22/v23 review, or creating a second independent physics review while the source/artifact identities remain unchanged. The two nonblocking future-hardening observations (duplicate JSON keys and near-axial research-intercept conditioning) are retained as future scope considerations, not silently advertised as fixed.

**Original reviewer verdict remains CHANGES REQUESTED.** This is builder remediation of its specified evidence defect, not a forged independent CLEARED verdict. PR #177 remains draft/unmerged pending acceptance of the correction and the owner's release decision. The reviewed source is unchanged; no production merge, upstream edit, public deployment or additional native authoring capability is introduced.
