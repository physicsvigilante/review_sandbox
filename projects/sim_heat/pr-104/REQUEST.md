# Targeted R2 review of radiating-surface power bounds

Review [PR 104](https://github.com/physicsvigilante/sim_heat/pull/104) at f2fd86455d682e7e127585cb5b47c1fb0ddeb3a8 against 020e123b7a94b4aa103ae335b813f3a957b8b9cc. Reproduce the PR 101 extreme-input limitation and verify the new intersection against an independent signed-energy calculation. Challenge positive, negative and near-zero transfer with uncertain port temperature or resistance. Verify regression, preserved ordinary cases and offline flags.

- [Study and radiation replay](https://github.com/physicsvigilante/sim_heat/actions/runs/44864757798/job/136725831410) and [archive](https://github.com/physicsvigilante/sim_heat/actions/runs/44864757798/artifacts/14690594216), SHA-256 a5b3b2c451b00e08ead4d76f2ae4ae8668a9de9b7b3d931d2629de568821ce15.
- [Frozen general conduction replay](https://github.com/physicsvigilante/sim_heat/actions/runs/44864757753/job/136725830945) and [archive](https://github.com/physicsvigilante/sim_heat/actions/runs/44864757753/artifacts/14691611057), SHA-256 dd564cdcb0553eed9fd87bc182ab0d727119d26b75350ce44f692d61548523a8.
