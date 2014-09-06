import struct
import socket
import binascii

rawSocket = socket.socket(socket.PF_PACKET, 
	socket.SOCK_RAW, socket.htons(0x0800))

pkt = rawSocket.recvfrom(2048)

# Decoding Ethernet Header
etherHeader = pkt[0][0:14]

eth_hdr = struct.unpack("!6s6s2s", etherHeader)

print "Destination Mac Address : ", binascii.hexlify(eth_hdr[0])
print "Source Mac Address : ", binascii.hexlify(eth_hdr[1])
print "Ether Type : ", binascii.hexlify(eth_hdr[2])

# Decoding IP Header
ipHeader = pkt[0][14:34]

ip_hdr = struct.unpack("!12s4s4s", ipHeader)

print "Source IP : " + socket.inet_ntoa(ip_hdr[1]) 
print "Destination IP : " + socket.inet_ntoa(ip_hdr[2])

