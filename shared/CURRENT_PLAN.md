# VN1 current plan

## Current Goal
Build and verify a board-independent 128-channel timing baseline and TCT40 hardware architecture.

## Scope
Audit all 12 supplied board files; record conflicts. Implement Python directional field model,
planar/concave comparisons and emitter scaling. Implement common timebase, separate request/calibration,
complete-map atomic commit, safe enable and parameterized serializer. Run Python, Icarus and
Vivado 2025.2 XSim; synthesize only with a documented exact part. Supply physical bring-up guide.

## Non-Goals
No guessed XDC, no bitstream, final PCB, PS software integration, camera loop or physical levitation claim.

## Files Expected To Change
rtl/, tb/, software/, tests/, scripts/, docs/, hardware/, constraints/, evidence/, shared/, README.md.
Existing board files remain untouched and local (third-party redistribution rights unconfirmed).

## Risks
Part/package/grade unreadable; clock/source disagreement resolved by user in favor of .const (33 MHz); malformed GPIO numbering;
unknown bank voltage. 128 x 256 x 40 kHz = 1.31072 Gbit/s aggregate output state bandwidth.
A naive 595 chain cannot meet this. Serializer is a digital interface candidate, not an approved PCB.

## Validation
Analytic acoustic checks; TB01-TB15; complete-map rejection and safety fault cases;
Python edge-by-edge oracle; three identical simulation runs; independent Icarus/XSim traces.
Board-gate script must refuse synthesis/project generation without verified part and clock facts.

## Evidence Required
Board manifest hashes, exact commands/tool versions/exit codes, test summaries, trace hashes,
field comparison CSV and plots, explicit synthesis/implementation status.

## Done When
All feasible digital/model gates pass; remaining hardware facts are explicitly blocked; documentation,
state and evidence agree; clean reproducibility run; reviewed commit on main.

## Need ChatGPT Decision?
Yes for unresolved board facts and physical serializer component/topology freeze.
These do not block board-independent simulation or field modeling.

## Current execution result
Digital/model implementation and cross-tool verification complete. Authoritative digital evidence:
evidence/simulation/vn1_release/summary.json (PASS). Model outputs: evidence/model/vn1/.
Physical synthesis/implementation/bring-up remain blocked. Finish clean-checkout reproduction, state/evidence
audit and stable checkpoint; do not expand into PCB fabrication or advanced field modes.
