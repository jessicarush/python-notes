'''Pygal - Analyzing Die Rolls'''

# Pygal is a python visualization package which produces scalable vector
# graphics. If you plan to use your visualizations online, this is ideal.

# pip3 install pygal

# http://pygal.org/en/stable/
# http://pygal.org/en/stable/documentation/types/index.html

# -----------------------------------------------------------------------------
# Ideally the following class would be saved as a module: die.py
# -----------------------------------------------------------------------------

from random import randint

class Die():
    '''A class representing a single Die.'''

    def __init__(self, sides=6):
        '''Assume a six-sided die.'''
        self.sides = sides

    def roll(self):
        '''Return a random value between 1 and number of sides.'''
        return randint(1, self.sides)


# -----------------------------------------------------------------------------
# Ideally the following would be in it's own file and we'd import the class
# -----------------------------------------------------------------------------

import pygal
# from die import Die

# create a D6:
die = Die()

# make some rolls and store the results in a list:
# results = []
# for roll_num in range(1000):
#     result = die.roll()
#     results.append(result)

# or use a list comprehension:
results = [die.roll() for roll_num in range(1000)]

# analyze the die results:
# frequencies = []
# for value in range(1, die.sides+1):
#     frequency = results.count(value)
#     frequencies.append(frequency)

# or use a list comprehension:
frequencies = [results.count(value) for value in range(1, die.sides+1)]

# visualize the results:
histogram = pygal.Bar()

histogram.title = 'Results of rolling D6 1000 times'
histogram.x_labels = list(range(1, die.sides+1))
histogram.x_title = 'result'
histogram.y_title = 'frequency of result'

histogram.add('D6', frequencies)
histogram.render_to_file('die_visual_1.svg')

# -----------------------------------------------------------------------------
# Two dice
# -----------------------------------------------------------------------------

die_1 = Die()
die_2 = Die()

results = [(die_1.roll() + die_2.roll()) for roll_num in range(1000)]
max_result = die_1.sides + die_2.sides
frequencies = [results.count(value) for value in range(1, max_result+1)]

hist2 = pygal.Bar()

hist2.title = 'Results of rolling two D6 1000 times'
hist2.x_labels = list(range(1, max_result+1))
hist2.x_title = 'result'
hist2.y_title = 'frequency of result'

hist2.add('D6 + D6', frequencies)
hist2.render_to_file('die_visual_2.svg')

# -----------------------------------------------------------------------------
# Two different dice
# -----------------------------------------------------------------------------

die_1 = Die()
die_2 = Die(10)

results = [(die_1.roll() + die_2.roll()) for roll_num in range(1000)]
max_result = die_1.sides + die_2.sides
frequencies = [results.count(value) for value in range(1, max_result+1)]

hist2 = pygal.Bar()

hist2.title = 'Results of rolling a D6 and D10 10,000 times'
hist2.x_labels = list(range(1, max_result+1))
hist2.x_title = 'result'
hist2.y_title = 'frequency of result'

hist2.add('D6 + D10', frequencies)
hist2.render_to_file('die_visual_3.svg')
