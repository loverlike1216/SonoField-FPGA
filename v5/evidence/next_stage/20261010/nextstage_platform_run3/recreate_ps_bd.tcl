
################################################################
# This is a generated script based on design: prepcb_ps
#
# Though there are limitations about the generated script,
# the main purpose of this utility is to make learning
# IP Integrator Tcl commands easier.
################################################################

namespace eval _tcl {
proc get_script_folder {} {
   set script_path [file normalize [info script]]
   set script_folder [file dirname $script_path]
   return $script_folder
}
}
variable script_folder
set script_folder [_tcl::get_script_folder]

################################################################
# Check if script is running in correct Vivado version.
################################################################
set scripts_vivado_version 2025.2
set current_vivado_version [version -short]

if { [string first $scripts_vivado_version $current_vivado_version] == -1 } {
   puts ""
   if { [string compare $scripts_vivado_version $current_vivado_version] > 0 } {
      catch {common::send_gid_msg -ssname BD::TCL -id 2042 -severity "ERROR" " This script was generated using Vivado <$scripts_vivado_version> and is being run in <$current_vivado_version> of Vivado. Sourcing the script failed since it was created with a future version of Vivado."}

   } else {
     catch {common::send_gid_msg -ssname BD::TCL -id 2041 -severity "ERROR" "This script was generated using Vivado <$scripts_vivado_version> and is being run in <$current_vivado_version> of Vivado. Please run the script in Vivado <$scripts_vivado_version> then open the design in Vivado <$current_vivado_version>. Upgrade the design by running \"Tools => Report => Report IP Status...\", then run write_bd_tcl to create an updated script."}

   }

   return 1
}

################################################################
# START
################################################################

# To test this script, run the following commands from Vivado Tcl console:
# source prepcb_ps_script.tcl


# The design that will be created by this Tcl script contains the following 
# module references:
# nextstage_pl

# Please add the sources of those modules before sourcing this Tcl script.

# If there is no project opened, this script will create a
# project, but make sure you do not have an existing project
# <./myproj/project_1.xpr> in the current working folder.

set list_projs [get_projects -quiet]
if { $list_projs eq "" } {
   create_project project_1 myproj -part xc7z020clg400-2
}


# CHANGE DESIGN NAME HERE
variable design_name
set design_name prepcb_ps

# If you do not already have an existing IP Integrator design open,
# you can create a design using the following command:
#    create_bd_design $design_name

# Creating design if needed
set errMsg ""
set nRet 0

set cur_design [current_bd_design -quiet]
set list_cells [get_bd_cells -quiet]

if { ${design_name} eq "" } {
   # USE CASES:
   #    1) Design_name not set

   set errMsg "Please set the variable <design_name> to a non-empty value."
   set nRet 1

} elseif { ${cur_design} ne "" && ${list_cells} eq "" } {
   # USE CASES:
   #    2): Current design opened AND is empty AND names same.
   #    3): Current design opened AND is empty AND names diff; design_name NOT in project.
   #    4): Current design opened AND is empty AND names diff; design_name exists in project.

   if { $cur_design ne $design_name } {
      common::send_gid_msg -ssname BD::TCL -id 2001 -severity "INFO" "Changing value of <design_name> from <$design_name> to <$cur_design> since current design is empty."
      set design_name [get_property NAME $cur_design]
   }
   common::send_gid_msg -ssname BD::TCL -id 2002 -severity "INFO" "Constructing design in IPI design <$cur_design>..."

} elseif { ${cur_design} ne "" && $list_cells ne "" && $cur_design eq $design_name } {
   # USE CASES:
   #    5) Current design opened AND has components AND same names.

   set errMsg "Design <$design_name> already exists in your project, please set the variable <design_name> to another value."
   set nRet 1
} elseif { [get_files -quiet ${design_name}.bd] ne "" } {
   # USE CASES: 
   #    6) Current opened design, has components, but diff names, design_name exists in project.
   #    7) No opened design, design_name exists in project.

   set errMsg "Design <$design_name> already exists in your project, please set the variable <design_name> to another value."
   set nRet 2

} else {
   # USE CASES:
   #    8) No opened design, design_name not in project.
   #    9) Current opened design, has components, but diff names, design_name not in project.

   common::send_gid_msg -ssname BD::TCL -id 2003 -severity "INFO" "Currently there is no design <$design_name> in project, so creating one..."

   create_bd_design $design_name

   common::send_gid_msg -ssname BD::TCL -id 2004 -severity "INFO" "Making design <$design_name> as current_bd_design."
   current_bd_design $design_name

}

