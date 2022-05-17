'''Match Statements'''


# New to Python 3.10, structural pattern matching has been added in the form of
# a match statement and case statements of patterns with associated actions. It
# seems similar to JavaScript switch statements but better.

# https://peps.python.org/pep-0634/
# https://peps.python.org/pep-0636/

# Patterns consist of sequences, mappings, primitive data types as well as class
# instances. Pattern matching enables programs to extract information from
# complex data types, branch on the structure of data, and apply specific
# actions based on different forms of data.

subject = 'b'
result = None

match subject:
    case 'a':
        result = 'one'
    case 'b':
        result = 'two'
    case 'c':
        result = 'three'
    case _:
        result = 'wildcard'

print(result)  # two

# A match statement takes an expression and compares its value to successive
# patterns given as one or more case blocks. Specifically, pattern matching
# operates by:

# - using data with type and shape (the subject)
# - evaluating the subject in the match statement
# - comparing the subject with each pattern in a case statement from top to
#   bottom until a match is confirmed.
# - executing the action associated with the pattern of the confirmed match
# - If an exact match is not confirmed, the last case, a wildcard _, if provided,
#   will be used as the matching case. If an exact match is not confirmed and a
#   wildcard case does not exist, the entire match block is a no-op.


# Match to a literal
# -----------------------------------------------------------------------------

def http_status(code):
    match code:
        case 200:
            return 'ok'
        case 400:
            return 'bad request'
        case 401 | 403 | 405:
            return 'not allowed'
        case 404:
            return 'not found'
        case _:
            return 'something else broke'

print(http_status(500))  # something else broke


# Patterns with a variable
# ----------------------------------------------------------------------------

def show_point(point):
    match point:
        case (0, 0):
            print('origin')
        case (x, 0):
            print(f'x={x}')
        case (0, y):
            print(f'y={y}')
        case (x, y):
            print(f'x={x}, y={y}')
        case _:
            raise ValueError('Not a point')

show_point((15, 4))  # x=15, y=4
show_point((0, 5))   # y=5


# Patterns with classes
# ----------------------------------------------------------------------------

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def location(point):
    match point:
        case Point(x=0, y=0):
            print('origin')
        case Point(x=x, y=y):
            print(f'x={x}, y={y}')
        case _:
            raise ValueError('Not a point')


location(Point(x=0, y=0))    # origin
location(Point(x=12, y=66))  # x=12, y=66


# Add an if clause as a 'guard'
# ----------------------------------------------------------------------------

def location(point):
    match point:
        case Point(x=0, y=0):
            print('origin')
        case Point(x=x, y=y) if x == y:
            print(f'the point is on the diagonal: x={x}, y={y}')
        case Point(x=x, y=y):
            print(f'x={x}, y={y}')
        case _:
            raise ValueError('Not a point')


location(Point(x=12, y=12))  # the point is on the diagonal: x=12, y=12


# Complex patterns and the wildcard
# ----------------------------------------------------------------------------
# The _ wildcard can be used for items within a pattern, for example:

message = ('error', 100, ['foo'])

match message:
    case ('warning', code, 50):
        print('a warning has been received')
    case ('error', code, _):
        print(f'an error {code} has occurred')

# an error 100 has occurred

