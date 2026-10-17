`timescale 1ns/1ps
// Four-lane SPI engine. Capture OLD DOUT at the edge launching SCLK rising;
// AD7606B advances DOUT only after that edge (Rev B Figure 6).
module adc_serial #(parameter integer DOUT_LANES=4, SCLK_DIVIDER=4, FINISH_HOLD_CYCLES=1)(input wire clk,rst_n,start,input wire [5:0] bits,
 input wire [15:0] command,input wire [DOUT_LANES-1:0] dout,
 output reg cs_n,sclk,sdi,busy,done,output reg [127:0] received);
 reg [5:0] index, length;
 localparam integer DIV_W=$clog2(SCLK_DIVIDER);
 reg [DIV_W-1:0] divider;
 initial if((DOUT_LANES!=4&&DOUT_LANES!=8)||SCLK_DIVIDER<4||(SCLK_DIVIDER%2)!=0)$fatal(1,"invalid ADC candidate parameters");
 reg finishing;
 localparam integer FIN_W=$clog2(FINISH_HOLD_CYCLES+1);reg[FIN_W-1:0]finish_hold;
 reg [15:0] tx;
 reg [31:0] lane[0:DOUT_LANES-1];
 integer k;
 always @(posedge clk or negedge rst_n) begin
  if(!rst_n) begin
   cs_n<=1;sclk<=1;sdi<=0;busy<=0;done<=0;received<=0;
   index<=0;length<=0;divider<=0;finishing<=0;finish_hold<=0;tx<=0;
   for(k=0;k<DOUT_LANES;k=k+1)lane[k]<=0;
  end else begin
   done<=0;
   if(start && !busy) begin
    cs_n<=0;sclk<=1;sdi<=command[15];busy<=1;index<=0;
    length<=bits;divider<=0;finishing<=0;finish_hold<=0;tx<=command;
    for(k=0;k<DOUT_LANES;k=k+1)lane[k]<=0;
   end else if(busy) begin
    if(finishing) begin
     if(finish_hold<FINISH_HOLD_CYCLES-1)finish_hold<=finish_hold+1;
     else begin
     cs_n<=1;sdi<=0;busy<=0;done<=1;
     for(k=0;k<DOUT_LANES;k=k+1) begin
      if(DOUT_LANES==8)received[k*16+:16]<=lane[k][15:0];
      else begin
       received[(2*k)*16+:16]<=lane[k][31:16];
       received[(2*k+1)*16+:16]<=lane[k][15:0];
      end
     end
    end
    end else begin
     if(divider==SCLK_DIVIDER-1)divider<=0;else divider<=divider+1;
     if(divider==SCLK_DIVIDER/2-1)sclk<=0;
     if(divider==SCLK_DIVIDER-1) begin
      sclk<=1;
      for(k=0;k<DOUT_LANES;k=k+1)lane[k]<={lane[k][30:0],dout[k]};
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
