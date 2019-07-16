'''Logging Error Messages'''


# The Python standard library module for logging is logging.
# https://docs.python.org/3/library/logging.html

# The logging module includes:
# – The message that you want to save to the log
# – Ranked priority levels as functions:
#   debug(), info(), warning(), error(), and critical()
# – One or more logger objects as the main connection with the module
# – Handlers that direct the message to your terminal, a file, a database,
#   or somewhere else
# – Formatters that create the output
# – Filters that make decisions based on the input

import logging

fmt = '%(asctime)s %(levelname)s %(lineno)s %(message)s'
logging.basicConfig(level=logging.DEBUG, filename='data/test.log', format=fmt)

# priority levels:
logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')


# Breakdown
# -----------------------------------------------------------------------------
# The default priority level is warn. Set the default by using basicConfig().
# This config should appear before any other logging functions as above.

logging.basicConfig(level=logging.DEBUG)

# handlers direct messages to different places, for example, a log file:

logging.basicConfig(level=logging.DEBUG, filename='data/test.log')

# you can format your logged messages:

fmt = '%(asctime)s %(levelname)s %(lineno)s %(message)s'
logging.basicConfig(level=logging.DEBUG, filename='data/test.log', format=fmt)

# here's a logger object:

logger = logging.getLogger('MyLogger')
logger.debug('here is my debug message')

# Calling basicConfig() with a filename argument created a FileHandler and made
# it available to the logger. The logging module includes at least 15 handlers
# to send messages to places such as the screen, email, web servers and files.

# The information here is pretty scant. For more information on this topic, go
# through the following in Doug Hellman's Python 3 Standard Library by example:
# p.980–986, p.563–564, p.644–647, p.650–653, p.671–674


# Log Record attributes
# -----------------------------------------------------------------------------
# There are a number of attributes (bits of information) that can be included
# in your logged message format. For a full list see:
# https://docs.python.org/3/library/logging.html#logrecord-attributes


# Logging Levels
# -----------------------------------------------------------------------------
# The predifined logging levels all have a numeric value associated to them.
# This is mostly of interest because you can define your own levels.

# Level     | Numeric value
# ----------|--------------
# CRITICAL  | 50
# ERROR     | 40
# WARNING   | 30
# INFO      | 20
# DEBUG     | 10
# NOTSET    | 0

# To define your own level:

SPECIAL_INFO_LEVEL_NUM = 21
logging.addLevelName(SPECIAL_INFO_LEVEL_NUM, 'SPECIAL_INFO')

def special_info(self, message, *args, **kws):
    if self.isEnabledFor(SPECIAL_INFO_LEVEL_NUM):
        self._log(SPECIAL_INFO_LEVEL_NUM, message, args, **kws)

logging.Logger.special_info = special_info

logger.special_info('Hey, this is special')

# That being said, while defining your own levels is possible, it shouldn't
# really be necessary, as the existing levels have been chosen on the basis of
# practical experience. It's also a very bad idea if you are developing a
# library as your custom level could conflict with others.
