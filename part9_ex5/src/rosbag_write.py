#!/usr/bin/env python3

import rospy
from part9_ex5.msg import Dog
import rosbag
from std_msgs.msg import Int32, String

bag = rosbag.Bag('test.bag', 'w')


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data)
    bag.write('topic',data)

def listener():

    try:
        # In ROS, nodes are uniquely named. If two nodes with the same
        # name are launched, the previous one is kicked off. The
        # anonymous=True flag means that rospy will choose a unique
        # name for our 'listener' node so that multiple listeners can
        # run simultaneously.
        rospy.init_node("subscriber", anonymous=True)
        topic_name=rospy.get_param("~topic_name")
        rospy.Subscriber(topic_name, Dog, callback)

        # spin() simply keeps python from exiting until this node is stopped
        rospy.spin()
    finally:
        bag.close()