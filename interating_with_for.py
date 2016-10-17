# Iterating with FOR

# Iterating over lists, tuples and sets returns items.
list1 = ['one' , 'two', 'three']
tuple1 = ('four', 'five', 'six')
set1 = {'seven', 'eight', 'nine'}

for item in list1:
    print(item)

for item in tuple1:
    print(item)

for item in set1:
    print(item)

# Iterating over strings returns characters.
string1 = "ten"

for char in string1:
    print(char)

# Iterating over dictionaies returns keys.
dict1 = {'eleven' : '11', 'twelve': '12', 'thirteen': '13'}

for item in dict1: # will choose keys
    print(item)

# same as:
for item in dict1.keys():
    print(item)

# Therefor, to iterate over a dictionary and get values:
for item in dict1.values():
    print(item)

# To iterate over both keys and values:
for item in dict1.items():
    print(item)

# Break apart the resulting tuple by doing this:
for key, value in dict1.items():
    print(key, 'is', value)

# testing break:
cheeses = []
for cheese in cheeses:
    print('This shop has', cheese)
    break
else:
    print('no cheese')

# Iterating over multiple sequences with zip()
days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['Apple', 'Banana', 'Pear']
drinks = ['Tea', 'Juice', 'Wine']
desserts = ['Ice cream', 'Cookies', 'Cake', 'Candy']

for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day, ': eat', fruit, ', drink', drink, ', cheat with', dessert)

# for using range(start, stop, step)

for x in range(5, -1, -1):
    print(x, end='...')

evennumberlist = list(range(0, 20, 2))
print(evennumberlist)
