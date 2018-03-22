import socket
import struct
import sys

mcast_grp = '224.1.1.1'
server_address = ('', 5000)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(server_address)

group = socket.inet_aton(mcast_grp)
mreq = struct.pack('4sl', group, socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

while True:
	try:
		data, addr = sock.recvfrom(1024)
		print data
		print addr
	except KeyboardInterrupt:
		print "Stopped listening"
		break
	except Exception as e: 
	print (e)
	break