# GUI execution-evidence failure

Current model: GPT-6.1 Sol High. Date:2026-10-03. Original recovery report remains FAIL.

All four real GUI simulation executions completed:3696frames,three Icarus plus XSim. Returned trajectory/map/trap/ACK hashes match each other and the earlier PASS exactly. However saved trajectory_01.json contained3696NOT_EVALUATED preview rows, so the strict final validity assertion failed. This report does not turn that failed gate into PASS.

Source inspection: action handed a path to the worker, but poll persisted self.preview_path, a mutable UI property that could hold a later preview. The evidence file did not guarantee it corresponded to the dispatched command. The new implementation snapshots the exact dispatched evaluated path and execution result in the completion event, saves that snapshot, and asserts its SHA256 matches the returned executed-trajectory digest. Architecture,RTL,transport,timing and Acceptance remain unchanged.

Two meaningful tests prove a replaced UI preview cannot overwrite execution evidence and a mismatched digest is rejected before success metadata/file persistence. A new complete regression run is under regression_fixed; original artifacts and failure assertions are preserved.

The previous interrupted2026-09-29 GUI retry remains a distinct failure with unconfirmed cause. It is not retroactively attributed to this issue.
