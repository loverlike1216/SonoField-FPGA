set audit [file normalize [file join [file dirname [info script]] ..]]
set root E:/Codex_project/AMD_Sonofield/v5
set label [expr {[llength $argv]?[lindex $argv 0]:"native01"}]
set work [file join $audit $label]
set resultdir [file join $audit results $label]
file mkdir $resultdir
if {[file exists [file join $work final.xpr]]} {error "Use fresh implementation directory"}
create_project final $work -part xc7z020clg400-2
set f [open [file join $root config nextstage_source_list.txt] r]
foreach rel [split [string trim [read $f]] \n] {
 set p [file join $root [string trim $rel]]
 if {[file extension $p]eq ".v"} {read_verilog $p} else {read_verilog -sv $p}
}
close $f
read_verilog [file join $root rtl board draw_ready_pl.v]
read_verilog [file join $root rtl timing draw_ready_clocks.v]
set_property include_dirs [list [file join $root rtl generated]] [current_fileset]
add_files [list [file join $root rtl generated transport_valid.svh] [file join $root rtl generated registers.svh]]
create_bd_design draw_ready_ps
set ps [create_bd_cell -type ip -vlnv xilinx.com:ip:processing_system7:* ps7]
set_property -dict [list CONFIG.PCW_USE_M_AXI_GP0 {1} CONFIG.PCW_EN_CLK0_PORT {1} CONFIG.PCW_FPGA0_PERIPHERAL_FREQMHZ {100} CONFIG.PCW_USE_FABRIC_INTERRUPT {1} CONFIG.PCW_IRQ_F2P_INTR {1} CONFIG.PCW_UIPARAM_DDR_ENABLE {0} CONFIG.PCW_UART1_PERIPHERAL_ENABLE {1} CONFIG.PCW_UART1_UART1_IO {MIO 48 .. 49}] $ps
set clk [create_bd_cell -type module -reference draw_ready_clocks clocks]
set core [create_bd_cell -type module -reference draw_ready_pl pl_core]
set inter [create_bd_cell -type ip -vlnv xilinx.com:ip:axi_interconnect:* interconnect]
set_property CONFIG.NUM_MI 4 $inter
set bram [create_bd_cell -type ip -vlnv xilinx.com:ip:axi_bram_ctrl:* task_bram]
set_property -dict [list CONFIG.SINGLE_PORT_BRAM {1} CONFIG.DATA_WIDTH {32}] $bram
set mem [create_bd_cell -type ip -vlnv xilinx.com:ip:blk_mem_gen:* task_memory]
set_property -dict [list CONFIG.Memory_Type {True_Dual_Port_RAM} CONFIG.Use_Byte_Write_Enable {true} CONFIG.Byte_Size {8} CONFIG.Register_PortB_Output_of_Memory_Primitives {false}] $mem
set gpio [create_bd_cell -type ip -vlnv xilinx.com:ip:axi_gpio:* service_io]
set_property -dict [list CONFIG.C_GPIO_WIDTH {32} CONFIG.C_ALL_OUTPUTS {1} CONFIG.C_IS_DUAL {1} CONFIG.C_GPIO2_WIDTH {32} CONFIG.C_ALL_INPUTS_2 {1} CONFIG.C_INTERRUPT_PRESENT {1} CONFIG.C_DOUT_DEFAULT {0x00000000}] $gpio
set iic [create_bd_cell -type ip -vlnv xilinx.com:ip:axi_iic:* i2c_mux]
set reset [create_bd_cell -type ip -vlnv xilinx.com:ip:proc_sys_reset:* reset]
set_property CONFIG.C_EXT_RESET_HIGH 0 $reset
connect_bd_intf_net [get_bd_intf_pins ps7/M_AXI_GP0] [get_bd_intf_pins interconnect/S00_AXI]
foreach {m dest} {M00_AXI task_bram/S_AXI M01_AXI service_io/S_AXI M02_AXI pl_core/S_AXI M03_AXI i2c_mux/S_AXI} {connect_bd_intf_net [get_bd_intf_pins interconnect/$m] [get_bd_intf_pins $dest]}
connect_bd_intf_net [get_bd_intf_pins task_bram/BRAM_PORTA] [get_bd_intf_pins task_memory/BRAM_PORTA]
connect_bd_net [get_bd_pins service_io/gpio_io_o] [get_bd_pins pl_core/control]
connect_bd_net [get_bd_pins pl_core/status] [get_bd_pins service_io/gpio2_io_i]
foreach {a b} {bram_clk clkb bram_rst rstb bram_en enb bram_we web bram_addr addrb bram_wrdata dinb bram_rddata doutb} {connect_bd_net [get_bd_pins pl_core/$a] [get_bd_pins task_memory/$b]}
set irq [create_bd_cell -type ip -vlnv xilinx.com:ip:xlconcat:* irq_concat]
set_property CONFIG.NUM_PORTS 3 $irq
foreach {a b} {pl_core/irq In0 service_io/ip2intc_irpt In1 i2c_mux/iic2intc_irpt In2} {connect_bd_net [get_bd_pins $a] [get_bd_pins irq_concat/$b]}
connect_bd_net [get_bd_pins irq_concat/dout] [get_bd_pins ps7/IRQ_F2P]
connect_bd_net [get_bd_pins clocks/core_clk] [get_bd_pins pl_core/clk] [get_bd_pins ps7/M_AXI_GP0_ACLK] [get_bd_pins reset/slowest_sync_clk] [get_bd_pins task_bram/s_axi_aclk] [get_bd_pins service_io/s_axi_aclk] [get_bd_pins i2c_mux/s_axi_aclk] [get_bd_pins interconnect/ACLK] [get_bd_pins interconnect/S00_ACLK] [get_bd_pins interconnect/M00_ACLK] [get_bd_pins interconnect/M01_ACLK] [get_bd_pins interconnect/M02_ACLK] [get_bd_pins interconnect/M03_ACLK]
connect_bd_net [get_bd_pins clocks/tx_clk] [get_bd_pins pl_core/tx_clk]
connect_bd_net [get_bd_pins clocks/locked] [get_bd_pins reset/dcm_locked]
connect_bd_net [get_bd_pins ps7/FCLK_RESET0_N] [get_bd_pins reset/ext_reset_in]
connect_bd_net [get_bd_pins reset/peripheral_aresetn] [get_bd_pins pl_core/rst_n] [get_bd_pins task_bram/s_axi_aresetn] [get_bd_pins service_io/s_axi_aresetn] [get_bd_pins i2c_mux/s_axi_aresetn]
connect_bd_net [get_bd_pins reset/interconnect_aresetn] [get_bd_pins interconnect/ARESETN] [get_bd_pins interconnect/S00_ARESETN] [get_bd_pins interconnect/M00_ARESETN] [get_bd_pins interconnect/M01_ARESETN] [get_bd_pins interconnect/M02_ARESETN] [get_bd_pins interconnect/M03_ARESETN]
make_bd_intf_pins_external [get_bd_intf_pins ps7/FIXED_IO]
make_bd_intf_pins_external [get_bd_intf_pins i2c_mux/IIC]
make_bd_pins_external [get_bd_pins clocks/ref_clk50]
foreach p {physical_health adc_busy adc_dout adc_reset adc_convst adc_cs_n adc_sclk adc_sdi rx_blank serial_data shift_clock latch_clock output_disable heartbeat efuse_up efuse_dn} {make_bd_pins_external [get_bd_pins pl_core/$p]}
foreach {slave offset} {pl_core/S_AXI/reg0 0x40000000 task_bram/S_AXI/Mem0 0x42000000 service_io/S_AXI/Reg 0x41200000 i2c_mux/S_AXI/Reg 0x41600000} {assign_bd_address -offset $offset -range 0x00010000 -target_address_space [get_bd_addr_spaces ps7/Data] [get_bd_addr_segs $slave] -force}
validate_bd_design
save_bd_design
set_property synth_checkpoint_mode None [get_files draw_ready_ps.bd]
generate_target all [get_files draw_ready_ps.bd]
make_wrapper -files [get_files draw_ready_ps.bd] -top -import
set_property top draw_ready_ps_wrapper [current_fileset]
write_bd_tcl -force [file join $resultdir NATIVE_PS_RECREATE.tcl]
write_hw_platform -fixed -force -file [file join $resultdir DRAW_READY_PLATFORM.xsa]
puts "NATIVE_BD_CREATED"
read_xdc [file join $root hardware constraints ax7020_draw_ready.xdc]
set_property STEPS.SYNTH_DESIGN.ARGS.FLATTEN_HIERARCHY rebuilt [get_runs synth_1]
launch_runs synth_1 -jobs 4
wait_on_run synth_1
open_run synth_1
report_timing_summary -file [file join $resultdir NATIVE_SYNTH_TIMING.rpt]
write_checkpoint -force [file join $resultdir NATIVE_SYNTH.dcp]
launch_runs impl_1 -to_step route_design -jobs 4
wait_on_run impl_1
open_run impl_1
#Physical optimization replicates the RCLK FF: the pad replica retains IOB,
#while the internal completion-tracking FF must not carry an invalid annotation.
foreach c [get_cells -hier -filter {NAME =~ *tx44*serial*tx*latch_clock_reg}] {
 set ends [all_fanout -from [get_pins $c/Q] -endpoints_only]
 if {![regexp {OBUF|latch_clock_0} $ends]} {set_property IOB FALSE $c}
}
report_timing_summary -delay_type min_max -report_unconstrained -file [file join $resultdir NATIVE_ROUTED_TIMING.rpt]
report_drc -file [file join $resultdir NATIVE_ROUTED_DRC.rpt]
report_methodology -file [file join $resultdir NATIVE_METHODOLOGY.rpt]
report_clock_interaction -file [file join $resultdir NATIVE_CLOCK_INTERACTION.rpt]
report_cdc -file [file join $resultdir NATIVE_CDC.rpt]
report_io -file [file join $resultdir NATIVE_PHYSICAL_IO.rpt]
report_utilization -file [file join $resultdir NATIVE_UTILIZATION.rpt]
write_checkpoint -force [file join $resultdir NATIVE_ROUTED.dcp]
set f [open [file join $resultdir NATIVE_IMPLEMENTATION_STATUS.txt] w]
puts $f [get_property STATUS [get_runs impl_1]]
puts $f "SETUP [get_property SLACK [get_timing_paths -delay_type max -max_paths 1]]"
puts $f "HOLD [get_property SLACK [get_timing_paths -delay_type min -max_paths 1]]"
close $f
puts "NATIVE_ROUTE_COMPLETE_NO_BITSTREAM_OR_BOARD_PROGRAM"

