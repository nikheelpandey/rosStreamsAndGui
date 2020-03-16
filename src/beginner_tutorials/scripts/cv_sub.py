#!/usr/bin/env python3
# Import ROS libraries and messages
import rospy
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge, CvBridgeError

# Initialize the ROS
rospy.init_node('frameCatcher', anonymous=True)

rospy.loginfo("ROS init!")
bridge = CvBridge()


# Loop to keep the program from shutting down unless ROS is shut down, or CTRL+C is pressed


def show_image(img):
    cv2.imshow("Image Window", img)
    cv2.waitKey(3)

# Define a callback for the Image message
def image_callback(img_msg):
    # log some info about the image topic
    rospy.loginfo(img_msg.header)

    # Try to convert the ROS Image message to a CV2 Image
    try:
        cv_image = bridge.imgmsg_to_cv2(img_msg, "RGB8")
    except CvBridgeError as e:
        rospy.logerr("CvBridge Error: {0}".format(e))

    # Show the converted image
    show_image(cv_image)


# Initalize a subscriber to the "image" topic with the function "image_callback" as a callback
sub_image = rospy.Subscriber("image", Image, image_callback)

# Initialize an OpenCV Window named "Image Window"
cv2.namedWindow("Image Window", 1)


while not rospy.is_shutdown():
    rospy.spin()