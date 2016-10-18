# Namespaces (local and global variable names)

# You can get the value of a global variable from within a function

animal = 'fruitbat'

def print_global():
    print('inside print_global:', animal)

print_global()

# But if you get the value of a global variable and and try to change it within a function, 
# you get an error:
"""
def change_and_print_global():
    print('inside change_and_print_global:', animal)
    animal = 'wombat'
    print('after the change:', animal)
"""

# If you change the variable you are actually changing a differnt variable (also named animal) 
# inside of the function. Use ID to see they are diferent:

def change_local():
    animal = 'wombat'
    print('inside change_local:', animal, id(animal))

change_local()
print('global animal:', animal, id(animal))

# To access and change a global variable from within a function you need to be explicit 
# by using the global keyword:

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
