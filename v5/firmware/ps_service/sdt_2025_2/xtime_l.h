/* Compatibility include for the 2025.2 SDT BSP's xiltimer service.
 * The existing service uses XTime_GetTime and COUNTS_PER_SECOND, both supplied
 * by xiltimer.h/xtimer_config.h. No timer implementation or clock is replaced.
 * Offline candidate only; this header does not qualify the physical platform.
 */
#ifndef SF_SDT_2025_2_XTIME_COMPAT_H
#define SF_SDT_2025_2_XTIME_COMPAT_H
#include "xiltimer.h"
#endif
