# python3 server.py 127.0.0.1 7777
from socket import socket, AF_INET, SOCK_STREAM
import time


def main():
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(('', 8888))
    s.listen(5)

    while True:
        client, addr = s.accept()
        data = client.recv(4096)
        print(data.decode('utf-8'))
        msg = 'Hi, client'
        client.send(msg.encode('utf-8'))
        client.close()
