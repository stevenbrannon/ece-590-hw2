import socket
import cv2
import pickle
from time import sleep

UDP_IP = "192.168.1.102"
UDP_PORT = 5005
MESSAGE = "Hello, World!"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

# Define a message structure for a two wheeled robot
# All messages are represented as ascii strings. A single message shall be
# enclosed in braces i.e. a null message is defined as "{}"
# The first string within the message is the message type. It applies
# to all key value pairs in the message. A delclaritive massage may be defined
# as "{reset}" which causes the robot to reset. There may be an optional list
# of modifiers to the command in a comma seperated list of key value pairs.
# e.g. "{speed(unit:rad/sec) m0:20 m1:-25.0}" tells the robot to set the speed 
# in radians per second of motor0 to 20 and motor1 to -25

sock = socket.socket(socket.AF_INET,  	 # Internet
		     socket.SOCK_DGRAM)  # UDP

img = cv2.imread('robot.png')
img_str = pickle.dumps(img)
IMAGE_COMMAND ="{" + "image disp0:{}".format(img_str) + "}"

# loop forever sending the image packet at about 5Hz
while True:
	sock.sendto(IMAGE_COMMAND, (UDP_IP, UDP_PORT))
	sleep(.2)
