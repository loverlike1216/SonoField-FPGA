`timescale 1ns/1ps
module tb_axi_native_bridge;
 reg clk=0;always #5 clk=~clk;
 reg rst_n=0;
 reg [31:0] s_awaddr=0,s_wdata=0,s_araddr=0;reg[3:0]s_wstrb=15;
 reg s_awvalid=0,s_wvalid=0,s_arvalid=0,s_bready=0,s_rready=0;
 wire s_awready,s_wready,s_arready,s_bvalid,s_rvalid;
 wire[1:0]s_bresp,s_rresp;wire[31:0]s_rdata;
 wire bus_valid,bus_write;wire[7:0]bus_address;wire[31:0]bus_wdata;
 wire[31:0]bus_rdata;wire bus_ready,bus_error,irq;
 reg native_irq=0;integer select_native=0,delay=0,writes=0,checks=0;reg delayed_error=0;
 reg[31:0]memory[0:31];integer i;
 wire real_ready,real_error,real_irq;wire[31:0]real_data;
 reg arm=0,stop=0,frame_valid=0;reg[2175:0]frame_data=0;reg[31:0]frame_sequence=0;
 wire frame_ready,running;wire[31:0]buffered_count;
 assign bus_ready=(select_native==3)?real_ready:((select_native==0)&&delay>=3&&bus_valid);
 assign bus_error=(select_native==3)?real_error:((select_native==1&&bus_valid)||delayed_error);
 assign bus_rdata=(select_native==3)?real_data:memory[bus_address>>2];
 axi_native_bridge #(.TIMEOUT_CYCLES(12)) dut(.*);
 sono_motion_system #(.POWER_WAIT_CYCLES(264000001),.INTERVAL_CYCLES(2640000)) real_system(
 .clk(clk),.rst_n(rst_n),.hardware_enable(1'b1),.motion_arm(arm),.motion_stop(stop),
 .frame_valid(frame_valid),.frame_data(frame_data),.frame_sequence(frame_sequence),.frame_last(1'b0),
 .frame_ready(frame_ready),.buffered_count(buffered_count),.motion_running(running),
 .bus_valid(bus_valid&&select_native==3),.bus_write(bus_write),.bus_address(bus_address),.bus_wdata(bus_wdata),
 .bus_rdata(real_data),.bus_ready(real_ready),.bus_error(real_error),.irq(real_irq),
 .adc_busy(1'b0),.adc_dout(4'b0));
 always @(posedge clk)begin
  if(!rst_n)begin delay<=0;writes<=0;delayed_error<=0;for(i=0;i<32;i=i+1)memory[i]<=0;end
  else begin
   delayed_error<=0;
   if(bus_valid&&select_native==0)begin
    if(delay<3)delay<=delay+1;
    if(bus_ready&&bus_write)begin
     writes<=writes+1;
     if(bus_wdata==32'hdeadbeef)delayed_error<=1;
     else memory[bus_address>>2]<=bus_wdata;
    end
   end else delay<=0;
  end
 end
 task reset;
  begin @(negedge clk);rst_n=0;s_awvalid=0;s_wvalid=0;s_arvalid=0;s_bready=0;s_rready=0;arm=0;stop=0;frame_valid=0;
   repeat(4)@(negedge clk);rst_n=1;repeat(6)@(negedge clk);
  end
 endtask
 task aw(input[31:0]a,input integer wait_cycles);
  begin repeat(wait_cycles)@(negedge clk);@(negedge clk);s_awaddr=a;s_awvalid=1;
   @(posedge clk);while(!s_awready)@(posedge clk);@(negedge clk);s_awvalid=0;
  end
 endtask
 task wd(input[31:0]v,input[3:0]strobe,input integer wait_cycles);
  begin repeat(wait_cycles)@(negedge clk);@(negedge clk);s_wdata=v;s_wstrb=strobe;s_wvalid=1;
   @(posedge clk);while(!s_wready)@(posedge clk);@(negedge clk);s_wvalid=0;
  end
 endtask
 task wr(input[31:0]a,input[31:0]v,input[3:0]strobe,input integer awdelay,input integer wdelay,input[1:0]expected);
  begin
   fork aw(a,awdelay);wd(v,strobe,wdelay);join
   while(!s_bvalid)@(negedge clk);
   repeat(4)begin if(!s_bvalid||s_bresp!==expected)$fatal(1,"B response/backpressure %h expected %h",s_bresp,expected);@(negedge clk);end
   s_bready=1;@(negedge clk);s_bready=0;checks=checks+1;
  end
 endtask
 task rd(input[31:0]a,input[1:0]expected,input[31:0]value,input check_value);
  reg[31:0]held;
  begin
   @(negedge clk);s_araddr=a;s_arvalid=1;@(posedge clk);while(!s_arready)@(posedge clk);
   @(negedge clk);s_arvalid=0;while(!s_rvalid)@(negedge clk);held=s_rdata;
   repeat(4)begin
    if(!s_rvalid||s_rresp!==expected||s_rdata!==held)$fatal(1,"R response/backpressure");
    if(check_value&&s_rdata!==value)$fatal(1,"R data %h expected %h",s_rdata,value);
    @(negedge clk);
   end
   s_rready=1;@(negedge clk);s_rready=0;checks=checks+1;
  end
 endtask
 task enqueue(input[31:0]seq);
  begin @(negedge clk);frame_sequence=seq;frame_valid=1;@(posedge clk);while(!frame_ready)@(posedge clk);@(negedge clk);frame_valid=0;end
 endtask
 initial begin
  reset();
  wr(12,40000,15,0,5,0);rd(12,0,40000,1);
  wr(16,8,15,5,0,0);rd(16,0,8,1);
  wr(20,9,15,0,0,0);if(writes!=3)$fatal(1,"Repeated native write");
  wr(20,999,0,0,0,0);rd(20,0,9,1);if(writes!=3)$fatal(1,"Zero strobe wrote");
  wr(20,999,3,0,0,2);wr(3,999,15,0,0,3);rd(256,3,0,0);
  wr(24,32'hdeadbeef,15,0,0,2); // registered native error, after ready
  select_native=1;wr(12,42,15,0,0,2);rd(4,2,0,0);
  select_native=2;rd(4,2,0,0);wr(12,42,15,0,0,2); // bounded native timeout
  select_native=0;native_irq=1;#1;if(!irq)$fatal(1,"IRQ lost");native_irq=0;#1;if(irq)$fatal(1,"IRQ stuck");
  // Simultaneous independent read/write request, each answered once.
  fork wr(28,7,15,0,0,0);rd(16,0,8,1);join
  aw(12,0);reset();if(s_bvalid||s_rvalid||bus_valid)$fatal(1,"Reset pending request leak");
  // Real existing motion/digital integration: status + safe write + ownership.
  // ADC is still in its 2-second POWER wait, so ready/idle status bits are zero.
  select_native=3;reset();rd(4,0,0,1);wr(12,40001,15,0,0,0);rd(12,0,40001,1);
  for(i=0;i<128;i=i+1)frame_data[i*17+:17]=17'h10000;
  enqueue(0);enqueue(1);@(negedge clk);arm=1;@(negedge clk);arm=0;
  if(!running)$fatal(1,"Motion queue failed to own bus");
  rd(4,2,0,0);wr(12,41000,15,0,0,2);
  @(negedge clk);stop=1;repeat(3)@(negedge clk);reset();rd(12,0,40000,1);
  wr(12,1,15,0,0,2); // actual native range error must cross AXI
  $display("PASS AXI_NATIVE checks=%0d independent_AW_W backpressure invalid error reset ownership IRQ",checks);$finish;
 end
 initial begin #1000000;$fatal(1,"AXI test timeout");end
endmodule
