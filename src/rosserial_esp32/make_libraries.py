#!/usr/bin/env python

# Software License Agreement (BSD License)
#
# Copyright (c) 2019, Sachin Parekh
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import rospkg
import rosserial_client
from rosserial_client.make_library import *

THIS_PACKAGE = "rosserial_esp32"

__usage__ = """
make_libraries.py generates the ESP32 rosserial library files for ESP32 (ESP-IDF).
It requires the location of your esp-idf/components folder.

rosrun rosserial_esp32 make_libraries.py $IDF_PATH/components
"""

# for copying files
import shutil

ROS_TO_EMBEDDED_TYPES = {
    'bool'    :   ('bool',              1, PrimitiveDataType, []),
    'byte'    :   ('int8_t',            1, PrimitiveDataType, []),
    'int8'    :   ('int8_t',            1, PrimitiveDataType, []),
    'char'    :   ('char',              1, PrimitiveDataType, []),
    'uint8'   :   ('uint8_t',           1, PrimitiveDataType, []),
    'int16'   :   ('int16_t',           2, PrimitiveDataType, []),
    'uint16'  :   ('uint16_t',          2, PrimitiveDataType, []),
    'int32'   :   ('int32_t',           4, PrimitiveDataType, []),
    'uint32'  :   ('uint32_t',          4, PrimitiveDataType, []),
    'int64'   :   ('int64_t',           8, PrimitiveDataType, []),
    'uint64'  :   ('uint64_t',          8, PrimitiveDataType, []),
    'float32' :   ('float',             4, PrimitiveDataType, []),
    'float64' :   ('double',            8, PrimitiveDataType, []),
    'time'    :   ('ros::Time',         8, TimeDataType, ['ros/time']),
    'duration':   ('ros::Duration',     8, TimeDataType, ['ros/duration']),
    'string'  :   ('char*',             0, StringDataType, []),
    'Header'  :   ('std_msgs::Header',  0, MessageDataType, ['std_msgs/Header'])
}

# need correct inputs
if (len(sys.argv) < 2):
    print __usage__
    exit()

# get output path
path = sys.argv[1]

if path[-1] == "/":
    path = path[0:-1]
print "\nExporting to %s" % path

rospack = rospkg.RosPack()

# Create rosserial_esp32 component folder if it doesn't exists
if not os.path.exists(path+"/rosserial_esp32/"):
    os.makedirs(path+"/rosserial_esp32/include/")
    with open(path+"/rosserial_esp32/component.mk", "w") as file:
        pass

# copy ros_lib stuff in
rosserial_esp32_dir = rospack.get_path(THIS_PACKAGE)
files = os.listdir(rosserial_esp32_dir+"/src/ros_lib")
for f in files:
    if os.path.isfile(rosserial_esp32_dir+"/src/ros_lib/"+f):
        if f.endswith(".h"):
            shutil.copy(rosserial_esp32_dir+"/src/ros_lib/"+f, path+"/rosserial_esp32/include/")
        else:
            shutil.copy(rosserial_esp32_dir+"/src/ros_lib/"+f, path+"/rosserial_esp32/")

rosserial_client_copy_files(rospack, path+"/rosserial_esp32/include/")

# generate messages
rosserial_generate(rospack, path+"/rosserial_esp32/include/", ROS_TO_EMBEDDED_TYPES)

# Move source files to parent directory
src_files = os.listdir(path+"/rosserial_esp32/include/")
for f in src_files:
    if f.endswith(".cpp"):
        shutil.move(path+"/rosserial_esp32/include/"+f, path+"/rosserial_esp32/")
