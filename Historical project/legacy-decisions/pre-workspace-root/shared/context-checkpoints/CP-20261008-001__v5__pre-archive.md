---
checkpoint_id: CP-20261008-001
project_id: SONOFIELD_FPGA
active_version: v2
authorized_target_version: v5
branch: main
base_commit: 851d1ef747cd95da13e5eb0705b5a7885b68d83c
head_commit: 851d1ef747cd95da13e5eb0705b5a7885b68d83c
created_at: 2026-10-08T08:27:37.132790+00:00
status: VALID
source_of_truth: repository
---

# Context Checkpoint

Current identity/version/stage and exact validation/commit scope are in the paired JSON. Current model GPT-6.1 Sol High (user-declared); historical models/records unchanged. This is an evidence checkpoint, not a new version/release. User explicitly authorized v5; no v4.

## Current goal and architecture

Safely establish standalone AX7020 v5 source while preserving original engineering/history. Host solver/trajectory -> PS C/transport boundary -> AXI PL ->128 coherent 8bit phase channels with independent calibration and atomic commits ->serializer -> future qualified drivers/TX; central ADC/calibration feedback currently simulated. Physical operation not verified. Core geometry and safety behavior stay fixed.

## Completed and current plan

186 copied assets; own runtime fixtures/config/source; full115 tests/3696frame4runs cross-simulator PASS; native documented-part OOC synthesis complete. 3343 historical original non-cache files preserved. No historical archive yet; current shared state remains v2 until post-archive verification; v5 is authorized target with tested digital baseline.

## Next actions

- Commit recovery point
- Archive only snapshots/indexes, preserve old paths
- Repeat full baseline after archival
- Activate v5 per actual user approval

## Active decisions and state conflicts

Direct user authorization overrides old default-v2/no-upgrade execution restrictions. Old shared v2/v3 records are original historical facts; v5 platform transition is user-driven, not a model switch. Preserve them in Git and archived snapshots. No automatic old board decision executes on AX7020. Current blockers and acceptance remain separate from old results.

## Blockers, validation and limitations

- AX7020_PHYSICAL_REVISION
- MATCHED_PS_DDR_XSA_BSP
- PRODUCTION_IO_EXTERNAL_TIMING
- REAL_TRANSPORT_AND_ACOUSTICS
- CHAT_MEMORY_ACCESS_BLOCKED
- No physical board/PS initialization/programming/UART/GPIO/PCB test this iteration
- Full-board implementation/bitstream NOT_RUN
- Standalone uses same installed dependencies, not another computer
- External ChatGPT BLOCKED; observable Codex transcript PARTIAL
- Untracked/private originals remain local; not all local data is published

## Do Not Change / Invariants

- Frozen original versions/byte hashes/history
- Core algorithms/protocol/registers/calibration/atomic/safety/geometry/test thresholds
- Do not import old Robei board constraints or historical PASS
- No new version without explicit user approval
- No board programming without reviewed integration facts
- 128channels;PHASE_BITS8;common master phase
- Separate requested+calibration mod256;atomic map switch
- 10mm candidate;12mm radiating-center pitch;100mm face gap adjustable90..115mm;dual8x8;origin center
- Default Windows shell pwsh7
- All runtime inputs local to v5; tool binaries/interpreter may be external

## Repository delta / resume / evidence provenance

User now explicitly authorizes AX7020 v5; no model-only change;186 copies and fresh current digital/OOC evidence, isolated old board state; prior records retain original provenance. Open current-version AI problems:none newly created; historical problems retain their scopes. Recovery HEAD:851d1ef747cd95da13e5eb0705b5a7885b68d83c. Evidence-bearing source/recovery HEAD observed before this checkpoint commit; not a self-referential checkpoint commit.

Read v5/README.md and current shared state/checkpoint/plan; verify current Git then actual AX7020 platform preflight; do not scan all history.

- shared/organization/DIRECTORY_AUDIT.md
- shared/organization/VERSION_MIGRATION_PLAN.json
- v5/config/inheritance_manifest.json
- shared/organization/HISTORICAL_INTEGRITY.json
- v5/evidence/baseline/before_migration_complete/summary.json
- v5/evidence/synthesis/loaded_sources.txt
