import os
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, SetEnvironmentVariable
from launch.substitutions import Command, FindExecutable, LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
import launch_ros.descriptions

def generate_launch_description():
    # 1. Rutas de los dos paquetes involucrados
    rover_share = get_package_share_directory('rover_description')
    world_share = get_package_share_directory('urjc_excavation_world')

    # 2. DEFINICIÓN DE MÚLTIPLES RUTAS DE ENTORNO
    # Unimos las rutas de ambos paquetes separadas por ':' para que Gazebo encuentre todo
    resource_paths = [
        os.path.join(rover_share, '..'), 
        os.path.join(world_share, 'models')
    ]
    # Convertimos la lista en un string: "/ruta/a/rover:ruta/a/world"
    combined_resource_path = ":".join(resource_paths)

    # 3. Procesamiento del Robot (Xacro)
    robot_description_content = Command([
            PathJoinSubstitution([FindExecutable(name="xacro")]),
            " ",
            os.path.join(rover_share, 'robots', 'robot.urdf.xacro'),
    ])

    # 4. Configuración del Mundo
    world_file_path = os.path.join(world_share, 'worlds', 'urjc_excavation_msr.world')

    # Acciones y Nodos
    set_env = SetEnvironmentVariable('GZ_SIM_RESOURCE_PATH', combined_resource_path)
    
    gazebo_cmd = ExecuteProcess(
        cmd=['gz', 'sim', '-r', '-v4', world_file_path],
        output='screen'
    )

    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        parameters=[{
          'use_sim_time': True,
          'robot_description': launch_ros.descriptions.ParameterValue(robot_description_content, value_type=str),
        }],
    )

    spawn_robot_node = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=[
            '-name', 'my_rover',
            '-topic', 'robot_description',
            '-x', '0.0', '-y', '0.0', '-z', '0.5'
        ],
        output='screen',
    )

    joint_state_publisher_gui_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui'
    )

    joint_state_bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=[
            # Mapeamos el tópico de estados de articulaciones de ROS a Gazebo
            '/joint_states@sensor_msgs/msg/JointState[gz.msgs.Model',
        ],
        output='screen'
    )

    return LaunchDescription([
        set_env,
        gazebo_cmd,
        robot_state_publisher_node,
        spawn_robot_node,
        joint_state_publisher_gui_node,
        joint_state_bridge
    ])


