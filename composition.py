# Composition
# Inheritance is a good technique (child is-a parent) but it can be tempting to build elaborate
# inheritance hierarchies. Sometimes composition or aggregation (x has-a y) makes more sense.

class Floor():
    def __init__(self, kind):
        self.kind = kind

class Windows():
    def __init__(self, quantity):
        self.quantity = quantity

class Room():
    def __init__(self, floor, windows):
        self.floor = floor
        self.windows = windows
    def about(self):
        print('This room has a', floor.kind, 'floor and', windows.quantity, 'windows')

floor = Floor('hardwood')
windows = Windows('4')
kitchen = Room(floor, windows)
kitchen.about()
