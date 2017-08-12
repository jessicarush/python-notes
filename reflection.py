# type()

import datetime

now = datetime.datetime.utcnow()

type(now)       # <class 'datetime.datetime'>
type(234)       # <class 'int'>
type('hello')   # <class 'str'>

# isinstance()
# because everything in Python is an object, isinsatnce works everywhere:

isinstance(now, datetime.datetime)  # True
isinstance(234, int)                # True
isinstance('hello', str)            # True
