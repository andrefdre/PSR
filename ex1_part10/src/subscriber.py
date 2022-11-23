#!/usr/bin/env python3

import rospy
import sensor_msgs

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data)

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node("subscriber", anonymous=True)
    rospy.Subscriber("/left_laser/laserscan", sensor_msgs, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()