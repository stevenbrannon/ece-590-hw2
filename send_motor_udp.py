import socket
from time import sleep

UDP_IP = "192.168.1.101"
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


MOTOR_COMMAND = "{speed m0:20 m1:25}"

# loop forever sending the motor control packet at about 50Hz
while True:
	sock.sendto(MOTOR_COMMAND, (UDP_IP, UDP_PORT))
	sleep(2)
