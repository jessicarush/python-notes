'''Packages: organize modules into file hierarchies'''


# Module 1: sources/daily.py
# -----------------------------------------------------------------------------

def forecast():
    '''Daily forecast'''
    return 'Like yesterday'


# Module 2: sources/weekly.py
# -----------------------------------------------------------------------------

def forecast():
    '''Weekly forecast'''
    return['snow', 'clear', 'sleet', 'rain', 'freezing rain', 'fog', 'hail']


# __init__.py
# -----------------------------------------------------------------------------

# In the sources directory you'll need to create a file named __init__.py
# This file can be empty. Python needs it to treat the directory containing
# it as a package.

# Note that this __init__.py file runs as soon as you import anything from the
# package. It can be used to set some shared variables or execute some
# "initialization" code. That being said, programmers do not expect actual
# logic to happen in this file so keep it at that.


# Main program: weather.py
# -----------------------------------------------------------------------------

from sources import daily, weekly

print('daily forecast:', daily.forecast())
print('weekly forecast:')

for number, outlook in enumerate(weekly.forecast(), 1):
    print(number, outlook)

# The enumerate function above takes apart a list and feeds each item to the
# for loop, adding a number to each item starting from 1.


# Importing specific function/classes
# -----------------------------------------------------------------------------

# If you wanted to import a function or class from a file that's within
# a directory like this you'd say:

from sources.daily import myfunction
