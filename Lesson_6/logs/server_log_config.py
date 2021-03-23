import logging
from logging import handlers

logger = logging.getLogger('server_app')
_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(module)s - %(message)s ')

logger.addHandler(logging.handlers.TimedRotatingFileHandler('server_log.log', when='D', interval=1, delay=False))
fh = logging.FileHandler('server_log.log', encoding='utf-8')
fh.setLevel(logging.DEBUG)
fh.setFormatter(_formatter)

logger.addHandler(fh)
logger.setLevel(logging.DEBUG)


if __name__ == '__main__':
    logger.critical('Critical error')
    logger.error('error')
    logger.debug('debug info')
    logger.info('info')
