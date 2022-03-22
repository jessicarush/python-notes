'''A brief look at NumPy (Numerical Python).'''


# http://www.numpy.org/

# NumPy is a library for Python that adds support for "large, multi-dimensional
# arrays and matrices, along with a large collection of high-level mathematical
# functions to operate on these arrays."

# numpy arrays look similar to python lists but they are much more efficient,
# especially when it comes to iterating over them, running other functions.

# numpy is a base library for many other libraries such as pandas, matplotlib,
# and OpenCV (image processing library).

import numpy


# One Dimensional Arrays
# -----------------------------------------------------------------------------
n = numpy.arange(27)

print(n)        # [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 ...]
print(type(n))  # <class 'numpy.ndarray'>

n_start_stop_step = numpy.arange(0, 100, 10)
print(n_start_stop_step)  # [ 0 10 20 30 40 50 60 70 80 90]


# Two Dimensional Arrays
# -----------------------------------------------------------------------------
n = n.reshape(3, 9)

print(n)
# [[ 0  1  2  3  4  5  6  7  8]
#  [ 9 10 11 12 13 14 15 16 17]
#  [18 19 20 21 22 23 24 25 26]]

# This is how image files can be stored... each row is a row of pixels.


# Three Dimensional Arrays
# -----------------------------------------------------------------------------
n = n.reshape(3, 3, 3)

print(n)
# [[[ 0  1  2]
#   [ 3  4  5]
#   [ 6  7  8]]
#
#  [[ 9 10 11]
#   [12 13 14]
#   [15 16 17]]
#
#  [[18 19 20]
#   [21 22 23]
#   [24 25 26]]]


# Create numpy arrays from Python lists
# -----------------------------------------------------------------------------

a = [12, 45, 255]
b = [34, 45, 101]
c = [122, 60, 10]

n = numpy.asarray([a, b, c])

print(type(n))  # <class 'numpy.ndarray'>
print(n)
# [[ 12  45 255]
#  [ 34  45 101]
#  [122  60  10]]


# Indexing, slicing, iterating arrays
# -----------------------------------------------------------------------------
print(n.shape)
# (3, 3)

n_slice = n[1:3, 1:3]
print(n_slice)
# [[ 45 101]
#  [ 60  10]]

single_value = n[1, 2]
print(single_value)
# 101

# iterate through an array:
for i in n:
    print(i)
# [ 12  45 255]
# [ 34  45 101]
# [122  60  10]

# iterate through columns instead for rows by using the transpose method:
for i in n.T:
    print(i)
# [ 12  34 122]
# [45 45 60]
# [255 101  10]

# iterate through each value by using the flat method:
for i in n.flat:
    print(i, end=', ')
print('')
# 12, 45, 255, 34, 45, 101, 122, 60, 10,


# Stacking and splitting arrays
# -----------------------------------------------------------------------------
stacked_array = numpy.hstack((n, n))
print(stacked_array)
# [[ 12  45 255  12  45 255]
#  [ 34  45 101  34  45 101]
#  [122  60  10 122  60  10]]

stacked_array = numpy.vstack((n, n))
print(stacked_array)
# [[ 12  45 255]
#  [ 34  45 101]
#  [122  60  10]
#  [ 12  45 255]
#  [ 34  45 101]
#  [122  60  10]]

# Note you can stack together (concatenate) as many arrays as you want
# (provided they have the same dimensions):

stacked_array = numpy.hstack((n, n, n.T, n.T))
print(stacked_array)
# [[ 12  45 255  12  45 255  12  34 122  12  34 122]
#  [ 34  45 101  34  45 101  45  45  60  45  45  60]
#  [122  60  10 122  60  10 255 101  10 255 101  10]]

split_array = numpy.hsplit(stacked_array, 2)
for i in split_array:
    print(i)
# [[ 12  45 255  12  45 255]
#  [ 34  45 101  34  45 101]
#  [122  60  10 122  60  10]]
# [[ 12  34 122  12  34 122]
#  [ 45  45  60  45  45  60]
#  [255 101  10 255 101  10]]

split_array = numpy.vsplit(stacked_array, 3)
for i in split_array:
    print(i)
# [[ 12  45 255  12  45 255  12  34 122  12  34 122]]
# [[ 34  45 101  34  45 101  45  45  60  45  45  60]]
# [[122  60  10 122  60  10 255 101  10 255 101  10]]
