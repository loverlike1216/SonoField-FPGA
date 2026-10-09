`timescale 1ns/1ps
module tb_motion_faults;
 parameter integer INTERVAL_CYCLES=1200;
 reg clk=0;always #5 clk=~clk;
 reg rst_n=0,arm=0,stop=0,valid=0,last=0,map_ack=0,ack_enable=1;
 reg [2175:0] data=0;reg [31:0] sequence_in=0;
 wire ready,bv,bw,running,done,underflow,overflow,invalid_frame,ack_timeout,disable_request,rq,aq;
 wire [31:0] count,bd,ackseq;wire [7:0] ba;
 motion_queue #(.DEPTH(2),.INTERVAL_CYCLES(INTERVAL_CYCLES),.ACK_TIMEOUT_CYCLES(100)) dut(
 .clk(clk),.rst_n(rst_n),.arm(arm),.stop(stop),.frame_valid(valid),.frame_data(data),.frame_sequence(sequence_in),
 .frame_last(last),.frame_ready(ready),.count(count),.bus_valid(bv),.bus_write(bw),.bus_address(ba),.bus_wdata(bd),
 .bus_ready(bv),.bus_error(1'b0),.map_ack(map_ack),.running(running),.done(done),.underflow(underflow),
 .overflow(overflow),.invalid_frame(invalid_frame),.ack_timeout(ack_timeout),.disable_request(disable_request),
 .acknowledged_sequence(ackseq),.request_pulse(rq),.ack_pulse(aq));
 // Bus responder verifies each complete 128-word transfer before ACK. Integration
 // against the real phase bank and digital system is covered in tb_motion.
 integer writes=0,cycles=0,prev=-1,requests=0,acks=0;
 reg [6:0] selected=0;reg [16:0] word_data=0;reg [127:0] written=0;
 always @(posedge clk)begin
  cycles=cycles+1;map_ack<=0;
  if(!rst_n)begin writes=0;written=0;prev=-1;requests=0;acks=0;end
  else begin
   if(bv)case(ba)
    8'h54:selected=bd[6:0];
    8'h58:word_data=bd[16:0];
    8'h5c:begin
     if(written[selected])$fatal(1,"Duplicate channel");
     written[selected]=1;writes=writes+1;
     if(word_data!==(17'h10000|selected))$fatal(1,"Corrupt channel order");
    end
    8'h60:begin
     if(!(&written)||writes!=128)$fatal(1,"Partial map commit");
     writes=0;written=0;if(ack_enable)map_ack<=1;
    end
    default:$fatal(1,"Unexpected bus address");
   endcase
   if(rq)begin
    if(prev>=0&&cycles-prev!=INTERVAL_CYCLES)$fatal(1,"Cadence mismatch");
    prev=cycles;requests=requests+1;
   end
   if(aq)acks=acks+1;
  end
 end
 task reset;
 begin
  @(negedge clk);rst_n=0;valid=0;arm=0;stop=0;last=0;ack_enable=1;
  repeat(3)@(negedge clk);
  if(!disable_request||running||count)$fatal(1,"Unsafe reset");
  rst_n=1;repeat(2)@(negedge clk);
 end endtask
 task push(input integer seq,input integer final_frame);
 begin
  @(negedge clk);sequence_in=seq;last=final_frame;valid=1;
  @(negedge clk);valid=0;
 end endtask
 task start;
 begin @(negedge clk);arm=1;@(negedge clk);arm=0;end endtask
 initial begin
  for(integer c=0;c<128;c=c+1)data[c*17+:17]=17'h10000|c;
  reset();push(0,0);push(1,1);start();wait(done);repeat(3)@(negedge clk);
  if(acks!=2||ackseq!=1||underflow||overflow||ack_timeout)$fatal(1,"Double-buffer run failed");
  $display("PASS MOTION-RTL01/02/03/04 complete maps, ordered double-buffer swap, cadence=%0d cycles",INTERVAL_CYCLES);
  reset();push(0,0);push(1,0);start();wait(underflow);#1;
  if(!disable_request)$fatal(1,"Underflow not safe");
  $display("PASS MOTION-RTL05 underflow disables");
  reset();push(0,0);push(1,0);push(2,0);#1;
  if(!overflow||!disable_request)$fatal(1,"Overflow not rejected");
  $display("PASS MOTION-RTL06 overflow");
  reset();push(0,0);push(1,1);start();repeat(80)@(negedge clk);stop=1;#1;
  if(!disable_request)$fatal(1,"STOP not immediate");
  repeat(3)@(negedge clk);stop=0;repeat(3)@(negedge clk);
  if(!disable_request||count||running)$fatal(1,"STOP release resumed stale motion");
  $display("PASS MOTION-RTL07 STOP mid-load remains disabled until reset");
  reset();push(0,0);push(1,1);start();repeat(80)@(negedge clk);reset();
  if(count||running)$fatal(1,"Reset mid-load retained queue");
  $display("PASS MOTION-RTL08 reset mid-trajectory");
  push(7,0);#1;if(!invalid_frame||!disable_request)$fatal(1,"Bad sequence accepted");
  reset();data=0;push(0,0);#1;if(!invalid_frame||!disable_request)$fatal(1,"Empty mask accepted");
  $display("PASS MOTION-RTL09 invalid frame/sequence reject");
  for(integer c=0;c<128;c=c+1)data[c*17+:17]=17'h10000|c;
  reset();push(0,1);start();wait(done);repeat(3)@(negedge clk);
  if(ackseq!=0||underflow||overflow||invalid_frame)$fatal(1,"Safe recovery failed");
  $display("PASS MOTION-RTL10 reset and new complete map recover safely");
  reset();ack_enable=0;push(0,1);start();wait(ack_timeout);#1;
  if(!disable_request)$fatal(1,"Lost ACK unsafe");
  $display("PASS MOTION extra lost ACK timeout");$finish;
 end
 initial begin #200000000;$fatal(1,"Fault test timeout");end
endmodule

// Windows Vivado .bat launchers split unquoted '=' arguments. A source wrapper
// preserves the exact production parameter without depending on shell quoting.
module tb_motion_cadence;
 tb_motion_faults #(.INTERVAL_CYCLES(2640000)) tests();
endmodule
