---
problem_id: P-20260927-001
project_id: SONOFIELD_FPGA
active_version: v2
current_stage: BOARD_TRANSPORT_AND_PS_PL_INTEGRATION_PREFLIGHT
status: OPEN
created_at: 2026-09-27
created_by: Codex
base_commit: d25e1d857334c061493459ce49a24debba222432
problem_hash: 0bf40cdd79faaf5fd4aca4af6e1f7cf85eab8662128f4633ea1acb3b4ef61916
---

# Decision Needed
Choose a bounded 132 MHz timing-closure approach before physical integration. No architecture change has been approved.

# Goal
Preserve the existing phase/motion/register semantics while obtaining a deployable timing design after exact part identification.

# Current Engineering State
v2 offline bridge and protocol implemented. Package CLG400 confirmed; speed unknown. All three candidate OOC syntheses complete, but setup WNS is -8.128/-4.995/-3.609 ns. No implementation or bitstream.

# Repository Facts
Starting commit d25e1d857334c061493459ce49a24debba222432. Top sono_axi_system at 132 MHz, existing sono_motion_system unchanged. Candidate package does not establish physical speed grade.

# Evidence
v2/evidence/board_transport/candidate_synthesis/summary.json and each timing.rpt/utilization.rpt. -1 worst path: native_system/digital/carrier_acc_reg[7]/C to native_system/digital/serial/bit_index_reg[0]/CE; 15.451 ns data path. External delays are unconstrained; route delays are synthesis estimates.

# What Codex Tried
One local RAM inference correction removed Synth8-3391 without changing behavioral semantics. Three grades now synthesize (8681 LUT,17996 FF,4 BRAM). No timing-driven micro-patching or constraint relaxation attempted.

# Root Cause Hypotheses
Long combinational accumulator/comparison/control path and fanout to serializer enables; detailed path/logic review required. Synthesis routing estimates may change after placement but cannot justify declaring closure.

# Candidate Options
1. Review/pipeline phase/control evaluation while preserving atomic commit and serializer scheduling, with cycle-accurate reference updates approved first.
2. Diagnose placement/fanout on a correctly identified physical target after board constraints exist.
3. Reconsider core/serialization architecture only as an explicit scope decision, not a silent frequency reduction.

# Constraints
No guessed part, false-path masking, PCB edits, hardware downloads, v1 edits or v3. Keep existing functional register map and atomic phase behavior.

# Acceptance Impact
Offline protocol/AXI preflight can be reviewed independently; physical timing/transport remains blocked.

# Preliminary Engineering Assessment
Resource capacity fits all candidates. Speed-grade selection alone does not establish 132 MHz timing closure. Recommend reviewing the existing control critical path first.

# Questions For Chat
Approve a bounded timing-focused investigation and define latency invariants before any pipeline change, or defer it until exact part and physical clock constraints are available?

# User Approval Boundary
No architecture decision is fabricated. Major latency/interface/scope change requires Chat/user decision. No physical action authorized by this record.
