
# 1. Fundamental ROS concepts 

### 1.1 ROS File system
```
   mkdir -p new_ros_ws/src 
   $ cd new_ros_ws 
   new_ros_ws $ source /opt/ros/noetic/setup.bash 
```
### 1.2 Build Pkg 
```
  $ catkin init
  $ catkin build
```
### 1.3 Directory Vists 
 ```
  $ tree -L 1 
  src $ tree -L 2 -d 
```
------------------------------------------------------------

### 1.4 Custom message types 
```
  $ rosmsg show sensor_msgs/ TAB
  $ rosmsg show sensor_msgs/Range 
  $ rosmsg show sensor_msgs/Range -r

  $ rosmsg show hrwros_msgs/SensorInformation 
```
### 1.5 To create a new ROS package, we will use catkin:
```
  $ cd <path_to_ros_ws>/src
  $ catkin_create_pkg hrwros_week2 std_msgs
```
### 1.6  ROS Nodes 
```
  rosnode list
```
### 1.7 ROS TF frame tree
```
  rosrun rqt_tf_tree rqt_tf_tree
```
------------------------------------------------------------

## 2. Publisher node
```
  $ rosrun hrwros_week1 sensor_info_publisher.py
  $ rosrun pkg_name file_name
```
## 3. Subscriber node
```
  $ rostopic info /sensor_info
  $ rospack list
```
-----------------------------------------------------------

## 4. Service  node
```
  $ rosservice list 
  $ rosservice call <service_name> <arguments_req>
 ```
 
 ```
 float64 distance_metres      # Request message 
  ---                         # Demarcation 
 float64 distance_feet       # Response message 
```
### 4.1  Custom Service  
```
  $ rossrv show hrwros_msgs/ConvertMetresToFeet
  $ rossrv show hrwros_msgs/ConvertMetresToFeet -r
```
### 4.2 Services launch
```
  $ source $HOME/hrwros_ws/devel/setup.bash

  $ rosrun hrwros_week1 metres_to_feet_server.py
  $ rosrun hrwros_week1 metres_to_feet_client.py
 ```
-----------------------------------------------------------

### 5.  Action Node  
```
  $ rosmsg show pkg_msgs/CounterWithDelayAction

  $ rosrun actionlib_msgs genaction.py -o msg action/CounterWithDelay.action
```

### 5.1 Action launch 
```
  $ rosrun hrwros_week1 counter_with_delay_as.py
  $ rosrun hrwros_week1 counter_with_delay_ac.py

  $ rostopic echo /counter_with_delay/feedback
```
## Assisgnment 3 
```
  $ roslaunch hrwros_week1_assignment hrwros_week1_assignment3.launch
  $ rqt_plot /counter_with_delay/feedback/feedback/counts_elapsed
  $ rosrun hrwros_week1 counter_with_delay_ac.py
```

