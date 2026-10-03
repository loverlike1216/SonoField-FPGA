# Identity and two documented DDR controller registers only. No reset/init/halt/DDR access.
puts "PROBE_XSDB_VERSION=[version]"
connect -url tcp:127.0.0.1:3121
puts "PROBE_TARGETS_BEFORE"
puts [targets]
puts "PROBE_TARGET_PROPERTIES=[targets -target-properties]"
set matches [targets -filter {name == "APU"} -target-properties]
if {[llength $matches] != 1} {puts "PROBE_REGISTER_ACCESS=BLOCKED_AMBIGUOUS_OR_NO_APU";disconnect;exit}
targets -set -filter {name == "APU"}
foreach {label address} {DDRC_CTRL 0xF8006000 DDRC_CTRL_REG1 0xF8006060} {
 if {[catch {set value [mrd -address-space AP0 -value $address 1]} error]} {
  puts "PROBE_READ_ERROR $label $address $error"
 } else {puts "PROBE_READ $label $address $value"}
}
puts "PROBE_TARGETS_AFTER"
puts [targets]
disconnect
puts "PROBE_FINISHED_NO_RESET_INIT_HALT_DOWNLOAD_MWR_OR_DDR_TEST"
exit
