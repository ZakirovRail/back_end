import logging

logger = logging.getLogger('client_app')
_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(module)s - %(message)s ')

fh = logging.FileHandler('client_log.log', encoding='utf-8')
fh.setLevel(logging.DEBUG)
fh.setFormatter(_formatter)

logger.addHandler(fh)
logger.setLevel(logging.DEBUG)
