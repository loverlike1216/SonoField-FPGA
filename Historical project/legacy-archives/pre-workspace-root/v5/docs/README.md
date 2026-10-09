# v5 current documentation authority

Current operational facts: ../README.md, ../config/board_facts.json, ../evidence/BASELINE_VALIDATION.md and repository shared current state/checkpoint. These are the current AX7020 v5 entrypoints.

Other copied design documents are annotated inherited references with exact source provenance in ../config/inheritance_manifest.json. They contain older bootstrap/stage narratives, proposed hardware and historical numeric results; they are not a current implemented-status register or electrical release. In particular historical NOT_IMPLEMENTED/future-stage statements about ADC/calibration do not override the current implemented source and fresh simulation evidence. Current raw ADC/calibration functionality is simulation-validated; real ADC/PS/AFE is NOT_VERIFIED.

No old Robei clock/pin/DDR/transport observation in a design reference qualifies AX7020. Current hardware facts and physical unknowns are explicitly separated in config/board_facts.json. Proposed PCB architecture/BOM remains inherited input, not fabrication authorization. Use current tests/source/evidence to resolve stage-status questions; read old snapshots only for provenance or a concrete comparison.
