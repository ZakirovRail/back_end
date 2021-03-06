# python3 client.py 127.0.0.1 7777

import socket
import json
import sys
import time
import logging

from utils import load_configs, send_message, get_message

CONFIGS = dict()
CLIENT_LOGGER = logging.getLogger('client')


def create_presence_message(account_name, CONFIGS):
    message = {
        CONFIGS.get('ACTION'): CONFIGS.get('PRESENCE'),
        CONFIGS.get('TIME'): time.time(),
        CONFIGS.get('USER'): {
            CONFIGS.get('ACCOUNT_NAME'): account_name
        }
    }
    CLIENT_LOGGER.info(f'The presence message were created')
    return message


def handle_response(message, CONFIGS):
    CLIENT_LOGGER.info(f'Parsing message from the server')
    if CONFIGS.get('RESPONSE') in message:
        if message[CONFIGS.get('RESPONSE')] == 200:
            CLIENT_LOGGER.info(f'The response was handled successfully for the message from the server')
            return '200: OK'
        CLIENT_LOGGER.critical(f'Failed message parsing from the server')
        return f'400 : {message[CONFIGS.get("ERROR")]}'
    raise ValueError


def main():
    global CONFIGS
    CONFIGS = load_configs(is_server=False)
    try:
        server_address = sys.argv[1]
        server_port = int(sys.argv[2])
        if not 65535 >= server_port >= 1024:
            raise ValueError
    except IndexError:
        server_address = CONFIGS.get('DEFAULT_IP_ADDRESS')
        server_port = CONFIGS.get('DEFAULT_PORT')
    except ValueError:
        CLIENT_LOGGER.critical(f'The port should be specified in the range of (1024, 65535)')
        print('The port should be in the range of 1024 and 65535')
        sys.exit(1)

    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.connect((server_address, server_port))
    presence_message = create_presence_message('Guest', CONFIGS)
    CLIENT_LOGGER.info(f'Sending a message to the server')
    send_message(transport, presence_message, CONFIGS)
    try:
        response = get_message(transport, CONFIGS)
        handled_response = handle_response(response, CONFIGS)
        CLIENT_LOGGER.debug(f'The response were handled: {response}')
        CLIENT_LOGGER.info(f'The response were handled: {handled_response}')
        print(f'The response from the server: {response}')
        print(handled_response)
    except (ValueError, json.JSONDecodeError):
        CLIENT_LOGGER.critical(f'An error during decoding of server message')
        print('Error message decoding ')


if __name__ == '__main__':
    main()
