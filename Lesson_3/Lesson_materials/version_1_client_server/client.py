from socket import socket, AF_INET, SOCK_STREAM
import time

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 8888))

time_data = s.recv(1024)
s.close()
print(time_data)
print(time_data.decode('utf-8'))

