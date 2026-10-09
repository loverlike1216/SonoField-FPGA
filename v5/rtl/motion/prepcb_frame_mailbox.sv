`timescale 1ns/1ps
// Dual-port BRAM mailbox: 128 words of 17-bit maps, seq at128, last at129.
// PS publishes by toggling publish AFTER all words are written; hold until ready.
module prepcb_frame_mailbox(input wire clk,rst_n,publish,
 output wire bram_clk,bram_rst,output wire [3:0] bram_we,
 output reg bram_en,output reg [31:0] bram_addr,output wire [31:0] bram_wrdata,
 input wire [31:0] bram_rddata,
 output reg frame_valid,output reg [2175:0] frame_data,
 output reg [31:0] frame_sequence,output reg frame_last,input wire frame_ready,
 output wire busy,output reg invalid);
 reg seen;reg [2:0] state;reg [7:0] word_index;
 assign bram_clk=clk;assign bram_rst=~rst_n;assign bram_we=0;assign bram_wrdata=0;
 assign busy=(state!=0)||frame_valid;
 always @(posedge clk or negedge rst_n)begin
  if(!rst_n)begin seen<=0;state<=0;word_index<=0;bram_en<=0;bram_addr<=0;frame_valid<=0;frame_data<=0;frame_sequence<=0;frame_last<=0;invalid<=0;end
  else case(state)
   0:begin
    bram_en<=0;
    if(publish!=seen&&!frame_valid)begin seen<=publish;word_index<=0;bram_addr<=0;bram_en<=1;invalid<=0;state<=1;end
   end
   1:state<=2; // synchronous BRAM read latency
   2:begin
    if(word_index<128)begin
     if(bram_rddata[31:17]!=0)invalid<=1;
     frame_data[word_index*17+:17]<=bram_rddata[16:0];
    end else if(word_index==128)frame_sequence<=bram_rddata;
    else begin frame_last<=bram_rddata[0];if(bram_rddata[31:1]!=0)invalid<=1;end
    if(word_index==129)begin bram_en<=0;state<=3;end
    else begin word_index<=word_index+1;bram_addr<=bram_addr+4;state<=1;end
   end
   3:begin if(!invalid&&frame_sequence!=0)frame_valid<=1;else invalid<=1;state<=4;end
   4:if(invalid||frame_ready)begin frame_valid<=0;state<=0;end
   default:state<=0;
  endcase
 end
endmodule
