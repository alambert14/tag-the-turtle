#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from turtlesim.msg import Pose

def callback(data):
	
def chaser():
	rospy.init_node('listener', anonymous=true)
	rospy.Subscriber('cmd_vel', Pose, callback)
	rospy.spin()

	
