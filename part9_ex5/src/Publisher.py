#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from part9_ex5.msg import Dog

def main():
    dog=Dog()
    dog.name='Luffy'
    dog.color='black'
    dog.age=2
    dog.brothers.append('Ace')
    rospy.init_node("Publisher", anonymous=True)
    topic_name=rospy.get_param("~topic_name")
    frequency=rospy.get_param("~frequency")
    pub = rospy.Publisher(topic_name, Dog, queue_size=10)
    rate = rospy.Rate(frequency)

    while not rospy.is_shutdown():
        pub.publish(dog)
        rate.sleep()

    
if __name__ == '__main__':
        main()
