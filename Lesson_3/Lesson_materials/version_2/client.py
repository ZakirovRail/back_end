# python3 client.py 127.0.0.1 7777

from socket import socket, AF_INET, SOCK_STREAM
import time

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 8888))


msg = "Hi,server"
s.send(msg.encode('utf-8'))
data = s.recv(4096)
print(data.decode('utf-8'))
s.close()


