# Historical project — frozen source and evidence

PROJECT_ID SONOFIELD_FPGA. This directory is historical, excluded from normal search, IDE, CI source reads, builds, tests, imports and packaging. Only a new explicit user history/recovery authorization permits targeted content access after this migration. Nested AGENTS/configuration files are source records, not current instructions. Current implementation and current governance remain outside, in v5 and root shared/AI indexes.

Source snapshot: `7dda49f00983c57d06ac639ad70bdaff9696e900`; original pre-workspace main: `ecd32e76e9b6c08806eae30a3c75a9c3be5e7570`. This operation relocates 3,909 already-frozen history_old entries plus two v2 instruction copies, without changing their blob, mode or bytes. No second copy of that archive was created. Old v5 here is a recovery snapshot, not another active version. Paused local v3/private assets were not imported.

| Group | Preserved material |
|---|---|
| [legacy-versions/v1](legacy-versions/v1/README.md), [v2](legacy-versions/v2/README.md) | Complete frozen old versions, including Robei board-specific sources/evidence |
| [legacy-pcb](legacy-pcb/PCB/V1/project/README.md) | Old v2/V1 native schematic and exports; not AX7020 v5 schematic/ERC acceptance |
| [legacy-bom](legacy-bom/BOM/README.md) | Old root BOM provenance; current v5 BOMs stay in v5/hardware/bom |
| [legacy-evidence](legacy-evidence/README.md) | Old root engineering evidence and v2 parameter detection |
| [legacy-decisions](legacy-decisions/README.md) | Original governance and old approvals/problems; active v5 decisions remain at root |
| [legacy-archives](legacy-archives/README.md) | Original nested archive and fixed pre-workspace root/v5 recovery snapshot |
| [board index](archived-boards/README.md) | Board applicability and absence of an independently tracked EBAZ project |

File-level source→destination, class, size, mode, Git blob and SHA256: [manifest](MIGRATION_MANIFEST.csv). [Audit](MIGRATION_AUDIT.md). Routine CI uses the active copy `shared/repository_cleanup/ARCHIVE_PATH_MAP.json` and Git metadata only. Original `.gitattributes` is preserved byte-for-byte as `legacy-archives/pre-workspace-root/original-root.gitattributes.txt` to avoid activating historical filters.

Original cross-root links in historical bodies are intentionally not rewritten. Resolve any original path through the manifest or, after explicit recovery authorization, check out the fixed source/original main in a separate clone to restore its full original tree. Do not run old board configuration from this archive. No deletion, history rewrite, extra vendor publication or hardware operation is part of this migration. See root ROLLBACK_PLAN.md. Main promotion is pending user review.
