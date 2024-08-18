from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    # Ruta al paquete slam_toolbox
    slam_toolbox_dir = get_package_share_directory('slam_toolbox')

    # Archivo de parámetros de SLAM Toolbox
    params_file = os.path.join(
        get_package_share_directory('mapping'),
        'config',
        'mapper_params_online_async.yaml'
    )

    return LaunchDescription([
        # Nodo de SLAM Toolbox
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(slam_toolbox_dir, 'launch', 'online_async_launch.py')
            ),
            launch_arguments={'params_file': params_file, 'use_sim_time': 'true'}.items()
        ),
        # Nodo de RViz
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', os.path.join(get_package_share_directory('mapping'), 'rviz', 'mapping_config.rviz')]
        )
    ])
