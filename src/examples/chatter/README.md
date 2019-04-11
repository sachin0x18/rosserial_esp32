## Chatter

This code publishes data on the topic `chatter`

### Build and Flash

Generate the ROS libraries prior to building this example as instructed in the README of root directory

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
$ rostopic echo chatter
```
