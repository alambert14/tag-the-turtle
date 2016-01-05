#!/usr/bin/env python

import turtlesim.srv
import rospy
#import roslib; roslib.load_manifest('turtle_tag')

#def spawn(req):
	
#	print "Spawning a turtle"

def spawn_turtle():
	rospy.wait_for_service('spawn')
	spawner = rospy.ServiceProxy('spawn', turtlesim.srv.Spawn)
	try:
		spawner(10,10,10, "turt")
	except rospy.ServiceException as exc:
		print("Serivce did not process request: " + str(exc))
#	rospy.spin()

if __name__ == "__main__":
	rospy.init_node('spawn')
	spawn_turtle()
