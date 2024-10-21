.PHONY: build

build:
	rosdep install --from-paths src -y --ignore-src
	colcon build

launch: SHELL:=/bin/bash
launch:
	source install/local_setup.bash && \
	ros2 launch environment_gazebo kuka_lwr_4_plus.launch.py

all: build launch
