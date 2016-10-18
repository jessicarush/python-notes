# Handle errors with try and except

shortlist = [1, 2, 3]
position = 5

try:
    shortlist[position]
except:
    print('Need a position between 0 and ', len(shortlist)-1)


# Handle different types of exceptions using Pyhton standard exception names:

newshortlist = [1, 2, 3]

while True:
    value = input('Position [q to quit]: ')
    if value == 'q':
        break
    try:
        position = int(value)
        print(newshortlist[position])
    except IndexError as err:
        print('Bad index:', position)
    except Exception as other:
        print('Something else broke:', other)

# Make your own exceptions. An exception is a class, It's a child of the base class Exception

class UppercaseException(Exception):
    pass

words = ['one', 'two', 'THREE', 'four']

for word in words:
    if word.isupper():
        raise UppercaseException(word)
