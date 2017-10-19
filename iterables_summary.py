'''Review of Lists, Tuples, Dictionaries & Sets'''

# Compare data structures:

# List: mutable, ordered, repeats ok
colours_list = ['red', 'orange', 'black', 'black']
# Tuple: immutable, ordered, repeats ok
colours_tuple = ('red', 'orange', 'black', 'black')
# Dict: keys – immutable, unordered, no repeats
#       values – mutable, unordered, repeats ok
colours_dict = {'red' : 'Pantone 185C',
                'orange' : 'Pantone 021C',
                'black' : 'Pantone 6C'}
# Sets: mutable, unordered, no repeats
colours_set = {'red', 'orange', 'black'}

print(type(colours_list))   # <class 'list'>
print(type(colours_tuple))  # <class 'tuple'>
print(type(colours_dict))   # <class 'dict'>
print(type(colours_set))    # <class 'set'>

# in each case use [] brackets to access a single element
# (except sets which don't support indexing):

print(colours_list[2])        # black
print(colours_tuple[2])       # black
print(colours_dict['black'])  # Pantone 6C

# You can combine data structures, for example, you can make:
#  - a tuple of lists
#  - a list of lists
#  - a dictionary of lists (only the values van be lists)

colors = ['magenta', 'red', 'cyan']
moods = ['happy', 'sad', 'confused']
senses = ['smell', 'touch', 'taste']

dict_of_lists = {'Colors' : colors,
                 'Moods' : moods,
                 'Senses' : senses,}

# Reminder: Dictionary keys are immutable, therefor you cannot use a list
# or another dictionary as a key, but you CAN use a tuple because tuples
# are immutable too. A good example of this is with mapping – the GPS
# coordinates may be the key:

places = {(44, -93, 344) : 'home',
          (27, -80, 200) : 'work',}

# NOTE: Frozen sets can also be used as dict keys
