import os
from glob import glob

from setuptools import setup

package_name = 'robot_arm'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        # ('share/ament_index/resource_index/packages',
            # ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.*')),
        (os.path.join('share', package_name, 'description', 'worlds'), glob('description/worlds/*.world')),
        (os.path.join('share', package_name, 'config'), glob('config/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='faaizz',
    maintainer_email='fr33ziey@gmail.com',
    description='7-DOF Robot Arm Simulation',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
          'my_node = robot_arm.node:main',
        ],
    },
)
