/* Executable host/target-portable extensions. Target adapter/BSP separately gated.
 * No sensor defaults, no automatic ARM, no fictitious CAL_RESULT quality.
 */
#include "prepcb_service.h"
#include <math.h>
#include <string.h>
static uint32_t get32(const uint8_t *p){return (uint32_t)p[0]|(uint32_t)p[1]<<8|(uint32_t)p[2]<<16|(uint32_t)p[3]<<24;}
static void put32(uint8_t *p,uint32_t v){unsigned i;for(i=0;i<4;i++)p[i]=(uint8_t)(v>>(8*i));}
void sf_pc_init(sf_pc *p,sf_pc_io io){memset(p,0,sizeof(*p));p->io=io;p->pose[2]=.1;}
void sf_pc_attach(sf_service *s,sf_pc *p){s->extension=p;}
static int poll_temp(sf_pc *p){unsigned i;for(i=0;i<3;i++){
 if(!p->io.read_temp||p->io.read_temp(p->io.context,i,&p->temperature[i])||p->temperature[i]<0||p->temperature[i]>50*128)return -1;
 }return 0;}
void sf_pc_map(const int32_t target_um[3],const int16_t temperatures[3],const uint8_t calibration[128],uint32_t words[128]){
 const double nominal[6]={0,0,.1,0,0,0};
 sf_pc_map_geometry(target_um,temperatures,calibration,nominal,words);
}
static double temperature_at(double z,const int16_t t[3],double gap){
 double center=t[0]/128.;
 return z>=0?center+(t[1]/128.-center)*fmin(1,2*z/gap):center+(t[2]/128.-center)*fmin(1,-2*z/gap);
}
void sf_pc_map_geometry(const int32_t target_um[3],const int16_t temperatures[3],const uint8_t calibration[128],const double pose[6],uint32_t words[128]){
 unsigned channel;const double pi=3.14159265358979323846;
 double sx=sin(pose[3]*pi/180),cx=cos(pose[3]*pi/180),sy=sin(pose[4]*pi/180),cy=cos(pose[4]*pi/180),sz=sin(pose[5]*pi/180),cz=cos(pose[5]*pi/180);
 for(channel=0;channel<128;channel++){
  double x=(-42+12*(int)(channel%8))*.001,y=(-42+12*(int)((channel%64)/8))*.001,z=0;
  if(channel<64){double a=x,b=y;
   x=cz*cy*a+(cz*sy*sx-sz*cx)*b+pose[0];
   y=sz*cy*a+(sz*sy*sx+cz*cx)*b+pose[1];z=-sy*a+cy*sx*b+pose[2];}
  x-=pose[0]/2;y-=pose[1]/2;z-=pose[2]/2;
  double dx=target_um[0]*1e-9-x,dy=target_um[1]*1e-9-y,dz=target_um[2]*1e-9-z;
  double length=sqrt(dx*dx+dy*dy+dz*dz),integral=0;
  /* Exact piecewise-linear inverse-speed integral, independent of Python Gauss. */
  double split[5]={0,1,1,1,1};unsigned segments=1;
  for(int knot=-1;knot<=1;knot++)if(fabs(dz)>1e-15){
   double t=(knot*pose[2]/2-z)/dz;if(t>0&&t<1)split[segments++]=t;
  }
  split[segments]=1;
  for(unsigned a=0;a<=segments;a++)for(unsigned b=a+1;b<=segments;b++)if(split[b]<split[a]){double tmp=split[a];split[a]=split[b];split[b]=tmp;}
  for(unsigned part=0;part<segments;part++){
   double lo=split[part],hi=split[part+1];
   double ca=331.3+.606*temperature_at(z+lo*dz,temperatures,pose[2]);
   double cb=331.3+.606*temperature_at(z+hi*dz,temperatures,pose[2]);
   integral+=(hi-lo)*(fabs(cb-ca)<1e-9?1/ca:log1p((cb-ca)/ca)/(cb-ca));
  }
  double phase=-40000*length*integral*256+(channel>=64?128:0);
  int code=(int)nearbyint(phase);
  words[channel]=0x10000u|((uint32_t)calibration[channel]<<8)|(uint8_t)code;
 }
}
void sf_pc_tick(sf_service *s,uint32_t now){
 sf_pc *p=s->extension;uint32_t words[128];
 if(!p)return;
 sf_tick(s,now);
 if(!s->connected||!p->io.safe_ready||!p->io.safe_ready(p->io.context)){
  p->running=p->paused=p->calibrating=0;s->io.disable(s->io.context);return;
 }
 if(!p->running||p->paused||(uint32_t)(now-p->last_tick_ms)<20)return;
 if(poll_temp(p)){p->running=0;sf_disconnect(s);return;}
 sf_pc_map_geometry(p->points[p->cursor],p->temperature,p->calibration_phase,p->pose,words);
 if(p->previous_valid)for(unsigned i=0;i<128;i++){
  int delta=((int)(words[i]&255)-(int)(p->previous_map[i]&255)+384)%256-128;
  if(delta>8||delta< -8){p->running=0;sf_disconnect(s);return;}
 }
 if(!p->io.submit_map||p->io.submit_map(p->io.context,words,p->cursor+1,p->cursor+1==p->total)){
  p->running=0;sf_disconnect(s);return;
 }
 memcpy(p->previous_map,words,sizeof(words));p->previous_valid=1;
 p->last_tick_ms=now;if(++p->cursor==p->total)p->running=0;
}
uint8_t sf_pc_dispatch(sf_service *s,uint8_t cmd,const uint8_t *data,size_t n,uint8_t *out,size_t *count){
 sf_pc *p=s->extension;unsigned i;uint32_t total,index,progress;
 *count=0;if(!p)return SF_ERR_UNSUPPORTED;
 if(cmd!=SF_PC_UPLOAD&&cmd!=SF_PC_RAW&&n)return SF_ERR_BAD_FRAME;
 switch(cmd){
 case SF_PC_CAPS:
  put32(out,0x47u|(p->io.raw_read?8u:0u)|((p->io.cal_start&&p->io.cal_progress)?16u:0u));
  put32(out+4,SF_PC_MAX_FRAMES);put32(out+8,50);*count=12;return SF_ERR_OK;
 case SF_PC_TEMP:
  if(poll_temp(p))return SF_ERR_BUS_ERROR;
  for(i=0;i<3;i++){out[2*i]=(uint8_t)p->temperature[i];out[2*i+1]=(uint8_t)(p->temperature[i]>>8);}*count=6;return SF_ERR_OK;
 case SF_PC_CAL_START:
  if(p->running||!p->io.safe_ready||!p->io.safe_ready(p->io.context)||poll_temp(p)||!p->io.cal_start||p->io.cal_start(p->io.context))return SF_ERR_DENIED;
  p->calibrating=1;return SF_ERR_OK;
 case SF_PC_CAL_PROGRESS:
  if(!p->io.cal_progress||p->io.cal_progress(p->io.context,&progress))return SF_ERR_BUS_ERROR;
  put32(out,progress);*count=4;return SF_ERR_OK;
 case SF_PC_CAL_RESULT:
  /* Geometry fitting runs on PC; no board solver/measurement claim. */
  out[0]=p->calibration_verified?1:0;*count=1;return SF_ERR_OK;
 case SF_PC_CAL_ABORT:case SF_PC_STOP:
  p->running=p->paused=p->calibrating=0;s->io.disable(s->io.context);return SF_ERR_OK;
 case SF_PC_UPLOAD:
  if(n<20||(n-8)%12||p->running)return SF_ERR_BAD_FRAME;
  total=get32(data);index=get32(data+4);
  if(!total||total>SF_PC_MAX_FRAMES||index+(n-8)/12>total)return SF_ERR_DENIED;
  if(index==0){p->received=0;p->total=total;p->cursor=0;}
  if(index!=p->received||total!=p->total)return SF_ERR_BAD_SEQUENCE;
  for(i=8;i<n;i+=12){for(unsigned axis=0;axis<3;axis++){
   int32_t v=(int32_t)get32(data+i+4*axis);int32_t bound=axis==2?6000000:10000000;
   if(v < -bound||v>bound)return SF_ERR_DENIED;
   p->points[p->received][axis]=v;
  }p->received++;}put32(out,p->received);*count=4;return SF_ERR_OK;
 case SF_PC_START:
  if(!p->calibration_verified||p->received!=p->total||!p->total||poll_temp(p)||!p->io.safe_ready||!p->io.safe_ready(p->io.context))return SF_ERR_DENIED;
  for(i=1;i<p->total;i++){
   double step2=0,acc2=0,jerk2=0;
   for(unsigned axis=0;axis<3;axis++){
    double step=(p->points[i][axis]-p->points[i-1][axis])*1e-6;
    step2+=step*step;
    if(i>=2){double a=(p->points[i][axis]-2.*p->points[i-1][axis]+p->points[i-2][axis])*1e-6*2500;acc2+=a*a;}
    if(i>=3){double j=(p->points[i][axis]-3.*p->points[i-1][axis]+3.*p->points[i-2][axis]-p->points[i-3][axis])*1e-6*125000;jerk2+=j*j;}
   }
   /* Fixed nominal guards + independently derived nanometre rounding budget. */
   if(step2>.200002*.200002||acc2>8.01*8.01||jerk2>41*41)return SF_ERR_DENIED;
  }
  p->cursor=0;p->previous_valid=0;p->running=1;p->paused=0;p->last_tick_ms=s->last_rx_ms;return SF_ERR_OK;
 case SF_PC_PAUSE:if(!p->running)return SF_ERR_DENIED;p->paused=1;return SF_ERR_OK;
 case SF_PC_RESUME:if(!p->running||!p->paused||poll_temp(p)||!p->io.safe_ready||!p->io.safe_ready(p->io.context))return SF_ERR_DENIED;p->paused=0;p->last_tick_ms=s->last_rx_ms;return SF_ERR_OK;
 case SF_PC_RAW:
  if(n!=8||!p->io.raw_read)return SF_ERR_DENIED;
  index=get32(data);total=get32(data+4);
  if(total>240||index>16384||total>16384-index||p->io.raw_read(p->io.context,index,out+8,total))return SF_ERR_DENIED;
  put32(out,index);put32(out+4,total);*count=total+8;return SF_ERR_OK;
 default:return SF_ERR_UNSUPPORTED;
 }
}
int sf_pc_features(const int16_t *data,unsigned frames,unsigned channel,double fs,double f,double *amplitude,double *phase,double *coarse_s){
 double re=0,im=0,energy=0,peak=0;unsigned onset=0;
 if(!data||frames<16||frames>1024||channel>=8||fs<=2*f||f<38500||f>41500)return -1;
 for(unsigned i=0;i<frames;i++){double v=data[8*i+channel];if(v>=32760||v<=-32760)return -2;
  re+=v*cos(2*3.14159265358979323846*f*i/fs);im-=v*sin(2*3.14159265358979323846*f*i/fs);
  if(fabs(v)>peak)peak=fabs(v);
  energy+=v*v;
 }
 if(energy==0)return -3;
 for(unsigned i=0;i<frames;i++)if(fabs((double)data[8*i+channel])>.25*peak){onset=i;break;}
 *amplitude=2*sqrt(re*re+im*im)/frames;*phase=atan2(im,re);*coarse_s=onset/fs;
 return 0; /* envelope onset is an ESTIMATE requiring ring-up/frontend qualification */
}
