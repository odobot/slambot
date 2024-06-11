import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue
from launch.actions import DeclareLaunchArgument, SetEnvironmentVariable, IncludeLaunchDescription
from launch.substitutions import Command, LaunchConfiguration
from ament_index_python.packages import get_package_share_directory, get_package_prefix
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    model_arg = DeclareLaunchArgument(
        name="model",
        default_value=os.path.join(get_package_share_directory("slambot"), "urdf", "slambot.urdf.xacro"),
        description="Absolute path to the robot URDF file"
    )

    env_var = SetEnvironmentVariable("GAZEBO_MODEL_PATH", os.path.join(get_package_prefix("slambot"), "share"))

    robot_description = ParameterValue(Command(["xacro ", LaunchConfiguration("model")]))

    robot_state_publisher = Node(
        package="robot_state_publisher",  
        executable="robot_state_publisher",
        parameters=[{"robot_description":robot_description}]
    )

    start_gazebo_server = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(get_package_share_directory("gazebo_ros"), "launch", "gzserver.launch.py"))
    )

    start_gazebo_client = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(get_package_share_directory("gazebo_ros"), "launch", "gzclient.launch.py"))
    )

    spawn_robot = Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        arguments=["-entity", "slambot", "-topic", "robot_description"]
    )

    return LaunchDescription([\
        env_var,
        model_arg,
        robot_state_publisher,
        start_gazebo_server,
        start_gazebo_client,
        spawn_robot
    ])

# Second code

# import os

# from ament_index_python.packages import get_package_share_directory


# from launch import LaunchDescription
# from launch.actions import IncludeLaunchDescription
# from launch.launch_description_sources import PythonLaunchDescriptionSource

# from launch_ros.actions import Node



# def generate_launch_description():


#     # Include the robot_state_publisher launch file, provided by our own package. Force sim time to be enabled
#     # !!! MAKE SURE YOU SET THE PACKAGE NAME CORRECTLY !!!

#     package_name='slambot' #<--- CHANGE ME

#     rsp = IncludeLaunchDescription(
#                 PythonLaunchDescriptionSource([os.path.join(
#                     get_package_share_directory(package_name),'launch','robot_description.launch.py'
#                 )]), launch_arguments={'use_sim_time': 'true'}.items()
#     )

#     # Include the Gazebo launch file, provided by the gazebo_ros package
#     gazebo = IncludeLaunchDescription(
#                 PythonLaunchDescriptionSource([os.path.join(
#                     get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')]),
#              )

#     # Run the spawner node from the gazebo_ros package. The entity name doesn't really matter if you only have a single robot.
#     spawn_entity = Node(package='gazebo_ros', 
#                         executable='spawn_entity.py',
#                         arguments=['-topic', 'robot_description',
#                                    '-entity', 'slambot'],
#                         output='screen')



#     # Launch them all!
#     return LaunchDescription([
#         rsp,
#         gazebo,
#         spawn_entity,
#     ])


# The third code

# import os

# from ament_index_python.packages import get_package_share_directory

# from launch import LaunchDescription
# from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument, SetEnvironmentVariable
# from launch.launch_description_sources import PythonLaunchDescriptionSource
# from launch_ros.actions import Node
# from launch.substitutions import Command, LaunchConfiguration

# def generate_launch_description():
#     # Package and file paths
#     package_name = 'slambot'
#     urdf_file = 'slambot.urdf.xacro'
#     urdf_path = os.path.join(get_package_share_directory(package_name), 'urdf', urdf_file)
#     gazebo_ros_pkg = 'gazebo_ros'
#     gzserver_launch = 'gzserver.launch.py'
#     gzclient_launch = 'gzclient.launch.py'
    
#     # Declare the launch arguments
#     model_arg = DeclareLaunchArgument(
#         name='model',
#         default_value=urdf_path,
#         description='Absolute path to the robot URDF file'
#     )
    
#     # Set environment variable for Gazebo model path
#     env_var = SetEnvironmentVariable(
#         name='GAZEBO_MODEL_PATH',
#         value=os.path.join(get_package_share_directory(package_name), 'share')
#     )
    
#     # Robot description parameter
#     robot_description = Command(['xacro ', LaunchConfiguration('model')])
    
#     # Robot state publisher node
#     robot_state_publisher = Node(
#         package='robot_state_publisher',
#         executable='robot_state_publisher',
#         parameters=[{'robot_description': robot_description}],
#         output='screen'
#     )
    
#     # Include Gazebo server and client launch files
#     start_gazebo_server = IncludeLaunchDescription(
#         PythonLaunchDescriptionSource(
#             os.path.join(get_package_share_directory(gazebo_ros_pkg), 'launch', gzserver_launch)
#         )
#     )
    
#     start_gazebo_client = IncludeLaunchDescription(
#         PythonLaunchDescriptionSource(
#             os.path.join(get_package_share_directory(gazebo_ros_pkg), 'launch', gzclient_launch)
#         )
#     )
    
#     # Spawn robot entity in Gazebo
#     spawn_robot = Node(
#         package='gazebo_ros',
#         executable='spawn_entity.py',
#         arguments=['-entity', 'slambot', '-topic', 'robot_description'],
#         output='screen'
#     )
    
#     return LaunchDescription([
#         env_var,
#         model_arg,
#         robot_state_publisher,
#         start_gazebo_server,
#         start_gazebo_client,
#         spawn_robot
#     ])

# if __name__ == '__main__':
#     generate_launch_description()
