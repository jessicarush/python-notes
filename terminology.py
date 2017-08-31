'''Misc Terms''''

# Literal --------------------------------------------------------------------

# a literal lets you assign values of an object in a single assignment,
# for example:

# assign a string literal to message
message = "some information"

# assign an int literal to x
x = 100

# assign a dictionary literal to plants
plants = {'spider': 'long, slender leaves',
          'succulent': 'like a cactus',
          'fern': 'perfers the forest'}

# None -----------------------------------------------------------------------

# None is not the same as False. Though it may look false when evaluated as a
# boolean, None is technically none as seen here:

thing = None

def is_none(thing):
    if thing is None:
        print("it's none")
    elif thing:
        print("it's True")
    else:
        print("it must be False")

is_none(thing)

# Keyword arguments: **name --------------------------------------------------

# The keyword argument **h extracts the keys and values from the dictionary
# and supplies them as arguments to the class Element()

class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

h = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}

hydrogen = Element(**h)

print(hydrogen.symbol)
