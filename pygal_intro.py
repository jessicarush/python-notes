'''Pygal - Data Visualization Library'''

# Pygal is a python visualization package which produces scalable vector
# graphics. If you plan to use your visualizations online, this is ideal.

# pip3 install pygal

# http://pygal.org/en/stable/
# http://pygal.org/en/stable/documentation/types/index.html


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


# Misc notes: configuration
# -----------------------------------------------------------------------------
# There is a config class in the Pygal module (but the documentation is weak
# in terms of what is in this class). In short, config values are settable
# on the chart object:

chart = pygal.Bar()
chart.show_legend = False
chart.human_readable = True
chart.fill = True

# or, you can create a config object and set to the object:
my_config = pygal.Config()
my_config.show_legend = False
chart = pygal.Bar(my_config)

# or, config values can be passed as keyword args at init:

chart = pygal.XY(show_legend=False, human_readable=True, fill=True)

# or, config values can be passed when you render() at the end:

chart.render(show_legend=False, human_readable=True, fill=True)

# There are examples of many of the config options here:
# http://pygal.org/en/stable/documentation/configuration/chart.html
# http://pygal.org/en/stable/documentation/configuration/serie.html
# http://pygal.org/en/stable/documentation/configuration/value.html

# Configuration options should not be confused with styling:


# Misc notes: styling
# -----------------------------------------------------------------------------
# http://pygal.org/en/stable/documentation/styles.html
# It looks like in order to customize styles (ie fonts, colors) there are a
# couple of options:

# 1. choose a different theme from pygals list (14 in total):

from pygal.style import NeonStyle

pie_chart = pygal.Pie(style=NeonStyle)

# 2. choose one of five parametric themes (a parametric theme uses one default
# color and generates the others from that one). These include: lighten, darken,
# saturate, desaturate, and rotate. Apply thusly:

from pygal.style import DarkenStyle

my_style = DarkenStyle('#04dba4')
pie_chart = pygal.Pie(style=my_style)

# 3. or you can create your own style class:

from pygal.style import Style

my_style = Style(
  background='transparent',
  plot_background='transparent',
  foreground='#53E89B',
  legend_font_size=9,
  colors=('#E853A0', '#E8537A', '#E95355', '#E87653', '#E89B53'))

pie_chart = pygal.Pie(style=my_style)

# 4. once you have a style (whether it's imported or one you created yourself),
# you can add properties this way too:

my_style.title_font_size = 16
my_style.label_font_size = 10

# a list of available style properties can be found here:
# # http://pygal.org/en/stable/documentation/custom_styles.html

# The biggest complaint I have so far, is there doesn't seem to be an easy
# way to adjust the position of elements. There are a few things I can do like:
# – config the legend to be at the bottom
# – add margins around the whole chart
# – specify a size for the chart

# But if I want to say left align the title or add space above the legend only,
# or add space between the legend and the chart without changing the size of
# the chart... it appears to be limited. Perhaps this functionality will
# improve over time.
