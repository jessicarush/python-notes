# type()

import datetime

now = datetime.datetime.utcnow()

type(now)       # <class 'datetime.datetime'>
type(234)       # <class 'int'>
type('hello')   # <class 'str'>

# bool()
# will tell you whether something is True or False

x = []
y = ['one']

bool(x)        # False
bool(y)        # True

# isinstance()
# because everything in Python is an object, isinsatnce works everywhere:

isinstance(now, datetime.datetime)  # True
isinstance(234, int)                # True
isinstance('hello', str)            # True
