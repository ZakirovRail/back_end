from socket import socket, AF_INET, SOCK_STREAM

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 8888))

while True:
    tm = s.recv(1024)
    print(tm.decode('utf-8'))
s.close()
