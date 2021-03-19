import logging
import sys
from logging import handlers

log = logging.getLogger('app')
log.setLevel(logging.INFO)

log.addHandler(logging.FileHandler('app_02.log'))  # display logs in file
# log.addHandler(logging.StreamHandler(sys.stderr))  # display logs in console
# log.addHandler(handlers.RotatingFileHandler('app.log', maxBytes=10))  # display logs in different files if achieve defined size file
# log.addHandler(handlers.TimedRotatingFileHandler('app.log', when= , delay=  ))  # display logs in different files
# log.removeHandler()







