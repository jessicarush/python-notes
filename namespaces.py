'''Namespaces'''


# Local and global variables
# -----------------------------------------------------------------------------
# You can get the value of a global variable from within a function

animal = 'fruitbat'

def print_global():
    print('inside print_global:', animal)

print_global()
# inside print_global: fruitbat

# But if you get the value of a global variable and and try to change it within
# a function, you get an error because as soon as you start assigning to a
# variable, python wants to make it a local variable, and since no local
# variable has been initialized... error:

def change_and_print_global():
    print('inside change_and_print_global:', animal)
    animal = 'wombat'
    print('after the change:', animal)

# change_and_print_global()
# UnboundLocalError: local variable 'animal' referenced before assignment

# So, if you reassign the variable you are actually making a new local variable
# (also named animal) inside of the function. Use ID to see they're different:

def change_local():
    animal = 'wombat'
    print('local animal:', animal, id(animal))

change_local()
print('global animal:', animal, id(animal))

# local animal: wombat 4316476056
# global animal: fruitbat 4316756144

# To access and change a global variable from within a function you need to be
# explicit by using the global keyword:

def change_and_print_global():
    global animal
    print('inside change_and_print_global:', animal)
    animal = 'wombat'
    print('after the change:', animal)

change_and_print_global()
# inside change_and_print_global: fruitbat
# after the change: wombat


# nonlocal
# -----------------------------------------------------------------------------
# Python 3 introduced the nonlocal keyword that allows you to assign to
# variables in an outer, but non-global, scope.
x = 'orange'
def testing_nonlocal():
    x = 'lemon'
    def inside():
        nonlocal x  # if this statement is removed, the printed output
        x = 'lime'  # would be 'lime', then 'lemon' because we actually
        print(x)    # would have 3 unique 'x' variables.
    inside()
    print(x)

print(x)
# orange
testing_nonlocal()
# lime
# lime

# NOTE: when you reference a variable name, python will start by looking for
# the variable definition locally, and then move outward until if finds it.
# The order of scopes is as follows:

# – local
# – enclosing
# – global
# – built-ins


# locals() and globals()
# -----------------------------------------------------------------------------
# Python provides two functions to access the contents of your Namespaces
# locals() and globals():

fruit = 'orange'

def testing_local():
    fruit = 'apple'
    print('locals:', locals())

testing_local()
# locals: {'fruit': 'apple'}

print('globals:')
g = sorted(globals())
for x in g:
    print(x)
# globals:
# __annotations__
# __builtins__
# __cached__
# __doc__
# __file__
# __loader__
# __name__
# __package__
# __spec__
# animal
# change_and_print_global
# change_local
# fruit
# print_global
# testing_local
# testing_nonlocal
# x


# __name__, __doc__
# -----------------------------------------------------------------------------
# The name of a function is in the system variable: function.__name__
# The functions document string in in the variable: function.__doc__

def amazing():
    '''This is the functions description'''
    print('This function is named:', amazing.__name__)
    print('Its docstring says:', amazing.__doc__)
    print('The main program running is assigned a special name:', __name__)

amazing()
