# PR #47 — current-source premerge author gates complete

2026-11-18. Addendum to AUTHOR-QUALIFICATION-01.md. This closes the previously pending full OS gate; it does not alter historical pending/failure records or constitute independent review.

Exact candidate `fcf9fede87ccd37597d0ba8c9b9013ee99b764f0`, tree `65935bb395552d3dfb466a6e48d03230f18b6b66`, base `aeea3fedb00de4e20304d1f88aa038f3fac1e99e`. Original PR preview `457e2e3d79b205a7bb61fe7c4af5d9d585415d96` has the same tree and ordered [base, candidate] parents. This is premerge qualification, not an actual-main run.

## Full clean-install CI completed

Workflow **44281829329 COMPLETED SUCCESS**. Ubuntu job134724212910 and Windows job134724213752 completed successfully. Each original OS log reports **1,783 headless +18 historical (one obsolete guard deselected) +46 real-PyVista tests passed**. All subsequent evidence/negative/native workflow steps and artifact preservation completed. Counts overlap the local/focused suites; they are not additional unique tests.

| Original artifact | ID | Whole ZIP SHA256 |
|---|---|---|
| Ubuntu |14418810185|`aa8951738d38dc58e54a1fc1ec36ab685344ae1c716876cd4d39572c02a436f2`|
| Windows |14417263763|`fa28ad0ac8f34601d8bf8f5c77141d1d9d888bec40271b2e393055f3b3647b76`|

Both original archives were downloaded and audited read-only:2,186 unique safe paths, valid ZIP CRC, correct original preview head-sha,173 integrity inventories and1,750 hash references each. Exactly1,749 references match; the only mismatch is the known deliberately altered negative at `derived-001/G1/review-challenge-resealed-native/native/result.json`, retained as a negative, not certified as intact evidence. All34 native implementation-module receipts match the exact source (Windows CRLF represented in memory only). The old physics demonstration remains17 valid native observations with64 reference checks. E1 signed ensemble readout is complete and G1 remains partial; no partial result was promoted to complete.

## All five exact-source workflows now successful

Full Linux/Windows44281829329; dedicated Gauss lesson44281828953 (83 overlapping focused tests,eight retained scenes); existing viewer44281828951; conductor lesson44281829138; source snapshot44281829140. All six original archives (two OS plus Gauss,viewer,cavity,source) have been downloaded and audited. See report01 for their individual digests and source/image checks.

## Review checkpoint, not a release

The implemented milestone is now ready for the prepared **independent R2 physics/graphics review**. PR47 stays DRAFT/UNMERGED. No independent review, manual Windows operation or teacher acceptance is asserted. Do not stack another physics feature or merge before the independent gate. After any accepted review and exact-head guarded integration, fresh actual-main qualification and new original artifact audits are still required. Main and its382 baseline files have not been modified by this PR.
