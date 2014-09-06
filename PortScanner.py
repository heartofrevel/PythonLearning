#!/usr/bin/env python

import subprocess
import socket
import sys
from datetime import datetime

subprocess.call('clear', shell=True)

server = raw_input("Enter Host : ")
serverIP = socket.gethostbyname(server)

t1 = datetime.now()

try:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	for port in xrange(1,65535):
		result = sock.connect_ex((serverIP, port))
		#print result
		if result == 0:
			print "Port Open "+str(port)
	sock.close()
except:
	print "Error"

t2 = datetime.now()

total =  t2 - t1
print total