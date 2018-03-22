# import socket 

# MCAST_GRP = '224.1.1.1'
# MCAST_PORT = 5007

# sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
# sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
# sock.sendto("message", (MCAST_GRP, MCAST_PORT))

import socket
import struct
import sys

mcast_grp = ('224.3.29.71', 5000)
message = "Hello, World"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
#ttl = struct.pack('b',1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
sock.sendto(message, mcast_grp)
