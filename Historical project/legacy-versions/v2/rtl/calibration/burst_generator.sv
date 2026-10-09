`timescale 1ns/1ps
module burst_generator #(parameter integer CLOCK_HZ=132000000)(
 input wire clk,rst_n,start,abort,input wire [31:0] frequency,cycles,
 input wire [7:0] start_phase,output reg active,done,output wire waveform);
 localparam integer ACC_BITS=$clog2(CLOCK_HZ);
 reg[ACC_BITS-1:0] remainder;
 reg[23:0] phase_step;
 reg[31:0] completed,n_latched;
 reg[7:0] base_phase,offset;
 wire[ACC_BITS:0] sum={1'b0,remainder}+phase_step;
 wire advance=sum>=CLOCK_HZ;
 wire[7:0] phase=base_phase+offset;
 // Exact for the production register contract (38500..41500 Hz).
 // Rational phase arithmetic removes the old wide combinational divider.
 assign waveform=active&&!phase[7];
 always @(posedge clk or negedge rst_n)begin
  if(!rst_n)begin active<=0;done<=0;remainder<=0;base_phase<=0;completed<=0;phase_step<=0;n_latched<=0;offset<=0;end
  else begin
   done<=0;
   if(abort)begin active<=0;remainder<=0;base_phase<=0;end
   else if(start&&!active&&cycles!=0)begin
    active<=1;remainder<=0;base_phase<=0;completed<=0;phase_step<={frequency[15:0],8'b0};n_latched<=cycles;offset<=start_phase;
   end else if(active)begin
    if(advance)begin
     remainder<=sum-CLOCK_HZ;base_phase<=base_phase+1'b1;
     if(&base_phase)begin
      completed<=completed+1;
      if(completed+1==n_latched)begin active<=0;done<=1;end
     end
    end else remainder<=sum;
   end
  end
 end
endmodule
