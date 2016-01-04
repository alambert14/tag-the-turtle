#~/usr/bin/env python

from turtlesim/spawn.srv import *
import rospy

#def spawn(req):
	
#	print "Spawning a turtle"

def spawn_server():
#	rospy.init_node('spawn_server')
#	s = rospy.Service('spawn_turtle', Spawn, spawn)
	spawn = rospy.SerivceProxy('spawn_turtle', Spawn)
	spawn(50,50,10,"turt")
	rospy.spin()

if __name__ == "__main__":
	spawn_server()
