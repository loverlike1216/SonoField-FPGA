`timescale 1ns/1ps
module tb_ad7606c16;
 reg clk=0;always #3.787878788 clk=~clk;
 reg rst_n=0,request=0,hold=0;reg[2:0]inject=0;reg[63:0]time_now=0;
 wire busy,reset,convst,cs_n,sclk,sdi,ready,error,valid,idle,configured;
 wire[3:0]dout;wire[127:0]frame;wire[63:0]stamp;
 integer c,seq,trace,fault,producer,received_count;reg continuous_mode=0;
 ad7606c16_if #(.POWER_WAIT_CYCLES(4),.RESET_CYCLES(4),.SETUP_CYCLES(4)) dut(
 .clk(clk),.rst_n(rst_n),.sample_request(request),.time_now(time_now),.busy_async(busy),.dout(dout),
 .adc_reset(reset),.convst(convst),.cs_n(cs_n),.sclk(sclk),.sdi(sdi),.ready(ready),.error(error),.frame_valid(valid),.frame(frame),.frame_timestamp(stamp),.idle(idle));
 ad7606c16_model model(.reset(reset),.convst(convst),.cs_n(cs_n),.sclk(sclk),.sdi(sdi),.hold_busy(hold),.inject(inject),.busy(busy),.dout(dout),.configured(configured));
 task restart;
  begin rst_n=0;request=0;repeat(5)@(negedge clk);rst_n=1;end
 endtask
 task pulse_request;
  begin @(negedge clk);time_now=time_now+165;request=1;@(negedge clk);request=0;end
 endtask
 always @(negedge clk)if(continuous_mode&&valid)begin
  for(c=0;c<8;c=c+1)if(frame[c*16+:16]!==model.sample(c,received_count))$fatal(1,"C16 continuous channel correspondence");
  received_count=received_count+1;
 end
 initial begin
  trace=$fopen("c16_trace.txt","w");restart();wait(ready||error);
  if(error||!configured||model.registers[7]!=255)$fatal(1,"C16 init/readback failed");
  for(seq=0;seq<64;seq=seq+1)begin
   pulse_request();wait(valid||error);if(error)$fatal(1,"C16 valid capture error");
   for(c=0;c<8;c=c+1)if(frame[c*16+:16]!==model.sample(c,seq))$fatal(1,"C16 channel/sign mapping");
   if(stamp!==time_now)$fatal(1,"C16 timestamp mismatch");
   $fdisplay(trace,"%0d %032h %0d",seq,frame,stamp);
   repeat(3)@(negedge clk); // consume the one-cycle frame_valid before next request
  end
  restart();wait(ready);received_count=0;continuous_mode=1;
  for(producer=0;producer<32;producer=producer+1)begin pulse_request();repeat(163)@(negedge clk);end
  wait(received_count==32||error);if(error)$fatal(1,"C16 continuous800kSPS error");continuous_mode=0;
  for(fault=1;fault<=5;fault=fault+1)begin
   inject=fault;restart();wait(error||ready);if(!error)$fatal(1,"C16 bad readback accepted");
   repeat(5)@(negedge clk);if(ready||valid||convst)$fatal(1,"C16 failure not closed");
  end
  inject=0;restart();wait(ready);hold=1;pulse_request();wait(error);repeat(5)@(negedge clk);
  if(ready||valid||convst)$fatal(1,"C16 BUSY timeout unsafe");
  hold=0;restart();wait(ready);pulse_request();pulse_request();wait(error);
  restart();wait(ready);rst_n=0;repeat(4)@(negedge clk);if(ready||valid||convst)$fatal(1,"C16 logic power/reset unsafe");
  $fclose(trace);$display("PASS C16 signed64 frames continuous32 at800kSPS readback5 negatives BUSY timeout overlap reset");$finish;
 end
 initial begin #10000000;$fatal(1,"C16 test watchdog");end
endmodule
