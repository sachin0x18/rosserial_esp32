## Echo

This code subscribes to `echo` and publishes on `ack`
The data received on `echo` will be published on `ack`

### Build and Flash

Generate the ROS libraries prior to building this example as instructed in the README of root directory (If done already, ignore)

```
$ export ESPPORT=/dev/ttyUSB0
$ make defconfig
$ make -j4 flash
```

On a new terminal

```
$ roscore
```

On another new terminal

```
$ rosrun rosserial_python serial_node.py _baud:=115200
```

On another new terminal
```
$ rostopic echo ack
```

On another new terminal
```
rostopic pub echo std_msgs/String "Hello World\!" --once
```
