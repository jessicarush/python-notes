'''Importing Modules'''

# You can import your own python file as a module or a module from the 
# python standard library in the same way:

import random
import myfile

# when you import this way, you need to include the module name as a prefix
# to any functions you want to use from that module. This is to avoid any
# possible naming conflicts between modules.

possibilities = [ 'red', 'orange', 'yellow', 'green', 'blue', 'cyan']

random.choice(possibilities)

# Import a function from a module:

from random import choice

# when you import this way, you can reference the function name directly:

choice(possibilities)

# Import a module and give it another name using 'as':

import random as ran

ran.choice(possibilities)

# Import a function from a module and give it another name:

from random import choice as mix

mix(possibilities)

# Import a class from a module:

from myclasses import Person

# When importing, Python looks in the current directory first (so if you have a
# file named random.py in your current directory, it will use that over the one
# in the standard library. The standard library on a mac:

# Library/Frameworks/Python.framework/Versions/3.5/lib/python3.6


# __name__ == '__main__'
# -----------------------------------------------------------------------------
# If you intend for your module to be imported, remember that your program
# should most likely run by calling a function, not just start running as soon
# as its imported. When you want to test and run your code from within module,
# itself use this:

if __name__ == '__main__':
    pass # call the function that starts the script


# see also packages.py
