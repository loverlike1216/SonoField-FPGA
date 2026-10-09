/* Explicit HOST_FIXTURE executable; files supply sensors/raw captures/health.
 * It proves C behavior, never a PS/ADC/physical UART result.
 */
#include "prepcb_service.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef struct {sf_pc pc;FILE *response,*maps;int16_t temps[3];uint8_t flags;uint32_t disables;} fixture;
static int rd(void *p,uint32_t a,uint32_t *v){(void)p;(void)a;(void)v;return -1;}
static int wr(void *p,uint32_t a,uint32_t v){(void)p;(void)a;(void)v;return -1;}
static int disable(void *p){((fixture*)p)->disables++;return 0;}
static void send_data(void *p,const uint8_t *b,size_t n){fwrite(b,1,n,((fixture*)p)->response);}
static int temperature(void *p,unsigned i,int16_t *v){fixture *f=p;if(!(f->flags&1)||i>=3)return -1;*v=f->temps[i];return 0;}
static int ready(void *p){return (((fixture*)p)->flags&2)!=0;}
static int submit(void *p,const uint32_t *words,uint32_t seq,int last){fixture *f=p;
 fwrite(&seq,4,1,f->maps);fwrite(&last,4,1,f->maps);return fwrite(words,4,128,f->maps)!=128;}
static int cal_start(void *p){return ready(p)?0:-1;}
static int progress(void *p,uint32_t *v){(void)p;*v=0;return 0;}
int main(int argc,char **argv){fixture f;sf_service s;uint8_t input[272];size_t n;uint32_t now=0;
 if(argc!=6){fprintf(stderr,"HOST_FIXTURE requests sensor_input responses maps trace\n");return 2;}
 memset(&f,0,sizeof(f));FILE *sensor=fopen(argv[2],"rb"),*req=fopen(argv[1],"rb"),*trace=fopen(argv[5],"w");
 f.response=fopen(argv[3],"wb");f.maps=fopen(argv[4],"wb");
 if(!sensor||!req||!trace||!f.response||!f.maps)return 3;
 if(fread(f.temps,2,3,sensor)!=3||fread(&f.flags,1,1,sensor)!=1)return 4;
 fclose(sensor);
 sf_io io={&f,rd,wr,disable,send_data};sf_pc_io ext={&f,temperature,ready,submit,cal_start,progress,0};
 sf_init(&s,io);sf_pc_init(&f.pc,ext);sf_pc_attach(&s,&f.pc);
 f.pc.calibration_verified=(f.flags&4)!=0; /* explicit synthetic calibration fixture flag */
 while(fread(&n,sizeof(n),1,req)==1){
  if(n>sizeof(input)||fread(input,1,n,req)!=n)return 5;
  sf_receive(&s,input,n,now);sf_pc_tick(&s,now);now+=1;
 }
 for(unsigned i=0;i<f.pc.total+1&&f.pc.running;i++){
  now+=20;s.last_rx_ms=now; /* explicit HOST_FIXTURE heartbeat; real service requires fresh valid packet */
  sf_pc_tick(&s,now);
 }
 sf_tick(&s,now+1000);sf_pc_tick(&s,now+1000);
 fprintf(trace,"{\"classification\":\"HOST_FIXTURE\",\"received\":%u,\"submitted\":%u,\"disables\":%u,\"connected_after_timeout\":%d}\n",f.pc.received,f.pc.cursor,f.disables,s.connected);
 fclose(req);fclose(trace);fclose(f.response);fclose(f.maps);return 0;
}
