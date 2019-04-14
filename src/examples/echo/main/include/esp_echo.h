#ifndef ESP_SUBSCRIBER_H
#define ESP_SUBSCRIBER_H

#ifdef __cplusplus
extern "C" {
#endif

void rosserial_setup();

void rosserial_spinonce();

#ifdef __cplusplus
}
#endif

#endif /* ESP_SUBSCRIBER_H */
