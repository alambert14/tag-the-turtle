#!/usr/bin/env python
import rospy
from turtlesim.msg import Pose

class evader():
	pub = rospy.Publisher('cmd_vel', Pose, queue_size=10)
	rospy.init_node('evader', anonymous=True)
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		position = Pose(Pose.x, Pose.y, Pose.theta, Pose.linear_velocity, Pose.angular_velocity)
		pub.publish(position)

	
