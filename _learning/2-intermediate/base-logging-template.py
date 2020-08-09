#!/usr/bin/python3

################################################################
# Example of logging module
################################################################

import logging
import logging.handlers
import sys

logger = logging.getLogger("")
logger.setLevel(logging.DEBUG)
handler = logging.handlers.RotatingFileHandler(
   '/home/user/gerry/example3.log', maxBytes=(1048576*5), backupCount=7
)
formatter = logging.Formatter("%(asctime)s => %(levelname)s : %(message)s", datefmt='%Y-%m-%d %I:%M:%S %p')
handler.setFormatter(formatter)
logger.addHandler(handler)

logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))

logging.info('hello world')

logging.error('error - hello world')

logging.warning('warning - hello world')
name = 'Gerry'

logging.error('%s raised an error', name)

a = 5
b = 0

try:
   c = a / b
except Exception as e:
   logging.error("Exception occurred", exc_info=True)

   logging.warning('warning - hello world')