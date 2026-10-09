/* Host verification fixture: register callbacks are a model, not live hardware. */
#include "service.h"
#include <string.h>
#ifdef _WIN32
#define EXPORT __declspec(dllexport)
#else
#define EXPORT
#endif
static sf_service service;static uint32_t regs[32],writes,disabled,clock_ms;
static uint8_t response[4096];static size_t response_size;static int bus_fail;
static int read32(void *p,uint32_t a,uint32_t *v){(void)p;if(bus_fail)return -1;*v=regs[a/4];return 0;}
static int write32(void *p,uint32_t a,uint32_t v){(void)p;if(bus_fail)return -1;regs[a/4]=v;writes++;return 0;}
static int disable(void *p){(void)p;disabled++;regs[0]=0;regs[2]=0;return bus_fail?-1:0;}
static void send(void *p,const uint8_t *d,size_t n){(void)p;if(response_size+n<=sizeof(response)){memcpy(response+response_size,d,n);response_size+=n;}}
EXPORT void fixture_init(void){sf_io io={0,read32,write32,disable,send};memset(regs,0,sizeof(regs));regs[1]=128;writes=disabled=clock_ms=0;response_size=0;bus_fail=0;sf_init(&service,io);}
EXPORT void fixture_feed(const uint8_t *d,unsigned n){sf_receive(&service,d,n,clock_ms);}
EXPORT unsigned fixture_read(uint8_t *p,unsigned n){if(n>response_size)n=(unsigned)response_size;memcpy(p,response,n);memmove(response,response+n,response_size-n);response_size-=n;return n;}
EXPORT void fixture_tick(unsigned n){clock_ms+=n;sf_tick(&service,clock_ms);}
EXPORT unsigned fixture_writes(void){return writes;}
EXPORT unsigned fixture_disabled(void){return disabled;}
EXPORT unsigned fixture_connected(void){return (unsigned)service.connected;}
EXPORT void fixture_bus_fail(unsigned fail){bus_fail=(int)fail;}
