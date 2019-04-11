## rosserial_esp32

This package is based on [rosserial](http://wiki.ros.org/rosserial) to enable communication between ROS and ESP32 using ESP-IDF.

### Generate ROS libraries
Follow the steps below in order to generate and include ROS libraries in esp32 project
```
$ cd path/to/catkin_ws/src/
$ git clone https:/www.github.com/sachin0x18/rosserial_esp32.git
$ cd /path/to/esp32_project_dir/
$ mkdir -p main/include/
$ rosrun rosserial_esp32 make_libraries.py .
$ mv main/include/*.cpp main/
```

After execution of above commands, all the necessary ROS files would have been copied into `esp32_project_dir/main/include`

### Examples
> Work in progress
