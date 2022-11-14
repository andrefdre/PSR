#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from part9_ex5.msg import Dog

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data)

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node("subscrber", anonymous=True)
    topic_name=rospy.get_param("~topic_name")
    rospy.Subscriber(topic_name, Dog, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()