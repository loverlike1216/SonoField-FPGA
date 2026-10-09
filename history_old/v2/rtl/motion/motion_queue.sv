`timescale 1ns/1ps
// PS execution boundary: complete maps enter a bounded ring. A PL clock owns cadence.
// Single bus master while running; integration/arbitration into PS is not deployed.
module motion_queue #(
 parameter integer DEPTH=4, INTERVAL_CYCLES=2640000, ACK_TIMEOUT_CYCLES=6600
)(input wire clk,rst_n,arm,stop,
 input wire frame_valid,input wire [2175:0] frame_data,
 input wire [31:0] frame_sequence,input wire frame_last,
 output wire frame_ready,output wire [31:0] count,
 output reg bus_valid,bus_write,output reg [7:0] bus_address,output reg [31:0] bus_wdata,
 input wire bus_ready,bus_error,input wire map_ack,
 output reg running,done,underflow,overflow,invalid_frame,ack_timeout,
 output wire disable_request,output reg [31:0] acknowledged_sequence,
 output reg request_pulse,output reg ack_pulse);
 reg [2175:0] queue[0:DEPTH-1]; reg [31:0] seq[0:DEPTH-1]; reg last[0:DEPTH-1];
 localparam integer PTR_BITS=$clog2(DEPTH);
 localparam integer TIMER_BITS=$clog2(INTERVAL_CYCLES);
 localparam integer WATCHDOG_BITS=$clog2(ACK_TIMEOUT_CYCLES+1);
 localparam integer COUNT_BITS=$clog2(DEPTH+1);
 reg [COUNT_BITS-1:0] occupancy;
 assign count=occupancy;
 reg [PTR_BITS-1:0] rd,wr;
 reg [6:0] channel;
 reg [3:0] state;
 reg [TIMER_BITS-1:0] timer;
 reg [WATCHDOG_BITS-1:0] watchdog;
 reg [2175:0] active; reg [31:0] active_sequence,next_sequence; reg active_last;
 reg stopped,sealed;
 // Static 17-bit slices and balanced 8:1/16:1 selection avoid the old
 // integer channel*17 barrel selector/DSP. This changes no bus cycle.
 wire [16:0] lane_word[0:127];
 reg [16:0] selected_bank[0:15];
 genvar lane,bank;
 generate
  for(lane=0;lane<128;lane=lane+1)begin: words
   assign lane_word[lane]=active[lane*17+:17];
  end
  for(bank=0;bank<16;bank=bank+1)begin: selectors
   always @* begin
    case(channel[2:0])
     0:selected_bank[bank]=lane_word[bank*8+0];
     1:selected_bank[bank]=lane_word[bank*8+1];
     2:selected_bank[bank]=lane_word[bank*8+2];
     3:selected_bank[bank]=lane_word[bank*8+3];
     4:selected_bank[bank]=lane_word[bank*8+4];
     5:selected_bank[bank]=lane_word[bank*8+5];
     6:selected_bank[bank]=lane_word[bank*8+6];
     7:selected_bank[bank]=lane_word[bank*8+7];
    endcase
   end
  end
 endgenerate
 wire [16:0] selected_word=selected_bank[channel[6:3]];
 wire fault=underflow||overflow||invalid_frame||ack_timeout||bus_error;
 wire pop=running&&timer==0&&state==0&&occupancy!=0;
 assign frame_ready=rst_n&&!fault&&!stop&&!stopped&&!sealed&&(occupancy<DEPTH)&&!pop;
 assign disable_request=!rst_n||stop||stopped||fault;
 // No acceptance on the same cycle as pop: avoids ambiguous FIFO occupancy updates.
 wire push=frame_valid&&frame_ready&&!pop;
 reg enabled_any;
 integer i;
 always @* begin
  enabled_any=0;
  for(integer n=0;n<128;n=n+1)enabled_any=enabled_any||frame_data[n*17+16];
 end
 initial begin
  if(DEPTH<2||INTERVAL_CYCLES<800||ACK_TIMEOUT_CYCLES<1)$fatal(1,"Invalid motion queue parameters");
 end
 always @(posedge clk or negedge rst_n) begin
  if(!rst_n)begin
   rd<=0;wr<=0;occupancy<=0;running<=0;done<=0;underflow<=0;overflow<=0;invalid_frame<=0;ack_timeout<=0;
   bus_valid<=0;bus_write<=1;bus_address<=0;bus_wdata<=0;state<=0;timer<=0;watchdog<=0;
   active<=0;active_sequence<=0;next_sequence<=0;active_last<=0;channel<=0;
   acknowledged_sequence<=32'hffffffff;request_pulse<=0;ack_pulse<=0;
   stopped<=0;sealed<=0;
  end else begin
   request_pulse<=0;ack_pulse<=0;bus_valid<=0;
   if(stop||fault||stopped)begin
    if(stop)stopped<=1;
    running<=0;occupancy<=0;state<=0;rd<=0;wr<=0;next_sequence<=0;done<=0;
   end else begin
    if(frame_valid&&(occupancy>=DEPTH))overflow<=1;
    if(frame_valid&&sealed)invalid_frame<=1;
    if(push)begin
     if(frame_sequence!=next_sequence||!enabled_any)invalid_frame<=1;
     else begin
      queue[wr]<=frame_data;seq[wr]<=frame_sequence;last[wr]<=frame_last;
      wr<=(wr==DEPTH-1)?0:wr+1'b1;occupancy<=occupancy+1;next_sequence<=next_sequence+1;
      if(frame_last)sealed<=1;
     end
    end
    if(arm&&!running&&!done)begin
     if(occupancy>=2||(occupancy==1&&last[rd]))begin running<=1;timer<=0;end
     else underflow<=1;
    end
    if(running&&timer>0)timer<=timer-1;
    if(running&&timer==0&&state!=0)ack_timeout<=1;
    if(running&&timer==0&&state==0)begin
     if(occupancy==0)underflow<=1;
     else begin
      active<=queue[rd];active_sequence<=seq[rd];active_last<=last[rd];
      rd<=(rd==DEPTH-1)?0:rd+1'b1;occupancy<=occupancy-1;channel<=0;state<=1;
      timer<=INTERVAL_CYCLES-1;request_pulse<=1;
     end
    end
    case(state)
     1:begin bus_valid<=1;bus_address<=8'h54;bus_wdata<={25'b0,channel};state<=2;end
     2:if(bus_ready)state<=3;else state<=1;
     3:begin bus_valid<=1;bus_address<=8'h58;bus_wdata<={15'b0,selected_word};state<=4;end
     4:if(bus_ready)state<=5;else state<=3;
     5:begin bus_valid<=1;bus_address<=8'h5c;bus_wdata<=1;state<=6;end
     6:if(bus_ready)begin if(channel==127)state<=7;else begin channel<=channel+1;state<=1;end end else state<=5;
     7:begin bus_valid<=1;bus_address<=8'h60;bus_wdata<=1;state<=8;watchdog<=0;end
     8:begin
      if(map_ack)begin
       acknowledged_sequence<=active_sequence;ack_pulse<=1;state<=0;
       if(active_last)begin running<=0;done<=1;end
      end else if(watchdog>=ACK_TIMEOUT_CYCLES)ack_timeout<=1;
      else watchdog<=watchdog+1;
     end
     default:begin end
    endcase
   end
  end
 end
endmodule