common::send_gid_msg -ssname BD::TCL -id 2005 -severity "INFO" "Currently the variable <design_name> is equal to \"$design_name\"."

if { $nRet != 0 } {
   catch {common::send_gid_msg -ssname BD::TCL -id 2006 -severity "ERROR" $errMsg}
   return $nRet
}

set bCheckIPsPassed 1
##################################################################
# CHECK IPs
##################################################################
set bCheckIPs 1
if { $bCheckIPs == 1 } {
   set list_check_ips "\ 
xilinx.com:ip:processing_system7:5.5\
xilinx.com:ip:axi_bram_ctrl:4.1\
xilinx.com:ip:blk_mem_gen:8.4\
xilinx.com:ip:axi_gpio:2.0\
xilinx.com:ip:proc_sys_reset:5.0\
xilinx.com:ip:xlslice:1.0\
xilinx.com:ip:xlconcat:2.1\
xilinx.com:ip:axi_iic:2.1\
"

   set list_ips_missing ""
   common::send_gid_msg -ssname BD::TCL -id 2011 -severity "INFO" "Checking if the following IPs exist in the project's IP catalog: $list_check_ips ."

   foreach ip_vlnv $list_check_ips {
      set ip_obj [get_ipdefs -all $ip_vlnv]
      if { $ip_obj eq "" } {
         lappend list_ips_missing $ip_vlnv
      }
   }

   if { $list_ips_missing ne "" } {
      catch {common::send_gid_msg -ssname BD::TCL -id 2012 -severity "ERROR" "The following IPs are not found in the IP Catalog:\n  $list_ips_missing\n\nResolution: Please add the repository containing the IP(s) to the project." }
      set bCheckIPsPassed 0
   }

}

##################################################################
# CHECK Modules
##################################################################
set bCheckModules 1
if { $bCheckModules == 1 } {
   set list_check_mods "\ 
nextstage_pl\
"

   set list_mods_missing ""
   common::send_gid_msg -ssname BD::TCL -id 2020 -severity "INFO" "Checking if the following modules exist in the project's sources: $list_check_mods ."

   foreach mod_vlnv $list_check_mods {
      if { [can_resolve_reference $mod_vlnv] == 0 } {
         lappend list_mods_missing $mod_vlnv
      }
   }

   if { $list_mods_missing ne "" } {
      catch {common::send_gid_msg -ssname BD::TCL -id 2021 -severity "ERROR" "The following module(s) are not found in the project: $list_mods_missing" }
      common::send_gid_msg -ssname BD::TCL -id 2022 -severity "INFO" "Please add source files for the missing module(s) above."
      set bCheckIPsPassed 0
   }
}

if { $bCheckIPsPassed != 1 } {
  common::send_gid_msg -ssname BD::TCL -id 2023 -severity "WARNING" "Will not continue with creation of design due to the error(s) above."
  return 3
}

##################################################################
# DESIGN PROCs
##################################################################



