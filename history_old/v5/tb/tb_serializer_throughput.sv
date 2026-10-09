`timescale 1ns/1ps
module tb_serializer_throughput;
 reg clk=0;always #5 clk=~clk;
 reg rst_n=0,start=0;reg[127:0]waveform=0;
 wire[31:0]data;wire sc,lc,busy,done,overrun;
 serializer dut(clk,rst_n,start,waveform,data,sc,lc,busy,done,overrun);
 integer n,k,edges,done_age;
 initial begin
  repeat(3)@(negedge clk);rst_n=1;
  for(n=0;n<100;n=n+1)begin
   if(busy)$fatal(1,"Not ready at 11-cycle start interval");
   waveform={32'h87654321+n,32'h12345678+n,32'hFEDCBA98+n,32'h00000123+n};
   start=1;edges=0;done_age=-1;
   for(k=0;k<11;k=k+1)begin
    @(posedge clk);#1;
    if(sc)edges=edges+1;
    if(done)done_age=k;
    if(overrun)$fatal(1,"overrun at legal cadence");
    @(negedge clk);start=0;
   end
   if(edges!=4||done_age!=10||busy)$fatal(1,"Bad serialization lifecycle");
  end
  $display("PASS SERIALIZER_THROUGHPUT starts=100 acceptance_cycles=11 done_offset=10 shift_edges=4");$finish;
 end
endmodule
