#! /usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2018, Delft University of Technology
# TU Delft Robotics Institute.
# All rights reserved.
#
#
# Authors: the HRWROS mooc instructors

# Assignment 2 for Week1: In this assignment you will subscribe to the topic that
# publishes information on the box height in metres and use the metres_to_feet
# service to convert this height in metres to height in feet.

import sys
import rospy
from hrwros_week1_assignment.msg import BoxHeightInformation

from hrwros_msgs.srv import ConvertMetresToFeet
from hrwros_msgs.srv import ConvertMetresToFeetRequest
from hrwros_msgs.srv import ConvertMetresToFeetResponse


def box_height_info_callback(data):
    try:
        # Create a proxy for the service to convert metres to feet - Part2.
        # metres_to_feet = rospy.ServiceProxy(<update the correct details here>)
        metres_to_feet = rospy.ServiceProxy('metres_to_feet', ConvertMetresToFeet)

        # Call the service here.
        # service_response = <write-your-code-here-Part2>
        service_response = metres_to_feet(data.box_height)

        # Write a log message here to print the height of this box in feet.
        # <write-your-code-here-Part2>
        rospy.loginfo("Box height of %0.3f m = %4.2f feet"%(data.box_height, service_response.distance_feet))
        rospy.loginfo("Conversion successful!")

    except rospy.ServiceException as e:

        print("Service call failed: %s" % e)


if __name__ == '__main__':
    # Initialize the ROS node here.
    rospy.init_node('box_height_in_feet', anonymous=False)

    # First wait for the service to become available - Part2.
    rospy.loginfo("Waiting for service...")
    rospy.wait_for_service('metres_to_feet')
    rospy.loginfo("Service %s is now available", 'metres_to_feet')

    # Create a subscriber to the box height topic - Part1.
    rospy.Subscriber('box_height_info', BoxHeightInformation,box_height_info_callback)

    # Prevent this ROS node from terminating until Ctrl+C is pressed.
    rospy.spin()
