#ifndef SF_SERVICE_H
#define SF_SERVICE_H
#include <stdint.h>
#include <stddef.h>
#include "generated.h"
typedef struct {
    void *context;
    int (*read32)(void *, uint32_t, uint32_t *);
    int (*write32)(void *, uint32_t, uint32_t);
    int (*disable)(void *);
    void (*send)(void *, const uint8_t *, size_t);
} sf_io;
typedef struct {
    sf_io io;
    uint8_t buffer[SF_MAX_PAYLOAD+16];
    size_t used;
    uint32_t last_sequence, last_rx_ms;
    int connected;
    uint8_t nonce[8];
} sf_service;
void sf_init(sf_service *, sf_io);
void sf_receive(sf_service *, const uint8_t *, size_t, uint32_t now_ms);
void sf_tick(sf_service *, uint32_t now_ms);
void sf_disconnect(sf_service *);
#endif
