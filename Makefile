SHELL=/bin/bash
BASE_PATH=$(PWD)/gazebo
world:
	export GZ_SIM_RESOURCE_PATH=$(BASE_PATH)/models
	gz sim $(BASE_PATH)/worlds/small_warehouse.world

robot:
	gz service -s /world/default/create --reqtype gz.msgs.EntityFactory --reptype gz.msgs.Boolean --timeout 1000 --req 'sdf_filename: "$(BASE_PATH)/models/kuka-lwr-4plus/model.urdf", name: "kuka-lwr-4plus"'

# ROS
rqt:
	rqt

turtlesim:
	ros2 run turtlesim turtlesim_node
turtlesimcontrol:
	ros2 run turtlesim turtle_teleop_key
