# Selective copy from v2 to v5

186 actual inherited assets, individually listed in config/inheritance_manifest.json and shared/organization/VERSION_MIGRATION_PLAN.json. Source copies preserve historical source hashes. RTL/TB/firmware algorithms keep stable names. UI/version fields, fail-closed board profiles and local fixture paths were adapted only in v5. Every adapted file has its reviewed expected hash. Reference docs are explicitly inherited, not new test results.

Regenerate: native Vivado project, synthesis reports and all test evidence. Excluded: old Robei XDC/preset/board facts, COM identities, physical evidence, old PASS logs and board programming scripts. Explicit input copies: three golden RTL fixtures and original SYNTHETIC calibration_reference.json. No old-version worktree is required at runtime. See evidence/BASELINE_VALIDATION.md for before/after and standalone results.

Preserve originals: v1/v2/v3, PCB, BOM, Zynq7020, parameter_detection and root evidence remain in original paths because historical scripts/reports reference them. archive contains governance snapshots and frozen indexes, never hides old source loads.
