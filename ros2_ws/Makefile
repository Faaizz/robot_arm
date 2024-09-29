.PHONY: build

build:
	rosdep install --from-paths src -y --ignore-src
	colcon build --symlink-install
	mkdir -p install/robot_arm/share/robot_arm/description/models
	cp -R src/robot_arm/description/models/* install/robot_arm/share/robot_arm/description/models

launch: build
	ros2 launch robot_arm robot_arm.launch.yaml
