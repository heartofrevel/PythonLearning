import socket
from multiprocessing import Process


def sendAndReceive():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('localhost', 4567))
	inp = raw_input()
	s.send(inp)
	data = s.recv(10240)
	s.close()
	print 'Received'
	print data


for i in xrange(1000):
	p = Process(target=sendAndReceive)
	p.start()






	