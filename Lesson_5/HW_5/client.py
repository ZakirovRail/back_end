# python3 client.py 127.0.0.1 7777

import socket
import json
import sys
import time
import logging
import client_log_config


from utils import load_configs, send_message, get_message

CONFIGS = dict()
logger = logging.getLogger('client_app')


def create_presence_message(account_name, CONFIGS):
    message = {
        CONFIGS.get('ACTION'): CONFIGS.get('PRESENCE'),
        CONFIGS.get('TIME'): time.time(),
        CONFIGS.get('USER'): {CONFIGS.get('ACCOUNT_NAME'): account_name}
    }
    logger.info(f'The presence message were created \n {message}')
    return message


def handle_response(message, CONFIGS):
    if CONFIGS.get('RESPONSE') in message:
        if message[CONFIGS.get('RESPONSE')] == 200:
            logger.info(f'The response was handled successfully for the message \n {message}')
            return '200: OK'
        logger.error(f'The response was handled with an error for the message \n {message} \n. '
                     f'The error will be returned')
        return f'400 : {message[CONFIGS.get("ERROR")]}'
    logger.error(f'The RESPONSE is missed in the message \n {message}. \n Will be raised {ValueError}')
    raise ValueError


def main():
    global CONFIGS
    logger.debug(f'The following configs are set \n. {CONFIGS}')
    CONFIGS = load_configs(is_server=False)
    logger.debug(f'For the key "is_server" set to "False" value')
    try:
        server_address = sys.argv[1]
        logger.debug(f'The server_address set to {server_address}')
        server_port = int(sys.argv[2])
        logger.debug(f'The server_port set to {server_port}')
        if not 65535 >= server_port >= 1024:
            logger.error(f'The specified server_port out of range (1024, 65535). \n Entered value is {server_port}'
                         f'\n Will be raised {ValueError}')
            raise ValueError
    except IndexError:
        server_address = CONFIGS.get('DEFAULT_IP_ADDRESS')
        server_port = CONFIGS.get('DEFAULT_PORT')
        logger.warning(f'A server_address and a server_port are not specified, will be set to default values \n'
                       f' The server_address - {server_address} \n'
                       f' The server_port {server_port}')
    except ValueError:
        logger.error(f'The specified server_port out of range (1024, 65535). \n Entered value is {server_port}'
                     f'\n Will be raised {ValueError}')
        print('The port should be in the range of 1024 and 65535')
        sys.exit(1)

    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logger.debug(f'The socket was established for connection')
    transport.connect((server_address, server_port))
    logger.debug(f'The connection with a server were established using {server_address} and {server_port}')
    presence_message = create_presence_message('Guest', CONFIGS)
    logger.info(f'The presence_message were created: \n'
                f'{presence_message}')
    send_message(transport, presence_message, CONFIGS)
    logger.debug(f'The presence_message were sent to the server with parameters: \n'
                 f'socket - {transport}'
                 f'presence message - {presence_message}'
                 f'CONFIGS - {CONFIGS}')
    try:
        response = get_message(transport, CONFIGS)
        logger.debug(f'The response were received:  \n {response}')
        handled_response = handle_response(response, CONFIGS)
        logger.info(f'The response were handled:  \n {handled_response}')
        print(f'The response from the server: {response}')
        print(handled_response)
    except (ValueError, json.JSONDecodeError):
        logger.error(f'An error during decoding of server\'s response occurred. \n'
                     f'The response - {response} \n'
                     f'Error message - {ValueError}')
        print('Error message decoding ')


if __name__ == '__main__':
    logger.debug(f'Start running client with the main() method')
    main()
