'''Resources''''

# -----------------------------------------------------------------------------
# Python philosophy
# -----------------------------------------------------------------------------

import this

# -----------------------------------------------------------------------------
# Good explanations
# -----------------------------------------------------------------------------
# Python Docs- https://docs.python.org/3/
# Built-ins: https://www.programiz.com/python-programming/methods/built-in
# http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/

# -----------------------------------------------------------------------------
# When looking for code
# -----------------------------------------------------------------------------
# PyPI - https://pypi.python.org/pypi
# Github - https://github.com/trending?l=python
# Active State - http://code.activestate.com/recipes/langs/python/

# -----------------------------------------------------------------------------
# help()
# -----------------------------------------------------------------------------
# In the python interpreter, use the help function to get information on a
# module or built-in function, or run the help utility to get information on
# keywords, symbols, topics, modules and built-in functions. For example:

help()      # Welcome to Python 3.6's help utility!

keywords    # lists all keywords
symbols     # lists all symbols
topics      # lists all help topics
modules     # list all modules
builtins    # lists all built-in functions and exceptions

yield       # describes the yield statement
@           # describes decorators
DEBUGGING   # provides information on 'pdb' the python debugger
random      # provides information on the random standard library module
print       # provides information in the print built-in function
ValueError  # provides information on the ValueError exception

# you don't have to enter the help utility to get help either, you can pass
# the name of a function or module directly (this method doesn't work for
# Topics, Keywords or Symbols).

help(print)
help(ValueError)
import random
help(random)

# you can also ask for specific help on a method or class such as:

help(list.extend)
help(str.translate)
help(set.difference)
help(datetime.datetime)

# -----------------------------------------------------------------------------
# dir()
# -----------------------------------------------------------------------------
# The built-in dir function is an easy way to grab a list of all the attributes
# available inside an object (i.e., its methods and simpler data items). It can
# be called on any object that has attributes, including imported modules and
# built-in types, as well as the name of a data type.

import random
dir(random)

# To find out what attributes are provided in objects of built-in types, run
# dir on a literal or an existing instance of the desired type. For example,
# to see list, string, dict attributes, you can pass empty objects:

dir(list)
#  [..., 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop',
#  'remove', 'reverse', 'sort']
dir(str)
#  [..., 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith',
#  'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha',
#  'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable',
#  'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip',
#  'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust',
#  'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith',
#  'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']'
dir(dict)
#  [..., 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem',
#  'setdefault', 'update', 'values']
dir(tuple)
#  [..., 'count', 'index']
dir(set)
#  [...,  'add', 'clear', 'copy', 'difference', 'difference_update', 'discard',
#  'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset',
#  'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update',
#  'union', 'update']

# -----------------------------------------------------------------------------
# Docstrings
# -----------------------------------------------------------------------------
# Builtins, modules and more have their own docstrings, which can also provide
# information. For example:

print(print.__doc__)
import random
print(random.__doc__)
print(random.choice.__doc__)

# -----------------------------------------------------------------------------
# HTML PyDoc
# -----------------------------------------------------------------------------
# Another way to view help similar to the help() and docstrings is to use
# the built-in PyDoc HTML by running this command in terminal:

# python3 -m pydoc -b

# The interesting thing about this is, it will include any python modules
# (.py files) it finds from the current directory you were in when you
# launched it. It's actually pretty great!

# -----------------------------------------------------------------------------
# View the source code
# -----------------------------------------------------------------------------
# If you want to take a look at the actual file to read the comments and
# docstring there, you can use the __file__ magic method to show you the
# path to where this module lives:

import os
print(os.__file__)
# /Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/os.py
