#!/usr/bin/env python

import subprocess
import socket
import thread
from datetime import datetime
from time import sleep
import sys

subprocess.call('clear')

server = raw_input("Enter Host : ")
serverIP = socket.gethostbyname(server)

startPort = int(raw_input("Enter Start Port : "))
endPort = int(raw_input("Enter End Port : "))

threadCount = int(raw_input("Enter thread count : "))

portCount = endPort - startPort
portPerThread = portCount/threadCount

start = startPort
end = startPort+portPerThread

def portScan(startPort, endPort):
	try:
		for port in xrange(startPort, endPort+1):
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			result = sock.connect_ex((serverIP, port))
			#print result
			if result == 0:
				print "Port Open "+str(port)
				pass
			sock.close()

	except KeyboardInterrupt:
    		print "You pressed Ctrl+C"
    		sys.exit()

	except socket.gaierror:
    		print 'Hostname could not be resolved. Exiting'
    		sys.exit()

	except socket.error:
    		print "Couldn't connect to server"
    		sys.exit()

for i in range(threadCount):
	print "Adding Thread %d"%i
	thread.start_new_thread(portScan, (start, end,))
	start = end+1
	end  = start+portPerThread
	print "Thread Added %d"%i

while True:
	pass