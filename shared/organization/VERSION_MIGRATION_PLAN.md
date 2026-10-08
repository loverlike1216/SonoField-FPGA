# v5 reuse inventory

Direct user approves v5 AX7020; source currentv2 with core validated at9936a737. v4 is not created. Old versions kept intact. Complete per-file classifications: VERSION_MIGRATION_PLAN.json.

COPY_AS_IS: RTL/TB/tests/firmware,algorithms,geometry,transducer/BOM reference. COPY_AND_UPDATE: copied orchestration paths/version labels/board gates and current docs. REGENERATE: all evidence/build/cache/current board config. DO_NOT_COPY: Robei boardfacts/identity/DDR/pins/J3-J6 budgets,XDC,old native EDA scripts,old evidence/PASS reports,old model-specific management generators. UNKNOWN: user current AX7020 board revision,PS/XSA/connector allocation; stop physical deployment until sourced.

BOM/reference circuits remain unqualified inherited design input; they are not AX7020 electrical release. Golden RTL fixtures are explicit historical validation inputs copied into v5/simulation/golden, not hidden loads from old evidence. Normal v5 operation must not open old-version source.
