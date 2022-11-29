#!/usr/bin/env python3

import math
import rospy
from visualization_msgs.msg import Marker,MarkerArray


def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node("rviz_publisher", anonymous=False)
    pub = rospy.Publisher('~markers', MarkerArray, queue_size=10)
    rate = rospy.Rate(1) # 10hz
    theta=0
    alpha=0

    while not rospy.is_shutdown():
        marker_array=MarkerArray()

        marker=Marker()
        marker.header.frame_id='world'
        marker.ns='my_drawings'
        marker.id=0
        marker.type=Marker.SPHERE
        marker.action=Marker.MODIFY

        marker.pose.position.x=0
        marker.pose.position.y=0
        marker.pose.position.z=0

        theta+=0.1
        if theta>=1:
            theta=0
        marker.pose.orientation.x=theta 
        marker.pose.orientation.y=0
        marker.pose.orientation.z=0

        marker.scale.x=1
        marker.scale.y=1
        marker.scale.z=3

        marker.color.r=0
        marker.color.g=1
        marker.color.b=0
        marker.color.a=0.3 #transparency

        marker.text='Not used'


        marker_array.markers.append(marker)

        alpha+=0.1
        if alpha>2*math.pi:
            alpha=0
        
        radius=3

        marker=Marker()
        marker.header.frame_id='world'
        marker.ns='my_drawings'
        marker.id=1
        marker.type=Marker.CUBE
        marker.action=Marker.MODIFY

        marker.pose.position.x=radius*math.cos(alpha)
        marker.pose.position.y=radius*math.sin(alpha)
        marker.pose.position.z=0
        marker.pose.orientation.x=0
        marker.pose.orientation.y=0
        marker.pose.orientation.z=0

        marker.scale.x=0.3
        marker.scale.y=0.3
        marker.scale.z=0.3

        marker.color.r=0
        marker.color.g=1
        marker.color.b=0
        marker.color.a=1 #transparency

        marker.text='Not used'


        marker_array.markers.append(marker)

        marker=Marker()
        marker.header.frame_id='world'
        marker.ns='my_drawings'
        marker.id=2
        marker.type=Marker.TEXT_VIEW_FACING
        marker.action=Marker.MODIFY

        marker.pose.position.x=0
        marker.pose.position.y=0
        marker.pose.position.z=0
        marker.pose.orientation.x=0
        marker.pose.orientation.y=0
        marker.pose.orientation.z=0

        marker.scale.x=1
        marker.scale.y=1
        marker.scale.z=3

        marker.color.r=0
        marker.color.g=1
        marker.color.b=0
        marker.color.a=1 #transparency

        marker.text='Not used'

        marker_array.markers.append(marker)

        pub.publish(marker_array)

        rate.sleep()
        

if __name__ == '__main__':
    listener()