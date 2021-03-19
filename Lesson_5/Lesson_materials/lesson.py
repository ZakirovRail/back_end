# python3 lesson.py
import logging

logging.basicConfig(
    filename='app.log',
    format='%(levelname)-10s %(asctime)-30s %(message)s',
    level=logging.DEBUG
)

log = logging.getLogger('app.' + __name__)
# log = logging.getLogger('basic')

log.debug('debug message')
log.info('info message')
log.warning('warning message')
log.error('error message')
log.critical('critical message')





