

### 3.1 Introduction to autonomous navigation
```
  rosrun rqt_robot_steering rqt_robot_steering
  - INPUT 
  /cmd_vel_mux/input/teleop
```
#### 3.1.1 Hands-on practice Part 1: Services
```
  $ roslaunch turtlebot_gazebo turtlebot_world.launch
  $ rosservice call gazebo/get_model_state '{model_name: mobile_base}'
```
```
  $ roslaunch turtlebot_rviz_launchers view_robot.launch
```
#### 3.1.2  Hands-on practice Part 2 : Nodes and Topics
```
  $ rosnode info /cmd_vel_mux
```
```
  $ roslaunch turtlebot_teleop keyboard_teleop.launch
  $ rosnode info /turtlebot_teleop_keyboard 
```
##### 3.1.2.1 Odometry
```
  $ rostopic  echo /odom -n1
  $ rostopic  echo /odom/pose -n1
```
```
  $ rosrun rqt_graph rqt_graph
```
```
  $ rostopic pub -r 10 /cmd_vel_mux/input/teleop geometry_msgs/Twist '{linear: {x: 0.1, y: 0, z: 0}, angular: {x: 0, y: 0, z: -1}}'

  $ rosmsg show geometry_msgs/Twist
```
-------------------------------------------------------------------------

### 3.2 Localization
```
  $ roslaunch turtlebot_gazebo turtlebot_world.launch
  $ rosnode list
```
```
  $ roslaunch turtlebot_gazebo gmapping_demo.launch
  $ rosnode info /slam_gmapping
```
```
  $ roslaunch turtlebot_rviz_launchers view_navigation.launch
    Set LaserScan/size(m) to 0.06         
    Set LaserScan/style to 'flat squares' 
    Set Localmap/Costmap/Topic to /map    
    Set Globalmap/Costmap/Topic to /map   
```

```
  $ roslaunch turtlebot_teleop keyboard_teleop.launch
```
```
  $ rosrun map_server map_saver -f $HOME/<choose a directory>/test_map

  $ roslaunch turtlebot_rviz_launchers view_navigation.launch
```
-------------------------------------------------------------------------

### 3.3  Path planning and obstacle avoidance
```
  $ roslaunch turtlebot_gazebo turtlebot_world.launch
```
```
  $ roslaunch turtlebot_gazebo amcl_demo.launch
 ```
 ```
  $ roslaunch turtlebot_rviz_launchers view_navigation.launch
    Add path with name Full   Path and add  /move_base/NavfnROS/plan              
    Add path with name Global Plan and add  /move_base/DWAPlannerROS/global_plan  
    Add path with name Local  Plan add add  /move_base/DWAPlannerROS/local_plan   
 ```
