from socket import socket, AF_INET, SOCK_STREAM

address = ('localhost', 8888)
responses = []


def client(responses):
    with socket(AF_INET, SOCK_STREAM) as sock:
        sock.connect(address)
        while True:
            data = sock.recv(1024).decode('utf-8')
            print(data)
            if data:
                responses.append(data)
                print('Response:', data)


if __name__ == '__main__':
    client(responses)
