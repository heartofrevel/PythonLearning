#!/usr/bin/env python

import socket
import sys
from datetime import datetime

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ("localhost", 4567, )
# print 'Starting up on %s port %s', % server_address
server.bind(server_address)

server.listen(100000)


while True:
	connection, client_addrsss = server.accept()
	print 'Connection from', connection.getpeername()

	data = connection.recv(4096)
	if data:
		print 'Received ', repr(data)
		if(data=="Buffalo"):
			print "Hello Buffalo"
		data = data.rstrip()
		# connection.send("%s\n%s\n%s\n" %('-'*80, data.center(80), '-'*80))
		connection.send(str(dayyyhtetime.time(datetime.now())))
		print "Response Sent"

	connection.shutdown(socket.SHUT_RD | socket.SHUT_WR)
	connection.close()
	print "Connection Closed"

server.close()
