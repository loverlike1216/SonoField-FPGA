`timescale 1ns/1ps
// Independent C-16 digital model. No analog/CRC-enabled transfer is simulated.
module ad7606c16_model(input wire reset,convst,cs_n,sclk,sdi,hold_busy,
 input wire [2:0] inject,output reg busy,output reg [3:0] dout,output reg configured);
 reg [7:0] registers[0:63];reg register_mode;reg [5:0] address;
 reg [31:0] stream[0:3];reg [15:0] incoming;reg [127:0] converted;
 integer i,n,edges,conversion;real last_sample,last_rise,last_fall;
 function [15:0] sample(input integer c,input integer seq);
  case(c)
   0:sample=16'h8000+seq;1:sample=16'h7fff-seq;2:sample=16'hffff;
   3:sample=16'h0000;4:sample=16'h0001;5:sample=16'h8001;
   6:sample=16'h1234+seq;default:sample=16'habcd-seq;
  endcase
 endfunction
 task defaults;
  begin
   for(i=0;i<64;i=i+1)registers[i]=0;
   registers[2]=8'h08;for(i=3;i<=6;i=i+1)registers[i]=8'h33;
   registers[47]=8'h23;address=0;register_mode=0;configured=0;busy=0;conversion=0;
   last_sample=-10000;last_rise=0;last_fall=0;
  end
 endtask
 initial begin defaults();dout=0;converted=0;end
 always @(posedge reset)begin disable converting;defaults();end
 always @(posedge convst)begin: converting
  if(!configured)$fatal(1,"C16 conversion without verified software configuration");
  if($realtime-last_sample<1249.9)$fatal(1,"C16 exceeds initial800kSPS profile");
  last_sample=$realtime;
  #22 busy=1;
  if(conversion%2==0)#628;else #478;
  if(!hold_busy)begin
   if(!cs_n)$fatal(1,"C16 read crosses BUSY data replacement");
   if(last_rise!=0&&$realtime-last_rise<25)$fatal(1,"C16 missing read-before-BUSY margin");
   for(i=0;i<8;i=i+1)converted[16*i+:16]=sample(i,conversion);
   conversion=conversion+1;busy=0;
  end
 end
 always @(negedge cs_n)begin
  n=0;edges=0;incoming=0;
  for(i=0;i<4;i=i+1)begin
   if(register_mode)stream[i]=(i==0?{8'b0,registers[address],16'b0}:0);
   else stream[i]={converted[32*i+:16],converted[32*i+16+:16]};
   if(inject==1&&address==7&&i==0)stream[i]=0; // incorrect BW readback
   if(inject==2)stream[i]=32'hffffffff; // absent / pulled-up device
   if(inject==3&&address==2&&i==0)stream[i]={8'b0,8'h50,16'b0}; // wrong status format
   if(inject==4&&i==0&&register_mode)stream[i]={8'b0,registers[(address+1)%64],16'b0};
   if(inject==5&&address==33&&i==0)stream[i]={8'b0,8'h04,16'b0}; // unexpected CRC enable
   dout[i]<=#18 stream[i][31];
  end
 end
 always @(negedge sclk)if(!cs_n)begin
  if(last_rise!=0&&$realtime-last_rise<12)$fatal(1,"C16 SCLK high timing");
  last_fall=$realtime;incoming={incoming[14:0],sdi};edges=edges+1;
 end
 always @(posedge sclk)if(!cs_n)begin
  if($realtime-last_fall<12)$fatal(1,"C16 SCLK low timing");
  last_rise=$realtime;n=n+1;
  for(i=0;i<4;i=i+1)dout[i]<=#15.7(n<32?stream[i][31-n]:1'b0);
 end
 always @(posedge cs_n)if(edges==16)begin
  if(incoming[15:14]==2'b01)begin address=incoming[13:8];register_mode=1;end
  else if(register_mode&&incoming[15:14]==0)begin
   address=incoming[13:8];
   if(address==0)begin register_mode=0;configured=(registers[2]==8'h10&&registers[3]==8'h11&&registers[4]==8'h11&&registers[5]==8'h11&&registers[6]==8'h11&&registers[8]==0&&registers[33]==0);end
   else registers[address]=incoming[7:0];
  end
 end
endmodule
