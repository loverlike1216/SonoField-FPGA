`timescale 1ns/1ps
// Independent full C16 -> scheduler/BRAM -> bounded read/ACK ownership test.
module tb_c16_capture_chain;
 reg clk=0;always #3.787878788 clk=~clk;
 reg rst_n=0,start=0,abort=0,ack=0;reg[63:0]time_now=0;
 wire reset,convst,cs_n,sclk,sdi,busy,configured,adc_ready,adc_idle,adc_error,valid,request;
 wire[3:0]dout,state_debug;wire[127:0]frame;wire[63:0]stamp,first_stamp,burst_stamp;
 reg[11:0]read_address=0;wire[31:0]read_data;wire capture_ready,done,error,burst_start,burst_active,burst_done,wave,active;
 wire[6:0]tx;wire[7:0]sequence_number;wire[10:0]count;wire[1:0]blank;
 integer scan,n,w,trace;reg[127:0]expected;reg[63:0]saved_stamp;
 always@(posedge clk)time_now<=time_now+1;
 ad7606c16_if #(.POWER_WAIT_CYCLES(4),.RESET_CYCLES(4),.SETUP_CYCLES(4)) adc(
 .clk(clk),.rst_n(rst_n),.sample_request(request),.time_now(time_now),.busy_async(busy),.dout(dout),
 .adc_reset(reset),.convst(convst),.cs_n(cs_n),.sclk(sclk),.sdi(sdi),.ready(adc_ready),.error(adc_error),.frame_valid(valid),.frame(frame),.frame_timestamp(stamp),.idle(adc_idle));
 ad7606c16_model model(.reset(reset),.convst(convst),.cs_n(cs_n),.sclk(sclk),.sdi(sdi),.hold_busy(1'b0),.inject(3'b0),.busy(busy),.dout(dout),.configured(configured));
 calibration_scheduler scheduler(.clk(clk),.rst_n(rst_n),.start(start),.abort(abort),.ack(ack),.adc_ready(adc_ready),.adc_idle(adc_idle),.adc_error(adc_error),.frame_valid(valid),.frame(frame),.frame_timestamp(stamp),.time_now(time_now),
 .sample_period(32'd165),.pre_samples(32'd32),.main_samples(32'd800),.tail_samples(32'd192),.settle_cycles(32'd16),.guard_cycles(32'd32),.first_tx(7'd0),.scan_count(8'd2),
 .burst_active(burst_active),.burst_done(burst_done),.read_address(read_address),.read_data(read_data),.sample_request(request),.burst_start(burst_start),.capture_ready(capture_ready),.done(done),.error(error),.selected_tx(tx),.capture_sequence(sequence_number),.frame_count(count),.first_timestamp(first_stamp),.burst_timestamp(burst_stamp),.rx_blank(blank),.active(active),.state_debug(state_debug));
 burst_generator burst(.clk(clk),.rst_n(rst_n),.start(burst_start),.abort(abort),.frequency(32'd40000),.cycles(32'd16),.start_phase(8'd0),.active(burst_active),.done(burst_done),.waveform(wave));
 initial begin
  trace=$fopen("capture_trace.txt","w");repeat(6)@(negedge clk);rst_n=1;wait(adc_ready);@(negedge clk);start=1;@(negedge clk);start=0;
  for(scan=0;scan<2;scan=scan+1)begin
   wait(capture_ready||error||adc_error);if(error||adc_error||count!=1024||sequence_number!=scan)$fatal(1,"C16 full capture failed");
   if(burst_stamp-first_stamp!=32*165)$fatal(1,"C16 common burst/sample timebase");saved_stamp=first_stamp;
   for(n=0;n<1024;n=n+1)begin
    for(w=0;w<8;w=w+1)expected[w*16+:16]=model.sample(w,scan*1024+n);
    for(w=0;w<4;w=w+1)begin
     @(negedge clk);read_address=n*4+w;repeat(2)@(negedge clk);
     if(read_data!==expected[w*32+:32])$fatal(1,"C16 signed buffer read/channel order");
    end
    $fdisplay(trace,"%0d %0d %032h",scan,n,expected);
   end
   repeat(16)@(negedge clk);if(!capture_ready||count!=1024||first_stamp!=saved_stamp||!adc_idle||error||adc_error)$fatal(1,"C16 snapshot overwritten without ACK");
   ack=1;@(negedge clk);ack=0;@(negedge clk);
  end
  wait(done);abort=1;@(negedge clk);abort=0;repeat(3)@(negedge clk);if(capture_ready||active)$fatal(1,"C16 abort publication");
  $fclose(trace);$display("PASS C16_CAPTURE_CHAIN 2x1024 signed frames timestamp burst BRAM read ACK ownership abort");$finish;
 end
 initial begin #10000000;$fatal(1,"C16 capture chain timeout");end
endmodule
