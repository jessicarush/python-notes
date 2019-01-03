'''Demo: Helper functions can be more readable than complex expressions.'''


# Consider we're receiving some rgba values from a query string of a url.
# The output we want is an integer for each r, g, b, and a. Let's say if the
# values are missing, we want them to be 0.

# Let's first see what type of data we get:

from urllib.parse import parse_qs

values = parse_qs('red=52&blue=0&green=', keep_blank_values=True)

print(values)
print(type(values))
# {'red': ['52'], 'blue': ['0'], 'green': ['']}
# <class 'dict'>

# The get method will allow us to check for values even if they don't exist:

red = values.get('red')
green = values.get('green')
blue = values.get('blue')
opacity = values.get('opacity')

print('red:', red)
print('green:', green)
print('blue:', blue)
print('opacity:', opacity)
# red: ['52']
# green: ['']
# blue: ['0']
# opacity: None

# So, if I just want the number, I would have to specfify the first item in the
# list[0]. And if the list is empty I'd have to say 'or 0'. And if the value
# didn't exist at all (None), then I'd have to pass an optional value to the
# get method (an empty list):

red = values.get('red', [''])[0] or 0
green = values.get('green', [''])[0] or 0
blue = values.get('blue', [''])[0] or 0
opacity = values.get('opacity', [''])[0] or 0

print('red:', red)
print('green:', green)
print('blue:', blue)
print('opacity:', opacity)
# red: 52
# green: 0
# blue: 0
# opacity: 0

# But I also have to make sure the values are integers:

red = int(values.get('red', [''])[0] or 0)
green = int(values.get('green', [''])[0] or 0)
blue = int(values.get('blue', [''])[0] or 0)
opacity = int(values.get('opacity', [''])[0] or 0)

# Now these expressions have become unreadable and repetitive.
# Here's where a helper function would be useful:

def get_value(values, key, default=0):
    result = values.get(key, [''])
    if result[0]:
        result = int(result[0])
    else:
        result = default
    return result

red = get_value(values, 'red')
green = get_value(values, 'green')
blue = get_value(values, 'blue')
opacity = get_value(values, 'opacity')

# Though it means more lines of code, in the end its more readable.
