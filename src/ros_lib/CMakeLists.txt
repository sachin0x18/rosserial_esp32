set (srcs
    "duration.cpp"
    "time.cpp")

if(CONFIG_ROSSERIAL_OVER_WIFI)
     list(APPEND srcs "esp_ros_wifi.c")
 endif()


idf_component_register(SRCS "${srcs}"
                       INCLUDE_DIRS "include"
                       REQUIRES vfs nvs_flash)
