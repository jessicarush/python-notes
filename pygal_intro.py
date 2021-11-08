'''Pygal - Data Visualization Library'''


# Pygal is a python visualization package which produces scalable vector
# graphics. If you plan to use your visualizations online, this is ideal.

# pip install pygal

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
num_rolls = 1000

# make some rolls and store the results in a list:
# results = []
# for roll_num in range(num_rolls):
#     result = die.roll()
#     results.append(result)

# or use a list comprehension:
results = [die.roll() for roll_num in range(num_rolls)]

# analyze the die results:
# frequencies = []
# for value in range(1, die.sides + 1):
#     frequency = results.count(value)
#     frequencies.append(frequency)

# or use a list comprehension:
frequencies = [results.count(value) for value in range(1, die.sides + 1)]

# visualize the results:
histogram = pygal.Bar()

histogram.title = f'Results of rolling D6 {num_rolls} times'
histogram.x_labels = list(range(1, die.sides + 1))
histogram.x_title = 'result'
histogram.y_title = 'frequency of result'

histogram.add('D6', frequencies)
histogram.render_to_file('demos/die_visual_1.svg')


# Two dice
# -----------------------------------------------------------------------------

die_1 = Die()
die_2 = Die()

results = [(die_1.roll() + die_2.roll()) for roll_num in range(num_rolls)]
max_result = die_1.sides + die_2.sides
frequencies = [results.count(value) for value in range(1, max_result + 1)]

hist2 = pygal.Bar()

hist2.title = f'Results of rolling two D6 {num_rolls} times'
hist2.x_labels = list(range(1, max_result + 1))
hist2.x_title = 'result'
hist2.y_title = 'frequency of result'

hist2.add('D6 + D6', frequencies)
hist2.render_to_file('demos/die_visual_2.svg')


# Two different dice
# -----------------------------------------------------------------------------

die_1 = Die()
die_2 = Die(10)

results = [(die_1.roll() + die_2.roll()) for roll_num in range(num_rolls)]
max_result = die_1.sides + die_2.sides
frequencies = [results.count(value) for value in range(1, max_result + 1)]

hist2 = pygal.Bar()

hist2.title = f'Results of rolling a D6 and D10 {num_rolls} times'
hist2.x_labels = list(range(1, max_result + 1))
hist2.x_title = 'result'
hist2.y_title = 'frequency of result'

hist2.add('D6 + D10', frequencies)
hist2.render_to_file('demos/die_visual_3.svg')


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

# A list of available style properties can be found here:
# http://pygal.org/en/stable/documentation/custom_styles.html

# The biggest complaint I have so far, is that there's granular styling for
# some things but not others. For example, I can set the plot's background to
# be transparent, but that also changes the tooltip box to transparent. You can
# set the border radius of the tooltip box, but not the border color or
# background independent from the resst of the plot. The main axis seem to be
# random. For the life of me I can't seem to get just one line along the x and
# y axis. It's like you get one or the other or all the grod lines in between.

# Other issues:
# - can't adjust line colors independent from label colors
# - can't align the title
# - can't adjust space between the labels and the chart

# Update:
# I've managed to work out some of these issues by modifying (hacking) the
# library's css. Look at:
# venv/lib/python3.7/site-packages/pygal/css


# Embedding the svg in an HTML page
# -----------------------------------------------------------------------------
# When you render_to_file('mychart.svg'), there are a number of ways to include
# it in your html. So far I've experimented with <iframe>, <embed> and <object>
# like so:

# iframe:
# <div class="chart-container"">
#   <iframe src="{{ url_for('static', filename='mychart.svg')}}"></iframe>
# </div>

# embed:
# <figure class="chart-container">
#   <embed class="js-chart-container" type="image/svg+xml"
#    src="{{ url_for('static', filename='mychart.svg')}}">
# </figure>

# object:
# <figure class="chart-container">
#   <object class="js-chart-container" type="image/svg+xml"
#    data="{{ url_for('static', filename='mychart.svg')}}"></object>
# </figure>

# The method that I'm going to be using going forward is the <object> method
# for two main reasons:

# 1. The object element (like embed and unlike iframe) is less fussy in terms
#    of having to apply a bunch of css to make the content fill the frame.

# 2. The object element uses the HTMLObjectElement DOM interface which (like
#    iframe and unlike embed) has a contentDocument and contentWindow property
#    which allow you to apply the location.reload() method. This method is
#    helpful for when you need the svg to refresh when the HTML page loads
#    instead of displaying a cached version. For example:

# document.querySelector('.js-chart-container').contentDocument.location.reload();
# document.querySelector('.js-chart-container').contentWindow.location.reload();
