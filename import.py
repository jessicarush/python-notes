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

#

# Import a function and give it another name:

from random import choice as mix
print(mix(possibilities))
