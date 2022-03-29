#!/usr/bin/env python3
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
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
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#

#
# Revision $Id$

# Node to subscribe to a Sensor Information topic.

import rospy
from hrwros_msgs.msg import SensorInformation


# Topic callback function.
def sensorInfoCallback(data):
    rospy.loginfo(' Distance reading from the sensor is : %f', data.sensor_data.range)


def sensorInfoListener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'sensorInfoListener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('sensor_info_subscriber', anonymous=False)

    rospy.Subscriber('sensor_info', SensorInformation, sensorInfoCallback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    sensorInfoListener()
