#!/usr/bin/env python3
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#

#
# Revision $Id$

# Node to publish to a string topic.

import rospy
from hrwros_week0_assignment.msg import Dummy


def sensorInfoPublisher():
    si_publisher = rospy.Publisher('dummy_topic', Dummy, queue_size=10)
    rospy.init_node('dummy_node', anonymous=False)
    rate = rospy.Rate(1)

    # Create new object to hold the name which will be published
    name = Dummy()

    # This should be changed to your own name instead of None
    # For exampe:
    # name.name = "Tim"
    name.name = "Amit"

    while not rospy.is_shutdown():
        # Publish the sensor information on the /sensor_info topic.
        si_publisher.publish(name)
        # Print log message if all went well.
        rospy.loginfo("All went well. Publishing topic ")
        rate.sleep()


if __name__ == '__main__':
    try:
        sensorInfoPublisher()
    except rospy.ROSInterruptException:
        pass
