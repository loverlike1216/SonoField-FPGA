# A0 qualification only. Use an owned localhost3122 hw_server, GDB ports disabled.
# Reads fixed SLCR configuration registers through DAP AP0; no FIFO/AXI/RAM access.
if {![string match "2025.2*" [version]]} {error "XSDB2025.2 required"}
connect -url tcp:127.0.0.1:3122
try {
    set before [targets]
    puts "TARGETS_BEFORE=$before"
    foreach core {0 1} {
        if {![string match "*ARM Cortex-A9 MPCore #$core (Running)*" $before]} {
            error "Expected both existing CPUs Running; no intervention authorized"
        }
    }
    if {[llength [targets -filter {name == "APU"} -target-properties]] != 1} {
        error "Expected one APU"
    }
    targets -set -filter {name == "APU"}
    foreach {label address} {
        BOOT_MODE 0xF800025C
        ARM_PLL_CTRL 0xF8000100
        IO_PLL_CTRL 0xF8000108
        UART_CLK_CTRL 0xF8000154
        UART_RST_CTRL 0xF8000228
        MIO_PIN_48 0xF80007C0
        MIO_PIN_49 0xF80007C4
    } {
        set value [mrd -address-space AP0 -value $address 1]
        puts [format "READ %s %s 0x%08X" $label $address $value]
    }
    set after [targets]
    puts "TARGETS_AFTER=$after"
    foreach core {0 1} {
        if {![string match "*ARM Cortex-A9 MPCore #$core (Running)*" $after]} {
            error "Unexpected CPU status; disconnect only"
        }
    }
    puts "READONLY_SLCR_COMPLETE_NO_HALT_RESET_INIT_WRITE_FIFO_AXI_OR_RAM_ACCESS"
} finally {
    disconnect
}
exit
