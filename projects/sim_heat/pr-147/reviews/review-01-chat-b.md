# Independent Chat B review of PR 147

**Verdict — the PR 145 finding is resolved for the offline furnace lesson.** Reviewed base `bd56b85b5902e7bd1c6e33c2c78addc7a1d04f0b`, head `cf35295c50be2da136bbc7f8e81072bb5021264a` and request commit `ba6dfdfedd30df05539ac6680c6d2a143fd08fde`. GitHub returned that base and head and an open draft PR. [Source diff](https://github.com/physicsvigilante/sim_heat/pull/147/files)

## Substitution checks

I ran the exact-head replay with independent wrappers around its real solver. Flattening both slopes raised the material mismatch on case three. Restoring the requested slope metadata after flat solves passed the midpoint case and failed on the fourth case's face-temperature or signed-flow check. Setting the repaired contact record to 7 K/W failed on case two. Replacing only the second panel's facts hash failed the source check. Dropping that panel tripped the strict layer-count check. The two lesson and two radiating-stack unittest methods passed. An initial temporary-directory lookup failed before loading the test modules. I reran from a persistent extraction of the pinned Git archive.

## Fourth case

I derived 4, 1 and 3 W/K from the facts file's kA/L values, giving each panel a reference conductance of 2 W/K. I solved inward from a trial surface temperature using 70-digit decimal arithmetic. The radiation equation gives the heat rate for that trial. For each panel I inverted the integral of its linear conductivity multiplier to obtain the warmer face, adding the contact jump between inversions. Bisection on the reconstructed hot face over 390–410 K surface trials recovered 400 K at the surface, 525 and 560 K at the cold and hot sides of the contact, 610 K at the inner face, and 175 W outward.

The exact values also satisfy both conductivity integrals, the 35 K contact jump and radiation balance. Both conductivity multipliers remain positive across the physical range, so the inward reconstructed hot face increases with the trial surface temperature. I checked that the archived replay intervals enclose the four exact panel-face temperatures, the radiated heat rate, and signed rod flows of 175, 43.75 and −131.25 W in each panel. The baseline has the same total heat rate yet different internal contact faces, 522.5 and 487.5 K. Those faces distinguish the fourth case even with forged slope labels. The third case alone retains its designed midpoint degeneracy.

## Pinned CI and scope

Both workflow runs returned success for the reviewed head and both artifact records identified the requested runs. Both downloaded ZIPs passed CRC tests.

- [Series run and artifact](https://github.com/physicsvigilante/sim_heat/actions/runs/44881378031/artifacts/14698580485) matched SHA-256 `74a3b199a3303512f9a2bb936edbb71467e4a7b025850637ade2f4cbb1e3c79e`. It contained five JSON files. The entire furnace lesson matched my local exact-head replay by parsed JSON equality.
- [TwinBridge run and artifact](https://github.com/physicsvigilante/sim_heat/actions/runs/44881378000/artifacts/14698426073) matched SHA-256 `1eefdcaf92dab1807d401b1a1d2404a3f8d18ff93e4ec730e235a6ae153d610c`. Its source-head file matched the pinned commit. The decompressed trace and parsed oracle and control reports matched their frozen held-out counterparts.

All four furnace cases record nativeExecuted, nativeQualified, independentlyCertifiedReference and runnerConsumable as false. This targeted independent-in-context review establishes an offline replay result. Source merge remains an owner decision.
