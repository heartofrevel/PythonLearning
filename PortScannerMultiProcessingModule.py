#!/usr/bin/env python

import socket
from multiprocessing import Process
import subprocess
from time import sleep
import optparse

subprocess.call('clear')


parser = optparse.OptionParser('Usage : ' +\
	 	'-h <hostname>  -s <StartPort> -e <EndPort>  -t <Threads>', version ="%prog 1.0"  )

parser.add_option("-l", "--host", dest="hostname", type="string", help="Enter Hostname to Scan")
parser.add_option("-s", "--start-port", dest="startPort", type="int", default=1, help="Starting Port")
parser.add_option("-e", "--end-port", dest="endPort", type="int", default=65534, help="Ending Port")
parser.add_option("-t", "--threads", dest="threadCount", type="int", default=5, help="Enter Number of threads you want to use.")

(options, args) = parser.parse_args()
if(options.hostname == None):
	parser.print_help()
	exit(0)
else:
	server = options.hostname
	startPort = options.startPort
	endPort = options.endPort
	threadCount = options.threadCount


# server = raw_input("Enter Host : ")
serverIP = socket.gethostbyname(server)

# startPort = int(raw_input("Enter Start Port : "))
# endPort = int(raw_input("Enter End Port : "))

# threadCount = int(raw_input("Enter thread count : "))

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
	p = Process(target=portScan, args=(start, end, ))
	p.start()
	start = end+1
	end  = start+portPerThread