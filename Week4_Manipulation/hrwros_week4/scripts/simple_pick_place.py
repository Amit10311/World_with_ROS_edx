#!/usr/bin/env python3

# Software License Agreement (BSD License)
#
# Author: Acorn Pooley
# Modified by: Mukunda Bharatheesha
#
# To use the python interface to move_group, import the moveit_commander
# module.  We also import rospy and some messages that we will use.
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import actionlib
import geometry_msgs


def simple_pick_place():
    # 1. First initialize moveit_commander and rospy.
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('simple_pick_place',
                    anonymous=True)

    # 2. Instantiate a MoveGroupCommander object. 
    # This object is an interface to one group of joints.  
    # In this case the group refers to the joints of robot1.
    # This interface can be used to plan and execute motions on robot1.
    robot1_group = moveit_commander.MoveGroupCommander("robot1")

    # MoveGroup Commander Object for robot2.
    # We're not using it so let's leave it commented out
    # robot2_group = moveit_commander.MoveGroupCommander("robot2")

    # 3. Action clients to the ExecuteTrajectory action server.
    robot1_client = actionlib.SimpleActionClient('execute_trajectory',
        moveit_msgs.msg.ExecuteTrajectoryAction)
    robot1_client.wait_for_server()

    ropy.loginfo('Execute Trajectory server is available for robot1')
    robot2_client = actionlib.SimpleActionClient('execute_trajectory',
        moveit_msgs.msg.ExecuteTrajectoryAction)

    robot2_client.wait_for_server()
    rospy.loginfo('Execute Trajectory server is available for robot2')

    # 4.1 Set a named joint configuration as the goal to plan for a move group.
    # Named joint configurations are the robot poses
    # defined via MoveIt! Setup Assistant.
    robot1_group.set_named_target("R1Home")

    # 4.2 Plan to the desired joint-space goal
    # using the default planner (RRTConnect).
    # Gets only the plan, and discards the other elements returned by plan()
    _, plan, _, _ = robot1_group.plan()

    # 5. Create a goal message object for the action server.
    robot1_goal = moveit_msgs.msg.ExecuteTrajectoryGoal()

    # 6.. Update the trajectory in the goal message.
    robot1_goal.trajectory = plan

    # 4.3. Send the goal to the action server.
    robot1_client.send_goal(robot1_goal)
    # robot1_client.wait_for_result()

    robot1_group.set_named_target("R1PreGrasp")

    _, plan, _, _ = robot1_group.plan()
    robot1_goal = moveit_msgs.msg.ExecuteTrajectoryGoal()
    robot1_goal.trajectory = plan

    robot1_client.send_goal(robot1_goal)
    robot1_client.wait_for_result()

    # 4.4. Cartesian Paths
    # 
    # You can plan a cartesian path directly by specifying a list of waypoints
    # for the end-effector to go through.
    waypoints = []
    # start with the current pose
    current_pose = robot1_group.get_current_pose()
    rospy.sleep(0.5)
    current_pose = robot1_group.get_current_pose()

    # 7. create linear offsets to the current pose
    new_eef_pose = geometry_msgs.msg.Pose()

    # 8. Manual offsets because we don't have a camera to detect objects yet.
    new_eef_pose.position.x = current_pose.pose.position.x + 0.10
    new_eef_pose.position.y = current_pose.pose.position.y - 0.20
    new_eef_pose.position.z = current_pose.pose.position.z - 0.20

    # 9. Retain orientation of the current pose.
    new_eef_pose.orientation = copy.deepcopy(current_pose.pose.orientation)

    waypoints.append(new_eef_pose)
    waypoints.append(current_pose.pose)

    # 10. We want the cartesian path to be interpolated at a resolution of 1 cm
    # which is why we will specify 0.01 as the eef_step in cartesian
    # translation.  

    # We will specify the jump threshold as 0.0, effectively
    # disabling it.
    fraction = 0.0
    for count_cartesian_path in range(0, 3):
        if fraction < 1.0:
            (plan_cartesian, fraction) = robot1_group.compute_cartesian_path(
                                                    waypoints,
                                                    0.01,     # eef_step
                                                    0.0)      # jump_threshold
        else:
            break

    robot1_goal = moveit_msgs.msg.ExecuteTrajectoryGoal()
    robot1_goal.trajectory = plan_cartesian

    robot1_client.send_goal(robot1_goal)
    robot1_client.wait_for_result()

    robot1_group.set_named_target("R1Place")

    _, plan, _, _ = robot1_group.plan()
    robot1_goal = moveit_msgs.msg.ExecuteTrajectoryGoal()
    robot1_goal.trajectory = plan

    robot1_client.send_goal(robot1_goal)
    robot1_client.wait_for_result()

    # 11. When finished shut down moveit_commander.
    moveit_commander.roscpp_shutdown()


if __name__ == '__main__':
    try:
        simple_pick_place()
    except rospy.ROSInterruptException:
        pass
