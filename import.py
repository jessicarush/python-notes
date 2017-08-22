# Importing Modules

# Import a module and give it another name using 'as':

import random as aleatoire

possibilities = [
    'red',
    'orange',
    'yellow',
    'green',
    'blue',
    'cyan'
]
print(aleatoire.choice(possibilities))

"""
Notice when we import a whole module, you have to use the module name. as
prefix to any functions you want to use from that module. This is to avoid any
possible naming conflicts between modules. In the next example we import a
function directly and rename it.
"""

# Import a function and give it another name:

from random import choice as mix
print(mix(possibilities))

"""
When importing, Pyhton looks in the current directory first (so if you have a
module named random.py in your current directory, it will use that over the one
in the standard library. The standard library on a mac:
Library/Frameworks/Python.framework/Versions/3.5/lib/python3.6
"""
