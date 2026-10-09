# OFFLINE DIAGNOSTICS ONLY. No exact physical PART is selected/persisted.
set root [file normalize [file join [file dirname [info script]] ..]]
set out [file join $root evidence board_transport candidate_synthesis]
file mkdir $out
set_param general.maxThreads 4
set candidates [lsort [get_parts -quiet -filter {DEVICE == xc7z020 && PACKAGE == clg400}]]
set summary [open [file join $out results.tsv] w]
puts $summary "part\tclassification\tclock_wns\tcore_wns\tcore_luts\tcore_ffs"
foreach part $candidates {
 set dest [file join $out $part];file mkdir $dest
 create_project -in_memory -part $part
 read_verilog [file join $root vivado clock_candidate.sv]
 synth_design -top clock_candidate -part $part -mode out_of_context
 create_clock -period 30.303030 -name clk33 [get_ports clk33]
 set_input_jitter [get_clocks clk33] 0.100
 # 100 ps is an ANALYSIS ASSUMPTION, not an oscillator measurement.
 report_clocks -file [file join $dest clocks.rpt]
 report_clock_networks -file [file join $dest clock_networks.rpt]
 report_timing_summary -file [file join $dest clock_timing.rpt]
 report_drc -file [file join $dest clock_drc.rpt]
 set cp [get_timing_paths -quiet -max_paths 1];set cw "NO_PATH";if {[llength $cp]} {set cw [get_property SLACK $cp]}
 close_project
 create_project -in_memory -part $part
 foreach dir {rtl rtl/timing rtl/phase rtl/output rtl/control rtl/acquisition rtl/calibration rtl/motion} {
  foreach f [glob -nocomplain [file join $root $dir *.sv]] {read_verilog -sv $f}
 }
 set_property include_dirs [list [file join $root rtl generated]] [current_fileset]
 synth_design -top sono_axi_system -part $part -mode out_of_context
 create_clock -period 7.575758 -name core132 [get_ports clk]
 report_utilization -file [file join $dest utilization.rpt]
 report_timing_summary -file [file join $dest timing.rpt]
 report_cdc -details -file [file join $dest cdc.rpt]
 set tp [get_timing_paths -quiet -max_paths 1];set tw "NO_PATH";if {[llength $tp]} {set tw [get_property SLACK $tp]}
 puts $summary "$part\tCANDIDATE_ANALYSIS_ONLY\t$cw\t$tw\t[llength [get_cells -hier -filter {REF_NAME =~ LUT*}]]\t[llength [get_cells -hier -filter {REF_NAME =~ FD*}]]"
 flush $summary
 close_project
}
close $summary
exit
