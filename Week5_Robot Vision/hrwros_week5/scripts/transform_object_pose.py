#!/usr/bin/env python3

# Software License Agreement (BSD License)
##
import rospy
from hrwros_gazebo.msg import LogicalCameraImage

import tf2_ros
import tf2_geometry_msgs

import geometry_msgs

def logical_camera_callback(data):
  # Check if the logical camera has seen our box which has the name 'object'.
  if (data.models[-1].type == 'object'):
    # Create a pose stamped message type from the camera image topic.
    object_pose = geometry_msgs.msg.PoseStamped()
    object_pose.header.stamp = rospy.Time.now()
    object_pose.header.frame_id = "logical_camera_frame"
    object_pose.pose.position.x = data.models[-1].pose.position.x
    object_pose.pose.position.y = data.models[-1].pose.position.y
    object_pose.pose.position.z = data.models[-1].pose.position.z
    object_pose.pose.orientation.x = data.models[-1].pose.orientation.x
    object_pose.pose.orientation.y = data.models[-1].pose.orientation.y
    object_pose.pose.orientation.z = data.models[-1].pose.orientation.z
    object_pose.pose.orientation.w = data.models[-1].pose.orientation.w
    while True:
      try:
        object_world_pose = tf_buffer.transform(object_pose, "world")
        break
      except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
        continue
    rospy.loginfo('Pose of the object in the world reference frame is:\n %s', object_world_pose)
    rospy.loginfo('Pose of the object in the logical camera reference frame is:\n %s', object_pose)
    rospy.signal_shutdown('Successfully transformed pose.')
  else:
    # Do nothing.
    print('')

if __name__== '__main__':  # Initialize ROS node to transform object pose.
  rospy.init_node('transform_object_pose',
                    anonymous=True)
  
  # Declate a TF buffer globally.
  tf_buffer = tf2_ros.Buffer()
  tf_listener = tf2_ros.TransformListener(tf_buffer)
  
  # Subscribe to the logical camera topic.
  rospy.Subscriber('hrwros/logical_camera', LogicalCameraImage, logical_camera_callback)

  rospy.spin()
