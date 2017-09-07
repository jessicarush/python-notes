# Namespaces

# Local and global variable names.

# You can get the value of a global variable from within a function

animal = 'fruitbat'

def print_global():
    print('inside print_global:', animal)

print_global()

# But if you get the value of a global variable and and try to change it within
# a function, you get an error because as soon as you start assigning to a
# variable, python wants to make it a local variable, amd since no local
# variable has been initialized... error:
"""
def change_and_print_global():
    print('inside change_and_print_global:', animal)
    animal = 'wombat'
    print('after the change:', animal)
"""

# So, if you reassign the variable you are actually making a new local variable
# (also named animal) inside of the function. Use ID to see they're different:

def change_local():
    animal = 'wombat'
    print('local animal:', animal, id(animal))

change_local()
print('global animal:', animal, id(animal))

# To access and change a global variable from within a function you need to be
# explicit by using the global keyword:

def change_and_print_global():
    global animal
    print('inside change_and_print_global:', animal)
    animal = 'wombat'
    print('after the change:', animal)

change_and_print_global()

# Python provides two functions to access the contents of your Namespaces
# locals() and globals():

fruit = 'orange'

def testing_local():
    fruit = 'apple'
    print('locals:', locals())

testing_local()
print('globals:', globals())

# The name of a function is in the system variable: function.__name__
# The functions document string in in the variable: function.__doc__

def amazing():
    '''This is the functions description'''
    print('Ths function is named:', amazing.__name__)
    print('And its docstring says:', amazing.__doc__)

amazing()

# FYI the main program itself is assigned the special variable name __main__
