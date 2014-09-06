#!/usr/bin/env python

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 4567))
s.send(raw_input());
data = s.recv(1024000)
s.close()
print 'Received'
print data