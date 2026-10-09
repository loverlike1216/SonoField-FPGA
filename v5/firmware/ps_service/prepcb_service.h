#ifndef SF_PREPCB_SERVICE_H
#define SF_PREPCB_SERVICE_H
#include "service.h"
#define SF_PC_MAX_FRAMES 512u
enum {SF_PC_CAPS=32,SF_PC_TEMP=33,SF_PC_CAL_START=34,SF_PC_CAL_PROGRESS=35,
 SF_PC_CAL_RESULT=36,SF_PC_CAL_ABORT=37,SF_PC_UPLOAD=38,SF_PC_START=39,
 SF_PC_PAUSE=40,SF_PC_RESUME=41,SF_PC_STOP=42,SF_PC_RAW=43};
typedef struct {
 void *context;
 int (*read_temp)(void *,unsigned,int16_t *); /* signed TMP117 1/128 C */
 int (*safe_ready)(void *); /* qualified armed + calibration gate, never GUI-owned */
 int (*submit_map)(void *,const uint32_t *,uint32_t,int); /* actual queue ready/ACK path */
 int (*cal_start)(void *); /* bounded single-TX capture scheduler */
 int (*cal_progress)(void *,uint32_t *);
 int (*raw_read)(void *,uint32_t,uint8_t *,uint32_t);
} sf_pc_io;
typedef struct {
 sf_pc_io io;
 int16_t temperature[3];
 int32_t points[SF_PC_MAX_FRAMES][3]; /* signed nanometres; 1nm transport resolution */
 uint32_t total,received,cursor,last_tick_ms;
 uint8_t running,paused,calibrating;
 uint8_t calibration_phase[128];
 uint8_t calibration_verified; /* defaults false; only genuine qualified source may set */
 uint8_t previous_valid;
 uint32_t previous_map[128];
 double pose[6]; /* upper relative to lower: metres and XYZ Euler degrees */
} sf_pc;
void sf_pc_init(sf_pc *,sf_pc_io);
void sf_pc_attach(sf_service *,sf_pc *);
void sf_pc_tick(sf_service *,uint32_t);
uint8_t sf_pc_dispatch(sf_service *,uint8_t,const uint8_t *,size_t,uint8_t *,size_t *);
void sf_pc_map(const int32_t target_um[3],const int16_t temperatures[3],const uint8_t calibration[128],uint32_t words[128]);
void sf_pc_map_geometry(const int32_t[3],const int16_t[3],const uint8_t[128],const double[6],uint32_t[128]);
int sf_pc_features(const int16_t *,unsigned,unsigned,double,double,double *,double *,double *);
#endif
