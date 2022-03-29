#!/usr/bin/env python3

# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.

#
# Revision $Id$

# Node to publish to a string topic.

import rospy
from std_msgs.msg import String


def simplePublisher():
    simple_publisher = rospy.Publisher('topic_1', String, queue_size=10)
    rospy.init_node('node_1', anonymous=False)
    rate = rospy.Rate(1)

    # The string to be published on the topic
    topic1_content = "Welcome to Hello (Real) World with ROS!!!"

    while not rospy.is_shutdown():
        simple_publisher.publish(topic1_content)
        rate.sleep()


if __name__ == '__main__':
    try:
        simplePublisher()
    except rospy.ROSInterruptException:
        pass
