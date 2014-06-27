import socket
import sys
import struct
from ctypes import *

class POINT(Structure):
	_fields_ = [("x", c_int),
					("y", c_int*4)]

point = POINT()

host = ''
port = 50007
# localAddr = ('10.10.11.68', port)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# print(socket.gethostname())
# sys.exit()
# s.bind(localAddr)
s.bind((host, port))
s.listen(1)

print(type(POINT))

conn, addr = s.accept()
print("Connected by", addr)

while True:
	data = conn.recv(1024)
	if not data:		
		break
	# print("Server received", data.decode("gbk"))
	# aa, bb = struct.unpack("HH", data)
	# print(aa, bb)
	cc = cast(data, POINTER(POINT)).contents
	print(cc.x)
	for i in cc.y:
		print(i)
	conn.sendall(data)

conn.close()