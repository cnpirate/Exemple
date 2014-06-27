import socket
import sys

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# print(s)

# port = socket.getservbyname("http", "tcp")
# print(port)

# s.connect(("www.baidu.com", port))

# print(s.getsockname())
# print(s.getpeername())

port = 70
host = sys.argv[1]
filename = sys.argv[2] + "\r \n"
content = filename.encode("gbk")

print("sdfasfd", filename)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.send(content)

while True:
	buf = s.recv(2048)
	if not len(buf.decode("gbk")):
		break
	sys.stdout.write(buf.decode("gbk"))
