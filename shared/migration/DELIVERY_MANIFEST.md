# Candidate delivery boundary

Include current README/AGENTS/CHANGELOG, current shared state/acceptance/runbook/migration reports, current open Problems and actual observable AI provenance, v5 source/config/firmware/testbench/golden fixtures/locked dependencies/tool scripts, current hardware proposals with unapproved status and selected real summaries/logs/canonical traces. Preserve original submitted BOM and distinguish the working candidate. No license is invented; third-party rights require review before external competition/release distribution.

Exclude history_old, .git, .venv, .migration-private, .portability, build/cache/Xil/simulator binaries/raw traces, local_raw, private vendor documents/device identity, BOM preview caches and unapproved fabrication/layout/Gerber artifacts. Include candidate design notes only when clearly marked NOT_RELEASED. Native v5 schematic/qualified netlist and ERC do not exist and cannot be included as completed assets.

Future package_submission should use an explicit Git-tracked allowlist, fixed candidate commit and deterministic sorted manifest of relative path/size/SHA256; normalize zip entry timestamps and verify unpacked hashes in a separate directory. It must fail if any forbidden/private/history path is selected. This task defines the boundary and does not manufacture or publish a final competition/hardware package.
