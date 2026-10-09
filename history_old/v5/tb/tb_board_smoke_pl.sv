`timescale 1ns/1ps
module tb_board_smoke_pl;
 reg clk=0;always #5 clk=~clk;reg rst_n=0;
 reg[31:0]s_awaddr=0,s_wdata=0,s_araddr=0;reg[3:0]s_wstrb=15;
 reg s_awvalid=0,s_wvalid=0,s_arvalid=0,s_bready=0,s_rready=0;
 wire s_awready,s_wready,s_arready,s_bvalid,s_rvalid,output_disable;
 wire[1:0]s_bresp,s_rresp;wire[31:0]s_rdata;wire[127:0]commanded_waveform;
 sono_board_smoke_pl dut(.clk(clk),.rst_n(rst_n),
 .s_awaddr(s_awaddr),.s_awvalid(s_awvalid),.s_awready(s_awready),
 .s_wdata(s_wdata),.s_wstrb(s_wstrb),.s_wvalid(s_wvalid),.s_wready(s_wready),
 .s_bresp(s_bresp),.s_bvalid(s_bvalid),.s_bready(s_bready),.s_araddr(s_araddr),.s_arvalid(s_arvalid),
 .s_arready(s_arready),.s_rdata(s_rdata),.s_rresp(s_rresp),.s_rvalid(s_rvalid),.s_rready(s_rready));
 assign output_disable=dut.system.output_disable;
 assign commanded_waveform=dut.system.commanded_waveform;
 task read32(input[31:0]address,input[31:0]expected);
  begin
   @(negedge clk);s_araddr=address;s_arvalid=1;
   @(posedge clk);while(!s_arready)@(posedge clk);@(negedge clk);s_arvalid=0;
   while(!s_rvalid)@(negedge clk);
   if(s_rresp!=0||s_rdata!==expected)$fatal(1,"AXI wrapper readback");
   s_rready=1;@(negedge clk);s_rready=0;
  end
 endtask
 always @(negedge clk)if(rst_n&&(!output_disable||commanded_waveform!==0))$fatal(1,"Smoke wrapper outputs not safe");
 initial begin
  repeat(4)@(negedge clk);rst_n=1;repeat(6)@(negedge clk);
  read32(4,0);read32(12,40000);
  @(negedge clk);s_awaddr=0;s_wdata=4;s_awvalid=1;s_wvalid=1;
  @(posedge clk);if(!s_awready||!s_wready)$fatal(1,"Wrapper ready");
  @(negedge clk);s_awvalid=0;s_wvalid=0;while(!s_bvalid)@(negedge clk);
  if(s_bresp!=0)$fatal(1,"Wrapper safe-disable write");s_bready=1;@(negedge clk);s_bready=0;
  read32(0,0);read32(8,0);
  $display("PASS BOARD_SMOKE_PL actual wrapper STATUS frequency safe-disable, outputs disabled");$finish;
 end
 initial begin #1000000;$fatal(1,"Wrapper timeout");end
endmodule
