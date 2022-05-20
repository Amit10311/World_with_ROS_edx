#!/usr/bin/env python3

# Software License Agreement (BSD License)
#
# Author: Mukunda Bharatheesha
##
import rospy
import tf2_ros

# String list for robot conversation
_robot1_strings = ['Turtlebot is at: ', 'Yes, I am sure. Turtlebot is at: ', 'Now, Robot2, get on with it. Turtlebot IS AT: ']
_robot2_strings = ['Are you sure? Turtlebot is actually at: ', 'You got to be kidding me!! I can guarantee that the Turtlebot is at: ', 'You hold back right there Robot1! Turtlebot is not where you say it is! Turtlebot is at: ']

# The robot_squabblers() function reporting live about the dispute between robot arms.
def robot_squabblers():
    # Initialize ROS node.
    rospy.init_node('robot_squabblers', anonymous = True)

    # Define TF buffer and associate it to a TF listener.
    tfBuffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tfBuffer)

    # Helper variables.
    rate_pub = rospy.Rate(0.5)
    rate_listener = rospy.Rate(10)
    string_idx = 0

    # Continuously display the transform between the base links of the two robots and the turtlebot.
    while not rospy.is_shutdown():
        # This try-except block makes sure any errors we might run into due to non-availability of TF frames
        # is correctly handled via exception handling.
        try:
            # Lookup translation information between robot1_base_link and turtlebot base_link.
            trans_r1 = tfBuffer.lookup_transform('robot1_base_link', 'base_link', rospy.Time())
            # Update and print string for Robot1.
            robot1_words = 'Robot1:' + _robot1_strings[string_idx]
            print ('%s (x=%4.2f, y=%4.2f).'%(robot1_words, trans_r1.transform.translation.x, trans_r1.transform.translation.y))

            # Lookup translation information between robot2_base_link and turtlebot base_link.
            trans_r2 = tfBuffer.lookup_transform('robot2_base_link', 'base_link', rospy.Time())

            # Update and print string for Robot1.
            robot2_words = 'Robot2:' + _robot2_strings[string_idx]
            print ('%s (x=%4.2f, y=%4.2f).'%(robot2_words, trans_r2.transform.translation.x, trans_r2.transform.translation.y))
            print ('-------------------')
            # Delay for transform
            string_idx +=1
            if(string_idx == 3):
                string_idx = 0
            rate_pub.sleep()
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            
            # In case the requested TF is not available, try again after a short duration.
            rate_listener.sleep()
            continue

if __name__ == '__main__':
    try:
        # Call the robot_squabblers() function.
        robot_squabblers()
    except rospy.ROSInterruptException:
        pass
