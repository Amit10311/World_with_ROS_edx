#!/usr/bin/env python3

# This code has been adapted from the ROS Wiki ROS Service tutorials to the context
# of this course.
# (http://wiki.ros.org/ROS/Tutorials/WritingServiceClient%28python%29)

from hrwros_msgs.srv import ConvertMetresToFeet, ConvertMetresToFeetRequest, ConvertMetresToFeetResponse

import rospy
import numpy as np

_CONVERSION_FACTOR_METRES_TO_FEET = 3.28  # Metres -> Feet conversion factor.


# Service callback function.
def process_service_request(req):

    # 1. Instantiate the response message object.
    res = ConvertMetresToFeetResponse()

    # 2. Perform sanity check. Allow only positive real numbers.
    # Compose the response message accordingly.
    if(req.distance_metres < 0):
        res.success = False
        res.distance_feet = -np.Inf  # Default error value.
    else:
        res.distance_feet = _CONVERSION_FACTOR_METRES_TO_FEET * req.distance_metres
        res.success = True
    
    # Add a delaying test 5 sec loop. (extra )
    for test_idx in range(0,5):
        rospy.sleep(1)

    # 3. Return the response message.
    return res


def metres_to_feet_server():
    # 1. ROS node for the service server.
    rospy.init_node('metres_to_feet_server', anonymous=False)

    # 2. Create a ROS service type.
    service = rospy.Service('metres_to_feet', ConvertMetresToFeet, process_service_request)

    # 3. Log message about service availability.
    rospy.loginfo('Convert metres to feet service is now available.')
    rospy.spin()


if __name__ == "__main__":
    metres_to_feet_server()
