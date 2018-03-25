'''Matplotlib – Random Walk'''

# A random walk is a path that has no clear direction but is determined by a
# series of random decisions. For example, a grain of pollen floating on a drop
# of water moves across the surface in a random walk. It is pushed around by
# water molecules and molecular motion in a water drop happens to be random.


# Ideally the following class would be saved as a module: random_walk.py
# -----------------------------------------------------------------------------

from random import choice

class RandomWalk():
    '''A class to generate random walks.'''

    def __init__(self, num_points=5000):
        '''Initialize attributes of walk.'''
        self.num_points = num_points

        # all walks start at (0,0):
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        '''Calculate all the points in the walk.'''
        # keep tracking the steps until the walk reaches the desired length:
        while len(self.x_values) < self.num_points:
            # decide on which direction to go and how far to go:
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance
            # reject moves that go nowhere:
            if x_step == 0 and y_step == 0:
                continue
            # calculate the next x and y values:
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)


# Ideally the following would be in it's own file and we'd import the class
# -----------------------------------------------------------------------------

import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
# from random_walk import RandomWalk

# colours:
a = '#69F4BD'
b = '#319589'
c = '#344D6c'
d = '#372560'
e = '#3E1B3C'

rw1 = RandomWalk(50000)
rw1.fill_walk()

# optional setting the window size:
plt.figure(figsize=(9, 5))

# make your own colour map:
cmap = LinearSegmentedColormap.from_list('mycmap', [a, b, c, d, e])

# create a list for the range needed for the colour map:
point_numbers = list(range(rw1.num_points))

# the main plot:
plt.scatter(rw1.x_values, rw1.y_values, s=1, c=point_numbers, cmap=cmap)

# emphasize the start and end points:
plt.scatter(0, 0, c='gold', s=25)
plt.scatter(rw1.x_values[-1], rw1.y_values[-1], c='red', s=25)

# title and axis size:
plt.title('Random Walk', fontsize=9)
plt.tick_params(axis='both', which='major', labelsize=7)

plt.show()
