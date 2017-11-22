'''Logging Error Messages'''

# The Python standard library module for logging is logging.
# https://docs.python.org/3/library/logging.html

# The logging module includes:
# – The message that you want to save to the log
# – Ranked priority levels as functions:
#   debug(), info(), warn(), error(), and critical()
# – One or more logger objects as the main connection with the module
# – Handlers that direct the message to your terminal, a file, a database,
#   or somewhere else
# – Formatters that create the output
# – Filters that make decisions based on the input

import logging

fmt = '%(asctime)s %(levelname)s %(lineno)s %(message)s'
logging.basicConfig(level=logging.DEBUG, filename='test.log', format=fmt)

# priority levels:

logging.debug('debug message')
logging.info('info message')
logging.warn('warning message')
logging.error('error message')
logging.critical('critical message')

# T he default priority level is warn. Set the default by using basicConfig().
# This config should appear before any other logging functions as above.

logging.basicConfig(level=logging.DEBUG)

# handlers direct messages to different places, for example, a log file:

logging.basicConfig(level=logging.DEBUG, filename='test.log')

# you can format your logged messages:

fmt = '%(asctime)s %(levelname)s %(lineno)s %(message)s'
logging.basicConfig(level=logging.DEBUG, filename='test.log', format=fmt)

# here's a logger object:

my_logger = logging.getLogger('MyLogger')
logger.debug('debug message')

# Calling basicConfig() with a filename argument created a FileHandler and made
# it available to the logger. The logging module includes at least 15 handlers
# to send messages to places such as the screen, email, web servers and files.

# The information here is pretty scant. On the next review of this topic, go
# through the following in Doug Hellman's Python 3 Standard Library by example:
# p.980–986, p.563–564, p.644–647, p.650–653, p.671–674
