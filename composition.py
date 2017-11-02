'''Composition & Aggregation'''

# Inheritance is a good technique (child is-a parent) but it can be tempting
# to build elaborate inheritance hierarchies. Sometimes composition or
# aggregation (x has-a y) makes more sense. There is actually a difference
# between the composition and aggregation though they often blur together.

# -----------------------------------------------------------------------------
# Composition
# -----------------------------------------------------------------------------
# In this example, the Room class creates a Floor object and a Windows object.
# The arguments for these two objects are passed in when the Room is created.
# If the Room is deleted, so are the Floor and Window instances.

class Floor():
    def __init__(self, material):
        self.material = material

class Windows():
    def __init__(self, quantity):
        self.quantity = quantity

class Room():
    def __init__(self, floor, windows):
        self.floor = Floor(floor)
        self.windows = Windows(windows)
    def about(self):
        print('This room has', self.floor.material, 'floors and',
               self.windows.quantity, 'windows')

bathroom = Room('tiled', 0)
bathroom.about()  # This room has tiled floors and 0 windows

# -----------------------------------------------------------------------------
# Aggregation
# -----------------------------------------------------------------------------
# Unlike composition, aggregation uses existing instances of objects to build up
# another object. The composed object does not actually own the objects that
# it's composed of. If it's destroyed, those objects continue to exist.

# This example creates Floor and a Window objects, then passes them as arguments
# to a Room object. If the Room object is deleted, the other two objects remain.

class Floor():
    def __init__(self, material):
        self.material = material

class Windows():
    def __init__(self, quantity):
        self.quantity = quantity

class Room():
    def __init__(self, floor, windows):
        self.floor = floor
        self.windows = windows
    def about(self):
        print('This room has', floor.material, 'floors and',
               windows.quantity, 'windows')

floor = Floor('hardwood')
windows = Windows('4')
kitchen = Room(floor, windows)

kitchen.about()  # This room has hardwood floors and 4 windows
