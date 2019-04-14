#include "stdio.h"
#include "esp_echo.h"
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"

int app_main()
{
    rosserial_setup();

    while(1) {
        rosserial_spinonce();
        vTaskDelay(100);
    }
}
