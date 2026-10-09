`timescale 1ns/1ps
module ad7606b_if #(
 parameter integer CLOCK_HZ=132000000,
 parameter integer POWER_WAIT_CYCLES=2*CLOCK_HZ+1,
 parameter integer RESET_CYCLES=(CLOCK_HZ/1000000)*4,
 parameter integer SETUP_CYCLES=(CLOCK_HZ/1000000)*254
)(input wire clk,rst_n,sample_request,input wire [63:0] time_now,
 input wire busy_async,input wire [3:0] dout,
 output reg adc_reset,convst,output wire cs_n,sclk,sdi,
 output reg ready,error,frame_valid,output reg [127:0] frame,
 output reg [63:0] frame_timestamp,output wire idle);
 localparam POWER=0,RESET=1,SETUP=2,INIT=3,WAIT_SPI=4,RUN=5;
 reg [2:0] state;
 reg [31:0] count,conversion_age;
 reg [4:0] init_index;
 reg spi_start;reg[5:0] spi_bits;reg[15:0] spi_command;
 wire spi_busy,spi_done;wire[127:0] spi_received;
 (* ASYNC_REG="TRUE" *) reg [1:0] busy_sync;
 reg busy_previous,conversion_pending,reading;
 reg [1:0] pulse;
 reg [63:0] pending_timestamp,reading_timestamp;
 wire busy_fall=busy_previous && !busy_sync[1];
 assign idle=ready&&!error&&!busy_sync[1]&&!conversion_pending&&!reading&&!spi_busy;
 function [15:0] init_command(input [4:0] n);
  case(n)
   0:init_command=16'h4200; // enter register mode by reading CONFIG
   1:init_command=16'h0210; // four DOUT, no status / CRC
   2:init_command=16'h0311;3:init_command=16'h0411;
   4:init_command=16'h0511;5:init_command=16'h0611; // all +/-5 V
   6:init_command=16'h4200;7:init_command=16'h4000; // CONFIG readback
   8:init_command=16'h4300;9:init_command=16'h4000;
   10:init_command=16'h4400;11:init_command=16'h4000;
   12:init_command=16'h4500;13:init_command=16'h4000;
   14:init_command=16'h4600;15:init_command=16'h4000;
   default:init_command=16'h0000; // exit to conversion mode
  endcase
 endfunction
 adc_serial spi(.clk(clk),.rst_n(rst_n),.start(spi_start),.bits(spi_bits),
  .command(spi_command),.dout(dout),.cs_n(cs_n),.sclk(sclk),.sdi(sdi),
  .busy(spi_busy),.done(spi_done),.received(spi_received));
 always @(posedge clk or negedge rst_n)
  if(!rst_n)begin busy_sync<=0;busy_previous<=0;end
  else begin busy_sync<={busy_sync[0],busy_async};busy_previous<=busy_sync[1];end
 always @(posedge clk or negedge rst_n)begin
  if(!rst_n)begin
   state<=POWER;count<=0;init_index<=0;adc_reset<=0;convst<=0;
   ready<=0;error<=0;frame_valid<=0;frame<=0;frame_timestamp<=0;
   spi_start<=0;spi_bits<=16;spi_command<=0;conversion_pending<=0;
   reading<=0;pulse<=0;conversion_age<=0;pending_timestamp<=0;reading_timestamp<=0;
  end else begin
   spi_start<=0;frame_valid<=0;
   if(pulse!=0)begin pulse<=pulse-1;if(pulse==1)convst<=0;end
   case(state)
    POWER:if(count==POWER_WAIT_CYCLES-1)begin adc_reset<=1;count<=0;state<=RESET;end else count<=count+1;
    RESET:if(count==RESET_CYCLES-1)begin adc_reset<=0;count<=0;state<=SETUP;end else count<=count+1;
    SETUP:if(count==SETUP_CYCLES-1)begin count<=0;state<=INIT;end else count<=count+1;
    INIT:begin spi_start<=1;spi_bits<=16;spi_command<=init_command(init_index);state<=WAIT_SPI;end
    WAIT_SPI:if(spi_done)begin
     if(init_index==7 && spi_received[23:16]!=8'h10)error<=1;
     if((init_index==9||init_index==11||init_index==13||init_index==15)&&spi_received[23:16]!=8'h11)error<=1;
     if(init_index==16)begin state<=RUN;ready<=!error;end
     else begin init_index<=init_index+1;state<=INIT;end
    end
    RUN:begin
     if(sample_request && !error)begin
      if(conversion_pending || busy_sync[1])error<=1;
      else begin convst<=1;pulse<=2;conversion_pending<=1;
       pending_timestamp<=time_now;conversion_age<=0;end
     end
     if(conversion_pending)begin
      conversion_age<=conversion_age+1;
      if(conversion_age>=CLOCK_HZ/100000)begin error<=1;conversion_pending<=0;end
     end
     if(busy_fall && conversion_pending)begin
      conversion_pending<=0;
      if(spi_busy||reading)error<=1;
      else begin spi_start<=1;spi_bits<=32;spi_command<=0;reading<=1;reading_timestamp<=pending_timestamp;end
     end
     if(spi_done && reading)begin
      frame<=spi_received;frame_timestamp<=reading_timestamp;
      frame_valid<=!error;reading<=0;
     end
    end
    default:error<=1;
   endcase
  end
 end
endmodule
