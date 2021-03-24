from socket import socket, AF_INET, SOCK_STREAM

address = ('localhost', 8888)


def client():
    with socket(AF_INET, SOCK_STREAM) as sock:
        sock.connect(address)
        while True:
            msg = input('Your message: ')
            if msg == 'exit':
                break
            sock.send(msg.encode('utf-8'))
            data = sock.recv(1024).decode('utf-8')
            print('Response:', data)


if __name__ == '__main__':
    client()
