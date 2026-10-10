#ifndef SF_ADC7606C16_H
#define SF_ADC7606C16_H
#include <stdint.h>
#include <stddef.h>
/* One bounded transaction must assert/deassert CS and return DOUTA 16-bit word.
 * Physical timing/straps and GPIO ownership belong to a reviewed target adapter.
 */
typedef int (*sf_c16_transfer)(void*,uint16_t,uint16_t*);
typedef struct {void *context;sf_c16_transfer transfer;int ready;uint8_t failed_register;} sf_c16;
int sf_c16_configure(sf_c16 *device,uint8_t bandwidth_mask);
int sf_tmp117_read(void *context,int (*read)(void*,unsigned,uint8_t,uint8_t,uint16_t*),unsigned segment,uint8_t address,int16_t *raw);
#endif
