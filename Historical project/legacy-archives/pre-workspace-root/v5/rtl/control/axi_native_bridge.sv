`timescale 1ns/1ps
// One AXI4-Lite transaction in flight. AW/W are buffered independently.
// Native bus has combinational ready/read and registered error: capture error
// one cycle AFTER native acceptance. Ownership errors can occur without ready.
module axi_native_bridge #(parameter integer TIMEOUT_CYCLES=64)(
 input wire clk,rst_n,
 input wire [31:0] s_awaddr,input wire s_awvalid,output wire s_awready,
 input wire [31:0] s_wdata,input wire [3:0] s_wstrb,input wire s_wvalid,output wire s_wready,
 output reg [1:0] s_bresp,output reg s_bvalid,input wire s_bready,
 input wire [31:0] s_araddr,input wire s_arvalid,output wire s_arready,
 output reg [31:0] s_rdata,output reg [1:0] s_rresp,output reg s_rvalid,input wire s_rready,
 output wire bus_valid,output reg bus_write,output reg [7:0] bus_address,output reg [31:0] bus_wdata,
 input wire [31:0] bus_rdata,input wire bus_ready,bus_error,input wire native_irq,output wire irq);
 localparam IDLE=0,ISSUE=1,CAPTURE=2,RESPOND=3;
 reg [1:0] state;reg aw_full,w_full,ar_full,issue_error;
 reg [31:0] awaddr,wdata,araddr;reg [3:0] wstrb;integer timer;
 wire idle=(state==IDLE);
 assign s_awready=rst_n&&idle&&!aw_full;
 assign s_wready=rst_n&&idle&&!w_full;
 assign s_arready=rst_n&&idle&&!ar_full;
 assign bus_valid=rst_n&&(state==ISSUE);
 assign irq=native_irq;
 `include "transport_valid.svh"
 initial if(TIMEOUT_CYCLES<2)$fatal(1,"Bridge timeout too small");
 always @(posedge clk or negedge rst_n)begin
  if(!rst_n)begin
   state<=IDLE;aw_full<=0;w_full<=0;ar_full<=0;awaddr<=0;wdata<=0;araddr<=0;wstrb<=0;
   s_bresp<=0;s_bvalid<=0;s_rdata<=0;s_rresp<=0;s_rvalid<=0;
   bus_write<=0;bus_address<=0;bus_wdata<=0;issue_error<=0;timer<=0;
  end else begin
   if(s_awvalid&&s_awready)begin aw_full<=1;awaddr<=s_awaddr;end
   if(s_wvalid&&s_wready)begin w_full<=1;wdata<=s_wdata;wstrb<=s_wstrb;end
   if(s_arvalid&&s_arready)begin ar_full<=1;araddr<=s_araddr;end
   case(state)
    IDLE:begin
     timer<=0;issue_error<=0;
     if(aw_full&&w_full)begin
      aw_full<=0;w_full<=0;bus_write<=1;bus_address<=awaddr[7:0];bus_wdata<=wdata;
      if(!sf_valid_address(awaddr)||wstrb!=4'hf)begin
       s_bvalid<=1;s_bresp<=!sf_valid_address(awaddr)?2'b11:(wstrb==0?2'b00:2'b10);state<=RESPOND;
      end else state<=ISSUE;
     end else if(ar_full)begin
      ar_full<=0;bus_write<=0;bus_address<=araddr[7:0];
      if(!sf_valid_address(araddr))begin s_rvalid<=1;s_rresp<=2'b11;s_rdata<=0;state<=RESPOND;end
      else state<=ISSUE;
     end
    end
    ISSUE:begin
     if(bus_ready||bus_error)begin issue_error<=bus_error;s_rdata<=bus_rdata;state<=CAPTURE;end
     else if(timer==TIMEOUT_CYCLES-1)begin issue_error<=1;state<=CAPTURE;end
     else timer<=timer+1;
    end
    CAPTURE:begin
     if(bus_write)begin s_bresp<=(issue_error||bus_error)?2'b10:2'b00;s_bvalid<=1;end
     else begin s_rresp<=(issue_error||bus_error)?2'b10:2'b00;s_rvalid<=1;end
     state<=RESPOND;
    end
    RESPOND:begin
     if(s_bvalid&&s_bready)begin s_bvalid<=0;state<=IDLE;end
     if(s_rvalid&&s_rready)begin s_rvalid<=0;state<=IDLE;end
    end
   endcase
  end
 end
endmodule
