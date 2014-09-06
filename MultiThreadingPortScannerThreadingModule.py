#!/usr/bin/env python

import threading
import subprocess
import socket
import Queue
from datetime import datetime
from time import sleep
import optparse

parser = optparse.OptionParser("Usage ")


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


class PortScan(threading.Thread):
	def __init__(self, queue, startPort, endPort):
		threading.Thread.__init__(self)
		self.queue = queue
		self.startPort = startPort
		self.endPort = endPort

	def run(self):
		try:
			for port in xrange(self.startPort, self.endPort+1):
				sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				result = sock.connect_ex((serverIP, port))
				sock.send("Hello\r\n")
				recvResult = sock.recv(100);
				print "Port Open"+str(port)
				#print result
				# if result == 0:
				# 	print "Port Open "+str(port)
			sock.close()
			# self.queue.task_done()


		except KeyboardInterrupt:
    			print "You pressed Ctrl+C"
    			sys.exit()

		except socket.gaierror:
    			print 'Hostname could not be resolved. Exiting'
    			sys.exit()

		except socket.error:
    			print "Couldn't connect to server"
    			sys.exit()
    	except :
    		sys.exit(0)


queue  = Queue.Queue()


for i in xrange(threadCount):
	print "Adding Thread"
	worker = PortScan(queue, start, end)
	worker.setDaemon(True)
	worker.start()
	start = end+1
	end  = start+portPerThread
	print "Thread Added %d"%i

sleep(5)