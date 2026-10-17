`timescale 1ns/1ps
//PS toggles only after allthree TMP117 reads pass identity/range/timeout checks.
//A stalled PS or sensor transaction cannot leave old healthflagsvalid forever.
module service_freshness #(parameter integer TIMEOUT_CYCLES=25600000)(
 input wire clk,rst_n,kick,qualified,output wire fresh);
 localparam integer W=$clog2(TIMEOUT_CYCLES+1);
 reg[W-1:0]age;reg previous;
 always@(posedge clk or negedge rst_n)
  if(!rst_n)begin age<=TIMEOUT_CYCLES;previous<=0;end
  else begin
   previous<=kick;
   if(!qualified)age<=TIMEOUT_CYCLES;
   else if(kick!=previous)age<=0;
   else if(age<TIMEOUT_CYCLES)age<=age+1;
  end
 assign fresh=rst_n&&qualified&&age<TIMEOUT_CYCLES;
endmodule
