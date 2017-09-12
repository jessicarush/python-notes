'''Packages: organize modules into file hierarchies'''

# Module 1: sources/daily.py

def forecast():
    '''Daily forecast'''
    return 'Like yesterday'

# Module 2: sources/weekly.py

def forecast():
    '''Weekly forecast'''
    return['snow', 'clear', 'sleet', 'rain', 'freezing rain', 'fog', 'hail']

# Main program: weather.py

from sources import daily, weekly

print('daily forecast:', daily.forecast())
print('weekly forecast:')

for number, outlook in enumerate(weekly.forecast(), 1):
    print(number, outlook)

# The enumerate function above takes apart a list and feeds each item to the for
# loop, adding a number to each item as a bonus.

# __init__.py -----------------------------------------------------------------

# In the sources directory you'll need to create a file named __init__.py
# This file can be empty. Python needs it to treat the directory containing
# it as a package.
