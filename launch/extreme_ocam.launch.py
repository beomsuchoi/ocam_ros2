from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    
    return LaunchDescription([
        # Front camera (ocam_ros2)
        Node(
            package='ocam_ros2',
            executable='ocam_ros2',
            name='ocam_front_node',
            parameters=[
                {'device_name': '/dev/ocam_front'},
                {'frame_id': 'ocam_front_frame'},
                {'resolution': 2},
                {'frame_rate': 30.0},
                {'exposure': 100},
                {'gain': 50},
                {'wb_blue': 200},
                {'wb_red': 160},
                {'auto_exposure': True},
                {'show_image': True}
            ],
            remappings=[
                ('/image_raw', '/ocam_front/image_raw'),
                ('/camera_info', '/ocam_front/camera_info')
            ]
        ),
        
        # Backup camera (ocam_ros2)
        Node(
            package='ocam_ros2',
            executable='ocam_ros2', 
            name='ocam_backup_node',
            parameters=[
                {'device_name': '/dev/ocam_backup'},
                {'frame_id': 'ocam_backup_frame'},
                {'resolution': 2},
                {'frame_rate': 30.0},
                {'exposure': 100},
                {'gain': 50},
                {'wb_blue': 200},
                {'wb_red': 160},
                {'auto_exposure': True},
                {'show_image': True}
            ],
            remappings=[
                ('/image_raw', '/ocam_backup/image_raw'),
                ('/camera_info', '/ocam_backup/camera_info')
            ]
        )
    ])