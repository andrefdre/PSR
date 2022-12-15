#!/usr/bin/env python3
import rospy

import math
import tf2_ros
import geometry_msgs.msg
import turtlesim.srv

def main():
    rospy.init_node('listener_moon_to_venus')


    listener = tf2_ros.TransformListener()

    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        try:
            (trans,rot) = listener.lookup_transform('venus','moon',rospy.Time(0)
              )
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            continue

        distance=math.sqrt(trans[0]**2+trans[1]**2)
        print(distance)

        rate.sleep()


    if __name__ == '__main__':
        main()