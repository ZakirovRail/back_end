# python3 server.py 127.0.0.1 7777
import socket
import json
import sys
import logging
import server_log_config

from utils import load_configs, send_message, get_message

CONFIGS = dict()
logger = logging.getLogger('server_app')


def handle_message(message, CONFIGS):
    logger.debug(f'Run handle_message method o server side')
    if CONFIGS.get('ACTION') in message \
            and message[CONFIGS.get('ACTION')] == CONFIGS.get('PRESENCE') \
            and CONFIGS.get('TIME') in message \
            and CONFIGS.get('USER') in message \
            and message[CONFIGS.get('USER')][CONFIGS.get('ACCOUNT_NAME')] == 'Guest':
        logger.debug(f'The server successfully handled client\'s message. \n'
                     f'The message from the client {message}'
                     f'Will be return "RESPONSE: 200". ')
        return {CONFIGS.get('RESPONSE'): 200}
    logger.error(f'An error during client\'s message occurred. \n'
                 f'The "RESPONSE: 400" will be returned ')
    return {
        CONFIGS.get('RESPONSE'): 400,
        CONFIGS.get('ERROR'): 'Bad Request'
    }


def main():
    global CONFIGS
    logger.debug(f'The following configs are set \n. {CONFIGS}')
    CONFIGS = load_configs()
    try:
        if '-p' in sys.argv:
            listen_port = int(sys.argv[sys.argv.index('-p') + 1])
            logger.debug(f'The following listen_port is set - "{listen_port}"')
        else:
            listen_port = CONFIGS.get('DEFAULT_PORT')
            logger.debug(f'The DEFAULT_PORT listen_port is set - "{CONFIGS.get("DEFAULT_PORT")}"')
        if not 65535 >= listen_port >= 1024:
            logger.error(f'An error occurred on the server side during establishing listen_port. \n'
                         f'The listen_port is out of range (1024, 65535)')
            raise ValueError
    except IndexError:
        logger.error(f'An IndexError error occurred on the server side, because the port was not specified')
        print('After -\'p\' should be specified the port')
        sys.exit(1)
    except ValueError:
        logger.error(f'An ValueError error occurred on the server side, because the port was '
                     f'specified out of range (1024, 65535)')
        print('The port should be specified in the range from 1024 to 65535')
        sys.exit(1)

    try:
        if '-a' in sys.argv:
            listen_address = sys.argv[sys.argv.index('-a') + 1]
        else:
            listen_address = ''
    except IndexError:
        print('After -\'a\' - requires specify address for ')
        sys.exit(1)

    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    logger.debug(f'The socket were created on the server\'s side. \n'
                 f'transport - {str(transport)}')

    transport.bind((listen_address, listen_port))
    logger.debug(f'The binding of socket with the server\'s parameters. \n'
                 f'listen_address - {listen_address}. \n'
                 f'listen_port - {listen_port}. \n')

    transport.listen(CONFIGS.get('MAX_CONNECTIONS'))
    logger.debug(f'The number of connections established by server. \n'
                 f'MAX_CONNECTIONS - {(CONFIGS.get("MAX_CONNECTIONS"))}')

    while True:
        client, client_address = transport.accept()
        logger.debug(f'Establishing connection with a client using the following: \n'
                     f'client - {client}'
                     f'client_address - {client_address}')
        try:
            message = get_message(client, CONFIGS)
            logger.debug(f'The message is received from the client: \n'
                         f'message - {message}')

            response = handle_message(message, CONFIGS)
            logger.debug(f'The response is sent to the client: \n'
                         f'response - {response}')

            send_message(client, response, CONFIGS)
            logger.debug(f'The message is sent: \n'
                         f'client - {client} \n'
                         f'response - {response}\n'
                         f'CONFIGS - {CONFIGS}\n')
            # client.close()
        except (ValueError, json.JSONDecodeError):
            print('Received inappropriate message from a client')
        finally:
            client.close()


if __name__ == '__main__':
    logger.debug(f'Start running server with the main() method')
    main()
