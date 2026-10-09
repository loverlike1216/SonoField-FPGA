/* Explicit HOST_FIXTURE. No hardware IO, PS BSP, UART or real sensor. */
#include "adc7606c16.h"
#include <stdio.h>
#include <string.h>
#define REQUIRE(x) do {if(!(x)){fprintf(stderr,"FAIL line %d\n",__LINE__);return 1;}}while(0)
typedef struct {uint8_t regs[64],queued;int fail;} device;
static int transfer(void *ctx,uint16_t command,uint16_t *response){
 device*d=ctx;*response=d->queued;if(d->fail==1)return -1;
 if(command&0x4000){unsigned r=(command>>8)&63;d->queued=d->regs[r];if(d->fail==2&&r==7)d->queued^=1;}
 else if(command){d->regs[(command>>8)&63]=(uint8_t)command;d->queued=0;}
 return 0;
}
static int sensor(void*ctx,unsigned segment,uint8_t address,uint8_t reg,uint16_t*value){
 int mode=*(int*)ctx;(void)segment;(void)address;
 if(mode==1)return -1;
 *value=reg==15?(mode==2?0x0118:0x1117):reg==1?(mode==3?0:mode==4?0x3000:0x2000):mode==5?0x8000:mode==6?6401:3200;
 return 0;
}
int main(void){
 device d;sf_c16 a={&d,transfer,0,0};unsigned mask;int mode;int16_t raw;
 for(mask=0;mask<256;mask++){memset(&d,0,sizeof d);d.regs[47]=0x23;REQUIRE(sf_c16_configure(&a,(uint8_t)mask)==0&&a.ready&&d.regs[7]==mask&&d.regs[2]==0x10);}
 for(mode=1;mode<=2;mode++){memset(&d,0,sizeof d);d.regs[47]=0x23;d.fail=mode;REQUIRE(sf_c16_configure(&a,255)<0&&!a.ready);}
 memset(&d,0,sizeof d);d.regs[47]=0x13;REQUIRE(sf_c16_configure(&a,255)<0&&!a.ready);
 mode=0;for(mask=0;mask<3;mask++){REQUIRE(sf_tmp117_read(&mode,sensor,mask,mask==0?0x48:mask==1?0x49:0x4b,&raw)==0&&raw==3200);}
 for(mode=1;mode<=6;mode++)REQUIRE(sf_tmp117_read(&mode,sensor,0,0x48,&raw)<0);
 mode=0;REQUIRE(sf_tmp117_read(&mode,sensor,1,0x48,&raw)<0);
 puts("PASS HOST_FIXTURE C16 masks256 badID/readback/transfer TMP117 three segments NACK/ID/notready/EEPROM/sentinel/range");return 0;
}
