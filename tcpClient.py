import socket
import struct
from ctypes import *

host = "cnpirate"
port = 50007

class POINT(Structure):
	_fields_ = [("x", c_int),
					("y", c_int*4)]
ylistType = c_int*4
ylist = ylistType()
for i in range(100, 104):
	ylist[i-100] = i

point = POINT(7, ylist)

aa = 5
bb = 6

sendBuff = struct.pack("HH", aa, bb)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
# s.sendall(b'Hello, world.')
s.sendall(point)
data = s.recv(1024)
s.close()
# print("Received", data.decode("gbk"))