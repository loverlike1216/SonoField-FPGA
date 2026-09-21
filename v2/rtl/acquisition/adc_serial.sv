`timescale 1ns/1ps
// Four-lane SPI engine. Capture OLD DOUT at the edge launching SCLK rising;
// AD7606B advances DOUT only after that edge (Rev B Figure 6).
module adc_serial(input wire clk,rst_n,start,input wire [5:0] bits,
 input wire [15:0] command,input wire [3:0] dout,
 output reg cs_n,sclk,sdi,busy,done,output reg [127:0] received);
 reg [5:0] index, length;
 reg [1:0] divider;
 reg finishing;
 reg [15:0] tx;
 reg [31:0] lane[0:3];
 integer k;
 always @(posedge clk or negedge rst_n) begin
  if(!rst_n) begin
   cs_n<=1;sclk<=1;sdi<=0;busy<=0;done<=0;received<=0;
   index<=0;length<=0;divider<=0;finishing<=0;tx<=0;
   for(k=0;k<4;k=k+1)lane[k]<=0;
  end else begin
   done<=0;
   if(start && !busy) begin
    cs_n<=0;sclk<=1;sdi<=command[15];busy<=1;index<=0;
    length<=bits;divider<=0;finishing<=0;tx<=command;
    for(k=0;k<4;k=k+1)lane[k]<=0;
   end else if(busy) begin
    if(finishing) begin
     cs_n<=1;sdi<=0;busy<=0;done<=1;
     for(k=0;k<4;k=k+1) begin
      received[(2*k)*16+:16]<=lane[k][31:16];
      received[(2*k+1)*16+:16]<=lane[k][15:0];
     end
    end else begin
     divider<=divider+1;
     if(divider==1)sclk<=0;
     if(divider==3) begin
      sclk<=1;
      for(k=0;k<4;k=k+1)lane[k]<={lane[k][30:0],dout[k]};
      if(index==length-1)finishing<=1;
      else begin
       index<=index+1;
       if(index<15)sdi<=tx[14-index];else sdi<=0;
      end
     end
    end
   end
  end
 end
endmodule
