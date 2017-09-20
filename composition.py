'''Composition'''

# Inheritance is a good technique (child is-a parent) but it can be tempting
# to build elaborate inheritance hierarchies. Sometimes composition or
# aggregation (x has-a y) makes more sense.

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


# In the example passing a Floor and a Window object as arguments to a Room
# object. The composition could also be embedded in the Room class itself:


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
