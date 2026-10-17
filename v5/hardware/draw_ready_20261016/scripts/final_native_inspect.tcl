set audit [file normalize [file join [file dirname [info script]] ..]]
set out [file join $audit results native21_final]
file mkdir $out
open_checkpoint [file join $audit results native21 NATIVE_ROUTED.dcp]
set tx_ports [get_ports {serial_data_0[*] shift_clock_0 latch_clock_0}]
set padregs [get_cells -hier -include_replicated_objects -filter {NAME =~ *tx44*serial*tx*serial_data_reg* || NAME =~ *tx44*serial*tx*shift_clock_reg || NAME =~ *tx44*serial*tx*latch_clock_reg}]
set_max_delay -datapath_only 4.5 -from $padregs -to $tx_ports
report_timing_summary -delay_type min_max -report_unconstrained -file [file join $out TIMING.rpt]
report_drc -file [file join $out DRC.rpt]
report_methodology -file [file join $out METHODOLOGY.rpt]
set f [open [file join $out PAD_DELAY.csv] w]
puts $f "port,max_ns,min_ns,max_startpoint,min_startpoint"
foreach p $tx_ports {
 set slow [get_timing_paths -to $p -delay_type max -max_paths 1]
 set fast [get_timing_paths -to $p -delay_type min -max_paths 1]
 puts $f "[get_property NAME $p],[get_property DATAPATH_DELAY $slow],[get_property DATAPATH_DELAY $fast],[get_property STARTPOINT_PIN $slow],[get_property STARTPOINT_PIN $fast]"
}
close $f
report_timing -from $padregs -to $tx_ports -delay_type max -max_paths 40 -file [file join $out PAD_TIMING.rpt]
report_cdc -file [file join $out CDC.rpt]
report_exceptions -coverage -file [file join $out EXCEPTION_COVERAGE.rpt]
set f [open [file join $out STATUS.txt] w]
puts $f "SETUP [get_property SLACK [get_timing_paths -delay_type max -max_paths 1]]"
puts $f "HOLD [get_property SLACK [get_timing_paths -delay_type min -max_paths 1]]"
puts $f "PORTS [llength $tx_ports]; includesreplicatedIOBdrivers"
close $f

set f [open [file join $out ADC_PAD_EDGES.csv] w]
puts $f "port,edge,max_ns,min_ns"
foreach port {adc_sclk_0 adc_cs_n_0 adc_sdi_0 adc_convst_0 adc_reset_0} {
 foreach edge {rise fall} {
 if {$edge eq "rise"} {set slow [get_timing_paths -rise_to [get_ports $port] -delay_type max -max_paths 1];set fast [get_timing_paths -rise_to [get_ports $port] -delay_type min -max_paths 1]} else {set slow [get_timing_paths -fall_to [get_ports $port] -delay_type max -max_paths 1];set fast [get_timing_paths -fall_to [get_ports $port] -delay_type min -max_paths 1]}
 puts $f "$port,$edge,[get_property DATAPATH_DELAY $slow],[get_property DATAPATH_DELAY $fast]"
 }
}
close $f
