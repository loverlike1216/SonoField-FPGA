# Open a real routed design in an additional visible Vivado window; no programming.
set root [file normalize [file join [file dirname [info script]] ..]]
set dcp [file join $root build pre_pcb_core_strategy3_routed.dcp]
if {![file exists $dcp]} {error "Reproduce strategy3 before opening its routed checkpoint"}
open_checkpoint $dcp
report_timing_summary -report_unconstrained -name SonoField_V2_Internal_132MHz
report_timing -max_paths 20 -name SonoField_V2_Critical_Paths
puts "SonoField-FPGA v2: real internal routed132MHz timing PASS. Full board/PS/PCB readiness remains NO."
