#include "adc7606c16.h"
static int read_register(sf_c16 *d,uint8_t address,uint8_t *value){
 uint16_t response;
 if(d->transfer(d->context,(uint16_t)(0x4000u|((uint16_t)address<<8)),&response)||d->transfer(d->context,0x4000u,&response))return -1;
 *value=(uint8_t)response;return 0;
}
int sf_c16_configure(sf_c16 *d,uint8_t bandwidth_mask){
 static const uint8_t address[]={2,3,4,5,6,7,8,0x21};
 uint8_t values[]={0x10,0x11,0x11,0x11,0x11,bandwidth_mask,0,0};
 uint8_t id,value;uint16_t response;size_t i;
 if(!d||!d->transfer)return -1;
 d->ready=0;d->failed_register=0x2f;
 if(read_register(d,0x2f,&id)||(id>>4)!=2)return -2;
 for(i=0;i<sizeof(address);i++){
  d->failed_register=address[i];
  if(d->transfer(d->context,(uint16_t)(((uint16_t)address[i]<<8)|values[i]),&response))return -3;
 }
 for(i=0;i<sizeof(address);i++){
  d->failed_register=address[i];
  if(read_register(d,address[i],&value)||value!=values[i])return -4;
 }
 if(d->transfer(d->context,0,&response))return -5;
 d->failed_register=0;d->ready=1;return 0;
}
int sf_tmp117_read(void *context,int (*read)(void*,unsigned,uint8_t,uint8_t,uint16_t*),unsigned segment,uint8_t address,int16_t *raw){
 uint16_t id,config,value;
 if(!read||!raw||segment>2||address!=(segment==0?0x48:segment==1?0x49:0x4b))return -1;
 if(read(context,segment,address,15,&id)||(id&0x0fffu)!=0x0117u)return -2;
 if(read(context,segment,address,1,&config)||(config&0x1000u)||!(config&0x2000u))return -3;
 if(read(context,segment,address,0,&value)||value==0x8000u)return -4;
 if((int16_t)value<0||(int16_t)value>6400)return -5;
 *raw=(int16_t)value;return 0;
}
