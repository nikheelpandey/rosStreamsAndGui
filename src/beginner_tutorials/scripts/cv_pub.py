
#!/usr/bin/env python3
import rospy
import sys
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

bridge = CvBridge()
rospy.init_node('image_pub')
rospy.loginfo('image_pub node started')
pub = rospy.Publisher('image', Image, queue_size=10)

cam = cv2.VideoCapture(0)

def start_node():

    while not rospy.is_shutdown():

        meta, frame = cam.read()
        if meta:
            msg_frame =bridge.cv2_to_imgmsg(frame,"bgr8")
            pub.publish(msg_frame, "RGB8")
        
        rospy.Rate(1.0).sleep()





if __name__ == '__main__':
    try:
        start_node()
    except rospy.ROSInterruptException:
        pass
