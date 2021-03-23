# python3 server.py 127.0.0.1 7777
import socket
import json
import sys
import logging

from utils import load_configs, send_message, get_message

CONFIGS = dict()
SERVER_LOGGER = logging.getLogger('server')


def handle_message(message, CONFIGS):
    global SERVER_LOGGER
    SERVER_LOGGER.debug(f'Run handle_message method o server side : {message}')
    if CONFIGS.get('ACTION') in message \
            and message[CONFIGS.get('ACTION')] == CONFIGS.get('PRESENCE') \
            and CONFIGS.get('TIME') in message \
            and CONFIGS.get('USER') in message \
            and message[CONFIGS.get('USER')][CONFIGS.get('ACCOUNT_NAME')] == 'Guest':
        return {CONFIGS.get('RESPONSE'): 200}
    return {
        CONFIGS.get('RESPONSE'): 400,
        CONFIGS.get('ERROR'): 'Bad Request'
    }


def main():
    global CONFIGS, SERVER_LOGGER
    CONFIGS = load_configs()
    listen_port = CONFIGS.get('DEFAULT_PORT')
    try:
        if '-p' in sys.argv:
            listen_port = int(sys.argv[sys.argv.index('-p') + 1])
        if not 65535 >= listen_port >= 1024:
            raise ValueError
    except IndexError:
        SERVER_LOGGER.critical(f'After -\'p\' should be specified the port')
        sys.exit(1)
    except ValueError:
        SERVER_LOGGER.critical(f'The port should be specified in the range from 1024 to 65535')
        sys.exit(1)

    try:
        if '-a' in sys.argv:
            listen_address = sys.argv[sys.argv.index('-a') + 1]
        else:
            listen_address = ''
    except IndexError:
        SERVER_LOGGER.critical(f'After -\'a\' - requires specify address for')
        sys.exit(1)

    SERVER_LOGGER.info(f'The server were run on port: {listen_port}, with the address: {listen_address}')

    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.bind((listen_address, listen_port))

    transport.listen(CONFIGS.get('MAX_CONNECTIONS'))

    while True:
        client, client_address = transport.accept()
        try:
            message = get_message(client, CONFIGS)
            response = handle_message(message, CONFIGS)
            send_message(client, response, CONFIGS)
            client.close()
        except (ValueError, json.JSONDecodeError):
            SERVER_LOGGER.critical(f'Incorrect message from the client')
            print('Received inappropriate message from a client')
        finally:
            client.close()


if __name__ == '__main__':
    main()
