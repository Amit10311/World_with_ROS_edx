## World_with_ROS_edx
Hello (Real) World with ROS – Robot Operating System from Edx

## **Course outline**

The course is made up of 7 weeks:

* **Week 0: Getting Started with Robotic Operating Systems (ROS)** 
  * General course introduction and information on all that you will need to complete this course, including a step by step installation guide for the required (free) software and an ungraded test assignment. 

* **Week 1: ROS Essentials.**
  *  Introduction to ROS Topics, Services, Actions and Nodes. Simple interaction with the course simulation environment.

* **Week 2: Build your own robot environment.**
  * Software representation of a Robot using Unified Robot Description Format (URDF), ROS parameter server and adding real-world object representations to the simulation environment.

* **Week 3: Autonomous Navigation**
  * Map creation with GMapping package, autonomously navigate a known map with ROS navigation.

* **Week 4: Manipulation**
  *  Motion planning, pick and place behaviors using industrial robots with ROS MoveIt!

* **Week 5: Robot Vision**
  *  Object detection, pose estimation.

* **Week 6: Final Project**
  * ROS file system, basic concepts of behavior design with state machines, build a production line application with two industrial robot arms and a mobile robot.
  
* Step 4.2: Type hrwros
   
```
 source /opt/ros/noetic/setup.bash
 cd  $HOME/hrwros_ws/hrwros_ws

 catkin build

 source $HOME/hrwros_ws/devel/setup.bash
 ```
 
 * Week 1 
 ```
 roslaunch hrwros_week1 hrwros_welcome.launch
 ```
