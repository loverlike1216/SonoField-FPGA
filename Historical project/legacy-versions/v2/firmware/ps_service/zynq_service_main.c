/* BSP integration source, NOT linked/downloaded to the physical board.
 * Build requires a reviewed XSA/BSP and explicit SF_* configuration; no defaults.
 * PS UART pinmux/DDR/clocks belong to that reviewed platform, not this service.
 */
#include "service.h"
#include "xuartps.h"
#include "xil_io.h"
#include "xtime_l.h"
#ifndef SF_UART_DEVICE_ID
#error Verified BSP UART device ID required
#endif
#ifndef SF_UART_BAUD
#error Verified UART baud required
#endif
#ifndef SF_PL_BASE
#error Verified AXI base address required
#endif
static XUartPs uart;
static int read_reg(void *p,uint32_t a,uint32_t *v) {
    (void)p;if(!sf_valid_register(a))return -1;*v=Xil_In32(SF_PL_BASE+a);return 0;
}
static int write_reg(void *p,uint32_t a,uint32_t v) {
    (void)p;if(!((a==SF_REG_CONTROL&&v==4)||(a==SF_REG_MODE&&v==0)))return -1;
    Xil_Out32(SF_PL_BASE+a,v);return 0;
}
static int disable(void *p) {return write_reg(p,SF_REG_CONTROL,4)||write_reg(p,SF_REG_MODE,0);}
static uint32_t now_ms(void) {XTime t;XTime_GetTime(&t);return (uint32_t)(t/(COUNTS_PER_SECOND/1000));}
static void send_bytes(void *p,const uint8_t *data,size_t n) {
    uint32_t start=now_ms();size_t pos=0;(void)p;
    while(pos<n && (uint32_t)(now_ms()-start)<100)pos+=XUartPs_Send(&uart,(uint8_t *)data+pos,(unsigned)(n-pos));
    if(pos<n)disable(0);
}
int main(void) {
    sf_service service;sf_io io={0,read_reg,write_reg,disable,send_bytes};uint8_t data[64];unsigned n;
    XUartPs_Config *cfg=XUartPs_LookupConfig(SF_UART_DEVICE_ID);
    if(!cfg || XUartPs_CfgInitialize(&uart,cfg,cfg->BaseAddress)!=XST_SUCCESS)return 1;
    if(XUartPs_SetBaudRate(&uart,SF_UART_BAUD)!=XST_SUCCESS)return 2;
    sf_init(&service,io);
    for(;;){n=XUartPs_Recv(&uart,data,sizeof(data));sf_receive(&service,data,n,now_ms());sf_tick(&service,now_ms());}
}
