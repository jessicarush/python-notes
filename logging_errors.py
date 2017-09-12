'''Logging Error Messages'''

# The standard Python library module is logging.
# https://docs.python.org/3/library/logging.html
# The logging module includes:

# The message that you want to save to the log
# Ranked priority levels as functions:
# debug(), info(), warn(), error(), and critical()
# One or more logger objects as the main connection with the module
# Handlers that direct the message to your terminal, a file, a database, or
# somewhere else
# Formatters that create the output
# Filters that make decisions based on the input

import logging

fmt = '%(asctime)s %(levelname)s %(lineno)s %(message)s'
logging.basicConfig(level=logging.DEBUG, filename='test.log', format=fmt)

# priority levels:

logging.debug('debug message')
logging.info('info message')
logging.warn('warning message')
logging.error('error message')
logging.critical('critical message')

# the default priority level is warn
# set the default by using basicConfig(). It should appear before any other
# logging functions as above.

logging.basicConfig(level=logging.DEBUG)

# here's a logger object:

logger = logging.getLogger('my_logger')
logger.debug('debug message')

# handlers direct messages to different places, for example, a log file:

logging.basicConfig(level=logging.DEBUG, filename='test.log')

# Calling basicConfig() with a filename argument created a FileHandler and made
# it available to the logger. The logging module includes at least 15 handlers
# to send messages to places such as the screen, email, web servers and files.

# you can format your logged messages:

fmt = '%(asctime)s %(levelname)s %(lineno)s %(message)s'
logging.basicConfig(level=logging.DEBUG, filename='test.log', format=fmt)
