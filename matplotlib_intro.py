'''Matplotlib - Mathematical Plotting Library'''

# $ pip3 install matplotlib
# http://matplotlib.org
# https://matplotlib.org/examples/index.html
# https://matplotlib.org/users/pyplot_tutorial.html

# -----------------------------------------------------------------------------
# plt.plot()
# -----------------------------------------------------------------------------

import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25, 36, 49, 64, 81]

# you can set style parameters like this:
plt.plot(squares, color='#FB4847', linewidth=1.5, antialiased=True)

# or like this:
lines = plt.plot(squares)
plt.setp(lines, color='#D3F382', linewidth=4.5, antialiased=False,
    solid_capstyle='round')

# set the title and label axes:
plt.title('Square Numbers', fontsize=14)
plt.xlabel('value', fontsize=10)
plt.ylabel('square of value', fontsize=10)

# set size of tick labels:
plt.tick_params(axis='both', labelsize=8)

# display the chart:
plt.show()

# By default it assumes the first data point corresponds to an x-coordinate of
# 0 but if it doesn't, you can always provide the input_values:

squares = [1, 4, 9, 16, 25, 36, 49, 64, 81]
x_vals = [1, 2, 3, 4, 5, 6, 7, 8, 9]

plt.plot(x_vals, squares, color='#FB4847')
plt.title('Specify x values', fontsize=14)
plt.show()

# -----------------------------------------------------------------------------
# plt.scatter()
# -----------------------------------------------------------------------------

# to plot single points use the scatter function:
plt.scatter(2, 4, s=200)

# plot many points:
x_vals = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y_vals = [1, 4, 9, 16, 25, 36, 49, 64, 81]
plt.scatter(x_vals, y_vals, s=80)

# format the plot:
plt.title('Scatter Function', fontsize=14)
plt.xlabel('value', fontsize=10)
plt.ylabel('square of value', fontsize=10)
plt.tick_params(axis='both', which='major', labelsize=8)

# display the plot:
plt.show()

# use a loop to generate points:
x_vals = list(range(1, 1001))
y_vals = [(x ** 2) for x in x_vals]
plt.scatter(x_vals, y_vals, s=40, c=(0.016, 0.859, 0.643))

# format the plot:
plt.title('Values from a Loop', fontsize=14)
plt.xlabel('value', fontsize=10)
plt.ylabel('square of value', fontsize=10)
plt.tick_params(axis='both', which='major', labelsize=8)

# set the range for each axis:
plt.axis([0, 1200, 0, 900000])

# display the plot:
plt.show()

# -----------------------------------------------------------------------------
# Short argument names
# -----------------------------------------------------------------------------
# Note that many of the keyword arg names can be specified in short form:
#    color or c
#    linewidth or lw
#    size or s
#    antialiased or aa
#    linestyle or ls
#    markeredgecolor or mec
#    markeredgewidth or mew
#    markerfacecolor or mfc
#    markersize or ms

# -----------------------------------------------------------------------------
# RGB color values
# -----------------------------------------------------------------------------
# matplotlibs RGB color values need to be input as a float between 0 and 1.
# for example, my favourite neon green (4, 219, 164) would translate to
# (0.016, 0.859, 0.643), rounded to 3 decimal places.

def rgb_convert(r, g, b):
    c = r/255, g/255, b/255
    return c

mint = rgb_convert(4, 219, 164)
coral = rgb_convert(255, 110, 103)
yella = rgb_convert(255, 204, 0)

# -----------------------------------------------------------------------------
# Colormaps
# -----------------------------------------------------------------------------
# https://matplotlib.org/examples/color/colormaps_reference.html

# Color mapping is using a gradient of two or more colors to emphasize
# patterns in data.

x_vals = list(range(1, 1001))
y_vals = [(x ** 2) for x in x_vals]
plt.scatter(x_vals, y_vals, c=y_vals, cmap=plt.cm.plasma, s=40)

plt.title('Color Maps', fontsize=14)
plt.xlabel('value', fontsize=10)
plt.ylabel('square of value', fontsize=10)
plt.tick_params(axis='both', which='major', labelsize=8)
plt.axis([0, 1200, 0, 900000])

plt.show()

# There are a bunch of preset gradients at the link above. Apparently you can
# create your own, but it can get pretty complicated:

# https://matplotlib.org/examples/pylab_examples/custom_cmap.html
# http://schubert.atmos.colostate.edu/~cslocum/custom_cmap.html
# https://seaborn.pydata.org/tutorial/color_palettes.html

# the simplest method I found is:

from matplotlib.colors import LinearSegmentedColormap

cmap = LinearSegmentedColormap.from_list('mycmap', [yella, coral, mint])

x_vals = list(range(1, 1001))
y_vals = [(x ** 2) for x in x_vals]
plt.scatter(x_vals, y_vals, c=y_vals, cmap=cmap, s=40)

plt.title('Custom Color Maps', fontsize=14)
plt.xlabel('value', fontsize=10)
plt.ylabel('square of value', fontsize=10)
plt.tick_params(axis='both', which='major', labelsize=8)
plt.axis([0, 1100, 0, 1000000])

# plt.show()

# -----------------------------------------------------------------------------
# Save to a File
# -----------------------------------------------------------------------------
# If you want to automatically save to a file, replace plt.show() with a call
# to plt.savefig().

# https://matplotlib.org/api/_as_gen/matplotlib.pyplot.savefig.html

# savefig(fname, dpi=None, facecolor='w', edgecolor='w',
#         orientation='portrait', papertype=None, format=None,
#         transparent=False, bbox_inches=None, pad_inches=0.1,
#         frameon=None)

plt.savefig('sample_plot.png', dpi=300, bbox_inches='tight')

# -----------------------------------------------------------------------------
# Misc
# -----------------------------------------------------------------------------
# If you wanted to remove the axis ticks and labels:
# plt.axes().get_xaxis().set_visible(False)
# plt.axes().get_yaxis().set_visible(False)

# That being said, the lines above throw a deprecation warning. Instead you're
# meant to assign the plot to a variable then run the method on that:

fig = plt.scatter(x_vals, y_vals, c=y_vals, cmap=cmap, s=40)
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)

# The figure function controls width, height, resolution (also can be set in
# savefig), and background color. The figsize parameter takes a tuple which is
# in inches. The default dpi is 80. Experimenting with dpi on my Retina MacBook
# has led me to believe just leave this value at it's default. The only place
# where changing the dpi is useful, is when saving the figure as a png using
# savefig() as demonstrated above.

plt.figure(figsize=(9, 5))
