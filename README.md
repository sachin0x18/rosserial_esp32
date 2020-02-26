## rosserial_esp32

This package is based on [rosserial](http://wiki.ros.org/rosserial) to enable communication between ROS and ESP32 using ESP-IDF.

Supports rosserial communication over **UART** and **WiFi**

### Generate ROS libraries
Follow the steps below in order to generate and include ROS libraries
(This will create a component in IDF_PATH and need to generate it only once)

```
$ cd path/to/catkin_ws/src/
$ git clone https:/www.github.com/sachin0x18/rosserial_esp32.git
$ rosrun rosserial_esp32 make_libraries.py $IDF_PATH/components/
```

After execution of above commands, all the necessary ROS files would have been generated in `$IDF_PATH/components/rosserial_esp32/`

### Examples
* [chatter](src/examples/chatter)
* [echo](src/examples/echo)
