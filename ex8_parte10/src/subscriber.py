#!/usr/bin/env python3

import rospy
from sensor_msgs import point_cloud2
from sensor_msgs.msg import LaserScan, PointCloud2,PointField
from std_msgs.msg import Header
from functools import partial
import math

def callback(msg,publisher):
    rospy.loginfo("I received a new laser scan msg")

    # inspiration from https://gist.github.com/lucasw/ea04dcd65bc944daea07612314d114bb
    # sensor_msgs.msg PointCloud2 is the actual serialized message, but to manipulate we use the sensor_msgs
    # point_cloud2 data structure.
    header = Header(seq=msg.header.seq, stamp=msg.header.stamp, frame_id=msg.header.frame_id)
    fields = [PointField('x', 0, PointField.FLOAT32, 1),
              PointField('y', 4, PointField.FLOAT32, 1),
              PointField('z', 8, PointField.FLOAT32, 1)]

    #Clustering
    clusters
    for idx in range(1, len(msg.ranges)):
        r_indx=msg.ranges[idx]
        r_idx_prev=msg.ranges[idx-1]
        theta = msg.angle_min + idx * msg.angle_increment

        x = r * math.cos(alpha)
        y = r * math.sin(alpha)
        z = 0
        points.append([x,y,z])


    # Create a list of xyz coords
    points = []
    for idx in range(0, len(msg.ranges)):
        alpha = msg.angle_min + idx * msg.angle_increment
        r = msg.ranges[idx]

        x = r * math.cos(alpha)
        y = r * math.sin(alpha)
        z = 0
        points.append([x,y,z])

    pc2 = point_cloud2.create_cloud(header, fields, points)  # create point_cloud2 data structure

    publisher.publish(pc2)


    # pub.publish(pc2)
    # rate.sleep()

def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node("LaserScan_2_PointCloud2", anonymous=True)
    pub = rospy.Publisher('chatter', PointCloud2, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    rospy.Subscriber("/left_laser/laserscan", LaserScan, partial(callback,publisher=pub))
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()