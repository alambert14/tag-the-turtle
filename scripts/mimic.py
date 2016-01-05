#!/usr/bin/env python
import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import

def mimic():
	rospy.init_node('mimic', anonymous=True)
	twist_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
	pose_sub = rospy.Subscriber('pose', Pose, pose_callback)

def pose_callback(turtlesim.pose()):
	twist = Twist()
	twist.angular.z = pose.angular_velocity
	twist.angular.x = pose.linear_velocity
	twist_pub.publish(twist)

if __name__ == '__main__':
	mimic()
	ros.spin()
		
	
