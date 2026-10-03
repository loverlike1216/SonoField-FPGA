# Verify candidate MMCM arithmetic with the authoritative part database only.
set root [file normalize [file join [file dirname [info script]] ..]]
set out [file join $root evidence pre_pcb_board_ready clock]
file mkdir $out
create_project -in_memory -part xc7z020clg400-1
read_verilog -sv [file join $root rtl timing board_clock_candidate.sv]
synth_design -top board_clock_candidate -part xc7z020clg400-1 -mode out_of_context
create_clock -period 30.000300003 -name documented33m333 [get_ports clk_in]
report_clocks -file [file join $out vendor_candidate_clocks.rpt]
report_drc -file [file join $out vendor_candidate_drc.rpt]
write_checkpoint -force [file join $root build pre_pcb_clock_candidate.dcp]
close_project
exit
