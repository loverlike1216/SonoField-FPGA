`timescale 1ns/1ps
// AD7606C-16 Rev.A Tables3/5/26/33/38, Figures111-113. Digital qualification only.
// OS=111, PAR/SER=1, VDRIVE=3V3 are external straps, not inferred from software.
module ad7606c16_if #(
 parameter integer CLOCK_HZ=132000000,
 parameter integer POWER_WAIT_CYCLES=2*CLOCK_HZ+1,
 parameter integer RESET_CYCLES=(CLOCK_HZ/1000000)*4,
 parameter integer SETUP_CYCLES=(CLOCK_HZ/1000000)*275,
 parameter [7:0] BANDWIDTH_MASK=8'hff,
 parameter integer BUSY_TIMEOUT_CYCLES=CLOCK_HZ/100000,
 parameter integer SPI_TIMEOUT_CYCLES=512
)(input wire clk,rst_n,sample_request,input wire [63:0] time_now,
 input wire busy_async,input wire [3:0] dout,
 output reg adc_reset,convst,output wire cs_n,sclk,sdi,
 output reg ready,error,frame_valid,output reg [127:0] frame,
 output reg [63:0] frame_timestamp,output wire idle);
 localparam POWER=0,RESET=1,SETUP=2,ISSUE=3,CHECK=4,RUN=5;
 reg [2:0] state;reg [31:0] count,age,spi_age;
 reg [4:0] init_index;reg start;reg [5:0] bits;reg [15:0] command;
 wire spi_busy,done;wire [127:0] received;
 (* ASYNC_REG="TRUE" *) reg [1:0] busy_sync;
 reg previous,pending,reading;reg [1:0] pulse;
 reg [63:0] pending_time,read_time;
 wire falling=previous&&!busy_sync[1];
 assign idle=ready&&!error&&!busy_sync[1]&&!pending&&!reading&&!spi_busy;
 function [15:0] initialization(input [4:0] n);
  case(n)
   0:initialization=16'h6f00; // device ID read, response on following frame
   1:initialization=16'h4200;
   2:initialization=16'h0210; // reserved0, normal, four DOUT, status off
   3:initialization=16'h0311;4:initialization=16'h0411;
   5:initialization=16'h0511;6:initialization=16'h0611; // +/-5V single-ended
   7:initialization={8'h07,BANDWIDTH_MASK};
   8:initialization=16'h0800; // no oversampling
   9:initialization=16'h2100; // interface CRC disabled; 16/32-bit profile
   10:initialization=16'h4200;11:initialization=16'h4300;
   12:initialization=16'h4400;13:initialization=16'h4500;
   14:initialization=16'h4600;15:initialization=16'h4700;
   16:initialization=16'h4800;17:initialization=16'h6100;
   18:initialization=16'h4000;
   default:initialization=16'h0000; // exit register mode
  endcase
 endfunction
 adc_serial serial(.clk(clk),.rst_n(rst_n),.start(start),.bits(bits),.command(command),.dout(dout),
 .cs_n(cs_n),.sclk(sclk),.sdi(sdi),.busy(spi_busy),.done(done),.received(received));
 always @(posedge clk or negedge rst_n)
  if(!rst_n)begin busy_sync<=0;previous<=0;end
  else begin busy_sync<={busy_sync[0],busy_async};previous<=busy_sync[1];end
 always @(posedge clk or negedge rst_n)begin
  if(!rst_n)begin
   state<=POWER;count<=0;age<=0;spi_age<=0;init_index<=0;adc_reset<=0;convst<=0;
   ready<=0;error<=0;frame_valid<=0;frame<=0;frame_timestamp<=0;
   start<=0;bits<=16;command<=0;pending<=0;reading<=0;pulse<=0;pending_time<=0;read_time<=0;
  end else begin
   start<=0;frame_valid<=0;
   if(pulse!=0)begin pulse<=pulse-1;if(pulse==1)convst<=0;end
   if(error)begin ready<=0;convst<=0;pending<=0;reading<=0;end
   else case(state)
    POWER:if(count==POWER_WAIT_CYCLES-1)begin adc_reset<=1;count<=0;state<=RESET;end else count<=count+1;
    RESET:if(count==RESET_CYCLES-1)begin adc_reset<=0;count<=0;state<=SETUP;end else count<=count+1;
    SETUP:if(count==SETUP_CYCLES-1)begin count<=0;state<=ISSUE;end else count<=count+1;
    ISSUE:begin start<=1;bits<=16;command<=initialization(init_index);spi_age<=0;state<=CHECK;end
    CHECK:begin
     spi_age<=spi_age+1;
     if(spi_age>=SPI_TIMEOUT_CYCLES)error<=1;
     if(done)begin
      if(init_index==1 && received[23:20]!=4'h2)error<=1;
      if(init_index==11 && received[23:16]!=8'h10)error<=1;
      if(init_index>=12 && init_index<=15 && received[23:16]!=8'h11)error<=1;
      if(init_index==16 && received[23:16]!=BANDWIDTH_MASK)error<=1;
      if((init_index==17||init_index==18) && received[23:16]!=0)error<=1;
      if(init_index==19)begin state<=RUN;ready<=1;end
      else begin init_index<=init_index+1;state<=ISSUE;end
     end
    end
    RUN:begin
     if(sample_request)begin
      if(pending||busy_sync[1])error<=1;
      else begin convst<=1;pulse<=2;pending<=1;pending_time<=time_now;age<=0;end
     end
     if(pending)begin age<=age+1;if(age>=BUSY_TIMEOUT_CYCLES)begin error<=1;pending<=0;end end
     if(falling&&pending)begin
      pending<=0;
      if(spi_busy||reading)error<=1;
      else begin start<=1;bits<=32;command<=0;reading<=1;spi_age<=0;read_time<=pending_time;end
     end
     if(reading)begin spi_age<=spi_age+1;if(spi_age>=SPI_TIMEOUT_CYCLES)error<=1;end
     if(done&&reading)begin frame<=received;frame_timestamp<=read_time;frame_valid<=1;reading<=0;end
    end
    default:error<=1;
   endcase
  end
 end
endmodule
