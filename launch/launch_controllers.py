from os.path import join
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import GroupAction, DeclareLaunchArgument
from controller_manager.launch_utils import generate_load_controller_launch_description

def generate_launch_description():
    # Declaración del argumento use_sim_time
    declare_sim_time = DeclareLaunchArgument(
        'use_sim_time',
        default_value='true',
        description="use_sim_time simulation parameter"
    )

    # Definición de carpetas de los paquetes
    pkg_share_folder = get_package_share_directory('rover_description')
    arm_pkg_share_folder = get_package_share_directory('robot_moveit_config')

    # Carga del Joint State Broadcaster
    joint_state_broadcaster = GroupAction(
        actions=[
            generate_load_controller_launch_description(
                controller_name='joint_state_broadcaster',
                controller_params_file=join(pkg_share_folder, 'config', 'rover_controllers.yaml')
            )
        ]
    )

    # Carga del controlador de la base móvil (Rover)
    base_controller = GroupAction(
        actions=[
            generate_load_controller_launch_description(
                controller_name='rover_base_control',
                controller_params_file=join(pkg_share_folder, 'config', 'rover_controllers.yaml')
            )
        ]
    )

    # Carga del controlador del brazo (Scara)
    # Nota: Utiliza el archivo YAML de la carpeta moveit_config según tu captura
    arm_controller = GroupAction(
        actions=[
            generate_load_controller_launch_description(
                controller_name='scara_controller',
                controller_params_file=join(arm_pkg_share_folder, 'config', 'ros2_controllers.yaml')
            )
        ]
    )

    # Carga del controlador de la pinza (Gripper)
    gripper_controller = GroupAction(
        actions=[
            generate_load_controller_launch_description(
                controller_name='gripper_controller',
                controller_params_file=join(arm_pkg_share_folder, 'config', 'ros2_controllers.yaml')
            )
        ]
    )

    # Creación de la descripción de lanzamiento
    ld = LaunchDescription()
    
    # Añadir acciones al LaunchDescription
    ld.add_action(declare_sim_time)
    ld.add_action(joint_state_broadcaster)
    ld.add_action(base_controller)
    ld.add_action(arm_controller)
    ld.add_action(gripper_controller)

    return ld