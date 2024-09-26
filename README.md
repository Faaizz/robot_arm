# robot_arm
Integrated planning and control of a robot arm in an industrial scenario

## Plan
1. Configure ROS2 project that spawns a Gazebo world with a robot arm in an industrial environment
2. Implement basic controls for the robot arm through the keyboard
3. Mount a camera at the tip of the robot arm and save minute-wise images to file through ROS2
4. Introduce multiple orange balls into the Gazebo world at significant distances apart
5. Determine if at least one orange ball is in the robot's field of view through online image processing & object recognition
6. Mount a LiDAR camera at the tip of the robot arm
7. Plan a trajectory to the location of the ball from the tip of the robot arm
8. Touch the ball with the tip of the robot arm

## References
- https://www.ce.cit.tum.de/ics/research/platforms/kuka-lwr-4/
- https://www.dlr.de/en/rm/research/robotic-systems/arms/lwr-iii/history-of-the-dlr-lwr