# Procedure to create entire design; Provide argument to make
# procedure reusable. If parentCell is "", will use root.
proc create_root_design { parentCell } {

  variable script_folder
  variable design_name

  if { $parentCell eq "" } {
     set parentCell [get_bd_cells /]
  }

  # Get object for parentCell
  set parentObj [get_bd_cells $parentCell]
  if { $parentObj == "" } {
     catch {common::send_gid_msg -ssname BD::TCL -id 2090 -severity "ERROR" "Unable to find parent cell <$parentCell>!"}
     return
  }

  # Make sure parentObj is hier blk
  set parentType [get_property TYPE $parentObj]
  if { $parentType ne "hier" } {
     catch {common::send_gid_msg -ssname BD::TCL -id 2091 -severity "ERROR" "Parent <$parentObj> has TYPE = <$parentType>. Expected to be <hier>."}
     return
  }

  # Save current instance; Restore later
  set oldCurInst [current_bd_instance .]

  # Set parent object as current
  current_bd_instance $parentObj


  # Create interface ports
  set IIC_0 [ create_bd_intf_port -mode Master -vlnv xilinx.com:interface:iic_rtl:1.0 IIC_0 ]

  set IIC_1 [ create_bd_intf_port -mode Master -vlnv xilinx.com:interface:iic_rtl:1.0 IIC_1 ]

  set IIC_2 [ create_bd_intf_port -mode Master -vlnv xilinx.com:interface:iic_rtl:1.0 IIC_2 ]

  set FIXED_IO_0 [ create_bd_intf_port -mode Master -vlnv xilinx.com:display_processing_system7:fixedio_rtl:1.0 FIXED_IO_0 ]


  # Create ports
  set health_0 [ create_bd_port -dir I -from 7 -to 0 health_0 ]
  set adc_busy_0 [ create_bd_port -dir I adc_busy_0 ]
  set adc_dout_0 [ create_bd_port -dir I -from 3 -to 0 adc_dout_0 ]
  set adc_reset_0 [ create_bd_port -dir O -type rst adc_reset_0 ]
  set adc_convst_0 [ create_bd_port -dir O adc_convst_0 ]
  set adc_cs_n_0 [ create_bd_port -dir O adc_cs_n_0 ]
  set adc_sclk_0 [ create_bd_port -dir O adc_sclk_0 ]
  set adc_sdi_0 [ create_bd_port -dir O adc_sdi_0 ]
  set rx_blank_0 [ create_bd_port -dir O -from 1 -to 0 rx_blank_0 ]
  set serial_data_0 [ create_bd_port -dir O -from 31 -to 0 serial_data_0 ]
  set shift_clock_0 [ create_bd_port -dir O shift_clock_0 ]
  set latch_clock_0 [ create_bd_port -dir O latch_clock_0 ]
  set output_disable_0 [ create_bd_port -dir O output_disable_0 ]
  set heartbeat_0 [ create_bd_port -dir O heartbeat_0 ]
  set efuse_up_0 [ create_bd_port -dir O efuse_up_0 ]
  set efuse_dn_0 [ create_bd_port -dir O efuse_dn_0 ]

  # Create instance: ps7, and set properties
  set ps7 [ create_bd_cell -type ip -vlnv xilinx.com:ip:processing_system7:5.5 ps7 ]
  set_property -dict [list \
    CONFIG.PCW_ACT_APU_PERIPHERAL_FREQMHZ {666.666687} \
    CONFIG.PCW_ACT_CAN_PERIPHERAL_FREQMHZ {10.000000} \
    CONFIG.PCW_ACT_DCI_PERIPHERAL_FREQMHZ {10.158730} \
    CONFIG.PCW_ACT_ENET0_PERIPHERAL_FREQMHZ {10.000000} \
    CONFIG.PCW_ACT_ENET1_PERIPHERAL_FREQMHZ {10.000000} \
    CONFIG.PCW_ACT_FPGA0_PERIPHERAL_FREQMHZ {128.571426} \
    CONFIG.PCW_ACT_FPGA1_PERIPHERAL_FREQMHZ {10.000000} \
    CONFIG.PCW_ACT_FPGA2_PERIPHERAL_FREQMHZ {10.000000} \
    CONFIG.PCW_ACT_FPGA3_PERIPHERAL_FREQMHZ {10.000000} \
    CONFIG.PCW_ACT_PCAP_PERIPHERAL_FREQMHZ {200.000000} \
    CONFIG.PCW_ACT_QSPI_PERIPHERAL_FREQMHZ {10.000000} \
    CONFIG.PCW_ACT_SDIO_PERIPHERAL_FREQMHZ {10.000000} \
    CONFIG.PCW_ACT_SMC_PERIPHERAL_FREQMHZ {10.000000} \
    CONFIG.PCW_ACT_SPI_PERIPHERAL_FREQMHZ {10.000000} \
    CONFIG.PCW_ACT_TPIU_PERIPHERAL_FREQMHZ {200.000000} \
    CONFIG.PCW_ACT_TTC0_CLK0_PERIPHERAL_FREQMHZ {111.111115} \
    CONFIG.PCW_ACT_TTC0_CLK1_PERIPHERAL_FREQMHZ {111.111115} \
    CONFIG.PCW_ACT_TTC0_CLK2_PERIPHERAL_FREQMHZ {111.111115} \
    CONFIG.PCW_ACT_TTC1_CLK0_PERIPHERAL_FREQMHZ {111.111115} \
    CONFIG.PCW_ACT_TTC1_CLK1_PERIPHERAL_FREQMHZ {111.111115} \
    CONFIG.PCW_ACT_TTC1_CLK2_PERIPHERAL_FREQMHZ {111.111115} \
    CONFIG.PCW_ACT_UART_PERIPHERAL_FREQMHZ {100.000000} \
    CONFIG.PCW_ACT_WDT_PERIPHERAL_FREQMHZ {111.111115} \
    CONFIG.PCW_CLK0_FREQ {128571426} \
    CONFIG.PCW_CLK1_FREQ {10000000} \
    CONFIG.PCW_CLK2_FREQ {10000000} \
    CONFIG.PCW_CLK3_FREQ {10000000} \
    CONFIG.PCW_EN_CLK0_PORT {1} \
    CONFIG.PCW_EN_DDR {0} \
    CONFIG.PCW_EN_UART1 {1} \
    CONFIG.PCW_FCLK_CLK0_BUF {TRUE} \
    CONFIG.PCW_FPGA0_PERIPHERAL_FREQMHZ {132} \
    CONFIG.PCW_FPGA_FCLK0_ENABLE {1} \
    CONFIG.PCW_IRQ_F2P_INTR {1} \
    CONFIG.PCW_MIO_48_IOTYPE {LVCMOS 3.3V} \
    CONFIG.PCW_MIO_48_PULLUP {enabled} \
    CONFIG.PCW_MIO_48_SLEW {slow} \
    CONFIG.PCW_MIO_49_IOTYPE {LVCMOS 3.3V} \
    CONFIG.PCW_MIO_49_PULLUP {enabled} \
    CONFIG.PCW_MIO_49_SLEW {slow} \
    CONFIG.PCW_MIO_TREE_PERIPHERALS {unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#UART\
1#UART 1#unassigned#unassigned#unassigned#unassigned} \
    CONFIG.PCW_MIO_TREE_SIGNALS {unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#unassigned#tx#rx#unassigned#unassigned#unassigned#unassigned}\
\
    CONFIG.PCW_UART1_GRP_FULL_ENABLE {0} \
    CONFIG.PCW_UART1_PERIPHERAL_ENABLE {1} \
    CONFIG.PCW_UART1_UART1_IO {MIO 48 .. 49} \
    CONFIG.PCW_UART_PERIPHERAL_FREQMHZ {100} \
    CONFIG.PCW_UART_PERIPHERAL_VALID {1} \
    CONFIG.PCW_UIPARAM_ACT_DDR_FREQ_MHZ {533.333374} \
    CONFIG.PCW_UIPARAM_DDR_ENABLE {0} \
    CONFIG.PCW_USE_FABRIC_INTERRUPT {1} \
    CONFIG.PCW_USE_M_AXI_GP0 {1} \
  ] $ps7


  # Create instance: interconnect, and set properties
  set interconnect [ create_bd_cell -type ip -vlnv xilinx.com:ip:axi_interconnect:2.1 interconnect ]
  set_property CONFIG.NUM_MI {6} $interconnect


  # Create instance: task_bram, and set properties
  set task_bram [ create_bd_cell -type ip -vlnv xilinx.com:ip:axi_bram_ctrl:4.1 task_bram ]
  set_property -dict [list \
    CONFIG.DATA_WIDTH {32} \
    CONFIG.SINGLE_PORT_BRAM {1} \
  ] $task_bram


  # Create instance: task_memory, and set properties
  set task_memory [ create_bd_cell -type ip -vlnv xilinx.com:ip:blk_mem_gen:8.4 task_memory ]
  set_property -dict [list \
    CONFIG.Memory_Type {True_Dual_Port_RAM} \
    CONFIG.Register_PortB_Output_of_Memory_Primitives {false} \
  ] $task_memory


  # Create instance: service_io, and set properties
  set service_io [ create_bd_cell -type ip -vlnv xilinx.com:ip:axi_gpio:2.0 service_io ]
  set_property -dict [list \
    CONFIG.C_ALL_INPUTS_2 {1} \
    CONFIG.C_ALL_OUTPUTS {1} \
    CONFIG.C_GPIO2_WIDTH {32} \
    CONFIG.C_GPIO_WIDTH {32} \
    CONFIG.C_INTERRUPT_PRESENT {1} \
    CONFIG.C_IS_DUAL {1} \
  ] $service_io


  # Create instance: reset, and set properties
  set reset [ create_bd_cell -type ip -vlnv xilinx.com:ip:proc_sys_reset:5.0 reset ]

  # Create instance: pl_core, and set properties
  set block_name nextstage_pl
  set block_cell_name pl_core
  if { [catch {set pl_core [create_bd_cell -type module -reference $block_name $block_cell_name] } errmsg] } {
     catch {common::send_gid_msg -ssname BD::TCL -id 2095 -severity "ERROR" "Unable to add referenced block <$block_name>. Please add the files for ${block_name}'s definition into the project."}
     return 1
   } elseif { $pl_core eq "" } {
     catch {common::send_gid_msg -ssname BD::TCL -id 2096 -severity "ERROR" "Unable to referenced block <$block_name>. Please add the files for ${block_name}'s definition into the project."}
     return 1
   }
  
  # Create instance: control_slice, and set properties
  set control_slice [ create_bd_cell -type ip -vlnv xilinx.com:ip:xlslice:1.0 control_slice ]
  set_property -dict [list \
    CONFIG.DIN_FROM {15} \
    CONFIG.DIN_TO {0} \
    CONFIG.DIN_WIDTH {32} \
    CONFIG.DOUT_WIDTH {16} \
  ] $control_slice


  # Create instance: irq_concat, and set properties
  set irq_concat [ create_bd_cell -type ip -vlnv xilinx.com:ip:xlconcat:2.1 irq_concat ]
  set_property CONFIG.NUM_PORTS {5} $irq_concat


  # Create instance: i2c_center, and set properties
  set i2c_center [ create_bd_cell -type ip -vlnv xilinx.com:ip:axi_iic:2.1 i2c_center ]

  # Create instance: i2c_upper, and set properties
  set i2c_upper [ create_bd_cell -type ip -vlnv xilinx.com:ip:axi_iic:2.1 i2c_upper ]

  # Create instance: i2c_lower, and set properties
  set i2c_lower [ create_bd_cell -type ip -vlnv xilinx.com:ip:axi_iic:2.1 i2c_lower ]

  # Create interface connections
  connect_bd_intf_net -intf_net i2c_center_IIC [get_bd_intf_ports IIC_0] [get_bd_intf_pins i2c_center/IIC]
  connect_bd_intf_net -intf_net i2c_lower_IIC [get_bd_intf_ports IIC_2] [get_bd_intf_pins i2c_lower/IIC]
  connect_bd_intf_net -intf_net i2c_upper_IIC [get_bd_intf_ports IIC_1] [get_bd_intf_pins i2c_upper/IIC]
  connect_bd_intf_net -intf_net interconnect_M00_AXI [get_bd_intf_pins interconnect/M00_AXI] [get_bd_intf_pins task_bram/S_AXI]
  connect_bd_intf_net -intf_net interconnect_M01_AXI [get_bd_intf_pins interconnect/M01_AXI] [get_bd_intf_pins service_io/S_AXI]
  connect_bd_intf_net -intf_net interconnect_M02_AXI [get_bd_intf_pins interconnect/M02_AXI] [get_bd_intf_pins pl_core/S_AXI]
  connect_bd_intf_net -intf_net interconnect_M03_AXI [get_bd_intf_pins interconnect/M03_AXI] [get_bd_intf_pins i2c_center/S_AXI]
  connect_bd_intf_net -intf_net interconnect_M04_AXI [get_bd_intf_pins interconnect/M04_AXI] [get_bd_intf_pins i2c_upper/S_AXI]
  connect_bd_intf_net -intf_net interconnect_M05_AXI [get_bd_intf_pins interconnect/M05_AXI] [get_bd_intf_pins i2c_lower/S_AXI]
  connect_bd_intf_net -intf_net ps7_FIXED_IO [get_bd_intf_ports FIXED_IO_0] [get_bd_intf_pins ps7/FIXED_IO]
  connect_bd_intf_net -intf_net ps7_M_AXI_GP0 [get_bd_intf_pins ps7/M_AXI_GP0] [get_bd_intf_pins interconnect/S00_AXI]
  connect_bd_intf_net -intf_net task_bram_BRAM_PORTA [get_bd_intf_pins task_bram/BRAM_PORTA] [get_bd_intf_pins task_memory/BRAM_PORTA]

  # Create port connections
  connect_bd_net -net adc_busy_0_1  [get_bd_ports adc_busy_0] \
  [get_bd_pins pl_core/adc_busy]
  connect_bd_net -net adc_dout_0_1  [get_bd_ports adc_dout_0] \
  [get_bd_pins pl_core/adc_dout]
  connect_bd_net -net control_slice_Dout  [get_bd_pins control_slice/Dout] \
  [get_bd_pins pl_core/control]
  connect_bd_net -net health_0_1  [get_bd_ports health_0] \
  [get_bd_pins pl_core/health]
  connect_bd_net -net i2c_center_iic2intc_irpt  [get_bd_pins i2c_center/iic2intc_irpt] \
  [get_bd_pins irq_concat/In2]
  connect_bd_net -net i2c_lower_iic2intc_irpt  [get_bd_pins i2c_lower/iic2intc_irpt] \
  [get_bd_pins irq_concat/In4]
  connect_bd_net -net i2c_upper_iic2intc_irpt  [get_bd_pins i2c_upper/iic2intc_irpt] \
  [get_bd_pins irq_concat/In3]
  connect_bd_net -net irq_concat_dout  [get_bd_pins irq_concat/dout] \
  [get_bd_pins ps7/IRQ_F2P]
  connect_bd_net -net pl_core_adc_convst  [get_bd_pins pl_core/adc_convst] \
  [get_bd_ports adc_convst_0]
  connect_bd_net -net pl_core_adc_cs_n  [get_bd_pins pl_core/adc_cs_n] \
  [get_bd_ports adc_cs_n_0]
  connect_bd_net -net pl_core_adc_reset  [get_bd_pins pl_core/adc_reset] \
  [get_bd_ports adc_reset_0]
  connect_bd_net -net pl_core_adc_sclk  [get_bd_pins pl_core/adc_sclk] \
  [get_bd_ports adc_sclk_0]
  connect_bd_net -net pl_core_adc_sdi  [get_bd_pins pl_core/adc_sdi] \
  [get_bd_ports adc_sdi_0]
  connect_bd_net -net pl_core_bram_addr  [get_bd_pins pl_core/bram_addr] \
  [get_bd_pins task_memory/addrb]
  connect_bd_net -net pl_core_bram_clk  [get_bd_pins pl_core/bram_clk] \
  [get_bd_pins task_memory/clkb]
  connect_bd_net -net pl_core_bram_en  [get_bd_pins pl_core/bram_en] \
  [get_bd_pins task_memory/enb]
  connect_bd_net -net pl_core_bram_rst  [get_bd_pins pl_core/bram_rst] \
  [get_bd_pins task_memory/rstb]
  connect_bd_net -net pl_core_bram_we  [get_bd_pins pl_core/bram_we] \
  [get_bd_pins task_memory/web]
  connect_bd_net -net pl_core_bram_wrdata  [get_bd_pins pl_core/bram_wrdata] \
  [get_bd_pins task_memory/dinb]
  connect_bd_net -net pl_core_efuse_dn  [get_bd_pins pl_core/efuse_dn] \
  [get_bd_ports efuse_dn_0]
  connect_bd_net -net pl_core_efuse_up  [get_bd_pins pl_core/efuse_up] \
  [get_bd_ports efuse_up_0]
  connect_bd_net -net pl_core_heartbeat  [get_bd_pins pl_core/heartbeat] \
  [get_bd_ports heartbeat_0]
  connect_bd_net -net pl_core_irq  [get_bd_pins pl_core/irq] \
  [get_bd_pins irq_concat/In0]
  connect_bd_net -net pl_core_latch_clock  [get_bd_pins pl_core/latch_clock] \
  [get_bd_ports latch_clock_0]
  connect_bd_net -net pl_core_output_disable  [get_bd_pins pl_core/output_disable] \
  [get_bd_ports output_disable_0]
  connect_bd_net -net pl_core_rx_blank  [get_bd_pins pl_core/rx_blank] \
  [get_bd_ports rx_blank_0]
  connect_bd_net -net pl_core_serial_data  [get_bd_pins pl_core/serial_data] \
  [get_bd_ports serial_data_0]
  connect_bd_net -net pl_core_shift_clock  [get_bd_pins pl_core/shift_clock] \
  [get_bd_ports shift_clock_0]
  connect_bd_net -net pl_core_status  [get_bd_pins pl_core/status] \
  [get_bd_pins service_io/gpio2_io_i]
  connect_bd_net -net ps7_FCLK_CLK0  [get_bd_pins ps7/FCLK_CLK0] \
  [get_bd_pins i2c_center/s_axi_aclk] \
  [get_bd_pins i2c_upper/s_axi_aclk] \
  [get_bd_pins i2c_lower/s_axi_aclk] \
  [get_bd_pins ps7/M_AXI_GP0_ACLK] \
  [get_bd_pins interconnect/ACLK] \
  [get_bd_pins interconnect/S00_ACLK] \
  [get_bd_pins interconnect/M00_ACLK] \
  [get_bd_pins interconnect/M01_ACLK] \
  [get_bd_pins task_bram/s_axi_aclk] \
  [get_bd_pins service_io/s_axi_aclk] \
  [get_bd_pins reset/slowest_sync_clk] \
  [get_bd_pins pl_core/clk] \
  [get_bd_pins interconnect/M02_ACLK] \
  [get_bd_pins interconnect/M03_ACLK] \
  [get_bd_pins interconnect/M04_ACLK] \
  [get_bd_pins interconnect/M05_ACLK]
  connect_bd_net -net ps7_FCLK_RESET0_N  [get_bd_pins ps7/FCLK_RESET0_N] \
  [get_bd_pins reset/ext_reset_in]
  connect_bd_net -net reset_interconnect_aresetn  [get_bd_pins reset/interconnect_aresetn] \
  [get_bd_pins interconnect/ARESETN] \
  [get_bd_pins interconnect/S00_ARESETN] \
  [get_bd_pins interconnect/M00_ARESETN] \
  [get_bd_pins interconnect/M01_ARESETN]
  connect_bd_net -net reset_peripheral_aresetn  [get_bd_pins reset/peripheral_aresetn] \
  [get_bd_pins i2c_center/s_axi_aresetn] \
  [get_bd_pins i2c_upper/s_axi_aresetn] \
  [get_bd_pins i2c_lower/s_axi_aresetn] \
  [get_bd_pins task_bram/s_axi_aresetn] \
  [get_bd_pins service_io/s_axi_aresetn] \
  [get_bd_pins pl_core/rst_n] \
  [get_bd_pins interconnect/M02_ARESETN] \
  [get_bd_pins interconnect/M03_ARESETN] \
  [get_bd_pins interconnect/M04_ARESETN] \
  [get_bd_pins interconnect/M05_ARESETN]
  connect_bd_net -net service_io_gpio_io_o  [get_bd_pins service_io/gpio_io_o] \
  [get_bd_pins control_slice/Din]
  connect_bd_net -net service_io_ip2intc_irpt  [get_bd_pins service_io/ip2intc_irpt] \
  [get_bd_pins irq_concat/In1]
  connect_bd_net -net task_memory_doutb  [get_bd_pins task_memory/doutb] \
  [get_bd_pins pl_core/bram_rddata]

  # Create address segments
  assign_bd_address -offset 0x41600000 -range 0x00010000 -target_address_space [get_bd_addr_spaces ps7/Data] [get_bd_addr_segs i2c_center/S_AXI/Reg] -force
  assign_bd_address -offset 0x41620000 -range 0x00010000 -target_address_space [get_bd_addr_spaces ps7/Data] [get_bd_addr_segs i2c_lower/S_AXI/Reg] -force
  assign_bd_address -offset 0x41610000 -range 0x00010000 -target_address_space [get_bd_addr_spaces ps7/Data] [get_bd_addr_segs i2c_upper/S_AXI/Reg] -force
  assign_bd_address -offset 0x40000000 -range 0x00010000 -target_address_space [get_bd_addr_spaces ps7/Data] [get_bd_addr_segs pl_core/S_AXI/reg0] -force
  assign_bd_address -offset 0x41200000 -range 0x00010000 -target_address_space [get_bd_addr_spaces ps7/Data] [get_bd_addr_segs service_io/S_AXI/Reg] -force
  assign_bd_address -offset 0x42000000 -range 0x00010000 -target_address_space [get_bd_addr_spaces ps7/Data] [get_bd_addr_segs task_bram/S_AXI/Mem0] -force


  # Restore current instance
  current_bd_instance $oldCurInst

  validate_bd_design
  save_bd_design
}
# End of create_root_design()


##################################################################
# MAIN FLOW
##################################################################

create_root_design ""


