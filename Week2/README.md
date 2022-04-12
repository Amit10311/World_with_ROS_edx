### 1. urdf_tutorial

 * Link : https://github.com/ros/urdf_tutorial/tree/master 
 * See the tutorials over at http://wiki.ros.org/urdf_tutorial 

### 2. Intrduction to URDF

```
 <link>s: robot structure
 <joint>s: connections and motion constraints
```

 1. Fixed     | rigid connection
 2. Revolute  | 1D rotation
 3. Continuous| unlimited revolute
 4. Prismatic | 1D translation
 5. Planar    | 2D translation
 6. Floating  | unlimited 6D

#### 2.1.1  Standardisation

 * ROS uses a right-handed coordinate system :

 * X+ (forward) Y+ (left) ←  Z+ (up) ↑

 * ROS uses SI units for everything:
    - Length: meters
    - Angles: radians

#### 2.1.2 Visual Robot Model with URDF
```
  $ roslaunch urdf_tutorial display.launch model:=urdf/01-myfirst.urdf

  $ roslaunch urdf_tutorial display.launch model:='$(find urdf_tutorial)/urdf/01-myfirst.urdf'
```
#### 2.1.3 Checking for Correctness
```
 * $ rosrun xacro xacro /path/to/robot_name.xacro > robot_name.urdf

 * $ check_urdf robot_name.urdf
 ```
-------------------------------------------------------------------------
### 2.2 Changing Worlds
```
 * roslaunch hrwros_support visualize_hrwros.launch 
```
