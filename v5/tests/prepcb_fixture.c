/* Observable HOST_FIXTURE transport for GUI/testing; no physical UART or sensors. */
#include "prepcb_service.h"
#include <string.h>
#include <math.h>
#ifdef _WIN32
#define EXPORT __declspec(dllexport)
#else
#define EXPORT
#endif
static sf_service service;static sf_pc pc;static uint32_t clock_ms,disables,submitted;
static int16_t temps[3];static int healthy,sensor_ok;
static uint8_t response[4096];static size_t response_size;
static uint32_t maps[SF_PC_MAX_FRAMES][128];
static int read32(void *p,uint32_t a,uint32_t *v){(void)p;(void)a;(void)v;return -1;}
static int write32(void *p,uint32_t a,uint32_t v){(void)p;(void)a;(void)v;return -1;}
static int disable(void *p){(void)p;disables++;return 0;}
static void send(void *p,const uint8_t *b,size_t n){(void)p;if(n+response_size<=sizeof(response)){memcpy(response+response_size,b,n);response_size+=n;}}
static int read_temp(void *p,unsigned i,int16_t *v){(void)p;if(!sensor_ok||i>=3)return -1;*v=temps[i];return 0;}
static int safe(void *p){(void)p;return healthy;}
static int raw_read(void *p,uint32_t offset,uint8_t *out,uint32_t count){(void)p;
 if(offset>16384||count>16384-offset)return -1;
 for(uint32_t i=0;i<count;i++){out[i]=(uint8_t)(offset+i);}return 0;}
static int submit(void *p,const uint32_t *words,uint32_t seq,int last){(void)p;(void)last;
 if(submitted>=SF_PC_MAX_FRAMES||seq!=submitted+1)return -1;
 memcpy(maps[submitted++],words,128*4);return 0;}
EXPORT void fixture_init(int16_t center,int16_t up,int16_t dn,unsigned flags){
 sf_io io={0,read32,write32,disable,send};sf_pc_io ext={0,read_temp,safe,submit,0,0,0};
 clock_ms=disables=submitted=0;response_size=0;temps[0]=center;temps[1]=up;temps[2]=dn;
 healthy=!!(flags&2);sensor_ok=!!(flags&1);sf_init(&service,io);sf_pc_init(&pc,ext);sf_pc_attach(&service,&pc);
 if(flags&8)pc.io.raw_read=raw_read; /* explicit synthetic byte pattern; not ADC */
 pc.calibration_verified=!!(flags&4); /* SYNTHETIC_REFERENCE explicit, never hardware provenance */
}
EXPORT void fixture_feed(const uint8_t *p,unsigned n){sf_receive(&service,p,n,clock_ms);}
EXPORT unsigned fixture_read(uint8_t *p,unsigned n){if(n>response_size)n=(unsigned)response_size;memcpy(p,response,n);memmove(response,response+n,response_size-n);response_size-=n;return n;}
EXPORT void fixture_tick(unsigned ms){clock_ms+=ms;sf_pc_tick(&service,clock_ms);}
EXPORT unsigned fixture_cursor(void){return pc.cursor;}
EXPORT unsigned fixture_disables(void){return disables;}
EXPORT unsigned fixture_connected(void){return service.connected;}
EXPORT unsigned fixture_map(unsigned index,uint32_t *words){if(index>=submitted)return 0;memcpy(words,maps[index],128*4);return 128;}
EXPORT void fixture_fault(unsigned flags){healthy=!!(flags&2);sensor_ok=!!(flags&1);}
EXPORT void fixture_set_temp(int16_t center,int16_t up,int16_t dn){temps[0]=center;temps[1]=up;temps[2]=dn;}
EXPORT void fixture_phase_map(const int32_t *target,const int16_t *t,const uint8_t *cal,const double *pose,uint32_t *words){sf_pc_map_geometry(target,t,cal,pose,words);}
EXPORT int fixture_features(const int16_t *data,unsigned frames,unsigned channel,double fs,double f,double *amplitude,double *phase,double *coarse){return sf_pc_features(data,frames,channel,fs,f,amplitude,phase,coarse);}
EXPORT int fixture_pose(const double *pose){
 if(pc.running||pose[2]<.09||pose[2]>.115)return -1;
 for(unsigned i=0;i<6;i++){if(!isfinite(pose[i])||(i<2&&fabs(pose[i])>.005)||(i>=3&&fabs(pose[i])>3))return -1;}
 memcpy(pc.pose,pose,6*sizeof(double));return 0;
}
