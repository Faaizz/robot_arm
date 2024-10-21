.PHONY: build

build:
	rosdep install --from-paths src -y --ignore-src
	colcon build

SHELL:=/bin/bash
launch/kuka: build
	source install/local_setup.bash && \
	ros2 launch environment_gazebo kuka_lwr_4_plus.launch.py
launch/mycobot: build
	source install/local_setup.bash && \
	ros2 launch environment_gazebo mycobot.launch.py
visualize: build
visualize/kuka: visualize
	source install/local_setup.bash && \
	ros2 launch environment_gazebo visualize_model.launch.yaml
visualize/mycobot: visualize
	source install/local_setup.bash && \
	ros2 launch environment_gazebo visualize_model.launch.yaml pkg:=mycobot_description

all: build launch
