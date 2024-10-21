import os
import launch.actions
import launch_ros.actions
import xacro
from tempfile import NamedTemporaryFile
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
  mycobot_description = get_package_share_directory('mycobot_description')
  robot_description_file = os.path.join(
    mycobot_description, 'urdf',
    'model.urdf.xacro',
  )
  robot_description_config = xacro.process_file(robot_description_file)
  tf = NamedTemporaryFile(delete=False, delete_on_close=False) 
  tf.write(robot_description_config.toxml(encoding='utf8'))
  tf.close()
  
  gz_spawn_entity = launch_ros.actions.Node(
    package='ros_gz_sim',
    executable='create',
    parameters=[{
      'world': 'default',
      'file': tf.name,
      'x': 1.5,
      'y': 1.5,
      'z': 0.0,
    },],
  )

  return LaunchDescription([
    launch.actions.SetEnvironmentVariable('GZ_SIM_RESOURCE_PATH', PathJoinSubstitution([
      FindPackageShare('environment_gazebo'),
      'models',
    ])),
    launch.actions.IncludeLaunchDescription(
      launch_description_source=PythonLaunchDescriptionSource([
        PathJoinSubstitution([
          FindPackageShare('ros_gz_sim'),
          'launch', 'gz_sim.launch.py',
        ]),
      ]),
      launch_arguments={
        'gz_args': [
          '-r ',
          PathJoinSubstitution([
            FindPackageShare('environment_gazebo'),
            'worlds',
            'small_warehouse.world',
          ]),
        ],
        'on_exit_shutdown': 'True'
      }.items(),
    ),
    launch_ros.actions.Node(
      package='ros_gz_bridge',
      executable='parameter_bridge',
      parameters=[{
        'config_file': PathJoinSubstitution([
          FindPackageShare('environment_gazebo'),
          'config',
          'ros_gz_bridge_config.yaml',
        ]),
      }],
      output='screen'
    ),  
    gz_spawn_entity,
    launch_ros.actions.Node(
      package='robot_state_publisher',
      executable='robot_state_publisher',
      output='screen',
      parameters=[{
        'use_sim-time': 'True',
        'robot_description': robot_description_config.toxml(),
      }],
    ),
    launch_ros.actions.Node(
      package='joint_state_publisher_gui',
      executable='joint_state_publisher_gui',
      output='screen',
    ),
    launch_ros.actions.Node(
      package='rviz2',
      executable='rviz2',
      output='screen',
      arguments=[
        "-d ", 
        PathJoinSubstitution([
          FindPackageShare('mycobot_description'),
          'rviz', 'config.rviz',
        ]),
      ]
    ),
  ])

if __name__=='__main__':
  generate_launch_description()
