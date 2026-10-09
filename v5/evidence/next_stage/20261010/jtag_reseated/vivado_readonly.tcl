# Identification only. No device programming, CPU reset, initialization or memory writes.
open_hw_manager
connect_hw_server -url 127.0.0.1:3122
puts "SONOFIELD_READONLY_BEGIN"
foreach target [get_hw_targets] {
    puts "TARGET $target"
    current_hw_target $target
    open_hw_target
    foreach device [get_hw_devices] {
        puts "DEVICE $device"
        report_property $device
        if {[catch {refresh_hw_device -update_hw_probes false $device} reason]} {
            puts "REFRESH_ERROR $reason"
        }
        report_property $device
        foreach sysmon [get_hw_sysmons -of_objects $device] {
            if {[catch {refresh_hw_sysmon $sysmon} reason]} {
                puts "SYSMON_ERROR $reason"
            } else {
                report_property $sysmon
            }
        }
    }
    close_hw_target
}
puts "SONOFIELD_READONLY_END"
disconnect_hw_server
close_hw_manager

