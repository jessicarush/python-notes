# Special (Magic) Methods
# Names of these methods begin with __. An example is __init__ which initializes
# a newly created object from its class and any arguments that were passed in.
# Example: create a method that compares two words but is case insensitive.

class Word():
    def __init__(self, text):
        self.text = text
    def equals(self, word2):
        return self.text.lower() == word2.text.lower()

# testing:

first = Word('ha')
second = Word('HA')
third = Word('nope')

print(first.equals(second))
print(first.equals(third))

# __eq__
# The above works but there's an tidier way using Magic Methods:

class Word():
    def __init__(self, text):
        self.text = text
    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()

first = Word('ha')
second = Word('HA')
third = Word('nope')

print(first == second)
print(first == third)

# Magic Methods for comparison:

def __eq__(self, other):        # self == other
    pass
def __ne__(self, other):        # self != other
    pass
def __lt__(self, other):        # self < other
    pass
def __gt__(self, other):        # self > other
    pass
def __le__(self, other):        # self <= other
    pass
def __ge__(self, other):        # self >= other
    pass

# Magic Methods for math:

def __add__(self, other):       # self + other
    pass
def __sub__(self, other):       # self - other
    pass
def __mul__(self, other):       # self * other
    pass
def __floordiv__(self, other):  # self // other
    pass
def __truediv__(self, other):   # self / other
    pass
def __mod__(self, other):       # self % other
    pass
def __pow__(self, other):       # self ** other
    pass

# Other common Magic Methods:

def __str__(self):
    pass
def __repr__(self):
    pass
def __len__(self):
    pass

# testing:

print(first)    # returns <__main__.Word object at 0x1010d9fd0>

# Add __str__ and __repr__ to clean up the output:

class Word():
    def __init__(self, text):
        self.text = text
    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()
    def __str__(self):
        return self.text
    def __repr__(self):
        return 'Word("' + self.text + '")'

first = Word('ha')
print(first)    # returns ha

# Another magic method is __dict__. It's used to return the dictionary used to
# store an object’s attributes

print(first.__dict__)
