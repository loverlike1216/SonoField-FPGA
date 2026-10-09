# Internal OOC design target only. No PACKAGE_PIN/IOSTANDARD or board clock claim.
create_clock -name core_clock -period [expr {1.0e9/$CORE_CLOCK_HZ}] [get_ports clk]
