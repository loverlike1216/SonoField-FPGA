# Vivado2025.2 offline candidate. No hardware manager, PS init or bitstream.
if {![string match "2025.2*" [version -short]]} {error "Vivado2025.2 required"}
set root [file normalize [file join [file dirname [info script]] ..]]
set label [expr {[llength $argv] ? [lindex $argv 0] : "platform_final"}]
if {![regexp {^[A-Za-z0-9_]+$} $label]} {error "Invalid build label"}
set work [file join $root build $label]
set out [file join $root evidence pre_pcb_20261009 $label]
file mkdir $out
if {[file exists [file join $work platform.xpr]]} {error "Use a fresh build directory"}
set parts [get_parts -quiet xc7z020*clg400*]
set f [open [file join $out parts.txt] w];puts $f $parts;close $f
if {[llength [get_parts -quiet xc7z020clg400-2]] != 1} {error "Required documented candidate part unavailable"}
create_project platform $work -part xc7z020clg400-2
set f [open [file join $root config ooc_source_list.txt] r]
foreach rel [split [string trim [read $f]] \n] {read_verilog -sv [file join $root [string trim $rel]]}
close $f
read_verilog -sv [file join $root rtl control prepcb_supervisor.sv]
read_verilog -sv [file join $root rtl motion prepcb_frame_mailbox.sv]
read_verilog [file join $root rtl board prepcb_pl.v]
set_property include_dirs [list [file join $root rtl generated]] [current_fileset]
add_files -norecurse [list [file join $root rtl generated transport_valid.svh] [file join $root rtl generated registers.svh]]
create_bd_design prepcb_ps
set ps [create_bd_cell -type ip -vlnv xilinx.com:ip:processing_system7:* ps7]
# Candidate on-chip-only PS platform; DDR deliberately disabled, no Rev3 preset imported.
set_property -dict [list CONFIG.PCW_USE_M_AXI_GP0 {1} CONFIG.PCW_EN_CLK0_PORT {1} CONFIG.PCW_FPGA0_PERIPHERAL_FREQMHZ {132} CONFIG.PCW_USE_FABRIC_INTERRUPT {1} CONFIG.PCW_IRQ_F2P_INTR {1} CONFIG.PCW_UIPARAM_DDR_ENABLE {0} CONFIG.PCW_UART1_PERIPHERAL_ENABLE {1} CONFIG.PCW_UART1_UART1_IO {MIO 48 .. 49}] $ps
set f [open [file join $out ps7_properties.txt] w];puts $f [report_property -return_string $ps];close $f
set inter [create_bd_cell -type ip -vlnv xilinx.com:ip:axi_interconnect:* interconnect]
set_property CONFIG.NUM_MI 6 $inter
set bram [create_bd_cell -type ip -vlnv xilinx.com:ip:axi_bram_ctrl:* task_bram]
set_property -dict [list CONFIG.SINGLE_PORT_BRAM {1} CONFIG.DATA_WIDTH {32}] $bram
set mem [create_bd_cell -type ip -vlnv xilinx.com:ip:blk_mem_gen:* task_memory]
set_property -dict [list CONFIG.Memory_Type {True_Dual_Port_RAM} CONFIG.Use_Byte_Write_Enable {true} CONFIG.Byte_Size {8} CONFIG.Register_PortB_Output_of_Memory_Primitives {false}] $mem
set gpio [create_bd_cell -type ip -vlnv xilinx.com:ip:axi_gpio:* service_io]
set_property -dict [list CONFIG.C_GPIO_WIDTH {32} CONFIG.C_ALL_OUTPUTS {1} CONFIG.C_IS_DUAL {1} CONFIG.C_GPIO2_WIDTH {32} CONFIG.C_ALL_INPUTS_2 {1} CONFIG.C_INTERRUPT_PRESENT {1}] $gpio
set reset [create_bd_cell -type ip -vlnv xilinx.com:ip:proc_sys_reset:* reset]
connect_bd_intf_net [get_bd_intf_pins ps7/M_AXI_GP0] [get_bd_intf_pins interconnect/S00_AXI]
connect_bd_intf_net [get_bd_intf_pins interconnect/M00_AXI] [get_bd_intf_pins task_bram/S_AXI]
connect_bd_intf_net [get_bd_intf_pins interconnect/M01_AXI] [get_bd_intf_pins service_io/S_AXI]
connect_bd_intf_net [get_bd_intf_pins task_bram/BRAM_PORTA] [get_bd_intf_pins task_memory/BRAM_PORTA]
set core [create_bd_cell -type module -reference prepcb_pl pl_core]
connect_bd_intf_net [get_bd_intf_pins interconnect/M02_AXI] [get_bd_intf_pins pl_core/S_AXI]
set slice [create_bd_cell -type ip -vlnv xilinx.com:ip:xlslice:* control_slice]
set_property -dict [list CONFIG.DIN_WIDTH {32} CONFIG.DIN_FROM {15} CONFIG.DIN_TO {0} CONFIG.DOUT_WIDTH {16}] $slice
connect_bd_net [get_bd_pins service_io/gpio_io_o] [get_bd_pins control_slice/Din]
connect_bd_net [get_bd_pins control_slice/Dout] [get_bd_pins pl_core/control]
connect_bd_net [get_bd_pins pl_core/status] [get_bd_pins service_io/gpio2_io_i]
foreach {a b} {bram_clk clkb bram_rst rstb bram_en enb bram_we web bram_addr addrb bram_wrdata dinb bram_rddata doutb} {
 connect_bd_net [get_bd_pins pl_core/$a] [get_bd_pins task_memory/$b]
}
set concat [create_bd_cell -type ip -vlnv xilinx.com:ip:xlconcat:* irq_concat]
set_property CONFIG.NUM_PORTS 5 $concat
set_property CONFIG.PCW_NUM_F2P_INTR_INPUTS 5 $ps
connect_bd_net [get_bd_pins pl_core/irq] [get_bd_pins irq_concat/In0]
connect_bd_net [get_bd_pins service_io/ip2intc_irpt] [get_bd_pins irq_concat/In1]
connect_bd_net [get_bd_pins irq_concat/dout] [get_bd_pins ps7/IRQ_F2P]
foreach {name port index} {center M03_AXI 2 upper M04_AXI 3 lower M05_AXI 4} {
 set iic [create_bd_cell -type ip -vlnv xilinx.com:ip:axi_iic:* i2c_$name]
 connect_bd_intf_net [get_bd_intf_pins interconnect/$port] [get_bd_intf_pins i2c_$name/S_AXI]
 connect_bd_net [get_bd_pins i2c_$name/iic2intc_irpt] [get_bd_pins irq_concat/In$index]
 connect_bd_net [get_bd_pins ps7/FCLK_CLK0] [get_bd_pins i2c_$name/s_axi_aclk]
 connect_bd_net [get_bd_pins reset/peripheral_aresetn] [get_bd_pins i2c_$name/s_axi_aresetn]
 make_bd_intf_pins_external [get_bd_intf_pins i2c_$name/IIC]
}
connect_bd_net [get_bd_pins ps7/FCLK_CLK0] [get_bd_pins ps7/M_AXI_GP0_ACLK] [get_bd_pins interconnect/ACLK] [get_bd_pins interconnect/S00_ACLK] [get_bd_pins interconnect/M00_ACLK] [get_bd_pins interconnect/M01_ACLK] [get_bd_pins task_bram/s_axi_aclk] [get_bd_pins service_io/s_axi_aclk] [get_bd_pins reset/slowest_sync_clk]
connect_bd_net [get_bd_pins ps7/FCLK_RESET0_N] [get_bd_pins reset/ext_reset_in]
connect_bd_net [get_bd_pins reset/interconnect_aresetn] [get_bd_pins interconnect/ARESETN] [get_bd_pins interconnect/S00_ARESETN] [get_bd_pins interconnect/M00_ARESETN] [get_bd_pins interconnect/M01_ARESETN]
connect_bd_net [get_bd_pins reset/peripheral_aresetn] [get_bd_pins task_bram/s_axi_aresetn] [get_bd_pins service_io/s_axi_aresetn]
connect_bd_net [get_bd_pins ps7/FCLK_CLK0] [get_bd_pins pl_core/clk] [get_bd_pins interconnect/M02_ACLK] [get_bd_pins interconnect/M03_ACLK] [get_bd_pins interconnect/M04_ACLK] [get_bd_pins interconnect/M05_ACLK]
connect_bd_net [get_bd_pins reset/peripheral_aresetn] [get_bd_pins pl_core/rst_n] [get_bd_pins interconnect/M02_ARESETN] [get_bd_pins interconnect/M03_ARESETN] [get_bd_pins interconnect/M04_ARESETN] [get_bd_pins interconnect/M05_ARESETN]
make_bd_intf_pins_external [get_bd_intf_pins ps7/FIXED_IO]
foreach p {health adc_busy adc_dout adc_reset adc_convst adc_cs_n adc_sclk adc_sdi rx_blank serial_data shift_clock latch_clock output_disable heartbeat efuse_up efuse_dn} {make_bd_pins_external [get_bd_pins pl_core/$p]}
assign_bd_address
validate_bd_design
save_bd_design
generate_target all [get_files prepcb_ps.bd]
make_wrapper -files [get_files prepcb_ps.bd] -top -import
write_bd_tcl -force [file join $out recreate_ps_bd.tcl]
write_hw_platform -fixed -force -file [file join $out prepcb_logical_candidate.xsa]
set f [open [file join $out loaded_sources.txt] w];puts $f [join [get_files] \n];close $f
puts "PREPCB_PS_BD_CREATED_NON_DEPLOYABLE"
close_project
# Independent logical PL OOC route. External board delays remain deliberately absent.
create_project -in_memory -part xc7z020clg400-2
set f [open [file join $root config ooc_source_list.txt] r]
foreach rel [split [string trim [read $f]] \n] {read_verilog -sv [file join $root [string trim $rel]]}
close $f
read_verilog -sv [file join $root rtl control prepcb_supervisor.sv]
read_verilog -sv [file join $root rtl motion prepcb_frame_mailbox.sv]
read_verilog [file join $root rtl board prepcb_pl.v]
set_property include_dirs [list [file join $root rtl generated]] [current_fileset]
synth_design -mode out_of_context -top prepcb_pl -part xc7z020clg400-2
create_clock -name core_clk -period 7.575758 [get_ports clk]
opt_design
place_design -directive Explore
phys_opt_design -directive AggressiveExplore
route_design -directive Explore
phys_opt_design -directive AggressiveExplore
report_timing_summary -delay_type min_max -report_unconstrained -file [file join $out pl_routed_timing.rpt]
report_utilization -file [file join $out pl_routed_utilization.rpt]
report_drc -file [file join $out pl_routed_drc.rpt]
report_cdc -file [file join $out pl_cdc.rpt]
write_checkpoint -force [file join $work prepcb_pl_routed.dcp]
puts "PREPCB_PL_OOC_ROUTED_NOT_BOARD_TIMING_CLOSURE"
