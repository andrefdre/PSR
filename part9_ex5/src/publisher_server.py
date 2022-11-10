#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from part9_ex5.msg import Dog

def main():
    dog=Dog()
    dog.name='Luffy'
    dog.color='black'
    dog.age=2
    dog.brothers.append='Ace'
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():

        pub.publish(dog)
        rate.sleep()

    
if __name__ == '__main__':
        main()
