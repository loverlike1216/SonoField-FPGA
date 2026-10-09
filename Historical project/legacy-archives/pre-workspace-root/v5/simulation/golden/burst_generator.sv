`timescale 1ns/1ps
module burst_generator #(parameter integer CLOCK_HZ=132000000)(
 input wire clk,rst_n,start,abort,input wire [31:0] frequency,cycles,
 input wire [7:0] start_phase,output reg active,done,output wire waveform);
 reg[31:0] accumulator,completed;
 reg[31:0] f_latched,n_latched;
 reg[7:0] offset;
 wire[32:0] sum={1'b0,accumulator}+f_latched;
 wire[39:0] scaled={accumulator,8'b0};
 wire[7:0] phase=scaled/CLOCK_HZ+offset;
 assign waveform=active&&!phase[7];
 always @(posedge clk or negedge rst_n)begin
  if(!rst_n)begin active<=0;done<=0;accumulator<=0;completed<=0;f_latched<=0;n_latched<=0;offset<=0;end
  else begin
   done<=0;
   if(abort)begin active<=0;accumulator<=0;end
   else if(start&&!active&&cycles!=0)begin
    active<=1;accumulator<=0;completed<=0;f_latched<=frequency;n_latched<=cycles;offset<=start_phase;
   end else if(active)begin
    if(sum>=CLOCK_HZ)begin
     accumulator<=sum-CLOCK_HZ;completed<=completed+1;
     if(completed+1==n_latched)begin active<=0;done<=1;end
    end else accumulator<=sum;
   end
  end
 end
endmodule
