`timescale 1ns/1ps
// Compare every observable output against the preserved pre-stage RTL.
module queue_pair #(parameter DEPTH=4)(input clk, output reg finished=0);
 reg rst_n=0,arm=0,stop=0,valid=0,last=0,ready=1,error=0,ack=0;
 reg [2175:0] frame=0;reg[31:0]seq=0;
 wire [145:0] a,b;
 wire ra,rb;wire[31:0]ca,cb,wa,wb,sa,sb;
 wire va,vb,wra,wrb;wire[7:0]aa,ab;
 wire runa,runb,da,db,ua,ub,oa,ob,ia,ib,ta,tb,xa,xb,rpa,rpb,apa,apb;
 motion_queue #(.DEPTH(DEPTH),.INTERVAL_CYCLES(1200),.ACK_TIMEOUT_CYCLES(13)) dut
 (clk,rst_n,arm,stop,valid,frame,seq,last,ra,ca,va,wra,aa,wa,ready,error,ack,runa,da,ua,oa,ia,ta,xa,sa,rpa,apa);
 motion_queue_golden #(.DEPTH(DEPTH),.INTERVAL_CYCLES(1200),.ACK_TIMEOUT_CYCLES(13)) ref_dut
 (clk,rst_n,arm,stop,valid,frame,seq,last,rb,cb,vb,wrb,ab,wb,ready,error,ack,runb,db,ub,ob,ib,tb,xb,sb,rpb,apb);
 assign a={ra,ca,va,wra,aa,wa,runa,da,ua,oa,ia,ta,xa,sa,rpa,apa};
 assign b={rb,cb,vb,wrb,ab,wb,runb,db,ub,ob,ib,tb,xb,sb,rpb,apb};
 integer cycles=0,words=0,seed=700+DEPTH,k,n;
 always @(posedge clk)begin
  #1;cycles=cycles+1;
  if(a!==b)$fatal(1,"QUEUE_EQ depth=%0d cycle=%0d actual=%h golden=%h",DEPTH,cycles,a,b);
  if(va&&aa==8'h58)words=words+1;
 end
 task reset_pair;begin
  @(negedge clk);rst_n=0;valid=0;arm=0;stop=0;ack=0;error=0;ready=1;
  repeat(3)@(negedge clk);rst_n=1;seq=0;
 end endtask
 task push_frame(input integer is_last);begin
  @(negedge clk);
  while(!ra)@(negedge clk);
  for(n=0;n<128;n=n+1)frame[n*17+:16]=$random(seed);
  for(n=0;n<128;n=n+1)frame[n*17+16]=1;
  valid=1;last=is_last;
  @(negedge clk);valid=0;seq=seq+1;
 end endtask
 initial begin
  // Repeated maps refill the ring and exercise non-power-of-two wrap.
  reset_pair;
  push_frame(0);push_frame(0);
  @(negedge clk);arm=1;@(negedge clk);arm=0;
  fork
   begin for(k=0;k<10;k=k+1)push_frame(k==9);end
   begin
    repeat(16000)begin
     @(negedge clk);ready=(($random(seed)&15)!=0);ack=(dut.state==8);
    end
   end
  join
  if(!da||words<128*12)$fatal(1,"Insufficient successful maps depth=%0d words=%0d",DEPTH,words);
  // Faults plus stalls, timeout and asynchronous stop/reset.
  reset_pair;@(negedge clk);arm=1;repeat(5)@(negedge clk);
  reset_pair;seq=7;push_frame(0);repeat(5)@(negedge clk);
  reset_pair;for(k=0;k<DEPTH;k=k+1)push_frame(0);
  @(negedge clk);valid=1;repeat(5)@(negedge clk);
  reset_pair;push_frame(1);@(negedge clk);arm=1;@(negedge clk);arm=0;
  repeat(1400)@(negedge clk);
  reset_pair;push_frame(0);push_frame(1);@(negedge clk);arm=1;@(negedge clk);arm=0;
  repeat(35)@(negedge clk);ready=0;repeat(80)@(negedge clk);stop=1;
  repeat(5)@(negedge clk);reset_pair;
  finished=1;$display("PASS QUEUE_EQ depth=%0d cycles=%0d words=%0d",DEPTH,cycles,words);
 end
endmodule
module tb_motion_queue_equivalence;
 reg clk=0;always #5 clk=~clk;
 wire a,b,c;
 queue_pair #(.DEPTH(2)) p2(clk,a);
 queue_pair #(.DEPTH(4)) p4(clk,b);
 queue_pair #(.DEPTH(5)) p5(clk,c);
 initial begin wait(a&&b&&c);$display("PASS QUEUE_EQ_ALL");$finish;end
 initial begin #3000000;$fatal(1,"equivalence timeout");end
endmodule
