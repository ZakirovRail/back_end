import logging
import sys
from logging import handlers

logger = logging.getLogger('app_2')

formatter = logging.Formatter('%(levelname)-10s %(asctime)s %(message)s')

file_handler = logging.FileHandler('app_2_log_2.log', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


if __name__ == '__main__':
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(_formatter)
    logger.addHandler(console)
    logger.warning('some warning')
    logger.fatal('some fatal')
    logger.info('some test')
    logger.debug('debug test')
    logger.error('error example')
    # logger.exception('exception example')
