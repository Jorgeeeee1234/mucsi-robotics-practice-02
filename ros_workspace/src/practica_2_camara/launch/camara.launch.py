"""Launch the USB camera driver with a configurable video device."""

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description() -> LaunchDescription:
    """Start usb_cam and publish its images in the camera namespace."""
    video_device = LaunchConfiguration('video_device')

    return LaunchDescription([
        DeclareLaunchArgument(
            'video_device',
            default_value='/dev/video0',
            description='Camera device visible inside the container.',
        ),
        Node(
            package='usb_cam',
            executable='usb_cam_node_exe',
            name='usb_cam',
            namespace='camera',
            parameters=[{'video_device': video_device}],
            output='screen',
        ),
    ])
