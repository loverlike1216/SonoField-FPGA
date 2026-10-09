# Conservative engineering target only. No hardware programming in this flow.
set root [file normalize [file join [file dirname [info script]] ..]]
set stage baseline
if {[llength $argv]>0} {set stage [lindex $argv 0]}
if {$stage ni {baseline round1 round2}} {error "Unsupported bounded timing round"}
set out [file join $root evidence core_timing_real_loop $stage]
file mkdir $out
set_param general.maxThreads 4
if {[version -short] ne "2025.2"} {error "Vivado 2025.2 required"}
create_project -in_memory -part xc7z020clg400-1
foreach dir {rtl rtl/timing rtl/phase rtl/output rtl/control rtl/acquisition rtl/calibration rtl/motion} {
 foreach f [glob -nocomplain [file join $root $dir *.sv]] {
  # Reproduce historical rounds from preserved inputs, not current round2 RTL.
  if {$stage eq "baseline" && [file tail $f] in {sono_digital_system.sv burst_generator.sv}} {
   set f [file join $root evidence core_timing_real_loop baseline [file tail $f]]
  } elseif {$stage eq "round1" && [file tail $f] eq "burst_generator.sv"} {
   set f [file join $root evidence core_timing_real_loop baseline burst_generator.sv]
  }
  read_verilog -sv $f
 }
}
set_property include_dirs [list [file join $root rtl generated]] [current_fileset]
synth_design -top sono_axi_system -part xc7z020clg400-1 -mode out_of_context
create_clock -period 7.575758 -name core132 [get_ports clk]
proc reports {out label} {
 file mkdir [file join $out $label]
 set dest [file join $out $label]
 report_timing_summary -report_unconstrained -file [file join $dest timing_summary.rpt]
 report_timing -max_paths 20 -nworst 1 -path_type full_clock_expanded -input_pins -file [file join $dest critical_paths.rpt]
 report_high_fanout_nets -max_nets 20 -file [file join $dest high_fanout.rpt]
 report_clock_utilization -file [file join $dest clock_utilization.rpt]
 report_clocks -file [file join $dest clocks.rpt]
 report_methodology -file [file join $dest methodology.rpt]
 report_drc -file [file join $dest drc.rpt]
 report_utilization -file [file join $dest utilization.rpt]
 report_cdc -details -file [file join $dest cdc.rpt]
 check_timing -verbose -file [file join $dest check_timing.rpt]
 set f [open [file join $dest critical_paths.tsv] w]
 set props {STARTPOINT_PIN ENDPOINT_PIN SLACK DATAPATH_DELAY LOGIC_LEVELS REQUIREMENT SKEW}
 puts $f [join $props "\t"]
 foreach path [get_timing_paths -max_paths 20 -nworst 1] {
  set row {}
  foreach prop $props {
   if {[lsearch -exact [list_property $path] $prop]>=0} {lappend row [get_property $prop $path]} else {lappend row UNKNOWN}
  }
  puts $f [join $row "\t"]
 }
 close $f
}
reports $out synthesis
write_checkpoint -force [file join $root build core_timing_${stage}.dcp]
if {$stage ne "baseline"} {
 opt_design
 place_design
 reports $out placed
 phys_opt_design
 route_design
 reports $out routed
 write_checkpoint -force [file join $root build core_timing_${stage}_routed.dcp]
}
close_project
exit
