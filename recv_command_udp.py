import socket
import cv2
import pickle

UDP_IP = "192.168.1.102"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

def parse_message(msg):
	idx = msg.find('{')
	idx_end = msg.find('}')
	if idx < 0 or idx_end < 0: # Invalid message
		return None
	m = msg[idx+1:idx_end]
	tok = m.split()
	cmd = tok[0]
	targets = {}
	for t in tok[1:]:
		x = t.split(':')
		targets[x[0]] = x[1]
	return (cmd, targets)

#test_msg = "{speed m0:20 m1:25}"
#print parse_message(test_msg)

while True:
	data, addr = sock.recvfrom(1024)
	res =  parse_message(data)
	print res
	
	if 'speed' in res[0]:
		print 'Command is "{}"'.format(res[0])
		for e in res[1].keys():
			print 'Motor {}: value = {}, 2x value = {}'.format(e,res[1][e], 2*float(res[1][e]))
	elif 'image' in res[0]:
		print 'Command is "{}"'.format(res[0])
		for e in res[1].keys():
			im = pickle.loads(res[1][e])
			cv2.imshow(e, im)
			cv2.waitKey(0.1)
