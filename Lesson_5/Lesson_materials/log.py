import logging
import sys
from logging import handlers

_formatter = logging.Formatter('%(levelname)-10s %(asctime)s %(message)s')

critical_handler = logging.StreamHandler(sys.stderr)
critical_handler.setLevel(logging.CRITICAL)
critical_handler.setFormatter(_formatter)

log = logging.getLogger('basic')

log.addHandler(critical_handler)
log.critical('some panic message')
