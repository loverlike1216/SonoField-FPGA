# User-confirmed part. Internal OOC timing only; no hardware programming.
set root [file normalize [file join [file dirname [info script]] ..]]
set stage strategy3
if {[llength $argv]>0} {set stage [lindex $argv 0]}
if {$stage ni {strategy1 strategy2 strategy3}} {error "Unsupported measured timing strategy"}
set source_out [file join $root evidence pre_pcb_board_ready timing $stage]
set out $source_out
if {[llength $argv]>1} {set out [file normalize [file join $root [lindex $argv 1]]]}
if {[file exists [file join $out routed timing_summary.rpt]]} {error "Archived evidence exists; select a new output directory using argv1"}
file mkdir $out
set_param general.maxThreads 4
if {[version -short] ne "2025.2"} {error "Vivado 2025.2 required"}
create_project -in_memory -part xc7z020clg400-1
foreach dir {rtl rtl/timing rtl/phase rtl/output rtl/control rtl/acquisition rtl/calibration rtl/motion} {
 foreach f [glob -nocomplain [file join $root $dir *.sv]] {
   if {[file tail $f] in {motion_queue.sv serializer.sv calibration_scheduler.sv}} {
   set name [file rootname [file tail $f]]
   set f [file join $source_out ${name}_executed.sv]
   if {![file exists $f]} {error "Missing exact stage source snapshot $f"}
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
write_checkpoint -force [file join $root build pre_pcb_core_${stage}.dcp]
if {$stage ne "baseline"} {
 opt_design
 place_design
 reports $out placed
 phys_opt_design
 route_design
 report_route_status -file [file join $out route_status.rpt]
 reports $out routed
 write_checkpoint -force [file join $root build pre_pcb_core_${stage}_routed.dcp]
}
close_project
exit
