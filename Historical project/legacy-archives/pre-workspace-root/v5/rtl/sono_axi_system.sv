`timescale 1ns/1ps
// Offline integration top, NOT a board pinout or a downloadable smoke-test top.
// One synchronous AXI/native clock. Physical PS clock conversion/CDC is not inferred.
module sono_axi_system #(parameter integer POWER_WAIT_CYCLES=264000001)(
 input wire clk,rst_n,hardware_enable,motion_arm,motion_stop,
 input wire frame_valid,input wire[2175:0]frame_data,input wire[31:0]frame_sequence,input wire frame_last,
 output wire frame_ready,output wire[31:0]buffered_count,acknowledged_sequence,
 output wire motion_running,motion_done,motion_underflow,motion_overflow,motion_invalid,motion_timeout,
 output wire motion_request_pulse,motion_ack_pulse,
 input wire[31:0]s_awaddr,input wire s_awvalid,output wire s_awready,
 input wire[31:0]s_wdata,input wire[3:0]s_wstrb,input wire s_wvalid,output wire s_wready,
 output wire[1:0]s_bresp,output wire s_bvalid,input wire s_bready,
 input wire[31:0]s_araddr,input wire s_arvalid,output wire s_arready,
 output wire[31:0]s_rdata,output wire[1:0]s_rresp,output wire s_rvalid,input wire s_rready,
 input wire adc_busy,input wire[3:0]adc_dout,
 output wire adc_reset,adc_convst,adc_cs_n,adc_sclk,adc_sdi,
 output wire[1:0]rx_blank,output wire[31:0]serial_data,
 output wire shift_clock,latch_clock,output_disable,output wire[127:0]commanded_waveform,output wire irq);
 wire bus_valid,bus_write,bus_ready,bus_error,native_irq;
 wire[7:0]bus_address;wire[31:0]bus_wdata,bus_rdata;
 axi_native_bridge bridge(.*);
 sono_motion_system #(.POWER_WAIT_CYCLES(POWER_WAIT_CYCLES)) native_system(.*, .irq(native_irq));
endmodule
