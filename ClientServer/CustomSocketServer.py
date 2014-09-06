#!/usr/bin/env python 

import SocketServer
import thread

class CustomHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		print "Connection : ", self.client_address
		data = "dummy"
		while len(data):
			data = self.request.recv(1024)
			self.request.send(data)
		print "Clinet Left"	



class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

serverAddress = ('0.0.0.0', 9000)
server = ThreadedTCPServer(serverAddress, CustomHandler)
server.serve_forever()


