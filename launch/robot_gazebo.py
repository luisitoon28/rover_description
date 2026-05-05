import os
from os import environ, pathsep
from os.path import join
from ament_index_python.packages import get_package_share_directory, get_package_prefix
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, SetEnvironmentVariable, IncludeLaunchDescription, OpaqueFunction
from launch.substitutions import PathJoinSubstitution, LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

def start_gzserver(context, *args, **kwargs):
    pkg_path = get_package_share_directory('urjc_excavation_world')
    world_name = LaunchConfiguration('world_name').perform(context)
    world = join(pkg_path, 'worlds', world_name + '.world')

    start_gazebo_server_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            join(get_package_share_directory('ros_gz_sim'), 'launch', 'gz_sim.launch.py')
        ),
        launch_arguments={'gz_args': ['-r -s -v 4 ', world]}.items()
    )

    start_gazebo_client_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            join(get_package_share_directory('ros_gz_sim'), 'launch', 'gz_sim.launch.py')
        ),
        launch_arguments={'gz_args': ['-g ']}.items()
    )

    return [start_gazebo_server_cmd, start_gazebo_client_cmd]

def get_model_paths(packages_names):
    model_paths = ""
    for package_name in packages_names:
        if model_paths != "":
            model_paths += pathsep
        package_path = get_package_prefix(package_name)
        model_paths += join(package_path, "share")
    if 'GZ_SIM_RESOURCE_PATH' in environ:
        model_paths += pathsep + environ['GZ_SIM_RESOURCE_PATH']
    return model_paths

def generate_launch_description():
    declare_world_name = DeclareLaunchArgument(
        'world_name', default_value='urjc_excavation_msr',
        description='Nombre del archivo .world'
    )

    # RSP desde robot_moveit_config
    robot_description_launcher = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            join(get_package_share_directory('robot_moveit_config'), 'launch', 'rsp.launch.py')
        )
    )

    # Bridge de parámetros (Telemetría, TFs, Reloj)
    bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        name='bridge_ros_gz',
        parameters=[{
            'config_file': join(get_package_share_directory('rover_description'), 'config', 'rover_bridge.yaml'),
            'use_sim_time': True
        }],
        output='screen'
    )

    # Image Bridge para las cámaras (Sintaxis corregida para Jazzy)
    gz_image_bridge_node = Node(
        package='ros_gz_image',
        executable='image_bridge',
        arguments=[
            '/front/image',
            '/gripper/image',
        ],
        remappings=[
            ('/front/image', '/front_camera/image'),
            ('/gripper/image', '/arm_camera/image'),
        ],
        output='screen',
        parameters=[{'use_sim_time': True}]
    )

    gazebo_spawn_robot = Node(
        package='ros_gz_sim',
        executable='create',
        output='screen',
        arguments=['-model', 'rover', '-topic', 'robot_description', '-use_sim_time', 'True']
    )

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        arguments=['-d', join(get_package_share_directory('rover_description'), 'rviz.rviz')],
        parameters=[{'use_sim_time': True}]
    )

    twist_stamped = Node(
        package='twist_stamper',
        executable='twist_stamper',
        parameters=[{'use_sim_time': True}],
        remappings=[('/cmd_vel_out', '/rover_base_control/cmd_vel'), ('/cmd_vel_in', '/cmd_vel')]
    )

    model_path = get_model_paths(['rover_description', 'urjc_excavation_world'])

    return LaunchDescription([
        SetEnvironmentVariable('GZ_SIM_RESOURCE_PATH', model_path),
        SetEnvironmentVariable('GZ_SIM_MODEL_PATH', model_path),
        declare_world_name,
        robot_description_launcher,
        bridge,
        gz_image_bridge_node,
        OpaqueFunction(function=start_gzserver),
        rviz_node,
        gazebo_spawn_robot,
        twist_stamped
    ])