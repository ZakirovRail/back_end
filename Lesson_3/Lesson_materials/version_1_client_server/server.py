from socket import socket, AF_INET, SOCK_STREAM
import time

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 8888))
s.listen(5)

while True:
    client, addr = s.accept()
    time_str = 'Текущее серверное время - ' + time.ctime(time.time()) + "\n"
    client.send(time_str.encode('utf-8'))
    client.close()
