# Read documented status/configuration registers through DAP AP0 only.
# No stop/rst/ps7_init/dow/con/mwr or DDR RAM access.
puts "XSDB_VERSION=[version]"
connect -url tcp:127.0.0.1:3121
puts "TARGETS_BEFORE=[targets]"
puts "TARGET_PROPERTIES=[targets -target-properties]"
set matches [targets -filter {name == "APU"} -target-properties]
if {[llength $matches] != 1} {error "Expected exactly one APU"}
targets -set -filter {name == "APU"}
foreach {label address} {BOOT_MODE 0xF800025C DDRC_CTRL 0xF8006000 DDRC_CTRL_REG1 0xF8006060} {
    if {[catch {set value [mrd -address-space AP0 -value $address 1]} reason]} {
        puts "READ_ERROR $label $address $reason"
    } else {puts "READ $label $address $value"}
}
puts "TARGETS_AFTER=[targets]"
disconnect
puts "NO_RESET_HALT_INITIALIZATION_DOWNLOAD_MEMORY_WRITE_OR_DDR_RAM_ACCESS"
exit
