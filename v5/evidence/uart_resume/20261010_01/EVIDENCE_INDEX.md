# UART resume evidence index — 2026-10-10

Current continuation source7d4dd090; samev5, offline ACCEPT WITH LIMITATIONS;
realboard/wholeplatform REVISE. Actual publication receipt is outside this seal:
shared/uart_resume/PUBLICATION_RECEIPT.json.

- FINAL_VERIFICATION.json, TEST_MATRIX.csv and FAILURE_REGISTER.json: measured gates, exact scope and preserved failures.
- windows_uart*.json, port_discovery.json: COM3Code0/driver11.6.0.420/pyserial3.5; enumeration-only.
- uart_slcr_readonly.log, hardware_summary.json, readonly_after.json, final_process_state.json: actual bounded read-only PS registers, CPU Running before/after, no UART open or board write, originalGUI retained and ownedservers stopped.
- vendor_hardware_inventory.json: actual2023.1vendor-share listing, V2.0schematic; no file-body/recovery/Rev3qualification claim. Provider obfuscated MD5 fields explicitly unverified.
- current_build/ and clean_build/: actual native2025.2SDT/empyro/BSP/ARMELF logs, BSPparameters, linker/map/readelf/size/symbols and checksums. Binaries remain ignored local build, never deployed.
- clean_environment/: independent nohardlinks/current-onlyclone/freshlockedvenv dependencies,203tests and byte/preservation audits; no historical worktree.
- target_reproduction.json and elf_audit_negative_cases.json: both builds/OCMaudits, unchangedapplication .text equality,3rejected actualELFmutants. Complete ELF/BSP path-dependent bytes are not declared bitexact; RWX warning retained.
- prior_seal_audit.json: all1160prior sealed files unchanged; previous full3696x4/native/digital evidence retained with original scope/time.
- check_*.json and preservation_final.json: structure/inheritance/legacycopy/S03324/immutable3026/frozen3918metadata; no archivebody/originalphysicalsandbox read.
- toolchain_receipt.json and SOURCE_HASHES.json: official portable Arm archive pin and exact current build/service sources.
- PRE_PUBLICATION_RECONCILIATION.json: current branch/main/PR1–4 before push; PR4 Draft and main unchanged.
- PUBLIC_PROVENANCE.json, PRIVACY_SCAN.json, FILE_HASHES.json: raw-to-public text conversion/redaction hashes, credential/privacy audit and exact public-byte seal. Ignored local_raw includes private rawlogs/HTML; no cookies/accesscodes published.
- attempts/ and failures/: authentic failed paths, not overwritten or hidden by corrected runs.

Result/reproduction/rollback: v5/docs/uart_resume/RESULT.md and REPRODUCE.md.
Latest recovery: CP-20261010-002. Observable interaction records are PARTIAL;
external ChatGPT/independent final review is unavailable/pending, not fabricated.
