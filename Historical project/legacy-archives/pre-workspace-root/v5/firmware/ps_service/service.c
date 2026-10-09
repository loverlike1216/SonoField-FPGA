/* Board-independent PS protocol core. All hardware access is explicit via sf_io.
 * Compile on host for cross-language verification or with a reviewed PS BSP.
 * No map/motion capability is advertised in this read/status stage.
 */
#include "service.h"
#include <string.h>
static uint32_t u32(const uint8_t *p) {return (uint32_t)p[0]|(uint32_t)p[1]<<8|(uint32_t)p[2]<<16|(uint32_t)p[3]<<24;}
static void put32(uint8_t *p,uint32_t x) {unsigned i;for(i=0;i<4;i++)p[i]=(uint8_t)(x>>(i*8));}
static uint32_t crc32(const uint8_t *p,size_t n) {
    uint32_t c=0xffffffffu;size_t i;unsigned j;
    for(i=0;i<n;i++){c^=p[i];for(j=0;j<8;j++)c=(c>>1)^(0xedb88320u& (0u-(c&1u)));}
    return ~c;
}
void sf_disconnect(sf_service *s) {s->connected=0;s->used=0;s->last_sequence=0;s->io.disable(s->io.context);}
void sf_init(sf_service *s,sf_io io) {memset(s,0,sizeof(*s));s->io=io;sf_disconnect(s);}
void sf_tick(sf_service *s,uint32_t now) {
    if((s->connected||s->used) && (uint32_t)(now-s->last_rx_ms)>=SF_WATCHDOG_MS)sf_disconnect(s);
}
static void reply(sf_service *s,uint8_t cmd,uint32_t seq,uint8_t status,const uint8_t *p,size_t n) {
    uint8_t out[SF_MAX_PAYLOAD+16];size_t len=n+1;
    memcpy(out,SF_MAGIC,4);out[4]=SF_VERSION;out[5]=cmd|0x80u;put32(out+6,seq);
    out[10]=(uint8_t)len;out[11]=(uint8_t)(len>>8);out[12]=status;
    if(n)memcpy(out+13,p,n);
    put32(out+12+len,crc32(out,12+len));s->io.send(s->io.context,out,16+len);
}
static void dispatch(sf_service *s,uint32_t now) {
    uint8_t cmd=s->buffer[5],status=SF_ERR_OK,out[SF_MAX_PAYLOAD];
    uint8_t *p=s->buffer+12;uint32_t seq=u32(s->buffer+6),address,value=0;
    size_t n=(size_t)s->buffer[10]|(size_t)s->buffer[11]<<8, count=0;
    if(cmd&0x80u){sf_disconnect(s);return;}
    /* Fresh nonce permits reconnect without line-control toggles. Replayed
     * handshake nonce while connected is still a duplicate, not a restart. */
    if(cmd==SF_CMD_PING && seq==1 && n==8 && memcmp(s->nonce,p,8)) {
        memcpy(s->nonce,p,8);sf_disconnect(s);
    }
    if(!s->connected) {
        if(cmd!=SF_CMD_PING||seq!=1){reply(s,cmd,seq,SF_ERR_NOT_CONNECTED,0,0);return;}
        if(s->io.disable(s->io.context)){reply(s,cmd,seq,SF_ERR_BUS_ERROR,0,0);return;}
        s->connected=1;s->last_sequence=0;
    }
    if(seq!=s->last_sequence+1u||s->last_sequence==0xffffffffu) {
        reply(s,cmd,seq,SF_ERR_BAD_SEQUENCE,0,0);sf_disconnect(s);return;
    }
    s->last_sequence=seq;s->last_rx_ms=now;
    switch(cmd) {
    case SF_CMD_PING:
        if(n>32)status=SF_ERR_BAD_FRAME;else {memcpy(out,p,n);count=n;}break;
    case SF_CMD_GET_VERSION:
    case SF_CMD_GET_CAPABILITIES:
        if(n)status=SF_ERR_BAD_FRAME;
        else {put32(out,cmd==SF_CMD_GET_VERSION?SF_VERSION:SF_CAP_BASIC);count=4;}break;
    case SF_CMD_SAFE_DISABLE:
        if(n)status=SF_ERR_BAD_FRAME;
        else if(s->io.disable(s->io.context))status=SF_ERR_BUS_ERROR;
        break;
    case SF_CMD_GET_STATUS:
    case SF_CMD_READ_REGISTER:
        if((cmd==SF_CMD_GET_STATUS&&n!=0)||(cmd==SF_CMD_READ_REGISTER&&n!=4)){status=SF_ERR_BAD_FRAME;break;}
        address=cmd==SF_CMD_GET_STATUS?SF_REG_STATUS:u32(p);
        if(!sf_valid_register(address)){status=SF_ERR_DENIED;break;}
        if(s->io.read32(s->io.context,address,&value))status=SF_ERR_BUS_ERROR;
        else {put32(out,value);count=4;}break;
    case SF_CMD_WRITE_REGISTER:
        if(n!=8){status=SF_ERR_BAD_FRAME;break;}address=u32(p);value=u32(p+4);
        if(!((address==SF_REG_CONTROL&&value==4)||(address==SF_REG_MODE&&value==0)))status=SF_ERR_DENIED;
        else if(s->io.write32(s->io.context,address,value))status=SF_ERR_BUS_ERROR;
        break;
    default: status=SF_ERR_UNSUPPORTED;break;
    }
    reply(s,cmd,seq,status,out,count);
    if(status!=SF_ERR_OK)sf_disconnect(s);
}
void sf_receive(sf_service *s,const uint8_t *data,size_t size,uint32_t now) {
    size_t i,n;
    sf_tick(s,now);
    for(i=0;i<size;i++) {
        if(!s->used)s->last_rx_ms=now;
        s->buffer[s->used++]=data[i];
        if(s->used<=4 && memcmp(s->buffer,SF_MAGIC,s->used)) {sf_disconnect(s);continue;}
        if(s->used>=12) {
            n=(size_t)s->buffer[10]|(size_t)s->buffer[11]<<8;
            if(s->buffer[4]!=SF_VERSION||!u32(s->buffer+6)||n>SF_MAX_PAYLOAD){sf_disconnect(s);continue;}
            if(s->used==n+16) {
                if(crc32(s->buffer,n+12)!=u32(s->buffer+n+12))sf_disconnect(s);
                else {dispatch(s,now);s->used=0;}
            }
        }
    }
}
