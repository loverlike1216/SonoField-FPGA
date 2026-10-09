# Candidate portability and regression

Result: ACCEPT WITH LIMITATIONS — CANDIDATE ONLY. BASE `ecd32e76e9b6c08806eae30a3c75a9c3be5e7570`; actual validated candidate source `0ab574f9e2ad422106655f3c827e89d262d93bb4`. All results below were produced by tools in this task. Main is not merged; permanent workspace promotion and post-merge fresh remote-main cold start remain user-gated.

| Gate | Fresh BASE before extraction | Migrated retry1 | Independent clean clone |
|---|---|---|---|
| Python/Tk tests |115/115 PASS|115/115 PASS|115/115 PASS|
| Full GUI-driven fixed trajectories |3696frames×4 PASS|3696frames×4 PASS|3696frames×4 PASS|
| Independent simulators |Icarus×3 +XSim2025.2×1|Icarus×3 +XSim2025.2×1|Icarus×3 +XSim2025.2×1|
| Canonical trajectory/map/trap/ACK |Exact historical BASE hashes|Exact fresh BASE hashes|Exact fresh BASE hashes|
| C service/protocol/AXI/MMIO/safety/serializer/calibration/golden equivalence |PASS|PASS|PASS|
| Offline hardware-candidate/BOM checks |15 PASS|15 PASS|15 PASS|
| ADC candidate interface, Icarus and XSim |256frames each PASS|256frames each PASS|256frames each PASS|
| Vivado2025.2 OOC rebuild / reopen |18 own-v5 sources PASS|18 own-v5 sources PASS|18 own-v5 sources PASS|
| OOC timing, WNS/WHS |+0.994ns/+0.157ns|+0.994ns/+0.157ns|+0.994ns/+0.157ns|

Evidence: [machine matrix](PORTABILITY_AND_REGRESSION.json), [canonical hash comparison](../../v5/evidence/migration/20261009/digital_behavior_comparison.json), [OOC comparison](../../v5/evidence/migration/20261009/ooc_comparison.json), [BASE](../../v5/evidence/migration/20261009/base/summary.json), [MIGRATED](../../v5/evidence/migration/20261009/migrated_retry1/summary.json), [CLEAN_CLONE](../../v5/evidence/migration/20261009/clean_clone/summary.json), [old sandbox preservation](../../v5/evidence/migration/20261009/old_sandbox_preservation.json), [source/search isolation](../../v5/evidence/migration/20261009/search_isolation.json), [102 protected hashes](../../v5/evidence/migration/20261009/active_reuse_hashes.json). Logs/source lists/runtime ownership/dependency versions remain in each environment's evidence. LOG_HASHES.json records raw-workspace and canonical-LF hashes, because Git legitimately normalizes text evidence line endings.

The independent clean clone has its own .git, no alternates/hardlink sharing, and a newly installed .venv using --no-cache-dir and locked requirements. It cloned the actual formal remote history then fetched committed candidate objects before publication; its own source/runtime/output paths are recorded in the actual commands. Reproduction does not require the old physical sandbox. The two environments share installed host Vivado/Icarus/GCC; this is not a second machine or OS.

Full demo canonical trajectory `1e5d592b95b9c0bf9ba69568eced9187cee573968aa253f9bb36e39f1353d66f`, phase maps `86a9a16a46321310681f724e22744f8289db5ee9d07abd3934a932efac72867b`, trap reports `a1a11fce45cfde8a7a8ab6d80658cfe0b406721b647400a55a91a8ab56dd2694`, ACK `2ba1491d01e8dc41162fc0885f4095a05bd937db486dc9ea907789f0b4d7c8ef`. APPLY_CENTER has its own four exact hashes in the comparison. No goldens/tests/thresholds were relaxed, and no skip flag was used.

Failures retained: Phase2 in-place restoration hit Windows errno22 before freeze, then same-volume atomic replacement succeeded with exact BASE hash. First migrated run failed9 assertions because the config-only guard rejected original temporary gate fixtures; configurations now remain confined to this v5 config/build scratch, all original115tests and full nested gates passed on retry. See migrated/failure_resolution.json and preparation_failure.json. No failure was relabelled PASS.

OOC remains pre-route, with no verified board input/output delays and HD.CLK_SRC warning; utilization7219LUT/17918registers/4RAMB36. Reopen warnings about unrelated installed board-store parts and the long clean-clone path are retained; selected exact device and all18source checks passed. No board clock/pin/preset, PS init, DDR, bitstream, SD/Flash or physical acoustic operation was performed. ARM target/BSP unqualified; whole platform REVISE. Native v5 schematic NOT_CREATED/ERC_NOT_RUN/MANUFACTURING_HOLD; BOM generator cold start and external ChatGPT/independent final review are not claimed. Original/working workbook bytes and all15offline checks are verified.
