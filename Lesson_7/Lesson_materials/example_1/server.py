import time
import select
from socket import socket, AF_INET, SOCK_STREAM


def mainloop():
    address = ('', 8888)
    clients = []
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(5)
    sock.settimeout(1)

    while True:
        try:
            conn, addr = sock.accept()
        except OSError as e:
            pass
        else:
            clients.append(conn)
        finally:
            w_list = []
            try:
                r_list, w_list, e_list = select.select([], clients, [], 0)
            except Exception as e:
                pass

            for s_client in w_list:
                time_str = time.ctime(time.time()) + '\n'
                try:
                    s_client.send(time_str.encode('utf-8'))
                except:
                    clients.remove(s_client)


print('Start server')
mainloop()
