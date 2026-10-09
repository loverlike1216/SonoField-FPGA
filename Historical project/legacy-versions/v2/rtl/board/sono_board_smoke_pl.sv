`timescale 1ns/1ps
// Safe PS-facing PL leaf. clk/rst_n and AXI are internal PS/PL nets,
// not connector pads. No acoustic/ADC/motion signal exists at this boundary.
module sono_board_smoke_pl # (parameter integer POWER_WAIT_CYCLES=264000001)(
 input wire clk,rst_n,
 input wire[31:0]s_awaddr,input wire s_awvalid,output wire s_awready,
 input wire[31:0]s_wdata,input wire[3:0]s_wstrb,input wire s_wvalid,output wire s_wready,
 output wire[1:0]s_bresp,output wire s_bvalid,input wire s_bready,
 input wire[31:0]s_araddr,input wire s_arvalid,output wire s_arready,
 output wire[31:0]s_rdata,output wire[1:0]s_rresp,output wire s_rvalid,input wire s_rready);
 wire irq;
 sono_axi_system #(.POWER_WAIT_CYCLES(POWER_WAIT_CYCLES)) system(
 .clk(clk),.rst_n(rst_n),.hardware_enable(1'b0),.motion_arm(1'b0),.motion_stop(1'b1),
 .frame_valid(1'b0),.frame_data(2176'b0),.frame_sequence(32'b0),.frame_last(1'b0),
 .s_awaddr(s_awaddr),.s_awvalid(s_awvalid),.s_awready(s_awready),
 .s_wdata(s_wdata),.s_wstrb(s_wstrb),.s_wvalid(s_wvalid),.s_wready(s_wready),
 .s_bresp(s_bresp),.s_bvalid(s_bvalid),.s_bready(s_bready),
 .s_araddr(s_araddr),.s_arvalid(s_arvalid),.s_arready(s_arready),
 .s_rdata(s_rdata),.s_rresp(s_rresp),.s_rvalid(s_rvalid),.s_rready(s_rready),
 .adc_busy(1'b0),.adc_dout(4'b0),.irq(irq));
endmodule
