`timescale 1ns/1ps
//F six-microtick bit cell; production250MHz =>41.666667MHz SRCLK.
//The historical module name is retained.125MHz start is held for2microticks.
//Registered predecode feeds pad registers without changing source edge schedule.
//RCLK rises at tick24 after fourthSRCLK(tick21), nextSRCLK earliesttick27.
module serializer_pipeline_44 #(
 parameter integer CHANNELS=128,LANES=32,BITS_PER_LANE=4
)(input wire clk,rst_n,start,input wire[CHANNELS-1:0]waveform,
 output reg[LANES-1:0]serial_data,output reg shift_clock,latch_clock,
 output wire busy,output reg frame_done,overrun);
 reg[CHANNELS-1:0]captured;
 reg active,previous_start;
 reg[4:0]age;
 reg[2:0]latch_count;
 reg[31:0]pre_data;
 reg shift_next,latch_next;
 integer l;
 wire request=start&&!previous_start;
 assign busy=active&&(age!=23);
 initial if(CHANNELS!=128||LANES!=32||BITS_PER_LANE!=4)
  $fatal(1,"F candidate is deliberately128TX32lane4bit only");
 always@(posedge clk or negedge rst_n)begin
  if(!rst_n)begin
   captured<=0;serial_data<=0;shift_clock<=0;latch_clock<=0;
   active<=0;previous_start<=0;age<=0;latch_count<=0;
   frame_done<=0;overrun<=0;pre_data<=0;shift_next<=0;latch_next<=0;
  end else begin
   previous_start<=start;
   shift_clock<=shift_next;latch_clock<=latch_next;
   frame_done<=latch_clock&&!latch_next;
   if(!active||age>=22)for(l=0;l<32;l=l+1)pre_data[l]<=waveform[l*4+3];
   if(latch_count!=0)begin
    latch_count<=latch_count-1;
    
    if(latch_count==1)latch_next<=0;
   end
   if(active)begin
    age<=age+1;
    case(age)
     1,7,13,19:shift_next<=1;
     4:begin shift_next<=0;for(l=0;l<32;l=l+1)pre_data[l]<=captured[l*4+2];end
     10:begin shift_next<=0;for(l=0;l<32;l=l+1)pre_data[l]<=captured[l*4+1];end
     16:begin shift_next<=0;for(l=0;l<32;l=l+1)pre_data[l]<=captured[l*4];end
     5,11,17:serial_data<=pre_data;
     22:begin shift_next<=0;latch_next<=1;latch_count<=3;end
     23:active<=0;
    endcase
   end
   if(request)begin
    if(busy)overrun<=1;
    else begin
     captured<=waveform;age<=0;active<=1;
     serial_data<=pre_data;
    end
   end
  end
 end
endmodule
