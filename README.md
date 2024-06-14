# SLAMBOT
## Installation
The package was made using [ROS2 Humble](https://docs.ros.org/en/humble/index.html)
## Dependencies
You need to have installed:
<br>
1. ros-xacro:
   ```console
   sudo apt install ros-<ros2-distro>-xacro
   ```
2. ros-joint-state-publisher:
   ```console
   sudo apt install ros-<ros2-distro>-joint-state-publisher-gui
   ```
3. gazebo-ros:
   ```console
   sudo apt install ros-<ros2-distro>-gazebo-ros-pkgs
   ```
4. ros2-control and ros2-controllers:
   ```console
   sudo apt install ros-<ros2-distro>-ros2-control ros-<ros2-distro>-ros2-controllers
   ```
4. colcon:
   ```console
   sudo apt install python3-colcon-common-extensions
   ```
## :hammer: Design
The design was made in fusion360 and used a [fusion2urdf](https://github.com/SpaceMaster85/fusion2urdf) exporter to obtain the urdf files needed 
## :hammer: How to build
To build the packages in this repository follow these steps:
1. `cd` into an existing or create a new [workspace](https://docs.ros.org/en/foxy/Tutorials/Beginner-Client-Libraries/Creating-A-Workspace/Creating-A-Workspace.html)
   ```console
   mkdir -p slambot/src
   ```
2. clone this repository in the `src` folder of your workspace
   ```console
   cd slambot/src
   ```
   ```console
   git clone https://github.com/odobot/slambot.git
   ```
3. Naviage back to the workspace folder
   ```console
   cd ../
   ```
4. build the workspace using the [colcon](https://colcon.readthedocs.io/en/released/reference/verb/build.html) build tool
   ```console
   colcon build --symlink-install
   ```
5. source the `setup.bash` file
   ```console
   source install/setup.bash
   ```
6. You can add the `setup.bash` file on the bashrc script file, just open the file and add it at end:
    ```console
    gedit ~/.bashrc
    ```
    ```console
    source ~/slambot/install/setup.bash
    ```
## :movie_camera: Rviz
To view the urdf in rviz open 3 terminals:
<br>
On the first terminal (needs to the terminal you sourced your setup.bash file in) type: 
```console
  ros2 launch slambot robot_description.launch.py
  ```
Second terminal
 ```console
  rviz2
  ```
In rviz for the Fixed frame use `base_link` add RobotModel at the Displays under the robot model there is Description topic add `/robot_description`.

Third terminal
 ```console
  ros2 run joint_state_publisher_gui joint_state_publisher_gui
 ```

## 🎥 Gazebo
To launch your robot arm in gazebo, run:
 ```console
  ros2 launch slambot gazebo.launch.py
  ```
