`timescale 1ns/1ps
// All input words originate in Controller.stream_map transactions produced by the GUI model.
module tb_motion;
 parameter integer INTERVAL_CYCLES=8192;
 reg clk=0; always #3.787879 clk=~clk;
 reg rst_n=0,arm=0,stop=0,frame_valid=0,frame_last=0;
 reg [2175:0] frame_data=0;reg [31:0] frame_sequence=0;
 wire frame_ready;wire [31:0] count,ack_sequence;
 wire bv,bw,br,be,disable_request,running,done,underflow,overflow,invalid_frame,ack_timeout,request_pulse,ack_pulse;
 wire [7:0] ba;wire [31:0] bd,bread;wire output_disable;
 wire adc_reset,convst,cs_n,sclk,sdi,busy,configured;wire [3:0] dout;
 reg hv=0;reg [7:0] ha=0;reg [31:0] hd=0;
 sono_motion_system #(.POWER_WAIT_CYCLES(32),.INTERVAL_CYCLES(INTERVAL_CYCLES)) system(
 .clk(clk),.rst_n(rst_n),.hardware_enable(1'b1),.motion_arm(arm),.motion_stop(stop),
 .frame_valid(frame_valid),.frame_data(frame_data),.frame_sequence(frame_sequence),.frame_last(frame_last),
 .frame_ready(frame_ready),.buffered_count(count),.acknowledged_sequence(ack_sequence),
 .motion_running(running),.motion_done(done),.motion_underflow(underflow),.motion_overflow(overflow),
 .motion_invalid(invalid_frame),.motion_timeout(ack_timeout),.motion_request_pulse(request_pulse),.motion_ack_pulse(ack_pulse),
 .bus_valid(hv),.bus_write(1'b1),.bus_address(ha),.bus_wdata(hd),.bus_rdata(bread),.bus_ready(br),.bus_error(be),
 .adc_busy(busy),.adc_dout(dout),.adc_reset(adc_reset),.adc_convst(convst),.adc_cs_n(cs_n),.adc_sclk(sclk),.adc_sdi(sdi),
 .rx_blank(),.serial_data(),.shift_clock(),.latch_clock(),.output_disable(output_disable),.commanded_waveform(),.irq());
 ad7606b_model adc(.reset(adc_reset),.convst(convst),.cs_n(cs_n),.sclk(sclk),.sdi(sdi),
 .hold_busy(1'b0),.busy(busy),.dout(dout),.configured(configured));
 reg [31:0] words[0:1536001];
 integer n,loaded=0,acks=0,cycles=0,last_request=-1,trace,enabled=0;
 reg [1023:0] previous=0;reg [127:0] previous_mask=0;
 task write_host(input [7:0] addr,input [31:0] data);
 begin @(negedge clk);hv=1;ha=addr;hd=data;@(negedge clk);hv=0;end endtask
 always @(posedge clk)begin
  cycles=cycles+1;#1;
  if(rst_n)begin
   if(underflow||overflow||invalid_frame||ack_timeout||be||system.digital.fault)$fatal(1,"Motion fault %d %d %d %d %d",underflow,overflow,invalid_frame,ack_timeout,be);
   if((system.digital.effective!==previous||system.digital.mask!==previous_mask)&&!system.digital.commit_ack)$fatal(1,"Nonatomic map change");
   if(request_pulse)begin
    if(last_request>=0&&cycles-last_request!=INTERVAL_CYCLES)$fatal(1,"Cadence drift");
    last_request=cycles;
   end
   if(ack_pulse)begin
    if(ack_sequence!=acks)$fatal(1,"ACK sequence mismatch");
    for(integer c=0;c<128;c=c+1)begin
     if(system.digital.bank.active_requested[c]!==words[1+acks*128+c][7:0]||
        system.digital.bank.active_calibration[c]!==words[1+acks*128+c][15:8]||
        system.digital.mask[c]!==words[1+acks*128+c][16])$fatal(1,"Python/RTL map mismatch frame %d channel %d",acks,c);
    end
    $fdisplay(trace,"%0d %0d %0256h %032h",acks,cycles,system.digital.effective,system.digital.mask);
    acks=acks+1;
   end
   previous=system.digital.effective;previous_mask=system.digital.mask;
  end
 end
 initial begin
  $readmemh("motion_maps.hex",words);n=words[0];
  if(n<1||n>12000)$fatal(1,"Invalid frame count");
  trace=$fopen("motion_ack.txt","w");
  repeat(5)@(negedge clk);rst_n=1;
  repeat(10)@(negedge clk);
  wait(system.digital.adc_ready);if(!configured)$fatal(1,"ADC setup failed");
  // Configure only the previously verified register interface, while disabled.
  write_host(8'h0c,words[1536001]);
  write_host(8'h08,1);write_host(8'h00,1);
  while(!done)begin
   @(negedge clk);frame_valid=0;arm=0;
   if(loaded<n&&frame_ready)begin
    for(integer c=0;c<128;c=c+1)frame_data[c*17+:17]=words[1+loaded*128+c][16:0];
    frame_sequence=loaded;frame_last=(loaded==n-1);frame_valid=1;loaded=loaded+1;
   end
   if(!running&&(count>=2||(count==1&&n==1)))arm=1;
  end
  @(negedge clk);frame_valid=0;arm=0;
  if(acks!=n)$fatal(1,"Missing ACKs");
  repeat(100)@(negedge clk);
  if(output_disable)$fatal(1,"Final hold not enabled");
  stop=1;#1;if(!output_disable)$fatal(1,"STOP must asynchronously disable output");
  repeat(3)@(negedge clk);if(count!=0||running)$fatal(1,"STOP must clear queue");
  $fclose(trace);$display("PASS MOTION RTL maps=%0d atomic separate calibration FIFO cadence ACK STOP",n);$finish;
 end
 initial begin #1000000000;$fatal(1,"Motion timeout");end
endmodule
