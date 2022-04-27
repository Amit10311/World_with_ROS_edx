## 4. Manipulation

1. Manipulation Basic Concepts
2. Manipulation with Movelt
3. MoveIt Setup Assistant
4. MoveIt! Commander
5. Move Group interface

###  1.MoveIt! Setup Assistant
```
  $ source $HOME/hrwros_ws/devel/setup.bash
  $ roslaunch moveit_setup_assistant setup_assistant.launch
```
```
  $ HOME/hrwros_ws/src/hrwros_support/urdf/hrwros.xacro

  $ HOME/hrwros_ws/src/hrwros/hrwros_moveit_config
```
```
  $ cd src/hrwros/hrwros_moveit_config
  $ cd config
  $ cd ../launch
```
```
  $ roscd hrwros_moveit_config/
  $ more package.xml
```
-------------------------------------------------------------------------

## 4.1  MoveIt Commander

 **Launch MoveIt Commander:** 

 * Start the Gazebo simulation and verify if the robot arms and the turtlebot are correctly displayed.
```
  $ roslaunch hrwros_gazebo hrwros_environment.launch
```

 * Start the command line tool to send motion commands to the robot.
```
  $ rosrun hrwros_week4 hrwros_moveit_commander_cmdline
```

 **MoveIt commander commands** 
 ```
  $ help

  $ use <group_name>
  
  $ go <named_target>
  
  $ go <up | down | left | right | forward | backward> <distance_in_m>

  $ current

  $ load <path_to_script_file/scrip_file_name>
```
