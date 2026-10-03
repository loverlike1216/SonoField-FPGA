# Read-only analysis of saved checkpoints. No RTL clock profile is changed.
set root [file normalize [file join [file dirname [info script]] ..]]
set out [file join $root evidence core_timing_real_loop timing_refactor trade]
file mkdir $out
set_param general.maxThreads 4
foreach stage {baseline round1 round2} {
 set suffix [expr {$stage eq "baseline"?"":"_routed"}]
 open_checkpoint [file join $root build core_timing_${stage}${suffix}.dcp]
 set f [open [file join $out ${stage}_failing_paths.tsv] w]
 puts $f "startpoint\tendpoint\tslack\tdelay\tlogic_levels"
 foreach p [get_timing_paths -slack_lesser_than 0 -max_paths 40000 -nworst 1] {
  puts $f "[get_property STARTPOINT_PIN $p]\t[get_property ENDPOINT_PIN $p]\t[get_property SLACK $p]\t[get_property DATAPATH_DELAY $p]\t[get_property LOGIC_LEVELS $p]"
 }
 close $f
 if {$stage eq "round2"} {
  # No place/route changes: this optimistic fixed-route screen only rejects
  # inadequate alternatives. A selectable clock profile needs fresh full build.
  foreach mhz {132.0 123.75 121.0 118.8 115.5 99.0 82.5} {
   create_clock -name core132 -period [expr {1000.0/$mhz}] [get_ports clk]
   report_timing_summary -file [file join $out screen_${mhz}MHz.rpt]
  }
 }
 close_design
}
# Verify each integer-MMCM ratio against the installed -1 device/tool rules.
foreach {label mult div} {132.0 24.0 6.0 123.75 30.0 8.0 121.0 22.0 6.0 118.8 36.0 10.0 115.5 28.0 8.0 99.0 24.0 8.0 82.5 20.0 8.0} {
 create_project -in_memory -part xc7z020clg400-1
 set f [open [file join $root build core_timing clock_trade.sv] w]
 puts $f "module clock_trade(input clk33, reset, output core_clk, shift_clk, locked);"
 puts $f "wire fb,fb_buf,c,s;"
 puts $f "MMCME2_BASE #(.CLKIN1_PERIOD(30.303030),.CLKFBOUT_MULT_F($mult),.DIVCLK_DIVIDE(1),.CLKOUT0_DIVIDE_F($div),.CLKOUT1_DIVIDE([expr {int($div)*2}])) mmcm(.CLKIN1(clk33),.CLKFBIN(fb_buf),.CLKFBOUT(fb),.CLKOUT0(c),.CLKOUT1(s),.RST(reset),.PWRDWN(1'b0),.LOCKED(locked));"
 puts $f "BUFG b0(.I(fb),.O(fb_buf)); BUFG b1(.I(c),.O(core_clk)); BUFG b2(.I(s),.O(shift_clk)); endmodule"
 close $f
 read_verilog [file join $root build core_timing clock_trade.sv]
 synth_design -top clock_trade -part xc7z020clg400-1 -mode out_of_context
 create_clock -name input33 -period 30.303030 [get_ports clk33]
 report_clocks -file [file join $out mmcm_${label}MHz_clocks.rpt]
 report_drc -file [file join $out mmcm_${label}MHz_drc.rpt]
 close_project
}
exit
